Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# farmFingerprint64 function

Computes the farmhash value of the input argument using the `Fingerprint64` function.

## Syntax

```
farmFingerprint64(*expression*)
```

## Argument

_expression_

The input expression must be a `VARCHAR` or `VARBYTE` data type.

## Return type

The `farmFingerprint64` function returns a `BIGINT`.

## Example

The following example returns the `farmFingerprint64` value of `Amazon Redshift` that is input as a `VARCHAR` data type.

```
SELECT farmFingerprint64('Amazon Redshift');
```

```

  farmfingerprint64
---------------------
 8085098817162212970
```

The following example returns the `farmFingerprint64` value of `Amazon Redshift` that is input as a `VARBYTE` data type.

```
SELECT farmFingerprint64('Amazon Redshift'::varbyte);
```

```

  farmfingerprint64
---------------------
 8085098817162212970
```
