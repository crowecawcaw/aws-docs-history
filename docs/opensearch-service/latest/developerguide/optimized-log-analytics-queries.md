

# Supported query languages
<a name="optimized-log-analytics-queries"></a>

The Optimized engine supports PPL (Piped Processing Language) and SQL as query languages. The Optimized engine runs both PPL and SQL natively through its vectorized execution engine. For complete syntax references, see the [OpenSearch SQL and PPL documentation](https://docs.opensearch.org/latest/sql-and-ppl/) on the OpenSearch website.

## PPL support
<a name="optimized-log-analytics-ppl"></a>

The Optimized engine runs PPL (Piped Processing Language) natively. PPL is the primary query language in OpenSearch UI and is used by plugins such as Alerting and Anomaly Detection. For complete PPL syntax, see the [OpenSearch PPL reference](https://docs.opensearch.org/latest/search-plugins/sql/ppl/index/) on the OpenSearch website.

### Supported PPL commands
<a name="optimized-log-analytics-ppl-commands"></a>

The following PPL commands are supported on the Optimized engine:


| Category | Commands | 
| --- | --- | 
| Filter and project | where, fields, table | 
| Order | sort, reverse | 
| Limit | head | 
| Top-N | top, rare | 
| Compute | eval | 
| Aggregate | stats, eventstats, addtotals, addcoltotals | 
| Dedup | dedup | 
| Rename | rename | 
| Text | replace | 
| Format | fieldformat | 
| Null handling | fillnull | 
| Parse | parse, rex, grok, regex, patterns, spath | 
| Bucketing | bin, chart, timechart | 
| Join | join, streamstats, lookup | 
| Combine | append, appendcol, appendpipe, multisearch, union | 
| Subquery | in subquery, scalar subquery | 

### Supported PPL functions
<a name="optimized-log-analytics-ppl-functions"></a>

The Optimized engine supports functions across the following families:
+ String: `upper`, `lower`, `length`, `concat`, `substring`, `trim`, `replace`, `reverse`, `left`, `right`, and more
+ Math: `abs`, `ceil`, `floor`, `round`, `sqrt`, `pow`, `log`, `exp`, trigonometric functions, and more
+ Date and time: `now`, `date`, `year`, `month`, `day`, `date_add`, `datediff`, `date_format`, and more
+ Condition: `if`, `ifnull`, `nullif`, `isnull`, `coalesce`, `case`
+ Type conversion: `cast`, `tostring`, `tonumber`
+ Aggregate: `count`, `sum`, `avg`, `min`, `max`, `percentile`, `stddev_pop`, `distinct_count`, and more
+ Relevance and full-text: `match`, `match_phrase`, `multi_match`, `query_string`
+ JSON: `json_object`, `json_extract`, `json_keys`, `json_array`
+ Collection and array: `array`, `array_length`, `mvjoin`, `split`, `mvzip`, `mvdedup`

### The search command
<a name="optimized-log-analytics-ppl-search"></a>

The `search` command has partial support on the Optimized engine. It works for text-based matching but does not support numeric, date, or IP field comparisons.


| Feature | Status | 
| --- | --- | 
| Free-text term search | Supported | 
| Phrase search | Supported | 
| String field equality (=, \!=) | Supported | 
| String field IN(...) | Supported | 
| Boolean operators over string predicates | Supported | 
| Numeric field comparison or range | Not supported. Use where instead. | 
| Date field comparison or range | Not supported. Use where instead. | 
| Wildcard patterns | Not supported | 

**Tip**  
Use the `where` command instead of inline `search` filters for non-text fields. The `where` command executes through the native analytics engine for acceleration, while `search` filters on numeric, date, or IP fields return zero rows.  

```
// Instead of: search source=logs Age > 50
// Use:
search source=logs | where Age > 50
```

### Unsupported PPL commands
<a name="optimized-log-analytics-ppl-unsupported"></a>

The following PPL commands are not supported on the Optimized engine:

`convert`, `expand`, `flatten`, `mvexpand`, `mvcombine`, `nomv`, `graphlookup`, `trendline`, `describe`, `explain`

Higher-order array functions (`transform`, `mvmap`, `reduce`, `forall`, `exists`, `filter`) are not supported.

### Example
<a name="optimized-log-analytics-ppl-example"></a>

The following PPL query combines full-text search with aggregation in a single statement:

```
search source=logs "connection refused"
| where status_code = 503
| stats count() by host, status_code
| sort - count
```

**Tip**  
For distributed grouped top-N queries, you can tune the accuracy and performance trade-off. See [Tune accuracy for distributed top-N queries](optimized-log-analytics-bp.md#optimized-log-analytics-bp-topn).

## SQL support
<a name="optimized-log-analytics-sql"></a>

You can use SQL on the Optimized engine through the REST API, JDBC/ODBC drivers, and Query Workbench. Use SQL for BI tools such as Grafana, Tableau, and Amazon QuickSight. For complete SQL syntax, see the [OpenSearch SQL reference](https://docs.opensearch.org/latest/search-plugins/sql/sql/index/) on the OpenSearch website.

### Supported SQL statements
<a name="optimized-log-analytics-sql-statements"></a>

The Optimized engine supports the following SQL statement categories:
+ `SELECT` (including expressions, `DISTINCT`, aliases, and literals)
+ `WHERE` (`IN`, `BETWEEN`, `AND`/`OR`, `NOT`, `IS NULL`)
+ `ORDER BY`
+ `LIMIT` and `OFFSET`
+ `GROUP BY`
+ `HAVING`
+ `CASE`
+ `LIKE` and `REGEXP`
+ `JOIN` (`INNER`, `LEFT`, `RIGHT`, `CROSS`)
+ Subqueries (in `WHERE`, `FROM`, and `EXISTS`)
+ `UNION ALL`
+ `EXPLAIN`
+ `SHOW` and `DESCRIBE`

### Supported SQL functions
<a name="optimized-log-analytics-sql-functions"></a>

The Optimized engine supports functions across the following families:


| Family | Functions (representative) | 
| --- | --- | 
| String | UPPER, LOWER, LENGTH, CONCAT, SUBSTRING, TRIM, REPLACE, LEFT, RIGHT, LOCATE, REVERSE, ASCII, CONCAT\_WS, STRCMP, POSITION | 
| Math | ABS, CEIL, FLOOR, ROUND, MOD, SQRT, POW, LOG, LOG2, LOG10, EXP, SIGN, TRUNCATE, RAND, trigonometric functions, CONV, CRC32 | 
| Date and time | NOW, CURDATE, DATE, YEAR, MONTH, DAY, DATE\_ADD, DATE\_SUB, DATEDIFF, TIMESTAMPDIFF, DATE\_FORMAT, UNIX\_TIMESTAMP, CONVERT\_TZ, and 40\+ additional datetime functions | 
| Conditional | IF, IFNULL, NULLIF, ISNULL | 
| Type conversion | CAST (INT, DOUBLE, STRING, DATE), TYPEOF | 
| Aggregate | COUNT, SUM, AVG, MIN, MAX, COUNT(DISTINCT), STDDEV\_POP, STDDEV\_SAMP, VAR\_POP, VAR\_SAMP, PERCENTILE, PERCENTILE\_APPROX | 
| Relevance and full-text | MATCH, MATCH\_PHRASE, MULTI\_MATCH, QUERY\_STRING, SIMPLE\_QUERY\_STRING, MATCH\_BOOL\_PREFIX, MATCH\_PHRASE\_PREFIX, WILDCARD\_QUERY | 
| Window | ROW\_NUMBER | 

### Unsupported SQL features
<a name="optimized-log-analytics-sql-gaps"></a>

The following SQL features are not supported on the Optimized engine:


| Feature | Workaround | 
| --- | --- | 
| UNION (distinct) | Use UNION ALL instead | 
| MINUS | No workaround available | 
| Filtered aggregate (FILTER (WHERE ...)) | Use SUM(CASE WHEN ... THEN ... END) instead | 
| RANK window function | No workaround available | 
| DENSE\_RANK window function | No workaround available | 

### Example
<a name="optimized-log-analytics-sql-example"></a>

The following SQL query combines full-text search with aggregation to find and count log entries by service:

```
SELECT service, region, COUNT(*) AS hits
FROM logs
WHERE MATCH(body, 'connection timeout')
GROUP BY service, region
ORDER BY hits DESC
```