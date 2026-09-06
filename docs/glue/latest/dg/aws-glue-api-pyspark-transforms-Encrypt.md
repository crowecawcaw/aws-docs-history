

# Encrypt class
<a name="aws-glue-api-pyspark-transforms-Encrypt"></a>

 The `Encrypt` transform encrypts source columns using the AWS Key Management Service key. The `Encrypt` transform can encrypt up to 128 MiB per cell. It will attempt to preserve the format on decryption. To preserve the data type, the data type metadata must serialize to less than 1KB. Otherwise, you must set the `preserve_data_type` parameter to false. The data type metadata will be stored in plaintext in the encryption context. 

## Example
<a name="pyspark-Encrypt-examples"></a>

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

kms = "${KMS}"
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
    df_encrypt = pii.Encrypt.apply(
        data_frame=input_df,
        spark_context=sc,
        source_columns=["phone"],
        kms_key_arn=kms
    )
except:
    print("Unexpected Error happened ")
    raise
```

## Output
<a name="pyspark-Encrypt-output"></a>

 The output will be a PySpark DataFrame with the original `id` column and an additional column containing the encrypted values of the `phone` column. 

```
```
+---+------------+-------------------------+
| id| phone | phone_encrypted |
+---+------------+-------------------------+
| 1| 1234560000| EncryptedData1234...abc |
| 2| 1234560001| EncryptedData5678...def |
| 3| 1234560002| EncryptedData9012...ghi |
| 4| 1234560003| EncryptedData3456...jkl |
| 5| 1234560004| EncryptedData7890...mno |
| 6| 1234560005| EncryptedData1234...pqr |
| 7| 1234560006| EncryptedData5678...stu |
| 8| 1234560007| EncryptedData9012...vwx |
| 9| 1234560008| EncryptedData3456...yz0 |
| 10| 1234560009| EncryptedData7890...123 |
+---+------------+-------------------------+
```
```

 The `Encrypt` transform takes the `source\_columns` as `["phone"]` and the `kms\_key\_arn` as the value of the `${KMS}` environment variable. The transformation encrypts the values in the `phone` column using the specified KMS key. The resulting `df\_encrypt` DataFrame contains the original `id` column, the original `phone` column, and an additional column named `phone\_encrypted` containing the encrypted values of the `phone` column. 

## Methods
<a name="aws-glue-api-pyspark-transforms-Encrypt-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-pyspark-transforms-Encrypt-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-Encrypt-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-Encrypt-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeErrors)
+ [describe](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describe)

## \_\_call\_\_(spark\_context, data\_frame, source\_columns, kms\_key\_arn, entity\_type\_filter=None, preserve\_data\_type=None)
<a name="aws-glue-api-pyspark-transforms-Encrypt-__call__"></a>

 The `Encrypt` transform encrypts source columns using the AWS Key Management Service key. 
+ `source_columns` – An array of existing columns.
+ `kms_key_arn` – The key ARN of the AWS Key Management Service key to use to Encrypt the source columns.
+ `entity_type_filter` – Optional array of entity types. Can be used to encrypt only detected PII in free-text column.
+ `preserve_data_type` – Optional boolean. Defaults to true. If false, the data type will not be stored.

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-Encrypt-apply"></a>

Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply).

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-Encrypt-name"></a>

Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name).

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-Encrypt-describeArgs"></a>

Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs).

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-Encrypt-describeReturn"></a>

Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn).

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-Encrypt-describeTransform"></a>

Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform).

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-Encrypt-describeErrors"></a>

Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors).

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-Encrypt-describe"></a>

Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe).