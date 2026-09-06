

# MASK\_DELIMITER
<a name="recipe-actions.MASK_DELIMITER"></a>

Masks characters between two delimiters with a user-specified masking symbol.

**Parameters**
+ `sourceColumns` – A list of existing column names.
+ `maskSymbol` – A symbol that will be used to replace specified characters.
+ `startDelimiter` – A character indicating where masking is to begin. Omitting this parameter will apply the mask starting from the start of the string.
+ `endDelimiter` – A character indicating where masking is to end. Omitting this parameter will apply the masking from the startDelimiter to the end of the string.
+ `preserveDelimiters` – If true, applies mask to delimiters.
+ `alphabet` – An array of character sets to preserve during masking. Valid enum values: SYMBOLS, WHITESPACE.
+ `entityTypeFilter` – Optional array of [entity types](https://docs.aws.amazon.com/databrew/latest/APIReference/API_EntityDetectorConfiguration.html#databrew-Type-EntityDetectorConfiguration-EntityTypes). Can be used to encrypt only detected PII in free-text column.

**Example**  
  

```
// Mask string between '<' and '>', ignoring white spaces, symbols, and lowercase letters
{ 
    "RecipeAction": {
        "Operation": "MASK_DELIMITER",
        "Parameters": {
            "sourceColumns": ["name"],
            "maskSymbol": "#",
            "startDelimiter": "<",
            "endDelimiter": ">",
            "preserveDelimiters": false,
            "alphabet": ["WHITESPACE", "SYMBOLS"]
        }
    }
}
```