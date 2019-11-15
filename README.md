Grafana dashboards
==================

This repository contains the dashboards deployed on the Grafana
instance used by the [Tor Project][] to monitor internal
infrastructure. It is part of a project to replace a dead Munin
deployment with Prometheus and Grafana.

Many of the dashboards here are copies of dashboards already available
in the [grafana.com dashboard database][] but some have been modified
to fix bugs or adapt to our infrastructure. They are, however,
generally designed to be used anywhere and respect the ad-hoc
standards of dashboard design. They should also work with the latest
version of Prometheus and associated exporters.

[grafana.com dashboard database]: https://grafana.com/dashboards/
[Tor Project]: https://torproject.org/

The point of this repository is to allow collaboration and welcome
improvements so that the multiplication of dashboards on grafana.com
stops somehow.

Available dashboards
--------------------

| Dashboard                        | Status     | Changes                                            |
| ---------                        | ------     | ----                                               |
| [Apache][]                       | unchannged |                                                    |
| [Bind][]                         | modified   | portability, legend, rate, other fixes             |
| Cache Health                     | new        | |
| [Grafana][]                      | unchanged  |                                                    |
| [Node exporter][]                | unchanged  |                                                    |
| [Node exporter server metrics][] | unchanged  |                                                    |
| [Postfix][]                      | new        | mostly new, based on a [custom dashboard][]        |
| [Postgres][]                     | modified   | buffers formulas, qps graphsize, min/max for cache |
| [Prometheus 2.0 overview][]      | modified   | modified to add disk usage and metrics scrape time |
| [Smartmon textfile][]            | unchanged  |                                                    |

 [Apache]: https://grafana.com/dashboards/3894/
 [Bind]: https://grafana.com/dashboards/10024/
 [Grafana]: https://grafana.com/dashboards/3590/
 [Node exporter]: https://grafana.com/dashboards/1860/
 [Node exporter server metrics]: https://grafana.com/dashboards/405/
 [Postfix]: https://grafana.com/dashboards/10013/
 [Postgres]: https://grafana.com/dashboards/455
 [Smartmon textfile]: https://grafana.com/dashboards/3992/
 [Prometheus 2.0 overview]: https://grafana.com/dashboards/3662/
[custom dashboard]: https://github.com/kumina/postfix_exporter/issues/21

Updating dashboards
-------------------

Dashboards in this repository can be refreshed from a running Grafana
instance by:

 1. clicking the "arrow" button (`Share dashboard`) on top
 2. choosing the `Export` tab
 3. setting the `Export for sharing externally` radio button
 4. hitting then `Save to file` button

Then run the following command on the file to make it usable internally:

    sed -i 's/${DS_[A-Z]*}/Prometheus/' FILENAME.json

Then committed into git and pushed to this repository. Pull requests
and issues are welcome.

That is for "modified" or "new" dashboards above. For "unchanged"
dashboards, they can be refreshed from the grafana.com database using
the `refresh.py` script.

This repository should be available at:

<https://gitlab.com/anarcat/grafana-dashboards>

But might be mirrored or forked elsewhere as well.
