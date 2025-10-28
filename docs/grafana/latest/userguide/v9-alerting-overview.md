# Overview

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The following gives you an overview of how Grafana Alerting works and
introduces you to some of the key concepts that work together and form the core of its
flexible and powerful alerting engine.

1. **Data source**

Connects to data to be used by alerting. This data is often
time-series data, for alerts, and shows the details of a system to be
monitored and analyzed. For more information, see [data sources](AMG-data-sources-builtin.md "AMG-data-sources-builtin.md"). 2. **Alert rules**

Set evaluation criteria that determines whether an alert instance will
fire. An alert rule consists of one or more queries and expressions to pull
data from the datasource, a condition describing what constitutes the need
for an alert, the frequency of evaluation, and optionally, the duration over
which the condition must be met for an alert to fire.

Grafana managed alerts support multi-dimensional alerting, which means
that each alert rule can create multiple alert instances. This is
exceptionally powerful if you are observing multiple series in a single
expression. 3. **Labels**

Match an alert rule and its instances to notification policies and
silences. They can also be used to group your alerts by severity. 4. **Notification policies**

Set where, when, and how the alerts get routed to notify your team when
the alert fires. Each notification policy
specifies a set of label matchers to indicate which alerts they are
responsible for. A notification policy has a contact point assigned to it
that consists of one or more notifiers. 5. **Contact points**

Define how your contacts are notified when an alert fires. We support a
multitude of ChatOps tools to ensure the alerts come to your team.

## Features

**One page for all alerts**

A single Grafana Alerting page consolidates both Grafana-managed alerts and alerts
that reside in your Prometheus-compatible data source in one single place.

**Multi-dimensional alerts**

Alert rules can create multiple individual alert instances per alert rule, known as
multi-dimensional alerts, giving you the power and flexibility to gain visibility into
your entire system with just a single alert.

**Routing alerts**

Route each alert instance to a specific contact point based on labels you define.
Notification policies are the set of rules for where, when, and how the alerts are
routed to contact points.

**Silencing alerts**

Silences allow you to stop receiving persistent notifications from one or more
alerting rules. You can also partially pause an alert based on certain criteria.
Silences have their own dedicated section for better organization and visibility, so
that you can scan your paused alert rules without cluttering the main alerting
view.

**Mute timings**

With mute timings, you can specify a time interval when you don’t want new
notifications to be generated or sent. You can also freeze alert notifications for
recurring periods of time, such as during a maintenance period.
