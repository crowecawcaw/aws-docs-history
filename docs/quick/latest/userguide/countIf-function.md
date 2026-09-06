

# countIf
<a name="countIf-function"></a>

Based on a conditional statement, the `countIf` function calculates the number of values in a dimension or measure, grouped by the chosen dimension or dimensions.

## Syntax
<a name="countIf-function-syntax"></a>

```
countIf(dimension or measure, condition)
```

## Arguments
<a name="countIf-function-arguments"></a>

 *dimension or measure*   
The argument must be a measure or a dimension. Null values are omitted from the results. Literal values don't work. The argument must be a field.

 *condition*   
One or more conditions in a single statement.

## Return type
<a name="countIf-function-return-type"></a>

Integer

## Example
<a name="countIf-function-example"></a>

The following function returns a count of the sales transactions (`Revenue`) that meet the conditions, including any duplicates. 

```
countIf (
    Revenue,
    # Conditions
        CalendarDay >= ${BasePeriodStartDate} AND 
        CalendarDay <= ${BasePeriodEndDate} AND 
        SourcingType <> 'Indirect'
)
```