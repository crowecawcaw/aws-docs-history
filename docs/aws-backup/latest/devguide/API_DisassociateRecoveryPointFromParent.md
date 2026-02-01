# DisassociateRecoveryPointFromParent

This action to a specific child (nested) recovery point removes the relationship
between the specified recovery point and its parent (composite) recovery point.

## Request Syntax

```
DELETE /backup-vaults/`backupVaultName`/recovery-points/`recoveryPointArn`/parentAssociation HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_DisassociateRecoveryPointFromParent_RequestSyntax "#API_DisassociateRecoveryPointFromParent_RequestSyntax")**

The name of a logical container where the child (nested) recovery point
is stored. Backup vaults are identified by names that are unique to the account used
to create them and the AWS Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

**[recoveryPointArn](#API_DisassociateRecoveryPointFromParent_RequestSyntax "#API_DisassociateRecoveryPointFromParent_RequestSyntax")**

The Amazon Resource Name (ARN) that uniquely identifies the child
(nested) recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 204

```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**InvalidRequestException**

Indicates that something is wrong with the input to the request. For example, a
parameter is of the wrong type.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/cli2/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/DotNetSDKV4/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/SdkForCpp/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/SdkForGoV2/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/SdkForKotlin/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/boto3/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DisassociateRecoveryPointFromParent.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DisassociateRecoveryPointFromParent.md")
