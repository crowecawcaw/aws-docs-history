# Using projection expressions in

DynamoDB

To read data from a table, you use operations such as `GetItem`,
`Query`, or `Scan`. Amazon DynamoDB returns all the item attributes
by default. To get only some, rather than all of the attributes, use a projection
expression.

A _projection expression_ is a string that identifies the
attributes that you want. To retrieve a single attribute, specify its name. For multiple
attributes, the names must be comma-separated.

The following are some examples of projection expressions, based on the
`ProductCatalog` item from [Referring to item attributes when using
expressions in DynamoDB](Expressions.md "Expressions.md"):

- A single top-level attribute.

`Title`

- Three top-level attributes. DynamoDB retrieves the entire `Color`
  set.

`Title, Price, Color`

- Four top-level attributes. DynamoDB returns the entire contents of
  `RelatedItems` and `ProductReviews`.

`Title, Description, RelatedItems, ProductReviews`

###### Note

Projection expression has no effect on provisioned throughput consumption. DynamoDB
determines capacity units consumed based on item size, instead of the amount of data
that is returned to an application.

**Reserved words and special characters**

DynamoDB has reserved words and special characters. DynamoDB allows you to use these
reserved words and special characters for names, but we recommend that you avoid doing
so because you have to use aliases for them whenever you use these names in an
expression. For a complete list, see [Reserved words in DynamoDB](ReservedWords.md "ReservedWords.md").

You'll need to use expression attribute names in place of the actual name if:

- The attribute name is on the list of reserved words in DynamoDB.
- The attribute name does not meet the requirement that the first character is
  `a-z` or `A-Z` and that the second character (if
  present) is `a-Z`, `A-Z`, or `0-9`.
- The attribute name contains a **#** (hash) or
  **:** (colon).
  The following AWS CLI example shows how to use a projection expression with a
  `GetItem` operation. This projection expression retrieves a top-level
  scalar attribute (`Description`), the first element in a list
  (`RelatedItems[0]`), and a list nested within a map
  (`ProductReviews.FiveStar`).

```
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '"Id": { "N": "123" } \
    --projection-expression "Description, RelatedItems[0], ProductReviews.FiveStar"
```

The following JSON would be returned for this example.

```
{
    "Item": {
        "Description": {
            "S": "123 description"
        },
        "ProductReviews": {
            "M": {
                "FiveStar": {
                    "L": [
                        {
                            "S": "Excellent! Can't recommend it highly enough! Buy it!"
                        },
                        {
                            "S": "Do yourself a favor and buy this."
                        }
                    ]
                }
            }
        },
        "RelatedItems": {
            "L": [
                {
                    "N": "341"
                }
            ]
        }
    }
}
```
