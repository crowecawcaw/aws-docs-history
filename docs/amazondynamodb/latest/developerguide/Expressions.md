# Expression attribute names (aliases)

in DynamoDB

An _expression attribute name_ is an alias (or placeholder) that you
use in an Amazon DynamoDB expression as an alternative to an actual attribute name. An expression
attribute name must begin with a pound sign (`#`) and be followed by one or more
alphanumeric characters. The underscore (`_`) character is also allowed.

This section describes several situations in which you must use expression attribute
names.

###### Note

The examples in this section use the AWS Command Line Interface (AWS CLI).

###### Topics

- [Reserved
  words](#Expressions.ExpressionAttributeNames.ReservedWords "#Expressions.ExpressionAttributeNames.ReservedWords")
- [Attribute names containing special characters](#Expressions.ExpressionAttributeNames.AttributeNamesContainingSpecialCharacters "#Expressions.ExpressionAttributeNames.AttributeNamesContainingSpecialCharacters")
- [Nested
  attributes](#Expressions.ExpressionAttributeNames.NestedAttributes "#Expressions.ExpressionAttributeNames.NestedAttributes")
- [Repeatedly referencing attribute names](#Expressions.ExpressionAttributeNames.RepeatingAttributeNames "#Expressions.ExpressionAttributeNames.RepeatingAttributeNames")

## Reserved

words

Sometimes you might need to write an expression containing an attribute name that
conflicts with a DynamoDB reserved word. (For a complete list of reserved words, see [Reserved words in DynamoDB](ReservedWords.md "ReservedWords.md").)

For example, the following AWS CLI example would fail because `COMMENT` is a
reserved word.

```
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"123"}}' \
    --projection-expression "Comment"
```

To work around this, you can replace `Comment` with an expression attribute
name such as `#c`. The `#` (pound sign) is required and indicates
that this is a placeholder for an attribute name. The AWS CLI example would now look like
the following.

```
aws dynamodb get-item \
     --table-name ProductCatalog \
     --key '{"Id":{"N":"123"}}' \
     --projection-expression "#c" \
     --expression-attribute-names '{"#c":"Comment"}'
```

###### Note

If an attribute name begins with a number, contains a space or contains a reserved
word, you _must_ use an expression attribute name to replace that
attribute's name in the expression.

## Attribute names containing special characters

In an expression, a dot (".") is interpreted as a separator character in a document
path. However, DynamoDB also allows you to use a dot character and other special
characters, such as a hyphen ("-") as part of an attribute name. This can be ambiguous
in some cases. To illustrate, suppose that you wanted to retrieve the
`Safety.Warning` attribute from a `ProductCatalog` item (see
[Referring to item attributes when using
expressions in DynamoDB](Expressions.md "Expressions.md")).

Suppose that you wanted to access `Safety.Warning` using a projection
expression.

```
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"123"}}' \
    --projection-expression "Safety.Warning"
```

DynamoDB would return an empty result, rather than the expected string ("`Always
 wear a helmet`"). This is because DynamoDB interprets a dot in an expression as a
document path separator. In this case, you must define an expression attribute name
(such as `#sw`) as a substitute for `Safety.Warning`. You could
then use the following projection expression.

```
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"123"}}' \
    --projection-expression "#sw" \
    --expression-attribute-names '{"#sw":"Safety.Warning"}'
```

DynamoDB would then return the correct result.

###### Note

If an attribute name contains a dot (".") or a hyphen ("-"), you
_must_ use an expression attribute name to replace that
attribute's name in the expression.

## Nested

attributes

Suppose that you wanted to access the nested attribute
`ProductReviews.OneStar`. In an expression attribute name, DynamoDB treats
the dot (".") as a character within an attribute's name. To reference the nested
attribute, define an expression attribute name for each element in the document
path:

- `#pr — ProductReviews`
- `#1star — OneStar`

You could then use `#pr.#1star` for the projection expression.

```
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"123"}}' \
    --projection-expression "#pr.#1star"  \
    --expression-attribute-names '{"#pr":"ProductReviews", "#1star":"OneStar"}'
```

DynamoDB would then return the correct result.

## Repeatedly referencing attribute names

Expression attribute names are helpful when you need to refer to the same attribute
name repeatedly. For example, consider the following expression for retrieving some of
the reviews from a `ProductCatalog` item.

```
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"123"}}' \
    --projection-expression "ProductReviews.FiveStar, ProductReviews.ThreeStar, ProductReviews.OneStar"
```

To make this more concise, you can replace `ProductReviews` with an
expression attribute name such as `#pr`. The revised expression would now
look like the following.

- `#pr.FiveStar, #pr.ThreeStar, #pr.OneStar`

```
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"123"}}' \
    --projection-expression "#pr.FiveStar, #pr.ThreeStar, #pr.OneStar" \
    --expression-attribute-names '{"#pr":"ProductReviews"}'
```

If you define an expression attribute name, you must use it consistently throughout
the entire expression. Also, you cannot omit the `#` symbol.
