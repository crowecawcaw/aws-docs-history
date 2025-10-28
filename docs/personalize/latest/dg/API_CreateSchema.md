# CreateSchema

Creates an Amazon Personalize schema from the specified schema string. The schema you create
must be in Avro JSON format.

Amazon Personalize recognizes three schema variants. Each schema is associated with a dataset
type and has a set of required field and keywords. If you are creating a schema for a dataset in a Domain dataset group, you
provide the domain of the Domain dataset group.
You specify a schema when you call [CreateDataset](API_CreateDataset.md "API_CreateDataset.md").

For more information on schemas, see
[Datasets and schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

###### Related APIs

- [ListSchemas](API_ListSchemas.md "API_ListSchemas.md")
- [DescribeSchema](API_DescribeSchema.md "API_DescribeSchema.md")
- [DeleteSchema](API_DeleteSchema.md "API_DeleteSchema.md")

## Request Syntax

```
{
   "domain": "`string`",
   "name": "`string`",
   "schema": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[domain](#API_CreateSchema_RequestSyntax "#API_CreateSchema_RequestSyntax")**

The domain for the schema. If you are creating a schema for a dataset in a Domain dataset group, specify
the domain you chose when you created the Domain dataset group.

Type: String

Valid Values: `ECOMMERCE | VIDEO_ON_DEMAND`

Required: No

**[name](#API_CreateSchema_RequestSyntax "#API_CreateSchema_RequestSyntax")**

The name for the schema.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[schema](#API_CreateSchema_RequestSyntax "#API_CreateSchema_RequestSyntax")**

A schema in Avro JSON format.

Type: String

Length Constraints: Maximum length of 20000.

Required: Yes

## Response Syntax

```
{
   "schemaArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[schemaArn](#API_CreateSchema_ResponseSyntax "#API_CreateSchema_ResponseSyntax")**

The Amazon Resource Name (ARN) of the created schema.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateSchema.md "../../../goto/cli2/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateSchema.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateSchema.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateSchema.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateSchema.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateSchema.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateSchema.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateSchema.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateSchema.md "../../../goto/boto3/personalize-2018-05-22/CreateSchema.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateSchema.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateSchema.md")
