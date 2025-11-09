# Encrypt class

The `Encrypt` transform encrypts source columns using the AWS Key Management Service key.
The `Encrypt` transform can encrypt up to 128 MiB per cell. It will attempt to preserve the format on decryption.
To preserve the data type, the data type metadata must serialize to less than 1KB. Otherwise, you must set the
`preserve_data_type` parameter to false. The data type metadata will be stored in plaintext in the encryption context.

## Example

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

The output will be a PySpark DataFrame with the original `id` column and an additional column containing
the encrypted values of the `phone` column.

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

The `Encrypt` transform takes the `source\_columns` as `["phone"]` and the `kms\_key\_arn` as the value of the
`${KMS}` environment variable. The transformation encrypts the values in the `phone` column using the specified KMS key.
The resulting `df\_encrypt` DataFrame contains the original `id` column, the original `phone` column, and an additional column
named `phone\_encrypted` containing the encrypted values of the `phone` column.

## Methods

- [\_\_call\_\_](#aws-glue-api-pyspark-transforms-Encrypt-__call__ "#aws-glue-api-pyspark-transforms-Encrypt-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-Encrypt-apply "#aws-glue-api-crawler-pyspark-transforms-Encrypt-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-Encrypt-name "#aws-glue-api-crawler-pyspark-transforms-Encrypt-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeArgs "#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeReturn "#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeTransform "#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeErrors "#aws-glue-api-crawler-pyspark-transforms-Encrypt-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-Encrypt-describe "#aws-glue-api-crawler-pyspark-transforms-Encrypt-describe")

## \_\_call\_\_(spark_context,

data_frame,
source_columns,
kms_key_arn,
entity_type_filter=None,
preserve_data_type=None)

The `Encrypt` transform encrypts source columns using the AWS Key Management Service key.

- `source_columns` – An array of existing columns.
- `kms_key_arn` – The key ARN of the AWS Key Management Service key to use to Encrypt the source columns.
- `entity_type_filter` – Optional array of entity types. Can be used to encrypt only detected PII
  in free-text column.
- `preserve_data_type` – Optional boolean. Defaults to true. If false, the data type will not
  be stored.

## apply(cls, \*args, \*\*kwargs)

Inherited from `GlueTransform`
[apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply").

## name(cls)

Inherited from `GlueTransform`
[name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name").

## describeArgs(cls)

Inherited from `GlueTransform`
[describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs").

## describeReturn(cls)

Inherited from `GlueTransform`
[describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn").

## describeTransform(cls)

Inherited from `GlueTransform`
[describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform").

## describeErrors(cls)

Inherited from `GlueTransform`
[describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors").

## describe(cls)

Inherited from `GlueTransform`
[describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
