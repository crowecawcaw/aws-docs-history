# ListSchemas

Returns the list of schemas associated with the account. The response provides the
properties for each schema, including the Amazon Resource Name (ARN).
For more information on schemas, see [CreateSchema](API_CreateSchema.md "API_CreateSchema.md").

## Request Syntax

```
{
   "maxResults": `number`,
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[maxResults](#API_ListSchemas_RequestSyntax "#API_ListSchemas_RequestSyntax")**

The maximum number of schemas to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListSchemas_RequestSyntax "#API_ListSchemas_RequestSyntax")**

A token returned from the previous call to `ListSchemas` for getting
the next set of schemas (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "nextToken": "***string***",
   "schemas": [
      {
         "creationDateTime": ***number***,
         "domain": "***string***",
         "lastUpdatedDateTime": ***number***,
         "name": "***string***",
         "schemaArn": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_ListSchemas_ResponseSyntax "#API_ListSchemas_ResponseSyntax")**

A token used to get the next set of schemas (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

**[schemas](#API_ListSchemas_ResponseSyntax "#API_ListSchemas_ResponseSyntax")**

A list of schemas.

Type: Array of [DatasetSchemaSummary](API_DatasetSchemaSummary.md "API_DatasetSchemaSummary.md") objects

Array Members: Maximum number of 100 items.

## Errors

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListSchemas.md "../../../goto/cli2/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListSchemas.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListSchemas.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListSchemas.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListSchemas.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListSchemas.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListSchemas.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListSchemas.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListSchemas.md "../../../goto/boto3/personalize-2018-05-22/ListSchemas.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListSchemas.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListSchemas.md")
