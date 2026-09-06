

# Available checks
<a name="profile.data-quality-available-checks"></a>

The following table lists references for all available conditions that can be used in your rules. Note that aggregated conditions cannot be combined with non-aggregated conditions in the same rule. 

**Note**  
For SDK users, to apply the same rule to multiple columns use the [ColumnSelectors](https://docs.aws.amazon.com/databrew/latest/APIReference/API_ColumnSelector.html) attribute of a [Rule](https://docs.aws.amazon.com/databrew/latest/APIReference/API_Rule.html) and specify validated columns using either their names or a regular expression. In this case, you should use implicit *CheckExpression*. For example, `“> :val”` to compare values in each of the selected columns with the provided value. DataBrew uses implicit syntax for defining [FilterExpression](https://docs.aws.amazon.com/databrew/latest/APIReference/API_FilterExpression.html) in dynamic datasets. If you want to specify column(s) for each check individually, don't set the *ColumnSelectors* attribute. Instead, provide an explicit expression. For example, `“:col > :val”` as a *CheckExpression* in a *Rule*.




- **Aggregate dataset conditions**
  - **Data quality check:** Number of rows / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(ROWS_COUNT) > :val", "SubstitutionMap": {":val", "10000"}`
  - **Data quality check:** Number of columns / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(COLUMNS_COUNT) == :val", "SubstitutionMap": {":val", "20"}`
  - **Data quality check:** Duplicate rows / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(DUPLICATE_ROWS_COUNT) < :val", "SubstitutionMap": {":val", "100"}`<br />or<br />`"CheckExpression": "AGG(DUPLICATE_ROWS_PERCENTAGE) < :val", "SubstitutionMap": {":val", "5"} `

- **Aggregate column statistics conditions**
  - **Data quality check:** Missing values / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(MISSING_VALUES_COUNT) < :val", "SubstitutionMap": {":val", "100"}`<br />or<br />`"CheckExpression": "AGG(MISSING_VALUES_PERCENTAGE) < :val", "SubstitutionMap": {":val", "5"} `
  - **Data quality check:** Duplicate values / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(DUPLICATE_VALUES_COUNT) < :val", "SubstitutionMap": {":val", "100"}`<br />or<br />`"CheckExpression": "AGG(DUPLICATE_VALUES_PERCENTAGE) < :val", "SubstitutionMap": {":val", "5"} `
  - **Data quality check:** Valid values / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(VALID_VALUES_COUNT) > :val", "SubstitutionMap": {":val", "10000"}`<br />or<br />`"CheckExpression": "AGG(VALID_VALUES_PERCENTAGE) > :val", "SubstitutionMap": {":val", "95"} `
  - **Data quality check:** Distinct values / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(DISTINCT_VALUES_COUNT) > :val", "SubstitutionMap": {":val", "1000"}`<br /> or <br />`"CheckExpression": "AGG(DISTINCT_VALUES_PERCENTAGE) >= :val", "SubstitutionMap": {":val", "50"} `
  - **Data quality check:** Unique values / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(UNIQUE_VALUES_COUNT) > :val", "SubstitutionMap": {":val", "100"}`<br />or<br />`"CheckExpression": "AGG(UNIQUE_VALUES_PERCENTAGE) > :val", "SubstitutionMap": {":val", "20"} `
  - **Data quality check:** Outliers / **Additional parameters:** Z-score threshold / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(Z_SCORE_OUTLIERS_COUNT, :zscore_dev) < :val", "SubstitutionMap": {":zscore_dev": "4", ":val", "100"}`<br /> or <br />` "CheckExpression": "AGG(Z_SCORE_OUTLIERS_PERCENTAGE) < :val", "SubstitutionMap": {":val", "5"} `
  - **Data quality check:** Value distribution statistics / **Additional parameters:** Statistics name (see next table) / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(<STAT_NAME>) < :val", "SubstitutionMap": {":val", "100"}`<br /> or <br />`"CheckExpression": "AGG(<STAT_NAME>, :param) < :val", "SubstitutionMap": {":param": "0.25", :val", "5"}` See next table for possible `STAT_NAME` values
  - **Data quality check:** Numerical statistics / **Additional parameters:** Statistics name (see next table) / **Comparison type:** Numeric comparison against custom value / **SDK syntax example:** `"CheckExpression": "AGG(<STAT_NAME>) < :val", "SubstitutionMap": {":val", "100"}`<br /> or <br />`"CheckExpression": "AGG(<STAT_NAME>, :param) < :val", "SubstitutionMap": {":param": "0.25", :val", "5"}` See next table for possible `STAT_NAME` values

- **Non aggregate (accepts threshold)**
  - **Data quality check:** Value is exactly / **Additional parameters:**  / **Comparison type:** Exact comparison against a list of values / **SDK syntax example:** `"CheckExpression": ":col IN :list", "SubstitutionMap": {":col": "`size`", ":list": "[\"S\",\"M\",\"L\",\"XL\"]"}`
  - **Data quality check:** Value is not exactly / **Additional parameters:**  / **Comparison type:** Value shouldn't exactly match any value from a list / **SDK syntax example:** `"CheckExpression": ":col NOT IN :list", "SubstitutionMap": {":col": "`domain`", ":list": "[\"GOV\",\"ORG\"]"}`
  - **Data quality check:** String values / **Additional parameters:**  / **Comparison type:** String comparison against custom value or other string column / **SDK syntax example:** `"CheckExpression": ":col STARTS_WITH :val", "SubstitutionMap": {":col": "`url`", ":val": "http"}`<br /> or <br />`"CheckExpression": ":col1 contains :col2", "SubstitutionMap": {":col1": "`url`", ":col2": "`company_name`"} `
  - **Data quality check:** Numeric values / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value or other numeric column  / **SDK syntax example:** `"CheckExpression": ":col IS_BETWEEN :val1 and :val2", "SubstitutionMap": {":col": "`APY`", ":val1": "0", ":val2": "10"}`<br /> or <br />`"CheckExpression": ":col1 <= :col2", "SubstitutionMap": {":col1": "`bank_rate`", ":col2": "`fed_rate`"} `
  - **Data quality check:** Value string length / **Additional parameters:**  / **Comparison type:** Numeric comparison against custom value or other numeric column  / **SDK syntax example:** `"CheckExpression": "length(:col) IS_BETWEEN :val1 and :val2", "SubstitutionMap": {":col": "`identifier`", ":val1": "8", ":val2": "12"}`<br /> or<br />` "CheckExpression": "length(:col1) <= :col2", "SubstitutionMap": {":col1": "`name`", ":col2": "`max_name_len`"} `



**Numeric comparisons**

DataBrew supports the following operations for numeric comparison: *Is equals (==)*, *Is not equals (\!=)*, *Less than (<)*, *Less than equals (<=)*, *Greater than (>)*, *Greater than equals (>=)* and *Is between (is\_between :val1 and :val2)*.

**String comparisons**

The following string comparisons are supported: *Starts with*, *Doesn’t start with*, *Ends with*, *Doesn’t end with*, *Contains*, *Doesn’t contain*, *Is equals*, *Is not equals*, *Matches*, *Doesn’t match*. 

The following table displays available statistics that you can use for Value distribution statistics and Numerical statistics:




- **Value distribution statistics**
  - **Statistics name:** Min / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(MAX) < :val", "SubstitutionMap": {":val", "100"}  
  - **Statistics name:** Max / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(MIN) > :val", "SubstitutionMap": {":val", "0"} 
  - **Statistics name:** Median / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(MEDIAN) >= :val", "SubstitutionMap": {":val", "50"} 
  - **Statistics name:** Mean / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(MEAN) <= :val", "SubstitutionMap": {":val", "10"} 
  - **Statistics name:** Mode / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(MODE) > :val", "SubstitutionMap": {":val", "0"}  
  - **Statistics name:** Standard deviation / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(STANDARD\_DEVIATION) > :val", "SubstitutionMap": {":val", "0"} 
  - **Statistics name:** Entropy / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(ENTROPY) > :val", "SubstitutionMap": {":val", "0"}  

- **Numerical statistics**
  - **Statistics name:** Sum / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(SUM) > :val", "SubstitutionMap": {":val", "0"} 
  - **Statistics name:** Kurtosis / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(KURTOSIS) > :val", "SubstitutionMap": {":val", "0"}  
  - **Statistics name:** Skewness / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(SKEWNESS) > :val", "SubstitutionMap": {":val", "0"}  
  - **Statistics name:** Variance / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(VARIANCE) > :val", "SubstitutionMap": {":val", "0"}  
  - **Statistics name:** Absolute deviation / **Additional parameters:**  / **SDK syntax:** "CheckExpression": "AGG(MEDIAN\_ABSOLUTE\_DEVIATION) > :val", "SubstitutionMap": {":val", "0"}  
  - **Statistics name:** Quantile / **Additional parameters:** Quantile: one of '0.25', '0.5', '0.75' / **SDK syntax:** "CheckExpression": "AGG(QUANTILE, :pct) > :val", "SubstitutionMap": {":pct": "0.25", ":val", "0"}  

