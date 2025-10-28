# Filter expression structure and elements

This section includes information about the structure of filter expressions and their elements.

###### Topics

- [Filter expression structure](#filter-expression-structure "#filter-expression-structure")
- [Filter expression elements](#filter-expression-elements "#filter-expression-elements")

## Filter expression structure

The general structure of a filter expression is as follows:

```

EXCLUDE/INCLUDE ItemID/ActionID/UserID WHERE `dataset type`.`field` IN/NOT IN (`value/parameter`)

```

You can either manually create filter expressions or get help with
expression syntax and structure by using the [Expression builder](filter-real-time.md#using-filter-expression-builder "filter-real-time.md#using-filter-expression-builder") in
the console.

## Filter expression elements

Use the following elements to create filter expressions:

**INCLUDE or EXCLUDE**

Use `INCLUDE` to limit recommendations to only items that meet the filter criteria _OR_ use
`EXCLUDE` to remove all items that meet the filter criteria.

**ItemID/ActionID/UserID**

Use one of these elements after the `INCLUDE` or `EXCLUDE` element. The element you use
depends on whether you are filtering items (for item recommendations), actions (for action recommendations), or
users (for user segments).

**WHERE**

Use `WHERE` to check conditions for items, actions, or users. You must use the
`WHERE` element after the `ItemID`, `ActionID`, or `UserID`.

**AND/OR**

To chain multiple conditions
together within the same filter expression, use `AND` or `OR`. Conditions chained together using
`AND` or `OR` can only affect fields of the dataset used
in the first condition.

**Dataset.field**

Provide the dataset and the metadata field that you want to
filter recommendations by in `dataset`.`field` format. For
example, to filter item recommendations based on the genres field in your Items dataset, you would use
Items.genres in your filter expression.

**IF condition**

Use an `IF` condition
_only_ to check conditions for the
`CurrentUser` and only _once_ at the
end of an expression. However, you can extend an `IF` condition using
`AND`.

**CurrentUser.attribute**

To filter item recommendations based on the user you are getting recommendations for, in _only_ an IF condition,
use `CurrentUser` and provide the user field. For example, `CurrentUser.AGE`.

**CurrentItem.attribute**

For only related items recipes and use cases, use
`CurrentItem`.`attribute` to filter items based on an attribute of the item you
specify in your request for related items recommendations. For example, `CurrentItem.GENRE` or
`CurrentItem.PRICE`.

You can apply a filter with the CurrentItem element only if your domain use case or custom recipe
generates related items recommendations,
such as the Similar-Items recipe or the _More Like X_ domain use case. The first time you create a filter with a
`CurrentItem` element, filter creation can a few minutes. If you use AWS KMS for encryption,
filter creation can take up to 15 minutes.

**IN/NOT IN**

Use `IN` or `NOT IN` as comparison operators to
filter based on matching (or not matching) one or more string values. Amazon Personalize filters
only on exact strings.

**Comparison operators**

Use =, <, <=, >, >=, and != operators to test numerical data, including data passed in a placeholder parameter, for
equality.

**Asterisk (\*) character**

Use `*` to include or exclude interactions of all types. Use
`*`
_only_ for filter expressions that use the `EVENT_TYPE`
field of an `Interactions` dataset.

**Pipe separator**

Use the pipe separator (`|`) to chain multiple expressions together.
For more information, see [Combining multiple expressions](multiple-expression-example.md "multiple-expression-example.md").

**Parameters**

For expressions that use comparison operators or the `IN` operator, use the
dollar sign ($) and a parameter name to add a placeholder parameter as a value. For
 example, `$GENRES`. For this example, when you get recommendations, you
supply the genre or genres to filter by.

###### Note

You define a parameter name when you add it to an expression. The parameter name
does not have to match the field name. We recommend that you use a parameter name
that is similar to the field name and easy to remember. You use the parameter
name (case sensitive) when you apply the filter to recommendations requests. For an example
that shows how to apply a filter with placeholder parameters when using the AWS SDKS, see [Applying a filter (AWS SDKs)](filter-real-time.md#applying-filter-sdk "filter-real-time.md#applying-filter-sdk").
