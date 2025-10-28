# Plotly panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The Plotly panel renders charts using
[Plotly](https://plotly.com/javascript/ "https://plotly.com/javascript/"), an open source
javascript graphing library.

The **Data**, **Layout** and
**Config** fields match the common parameters described in the
[Plotly
documentation](https://plotly.com/javascript/plotlyjs-function-reference/ "https://plotly.com/javascript/plotlyjs-function-reference/"). They must be in JSON format.

Data provided by the datasource can be transformed via a user-defined script before to
be injected in the Plotly chart. The script includes 2 arguments.

- `data` – Data returned by the data source.
- `variables` – An object that contains [Grafana variables](templates-and-variables.md "templates-and-variables.md") in the current
  dashboard (user variables and these few global variables: `__from`,
  `__to`, `__interval`, and
  `__interval_ms`).
  The script must return an object with one or more of the following properties:
  `data`, `layout`, `config` and `frames`.
  The following is an example.

```
let x  = data.series[0].fields[0].values.buffer
let y  = data.series[0].fields[1].values.buffer
let serie = {
    x : x,
    y : y,
    name : variables.project //where project is the name of a Grafana’s variable
}

return {
    data : [serie],
    config : {
    displayModeBar: false
    }
}
```

Object returned by the script and JSON provided in the _Data_, _Layout_ and _Config_ fields will be merged (deep merge).

If no script is provided, the panel will use only _Data_, _Layout_ and _Config_ fields.
