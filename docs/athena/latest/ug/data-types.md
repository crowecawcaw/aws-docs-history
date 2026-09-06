

# Data types in Amazon Athena
<a name="data-types"></a>

When you run `CREATE TABLE`, you specify column names and the data type that each column can contain. The tables that you create are stored in the AWS Glue Data Catalog. 

To facilitate interoperability with other query engines, Athena uses [Apache Hive](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types) data type names for DDL statements like `CREATE TABLE`. For DML queries like `SELECT`, `CTAS`, and `INSERT INTO`, Athena uses [Trino](https://trino.io/docs/current/language/types.html) data type names. The following table shows the data types supported in Athena. Where DDL and DML types differ in terms of name, availability, or syntax, they are shown in separate columns.



<table>
<thead>
  <tr><th>DDL</th><th>DML</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="2">BOOLEAN</td><td>Values are <code>true</code> and <code>false</code>.</td></tr>
  <tr><td colspan="2">TINYINT</td><td>An 8-bit signed integer in two's complement format, with a minimum value of -27 and a maximum value of 27-1.</td></tr>
  <tr><td colspan="2">SMALLINT</td><td>A 16-bit signed integer in two's complement format, with a minimum value of -215 and a maximum value of 215-1.</td></tr>
  <tr><td colspan="2">INT, INTEGER</td><td>A 32-bit signed value in two's complement format, with a minimum value of -231 and a maximum value of 231-1.</td></tr>
  <tr><td colspan="2">BIGINT</td><td> A 64-bit signed integer in two's complement format, with a minimum value of -263 and a maximum value of 263-1.</td></tr>
  <tr><td>FLOAT</td><td>REAL</td><td>A 32-bit signed single-precision floating point number. The range is 1.40129846432481707e-45 to 3.40282346638528860e+38, positive or negative. Follows the IEEE Standard for Floating-Point Arithmetic (IEEE 754).</td></tr>
  <tr><td colspan="2">DOUBLE</td><td>A 64-bit signed double-precision floating point number. The range is 4.94065645841246544e-324d to 1.79769313486231570e+308d, positive or negative. Follows the IEEE Standard for Floating-Point Arithmetic (IEEE 754).</td></tr>
  <tr><td colspan="2">DECIMAL({{precision}}, {{scale}})</td><td><code>precision</code> is the total number of digits. <code>scale</code> (optional) is the number of digits in fractional part with a default of 0. For example, use these type definitions: <code>decimal(11,5)</code>, <code>decimal(15)</code>. The maximum value for {{precision}} is 38, and the maximum value for {{scale}} is 38.</td></tr>
  <tr><td colspan="2">CHAR, CHAR({{length}})</td><td>Fixed length character data, with a specified length between 1 and 255, such as char(10). If {{length}} is specified, strings are truncated at the specified length when read. If the underlying data string is longer, the underlying data string remains unchanged.<br />For more information, see <a href="https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes-char">CHAR Hive data type</a>.</td></tr>
  <tr><td>STRING</td><td>VARCHAR</td><td>Variable length character data.</td></tr>
  <tr><td colspan="2">VARCHAR({{length}})</td><td>Variable length character data with a maximum read length. Strings are truncated at the specified length when read. If the underlying data string is longer, the underlying data string remains unchanged.</td></tr>
  <tr><td>BINARY</td><td>VARBINARY</td><td>Variable length binary data.</td></tr>
  <tr><td>Not available</td><td>TIME</td><td>A time of day with millisecond precision.</td></tr>
  <tr><td>Not available</td><td>TIME({{precision}})</td><td>A time of day with a specific precision. <code>TIME(3)</code> is equivalent to <code>TIME</code>.</td></tr>
  <tr><td>Not available</td><td>TIME WITH TIME ZONE</td><td>A time of day in a time zone. Time zones should be specified as offsets from UTC.</td></tr>
  <tr><td colspan="2">DATE</td><td>A calendar date with year, month, and day.</td></tr>
  <tr><td>TIMESTAMP</td><td>TIMESTAMP, TIMESTAMP WITHOUT TIME ZONE</td><td>A calendar date and time of day with millisecond precision.</td></tr>
  <tr><td>Not available</td><td>TIMESTAMP({{precision}}), TIMESTAMP({{precision}}) WITHOUT TIME ZONE</td><td>A calendar date and time of day with a specific precision. <code>TIMESTAMP(3)</code> is equivalent to <code>TIMESTAMP</code>.</td></tr>
  <tr><td>Not available</td><td>TIMESTAMP WITH TIME ZONE</td><td>A calendar date and time of day in a time zone. Time zones can be specified as offsets from UTC, as IANA time zone names, or using UTC, UT, Z, or GMT.</td></tr>
  <tr><td>Not available</td><td>TIMESTAMP({{precision}}) WITH TIME ZONE</td><td>A calendar date and time of day with a specific precision, in a time zone.</td></tr>
  <tr><td>Not available</td><td>INTERVAL YEAR TO MONTH</td><td>An interval of one or more whole months</td></tr>
  <tr><td>Not available</td><td>INTERVAL DAY TO SECOND</td><td>An interval of one or more seconds, minutes, hours, or days</td></tr>
  <tr><td>ARRAY&lt;{{element_type}}&gt;</td><td>ARRAY[{{element_type}}]</td><td>An array of values. All values must be of the same data type.</td></tr>
  <tr><td>MAP&lt;{{key_type}}, {{value_type}}&gt;</td><td>MAP({{key_type}}, {{value_type}})</td><td>A map where values can be looked up by key. All keys must be of the same data type, and all values must be of the same data type. For example, <code>map&lt;string, integer&gt;</code>.</td></tr>
  <tr><td>STRUCT&lt;{{field_name_1}}:{{field_type_1}}, {{field_name_2}}:{{field_type_2}}, …&gt;</td><td>ROW({{field_name_1}} {{field_type_1}}, {{field_name_2}} {{field_type_2}}, …)</td><td>A data structure with named fields and their values.</td></tr>
  <tr><td>Not available</td><td>JSON</td><td>JSON value type, which can be a JSON object, a JSON array, a JSON number, a JSON string, <code>true</code>, <code>false</code> or <code>null</code>.</td></tr>
  <tr><td>Not available</td><td>UUID</td><td>A UUID (Universally Unique IDentifier).</td></tr>
  <tr><td>Not available</td><td>IPADDRESS</td><td>An IPv4 or IPv6 address.</td></tr>
  <tr><td rowspan="5">Not available</td><td><a href="https://trino.io/docs/current/language/types.html#hyperloglog-type">HyperLogLog</a></td><td rowspan="5">These data types support approximate function internals. For more information about each type, visit the link to the corresponding entry in the Trino documentation.</td></tr>
  <tr><td><a href="https://trino.io/docs/current/language/types.html#p4hyperloglog">P4HyperLogLog</a></td></tr>
  <tr><td><a href="https://trino.io/docs/current/language/types.html#setdigest">SetDigest</a></td></tr>
  <tr><td><a href="https://trino.io/docs/current/language/types.html#quantile-digest">QDigest</a></td></tr>
  <tr><td><a href="https://trino.io/docs/current/language/types.html#t-digest">TDigest</a></td></tr>
</tbody>
</table>


**Topics**
+ [Data type examples](data-types-examples.md)
+ [Considerations for data types](data-types-considerations.md)
+ [Work with timestamp data](data-types-timestamps.md)