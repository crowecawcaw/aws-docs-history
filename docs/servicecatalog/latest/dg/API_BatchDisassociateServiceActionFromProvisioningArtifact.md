# BatchDisassociateServiceActionFromProvisioningArtifact

Disassociates a batch of self-service actions from the specified provisioning artifact.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "ServiceActionAssociations": [
      {
         "ProductId": "`string`",
         "ProvisioningArtifactId": "`string`",
         "ServiceActionId": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_BatchDisassociateServiceActionFromProvisioningArtifact_RequestSyntax "#API_BatchDisassociateServiceActionFromProvisioningArtifact_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[ServiceActionAssociations](#API_BatchDisassociateServiceActionFromProvisioningArtifact_RequestSyntax "#API_BatchDisassociateServiceActionFromProvisioningArtifact_RequestSyntax")**

One or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.

Type: Array of [ServiceActionAssociation](API_ServiceActionAssociation.md "API_ServiceActionAssociation.md") objects

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Required: Yes

## Response Syntax

```
{
   "FailedServiceActionAssociations": [
      {
         "ErrorCode": "***string***",
         "ErrorMessage": "***string***",
         "ProductId": "***string***",
         "ProvisioningArtifactId": "***string***",
         "ServiceActionId": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[FailedServiceActionAssociations](#API_BatchDisassociateServiceActionFromProvisioningArtifact_ResponseSyntax "#API_BatchDisassociateServiceActionFromProvisioningArtifact_ResponseSyntax")**

An object that contains a list of errors, along with information to help you identify the self-service action.

Type: Array of [FailedServiceActionAssociation](API_FailedServiceActionAssociation.md "API_FailedServiceActionAssociation.md") objects

Array Members: Maximum number of 50 items.

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/cli2/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/boto3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact.md")
