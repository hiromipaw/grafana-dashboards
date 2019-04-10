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
