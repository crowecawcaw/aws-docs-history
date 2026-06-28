# GET\_ACTION\_RESULT

Fetches the result of a previously submitted action. Only for use in the interactive experience.

###### Parameters

- `actionId` – The ActionId returned in the original SendProjectSessionAction response.

###### Example

```
{
    "RecipeAction": {
        "Operation": "GET_ACTION_RESULT",
        "Parameters": {
            "actionId": "7",
        }
    }
}
```
