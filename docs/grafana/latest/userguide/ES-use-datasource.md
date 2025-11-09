# Using the Amazon OpenSearch Service data source

## Metric query editor

The OpenSearch query editor allows you to select multiple metrics and
group by multiple terms or filters. Use the plus and minus icons to the
right to add/remove metrics or group by clauses. Some metrics and group by
clauses have options. Choose the option text to expand the\ row to view and
edit metric or group by options.

## Using Piped Processing Language (PPL)

The Amazon OpenSearch Service data source supports Piped Processing Language (PPL), which
enables simpler yet powerful querying and visualization capabilities for
OpenSearch. PPL enables customers to explore and find data without having
to compose lengthy OpenSearch Domain Specific Language (DSL) statements or
write queries using JSON objects. With PPL, you can write queries as a set
of commands delimited by pipes similar to UNIX pipes.

Take the following sample DSL query as an example:

```
GET opensearch_sample_data_logs/_search{"from":0,"size":0,"timeout":"1m","query":{"bool":{"should":[{"term":{"response.keyword":{"value":"404","boost":1}}},{"term":{"response.keyword":{"value":"503","boost":1}}}],"adjust_pure_negative":true,"boost":1}},"sort":[{"_doc":{"order":"asc"}}],"aggregations":{"composite_buckets":{"composite":{"size":1000,"sources":[{"host":{"terms":{"field":"host.keyword","missing_bucket":true,"order":"asc"}}},{"response":{"terms":{"field":"response.keyword","missing_bucket":true,"order":"asc"}}}]},"aggregations":{"request_count":{"value_count":{"field":"request.keyword"}},"sales_bucket_sort":{"bucket_sort":{"sort":[{"request_count":{"order":"desc"}}],"size":10}}}}}}>
```

The preceding DSL query can be replaced with the following PPL command
that is concise and human readable.

```
source = opensearch_sample_data_logs | where response='404' or response='503' | stats count(request) as request_count by host, response | sort –request_count
```

For more information about PPL, see [Querying
Amazon OpenSearch Service data using Piped Processing Language](../../../opensearch-service/latest/developerguide/ppl-support.md "../../../opensearch-service/latest/developerguide/ppl-support.md").

## Series naming and

alias patterns

You can control the name for time series using the `Alias`
input field.

| Pattern              | Description                                           |
| -------------------- | ----------------------------------------------------- |
| `{{term fieldname}}` | Replaced with value of a term Group By.               |
| `{{metric}}`         | Replaced with metric name (ex. Average, Min,<br>Max). |
| `{{field}}`          | Replaced with the metric field name.                  |

## Pipeline metrics

Some metric aggregations are called pipeline aggregations; for example,
_Moving Average_ and _Derivative_.
OpenSearch pipeline metrics require another metric to be based on. Use the
eye icon next to the metric to hide metrics from appearing in the graph.
This is useful for metrics you only have in the query for use in a pipeline
metric.

## Templating

Instead of hardcoding things such as server, application, and sensor name
in your metric queries you can use variables in their place. Variables are
shown as dropdown select boxes at the top of the dashboard. You can use
these dropdown boxes to change the data being displayed in your dashboard.

For more information about templating and template variables, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

### Query variable

The OpenSearch Service data source supports two types of queries you can use in
the _Query_ field of _Query_
variables. The query is written using a custom JSON string.

| Query                                                                      | Description                                                                                                                                                                    |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `{"find": "fields",<br>"type": "keyword"}`                                 | Returns a list of field names with the index type<br>`keyword`.                                                                                                                |
| `{"find": "terms",<br>"field": "@hostname",<br>"size": 1000}`              | Returns a list of values for a field using term<br>aggregation. Query will use current dashboard time range<br>as time range for query.                                        |
| `{"find": "terms",<br>"field": "@hostname",<br>"query": '<lucene query>'}` | Returns a list of values for a field using term<br>aggregation and a specified Lucene query filter. Query<br>will use current dashboard time range as time range for<br>query. |

There is a default size limit of 500 on terms queries. To set a custom
limit, set the size property in your query. You can use other variables
inside the query. The following code example shows the query definition
for a variable named `$host`.

```

{"find": "terms", "field": "@hostname", "query": "@source:$source"}

```

In the previous example, we use another variable named
`$source` inside the query definition. Whenever you
change, using the dropdown list, the current value of the
`$source` variable, it initiates an update of the
`$host` variable. After the update, the
`$host` variable contains only hostnames filtered by in
this case the `@source` document property.

These queries by default return results in term order (which can then
be sorted alphabetically or numerically as for any variable). To produce
a list of terms sorted by doc count (a top-N values list), add an
`orderBy` property of `doc_count`. This
automatically selects a descending sort. Using `asc` with
doc_count (a bottom-N list) can be done by setting `order:
 "asc"`, but it is discouraged because it increases
the error on document counts. To keep terms in the doc count order, set
the variable’s **Sort** dropdown list to
**Disabled**. Alternatively, you might
alternatively still want to use **Alphabetical** to
re-sort them.

```

{"find": "terms", "field": "@hostname", "orderBy": "doc_count"}

```

### Using variables in

queries

There are two syntaxes:

- `$<varname>` Example: @hostname:$hostname
- `[[varname]]` Example: @hostname:[[hostname]]

Why two ways? The first syntax is easier to read and write, but it
does not allow you to use a variable in the middle of a word. When the
_Multi-value_ or _Include all
value_ options are enabled, Grafana converts the labels
from plaintext to a Lucene-compatible condition.

In the previous example, we have a lucene query that filters
documents based on the `@hostname` property using a variable
named `$hostname`. It is also using a variable in the
_Terms_ group by field input box. This allows you
to use a variable to quickly change how the data is grouped.

## Annotations

Annotations allow you to overlay rich event information on top of graphs.
You add annotation queries using the Dashboard menu or Annotations view.
Grafana can query any OpenSearch index for annotation events. For more
information, see [Annotations](dashboard-annotations.md "dashboard-annotations.md").

| Name       | Description                                                                                                                             |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `Query`    | You can keep the search query blank or specify a Lucene<br>query.                                                                       |
| `Time`     | The name of the time field; must be date field.                                                                                         |
| `Time End` | Optional name of the time end field must be date field.<br>If set, annotations will be marked as a region between time<br>and time-end. |
| `Text`     | Event description field.                                                                                                                |
| `Tags`     | Optional field name to use for event tags (can be an<br>array or a CSV string).                                                         |

## Querying logs

Querying and displaying log data from OpenSearch is available in
Explore. To display your logs, select the OpenSearch Service data source, and then
optionally enter a Lucene query. For more information, see [Explore](explore.md "explore.md").

### Log queries

After the result is returned, the log panel shows a list of log rows
and a bar chart where the x-axis shows the time and the y-axis shows the
frequency or count.

### Filtering log messages

Optionally, enter a Lucene query into the query field to filter the
log messages. For example, using a default Filebeat setup, you should be
able to use `fields.level:error` to show only error log
messages.
