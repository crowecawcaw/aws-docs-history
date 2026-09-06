

# MASK\_DATE
<a name="recipe-actions.MASK_DATE"></a>

Masks components of a date with a user-specified mask symbol.

**Parameters**
+ `sourceColumns` – A list of existing column names.
+ `maskSymbol` – A symbol that will be used to replace specified characters.
+ `redact` – An array of date component enums to mask. Valid enum values: YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, MILLISECOND.
+ `locale` – Optional IETF BCP 47 language tag. Defaults to `en`. The locale to use for date formatting.

**Example**  
  

```
// Mask year
{ 
    "RecipeAction": {
        "Operation": "MASK_DATE",
        "Parameters": {
            "sourceColumns": ["birthday"],
            "maskSymbol": "#",
            "redact": ["YEAR"]
        }
    }
}
```