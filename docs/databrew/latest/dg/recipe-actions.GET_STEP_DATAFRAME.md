

# GET\_STEP\_DATAFRAME
<a name="recipe-actions.GET_STEP_DATAFRAME"></a>

Fetches the data frame from a step in the project's recipe. Only for use in the interactive experience. Used with the ViewFrame parameter to paginate across a large data frame.

**Parameters**
+ `stepIndex` – The index of the step in the project's recipe for which to fetch the data frame.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "GET_STEP_DATAFRAME",
        "Parameters": {
            "stepIndex": "0"
        }
    }
}
```