# Connect to a Splunk data source

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Configuration

### Data source

configuration

When configuring the Data Source, ensure that the URL field utilizes
`https` and points to the your configured Splunk port. The
default Splunk API point is 8089, not 8000 (this is default web UI port).
Enable _Basic Auth_ and specify Splunk username and
password.

#### Browser

(direct) access mode and CORS

Amazon Managed Grafana does not support browser direct access for the Splunk data
source.

### Advanced options

#### Stream mode

Enable stream mode if you want to get search results as they become
available. This is experimental feature, don’t enable it until you
really need it.

#### Poll result

Run search and then periodically check for result. Under the hood
this option runs `search/jobs` API call with
`exec_mode` set to `normal`. In this case API
request returns job SID, and then Grafana checks job status time to
time, in order to get job result. This option can be helpful for slow
queries. By default this option is disabled and Grafana sets
`exec_mode` to `oneshot` which allows
returning search result in the same API call. See more about
`search/jobs` API endpoint in [Splunk docs](https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTsearch#search.2Fjobs "https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTsearch#search.2Fjobs").

#### Search polling

interval

This option allow to adjust how often Amazon Managed Grafana will poll splunk for
search results. Time for next poll choosing randomly from [min, max)
interval. If you run a lot of heavy searches, it makes sense to increase
these values. Tips: increase _Min_ if search jobs
execution takes a long time, and _Max_ if you run a
lot of parallel searches (a lot of splunk metrics on Grafana dashboard).
Default is [500, 3000) milliseconds interval.

#### Automatic cancellation

If specified, the job automatically cancels after this many seconds
of inactivity (0 means never auto-cancel). Default is 30.

#### Status buckets

The most status buckets to generate. 0 indicates to not generate
timeline information. Default is 300.

#### Fields search mode

When you use visual query editor, data source attempts to get list of
available fields for selected source type.

- quick - use first available result from preview
- full - wait for job finish and get full result.

#### Default earliest time

Some searches can’t use dashboard time range (such as template
variable queries). This option helps to prevent search for all time,
which can slow down Splunk. The syntax is an integer and a time unit
`[+|-]<time_integer><time_unit>`. For example
`-1w`. [Time unit](https://docs.splunk.com/Documentation/Splunk/latest/Search/Specifytimemodifiersinyoursearch "https://docs.splunk.com/Documentation/Splunk/latest/Search/Specifytimemodifiersinyoursearch") can be `s, m, h, d, w, mon, q, y`.

#### Variables search

mode

Search mode for template variable queries. Possible values:

- fast - Field discovery off for event searches. No event or
  field data for stats searches.
- smart - Field discovery on for event searches. No event or
  field data for stats searches.
- verbose - All event & field data.

## Usage

### Query editor

#### Editor modes

Query editor support two modes: raw and visual. To switch between
these modes choose hamburger icon at the right side of editor and select
_Toggle Editor Mode_.

#### Raw mode

Use `timechart` command for time series data, as shown in
the following code example.

```

index=os sourcetype=cpu | timechart span=1m avg(pctSystem) as system, avg(pctUser) as user, avg(pctIowait) as iowait
index=os sourcetype=ps | timechart span=1m limit=5 useother=false avg(cpu_load_percent) by process_name

```

Queries support template variables, as shown in the following
example.

```
sourcetype=cpu | timechart span=1m avg($cpu)
```

Keep in mind that Grafana is time series–oriented application
and your search should return time series data (timestamp and value) or
single value. You can read about [timechart](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Timechart "https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Timechart") command and find more search examples in official
[Splunk Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual "https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual")

#### Splunk Metrics and

`mstats`

Splunk 7.x provides `mstats` command for analyzing
metrics. To get charts working properly with `mstats`, it
should be combined with `timeseries` command and
`prestats=t` option must be set.

````
Deprecated syntax:
| mstats prestats=t avg(_value) AS Value WHERE index="collectd" metric_name="disk.disk_ops.read" OR metric_name="disk.disk_ops.write" by metric_name span=1m
| timechart avg(_value) span=1m by metric_name Actual:
| mstats prestats=t avg(disk.disk_ops.read) avg(disk.disk_ops.write) WHERE index="collectd" by metric_name span=1m
| timechart avg(disk.disk_ops.read) avg(disk.disk_ops.write) span=1m ``` Read more about `mstats` command in [Splunk Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Mstats "https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Mstats"). #### Format as There are two supported result format modes - *Time series* (default) and *Table*. Table mode suitable for using with Table panel when you want to display aggregated data. That works with raw events (returns all selected fields) and `stats` search function, which returns table-like data. Examples: ``` index="os" sourcetype="vmstat" | fields host, memUsedMB index="os" sourcetype="ps" | stats avg(PercentProcessorTime) as "CPU time", latest(process_name) as "Process", avg(UsedBytes) as "Memory" by PID ``` The result is similar to *Statistics* tab in Splunk UI. Read more about `stats` function usage in [Splunk Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Stats "https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Stats"). #### Visual mode This mode provides step-by-step search creating. Note that this mode creates `timechart` splunk search. Just select index, source type, and metrics, and set split by fields if you want. ##### Metric You can add multiple metrics to search by choosing *plus* button at the right side of metric row. Metric editor contains list of frequently used aggregations, but you can specify here any other function. Just choose agg segment (`avg` by default) and type what you need. Select interested field from the dropdown list (or enter it), and set alias if you want. ##### Split by and Where If you set Split by field and use *Time series* mode, Where editor will be available. Choose *plus* and select operator, aggregation and value, for example *Where avg in top 10*. Note, this *Where* clause is a part of *Split by*. See more at [timechart docs](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/timechart#where_clause "https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/timechart#where_clause"). #### Options To change default timechart options, choose **Options** at the last row. See more about these options in [timechart docs](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/timechart "https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/timechart"). #### Rendered splunk search Choose the target letter at the left to collapse the editor and show the rendered splunk search. ### Annotations Use annotations if you want to show Splunk alerts or events on graph. Annotation can be either predefined Splunk alert or regular splunk search. #### Splunk alert Specify an alert name, or keep the field blank to get all fired alerts. Template variables are supported. #### Splunk search Use splunk search to get needed events, as shown in the following example. ``` index=os sourcetype=iostat | where total_ops > 400 index=os sourcetype=iostat | where total_ops > $io_threshold ``` Template variables are supported. The **Event field as text** option is suitable if you want to use field value as annotation text. The following example shows error message text from logs. ``` Event field as text: _raw Regex: WirelessRadioManagerd\[\d*\]: (.*) ``` Regex allows to extract a part of message. ### Template variables Template variables feature supports Splunk queries which return list of values, for example with `stats` command. ``` index=os sourcetype="iostat" | stats values(Device) ``` This query returns list of `Device` field values from `iostat` source. Then you can use these device names for time series queries or annotations. There are two possible types of variable queries can be used in Grafana. The first is a simple query (as presented earlier), which returns a list of values. The second type is a query that can create a key/value variable. The query should return two columns that are named `_text` and `_value`. The `_text` column value should be unique (if it is not unique then the first value is used). The options in the dropdown list will have a text and value so that you can have a friendly name as text and an ID as the value. For example, this search returns table with columns `Name` (Docker container name) and `Id` (container id). ``` source=docker_inspect | stats count latest(Name) as Name by Id | table Name, Id ``` To use container name as a visible value for variable and id as it’s real value, query should be modified, as in the following example. ``` source=docker_inspect | stats count latest(Name) as Name by Id | table Name, Id | rename Name as "_text", Id as "_value" ``` #### Multi-value variables It’s possible to use multi-value variables in queries. An interpolated search will be depending on variable usage context. There are a number of that contexts which plugin supports. Assume there’s a variable `$container` with selected values `foo` and `bar`: <br>• Basic filter for `search` command ``` source=docker_stats $container => source=docker_stats (foo OR bar) ``` <br>• Field-value filter ``` source=docker_stats container_name=$container => source=docker_stats (container_name=foo OR container_name=bar) ``` <br>• Field-value filter with the `IN` operator and `in()` function ``` source=docker_stats container_name IN ($container) => source=docker_stats container_name IN (foo, bar) source=docker_stats | where container_name in($container) => source=docker_stats | where container_name in(foo, bar) ``` #### Multi-value variables and quotes If variable wrapped in quotes (both double or single), its values also will be quoted, as in the following example. ``` source=docker_stats container_name="$container" => source=docker_stats (container_name="foo" OR container_name="bar") source=docker_stats container_name='$container' => source=docker_stats (container_name='foo' OR container_name='bar') ```
````
