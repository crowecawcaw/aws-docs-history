

# MASK\_RANGE
<a name="recipe-actions.MASK_RANGE"></a>

Masks characters between two positions with a user-specified masking symbol.

**Parameters**
+ `sourceColumns` – A list of existing column names.
+ `maskSymbol` – A symbol that will be used to replace specified characters.
+ `start` – A number indicating at which character position the masking is to begin (0-indexed, inclusive). Negative indexing is allowed. Omitting this parameter will apply the mask from the beginning of the string until 'stop'.
+ `stop` – A number indicating at which character position the masking is to end (0-indexed, exclusive). Negative indexing is allowed. Omitting this parameter will apply the mask from 'start' until the end of the string.
+ `alphabet` – An array of character sets enums to preserve during masking. Valid enum values: SYMBOLS, WHITESPACE.
+ `entityTypeFilter` – Optional array of [entity types](https://docs.aws.amazon.com/databrew/latest/APIReference/API_EntityDetectorConfiguration.html#databrew-Type-EntityDetectorConfiguration-EntityTypes). Can be used to encrypt only detected PII in free-text column.

**Example**  
  

```
// Mask entire string
{ 
    "RecipeAction": {
        "Operation": "MASK_RANGE",
        "Parameters": {
            "sourceColumns": ["firstName", "lastName"],
            "maskSymbol": "#"
        }
    }
}
```