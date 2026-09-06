

# SQL capabilities for minimum aggregation and comparison controls
<a name="custom-sql-capabilities"></a>

The following table lists the supported and unsupported SQL constructs and functions when a custom analysis rule uses minimum aggregation thresholds and comparison controls in the Spark analytics engine. Function categories follow the AWS Clean Rooms Spark SQL reference.


| Category | SQL construct | Supported | Common table expressions (CTEs) | Final SELECT clause | 
| --- |--- |--- |--- |--- |
| Query constructs |  + CACHE TABLE<br />+ Query hints<br />+ Analysis template (parameterized queries)  | Yes | Supported | Supported | 
| Clauses |  + SELECT<br />+ SELECT DISTINCT<br />+ FROM<br />+ FROM SUBQUERY<br />+ FROM INLINE TABLE (VALUES)<br />+ WHERE<br />+ GROUP BY<br />+ HAVING<br />+ ORDER BY<br />+ WITH (CTE)  | Yes | Supported | Supported | 
|  + GROUP BY CUBE<br />+ GROUP BY ROLLUP<br />+ GROUP BY GROUPING SETS<br />+ EXISTS<br />+ CLUSTER BY<br />+ DISTRIBUTE BY<br />+ SORT BY<br />+ LATERAL JOIN<br />+ PIVOT / UNPIVOT<br />+ WITH RECURSIVE  | No | — | — | 
| Join clauses |  + JOIN INNER<br />+ JOIN LEFT<br />+ JOIN FULL OUTER<br />+ JOIN CROSS<br />+ JOIN RIGHT<br />+ JOIN NATURAL  | Yes | Supported | Supported | 
|  + JOIN LEFT SEMI<br />+ JOIN LEFT ANTI  | No | — | — | 
| Set operators |  + UNION<br />+ UNION ALL  | Yes | Supported | Supported | 
|  + EXCEPT<br />+ EXCEPT ALL<br />+ INTERSECT<br />+ INTERSECT ALL  | No | — | — | 
| Sort and row limits |  + ORDER BY ASC / DESC<br />+ ORDER BY NULLS FIRST<br />+ ORDER BY NULLS LAST<br />+ LIMIT  | Yes | Supported | Supported | 
|  + OFFSET  | No | — | — | 
| Conditions |  + =<br />+ \!= / <><br />+ <<br />+ <=<br />+ ><br />+ >=<br />+ IN<br />+ NOT IN<br />+ LIKE<br />+ NOT LIKE<br />+ RLIKE<br />+ BETWEEN<br />+ IS TRUE / IS FALSE<br />+ AND<br />+ OR<br />+ NOT<br />+ IS DISTINCT FROM  | Yes | Supported | Supported | 
|  + <=> (null-safe equality)  | No | — | — | 
| Aggregate functions |  + AVG function<br />+ COUNT function<br />+ COUNT DISTINCT function<br />+ SUM function<br />+ MIN function<br />+ MAX function<br />+ STDDEV / STDDEV\_SAMP functions<br />+ STDDEV\_POP function<br />+ VAR\_SAMP / VARIANCE functions<br />+ VAR\_POP function<br />+ SKEWNESS function<br />+ APPROX\_COUNT\_DISTINCT function<br />+ COLLECT\_LIST function<br />+ COLLECT\_SET function<br />+ PERCENTILE function<br />+ APPROX\_PERCENTILE function<br />+ MEDIAN function  | Yes | Supported | When an aggregation threshold is set: MIN, MAX, PERCENTILE, APPROX\_PERCENTILE, MEDIAN, COLLECT\_LIST, and COLLECT\_SET must be combined with a qualifying aggregation (AVG, COUNT, SUM). They cannot be used as a standalone aggregation.<br />When only comparison controls are set: no such restriction.<br />All other aggregate functions are supported. | 
|  + ANY\_VALUE function<br />+ BOOL\_AND function<br />+ BOOL\_OR function  | No | — | — | 
| Array functions |  + ARRAY function<br />+ ARRAY\_CONTAINS function<br />+ ARRAY\_DISTINCT function<br />+ ARRAY\_INTERSECT function<br />+ ARRAY\_JOIN function<br />+ ARRAY\_REMOVE function<br />+ ARRAY\_SORT function<br />+ ARRAY\_UNION function<br />+ FLATTEN function<br />+ EXPLODE function  | Yes | Supported | Supported | 
|  + ARRAY\_EXCEPT function  | No | — | — | 
| Conditional expressions |  + IS NULL function<br />+ IS NOT NULL function<br />+ GREATEST function<br />+ LEAST function<br />+ CASE / WHEN functions<br />+ IF function<br />+ COALESCE function<br />+ NULLIF function<br />+ NVL function<br />+ NVL2 function  | Yes | Supported | Supported | 
| Constructor functions |  + STRUCT function<br />+ NAMED\_STRUCT function<br />+ MAP function  | Yes | Supported | Supported | 
| Data type formatting functions |  + STR\_TO\_MAP function<br />+ BASE64 function<br />+ UNBASE64 function<br />+ HEX function<br />+ UNHEX function<br />+ TO\_DATE function<br />+ DECODE function<br />+ ENCODE function<br />+ CAST function  | Yes | Supported | Supported | 
|  + TO\_CHAR function<br />+ TO\_NUMBER function  | No | — | — | 
| Date and time functions |  + CURRENT\_DATE function<br />+ CURRENT\_TIMESTAMP function<br />+ TO\_TIMESTAMP function<br />+ DATE\_DIFF function<br />+ DATE\_TRUNC function<br />+ DATE\_PART function<br />+ EXTRACT function<br />+ CONVERT\_TIMEZONE function<br />+ FROM\_UTC\_TIMESTAMP function<br />+ TIMESTAMP function<br />+ DAY / DAYOFMONTH functions<br />+ DAYOFWEEK function<br />+ WEEKOFYEAR function<br />+ MONTH function<br />+ YEAR function<br />+ HOUR function<br />+ MINUTE function<br />+ SECOND function  | Yes | Supported | Supported | 
|  + DAYOFYEAR function<br />+ DATE\_ADD function<br />+ ADD\_MONTHS function  | No | — | — | 
| Hash functions |  + MD5 function<br />+ SHA function<br />+ SHA1 function<br />+ SHA2 function<br />+ XXHASH64 function  | Yes | Supported | Supported | 
| JSON functions |  + GET\_JSON\_OBJECT function<br />+ TO\_JSON function  | Yes | Supported | Supported | 
| Math functions |  + ABS function<br />+ CEIL / CEILING functions<br />+ FLOOR function<br />+ ROUND function<br />+ LN function<br />+ LOG / LOG10 functions<br />+ POWER function<br />+ SQRT function<br />+ RAND / RANDOM functions<br />+ EXP function<br />+ SIGN function<br />+ TRUNC function  | Yes | Supported | Supported | 
|  + TRUNCATE function<br />+ CBRT function<br />+ PI function<br />+ RADIANS function<br />+ ACOS function<br />+ ASIN function<br />+ ATAN function<br />+ ATAN2 function<br />+ COS function<br />+ COT function<br />+ SIN function<br />+ DEGREES function  | No | — | — | 
| Mathematical operator symbols |  + \+<br />+ -<br />+ \*<br />+ /<br />+ %  | Yes | Supported | Supported | 
| Scalar functions |  + CARDINALITY function<br />+ SIZE function  | Yes | Supported | Supported | 
| String functions |  + CONCAT function<br />+ LOWER function<br />+ UPPER function<br />+ LENGTH / CHAR\_LENGTH / CHARACTER\_LENGTH functions<br />+ SUBSTR / SUBSTRING functions<br />+ TRIM function<br />+ BTRIM function<br />+ LTRIM function<br />+ RTRIM function<br />+ POSITION function<br />+ REPLACE function<br />+ REPEAT function<br />+ REGEXP\_REPLACE function<br />+ REGEXP\_SUBSTR function<br />+ SPLIT function<br />+ FORMAT\_STRING function<br />+ UUID function<br />+ LPAD function<br />+ RPAD function<br />+ LEFT function<br />+ RIGHT function  | Yes | Supported | Supported | 
|  + REVERSE function<br />+ TRANSLATE function<br />+ REGEXP\_COUNT function<br />+ REGEXP\_INSTR function<br />+ SPLIT\_PART function  | No | — | — | 
| Privacy-related functions |  + consent\_tcf\_v2\_decode function<br />+ consent\_gpp\_v1\_decode function  | Yes | Supported | Supported | 
| Window functions |  + ROW\_NUMBER function<br />+ RANK function<br />+ DENSE\_RANK function<br />+ LAG function<br />+ LEAD function<br />+ Window AVG function<br />+ Window COUNT function<br />+ Window SUM function<br />+ Window MIN function<br />+ Window MAX function<br />+ Window STDDEV\_POP function<br />+ Window STDDEV\_SAMP function<br />+ Window VAR\_POP function<br />+ Window VAR\_SAMP function<br />+ Window SKEWNESS function<br />+ Window APPROX\_COUNT\_DISTINCT function<br />+ Window APPROX\_PERCENTILE function<br />+ Window PERCENTILE function  | Yes | Supported | When an aggregation threshold is set: LAG, LEAD, Window MIN, Window MAX, Window APPROX\_PERCENTILE, and Window PERCENTILE must be combined with a qualifying aggregation. They cannot be used as a standalone value.<br />When only comparison controls are set: no such restriction.<br />All other window functions are supported. | 
|  + FIRST / FIRST\_VALUE functions<br />+ LAST / LAST\_VALUE functions<br />+ NTH\_VALUE function<br />+ CUME\_DIST function<br />+ PERCENT\_RANK function<br />+ NTILE function  | No | — | — | 
| Encryption and decryption functions |  + AES\_ENCRYPT function<br />+ AES\_DECRYPT function  | No | — | — | 
| Hyperloglog functions |  + HLL\_SKETCH\_AGG function<br />+ HLL\_UNION\_AGG function<br />+ HLL\_SKETCH\_ESTIMATE function<br />+ HLL\_UNION function  | No | — | — | 