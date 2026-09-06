

# Supported data types for Iceberg tables in Athena
<a name="querying-iceberg-supported-data-types"></a>

Athena can query Iceberg tables that contain the following data types:

```
binary
boolean
date
decimal
double
float
int
list
long
map
string
struct
timestamp without time zone
```

For more information about Iceberg table types, see the [schemas page for Iceberg](https://iceberg.apache.org/docs/latest/schemas/) in the Apache documentation.

The following table shows the relationship between Athena data types and Iceberg table data types.



<table>
<thead>
  <tr><th>Iceberg type</th><th>Athena type</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td><code>boolean</code></td><td><code>boolean</code></td><td></td></tr>
  <tr><td>-</td><td><code>tinyint</code></td><td>Not supported for Iceberg tables in Athena.</td></tr>
  <tr><td>-</td><td><code>smallint</code></td><td>Not supported for Iceberg tables in Athena.</td></tr>
  <tr><td><code>int</code></td><td><code>int</code></td><td>In Athena DML statements, this type is <code>INTEGER</code>.</td></tr>
  <tr><td><code>long</code></td><td><code>bigint</code></td><td></td></tr>
  <tr><td><code>double</code></td><td><code>double</code></td><td></td></tr>
  <tr><td><code>float</code></td><td><code>float</code></td><td></td></tr>
  <tr><td><code>decimal(P, S)</code></td><td><code>decimal(P, S)</code></td><td><code>P</code> is precision, <code>S</code> is scale.</td></tr>
  <tr><td>-</td><td><code>char</code></td><td>Not supported for Iceberg tables in Athena.</td></tr>
  <tr><td><code>string</code></td><td><code>string</code></td><td>In Athena DML statements, this type is <code>VARCHAR</code>.</td></tr>
  <tr><td><code>binary</code></td><td><code>binary</code></td><td></td></tr>
  <tr><td><code>date</code></td><td><code>date</code></td><td></td></tr>
  <tr><td><code>time</code></td><td>-</td><td rowspan="3">Only Iceberg timestamp (without time zone) is supported for Athena Iceberg DDL statements like <code>CREATE TABLE</code>, but all timestamp types can be queried through Athena.</td></tr>
  <tr><td><code>timestamp</code></td><td><code>timestamp</code></td></tr>
  <tr><td><code>timestamptz</code></td><td><code>timestamptz</code></td></tr>
  <tr><td><code>list&lt;E&gt;</code></td><td><code>array</code></td><td></td></tr>
  <tr><td><code>map&lt;K,V&gt;</code></td><td><code>map</code></td><td></td></tr>
  <tr><td><code>struct&lt;...&gt;</code></td><td><code>struct</code></td><td></td></tr>
  <tr><td><code>fixed(L)</code></td><td>-</td><td>The <code>fixed(L)</code> type is not currently supported in Athena.</td></tr>
</tbody>
</table>


For more information about data types in Athena, see [Data types in Amazon Athena](data-types.md).