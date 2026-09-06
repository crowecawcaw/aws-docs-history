

# CryptographicHash class
<a name="aws-glue-api-pyspark-transforms-CryptographicHash"></a>

 The `CryptographicHash` transform applies an algorithm to hash values in the column. 

## Example
<a name="pyspark-CryptographicHash-examples"></a>

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

secret = "${SECRET}"
sc = SparkContext()
spark = SparkSession(sc)

input_df = spark.createDataFrame(
    [
        (1, "1234560000"),
        (2, "1234560001"),
        (3, "1234560002"),
        (4, "1234560003"),
        (5, "1234560004"),
        (6, "1234560005"),
        (7, "1234560006"),
        (8, "1234560007"),
        (9, "1234560008"),
        (10, "1234560009"),
    ],
    ["id", "phone"],
)

try:
    df_output = pii.CryptographicHash.apply(
        data_frame=input_df,
        spark_context=sc,
        source_columns=["id", "phone"],
        secret_id=secret,
        algorithm="HMAC_SHA256",
        output_format="BASE64",
    )
    df_output.show()
except:
    print("Unexpected Error happened ")
    raise
```

## Output
<a name="pyspark-CryptographicHash-output"></a>

The output will be:

```
```
+---+------------+-------------------+-------------------+
| id| phone | id_hashed | phone_hashed |
+---+------------+-------------------+-------------------+
| 1| 1234560000 | QUI1zXTJiXmfIb... | juDBAmiRnnO3g... |
| 2| 1234560001 | ZAUWiZ3dVTzCo... | vC8lgUqBVDMNQ... |
| 3| 1234560002 | ZP4VvZWkqYifu... | Kl3QAkgswYpzB... |
| 4| 1234560003 | 3u8vO3wQ8EQfj... | CPBzK1P8PZZkV... |
| 5| 1234560004 | eWkQJk4zAOIzx... | aLf7+mHcXqbLs... |
| 6| 1234560005 | xtI9fZCJZCvsa... | dy2DFgdYWmr0p... |
| 7| 1234560006 | iW9hew7jnHuOf... | wwfGMCOEv6oOv... |
| 8| 1234560007 | H9V1pqvgkFhfS... | g9WKhagIXy9ht... |
| 9| 1234560008 | xDhEuHaxAUbU5... | b3uQLKPY+Q5vU... |
| 10| 1234560009 | GRN6nFXkxk349... | VJdsKt8VbxBbt... |
+---+------------+-------------------+-------------------+
```
```

 The transformation computes the cryptographic hashes of the values in the `id` and `phone` columns using the specified algorithm and secret key, and encodes the hashes in Base64 format. The resulting `df\_output` DataFrame contains all columns from the original `input\_df` DataFrame, plus the additional `id\_hashed` and `phone\_hashed` columns with the computed hashes. 

## Methods
<a name="aws-glue-api-pyspark-transforms-CryptographicHash-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-pyspark-transforms-CryptographicHash-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-CryptographicHash-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-CryptographicHash-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describeErrors)
+ [describe](#aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describe)

## \_\_call\_\_(spark\_context, data\_frame, source\_columns, secret\_id, algorithm=None, secret\_version=None, create\_secret\_if\_missing=False, output\_format=None, entity\_type\_filter=None)
<a name="aws-glue-api-pyspark-transforms-CryptographicHash-__call__"></a>

 The `CryptographicHash` transform applies an algorithm to hash values in the column. 
+ `source_columns` – An array of existing columns.
+ `secret_id` – The ARN of the Secrets Manager secret key. The key used in the hash-based message authentication code (HMAC) prefix algorithm to hash the source columns.
+ `secret_version` – Optional. Defaults to the latest secret version.
+ `entity_type_filter` – Optional array of entity types. Can be used to encrypt only detected PII in free-text column.
+ `create_secret_if_missing` – Optional boolean. If true will attempt to create the secret on behalf of the caller.
+ `algorithm` – The algorithm used to hash your data. Valid enum values: MD5, SHA1, SHA256, SHA512, HMAC\_MD5, HMAC\_SHA1, HMAC\_SHA256, HMAC\_SHA512.

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-CryptographicHash-apply"></a>

Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply).

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-CryptographicHash-name"></a>

Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name).

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describeArgs"></a>

Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs).

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describeReturn"></a>

Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn).

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describeTransform"></a>

Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform).

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describeErrors"></a>

Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors).

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-CryptographicHash-describe"></a>

Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe).