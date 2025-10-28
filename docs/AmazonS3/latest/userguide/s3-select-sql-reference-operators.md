# Operators

###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/")

Amazon S3 Select supports the following operators.

## Logical operators

- `AND`
- `NOT`
- `OR`

## Comparison operators

- `<`
- `>`
- `<=`
- `>=`
- `=`
- `<>`
- `!=`
- `BETWEEN`
- `IN` – For example: `IN ('a', 'b', 'c')`

## Pattern-matching operators

- `LIKE`
- `_` (Matches any character)
- `%` (Matches any sequence of characters)

## Unitary operators

- `IS NULL`
- `IS NOT NULL`

## Math operators

Addition, subtraction, multiplication, division, and modulo are supported, as
follows:

- -
- -
- \*
- /
- %

## Operator precedence

The following table shows the operators' precedence in decreasing order.

| Operator or element | Associativity | Required                         |
| ------------------- | ------------- | -------------------------------- |
| `-`                 | right         | unary minus                      |
| `*`, `/`, `%`       | left          | multiplication, division, modulo |
| `+`, `-`            | left          | addition, subtraction            |
| `IN`                |               | set membership                   |
| `BETWEEN`           |               | range containment                |
| `LIKE`              |               | string pattern matching          |
| `<``>`              |               | less than, greater than          |
| `=`                 | right         | equality, assignment             |
| `NOT`               | right         | logical negation                 |
| `AND`               | left          | logical conjunction              |
| `OR`                | left          | logical disjunction              |
