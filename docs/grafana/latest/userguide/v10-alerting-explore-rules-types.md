# Alert rule types

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Grafana supports several alert rule types. Learn more about each of the alert
rule types, how they work, and decide which one is best for your use
case.

## Grafana managed

rules

Grafana managed rules are the most flexible alert rule type. They allow
you to create alerts that can act on data from any of your existing data
sources.

In addition to supporting multiple data sources, you can add [expressions](v10-panels-query-xform-expressions.md "v10-panels-query-xform-expressions.md")
to transform your data and express alert conditions.

In Grafana managed alerting:

- Alert rules are created within Grafana, based on one or more data
  sources.
- Alert rules are evaluated by the alert rule evaluation engine
  from within Grafana.
- Alerts are delivered using the internal Grafana Alertmanager.

###### Note

You can also configure alerts to be delivered using an external
Alertmanager, or use both internal and external Alertmanagers. For more
information, see [Add an
external alertmanager](v10-alerting-setup-alertmanager.md "v10-alerting-setup-alertmanager.md").

## Data source

managed rules

To create data source managed alert rules you must have a compatible
Prometheus or Loki data source. You can check if your data source supports
rule creation via Grafana by testing the data source and observing if the
Ruler API is supported.

In data source managed alerting:

- Alert rules are created and stored within the data source
  itself.
- Alert rules can only be created based on Prometheus data.
- Alert rule evaluation and delivery is distributed across multiple
  nodes for high-availability and fault tolerance.

## Choose an alert

rule type

When choosing which alert rule type to use, consider the following
comparison between Grafana managed alert rules and data source managed
alert rules.

| Feature                                                                 | Grafana-managed alert rule                                                                                                   | Loki/Mimir-managed alert rule                                                                                                                           |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create alert rules based on data from any of our supported data sources | Yes                                                                                                                          | No: You can only create alert rules that are based on Prometheus data. The data source must have the Ruler API enabled.                                 |
| Mix and match data sources                                              | Yes                                                                                                                          | No                                                                                                                                                      |
| Includes support for recording rules                                    | No                                                                                                                           | Yes                                                                                                                                                     |
| Add expressions to transform your data and set alert conditions         | Yes                                                                                                                          | No                                                                                                                                                      |
| Use images in alert notifications                                       | Yes                                                                                                                          | No                                                                                                                                                      |
| Scaling                                                                 | More resource intensive, depend on the database, and are likely to suffer from transient errors. They only scale vertically. | Store alert rules within the data source itself and allow for “infinite” scaling. Generate and send alert notifications from the location of your data. |
| Alert rule evaluation and delivery                                      | Alert rule evaluation and delivery is done from within Grafana, using an external Alertmanager; or both.                     | Alert rule evaluation and alert delivery is distributed, meaning there is no single point of failure.                                                   |
