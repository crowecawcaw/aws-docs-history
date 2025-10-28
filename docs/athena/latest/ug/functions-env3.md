# Athena engine version 3 functions

Functions in Athena engine version 3 are based on Trino. For information about Trino functions, operators,
and expressions, see [Functions and
operators](https://trino.io/docs/current/functions.html "https://trino.io/docs/current/functions.html") and the following subsections from the Trino documentation.

- [Aggregate](https://trino.io/docs/current/functions/aggregate.html "https://trino.io/docs/current/functions/aggregate.html")
- [Array](https://trino.io/docs/current/functions/array.html "https://trino.io/docs/current/functions/array.html")
- [Binary](https://trino.io/docs/current/functions/binary.html "https://trino.io/docs/current/functions/binary.html")
- [Bitwise](https://trino.io/docs/current/functions/bitwise.html "https://trino.io/docs/current/functions/bitwise.html")
- [Color](https://trino.io/docs/current/functions/color.html "https://trino.io/docs/current/functions/color.html")
- [Comparison](https://trino.io/docs/current/functions/comparison.html "https://trino.io/docs/current/functions/comparison.html")
- [Conditional](https://trino.io/docs/current/functions/conditional.html "https://trino.io/docs/current/functions/conditional.html")
- [Conversion](https://trino.io/docs/current/functions/conversion.html "https://trino.io/docs/current/functions/conversion.html")
- [Date and
  time](https://trino.io/docs/current/functions/datetime.html "https://trino.io/docs/current/functions/datetime.html")
- [Decimal](https://trino.io/docs/current/functions/decimal.html "https://trino.io/docs/current/functions/decimal.html")
- [Geospatial](https://trino.io/docs/current/functions/geospatial.html "https://trino.io/docs/current/functions/geospatial.html")
- [HyperLogLog](https://trino.io/docs/current/functions/hyperloglog.html "https://trino.io/docs/current/functions/hyperloglog.html")
- [IP
  Address](https://trino.io/docs/current/functions/ipaddress.html "https://trino.io/docs/current/functions/ipaddress.html")
- [JSON](https://trino.io/docs/current/functions/json.html "https://trino.io/docs/current/functions/json.html")
- [Lambda](https://trino.io/docs/current/functions/lambda.html "https://trino.io/docs/current/functions/lambda.html")
- [Logical](https://trino.io/docs/current/functions/logical.html "https://trino.io/docs/current/functions/logical.html")
- [Machine
  learning](https://trino.io/docs/current/functions/ml.html "https://trino.io/docs/current/functions/ml.html")
- [Map](https://trino.io/docs/current/functions/map.html "https://trino.io/docs/current/functions/map.html")
- [Math](https://trino.io/docs/current/functions/math.html "https://trino.io/docs/current/functions/math.html")
- [Quantile
  digest](https://trino.io/docs/current/functions/qdigest.html "https://trino.io/docs/current/functions/qdigest.html")
- [Regular
  expression](https://trino.io/docs/current/functions/regexp.html "https://trino.io/docs/current/functions/regexp.html")
- [Session](https://trino.io/docs/current/functions/session.html "https://trino.io/docs/current/functions/session.html")
- [Set
  Digest](https://trino.io/docs/current/functions/setdigest.html "https://trino.io/docs/current/functions/setdigest.html")
- [String](https://trino.io/docs/current/functions/string.html "https://trino.io/docs/current/functions/string.html")
- [Table](https://trino.io/docs/current/functions/table.html "https://trino.io/docs/current/functions/table.html")
- [Teradata](https://trino.io/docs/current/functions/teradata.html "https://trino.io/docs/current/functions/teradata.html")
- [T-Digest](https://trino.io/docs/current/functions/tdigest.html "https://trino.io/docs/current/functions/tdigest.html")
- [URL](https://trino.io/docs/current/functions/url.html "https://trino.io/docs/current/functions/url.html")
- [UUID](https://trino.io/docs/current/functions/uuid.html "https://trino.io/docs/current/functions/uuid.html")
- [Window](https://trino.io/docs/current/functions/window.html "https://trino.io/docs/current/functions/window.html")

## invoker_principal() function

The `invoker_principal` function is unique to Athena engine version 3 and is not found in
Trino.

Returns a `VARCHAR` that contains the ARN of the principal (IAM role or
Identity Center identity) that ran the query calling the function. For example, if the
query invoker uses the permissions of an IAM role to run the query, the function
returns the ARN of the IAM role. The role that runs the query must allow the
`LakeFormation:GetDataLakePrincipal` action.

### Usage

```
SELECT invoker_principal()
```

The following table shows an example result.

| #   | \_col0                                 |
| --- | -------------------------------------- |
| 1   | arn:aws:iam::`111122223333`:role/Admin |
