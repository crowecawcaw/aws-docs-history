# Using magics in Amazon Neptune notebooks

The Neptune workbench provides a number of so-called _magic_
commands in the notebooks that save a great deal of time and effort. They fall into
two categories: _line magics_ and _cell magics_.

_Line magics_ are commands preceded by a single percent sign
(`%`). They only take line input, not input from the rest of the cell
body. Neptune workbench provides the following line magics:

- [%seed](#notebooks-line-magics-seed "#notebooks-line-magics-seed")
- [%load](#notebooks-line-magics-load "#notebooks-line-magics-load")
- [%load_ids](#notebooks-line-magics-load-ids "#notebooks-line-magics-load-ids")
- [%load_status](#notebooks-line-magics-load-status "#notebooks-line-magics-load-status")
- [%cancel_load](#notebooks-line-magics-cancel-load "#notebooks-line-magics-cancel-load")
- [%status](#notebooks-line-magics-status "#notebooks-line-magics-status")
- [%gremlin_status](#notebooks-line-magics-gremlin-status "#notebooks-line-magics-gremlin-status")
- [%opencypher_status, or %oc_status](#notebooks-line-magics-opencypher-status "#notebooks-line-magics-opencypher-status")
- [%stream_viewer](#notebooks-line-magics-stream-viewer "#notebooks-line-magics-stream-viewer")
- [%sparql_status](#notebooks-line-magics-sparql-status "#notebooks-line-magics-sparql-status")
- [%graph_notebook_config](#notebooks-line-magics-graph-notebook-config "#notebooks-line-magics-graph-notebook-config")
- [%graph_notebook_host](#notebooks-line-magics-graph-notebook-host "#notebooks-line-magics-graph-notebook-host")
- [%graph_notebook_version](#notebooks-line-magics-graph-notebook-version "#notebooks-line-magics-graph-notebook-version")
- [%graph_notebook_service](#notebooks-line-magics-graph-notebook-service "#notebooks-line-magics-graph-notebook-service")
- [%graph_notebook_vis_options](#notebooks-line-magics-graph-notebook-vis-options "#notebooks-line-magics-graph-notebook-vis-options")
- [%statistics](#notebooks-line-magics-statistics "#notebooks-line-magics-statistics")
- [%summary](#notebooks-line-magics-summary "#notebooks-line-magics-summary")
- [%reset_graph](#notebooks-line-magics-reset-graph "#notebooks-line-magics-reset-graph")
- [%get_graph](#notebooks-line-magics-get-graph "#notebooks-line-magics-get-graph")
  _Cell magics_ are preceded by two percent signs (`%%`) rather
  than one, and use the cell content as input, although they can also take line content as
  input. Neptune workbench provides the following cell magics:

- [%%sparql](#notebooks-cell-magics-sparql "#notebooks-cell-magics-sparql")
- [%%gremlin](#notebooks-cell-magics-gremlin "#notebooks-cell-magics-gremlin")
- [%%opencypher, or %%oc](#notebooks-cell-magics-opencypher "#notebooks-cell-magics-opencypher")
- [%%graph_notebook_config](#notebooks-cell-magics-graph-notebook-config "#notebooks-cell-magics-graph-notebook-config")
- [%%graph_notebook_vis_options](#notebooks-cell-magics-graph-notebook-vis-options "#notebooks-cell-magics-graph-notebook-vis-options")
  There are also two magics, a line magic and a cell magic, for working with
  [Neptune machine learning](machine-learning.md "machine-learning.md"):

- [%neptune_ml](#notebooks-line-magics-neptune_ml "#notebooks-line-magics-neptune_ml")
- [%%neptune_ml](#notebooks-cell-magics-neptune_ml "#notebooks-cell-magics-neptune_ml")

###### Note

When working with Neptune magics, you can generally get help text using a
`--help` or `-h` parameter. With a cell magic, the body cannot
be empty, so when getting help, put filler text, even a single character, in the
body. For example:

```
%%gremlin --help
  x
```

## Variable injection in cell or line magics

Variables defined in a notebook can be referenced inside any cell or line magics
in the notebook using the format: `${VAR_NAME}`.

For example, suppose you define these variables:

```
c = 'code'
my_edge_labels = '{"route":"dist"}'
```

Then, this Gremlin query in a cell magic:

```
%%gremlin -de $my_edge_labels
g.V().has('${c}','SAF').out('route').values('${c}')
```

Is equivalent to this:

```
%%gremlin -de {"route":"dist"}
g.V().has('code','SAF').out('route').values('code')
```

## Query arguments that work with all query languages

The following query arguments work with `%%gremlin`, `%%opencypher`,
and `%%sparql` magics in the Neptune workbench:

###### Common query arguments

- **`--store-to`**
  (or **`-s`**)   –  
  Specifies the name of a variable in which to store the query results.
- **`--silent`**   –  
  If present, no output is displayed after the query completes.
- **`--group-by`**
  (or **`-g`**)   –  
  Specifies the property used to group nodes (such as `code` or
  `T.region`). Vertices are colored based on their assigned group.
- **`--ignore-groups`**   –  
  If present, all grouping options are ignored.
- **`--display-property`**
  (or **`-d`**)   –  
  Specifies the property whose value should be displayed for each vertex.

The default value for each query language is as follows:

    + For Gremlin:   `T.label`.
    + For openCypher:   `~labels`.
    + For SPARQL:   `type`.

- **`--edge-display-property`**
  (or **`-t`**)   –  
  Specifies the property whose value should be displayed for each edge.

The default value for each query language is as follows:

    + For Gremlin:   `T.label`.
    + For openCypher:   `~labels`.
    + For SPARQL:   `type`.

- **`--tooltip-property`**
  (or **`-de`**)   –  
  Specifies a property whose value should be displayed as a tooltip for each
  node.

The default value for each query language is as follows:

    + For Gremlin:   `T.label`.
    + For openCypher:   `~labels`.
    + For SPARQL:   `type`.

- **`--edge-tooltip-property`**
  (or **`-te`**)   –  
  Specifies a property whose value should be displayed as a tooltip for each
  edge.

The default value for each query language is as follows:

    + For Gremlin:   `T.label`.
    + For openCypher:   `~labels`.
    + For SPARQL:   `type`.

- **`--label-max-length`**
  (or **`-l`**)   –  
  Specifies the maximum character length of any vertex label. Defaults to 10.
- **`--edge-label-max-length`**
  (or **`-le`**)   –  
  Specifies the maximum character length of any edge label. Defaults to 10.

In the case of openCypher only, this is `--rel-label-max-length`
or `-rel` instead.

- **`--simulation-duration`**
  (or **`-sd`**)   –  
  Specifies the maximum duration of the visualization physics simulation.
  Defaults to 1500 ms.
- **`--stop-physics`**
  (or **`-sp`**)   –  
  Disables visualization physics after the initial simulation has stabilized.

Property values for these arguments can consist either of a single property key,
or of a JSON string that can specify a different property for each label type.
A JSON string can only be specified using [variable injection](#notebook-magics-variable-injection "#notebook-magics-variable-injection").

## The `%seed` line magic

The `%seed` line magic is a convenient way to add data to your
Neptune endpoint that you can use to explore and experiment with Gremlin, openCypher,
or SPARQL queries. It provides a form where you can select the data model you want to
explore (property-graph or RDF) and then choose from among a number of different sample
data sets that Neptune provides.

## The `%load` line magic

The `%load` line magic generates a form that you can use to submit
a bulk load request to Neptune (see [Neptune Loader Command](load-api-reference-load.md "load-api-reference-load.md")). The source must be an Amazon S3 path
in the same region as the Neptune cluster.

## The `%load_ids` line magic

The `%load_ids` line magic retrieves the load Ids that have been
submitted to the notebook's host endpoint (see [Neptune Loader Get-Status request parameters](load-api-reference-status-requests.md#load-api-reference-status-parameters "load-api-reference-status-requests.md#load-api-reference-status-parameters")). The
request takes this form:

```
GET https://`your-neptune-endpoint`:`port`/loader
```

## The `%load_status` line magic

The `%load_status` line magic retrieves the load status of a particular
load job that has been submitted to the notebook's host endpoint, specified by the line
input (see [Neptune Loader Get-Status request parameters](load-api-reference-status-requests.md#load-api-reference-status-parameters "load-api-reference-status-requests.md#load-api-reference-status-parameters")). The
request takes this form:

```
GET https://`your-neptune-endpoint`:`port`/loader?loadId=`loadId`
```

The line magic looks like this:

```
%load_status `load id`
```

## The `%reset_graph` line magic

The `%reset_graph` (or `%_graph_reset`) line magic executes a
[ResetGraph](../../../neptune-analytics/latest/apiref/API_ResetGraph.md "../../../neptune-analytics/latest/apiref/API_ResetGraph.md")
call against the Neptune Analytics endpoint. It accepts the following optional line input:

- -ns or --no-skip-snapshot - If present, a final graph snapshot will be created before the graph data is deleted.
- --silent – If present, no output is displayed after the reset call is submitted.
- --store-to – Used to specify a variable to which to store the ResetGraph response.

## The `%cancel_load` line magic

The `%cancel_load` line magic cancels a particular load job (see [Neptune Loader Cancel Job](load-api-reference-cancel.md "load-api-reference-cancel.md")). The request takes this form:

```
DELETE https://`your-neptune-endpoint`:`port`/loader?loadId=`loadId`
```

The line magic looks like this:

```
%cancel_load `load id`
```

## The `%status` line magic

Retrieves [status information](access-graph-status.md "access-graph-status.md") from the
notebook's host endpoint ([%graph_notebook_config](#notebooks-line-magics-graph-notebook-config "#notebooks-line-magics-graph-notebook-config") shows the host
endpoint).

For Neptune DB hosts, status information will be fetched from the
[health status endpoint](access-graph-status.md "access-graph-status.md").
For Neptune Analytics hosts, the status will be retrieved via the
[GetGraph API](../../../neptune-analytics/latest/apiref/API_GetGraph.md "../../../neptune-analytics/latest/apiref/API_GetGraph.md").
See [%get_graph](#notebooks-line-magics-get-graph "#notebooks-line-magics-get-graph") for more
information.

## The `%get_graph` line magic

The `%get_graph` line magic retrieves information about a graph via the
[GetGraph API](../../../neptune-analytics/latest/apiref/API_GetGraph.md "../../../neptune-analytics/latest/apiref/API_GetGraph.md").
This magic is functionally identical to [%status](#notebooks-line-magics-status "#notebooks-line-magics-status") when used with Neptune Analytics.

## The `%gremlin_status` line magic

Retrieves [Gremlin query status information](gremlin-api-status.md "gremlin-api-status.md").

## The `%opencypher_status` line magic (also `%oc_status`)

Retrieves query status for an opencypher query. This line magic takes the
following optional arguments:

- **`--queryId`** or
  **`-q`**   –  
  Specifies the ID of a specific running query for which to show the status.
- **`--cancelQuery`** or
  **`-c`**   –  
  Cancels a running query. Does not take a value.
- **`--silent-cancel`** or
  **`-s`**   –  
  If `--silent` is set to `true` when cancelling
  a query, the running query is cancelled with an HTTP response code of
  `200`. Otherwise, the HTTP response code would be `500`.
- **`--store-to`**   –  
  Specifies the name of a variable in which to store the query results.
- **`-w/--includeWaiting`**   –  
  Neptune DB only. When set to true and other parameters are not present, causes status information for
  waiting queries to be returned as well as for running queries. This parameter does not take a value.
- **`--state`**   –  
  Neptune Analytics only. Specifies what subset of query states to retrieve the status of.
- **`-m/--maxResults`**   –  
  Neptune Analytics only. Sets an upper limit on the set of returned queries matching the value of
  `--state`.
- **`--silent`**   –  
  If present, no output is displayed after the query completes.

## The `%sparql_status` line magic

Retrieves [SPARQL query status information](sparql-api-status.md "sparql-api-status.md").

## The `%stream_viewer` line magic

The `%stream_viewer` line magic displays an interface that allows for
interactively exploring the entries logged in Neptune streams, if streams are enabled
on the Neptune cluster. It accepts the following optional arguments:

- **`language`**   –  
  The query language of the stream data: either `gremlin` or `sparql`.
  The default, if you don't supply this argument, is `gremlin`.
- **`--limit`**   –  
  Specifies the maximum number of stream entries to display per page.
  The default value, if you don't supply this argument, is `10`.

###### Note

The `%stream_viewer` line magic is fully supported only
on engine versions 1.0.5.1 and earlier.

## The `%graph_notebook_config` line magic

This line magic displays a JSON object containing the configuration that
the notebook is using to communicate with Neptune. The configuration includes:

- `host`: The endpoint to which to connect and issue
  commands.
- `port`: The port used when issuing commands to Neptune.
  The default is `8182`.
- `auth_mode`: The mode of authentication to use when
  issuing commands to Neptune. Must be `IAM` if connecting to a cluster
  that has IAM authentication enabled, or otherwise `DEFAULT`.
- `load_from_s3_arn`: Specifies an Amazon S3 ARN for
  the `%load` magic to use. If this value is empty, the ARN must
  be specified in the `%load` command.
- `ssl`: A Boolean value indicating whether or
  not to connect to Neptune using TLS. The default value is `true`.
- `aws_region`: The region where this notebook is
  deployed. This information is used for IAM authentication and for
  `%load` requests.

You can change the configuration by copying the `%graph_notebook_config`
output into a new cell and make changes to it there. Then if you run the [%%graph_notebook_config](#notebooks-cell-magics-graph-notebook-config "#notebooks-cell-magics-graph-notebook-config") cell
magic on the new cell, the configuration will be changed accordingly.

## The `%graph_notebook_host` line magic

Sets the line input as the notebook's host.

## The `%graph_notebook_version` line magic

The `%graph_notebook_version` line magic returns the Neptune workbench
notebook release number. For example, graph visualization was introduced in version
`1.27`.

## The `%graph_notebook_service` line magic

The `%graph_notebook_service` line magic sets the line input as the service name used for Neptune
requests.

## The `%graph_notebook_vis_options` line magic

The `%graph_notebook_vis_options` line magic displays the current
visualization settings that the notebook is using. These options are explained in the [vis.js](https://visjs.github.io/vis-network/docs/network/#options "https://visjs.github.io/vis-network/docs/network/#options")
documentation.

You can modify these settings by copying the output into a new cell,
making the changes you want, and then running the `%%graph_notebook_vis_options`
cell magic on the cell.

To restore the visualization settings to their default values, you
can run the `%graph_notebook_vis_options` line magic with a
`reset` parameter. This resets all the visualization settings:

```
%graph_notebook_vis_options reset
```

## The `%statistics` line magic

The `%statistics` line magic is used to retrieve or manage
DFE engine statistics (see [Managing statistics for the Neptune DFE to use](neptune-dfe-statistics.md "neptune-dfe-statistics.md")).
This magic can also be used to retrieve a [graph summary](neptune-graph-summary.md "neptune-graph-summary.md").

It accepts the following parameters:

- **`--language`**   –  
  The query language of the statistics endpoint: either or
  `propertygraph` (or `pg`) or `rdf`.

If not supplied, the default is `propertygraph`.

- **`--mode`** (or **`-m`**)   –  
  Specifies the type of request or action to submit: one of `status`,
  `disableAutoCompute`, `enableAutoCompute`, `refresh`,
  `delete`, `detailed`, or `basic`).

If not supplied, the default is `status` unless `--summary`
is specified, in which case the default is `basic`.

- **`--summary`**   –  
  Retrieves the graph summary from the statistics summary endpoint
  of the selected language.
- **`--silent`**   –  
  If present, no output is displayed after the query completes.
- **`--store-to`**   –  
  Used to specify a variable to which to store the query results.

## The `%summary` line magic

The `%summary` line magic is used to retrieve [graph summary](neptune-graph-summary.md "neptune-graph-summary.md") information.
It is available starting with Neptune engine version `1.2.1.0`.

It accepts the following parameters:

- **`--language`**   –  
  The query language of the statistics endpoint: either or
  `propertygraph` (or `pg`) or `rdf`.

If not supplied, the default is `propertygraph`.

- **`--detailed`**   –  
  Toggles the display of structures fields on or off in the output.

If not supplied, the default is the `basic` summary display mode.

- **`--silent`**   –  
  If present, no output is displayed after the query completes.
- **`--store-to`**   –  
  Used to specify a variable to which to store the query results.

## The `%%graph_notebook_config` cell magic

The `%%graph_notebook_config` cell magic uses a JSON object containing
configuration information to modify the settings that the notebook is using to communicate
with Neptune, if possible. The configuration takes the same form returned by the [%graph_notebook_config](#notebooks-line-magics-graph-notebook-config "#notebooks-line-magics-graph-notebook-config") line magic.

For example:

```
%%graph_notebook_config
{
  "host": "my-new-cluster-endpoint.amazon.com",
  "port": 8182,
  "auth_mode": "DEFAULT",
  "load_from_s3_arn": "",
  "ssl": true,
  "aws_region": "us-east-1"
}
```

## The `%%sparql` cell magic

The `%%sparql` cell magic issues a SPARQL query to the Neptune
endpoint. It accepts the following optional line input:

- **`-h` or `--help`**   –  
  Returns help text about these parameters.
- **`--path`**   –  
  Prefixes a path to the SPARQL endpoint. For example, if you specify
  `--path "abc/def"` then the endpoint called would be
  ``host`:`port`/abc/def`.
- **`--expand-all`**   –  
  This is a query visualization hint that tells the visualizer to include all
  `?s ?p ?o` results in the graph diagram regardless of binding type.

By default, a SPARQL visualization only includes triple patterns where the
`o?` is a `uri` or a `bnode` (blank node).
All other `?o` binding types such as literal strings or integers
are treated as properties of the `?s` node that can be viewed using
the **Details** pane in the **Graph** tab.

Use the `--expand-all` query hint when you may want to include such
literal values as vertices in the visualization instead.

Don't combine this visualization hint with explain parameters, because
explain queries are not visualized.

- **`--explain-type`**   –  
  Used to specify the explain mode to use (one of: `dynamic`,
  `static`, or `details`).
- **`--explain-format`**   –  
  Used to specify the response format for an explain query (one of
  `text/csv` or `text/html`).
- **`--store-to`**   –  
  Used to specify a variable to which to store the query results.

Example of an `explain` query:

```
%%sparql explain

SELECT * WHERE {?s ?p ?o} LIMIT 10
```

Example of a visualization query with an `--expand-all` visualization
hint parameter (see [SPARQL visualization](notebooks-visualization.md#notebooks-visualization-sparql "notebooks-visualization.md#notebooks-visualization-sparql")):

```
%%sparql --expand-all

SELECT * WHERE {?s ?p ?o} LIMIT 10
```

## The `%%gremlin` cell magic

The `%%gremlin` cell magic issues a Gremlin query to the Neptune
endpoint using WebSocket. It accepts an optional line input to toggle into [Gremlin explain](gremlin-explain.md "gremlin-explain.md") /> mode or
[Gremlin profile API](gremlin-profile-api.md "gremlin-profile-api.md"),
and a separate optional visualization hint input to modify visualization output
behavior (see [Gremlin visualization](notebooks-visualization.md#notebooks-visualization-Gremlin "notebooks-visualization.md#notebooks-visualization-Gremlin")).

Example of an `explain` query:

```
%%gremlin explain

g.V().limit(10)
```

Example of a `profile` query:

```
%%gremlin profile

g.V().limit(10)
```

Example of a visualization query with a visualization query hint:

```
%%gremlin -p v,outv

g.V().out().limit(10)
```

###### Optional parameters for `%%gremlin profile` queries

- **`--profile-chop`**   –  
  Specifies the maximum length of the profile results string. The default value
  if you don't supply this argument is 250.
- **`--profile-serializer`**   –  
  Specifies the serializer to use for the results. Allowed values are any of the
  valid MIME type or TinkerPop driver "Serializers" enum values. The default value
  if you don't supply this argument is `application.json`.
- **`--profile-no-results`**   –  
  Displays only the result count. If not used, all query results are displayed
  in the profile report by default.
- **`--profile-indexOps`**   –  
  Shows a detailed report of all index operations.

## The `%%opencypher` cell magic (also `%%oc`)

The `%%opencypher` cell magic (which also has the abbreviated
`%%oc` form), issues an openCypher query to the Neptune
endpoint. It accepts the following optional line input arguments:

- **`--mode`**   –  
  The query mode: either `query` or `bolt`. The default value
  if you don't supply this argument is `query`.
- **`--group-by`** or
  **`-g`**   –  
  Specifies the property used to group nodes. For example, `code, ~id`.
  The default value if you don't supply this argument is `~labels`.
- **`--ignore-groups`**   –  
  If present, all grouping options are ignored.
- **`--display-property`** or
  **`-d`**   –  
  Specifies the property whose value should be displayed for each vertex.
  The default value if you don't supply this argument is `~labels`.
- **`--edge-display-property`** or
  **`-de`**   –  
  Specifies the property whose value should be displayed for each edge.
  The default value if you don't supply this argument is `~labels`.
- **`--explain-type`**  –   Used to specify the
  explain mode to use (one of: dynamic, static, debug, or details).
- **`--label-max-length`** or
  **`-l`**   –  
  Specifies the maximum number of characters of a vertex label to display.
  The default value if you don't supply this argument is `10`.
- **`--store-to`** or
  **`-s`**   –  
  Specifies the name of a variable in which to store the query results.
- **`--plan-cache`** or
  **`-pc`**   –  
  Specifies the plan cache mode to use. The default value is `auto`.
- **`--query-timeout`** or
  **`-qt`**   –  
  Specifies the maximum query timeout in milliseconds. The default value is
  `1800000`.
- **`--query-parameters`** or
  **`qp`**   –  
  [Parameter definitions](opencypher-parameterized-queries.md "opencypher-parameterized-queries.md")
  to apply to the query. This option can either accept a single variable name,
  or a string representation of the map.

###### Example usage of `--query-parameters`

    1. Define a map of openCypher parameters in one notebook cell.




    ```
    params = '''{
     "name":"john",
     "age": 20,
    }'''
    ```
    2. Pass the parameters into `--query-parameters` in another cell with `%%oc`.




    ```
    %%oc --query-parameters params

    MATCH (n {name: $name, age: $age})
    RETURN n
    ```

## The `%%graph_notebook_vis_options` cell magic

The `%%graph_notebook_vis_options` cell magic lets you set
visualization options for the notebook. You can copy the settings returned
by the `%graph-notebook-vis-options` line magic into a new cell,
make changes to them, and use the `%%graph_notebook_vis_options`
cell magic to set the new values.

These options are explained in the [vis.js](https://visjs.github.io/vis-network/docs/network/#options "https://visjs.github.io/vis-network/docs/network/#options")
documentation.

To restore the visualization settings to their default values, you
can run the `%graph_notebook_vis_options` line magic with a
`reset` parameter. This resets all the visualization settings:

```
%graph_notebook_vis_options reset
```

## The `%neptune_ml` line magic

You can use the `%neptune_ml` line magic to initiate and manage various
Neptune ML operations.

###### Note

You can also initiate and manage some Neptune ML operations using the [%%neptune_ml](#notebooks-cell-magics-neptune_ml "#notebooks-cell-magics-neptune_ml")
cell magic.

- **`%neptune_ml export start`**   –  
  Starts a new export job.

###### Parameters

    + **`--export-url`**
    `exporter-endpoint`   –   (*optional*)
     The Amazon API Gateway endpoint where the exporter can be called.
    + **`--export-iam`**   –   (*optional*)
     Flag indicating that requests to the export url must be signed using SigV4.
    + **`--export-no-ssl`**   –   (*optional*)
     Flag indicating that SSL should not be used when connecting to the exporter.
    + **`--wait`**   –   (*optional*)
     Flag indicating that the operation should wait until the export has
     completed.
    + **`--wait-interval`**
    `interval-to-wait`   –   (*optional*)
     Sets the time, in seconds, between export status checks
     (*Default*: 60).
    + **`--wait-timeout`**
    `timeout-seconds`   –   (*optional*)
     Sets the time, in seconds, to wait for the export job to complete
     before returning the most recent status (*Default*: 3,600).
    + **`--store-to`**
    `location-to-store-result`   –   (*optional*)
     The variable in which to store the export result. If `--wait`
     is specified, the final status will be stored there.

- **`%neptune_ml export status`**   –  
  Retrieves the status of an export job.

###### Parameters

    + **`--job-id`** `export job ID`   –  
     The ID of the export job for which to retrieve status.
    + **`--export-url`**
    `exporter-endpoint`   –   (*optional*)
     The Amazon API Gateway endpoint where the exporter can be called.
    + **`--export-iam`**   –   (*optional*)
     Flag indicating that requests to the export url must be signed using SigV4.
    + **`--export-no-ssl`**   –   (*optional*)
     Flag indicating that SSL should not be used when connecting to the exporter.
    + **`--wait`**   –   (*optional*)
     Flag indicating that the operation should wait until the export has
     completed.
    + **`--wait-interval`**
    `interval-to-wait`   –   (*optional*)
     Sets the time, in seconds, between export status checks
     (*Default*: 60).
    + **`--wait-timeout`**
    `timeout-seconds`   –   (*optional*)
     Sets the time, in seconds, to wait for the export job to complete
     before returning the most recent status (*Default*: 3,600).
    + **`--store-to`**
    `location-to-store-result`   –   (*optional*)
     The variable in which to store the export result. If `--wait`
     is specified, the final status will be stored there.

- **`%neptune_ml dataprocessing start`**   –  
  Starts the Neptune ML dataprocessing step.

###### Parameters

    + **`--job-id`**
    `ID for this job`   –   (*optional*)
     ID to assign to this job.
    + **`--s3-input-uri`**
    `S3 URI`   –   (*optional*)
     The S3 URI at which to find the input for this dataprocessing job.
    + **`--config-file-name`**
    `file name`   –   (*optional*)
     Name of the configuration file for this dataprocessing job.
    + **`--store-to`**
    `location-to-store-result`   –   (*optional*)
     The variable in which to store the dataprocessing result.
    + **`--instance-type`**
    `(instance type)`   –   (*optional*)
     The instance size to use for this data-processing job.
    + **`--wait`**   –   (*optional*)
     Flag indicating that the operation should wait until the dataprocessing has
     completed.
    + **`--wait-interval`**
    `interval-to-wait`   –   (*optional*)
     Sets the time, in seconds, between dataprocessing status checks
     (*Default*: 60).
    + **`--wait-timeout`**
    `timeout-seconds`   –   (*optional*)
     Sets the time, in seconds, to wait for the dataprocessing job to complete
     before returning the most recent status (*Default*: 3,600).

- **`%neptune_ml dataprocessing status`**   –  
  Retrieves the status of a dataprocessing job.

###### Parameters

    + **`--job-id`**
    `ID of the job`   –  
     ID of the job for which to retrieve the status.
    + **`--store-to`**
    `instance type`   –   (*optional*)
     The variable in which to store the model-training result.
    + **`--wait`**   –   (*optional*)
     Flag indicating that the operation should wait until the model-training has
     completed.
    + **`--wait-interval`**
    `interval-to-wait`   –   (*optional*)
     Sets the time, in seconds, between model-training status checks
     (*Default*: 60).
    + **`--wait-timeout`**
    `timeout-seconds`   –   (*optional*)
     Sets the time, in seconds, to wait for the dataprocessing job to complete
     before returning the most recent status (*Default*: 3,600).

- **`%neptune_ml training start`**   –  
  Starts the Neptune ML model-training process.

###### Parameters

    + **`--job-id`**
    `ID for this job`   –   (*optional*)
     ID to assign to this job.
    + **`--data-processing-id`**
    `dataprocessing job ID`   –   (*optional*)
     ID of the dataprocessing job that created the artifacts to use for training.
    + **`--s3-output-uri`**
    `S3 URI`   –   (*optional*)
     The S3 URI at which to store the output from this model-training job.
    + **`--instance-type`**
    `(instance type)`   –   (*optional*)
     The instance size to use for this model-training job.
    + **`--store-to`**
    `location-to-store-result`   –   (*optional*)
     The variable in which to store the model-training result.
    + **`--wait`**   –   (*optional*)
     Flag indicating that the operation should wait until the model-training has
     completed.
    + **`--wait-interval`**
    `interval-to-wait`   –   (*optional*)
     Sets the time, in seconds, between model-training status checks
     (*Default*: 60).
    + **`--wait-timeout`**
    `timeout-seconds`   –   (*optional*)
     Sets the time, in seconds, to wait for the model-training job to complete
     before returning the most recent status (*Default*: 3,600).

- **`%neptune_ml training status`**   –  
  Retrieves the status of a Neptune ML model-training job.

###### Parameters

    + **`--job-id`**
    `ID of the job`   –  
     ID of the job for which to retrieve the status.
    + **`--store-to`**
    `instance type`   –   (*optional*)
     The variable in which to store the status result.
    + **`--wait`**   –   (*optional*)
     Flag indicating that the operation should wait until the model-training has
     completed.
    + **`--wait-interval`**
    `interval-to-wait`   –   (*optional*)
     Sets the time, in seconds, between model-training status checks
     (*Default*: 60).
    + **`--wait-timeout`**
    `timeout-seconds`   –   (*optional*)
     Sets the time, in seconds, to wait for the dataprocessing job to complete
     before returning the most recent status (*Default*: 3,600).

- **`%neptune_ml endpoint create`**   –  
  Creates a query endpoint for a Neptune ML model.

###### Parameters

    + **`--job-id`**
    `ID for this job`   –   (*optional*)
     ID to assign to this job.
    + **`--model-job-id`**
    `model-training job ID`   –   (*optional*)
     ID of the model-training job for which to create a query endpoint.
    + **`--instance-type`**
    `(instance type)`   –   (*optional*)
     The instance size to use for for the query endpoint..
    + **`--store-to`**
    `location-to-store-result`   –   (*optional*)
     The variable in which to store the result of the endpoint creation.
    + **`--wait`**   –   (*optional*)
     Flag indicating that the operation should wait until the endpoint creation has
     completed.
    + **`--wait-interval`**
    `interval-to-wait`   –   (*optional*)
     Sets the time, in seconds, between status checks
     (*Default*: 60).
    + **`--wait-timeout`**
    `timeout-seconds`   –   (*optional*)
     Sets the time, in seconds, to wait for the endpoint creation job to complete
     before returning the most recent status (*Default*: 3,600).

- **`%neptune_ml endpoint status`**   –  
  Retrieves the status of a Neptune ML query endpoint.

###### Parameters

    + **`--job-id`**
    `endpoint creation ID`   –   (*optional*)
     ID of an endpoint creation job for which to report status.
    + **`--store-to`**
    `location-to-store-result`   –   (*optional*)
     The variable in which to store the status result.
    + **`--wait`**   –   (*optional*)
     Flag indicating that the operation should wait until the endpoint creation has
     completed.
    + **`--wait-interval`**
    `interval-to-wait`   –   (*optional*)
     Sets the time, in seconds, between status checks
     (*Default*: 60).
    + **`--wait-timeout`**
    `timeout-seconds`   –   (*optional*)
     Sets the time, in seconds, to wait for the endpoint creation job to complete
     before returning the most recent status (*Default*: 3,600).

## The `%%neptune_ml` cell magic

The `%%neptune_ml` cell magic ignores line inputs such as `--job-id`
or `--export-url`. Instead, it lets you provide those inputs and others within
within the cell body.

You can also save such inputs in another cell, assigned to a Jupyter variable,
and then inject them into the cell body using that variable. That way, you can use such
inputs over and over without having to re-enter them all every time.

This only works if the injecting variable is the only content of the cell.
You cannot use multiple variables in one cell, or a combination of text and a
variable.

For example, the `%%neptune_ml export start` cell magic can consume a
JSON document in the cell body that contains all the parameters described in
[Parameters used to control the Neptune export process](export-parameters.md "export-parameters.md").

In the [Neptune-ML-01-Introduction-to-Node-Classification-Gremlin](https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/04-Machine-Learning/Neptune-ML-01-Introduction-to-Node-Classification-Gremlin.ipynb "https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/04-Machine-Learning/Neptune-ML-01-Introduction-to-Node-Classification-Gremlin.ipynb") notebook, under
**Configuring Features** in the **Export
the data and model configuration** section, you can see how the following
cell holds export parameters in a document assigned to a Jupyter variable named
`export-params`:

```
export_params = {
  "command": "export-pg",
  "params": {
    "endpoint": neptune_ml.get_host(),
    "profile": "neptune_ml",
    "useIamAuth": neptune_ml.get_iam(),
    "cloneCluster": False
   },
  "outputS3Path": f'{s3_bucket_uri}/neptune-export',
  "additionalParams": {
    "neptune_ml": {
      "targets": [
        {
          "node": "movie",
          "property": "genre"
        }
      ],
      "features": [
        {
          "node": "movie",
          "property": "title",
          "type": "word2vec"
        },
        {
          "node": "user",
          "property": "age",
          "type": "bucket_numerical",
          "range" : [1, 100],
          "num_buckets": 10
        }
      ]
    }
  },
  "jobSize": "medium"}
```

When you run this cell, Jupyter saves the parameters document under that name.
Then, you can use `${export_params}` to inject the JSON document into the
body of a `%%neptune_ml export start cell`, like this:

```
%%neptune_ml export start --export-url {neptune_ml.get_export_service_host()} --export-iam --wait --store-to export_results

${export_params}
```

### Available forms of the `%%neptune_ml` cell magic

The `%%neptune_ml` cell magic can be used in the following forms:

######

- **`%%neptune_ml export start`**   –  
  Starts a Neptune ML export process.
- **`%%neptune_ml dataprocessing start`**   –  
  Starts a Neptune ML dataprocessing job.
- **`%%neptune_ml training start`**   –  
  Starts a Neptune ML model-training job.
- **`%%neptune_ml endpoint create`**   –  
  Creates a Neptune ML query endpoint for a model.
