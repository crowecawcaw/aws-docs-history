

# Recipe step and function reference
<a name="recipe-actions-reference"></a>

In this reference, you can find descriptions of the recipe steps and functions that you can use programmatically, either from the AWS CLI or by using one of the AWS SDKs. In DataBrew, a *recipe step* is an action that transforms your raw data into a form that is ready to be consumed by your data pipeline. A DataBrew *function* is a special kind of recipe step that performs a computation based on parameters.

Categories for transformations in the UI include the following:
+ Basic column recipe steps
  + Filter
  + Column
+ Data cleaning recipe steps
  + Format
  + Clean
  + Extract
+ Data quality recipe steps
  + Missing
  + Invalid
  + Duplicates
  + Outliers
+ Personally indentifiable information (PII) recipe steps
  + Mask personal information
  + Replace personal information
  + Encrypt personal information
  + Shuffle rows
+ Column structure recipe steps
  + Split
  + Merge
  + Create
+ Column formatting recipe steps
  + Decimal precision
  + Thousands separator
  + Abbreviate numbers
+ Data structure recipe steps
  + Nest-Unnest
  + Pivot
  + Group
  + Join
  + Union
+ Data science recipe steps
  + Text
  + Scale
  + Mapping
  + Encode
+ Functions
  + Mathematical functions
  + Aggregate functions
  + Text functions
  + Date and time functions
  + Window functions
  + Web functions
  + Other functions

For more information about how these recipe steps and functions are used in a recipe (including the use of condition expressions) see [Defining a recipe structure](recipes.md#recipes.structure).

The following sections describe the recipe steps and functions, organized by what they do.

**Topics**
+ [Basic column recipe steps](recipe-actions.basic.md)
+ [Data cleaning recipe steps](recipe-actions.data-cleaning.md)
+ [Data quality recipe steps](recipe-actions.data-quality.md)
+ [Personally identifiable information (PII) recipe steps](recipe-actions.pii.md)
+ [Outlier detection and handling recipe steps](recipe-actions.outliers.md)
+ [Column structure recipe steps](recipe-actions.column-structure.md)
+ [Column formatting recipe steps](recipe-actions.column-formatting.md)
+ [Data structure recipe steps](recipe-actions.data-structure.md)
+ [Data science recipe steps](recipe-actions.data-science.md)
+ [Mathematical functions](recipe-actions.functions.math.md)
+ [Aggregate functions](recipe-actions.functions.aggregate.md)
+ [Text functions](recipe-actions.functions.text.md)
+ [Date and time functions](recipe-actions.functions.date.md)
+ [Window functions](recipe-actions.functions.window.md)
+ [Web functions](recipe-actions.functions.web.md)
+ [Other functions](recipe-actions.functions.other.md)