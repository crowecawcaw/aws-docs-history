

# `AWSSupportRemediator-EnableApiGatewayCacheEncryption`

**Description**

Enables encryption at rest for Amazon API Gateway REST API cache data.

The runbook targets methods where caching is enabled but encryption is disabled.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [API Gateway REST API cache data should be encrypted at rest](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-5).

If the API Gateway REST API stage does not exist, or all methods with caching enabled are already encrypted, the automation completes successfully without making changes.

Enabling cache data encryption updates the stage's method settings and invalidates existing cache entries for the affected methods. The backend services repopulate the cache as new requests arrive, which might cause a brief increase in backend load.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ RestApiId

  Type: String

  Description: (Required) The ID of the API Gateway REST API.
+ StageName

  Type: String

  Description: (Required) The name of the API Gateway stage.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `apigateway:GET`
+ `apigateway:PATCH`

**Document Steps**

1. **validateAPIGatewayStage** - Validates that the API Gateway REST API stage exists and determines whether any method with caching enabled has cache data encryption disabled. Builds the patch operations required to enable encryption on those methods.

1. **branchOnChangeRequired** - Branches on whether any method with caching enabled needs encryption. If no change is required, the runbook ends successfully.

1. **enableAPIGatewayCacheEncryption** - Applies the patch operations built in `validateAPIGatewayStage` to enable cache data encryption on the API Gateway REST API stage.

**Outputs**
+ validateAPIGatewayStage.ChangeRequired: Whether any method with caching enabled needs encryption.
+ validateAPIGatewayStage.ValidationMessage: A message describing the validation result when no change is required.
+ validateAPIGatewayStage.PatchOperations: The patch operations required to enable cache encryption on unencrypted methods.
+ validateAPIGatewayStage.InitialConfiguration: The method settings configuration before any change.
+ enableAPIGatewayCacheEncryption.UpdatedMethodSettings: The method settings configuration for the stage after the runbook enables encryption.