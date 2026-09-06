

# stdevp
<a name="stdevp-function"></a>

The `stdevp` function calculates the population standard deviation of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions.

## Syntax
<a name="stdevp-function-syntax"></a>

```
stdevp(measure, [group-by level])
```

## Arguments
<a name="stdevp-function-arguments"></a>

 *measure*   
The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field.

 *group-by level*   
(Optional) Specifies the level to group the aggregation by. The level added can be any dimension or dimensions independent of the dimensions added to the visual.  
The argument must be a dimension field. The group-by level must be enclosed in square brackets `[ ]`. For more information, see [Level-aware calculation - aggregate (LAC-A) functions](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations-aggregate.html).

## Examples
<a name="stdev-function-example"></a>

The following example returns the standard deviation of test scores for a class using all the scores recorded.

```
stdevp({Score})
```

You can also specify at what level to group the computation using one or more dimensions in the view or in your dataset. This is called a LAC-A function. For more information about LAC-A functions, see [Level-aware calculation - aggregate (LAC-A) functions](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations-aggregate.html). The following example calculates the standard deviation of test scores at the subject level, but not across other dimensions (Class) in the visual using all the scores recorded.

```
stdevp({Score}, [Subject])
```