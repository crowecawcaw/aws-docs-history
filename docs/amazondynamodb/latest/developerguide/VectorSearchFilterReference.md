

# SearchConditionExpression reference for vector indexes

This topic is a reference for the `SearchConditionExpression` parameter of a `SearchVectors` request against a vector index in Amazon DynamoDB. It describes the expression syntax, the supported operators, combinators, and functions, the vector index partition key rules, the condition limit, how DynamoDB compares Number values, the order in which the service validates an expression, and the validation error messages. For task-oriented examples of filtering a search, see [Filtering with SearchConditionExpression](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Search.Filtering).

**Topics**
+ [SearchConditionExpression syntax](#VectorSearchFilterReference.Syntax)
+ [Supported operators, combinators, and functions](#VectorSearchFilterReference.Operators)
+ [How conditions treat a missing attribute](#VectorSearchFilterReference.MissingAttributes)
+ [Vector index partition key rules](#VectorSearchFilterReference.PartitionKey)
+ [Condition limit](#VectorSearchFilterReference.ConditionLimit)
+ [Number comparison precision](#VectorSearchFilterReference.NumberPrecision)
+ [Example: combining IN, BETWEEN, and OR](#VectorSearchFilterReference.Example)
+ [Validation order](#VectorSearchFilterReference.ValidationOrder)
+ [Validation error messages](#VectorSearchFilterReference.Errors)

## SearchConditionExpression syntax
<a name="VectorSearchFilterReference.Syntax"></a>

A `SearchConditionExpression` in a `SearchVectors` request is a Boolean combination of conditions over the attributes declared in the vector index SearchSchema. A single comparison condition has the form `#name operator :value`.

You reference an attribute either by its literal name or through an expression attribute name alias (`#name`), and you supply the right side as an expression attribute value placeholder (`:value`). The request carries the aliases in `ExpressionAttributeNames` and the values in `ExpressionAttributeValues`, the same pattern that `Query`, `Scan`, and `UpdateItem` use. Alias an attribute name with `ExpressionAttributeNames` when the name is a DynamoDB reserved word.

`SearchConditionExpression` supports top-level attributes only. A condition cannot reference a nested attribute path, such as `a.b` or `a[0]`. If you need to filter on a nested value, project it into a top-level attribute when you write the item.

## Supported operators, combinators, and functions
<a name="VectorSearchFilterReference.Operators"></a>

`SearchConditionExpression` supports the following operators on inline filter attributes. For the operators allowed on the vector index partition key, see [Vector index partition key rules](#VectorSearchFilterReference.PartitionKey).


| Operator | Meaning | Inline filter attribute types | 
| --- | --- | --- | 
| = | Equality | Any (S, N, B) | 
| <> | Inequality | Any (S, N, B) | 
| IN (:a, :b, ...) | Membership in a list of values | Any (S, N, B) | 
| <, <=, >, >= | Range comparison | Number (N) only | 
| BETWEEN :lo AND :hi | Inclusive range | Number (N) only | 

A range operator (`<`, `<=`, `>`, `>=`, or `BETWEEN`) applied to a String or Binary attribute is rejected. The following details apply to the comparison, range, and membership operators.
+ The right side of a comparison must be an expression attribute value placeholder (`:value`). A condition cannot compare two attributes to each other.
+ `=` and `<>` apply to String, Number, and Binary inline filter attributes. For how `<>` treats an item that does not have the attribute, see [How conditions treat a missing attribute](#VectorSearchFilterReference.MissingAttributes).
+ `BETWEEN :lo AND :hi` is inclusive of both bounds. The two bounds can be equal, which the service accepts and treats as a single value equivalent to `=`. The service does not rewrite `BETWEEN` into a pair of `<=` and `>=` comparisons, and `BETWEEN` counts as one condition, not two.
+ An `IN` list accepts 1 to 100 expression attribute value placeholders. The list must contain value placeholders only. An attribute name, whether plain, aliased, or nested, inside an `IN` list is rejected.

You join conditions with the following logical operators.


| Combinator | Notes | 
| --- | --- | 
| AND | Always supported. | 
| OR | Supported between inline filter conditions. Not supported on a condition that references the vector index partition key attribute. | 
| NOT | Supported on an inline filter condition. Not supported on a condition that references the vector index partition key attribute. | 

Parentheses group subexpressions, following the same precedence that `FilterExpression` uses in `Query` and `Scan`.

`SearchConditionExpression` accepts two condition functions.


| Function | Meaning | 
| --- | --- | 
| attribute\_exists(\#name) | The named attribute is present on the item. | 
| attribute\_not\_exists(\#name) | The named attribute is not present on the item. | 

Other condition functions used by `Query`, `Scan`, and condition expressions on item-level operations, including `begins_with`, `contains`, `attribute_type`, and `size`, are rejected inside a `SearchConditionExpression`. Each function call counts as one condition.

## How conditions treat a missing attribute
<a name="VectorSearchFilterReference.MissingAttributes"></a>

An item does not have to carry every inline filter attribute. How a condition treats an item that does not have the attribute depends on the operator.
+ An `=`, range, `BETWEEN`, or `IN` condition does not match an item that does not have the attribute.
+ A `<>` condition and a `NOT` condition do match an item that does not have the attribute. For an inline filter attribute named `Brand`, `#brand <> :b` and `NOT (#brand = :b)` return the same items, including items that do not have `Brand`.

To exclude items that do not have the attribute, add an `attribute_exists` condition. For example, `#brand <> :b AND attribute_exists(#brand)` returns only items that have a `Brand` value other than `:b`.

## Vector index partition key rules
<a name="VectorSearchFilterReference.PartitionKey"></a>

If the vector index declares a vector index partition key (`HASH`) in its SearchSchema, a `SearchVectors` request that supplies a `SearchConditionExpression` must follow these rules for the partition key condition.
+ The expression must contain exactly one condition on the partition key attribute, and that condition must use `=`.
+ The partition key condition must appear at the top level of the expression, joined to the rest with `AND`. It must not appear inside an `OR` or a `NOT`.
+ The `<>` operator, range operators, `BETWEEN`, `IN` (even with a single value), and the `attribute_exists` and `attribute_not_exists` functions are not supported on the partition key attribute, even when it is declared as Number (`N`).
+ Parentheses around an `AND` group that contains the partition key condition are accepted, for example `(#category = :c AND #price > :p)`. An `OR` group among inline filter conditions next to the partition key condition is also accepted, for example `#category = :c AND (#brand = :b OR #brand = :d)`.

These rules apply whether the partition key is a String, Number, or Binary attribute. A partition key condition that violates any of them is rejected with a `ValidationException`. For the exact messages, see [Validation error messages](#VectorSearchFilterReference.Errors).

If the vector index does not declare a vector index partition key in its SearchSchema, no partition key condition is required. A `SearchConditionExpression` can then contain only inline filter conditions, and every `SearchVectors` call searches the entire index. For more information, see [SearchSchema](VectorSearch.md#VectorSearch.SearchSchema).

A single `SearchVectors` call targets exactly one partition key value. To search more than one partition key value, make one `SearchVectors` call for each value.

## Condition limit
<a name="VectorSearchFilterReference.ConditionLimit"></a>

A `SearchConditionExpression` can contain a limited number of conditions. When the vector index declares a vector index partition key (`HASH`), the partition key condition counts toward the limit.

Each of the following counts as one condition.
+ A comparison (`=`, `<>`, `<`, `<=`, `>`, `>=`).
+ A `BETWEEN` clause.
+ An `IN` clause, regardless of how many values appear in its list.
+ A function call (`attribute_exists` or `attribute_not_exists`).

The logical operators `AND`, `OR`, and `NOT`, and parentheses, do not count as conditions. An expression that contains too many conditions is rejected with a `ValidationException` and the message `Invalid SearchConditionExpression: The expression contains too many conditions; number of conditions: <count>, maximum: <max>`.

Two other limits apply to an expression.
+ An `IN` list can contain at most 100 value placeholders. A longer list is rejected.
+ An expression can also contain too many operators, even when it is within the condition limit. Such an expression is rejected with a `ValidationException` and the message `Invalid SearchConditionExpression: The expression contains too many operators; operator count: <count>`.

The number of conditions in an expression is separate from the number of inline filter attributes you can declare for each vector index. For the inline-filters-per-index quota, see [Vector indexes](ServiceQuotas.md#limits-vector-indexes).

## Number comparison precision
<a name="VectorSearchFilterReference.NumberPrecision"></a>

`SearchVectors` compares Number values in a `SearchConditionExpression` as 64-bit binary floating-point values (IEEE 754 double precision). `Query`, `Scan`, and condition expressions on item-level operations such as `GetItem` and `UpdateItem` compare Number values exactly, with up to 38 digits of precision. Both methods return the same items whenever the stored value and the expression value each have 15 or fewer significant digits.

Beyond 15 significant digits, two different Number values can round to the same double, and `SearchVectors` then treats them as equal. `SearchVectors` rounds each value to the nearest double, with ties to even, before it compares. Every integer from -9,007,199,254,740,992 to 9,007,199,254,740,992 (253) converts exactly. Larger integers can lose their last digits.

The following table shows how the two methods can disagree at high precision.


| Condition | Value of `:p` | `SearchVectors` matches | `Query` and `Scan` match | 
| --- | --- | --- | --- | 
| Price = :p | 20 | 19.999999999999999, 20, 20.000000000000001 | 20 | 
| Price > :p | 9007199254740992 | 9007199254740994 and larger | 9007199254740993 and larger | 
| Price = :p | 1234567890123456789 | 1234567890123456641 through 1234567890123456895 | 1234567890123456789 | 

The rounding applies only to the comparison. Items that `SearchVectors` returns contain their Number attributes exactly as stored.

The whole range of DynamoDB Number values (from 1E-130 to 9.99E\+125) fits in a double, so only precision is affected, never range.

### When to store a value as String instead
<a name="VectorSearchFilterReference.NumberPrecision.String"></a>

If your `SearchConditionExpression` filter must distinguish values that differ in the sixteenth significant digit or beyond, store the value as a String attribute. A 64-bit identifier, a nanosecond epoch timestamp, or a 20-digit account number all fall into this category.

String attributes support `=`, `<>`, and `IN` in a `SearchConditionExpression`. Range operators accept only Number (`N`) attributes, so a range filter on a value that needs more than 15 significant digits is not available during the search. If your workload needs both exact comparison and a range filter, precompute a bucket attribute (for example, a day stamp derived from a nanosecond timestamp), declare it as an inline filter, and filter on the bucket during the search. Then apply the exact range check in your application code on the returned items.

## Example: combining IN, BETWEEN, and OR
<a name="VectorSearchFilterReference.Example"></a>

The following `SearchVectors` example uses a vector index named `ProductCatalogIndex` on the `Products` table. Its SearchSchema declares `Category` as the vector index partition key (`HASH`, String) and declares `Brand` (String), `Price` (Number), and `Rating` (Number) as inline filter attributes. The search returns the five closest items in the `Shoes` category that are either from one of three brands or priced within a range.

```python
import boto3

dynamodb = boto3.client("dynamodb", region_name="us-east-1")

response = dynamodb.search_vectors(
    TableName="Products",
    IndexName="ProductCatalogIndex",
    SearchVector=[
        {"N": "0.14"},
        {"N": "-0.27"},
        {"N": "0.42"},
        {"N": "-0.63"},
    ],
    TopK=5,
    SearchConditionExpression=(
        "#category = :category "
        "AND ( #brand IN (:brand1, :brand2, :brand3) "
        "OR #price BETWEEN :lo AND :hi )"
    ),
    ExpressionAttributeNames={
        "#category": "Category",
        "#brand": "Brand",
        "#price": "Price",
    },
    ExpressionAttributeValues={
        ":category": {"S": "Shoes"},
        ":brand1": {"S": "AcmeRun"},
        ":brand2": {"S": "BravoStep"},
        ":brand3": {"S": "CirqueFit"},
        ":lo": {"N": "49.99"},
        ":hi": {"N": "99.99"},
    },
)

for result in response["SearchResults"]:
    print(result["Item"], result["Score"])
```
+ The partition key condition (`#category = :category`) appears at the top level and is joined to the inline filter group with `AND`. It must not appear inside the `OR` parentheses.
+ `IN (:brand1, :brand2, :brand3)` counts as one condition, regardless of how many values appear in the list.
+ `BETWEEN :lo AND :hi` is inclusive of both bounds and counts as one condition.
+ The value placeholders use the `N` type for Number attributes and the `S` type for String attributes, matching the attribute type declared for the attribute in the vector index SearchSchema and in `AttributeDefinitions`.
+ The expression has three conditions.

## Validation order
<a name="VectorSearchFilterReference.ValidationOrder"></a>

`SearchVectors` reports one error when a `SearchConditionExpression` fails validation. The service checks for faults in three groups. An error in an earlier group is reported ahead of any error in a later group.

1. Expression checks. The service checks expression syntax, resolves each expression attribute name alias and each value placeholder, and checks for nested attribute paths, reserved keywords, comparisons between two attributes, disallowed functions, `IN` and `BETWEEN` operands, the `IN` value limit, `BETWEEN` bound order and type, the condition limit, the operator limit, and unused value placeholders and names. These include the same expression checks that `Query` and `Scan` run.

1. Partition key checks. If the vector index declares a vector index partition key (`HASH`) in its SearchSchema, the service confirms that the expression contains one condition on the partition key attribute, that the condition uses `=`, that it is not inside an `OR` or a `NOT`, and that no second condition references the partition key attribute.

1. Attribute checks. The service confirms that each referenced attribute is declared in the SearchSchema, that a range operator or `BETWEEN` is used only on a Number (`N`) attribute, and that each value matches the declared attribute type. These checks are reported for the first faulty condition, in the order in which the conditions appear in the expression.

## Validation error messages
<a name="VectorSearchFilterReference.Errors"></a>

The following tables list the `ValidationException` messages that `SearchVectors` returns when a `SearchConditionExpression` fails validation. The tables are grouped by the validation group that reports each message. For a task-oriented list of common errors, see [Troubleshooting vector indexes](VectorSearchTroubleshooting.md).

The following messages are reported in the expression checks group. They cover expression syntax, placeholder and alias resolution, reserved words, nested paths, comparisons between two attributes, disallowed functions, `IN` and `BETWEEN` operands, the `IN` value limit, `BETWEEN` bound order and type, the condition and operator limits, and unused values and names.


| Error message | Cause | Resolution | 
| --- | --- | --- | 
| Invalid SearchConditionExpression: Syntax error; token: "<token>", near: "<text>" | The expression is not well-formed, for example a trailing AND, a missing comparator, or a right side without a colon prefix. | Correct the syntax. Every comparison takes the form attribute operator :value. Join multiple conditions with AND, OR, or NOT. | 
| Invalid SearchConditionExpression: The expression can not be empty; | The SearchConditionExpression is an empty string. | Supply a non-empty SearchConditionExpression, or omit the parameter when the index does not declare a partition key. | 
| Invalid SearchConditionExpression: An expression attribute name used in the document path is not defined; attribute name: <name> | The expression references an expression attribute name that ExpressionAttributeNames does not define. | Add the alias to ExpressionAttributeNames, or correct the alias spelling in the expression. | 
| Invalid SearchConditionExpression: An expression attribute value used in expression is not defined; attribute value: :value | The expression references a value placeholder that ExpressionAttributeValues does not define. | Add the placeholder to ExpressionAttributeValues, or correct the placeholder spelling in the expression. | 
| Invalid SearchConditionExpression: Attribute name is a reserved keyword; reserved keyword: <keyword> | A bare attribute name in the expression is a DynamoDB reserved word, for example name or bucket. | Alias the attribute with ExpressionAttributeNames, for example \#n mapped to name, and reference \#n in the expression. | 
| Invalid SearchConditionExpression: SearchConditionExpression cannot have conditions on nested attributes | A condition references a nested attribute path, for example a.b or a[0], or an alias that resolves to one. | SearchConditionExpression supports top-level attributes only. Project the nested value into a top-level attribute when the item is written. | 
| Invalid SearchConditionExpression: Invalid condition in SearchConditionExpression: Multiple attribute names used in one condition | A condition compares two attributes to each other, for example \#price > \#rating. | The right side of a comparison must be an expression attribute value placeholder (:value). | 
| Invalid SearchConditionExpression: The function is not allowed in a search condition; function: <name> | A condition calls a function that is not accepted inside a SearchConditionExpression, for example begins\_with, contains, attribute\_type, or size. | The only accepted functions are attribute\_exists and attribute\_not\_exists. Remove the disallowed function, or precompute the value and filter on an attribute declared in the SearchSchema. | 
| Invalid SearchConditionExpression: The IN operator list must contain only expression attribute values (:value), not attribute names | An entry in an IN list is an attribute name, whether plain, aliased, or nested, rather than a value placeholder. | Supply every IN list entry as an expression attribute value placeholder (:a, :b, and so on). | 
| Invalid SearchConditionExpression: The IN operator is provided with too many operands; number of operands: <count> | An IN list contains more than 100 value placeholders. | Reduce the IN list to 100 or fewer value placeholders. | 
| Invalid SearchConditionExpression: The BETWEEN operator bounds must be expression attribute values (:value), not attribute names | One or both bounds of a BETWEEN clause are attribute names rather than value placeholders. | Supply both bounds as expression attribute value placeholders (BETWEEN :lo AND :hi). | 
| Invalid SearchConditionExpression: The BETWEEN operator requires upper bound to be greater than or equal to lower bound; lower bound operand: AttributeValue: {N:<value>}, upper bound operand: AttributeValue: {N:<value>} | A BETWEEN clause has a lower bound greater than its upper bound. | Correct the request values. Equal bounds are accepted and match the single value. | 
| Invalid SearchConditionExpression: The BETWEEN operator requires same data type for lower and upper bounds; lower bound operand: AttributeValue: {N:<value>}, upper bound operand: AttributeValue: {S:<value>} | The two bounds of a BETWEEN clause are not the same DynamoDB attribute type. | Supply both bounds with the same type, for example two N values. | 
| Invalid SearchConditionExpression: The expression contains too many conditions; number of conditions: <count>, maximum: <max> | The expression contains more conditions than the maximum. Each comparison, BETWEEN, IN, and function counts as one. AND, OR, NOT, and parentheses do not count. | Reduce the number of conditions in the expression. For what counts as a condition, see [Condition limit](#VectorSearchFilterReference.ConditionLimit). | 
| Invalid SearchConditionExpression: The expression contains too many operators; operator count: <count> | The expression contains more operators than the service allows, even when it is within the condition limit. | Simplify the expression to use fewer operators. | 
| Value provided in ExpressionAttributeValues unused in expressions: keys: {:value} | ExpressionAttributeValues supplies a placeholder that no condition in the expression references. | Remove the unused placeholder, or reference it in the expression. | 
| Value provided in ExpressionAttributeNames unused in expressions: keys: {\#name} | ExpressionAttributeNames supplies an alias that no condition in the expression references. | Remove the unused alias, or reference it in the expression. | 

The following messages are reported in the partition key checks group, after the expression checks. They apply to a vector index that declares a vector index partition key (`HASH`) in its SearchSchema.


| Error message | Cause | Resolution | 
| --- | --- | --- | 
| SearchConditionExpression must be provided when SearchSchema has a HASH key | The vector index declares a partition key (HASH) in its SearchSchema, but the request supplied no SearchConditionExpression. | Supply a SearchConditionExpression with an equality condition on the partition key attribute. | 
| SearchConditionExpression must have all HASH attributes in configured SearchSchema | The expression omits a condition on the partition key attribute declared by the vector index SearchSchema. | Add an equality condition on the partition key attribute. The partition key condition is required in every SearchVectors request against an index that declares a partition key. | 
| SearchConditionExpression must use = on the HASH attribute, not inside OR or NOT; HASH attribute: <name> | A partition key condition uses an operator other than =, uses IN, uses BETWEEN, uses a function, or appears inside an OR or a NOT. | Place the partition key condition at the top level of the expression, join it to the rest with AND, and use =. | 
| SearchConditionExpression must contain only one condition on the HASH attribute; to search more than one HASH value, make one SearchVectors call for each value | The expression contains more than one condition that references the partition key attribute. | Remove the duplicate partition key conditions. A single SearchVectors call targets exactly one partition key value. | 

The following messages are reported in the attribute checks group, after the partition key checks. They identify the first condition with a fault, in the order in which the conditions appear in the expression.


| Error message | Cause | Resolution | 
| --- | --- | --- | 
| SearchConditionExpression must not contain any attributes that is not in SearchSchema. Invalid attribute: <name> | A condition references an attribute that is not declared in the SearchSchema of the index being searched. This includes an attribute\_exists or attribute\_not\_exists call on an attribute that is not in the SearchSchema. | Add the attribute to the SearchSchema when the index is created, or remove the condition. Attributes can be added to a SearchSchema only at vector index creation. | 
| SearchConditionExpression allows this operator only on Number (N) attributes; operator: <op>, attribute: <name>, attribute type: <type> | A range operator (<, <=, >, >=) or BETWEEN is applied to a String or Binary attribute. | Use =, <>, or IN for String and Binary attributes. If range filtering on the value is required, store a numeric form of the value as a Number attribute and declare it as an inline filter in the SearchSchema. | 
| Type of '<name>' attribute in SearchConditionExpression (<type>) does not match type in search schema (<type>) | A value placeholder (including one in an IN list) or the partition key value uses a DynamoDB type (S, N, or B) different from the type the SearchSchema declares for the attribute. | Supply the value in the declared attribute type. A Number attribute takes {"N": "..."}; a String attribute takes {"S": "..."}. | 