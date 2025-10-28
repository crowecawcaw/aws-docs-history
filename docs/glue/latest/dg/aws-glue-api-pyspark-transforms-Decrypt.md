# Decrypt class

The `Decrypt` transform decrypts inside of AWS Glue. Your data can also be decrypted outside of
AWS Glue with the AWS Encryption SDK. If the provided KMS key ARN does not match what was used to encrypt the
column, the decrypt operation fails.

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
    df_decrypt = pii.Decrypt.apply(
        data_frame=df_encrypt,
        spark_context=sc,
        source_columns=["phone"],
        kms_key_arn=kms
    )
    df_decrypt.show()
except:
    print("Unexpected Error happened ")
    raise

```

## Output

The output will be a PySpark DataFrame with the original `id` column and the decrypted `phone` column:

```

```

+---+------------+
| id| phone| +---+------------+
| 1| 1234560000|
| 2| 1234560001|
| 3| 1234560002|
| 4| 1234560003|
| 5| 1234560004|
| 6| 1234560005|
| 7| 1234560006|
| 8| 1234560007|
| 9| 1234560008|
| 10| 1234560009| +---+------------+ ` ` The `Encrypt` transform takes the `source\_columns` as `["phone"]` and the `kms\_key\_arn` as the value of the `${KMS}` environment variable. The transformation encrypts the values in the `phone` column using the specified KMS key. The encrypted DataFrame `df\_encrypt` is then passed to the `Decrypt` transform from the `awsglue.pii` module. It takes the `source\_columns` as `["phone"]` and the `kms\_key\_arn` as the value of the `${KMS}` environment variable. The transformation decrypts the encrypted values in the `phone` column using the same KMS key. The resulting `df\_decrypt` DataFrame contains the original `id` column and the decrypted `phone` column. ## Methods <br>• [\_\_call\_\_](#aws-glue-api-pyspark-transforms-Decrypt-__call__ "#aws-glue-api-pyspark-transforms-Decrypt-__call__") <br>• [apply](#aws-glue-api-crawler-pyspark-transforms-Decrypt-apply "#aws-glue-api-crawler-pyspark-transforms-Decrypt-apply") <br>• [name](#aws-glue-api-crawler-pyspark-transforms-Decrypt-name "#aws-glue-api-crawler-pyspark-transforms-Decrypt-name") <br>• [describeArgs](#aws-glue-api-crawler-pyspark-transforms-Decrypt-describeArgs "#aws-glue-api-crawler-pyspark-transforms-Decrypt-describeArgs") <br>• [describeReturn](#aws-glue-api-crawler-pyspark-transforms-Decrypt-describeReturn "#aws-glue-api-crawler-pyspark-transforms-Decrypt-describeReturn") <br>• [describeTransform](#aws-glue-api-crawler-pyspark-transforms-Decrypt-describeTransform "#aws-glue-api-crawler-pyspark-transforms-Decrypt-describeTransform") <br>• [describeErrors](#aws-glue-api-crawler-pyspark-transforms-Decrypt-describeErrors "#aws-glue-api-crawler-pyspark-transforms-Decrypt-describeErrors") <br>• [describe](#aws-glue-api-crawler-pyspark-transforms-Decrypt-describe "#aws-glue-api-crawler-pyspark-transforms-Decrypt-describe") ## \_\_call\_\_(spark_context, data_frame, source_columns, kms_key_arn) The `Decrypt` transform decrypts inside of AWS Glue. Your data can also be decrypted outside of AWS Glue with the AWS Encryption SDK. If the provided KMS key ARN does not match what was used to encrypt the column, the decrypt operation fails. <br>• `source_columns` – An array of existing columns. <br>• `kms_key_arn` – The key ARN of the AWS Key Management Service key to use to decrypt the source columns. ## apply(cls, \*args, \*\*kwargs) Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply"). ## name(cls) Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name"). ## describeArgs(cls) Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs"). ## describeReturn(cls) Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn"). ## describeTransform(cls) Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform"). ## describeErrors(cls) Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors"). ## describe(cls) Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
