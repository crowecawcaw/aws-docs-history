# Templates and variables

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

A variable is a placeholder for a value. You can use variables in metric queries and in
panel titles. Variables give you the ability to create more interactive and dynamic
dashboards. Instead of hardcoding things like server, application, and sensor names in your
metric queries, you can use variables in their place.

Variables are displayed as dropdown lists at the top of the dashboard. When you change the
value by using the dropdown list at the top of the dashboard, your panel’s metric queries
reflect the new value.

These can be especially useful for administrators who want to allow viewers to adjust
visualizations quickly but do not want to give them full editing permissions. Grafana
viewers can use variables.

By using variables and templates, you can single-source dashboards. If you have multiple
identical data sources or servers, you can make one dashboard and use variables to change
what you are viewing. This simplifies maintenance and upkeep.

For a list of supported variable types, and instructions for adding each type of variable,
see [Variable types](variables-types.md "variables-types.md")

## Templates

A _template_ is any query that contains a variable.

For example, if you were administering a dashboard to monitor several servers, you
could make a dashboard for each server. Or you could create one dashboard and use panels
with template queries, as shown in the following example.

```
wmi_system_threads{instance=~"$server"}
```

Variable values are always synced to the URL by using the syntax
`var-<varname>=value`.

## Variable best practices

Variable dropdown lists are displayed in the order they are listed in the variable
list in **Dashboard settings**.

Put the variables that you will change often at the top, so that they will be shown
first, at the far left on the dashboard.

## Variable syntax

Panel titles and metric queries can see variables by using two different syntaxes:

- `$varname` This syntax is easier to read, as in the following
  example: `apps.frontend.$server.requests.count`. However, you cannot
  use a variable in the middle of a word.
- `${var_name}` Use this syntax when you want to interpolate a variable
  in the middle of an expression.
