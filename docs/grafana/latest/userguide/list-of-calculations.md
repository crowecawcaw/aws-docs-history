# Calculations list

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

This topic lists and defines the calculations used in Amazon Managed Grafana.

Among other places, these calculations are used in the **Transform**
tab and the bar gauge, gauge, and stat visualizations.

| Calculation      | Description                                              |
| ---------------- | -------------------------------------------------------- |
| All nulls        | True when all values are null                            |
| All zeros        | True when all values are 0                               |
| Change count     | Number of times the field’s value changes                |
| Count            | Number of values in a field                              |
| Delta            | Cumulative change in value                               |
| Difference       | Difference between first and last value of a field       |
| Distinct count   | Number of unique values in a field                       |
| First (not null) | First, not null value in a field                         |
| Max              | Maximum value of a field                                 |
| Mean             | Mean value of all values in a field                      |
| Min              | Minimum value of a field                                 |
| Min (above zero) | Minimum, positive value of a field                       |
| Range            | Difference between maximum and minimum values of a field |
| Step             | Minimal interval between values of a field               |
| Total            | Sum of all values in a field                             |
