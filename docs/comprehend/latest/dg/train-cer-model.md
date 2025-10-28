# Train custom entity recognizers (API)

To create and train a custom entity recognition model, use the Amazon Comprehend
[CreateEntityRecognizer](../APIReference/API_CreateEntityRecognizer.md "../APIReference/API_CreateEntityRecognizer.md") API operation

###### Topics

- [Training custom entity recognizers using the AWS Command Line Interface](#get-started-api-cer-cli "#get-started-api-cer-cli")
- [Training custom entity recognizers using the AWS SDK for Java](#get-started-api-cer-java "#get-started-api-cer-java")
- [Training custom entity recognizers using Python (Boto3)](#cer-python "#cer-python")

## Training custom entity recognizers using the AWS Command Line Interface

The following examples demonstrate using the `CreateEntityRecognizer` operation
and other associated APIs with the AWS CLI.

The examples are formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

Create a custom entity recognizer using the `create-entity-recognizer` CLI command. For information
about the input-data-config parameter, see [CreateEntityRecognizer](../APIReference/API_CreateEntityRecognizer.md "../APIReference/API_CreateEntityRecognizer.md") in the _Amazon Comprehend API Reference_.

```
aws comprehend create-entity-recognizer \
     --language-code en \
     --recognizer-name test-6 \
     --data-access-role-arn "arn:aws:iam::`account number`:role/service-role/AmazonComprehendServiceRole-role" \
     --input-data-config "EntityTypes=[{Type=PERSON}],Documents={S3Uri=s3://`Bucket Name`/`Bucket Path`/documents},
                Annotations={S3Uri=s3://`Bucket Name`/`Bucket Path`/annotations}" \
     --region `region`
```

List all entity recognizers in a Region using the
`list-entity-recognizers` CLI command..

```
aws comprehend list-entity-recognizers \
     --region `region`
```

Check Job Status of custom entity recognizers using the
`describe-entity-recognizer` CLI command..

```
aws comprehend describe-entity-recognizer \
     --entity-recognizer-arn arn:aws:comprehend:`region`:`account number`:entity-recognizer/test-6 \
     --region `region`
```

## Training custom entity recognizers using the AWS SDK for Java

This example creates a custom entity recognizer and trains the model, using Java

For Amazon Comprehend examples that use Java, see [Amazon Comprehend Java examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/comprehend "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/comprehend").

## Training custom entity recognizers using Python (Boto3)

Instantiate Boto3 SDK:

```
import boto3
import uuid
comprehend = boto3.client("comprehend", region_name="`region`")
```

Create entity recognizer:

```
response = comprehend.create_entity_recognizer(
    RecognizerName="Recognizer-Name-Goes-Here-{}".format(str(uuid.uuid4())),
    LanguageCode="en",
    DataAccessRoleArn="`Role ARN`",
    InputDataConfig={
        "EntityTypes": [
            {
                "Type": "`ENTITY_TYPE`"
            }
        ],
        "Documents": {
            "S3Uri": "s3://`Bucket Name`/`Bucket Path`/documents"
        },
        "Annotations": {
            "S3Uri": "s3://`Bucket Name`/`Bucket Path`/annotations"
        }
    }
)
recognizer_arn = response["EntityRecognizerArn"]
```

List all recognizers:

```
response = comprehend.list_entity_recognizers()
```

Wait for recognizer to reach TRAINED status:

```
while True:
    response = comprehend.describe_entity_recognizer(
        EntityRecognizerArn=recognizer_arn
    )

    status = response["EntityRecognizerProperties"]["Status"]
    if "IN_ERROR" == status:
        sys.exit(1)
    if "TRAINED" == status:
        break

    time.sleep(10)
```
