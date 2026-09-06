

# GROUP\_BY
<a name="recipe-actions.GROUP_BY"></a>

Summarizes the data by grouping rows by one or more columns, and then applying an aggregation function to each group. 

**Parameters**
+ `sourceColumns` — A JSON-encoded string representing a list of columns that form the basis of each group.
+ `groupByAggFunctions` — A JSON-encoded string representing a list of aggregation function to apply. (If you don't want aggregation, specify `UNAGGREGATED`.)
+ `useNewDataFrame` — If true, the results from GROUP\_BY are made available in the project session, replacing its current contents.

**Example**  
  

```
[
  {
    "Action": {
      "Operation": "GROUP_BY",
      "Parameters": {
        "groupByAggFunctionOptions": "[{\"sourceColumnName\":\"all_votes\",\"targetColumnName\":\"all_votes_count\",\"targetColumnDataType\":\"number\",\"functionName\":\"COUNT\"}]",
        "sourceColumns": "[\"year\",\"state_name\"]",
        "useNewDataFrame": "true"
      }
    }
  }
]
```