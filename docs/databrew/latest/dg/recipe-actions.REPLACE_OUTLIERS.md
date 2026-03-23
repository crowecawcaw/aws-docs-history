# REPLACE_OUTLIERS

Updates the data point values that classify as outliers, based on the settings in the parameters.

###### Parameters

- `sourceColumn`
  – Specifies the name of an existing numeric column that might contain outliers.
- `outlierStrategy` – Specifies the approach to use in detecting
  outliers. Valid values include the following:
  - `Z_SCORE` – Identifies a value as an outlier when it
    deviates from the mean by more than the standard deviation threshold.
  - `MODIFIED_Z_SCORE` – Identifies a value as an outlier
    when it deviates from the median by more than the median absolute deviation
    threshold.
  - `IQR`
    – Identifies a values as an outlier when it falls beyond the first and last quartile of column data. The interquartile range (IQR) measures where the middle 50% of the data points are.

- `threshold` – Specifies the threshold value to use when
  detecting outliers. The `sourceColumn` value is identified as an outlier
  if the score that's calculated with the `outlierStrategy` exceeds this
  number. The default is 3.
- `replaceType` – Specifies the method to use when replacing
  outliers. Valid values include the following:
  - `WINSORIZE_VALUES`
    – Specifies using the minimum and maximum percentile to cap the values.
  - `REPLACE_WITH_CUSTOM`
  - `REPLACE_WITH_EMPTY`
  - `REPLACE_WITH_NULL`
  - `REPLACE_WITH_MODE`
  - `REPLACE_WITH_AVERAGE`
  - `REPLACE_WITH_MEDIAN`
  - `REPLACE_WITH_SUM`
  - `REPLACE_WITH_MAX`

- `modeType` – Indicates the type of modal function to use when
  `replaceType` is `REPLACE_WITH_MODE`. Valid values include
  the following: `MIN`, `MAX`, and `AVERAGE`.
- `minValue` – Indicates the minimum percentile value for the
  outlier range that is to be applied when `trimValue` is used. Valid range
  is 0–100.
- `maxValue` – Indicates the maximum percentile value for the
  outlier range that is to be applied when `trimValue` is used. . Valid
  range is 0–100.
- `value`
  – Specifies the value to insert when using `REPLACE_WITH_CUSTOM`.
- `trimValue`
  – Specifies whether to remove all or some of the outliers. This Boolean value is set to `TRUE` when `replaceType` is `REPLACE_WITH_NULL`, `REPLACE_WITH_MODE`, or `WINSORIZE_VALUES`. It defaults to `FALSE` for all others.

      + `FALSE` – Removes all outliers
      + `TRUE`
       –Removes outliers that rank outside of the percentile cap threshold specified in `minValue` and `maxValue`.

  The following examples display syntax for a single [RecipeAction](API_RecipeAction.md "API_RecipeAction.md")
  operation. A _recipe_ contains at least one [RecipeStep](API_RecipeStep.md "API_RecipeStep.md") operation, and a recipe step contains at least
  one recipe action. A _recipe action_ runs the data
  transform that you specify. A group of recipe actions run in sequential order to create the
  final dataset.

JSON
The following shows an example `RecipeAction` to use as member of
an example `RecipeStep` for a DataBrew [Recipe](API_Recipe.md "API_Recipe.md"), using JSON syntax.
For syntax examples showing a list of recipe actions, see [Defining a recipe structure](recipes.md#recipes.structure "recipes.md#recipes.structure").

###### Example in JSON

```
{
    "Action": {
        "Operation": "REPLACE_OUTLIERS",
        "Parameters": {
            "maxValue": "`95`",
            "minValue": "`5`",
            "modeType": "`AVERAGE`",
            "outlierStrategy": "`Z_SCORE`",
            "replaceType": "`REPLACE_WITH_MODE`",
            "sourceColumn": "`name-of-existing-column`",
            "threshold": "`3`",
            "trimValue": "`TRUE`"
        }
    }
}
```

For more information on using this recipe action in an API operation, see
[CreateRecipe](API_CreateRecipe.md "API_CreateRecipe.md") or
[UpdateRecipe](API_UpdateRecipe.md "API_UpdateRecipe.md"). You can use these and other API
operations in your own code.

YAML
The following shows an example `RecipeAction` to use as member of
an example `RecipeStep` for a DataBrew [Recipe](API_Recipe.md "API_Recipe.md"), using YAML syntax.
For syntax examples showing a list of recipe actions, see [Defining a recipe structure](recipes.md#recipes.structure "recipes.md#recipes.structure").

###### Example in YAML

```
- Action:
  Operation: REMOVE_OUTLIERS
  Parameters:
    sourceColumn: `name-of-existing-column`
    outlierStrategy: `Z_SCORE`
    threshold: '`3`'
    replaceType: `REPLACE_WITH_MODE`
    modeType: `AVERAGE`
    minValue: '`5`'
    maxValue: '`95`'
    trimValue: '`TRUE`'
```

For more information on using this recipe action in an API operation, see
[CreateRecipe](API_CreateRecipe.md "API_CreateRecipe.md") or
[UpdateRecipe](API_UpdateRecipe.md "API_UpdateRecipe.md"). You can use these and other API
operations in your own code.
