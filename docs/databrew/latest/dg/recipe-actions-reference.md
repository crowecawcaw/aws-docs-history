# Recipe step and function reference

In this reference, you can find descriptions of the recipe steps and functions that you can use
programmatically, either from the AWS CLI or by using one of the AWS SDKs. In DataBrew, a _recipe step_ is an action that transforms your raw data into a form
that is ready to be consumed by your data pipeline. A DataBrew _function_ is a special kind of recipe step that performs a computation
based on parameters.

Categories for transformations in the UI include the following:

- Basic column recipe steps
  - Filter
  - Column

- Data cleaning recipe steps
  - Format
  - Clean
  - Extract

- Data quality recipe steps
  - Missing
  - Invalid
  - Duplicates
  - Outliers

- Personally indentifiable information (PII) recipe steps
  - Mask personal information
  - Replace personal information
  - Encrypt personal information
  - Shuffle rows

- Column structure recipe steps
  - Split
  - Merge
  - Create

- Column formatting recipe steps
  - Decimal precision
  - Thousands separator
  - Abbreviate numbers

- Data structure recipe steps
  - Nest-Unnest
  - Pivot
  - Group
  - Join
  - Union

- Data science recipe steps
  - Text
  - Scale
  - Mapping
  - Encode

- Functions

      + Mathematical functions
      + Aggregate functions
      + Text functions
      + Date and time functions
      + Window functions
      + Web functions
      + Other functions

  For more information about how these recipe steps and functions are used in a recipe (including the use of
  condition expressions) see [Defining a recipe structure](recipes.md#recipes.structure "recipes.md#recipes.structure").

The following sections describe the recipe steps and functions, organized by what they do.

###### Topics

- [Basic column recipe steps](recipe-actions.md "recipe-actions.md")
- [Data cleaning recipe steps](recipe-actions.md "recipe-actions.md")
- [Data quality recipe steps](recipe-actions.md "recipe-actions.md")
- [Personally identifiable information (PII) recipe steps](recipe-actions.md "recipe-actions.md")
- [Outlier detection and handling recipe steps](recipe-actions.md "recipe-actions.md")
- [Column structure recipe steps](recipe-actions.md "recipe-actions.md")
- [Column formatting recipe steps](recipe-actions.md "recipe-actions.md")
- [Data structure recipe steps](recipe-actions.md "recipe-actions.md")
- [Data science recipe steps](recipe-actions.md "recipe-actions.md")
- [Mathematical functions](recipe-actions.functions.md "recipe-actions.functions.md")
- [Aggregate functions](recipe-actions.functions.md "recipe-actions.functions.md")
- [Text functions](recipe-actions.functions.md "recipe-actions.functions.md")
- [Date and time functions](recipe-actions.functions.md "recipe-actions.functions.md")
- [Window functions](recipe-actions.functions.md "recipe-actions.functions.md")
- [Web functions](recipe-actions.functions.md "recipe-actions.functions.md")
- [Other functions](recipe-actions.functions.md "recipe-actions.functions.md")
