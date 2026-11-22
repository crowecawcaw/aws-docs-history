

# Configure a custom execution role template for StackSets

By default, StackSets with service-managed permissions creates an execution role named `stacksets-exec-*` in each target account. StackSets attaches the `AdministratorAccess` policy to this role. You can't provision nested stacks, transforms, or macros with the default execution role.

With a *custom execution role template*, you provide a CloudFormation template that defines an IAM role with only the permissions that your workloads require. You can use a custom execution role to provision nested stacks, transforms, and macros.

When you specify an execution role template, StackSets deploys the template as a stack in each target account when it first creates stack instances in that account. The stack creates your custom IAM role, and StackSets uses that role for all subsequent operations in the account. Deploying the execution role stack takes several minutes per target account, and can take several hours when you deploy to many target accounts.

**Note**  
Custom execution role templates are supported only with *service-managed* permissions. To control the resources that users can deploy with *self-managed* permissions, see [Control the resources that users can include in specific StackSets](stacksets-prereqs-self-managed.md#stacksets-prereqs-executionrole).

**Topics**
+ [Prerequisites](#stacksets-custom-execution-role-prereqs)
+ [Execution role template requirements](#stacksets-custom-execution-role-requirements)
+ [Permissions](#stacksets-custom-execution-role-permissions)
+ [Execution role stack lifecycle](#stacksets-custom-execution-role-lifecycle)
+ [Create a StackSet with a custom execution role template](#stacksets-custom-execution-role-create)
+ [Update the execution role template](#stacksets-custom-execution-role-update)
+ [View the current execution role template](#stacksets-custom-execution-role-view)
+ [StackSet output bucket](#stacksets-custom-execution-role-output-bucket)
+ [Example execution role templates](#stacksets-custom-execution-role-examples)
+ [Troubleshoot custom execution role template errors](#stacksets-custom-execution-role-troubleshooting)
+ [Considerations](#stacksets-custom-execution-role-considerations)

## Prerequisites
<a name="stacksets-custom-execution-role-prereqs"></a>

Before you configure a custom execution role template, make sure that you have the following:
+ Trusted access with AWS Organizations activated, which creates the `AWSServiceRoleForCloudFormationStackSetsOrgAdmin` service-linked role in your management account. For more information, see [Activate trusted access](stacksets-orgs-activate-trusted-access.md).
+ The ID of your organization's management account, which you specify in the trust policy of your execution role template.

## Execution role template requirements
<a name="stacksets-custom-execution-role-requirements"></a>

Your execution role template must meet all of the following requirements. If the template doesn't meet a requirement, the [CreateStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackSet.html) or [UpdateStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html) operation returns a validation error.

A single IAM role resource  
The template must contain exactly one resource, and that resource must be of type [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html). StackSets rejects templates that contain multiple resources, or a resource of any other type.  
The role must not specify a `Path` property. An absent `Path`, or a `Path` of `/`, is allowed.  
The execution role name must begin with `stacksets-exec-custom-`, for example `stacksets-exec-custom-my-role`. StackSets names its own default execution role `stacksets-exec-{{hash}}`. Use the distinct prefix to tell a custom execution role from a default one by name alone. The prefix also keeps the role within the scope of the target account's service-linked role.  
The name must also satisfy the IAM role name constraints: at most 64 characters, made up of alphanumeric characters and the characters `_+=,.@-`.  
The role name must be the same across all stack instances. Don't use account-specific or AWS Region-specific values in the `RoleName` property.

A trust policy that trusts the StackSets service-linked role  
The IAM role must include an `AssumeRolePolicyDocument` that grants `sts:AssumeRole` access to the StackSets service-linked role in your management account. The trust policy must contain exactly one `Statement`, and that statement must specify exactly one AWS principal, in the following format.  

```
arn:aws:iam::{{management-account-id}}:role/aws-service-role/stacksets.cloudformation.amazonaws.com/AWSServiceRoleForCloudFormationStackSetsOrgAdmin
```
Replace {{management-account-id}} with the ID of your organization's management account.

An output named `StackSetExecutionRoleName`  
The template must define an output with the key `StackSetExecutionRoleName`, and the value of that output must be the name of the IAM role that the template creates. StackSets reads this output only to validate that the role that was provisioned matches the execution role name that's configured on the StackSet.  
If the `StackSetExecutionRoleName` output is missing or misspelled, the template fails validation. Make sure that the output key matches exactly.

No nested stacks or transforms  
The execution role template must not include nested stack resources (AWS::CloudFormation::Stack) or CloudFormation transforms, such as AWS::Serverless-2016-10-31 or custom macros.  
This restriction applies only to the execution role template itself. The StackSet template that the custom execution role deploys *can* include nested stacks, transforms, and macros.

## Permissions
<a name="stacksets-custom-execution-role-permissions"></a>

The following topics describe the permissions that a custom execution role needs, whose account the trust policy must name, and the capabilities that your StackSet operation must acknowledge.

### Minimum permissions for the custom execution role
<a name="stacksets-custom-execution-role-minimum-permissions"></a>

The role that your execution role template defines needs permissions for every action that your StackSet template performs in the target account, and it always needs full CloudFormation permissions. At minimum, grant `cloudformation:*`: StackSets creates, updates, deletes, and describes stacks in the target account on your behalf, and a role without full CloudFormation permissions can't complete stack instance operations.

Add the service actions and resources that your own StackSet template requires alongside that. For an example of this minimum, see *Example permissions policy 2* in [Grant self-managed permissions](stacksets-prereqs-self-managed.md).

### Trust policy for delegated administrators
<a name="stacksets-custom-execution-role-delegated-admin"></a>

The trust policy in your execution role template must always name the management account, even when a delegated administrator creates or updates the StackSet. StackSets assumes the execution role from the `AWSServiceRoleForCloudFormationStackSetsOrgAdmin` service-linked role, which is in the management account and not in the delegated administrator's account.

If you specify the delegated administrator's account ID instead, the operation fails with `Account ID in principal ARN must match stackset management account ID`.

### Capabilities for nested stacks, transforms, and macros
<a name="stacksets-custom-execution-role-capabilities"></a>

With a custom execution role, you can provision nested stacks, transforms, and macros in a target account. The role isn't sufficient on its own: because these resources have custom processing, you must also acknowledge `CAPABILITY_AUTO_EXPAND` for the StackSet operation.

Specify both of the following capabilities when your StackSet template uses any of them:
+ `CAPABILITY_NAMED_IAM` – always required when you specify a custom execution role template, because that template creates a named IAM role.
+ `CAPABILITY_AUTO_EXPAND` – required when your StackSet template contains nested stacks (AWS::CloudFormation::Stack), transforms, or macros.

```sh
$ aws cloudformation create-stack-set \
  --stack-set-name {{my-stack-set}} \
  --template-body file://{{my-stackset-template.yaml}} \
  --permission-model SERVICE_MANAGED \
  --execution-role-template-body file://{{execution-role-template.yaml}} \
  --execution-role-name {{stacksets-exec-custom-my-role}} \
  --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

**Note**  
`CAPABILITY_AUTO_EXPAND` applies to your StackSet template, not to the execution role template. The execution role template itself must never contain nested stacks or transforms. For more information, see [Execution role template requirements](#stacksets-custom-execution-role-requirements).

## Execution role stack lifecycle
<a name="stacksets-custom-execution-role-lifecycle"></a>

StackSets provisions the execution role template as a CloudFormation stack in each target account. It provisions the role at the following times:
+ The first time you create a stack instance in that target account. Later stack instance operations in an account that's already been provisioned reuse the existing role.
+ Whenever you update the execution role template on the StackSet. Because an update applies to all existing stack instances, StackSets reprovisions the role in every target account that the StackSet has already deployed to.

The stack name uses the following format, where any colons in the StackSet ID are replaced by dashes.

```
stacksets-exec-role-stack-{{stackset-region}}-{{stackset-id}}-{{short-uuid}}
```

For example, for a StackSet named `myStackSet` that was created in `us-west-2`, the stack name might look like the following.

```
stacksets-exec-role-stack-us-west-2-myStackSet-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee-12345678
```

If the resulting name exceeds the maximum stack name length, StackSets truncates the StackSet ID, starting from the end.

```
stacksets-exec-role-stack-us-west-2-myStackSet-aaaaaaaa-bbbb-cccc-dd-12345678
```

The execution role stack is always created in the home AWS Region of the partition, for example `us-east-1` for the `aws` partition and `cn-north-1` for the `aws-cn` partition, regardless of the Regions that you deploy stack instances to.

**Note**  
StackSets doesn't delete the execution role stack for you. The stack remains in the target account after you delete the StackSet, or after you change the StackSet back to the default execution role.

## Create a StackSet with a custom execution role template
<a name="stacksets-custom-execution-role-create"></a>

To create a StackSet that uses a custom execution role, specify the following parameters in your [CreateStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackSet.html) request:
+ Exactly one of the following. If you specify both, the operation returns an error.
  + `ExecutionRoleTemplateBody` – the execution role template body, as an inline string in JSON or YAML format.
  + `ExecutionRoleTemplateUrl` – the Amazon S3 URL of the execution role template file.
+ `ExecutionRoleName` – the name of the execution role that StackSets uses for StackSet operations in your target accounts. Set this name when you use custom execution roles. If it doesn't match the name of the role that your execution role template provisions, the stack instance deployments fail for that account.
+ `Capabilities` – `CAPABILITY_NAMED_IAM` is required when you specify an execution role template. If your StackSet template contains nested stacks, transforms, or macros, you must also specify `CAPABILITY_AUTO_EXPAND`. For more information about capabilities, see [Capabilities for nested stacks, transforms, and macros](#stacksets-custom-execution-role-capabilities).

You can also optionally specify `StackSetOutputBucket`, the name of an Amazon S3 bucket where StackSets stores a copy of the execution role template. For more information about the StackSet output bucket, see [StackSet output bucket](#stacksets-custom-execution-role-output-bucket).

### Create a StackSet with a custom execution role (console)
<a name="stacksets-custom-execution-role-create-console"></a>

**To create a StackSet with a custom execution role**

1. Follow the procedure in [Create a StackSet with service-managed permissions (console)](stacksets-orgs-associate-stackset-with-org.md#stacksets-orgs-associate-stackset-with-org-console).

1. On the **Specify template** page, under **Permissions**, choose **Service-managed permissions**.

1. Under **Execution role**, choose **Set execution role**. By default, the wizard uses **Use default execution role**, which is the administrator access role for the StackSet.

1. Specify your execution role template in one of the following ways:
   + Choose **Amazon S3 URL**, and then enter the Amazon S3 URL of your execution role template.
   + Choose **Upload a template file**, and then choose your local execution role template file.
**Note**  
If the operation returns a validation error, your template doesn't meet one of the requirements in [Execution role template requirements](#stacksets-custom-execution-role-requirements). For the specific errors and how to resolve them, see [Troubleshoot custom execution role template errors](#stacksets-custom-execution-role-troubleshooting).

1. For **IAM execution role name**, enter the execution role name to set on the StackSet. This name must match the name of the role that your execution role template provisions.

1. (Optional) For the StackSet output bucket, choose the Amazon S3 bucket where you want StackSets to store a copy of the execution role template. By default, StackSets uses the bucket that the template was uploaded from.

1. Complete the remaining steps of the wizard. On the **Review** page, you can review your execution role template under **View execution role template**.

### Create a StackSet with a custom execution role (AWS CLI)
<a name="stacksets-custom-execution-role-create-cli"></a>

To provide the execution role template inline, use the `--execution-role-template-body` parameter. If the operation returns a validation error, see [Troubleshooting](#stacksets-custom-execution-role-troubleshooting).

```sh
$ aws cloudformation create-stack-set \
  --stack-set-name {{my-stack-set}} \
  --template-body file://{{my-stackset-template.yaml}} \
  --permission-model SERVICE_MANAGED \
  --execution-role-template-body file://{{execution-role-template.yaml}} \
  --execution-role-name {{stacksets-exec-custom-my-role}} \
  --stack-set-output-bucket {{amzn-s3-demo-bucket}} \
  --capabilities CAPABILITY_NAMED_IAM
```

To provide the execution role template from Amazon S3, use the `--execution-role-template-url` parameter instead.

```sh
$ aws cloudformation create-stack-set \
  --stack-set-name {{my-stack-set}} \
  --template-body file://{{my-stackset-template.yaml}} \
  --permission-model SERVICE_MANAGED \
  --execution-role-template-url https://s3.amazonaws.com/{{amzn-s3-demo-bucket}}/{{execution-role-template.yaml}} \
  --execution-role-name {{stacksets-exec-custom-my-role}} \
  --stack-set-output-bucket {{amzn-s3-demo-bucket}} \
  --capabilities CAPABILITY_NAMED_IAM
```

**Note**  
When you provide the template from Amazon S3, make sure that the Amazon S3 bucket policy allows access from CloudFormation. The URL must be a valid Amazon S3 URL that specifies both a bucket and a key.

## Update the execution role template
<a name="stacksets-custom-execution-role-update"></a>

To update the execution role template for an existing StackSet, call [UpdateStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html) with a new `ExecutionRoleTemplateBody` or `ExecutionRoleTemplateUrl`. The same validation requirements apply, with the following differences:
+ `ExecutionRoleName` isn't required if the execution role name is already configured and isn't changing.
+ Because updating the execution role template updates all existing stack instances, you can't specify deployment targets in the same operation.

```sh
$ aws cloudformation update-stack-set \
  --stack-set-name {{my-stack-set}} \
  --execution-role-template-body file://{{updated-execution-role-template.yaml}} \
  --capabilities CAPABILITY_NAMED_IAM
```

StackSets reprovisions the execution role in every target account that the StackSet has already deployed to, and uses the updated template for deployments to new target accounts.

To update the execution role template in the console, choose **Replace current execution role** when you update the StackSet. This option lets you enter the Amazon S3 URL of an existing template or upload a local template file. You can also update the execution role name, either on its own or at the same time as the template. The name must always match the name of the role that your execution role template provisions, so change the name on its own only when the template already provisions a role with that name.

### Revert to the default execution role
<a name="stacksets-custom-execution-role-revert"></a>

To change a StackSet back to the default execution role with `AdministratorAccess`, set the `UseAdminExecutionRole` parameter to `true`.

```sh
$ aws cloudformation update-stack-set \
  --stack-set-name {{my-stack-set}} \
  --use-admin-execution-role
```

In the console, choose **Use default execution role** when you update the StackSet.

## View the current execution role template
<a name="stacksets-custom-execution-role-view"></a>

When you call [DescribeStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackSet.html), the response includes information about the configured execution role template. If your StackSet has an output bucket configured, the response returns the location of the copy of the template in the `StackSetOutputBucketPath` field.

```sh
$ aws cloudformation describe-stack-set \
  --stack-set-name {{my-stack-set}}
```

**Note**  
You see the `StackSetOutputBucketPath` field in the response whenever you have an output bucket configured. Its presence doesn't guarantee that StackSets successfully uploaded the object.

In the console, the execution role template is visible if the StackSet output bucket is configured and accessible. On the StackSet details page, expand **Execution role template** in the **Permissions** section to view the template, with the execution role name displayed above it. Choose **View in S3** to open the location where the template is stored. If the template isn't stored in a bucket, no template is shown.

When you update a StackSet, the **Use current execution role** option displays the custom execution role template that the StackSet currently uses.

## StackSet output bucket
<a name="stacksets-custom-execution-role-output-bucket"></a>

When you create or update a StackSet with an execution role template, StackSets validates the template and stores it in an internal service-managed Amazon S3 bucket.

To read the stored template yourself, specify the `StackSetOutputBucket` parameter when you call CreateStackSet or UpdateStackSet. If provided, StackSets attempts to upload a copy of the execution role template to your bucket when you call DescribeStackSet, so that you can maintain visibility into the stored template from your own Amazon S3 bucket.

The location of that copy is called the *StackSet output bucket path*, and it uses the following format.

```
s3://{{bucket-name}}/aws-cloudformation-stacksets/{{stack-set-name}}.{{stack-set-uuid}}/output.json
```

The DescribeStackSet response returns this location in the `StackSetOutputBucketPath` field. In the path, any colons in the StackSet ID are replaced by periods.

```json
{
  "StackSet": {
    "StackSetName": "my-stack-set",
    "StackSetId": "my-stack-set:1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    "StackSetOutputBucketPath": "s3://amzn-s3-demo-bucket/aws-cloudformation-stacksets/my-stack-set.1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d/output.json"
  }
}
```

You can download the stored template directly from this Amazon S3 path.

```sh
$ aws s3 cp s3://{{amzn-s3-demo-bucket}}/aws-cloudformation-stacksets/{{my-stack-set.1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d}}/output.json .
```

If you specify your own output bucket, make sure that the following are true:
+ The Amazon S3 bucket exists in the same AWS Region as the StackSet.
+ The bucket policy allows the CloudFormation service principal (`cloudformation.amazonaws.com`) to perform `s3:PutObject` on the specified path.

**Note**  
If the output bucket isn't accessible during CreateStackSet or UpdateStackSet, the operation might return a validation error.  
If the output bucket isn't accessible during DescribeStackSet, StackSets ignores the failure and the object doesn't appear in the bucket. The response still includes the `StackSetOutputBucketPath` field.

## Example execution role templates
<a name="stacksets-custom-execution-role-examples"></a>

The following examples show valid execution role templates that you can customize for your use case. In each example, replace `{{111122223333}}` with the ID of your management account.

### Example: Least-privilege execution role (YAML)
<a name="stacksets-custom-execution-role-example-least-privilege"></a>

The following template creates an execution role with permissions scoped to specific AWS services.

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: Custom execution role for CloudFormation StackSets
Resources:
  StackSetExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: stacksets-exec-custom-ExecutionRole
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              AWS: arn:aws:iam::{{111122223333}}:role/aws-service-role/stacksets.cloudformation.amazonaws.com/AWSServiceRoleForCloudFormationStackSetsOrgAdmin
            Action: sts:AssumeRole
      Policies:
        - PolicyName: StackSetExecutionPolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - s3:CreateBucket
                  - s3:DeleteBucket
                  - s3:PutBucketPolicy
                  - s3:GetBucketPolicy
                Resource: "arn:aws:s3:::amzn-s3-demo-bucket"
              - Effect: Allow
                Action: "cloudformation:*"
                Resource: "*"
Outputs:
  StackSetExecutionRoleName:
    Value: stacksets-exec-custom-ExecutionRole
    Description: Name of the execution role that this template creates
```

### Example: Execution role with a managed policy (JSON)
<a name="stacksets-custom-execution-role-example-managed-policy"></a>

The following template creates an execution role and attaches an AWS managed policy.

**Note**  
The managed policy in this example is read-only, so it doesn't grant enough permissions for successful StackSet operations. Replace it with a policy that grants the permissions that your StackSet template requires.

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Custom execution role for CloudFormation StackSets",
  "Resources": {
    "StackSetExecutionRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "RoleName": "stacksets-exec-custom-ExecutionRole",
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/aws-service-role/stacksets.cloudformation.amazonaws.com/AWSServiceRoleForCloudFormationStackSetsOrgAdmin"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "ManagedPolicyArns": [
          "arn:aws:iam::aws:policy/AWSCloudFormationReadOnlyAccess"
        ]
      }
    }
  },
  "Outputs": {
    "StackSetExecutionRoleName": {
      "Value": "stacksets-exec-custom-ExecutionRole",
      "Description": "Name of the execution role that this template creates"
    }
  }
}
```

### Example: Return the role name with Ref (YAML)
<a name="stacksets-custom-execution-role-example-ref"></a>

The following template uses `!Ref` on the IAM role resource to return the role name in the output, instead of hardcoding it. When you use `!Ref` on an AWS::IAM::Role resource, CloudFormation returns the role name. We recommend this approach. It prevents the `RoleName` property and the output value from drifting apart, even if you use parameters or conditions to determine the role name.

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: Custom execution role using Ref for dynamic role name output
Resources:
  StackSetExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: stacksets-exec-custom-ExecutionRole
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              AWS: arn:aws:iam::{{111122223333}}:role/aws-service-role/stacksets.cloudformation.amazonaws.com/AWSServiceRoleForCloudFormationStackSetsOrgAdmin
            Action: sts:AssumeRole
      Policies:
        - PolicyName: StackSetExecutionPolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - ec2:Describe*
                  - ec2:CreateTags
                  - ec2:RunInstances
                  - ec2:TerminateInstances
                Resource: "*"
              - Effect: Allow
                Action: "cloudformation:*"
                Resource: "*"
Outputs:
  StackSetExecutionRoleName:
    Value: !Ref StackSetExecutionRole
    Description: Returns the role name dynamically with Ref
```

## Troubleshoot custom execution role template errors
<a name="stacksets-custom-execution-role-troubleshooting"></a>

If your execution role template fails validation, StackSets can't deploy to your target accounts. Use the following table to identify the cause of a validation error and resolve it.

The following table lists common errors that you might encounter when you configure a custom execution role template. Most of them come from template validation, and fall into three groups: the structure of the template, the IAM properties of the role it defines, and the execution role name.


|  Error code  |  Error message  |  Description  |  Resolution  | 
| --- | --- | --- | --- | 
| `ValidationException` | `The execution role template must not contain nested stacks or transforms` | The template includes a nested stack resource (AWS::CloudFormation::Stack), or it declares a transform. | Remove all nested stack resources and transform declarations from the execution role template. | 
| `ValidationException` | `The execution role template must contain exactly 1 resource, of type AWS::IAM::Role` | The template contains more than one resource, or its single resource isn't of type AWS::IAM::Role. | Define exactly one resource, of type AWS::IAM::Role, and remove any additional resources. | 
| `ValidationException` | `IAM Role must contain AssumeRolePolicyDocument` | The IAM role in the template has no `AssumeRolePolicyDocument` property. | Add an `AssumeRolePolicyDocument` that grants `sts:AssumeRole` to the StackSets service-linked role in your management account. | 
| `ValidationException` | `AssumeRolePolicyDocument must contain exactly 1 statement` | The trust policy has either no statements or more than one statement. | Reduce the trust policy to exactly one statement that grants `sts:AssumeRole`. | 
| `ValidationException` | `AssumeRolePolicyDocument must contain exactly 1 principal` | The statement's `Principal.AWS` value is missing, or it's a list of principals instead of a single string. | Specify `Principal.AWS` as a single string containing the ARN of the StackSets organization administrator service-linked role. | 
| `ValidationException` | `Principal must match format: arn:aws:iam::<account-id>:role/aws-service-role/<service-principal>/AWSServiceRoleForCloudFormationStackSetsOrgAdmin` | The principal ARN doesn't follow the required format for the StackSets service-linked role. | Use the ARN format described in [Execution role template requirements](#stacksets-custom-execution-role-requirements). | 
| `ValidationException` | `Account ID in principal ARN must match stackset management account ID` | The account ID in the service-linked role ARN isn't the management account that the StackSet belongs to. | Make sure that the 12-digit account ID in the principal ARN matches your management account ID. | 
| `ValidationException` | `The IAM role in the execution role template must not specify a Path` | The role defines a `Path` property with a value other than `/`. | Remove the `Path` property, or set it to `/`. | 
| `ValidationException` | `The execution role template must contain 1 output with key: StackSetExecutionRoleName` | Your template doesn't define the required output, or it uses a different key name. | Add an `Outputs` section with a key named exactly `StackSetExecutionRoleName` that returns the role name. | 
| `ValidationException` | `A custom execution role name must start with 'stacksets-exec-custom-'` | The `ExecutionRoleName` that you specified doesn't begin with the required prefix. | Prefix the execution role name with `stacksets-exec-custom-`. | 
| `ValidationException` | `An execution role name must be at most 64 characters` | The `ExecutionRoleName` that you specified exceeds the IAM role name length limit. | Shorten the execution role name to 64 characters or fewer. | 
| `ValidationException` | `An execution role name must satisfy regular expression pattern: [a-zA-Z0-9_+=,.@\-]+` | The `ExecutionRoleName` that you specified contains characters that IAM doesn't allow in a role name. | Use only alphanumeric characters and the characters `_+=,.@-`. | 
| `ValidationException` | `StackSetOutputBucket must be an S3 bucket name, not an ARN or a path` | You specified an Amazon S3 ARN or a path that includes `/` instead of a bucket name. | Specify only the bucket name, for example `amzn-s3-demo-bucket`. | 
| `ValidationException` | `StackSetOutputBucket is not a valid S3 bucket name: {{bucket}}` | The value you specified doesn't satisfy the Amazon S3 bucket naming rules. | Use a bucket name of 3 to 63 lowercase alphanumeric characters, dots, and hyphens, starting and ending with an alphanumeric character. | 
| `ValidationException` | `Failed to parse template: {{detail}}` | StackSets couldn't parse the execution role template as JSON or YAML. | Correct the syntax error that the message reports, then retry the operation. | 
| `InvalidOperationException` | `Cannot specify deployment targets when updating the execution role for service-managed stack sets` | An UpdateStackSet call specified both a new execution role template and deployment targets. | Omit the deployment targets. Updating the execution role template always applies to all existing stack instances. | 

## Considerations
<a name="stacksets-custom-execution-role-considerations"></a>
+ Custom execution role templates are supported only with the *service-managed* permissions model.
+ StackSets creates the execution role stack once per target account, when it first deploys stack instances to that account.
+ If StackSets can't create the execution role stack in a target account, the stack instance deployments for that account also fail. Check the stack events in the target account for details. Deployments to other target accounts aren't affected and continue independently. To retry a failed account, create new stack instances that target that account.
+ If StackSets creates the execution role stack successfully but your execution role name doesn't match the role that the stack provisioned, the stack instance deployments for that account fail.
+ Updating the execution role template for a StackSet always updates the execution role in all existing stack instances.
+ The `CAPABILITY_NAMED_IAM` capability is required when you specify an execution role template.