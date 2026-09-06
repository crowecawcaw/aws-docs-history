

# firstValue
<a name="firstValue-function"></a>

The `firstValue` function calculates the first value of the aggregated measure or dimension partitioned and sorted by specified attributes.

## Syntax
<a name="firstValue-function-syntax"></a>

The brackets are required. To see which arguments are optional, see the following descriptions.

```
firstValue
	(
	     {{aggregated measure or dimension}}, 
	     {{[ sort_attribute ASC_or_DESC, ... ]}},
	     {{[ partition_by_attribute, ... ]}} 
	)
```

## Arguments
<a name="firstValue-function-arguments"></a>

*aggregated measure or dimension*   
An aggregated measure or dimension that you want to see the first value for.

*sort attribute*   
One or more aggregated fields, either measures or dimensions or both, that you want to sort the data by, separated by commas. You can either specify ascending (**ASC**) or descending (**DESC**) sort order.   
Each field in the list is enclosed in {} (curly braces), if it's more than one word. The entire list is enclosed in [ ] (square brackets).

*partition by attribute*  
(Optional) One or more measure or dimensions that you want to partition by, separated by commas.  
Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets). 

## Example
<a name="firstValue-function-example"></a>

The following example calculates the first `Destination Airport`, sorted by `Flight Date`, partitioned by `Flight Date` ascending and `Origin Airport`.

```
firstValue(
    {Destination Airport}
    [{Flight Date} ASC],
    [
        {Origin Airport},
        {Flight Date}
    ]
)
```