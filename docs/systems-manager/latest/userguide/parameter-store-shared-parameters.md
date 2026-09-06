

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Working with shared parameters in Parameter Store
<a name="parameter-store-shared-parameters"></a>

Sharing advanced parameters simplifies configuration data management in a multi-account environment. You can centrally store and manage your parameters and share them with other AWS accounts that need to reference them.

Parameter Store integrates with AWS Resource Access Manager (AWS RAM) to enable advanced parameter sharing. AWS RAM is a service that lets you share resources with other AWS accounts or through AWS Organizations.

With AWS RAM, you share resources that you own by creating a resource share. A resource share specifies the resources to share, permissions to grant, and the consumers with whom to share. Consumers can include:
+ Specific AWS accounts inside or outside of its organization in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ Its entire organization in AWS Organizations

For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)*.

This topic explains how to share parameters that you own, and how to use parameters that are shared with you.

**Topics**
+ [Prerequisites for sharing parameters](#prereqs)
+ [Sharing a parameter](#share)
+ [Stop sharing a shared parameter](#unshare)
+ [Identifying shared parameters](#identify)
+ [Accessing shared parameters](#accessing)
+ [Permissions sets for sharing parameters](#sharing-permissions)
+ [Maximum throughput for shared parameters](#throughput)
+ [Pricing for shared parameters](#pricing)
+ [Cross-account access for closed AWS accounts](#closed-accounts)

## Prerequisites for sharing parameters
<a name="prereqs"></a>

The following prerequisites must be met before you can share parameters from your account:
+ To share a parameter, you must own it in your AWS account. You can't share a parameter that has been shared with you.
+ To share a parameter, it must be in the advanced parameter tier. For information about parameter tiers, see [Choosing parameter tiers in Parameter Store](parameter-store-advanced-parameters.md). For information about changing an existing standard parameter to an advanced parameter, see [Changing a standard parameter to an advanced parameter](parameter-store-advanced-parameters-enabling.md).
+ To share a `SecureString` parameter, it must be encrypted with a customer managed key, and you must share the key separately through AWS Key Management Service. AWS managed keys cannot be shared. Parameters encrypted with the default AWS managed key can be updated to use a customer managed key instead. For AWS KMS key definitions, see [AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) in the *AWS Key Management Service Developer Guide*.
+ To share a parameter with your organization or an organizational unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

## Sharing a parameter
<a name="share"></a>

To share a parameter, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared. 

When you share a parameter that you own with other AWS accounts, you can choose from two AWS managed permissions to grant the consumers. For more information, see [Permissions sets for sharing parameters](#sharing-permissions). 

If you are part of an organization in AWS Organizations and sharing within your organization is enabled, you can grant consumers in your organization access from the AWS RAM console to the shared parameter. Otherwise, consumers receive an invitation to join the resource share and are granted access to the shared parameter after accepting the invitation.

You can share a parameter that you own using the AWS RAM console, or the AWS CLI.

**Note**  
While you can share a parameter using the Systems Manager [PutResourcePolicy](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutResourcePolicy.html) API operation, we recommend using AWS Resource Access Manager (AWS RAM) instead. This is because using `PutResourcePolicy` requires the extra step of promoting the parameter to a standard Resource Share using the AWS RAM [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html) API operation. Otherwise, the parameter won't be returned by the Systems Manager [DescribeParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html) API operation using the `--shared` option.

**To share a parameter that you own using the AWS RAM console**  
See [Creating a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

Make the following selections as you complete the procedure:
+ In the Step 1 page, for **Resources**, select `Parameter Store Advanced Parameter`, and then select the box of each parameter in the advanced parameter tier that you want to share.
+ In the Step 2 page, for **Managed permissions**, choose the permission to grant consumers, as described in [Permissions sets for sharing parameters](#sharing-permissions) later in this topic.

Choose other options based on your parameter sharing objectives.

**To share a parameter that you own using the AWS CLI**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command to add parameters to a new resource share.

Use the [associate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/associate-resource-share.html) command to add parameters to an existing resource share.

The following example creates a new resource share to share parameters with consumers in an organization and in an individual account.

```
aws ram create-resource-share \
    --name "MyParameter" \
    --resource-arns "arn:aws:ssm:us-east-2:123456789012:parameter/MyParameter" \
    --principals "arn:aws:organizations::123456789012:ou/o-63bEXAMPLE/ou-46xi-rEXAMPLE" "987654321098"
```

## Stop sharing a shared parameter
<a name="unshare"></a>

When you stop sharing a shared parameter, the consumer account can no longer access the parameter.

To stop sharing a parameter that you own, you must remove it from the resource share. You can do this using the Systems Manager console, AWS RAM console, or the AWS CLI.

**To stop sharing a parameter that you own using the AWS RAM console**  
See [Update a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) in the *AWS RAM User Guide*.

**To stop sharing a parameter that you own using the AWS CLI**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

## Identifying shared parameters
<a name="identify"></a>

Owners and consumers can identify shared parameters using the AWS CLI.

**To identify shared parameters using the AWS CLI**  
To identify shared parameters using the AWS CLI, you can choose from the Systems Manager `[describe-parameters](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-parameters.html)` command and the AWS RAM `[list-resources](https://docs.aws.amazon.com/cli/latest/reference/ram/list-resources.html)` command. 

When you use the `--shared` option with `describe-parameters`, the command returns the parameters that are shared with you.

The following is an example:

```
aws ssm describe-parameters --shared
```

## Accessing shared parameters
<a name="accessing"></a>

Consumers can access shared parameters using the AWS command line tools, and AWS SDKs. For consumer accounts, parameters shared with that account aren't included in the **My parameters** page.

**CLI Example: Accessing shared parameter details using the AWS CLI**  
To access shared parameter details using the AWS CLI, you can use the [get-parameter](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameter.html) or [get-parameters](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters.html) commands. You must specify the full parameter ARN as the `--name` in order to retrieve the parameter from another account.

The following is an example.

```
aws ssm get-parameter \
    --name arn:aws:ssm:us-east-2:123456789012:parameter/MySharedParameter
```

**Supported and unsupported integrations for shared parameters**  
Currently, you can use shared parameters in the following integration scenarios:
+ AWS CloudFormation [template parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types)
+ The [AWS Parameters and Secrets Lambda extension](ps-integration-lambda-extensions.md)
+ [Amazon Elastic Compute Cloud (EC2) launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/using-systems-manager-parameters.html)
+ Values for `ImageID` with the [EC2 RunInstances command](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) to create instances from an Amazon Machine Image (AMI)
+ [Retrieving parameter values in runbooks](https://repost.aws/knowledge-center/systems-manager-parameter-store) for Automation, a tool in Systems Manager

The following scenarios and integrated services do not currently support the use of shared parameters:
+ [Parameters in commands](sysman-param-runcommand.md) in Run Command, a tool in Systems Manager
+ AWS CloudFormation [dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html)
+ The [values of environment variables](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.parameter-store) in AWS CodeBuild
+ The [values of environment variables](https://docs.aws.amazon.com/apprunner/latest/dg/env-variable.html) in AWS App Runner
+ The [value of a secret](https://docs.aws.amazon.com/AmazonECS/latest/userguide/secrets-envvar-ssm-paramstore.html) in Amazon Elastic Container Service

## Permissions sets for sharing parameters
<a name="sharing-permissions"></a>

Consumer accounts receive read-only access to the parameters you share with them. The consumer can't update or delete the parameter. The consumer can't share the parameter with a third account. 

When you create a resource share in AWS Resource Access Manager for sharing your parameters, you can choose from two AWS managed permission sets to grant this read-only access:

**AWSRAMDefaultPermissionSSMParameterReadOnly**  
Allowed actions: `DescribeParameters`, `GetParameter`, `GetParameters`

**AWSRAMPermissionSSMParameterReadOnlyWithHistory**  
Allowed actions: `DescribeParameters`, `GetParameter`, `GetParameters`, `GetParameterHistory`

When you follow the steps in [Creating a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*, choose `Parameter Store Advanced Parameters` as the resource type. Select either of the managed permissions based on whether you want users to view parameter history.

**Note**  
If you're retrieving shared parameters programmatically (for example, using AWS Lambda) you might need to add the `ssm:GetResourcePolicies` and `ssm:PutResourcePolicy` permissions to any IAM roles calling AWS Resource Access Manager API actions.

## Maximum throughput for shared parameters
<a name="throughput"></a>

Systems Manager limits the maximum throughput (transactions per second) for the [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html) and [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html). operations. Throughput is enforced at the individual account level. Therefore, each account that consumes a shared parameter can use its maximum allowed throughput without being affected by other accounts. For more information about maximum throughput for parameters, see the following topics:
+ [Increasing Parameter Store throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html)
+ [Systems Manager Service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.

## Pricing for shared parameters
<a name="pricing"></a>

Cross-account sharing is only available in the advanced parameter tier. For advanced parameters, charges are incurred at the current price for the *storage* and *API usage* for each advanced parameter. The owning account is charged for storage of the advanced parameter. Any consuming account that makes an API call to a shared advanced parameter is charged for the parameter usage. 

For example, if Account A creates an advanced parameter, `MyAdvancedParameter`, that account is charged USD 0.05 per month to store the parameter. 

Account A then shares `MyAdvancedParameter` with Account B and Account C. During a month, the three accounts make calls to `MyAdvancedParameter`. The following table illustrates the charges they would incur for the number of calls each makes.

**Note**  
The charges in the following table are for illustration only. To verify current pricing, see [AWS Systems Manager Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store).


| Account | Number of calls | Charges | 
| --- | --- | --- | 
| Account A (owning account) | 10,000 calls |  +  One month advanced parameter storage: USD 0.05 <br />+  10,000 calls to `MyAdvancedParameter`: USD 0.05 <br />+  **Total: USD 0.10**   | 
| Account B (consuming account) | 20,000 calls |  +  20,000 calls to `MyAdvancedParameter`: USD 0.10 <br />+  **Total: USD 0.10**   | 
| Account C (consuming account) | 30,000 calls |  +  30,000 calls to `MyAdvancedParameter`: USD 0.15 <br />+  **Total: USD 0.15**   | 

## Cross-account access for closed AWS accounts
<a name="closed-accounts"></a>

If the AWS account that owns a shared parameter is closed, all consuming accounts lose access to the shared parameter. If the owning account is reopened within 90 days after the account is closed, consuming accounts regain access to the previously shared parameters. For more information about reopening an account during the Post-Closure Period, see [Accessing your AWS account after you close it](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-closing.html#accessing-after-closure) in the *AWS Account Management Reference Guide*.