# SENTENCE\_CASE

Changes each string in a column to sentence case. In _sentence case,_ the first letter of each sentence is capitalized, and the
rest of the sentence is transformed to lowercase. An example is: The quick brown fox.
Jumped over. The fence

###### Parameters

- `sourceColumn` – The name of an existing column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "SENTENCE_CASE",
        "Parameters": {
            "sourceColumn": "description"
        }
    }
}
```
