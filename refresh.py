#!/usr/bin/python3

'''Reimport upstream dashboards in our provisionning system.

This exists mostly because upstream Grafana cannot parse Dashboard
variables when provisionning:

https://github.com/grafana/grafana/issues/10786

Therefore we need to do pattern replacement ourselves. This also
serves as a canonical source of truth for where the dashboards come
from.


'''

import re

import requests


AUTO_DASHBOARD_MAP = {
    'apache.json': 'https://grafana.com/api/dashboards/3894/revisions/5/download',
    'bind.json': 'https://grafana.com/api/dashboards/10024/revisions/2/download',
    'grafana-internals.json': 'https://grafana.com/api/dashboards/3590/revisions/3/download',
    'node-exporter-full.json': 'https://grafana.com/api/dashboards/1860/revisions/13/download',
    'node-exporter-server-metrics.json': 'https://grafana.com/api/dashboards/405/revisions/8/download',
    'postfix.json': 'https://grafana.com/api/dashboards/10013/revisions/2/download',
    'smartmon-textfile.json': 'https://grafana.com/api/dashboards/3992/revisions/1/download',
}


MANUAL_DASHBOARD_MAP = {
    'postgresql.json': 'https://grafana.com/api/dashboards/455/revisions/2/download',
    'prometheus-2.0-overview.json': 'https://grafana.com/api/dashboards/3662/revisions/2/download',
}


def main():
    pattern = re.compile(rb'\${DS_[A-Z]+}')
    print("fetching dashboards...")
    for path, url in AUTO_DASHBOARD_MAP.items():
        print("%s -> %s" % (url, path))
        body = requests.get(url).content
        body = pattern.sub(b'Prometheus', body)
        with open(path, 'wb') as fp:
            fp.write(body)
    print("the following dashboards were modified locally:")
    for path, url in MANUAL_DASHBOARD_MAP.items():
        print("%s -> %s" % (url, path))
    print('''To update, see README.md''')


if __name__ == '__main__':
    main()
