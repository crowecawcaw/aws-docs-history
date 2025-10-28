# Scripted dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

###### Warning

This feature is deprecated and will be removed in a future release.

If you have many metric names that change (for example, new servers) in a defined
pattern, it can be time consuming to constantly create new dashboards.

With scripted dashboards, you can dynamically create your dashboards using
JavaScript. In the Grafana install folder, under `public/dashboards/`, there
is a file named `scripted.js`. This file contains an example of a
scripted dashboard. You can access it by using the URL:
`http://grafana_url/dashboard/script/scripted.js?rows=3&name=myName`

When you open `scripted.js`, you can see how it reads URL
parameters from the `ARGS` variable and then adds rows and panels.

## Example: scripted.js

```

var seriesName = 'argName';

if (!_.isUndefined(ARGS.name)) {
  seriesName = ARGS.name;
}

dashboard.panels.push({
  title: 'Events',
  type: 'graph',
  fill: 1,
  linewidth: 2,
  gridPos: {
    h: 10,
    w: 24,
    x: 0,
    y: 10,
  },
  targets: [
    {
      target: "randomWalk('" + seriesName + "')",
    },
    {
      target: "randomWalk('random walk2')",
    },
  ],
});

return dashboard;

```

## More examples

You can find more examples in the `public/dashboards/` directory of
your Grafana installation.
