

# MASK\_CUSTOM
<a name="recipe-actions.MASK_CUSTOM"></a>

Masks characters that match a provided custom value.

**Parameters**
+ `sourceColumns` – A list of existing column names.
+ `maskSymbol` – A symbol that will be used to replace specified characters.
+ `regex` – If true, treats `customValue` as a regex pattern to match.
+ `customValue` – All occurrences (or regex matches) of `customValue` will be masked in the string.
+ `entityTypeFilter` – Optional array of [entity types](https://docs.aws.amazon.com/databrew/latest/APIReference/API_EntityDetectorConfiguration.html#databrew-Type-EntityDetectorConfiguration-EntityTypes). Can be used to encrypt only detected PII in free-text column.

**Example**  
  

```
// Mask all occurrences of 'amazon' in the column
{ 
    "RecipeAction": {
        "Operation": "MASK_CUSTOM",
        "Parameters": {
            "sourceColumns": ["company"],
            "maskSymbol": "#",
            "customValue": "amazon"
        }
    }
}
```