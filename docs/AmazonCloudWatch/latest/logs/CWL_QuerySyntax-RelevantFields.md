

# relevantfields
<a name="CWL_QuerySyntax-RelevantFields"></a>

Use `relevantfields` to automatically identify which fields in your log data are most relevant to a given condition. The command compares the baseline logs against the subset matching your condition, and returns fields ranked by their relevance score.

**Syntax**

```
relevantfields [{{field1}}, {{field2}}, ...] where {{condition}}
```

The field list is optional. If omitted, all fields are analyzed.

The command returns the following output fields:
+ `@fieldName` — Name of the field
+ `@relevanceScore` — A score indicating relevancy on a scale of 0 to 1
+ `@topRelevanceContributors` — For categorical fields, shows entries with the highest shifts in frequency.
+ `@conditionalMedian` — For numerical fields, the median of values in logs that meet the condition
+ `@baselineMedian` — For numerical fields, the median of values in logs that do not meet the condition

**Examples**

**Analyze all fields for slow API responses**

```
relevantfields where Time > 400
```

**Focus analysis on specific fields**

```
relevantfields Controller, Path, Service where Time > 400
```

**Identify drivers of Lambda timeouts**

```
relevantfields where Duration > 5000
```