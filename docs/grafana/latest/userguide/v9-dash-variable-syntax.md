# Variable syntax

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Panel titles and metric queries can refer to variables using two different
syntaxes.

- `$varname` – This syntax is easy to read, but it
  does not allow you to use a variable in the middle of a word.

**Example:**
`apps.frontend.$server.requests.count`

- `${var_name}` – Use this syntax when you want to
  use a variable in the middle of an expression.
- `${var_name:<format>}` – This format gives you
  more control over how Grafana interprets values. For more information,
  see _Advanced variable format options_.
- `[[varname]]` – Do not use. This syntax is old and
  has been deprecated. It will be removed in a future release.
  Before queries are sent to your data source the query is _interpolated_, meaning the variable is replaced with its current
  value. During interpolation, the variable value might be _escaped_ in order to conform to the syntax of the query language and
  where it is used. For example, a variable used in a regex expression in an InfluxDB
  or Prometheus query will be regex escaped.

**Advanced variable format options**

The formatting of the variable interpolation depends on the data source, but
there are some situations where you might want to change the default
formatting.

For example, the default for the MySQL data source is to join multiple values as
comma-separated with quotes: `'server01','server02'`. In some cases, you
might want to have a comma-separated string without quotes:
`server01,server02`. You can make that happen with advanced variable
formatting options listed below.

**General syntax**

Syntax: `${var_name:option}`

If any invalid formatting option is specified, then
`glob` is the default/fallback option.

**CSV**

Formats variables with multiple values as a comma-separated string.

```
servers = [ 'test1',  'test2' ]
String to interpolate:  '${servers:csv}'
Interpolation result:  'test1,test2'
```

**Distributed - OpenTSDB**

Formats variables with multiple values in custom format for
OpenTSDB.

```
servers = [ 'test1',  'test2' ]
String to interpolate:  '${servers:distributed}'
Interpolation result:  'test1,servers=test2'
```

**Doublequote**

Formats single- and multi-valued variables into a comma-separated string,
escapes `"` in each value by
`\"` and quotes each value with
`"`.

```
servers = [ 'test1',  'test2' ]
String to interpolate:  '${servers:doublequote}'
Interpolation result:  '"test1","test2"'
```

**Glob - Graphite**

Formats variables with multiple values into a glob (for Graphite
queries).

```
servers = [ 'test1',  'test2' ]
String to interpolate:  '${servers:glob}'
Interpolation result:  '{test1,test2}'
```

**JSON**

Formats variables with multiple values as a comma-separated string.

```
servers = [ 'test1',  'test2' ]
String to interpolate:  '${servers:json}'
Interpolation result:  '["test1", "test2"]'
```

**Lucene - Elasticsearch**

Formats variables with multiple values in Lucene format for
Elasticsearch.

```
servers = [ 'test1',  'test2' ]
String to interpolate:  '${servers:lucene}'
Interpolation result:  '("test1" OR "test2")'
```

**Percentencode**

Formats single and multivalued variables for use in URL parameters.

```
servers = [ 'foo()bar BAZ',  'test2' ]
String to interpolate:  '${servers:percentencode}'
Interpolation result:  'foo%28%29bar%20BAZ%2Ctest2'
```

**Pipe**

Formats variables with multiple values into a pipe-separated
string.

```
servers = [ 'test1.',  'test2' ]
String to interpolate:  '${servers:pipe}'
Interpolation result:  'test1.|test2'
```

**Raw**

Turns off data source-specific formatting, such as single quotes in an SQL
query.

```
servers = [ 'test.1',  'test2' ]
String to interpolate:  '${var_name:raw}'
Interpolation result:  'test.1,test2'
```

**Regex**

Formats variables with multiple values into a regex string.

```
servers = [ 'test1.',  'test2' ]
String to interpolate:  '${servers:regex}'
Interpolation result:  '(test1\.|test2)'
```

**Singlequote**

Formats single- and multi-valued variables into a comma-separated string,
escapes `'` in each value by
`\'` and quotes each value with
`'`.

```
servers = [ 'test1',  'test2' ]
String to interpolate:  '${servers:singlequote}'
Interpolation result:  "'test1','test2'"
```

**Sqlstring**

Formats single- and multi-valued variables into a comma-separated string,
escapes `'` in each value by
`''` and quotes each value with
`'`.

```
servers = [ "test'1",  "test2" ]
String to interpolate:  '${servers:sqlstring}'
Interpolation result:  "'test''1','test2'"
```

**Text**

Formats single- and multi-valued variables into their text representation. For a
single variable, it will just return the text representation. For multi-valued
variables, it will return the text representation combined with
`+`.

```
servers = [ "test1",  "test2" ]
String to interpolate:  '${servers:text}'
Interpolation result:  "test1 + test2"
```

**Query parameters**

Formats single- and multi-valued variables into their query parameter
representation. Example:
`var-foo=value1&var-foo=value2`

```
servers = [ "test1",  "test2" ]
String to interpolate:  '${servers:queryparam}'
Interpolation result:  "var-servers=test1&var-servers=test2"
```
