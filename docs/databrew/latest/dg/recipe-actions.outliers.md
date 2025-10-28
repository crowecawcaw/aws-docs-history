# RESCALE_OUTLIERS_WITH_SKEW

Returns a new column with a rescaled outlier value in each row, based on the settings in
the parameters. This action works to reduce distribution skewness by applying the specified
log or root transform. We recommend this action for handling skewed data.

###### Parameters

- `sourceColumn`
  – Specifies the name of an existing numeric column that might contain outliers.
- `targetColumn`
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
- `skewFunction` – Specifies the method to use when replacing
  outliers. Valid values include the following:
  - LOG – Applies a strong transformation to reduce positive and negative skew. This is a natural logarithm (2.718281828).
  - ROOT (with `value = 3` ) – Applies a fairly strong transformation to reduce positive and negative skew. (Cube root)
  - ROOT (with `value = 2` ) – Applies a moderate transformation to reduce positive skew only. (Square root)
  - SQUARE – Applies a moderate transformation to reduce negative skew. (Square)
  - Custom transform – Applies the specified `LOG` or
    `ROOT` transform using the custom number provided in the
    `value` parameter.

- `value`
  – Specifies the value to use for the custom transform. If `skewFunction` is LOG, this value represents the base of the log. If `skewFunction` is ROOT, this value represents the power of the root.
  The following examples display syntax for a single [RecipeAction](API_RecipeAction.md "API_RecipeAction.md")
  operation. A _recipe_ contains at least one [RecipeStep](API_RecipeStep.md "API_RecipeStep.md") operation, and a recipe step contains at least
  one recipe action. A _recipe action_ runs the data
  transform that you specify. A group of recipe actions run in sequential order to create the
  final dataset.

JSON
The following shows an example `RecipeAction` to use as
member of an example `RecipeStep` for a DataBrew [Recipe](API_Recipe.md "API_Recipe.md"), using JSON syntax. For syntax examples showing a list of recipe
actions, see [Defining a recipe structure](recipes.md#recipes.structure "recipes.md#recipes.structure").

###### Example in JSON

```
{
    "Action": {
        "Operation": "RESCALE_OUTLIERS_WITH_SKEW",
        "Parameters": {
            "outlierStrategy": "`Z_SCORE`",
            "threshold": "`3`",
            "skewFunction": "`ROOT`",
            "sourceColumn": "`name-of-existing-column`",
            "targetColumn": "`name-of-new-column`",
            "value": "`4`"
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
  Operation: RESCALE_OUTLIERS_WITH_SKEW
  Parameters:
    outlierStrategy: `Z_SCORE`
    threshold: '`3`'
    skewFunction: `ROOT`
    sourceColumn: `name-of-existing-column`
    targetColumn: `name-of-new-column`
    value: '`4`'
```

For more information on using this recipe action in an API operation, see
[CreateRecipe](API_CreateRecipe.md "API_CreateRecipe.md") or
[UpdateRecipe](API_UpdateRecipe.md "API_UpdateRecipe.md"). You can use these and other API
operations in your own code.
