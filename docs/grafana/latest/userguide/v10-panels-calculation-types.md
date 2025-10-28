# Calculation types

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The following table contains a list of calculations you can perform in Grafana. You can
find these calculations in the **Transform** tab and in the bar
gauge, gauge, and stat visualizations.

| Calculation        | Description                                               |
| ------------------ | --------------------------------------------------------- |
| All nulls          | True when all values are null                             |
| All values         | Array with all values                                     |
| All unique values  | Array with all unique values                              |
| All zeros          | True when all values are 0                                |
| Change count       | Number of times the field’s value changes                 |
| Count              | Number of values in a field                               |
| Delta              | Cumulative change in value, only counts increments        |
| Difference         | Difference between first and last value of a field        |
| Difference percent | Percentage change between first and last value of a field |
| Distinct count     | Number of unique values in a field                        |
| First              | First value in a field                                    |
| First\* (not null) | First, not null value in a field (also excludes NaNs)     |
| Last               | Last value in a field                                     |
| Last\* (not null)  | Last, not null value in a field (also excludes NaNs)      |
| Max                | Maximum value of a field                                  |
| Mean               | Mean value of all values in a field                       |
| Variance           | Variance of all values in a field                         |
| StdDev             | Standard deviation of all values in a field               |
| Min                | Minimum value of a field                                  |
| Min (above zero)   | Minimum, positive value of a field                        |
| Range              | Difference between maximum and minimum values of a field  |
| Step               | Minimal interval between values of a field                |
| Total              | Sum of all values in a field                              |
