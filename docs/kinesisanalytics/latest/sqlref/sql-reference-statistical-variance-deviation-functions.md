

# Statistical Variance and Deviation Functions
<a name="sql-reference-statistical-variance-deviation-functions"></a>

Each of these functions takes a set of numbers, ignores nulls, and can be used as either an aggregate function or an analytical function. For more information, see [Aggregate Functions](sql-reference-aggregate-functions.md) and [Analytic Functions](sql-reference-analytic-functions.md).

The relationships among these functions are described in the following table.


| Function purpose | Function name | Formula | Comments | 
| --- | --- | --- | --- | 
| Hotspots | [HOTSPOTS](sqlrf-hotspots.md) (expr) | Detects hotspots of frequently occurring data in the data stream. |  | 
| Random Cut Forest | [RANDOM\_CUT\_FOREST](sqlrf-random-cut-forest.md) (expr) | Detects anomalies in the data stream. |  | 
| Random Cut Forest with Explanation | [RANDOM\_CUT\_FOREST\_WITH\_EXPLANATION](sqlrf-random-cut-forest-with-explanation.md) (expr) | Detects anomalies in the data stream, and returns an attribution score based on how anomalous the data in each column is. |  | 
| Population variance | [VAR\_POP](sql-reference-VARPOP.md)(expr) | ( SUM(expr\*expr) - SUM(expr)\*SUM(expr) / COUNT(expr)) / COUNT(expr) | Applied to an empty set, it returns null. | 
| Population standard deviation | [STDDEV\_POP](sql-reference-STDDEVPOP.md) | Square root of the population variance (VAR\_POP). | When VAR\_POP returns null, STDDEV\_POP returns null. | 
| Sample variance | [VAR\_SAMP](sql-reference-VARSAMP.md) | (SUM(expr\*expr) - SUM(expr)\*SUM(expr) / COUNT(expr)) / (COUNT(expr)−1) | Applied to an empty set, it returns null.<br /><br />Applied to an input set of one element, VAR\_SAMP returns null. | 
| Sample standard deviation | [STDDEV\_SAMP](sql-reference-STDDEVSAMP.md) (expr) | Square root of the sample variance (VAR\_SAMP). | Applied to only 1 row of input data, STDDEV\_SAMP returns null. | 