- `${var_name:<format>}` This format gives you more control over
  how Grafana interpolates values. For more information, see [Advanced variable format
  options](#advanced-variable-format-options "#advanced-variable-format-options").

Before queries are sent to your data source, the query is
_interpolated_, meaning that the variable is replaced with its
current value. During interpolation, the variable value might be
_escaped_ to conform to the syntax of the query language and
where it is used. For example, a variable that is used in a regex expression in a
Prometheus query will be regex-escaped. Read the data source–specific
documentation topic for details on value escaping during interpolation.

For information about advanced syntax to override data source default formatting, see
[Advanced variable format
options](#advanced-variable-format-options "#advanced-variable-format-options").

## Other variable options

This section explains the other variable options that are available.

### Entering variable selection

options

You can use **Selection Options** to manage variable
option selections. All selection options are optional, and they are off by default.

#### Multi-value

If you turn this option on, the variable dropdown list supports the selection
of multiple options at the same time. For more information, see [Formatting multi-value
variables](#formatting-multi-value-variables "#formatting-multi-value-variables").

#### Include All option

The Grafana workspace adds an `All` option to the variable dropdown
list. If an end user selects this option, all variable options are selected.

#### Custom all value

This option is visible only if the **Include All
option** is selected.

To define the value of the `All` option, enter regex, glob, or
Lucene syntax in the **Custom all value** field.

By default, the `All` value includes all options in combined
expression. This can become very long and can have performance problems.
Sometimes it can be better to specify a custom all value, like a wild card
regex.

When you use custom regex, glob, or Lucene syntax in the **Custom all value** option, it is never escaped, so you must
consider what is a valid value for your data source.

### Advanced variable format

options

The formatting of the variable interpolation depends on the data source, but
there are some situations where you might want to change the default formatting.

For example, the default for the MySQL data source is to join multiple values as
comma-separated with quotes: `'server01','server02'`. In some cases, you
might want to have a comma-separated string without quotes:
`server01,server02`. To do this, use the following advanced variable
formatting options.

#### General syntax

Syntax: `${var_name:option}`

If any invalid formatting option is specified, `glob` is the
default, or fallback, option.

#### CSV

Formats variables with multiple values as a comma-separated string.

```

servers = ['test1', 'test2']
String to interpolate: '${servers:csv}'
Interpolation result: 'test1,test2'

```

#### Distributed - OpenTSDB

Formats variables with multiple values in custom format for OpenTSDB.

```

servers = ['test1', 'test2']
String to interpolate: '${servers:distributed}'
Interpolation result: 'test1,servers=test2'

```

#### Doublequote

Formats single-value and multi-value variables into a comma-separated string,
escapes `"` in each value by `\"`, and quotes
each value with `"`.

```

servers = ['test1', 'test2']
String to interpolate: '${servers:doublequote}'
Interpolation result: '"test1","test2"'

```

#### Glob - Graphite

Formats variables with multiple values into a glob (for Graphite queries).

```

servers = ['test1', 'test2']
String to interpolate: '${servers:glob}'
Interpolation result: '{test1,test2}'

```

#### JSON

Formats variables with multiple values as a comma-separated string.

```

servers = ['test1', 'test2']
String to interpolate: '${servers:json}'
Interpolation result: '["test1", "test2"]'

```

#### Lucene - OpenSearch

Formats variables with multiple values in Lucene format for OpenSearch.

```

servers = ['test1', 'test2']
String to interpolate: '${servers:lucene}'
Interpolation result: '("test1" OR "test2")'

```

#### Percentencode

Formats single-value and multi-value variables for use in URL parameters.

```

servers = ['foo()bar BAZ', 'test2']
String to interpolate: '${servers:percentencode}'
Interpolation result: 'foo%28%29bar%20BAZ%2Ctest2'

```

#### Pipe

Formats variables with multiple values into a pipe-separated string.

```

servers = ['test1.', 'test2']
String to interpolate: '${servers:pipe}'
Interpolation result: 'test1.|test2'

```

#### Raw

Turns off data source–specific formatting, such as single quotes in an
SQL query.

```

servers = ['test1.', 'test2']
String to interpolate: '${var_name:raw}'
Interpolation result: '{test.1,test2}'

```

#### Regex

Formats variables with multiple values into a regex string.

```

servers = ['test1.', 'test2']
String to interpolate: '${servers:regex}'
Interpolation result: '(test1\.|test2)'

```

#### Singlequote

Formats single- and multi-value variables into a comma-separated string,
escapes `'` in each value by `\'` and quotes each value
with `'`.

```

servers = ['test1', 'test2']
String to interpolate: '${servers:singlequote}'
Interpolation result: "'test1','test2'"

```

#### Sqlstring

Formats single- and multi-value variables into a comma-separated string,
escapes `'` in each value by `''` and quotes each value
with `'`.

```

servers = ["test'1", "test2"]
String to interpolate: '${servers:sqlstring}'
Interpolation result: "'test''1','test2'"

```

#### Text

Formats single-value and multi-value variables into their text
representation. For a single variable, it will just return the text
representation. For multi-value variables, it will return the text
representation combined with `+`.

```

servers = ["test1", "test2"]
String to interpolate: '${servers:text}'
Interpolation result: "test1 + test2"

```

### Formatting multi-value

variables

Interpolating a variable with multiple values selected is tricky as it is not
straight forward how to format the multiple values into a string that is valid in
the given context where the variable is used. Grafana tries to solve this by
enabling each data source plugin to inform the templating interpolation engine what
format to use for multiple values.

###### Note

The **Custom all value** option on the variable
must be blank for Grafana to format all values into a single string. If leave it
blank, then the Grafana concatenates (adds together) all the values in the
query. Something like `value1,value2,value3`. If a custom
`all` value is used, then instead the value will be something
like `*` or `all`.

#### Multi-value

variables with a Graphite data source

Graphite uses glob expressions. A variable with multiple values would, in
this case, be interpolated as `{host1,host2,host3}` if the current
variable value was _host1_, _host2_, and
_host3_.

#### Multi-value variables with a Prometheus or InfluxDB data source

InfluxDB and Prometheus use regex expressions, so the same variable would be
interpolated as `(host1|host2|host3)`. Every value would also be
regex escaped. If not, a value with a regex control character would break the
regex expression.

#### Multi-value

variables with an Elastic data source

Amazon OpenSearch uses Lucene query syntax, so the same variable would be
formatted as `("host1" OR "host2" OR
 "host3")`. In this case, every value must be escaped so that
the value contains only Lucene control words and quotation marks.

#### Troubleshooting formatting

Automatic escaping and formatting can cause problems. It can be tricky to
grasp the logic behind a problem, especially for InfluxDB and Prometheus, where
the use of regex syntax requires that the variable is used in regex operator
context.

If you do not want Grafana to do this automatic regex escaping and
formatting, you must do one of the following:

- Turn off the **Multi-value**
  **Include All option** options.
- Use the [raw variable format]({{< relref
  "advanced-variable-format-options.md#raw"
  > }}).

### Filtering variables with regex

Using the Regex Query option, you can filter the list of options returned by the
variable query or modify the options returned.

This section shows how to use regex to filter and modify values in the variable
dropdown list.

Using the Regex Query option, you filter the list of options returned by the
Variable query or modify the options returned. For more information, see [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions").

Examples of filtering on the following list of options:

```

backend_01
backend_02
backend_03
backend_04

```

#### Filtering so that only the options that end with `01` or

`02` are returned

Regex:

```

/.*[01|02]/

```

Result:

```

backend_01
backend_02

```

#### Filtering and modifying the options using a regex capture group to return

part of the text

Regex:

```

/.*(01|02)/

```

Result:

```

01
02

```

#### Filtering and modifying

- Prometheus Example

List of options:

```

up{instance="demo.robustperception.io:9090",job="prometheus"} 1 1521630638000
up{instance="demo.robustperception.io:9093",job="alertmanager"} 1 1521630638000
up{instance="demo.robustperception.io:9100",job="node"} 1 1521630638000

```

Regex:

```

/.*instance="([^"]*).*/

```

Result:

```

demo.robustperception.io:9090
demo.robustperception.io:9093
demo.robustperception.io:9100

```

#### Filtering and modifying using named text and value capture groups

Using named capture groups, you can capture separate "text" and
"value" parts from the options returned by the variable query.
The variable dropdown list can contain a friendly name for each value that can
be selected.

For example, when querying the `node_hwmon_chip_names` Prometheus
metric, the `chip_name` is friendlier than the `chip`
value. Start with the following variable query result.

```

node_hwmon_chip_names{chip="0000:d7:00_0_0000:d8:00_0",chip_name="enp216s0f0np0"} 1
node_hwmon_chip_names{chip="0000:d7:00_0_0000:d8:00_1",chip_name="enp216s0f0np1"} 1
node_hwmon_chip_names{chip="0000:d7:00_0_0000:d8:00_2",chip_name="enp216s0f0np2"} 1
node_hwmon_chip_names{chip="0000:d7:00_0_0000:d8:00_3",chip_name="enp216s0f0np3"} 1

```

Pass it through the following Regex.

```

/chip_name="(?<text>[^"]+)|chip="(?<value>[^"]+)/g

```

The following dropdown list is produced.

```

Display Name          Value
------------          -------------------------
enp216s0f0np0         0000:d7:00_0_0000:d8:00_0
enp216s0f0np1         0000:d7:00_0_0000:d8:00_1
enp216s0f0np2         0000:d7:00_0_0000:d8:00_2
enp216s0f0np3         0000:d7:00_0_0000:d8:00_3

```

**Note:** Only `text` and
`value` capture group names are supported.

### Repeating panels or rows

You can create dynamic dashboards using _template variables_.
All variables in your queries expand to the current value of the variable before the
query is sent to the database. With variables, you can reuse a single dashboard for
all your services.

Template variables can be very useful for dynamically changing your queries
across a whole dashboard. If you want Grafana to dynamically create new panels or
rows based on the values that you have selected, you can use the
_Repeat_ feature.

#### Repeating panels

If you have a variable with `Multi-value` or `Include all
 value` options turned on, you can choose one panel and have Grafana
repeat that panel for every selected value. You can find the
_Repeat_ feature under the _General
tab_ in panel edit mode.

The `direction` controls how the panels are arranged.

If you choose `horizontal`, the panels are arranged side-by-side.
Grafana automatically adjusts the width of each repeated panel so that the whole
row is filled. Currently, you cannot mix other panels on a row with a repeated
panel.

Set `Max per row` to tell Grafana how many panels per row you want
at most. It defaults to _4_.

If you choose `vertical`, the panels are arranged from top to
bottom in a column. The width of the repeated panels is the same as of the first
panel (the original template) that is being repeated.

Make changes only to the first panel (the original template). For the changes
take effect on all panels, you need to start a dynamic dashboard re-build. You
can do this by either changing the variable value (that is, the basis for the
repeat) or reloading the dashboard.

###### Note

Repeating panels require variables to have one or more items selected. You
cannot repeat a panel zero times to hide it.

#### Repeating rows

As seen above with the panels you can also repeat rows if you have variables
set with `Multi-value` or `Include all value` selection
option.

To turn on this feature, you must first add a new _Row_ by
using the _Add Panel_ menu. Then pause on the row title and
choose the cog button to access the `Row Options` configuration
panel. You can then select the variable you want to repeat the row for.

A best practice is to use a variable in the row title as well.
