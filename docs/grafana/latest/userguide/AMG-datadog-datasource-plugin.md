# Connect to a Datadog data

source

The Datadog data source enables you to visualize metrics from the Datadog
monitoring service in Amazon Managed Grafana.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Usage

### Caching

For large dashboards, that make lots of queries it is possible to be rate
limited by the Datadog API (reach the maximum number of API calls per hour
that the Datadog API allows). The caching feature caches unique queries for
60 seconds. This interval can be changed to be longer or shorter on the
config page.

### Query editor

It’s easy - select aggregation and metric. If you want to filter result,
select one or more tags.

The Datadog data source supports all of the advanced functions that the
Datadog query editor supports. Select it from the dropdown list and arrange
by choosing a function name.

**Alias by field usage possibilities**:

- Enter the alias into the "Alias by" field.
- Use scoped variables:
  - `$__metric` = replaced with metric name
  - `$__display_name` = replaced with metric name
  - `$__expression` = replaced with full metric
    expression
  - `$__aggr` = replaced with metric aggregation
    function (for example, avg, max, min, sum)
  - `$__scope` = replaced with metric scope (for
    example, region, site, env, host)

- Use regular expressions:
  - Enter your regular expression into "Alias
    RegExp" field in `/you regexp
here/flags` format.
  - If "Alias by" field is empty, RegExp results
    will be joined using. Example with metric expression =
    `avg:system.load.5{*}` : "Alias
    by" field input: """Alias RegExp"
    field input: `avg:(.+)\.(\d)` Result:
    `system.load, 5`
  - Use `$<group_number>` variables in
    "Alias by" field. Example with metric
    expression = `avg:system.load.5{*}` :
    "Alias by" field input: `$1: $2
seconds`
    "Alias RegExp" field input:
    `avg:(.+)\.(\d)` Result: `system.load: 5
seconds`
  - Use `$0` to get the whole expression. Example
    with metric expression =
    `datadog.dogstatsd.packet.count{*}` :
    "Alias by" field input: `Expression:
 $0`
    "Alias RegExp" field input:
    `DOGstatsd\.(.*)\.(.*){\*}/i` Result:
    `Expression:
 datadog.dogstatsd.packet.count{*}`
    Note: you’ll get an error using nonexistent group number.

#### Metric arithmetic

To use metric arithmetic set _Query type_ to
_Arithmetic_. Link to the metric that you want by
using `#` sign. For example, `#A * 2` will double
the result of query `A`. Arithmetic between two metrics works
in the same way - add queries which results you want to use for the
calculation and then link to these metrics in the third query, such as
`#A / #B`.

### Annotations

An annotation is an event that is overlaid on top of graphs - an example
of an event is a deployment or an outage. With this data source, you can
fetch events from Datadog and overlay them on graphs in Amazon Managed Grafana.
Annotations events can be filtered by source, tag or priority.

### Templating

There are a few options for getting values of template variable - metrics
and tags. To fetch the list of available metrics specify `*` in
the _Query_ field.

To return all tags use the value: `tag` or `scope`.

To return tags for a specified tag group then use one of the following
default category values:

- `host`
- `device`
- `env`
- `region`
- `site`
- `status`
- `version`

For custom tag groups, then just enter the tag group name. For
example, if your custom tag group name is `subscription_name`,
enter that in the _Query_ field.

Filter results by using the _Regex_ field. Multi-value
variables are supported when using tags - multiple selected tag values will
be converted into a comma separated list of tags.

#### Ad-hoc filters

There is a new special type of template variable in Grafana called
_Ad-hoc filters_. This variable will apply to
_all_ the Datadog queries in a dashboard. This
allows using it like a quick filter. An ad-hoc variable for Datadog
fetches all the key-value pairs from tags, for example,
`region:east, region:west`, and uses them as query tags.
To create this variable, select the _Ad-hoc filters_
type and choose your Datadog data source. You can set any name for this
variable.
