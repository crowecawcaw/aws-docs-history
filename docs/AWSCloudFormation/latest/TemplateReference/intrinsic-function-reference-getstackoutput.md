

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Fn::GetStackOutput`
<a name="intrinsic-function-reference-getstackoutput"></a>

The intrinsic function `Fn::GetStackOutput` returns the value of an output from another stack. Unlike `Fn::ImportValue`, this function does not require the referenced stack to explicitly export the output value. It also supports cross-account and cross-region references.

Use this function when you need to reference stack outputs across AWS accounts or Regions, or when you want to reference outputs without managing explicit exports.

**Note**  
`Fn::GetStackOutput` creates a weak reference. The referenced value is resolved at stack create or update time. If the referenced stack or output is later deleted or modified, the consuming stack is not automatically updated or notified. To ensure consistency, protect referenced stacks and outputs from unintended changes.

**Note**  
`Fn::GetStackOutput` does not support cross-partition references.

## Declaration
<a name="w2aac24c43c11"></a>

### JSON
<a name="intrinsic-function-reference-getstackoutput-syntax.json"></a>

```
{
  "Fn::GetStackOutput": {
    "StackName": "{{stack-name}}",
    "OutputName": "{{output-name}}",
    "Region": "{{region}}",
    "RoleArn": "{{role-arn}}"
  }
}
```

### YAML
<a name="intrinsic-function-reference-getstackoutput-syntax.yaml"></a>

You can use the full function name:

```
Fn::GetStackOutput:
  StackName: {{stack-name}}
  OutputName: {{output-name}}
  Region: {{region}}
  RoleArn: {{role-arn}}
```

Alternatively, you can use the short form:

```
!GetStackOutput
  StackName: {{stack-name}}
  OutputName: {{output-name}}
  Region: {{region}}
  RoleArn: {{role-arn}}
```

**Important**  
You can't use the short form of `!GetStackOutput` when it contains other short form functions such as `!Sub` or `!Ref` as parameter values. In that case, use the full function name:  

```
# Do not use
!GetStackOutput
  StackName: !Ref MyStackNameParam
  OutputName: VpcId

# Use this instead
Fn::GetStackOutput:
  StackName: !Ref MyStackNameParam
  OutputName: VpcId
```

## Parameters
<a name="w2aac24c43c13"></a>

StackName  
The name of the stack that contains the output you want to reference.  
*Required:* Yes

OutputName  
The logical ID of the output to reference. This is the key defined in the Outputs section of the referenced stack's template.  
*Required:* Yes

Region  
The AWS Region where the referenced stack is deployed. Defaults to the Region of the stack being created or updated.  
*Required:* No

RoleArn  
The ARN of an IAM role with `cloudformation:DescribeStacks` permissions on the referenced stack. This role must be assumable by the execution role of the stack being created or updated. Defaults to the execution role of the current stack. Use this parameter when referencing a stack in a different AWS account.  
*Required:* No

## Return value
<a name="w2aac24c43c15"></a>

The value of the specified output from the referenced stack.

## Examples
<a name="w2aac24c43c17"></a>

### Same account, same Region
<a name="intrinsic-function-reference-getstackoutput-example-same-account-region"></a>

The following example references the `VpcId` output from a stack named `ProducerStack` in the same account and Region. Because no `Region` or `RoleArn` is specified, CloudFormation uses the current stack's Region and execution role.

#### JSON
<a name="intrinsic-function-reference-getstackoutput-example-same.json"></a>

```
{
  "Fn::GetStackOutput": {
    "StackName": "ProducerStack",
    "OutputName": "VpcId"
  }
}
```

#### YAML
<a name="intrinsic-function-reference-getstackoutput-example-same.yaml"></a>

```
Fn::GetStackOutput:
  StackName: ProducerStack
  OutputName: VpcId
```

### Same account, different Region
<a name="intrinsic-function-reference-getstackoutput-example-cross-region"></a>

The following example references the `VpcId` output from `ProducerStack` deployed in `us-west-2`, while the consuming stack is in a different Region. The `Region` parameter directs CloudFormation to look up the referenced value in `us-west-2`.

#### JSON
<a name="intrinsic-function-reference-getstackoutput-example-cross-region.json"></a>

```
{
  "Fn::GetStackOutput": {
    "StackName": "ProducerStack",
    "OutputName": "VpcId",
    "Region": "us-west-2"
  }
}
```

#### YAML
<a name="intrinsic-function-reference-getstackoutput-example-cross-region.yaml"></a>

```
Fn::GetStackOutput:
  StackName: ProducerStack
  OutputName: VpcId
  Region: us-west-2
```

### Cross-account
<a name="intrinsic-function-reference-getstackoutput-example-cross-account"></a>

The following example references the `VpcId` output from `ProducerStack` in account `111111111111`. The consuming stack is in account `222222222222`. The `RoleArn` specifies a role in account `111111111111` with `cloudformation:DescribeStacks` permissions, which must be assumable by the consuming stack's execution role.

#### JSON
<a name="intrinsic-function-reference-getstackoutput-example-cross-account.json"></a>

```
{
  "Fn::GetStackOutput": {
    "StackName": "ProducerStack",
    "OutputName": "VpcId",
    "RoleArn": "arn:aws:iam::111111111111:role/GetStackOutputRole"
  }
}
```

#### YAML
<a name="intrinsic-function-reference-getstackoutput-example-cross-account.yaml"></a>

```
Fn::GetStackOutput:
  StackName: ProducerStack
  OutputName: VpcId
  RoleArn: arn:aws:iam::111111111111:role/GetStackOutputRole
```

### Cross-account and cross-Region
<a name="intrinsic-function-reference-getstackoutput-example-cross-account-region"></a>

The following example references an output from a stack in a different account and a different Region. Both the `RoleArn` and `Region` parameters are specified.

#### JSON
<a name="intrinsic-function-reference-getstackoutput-example-cross-account-region.json"></a>

```
{
  "Fn::GetStackOutput": {
    "StackName": "ProducerStack",
    "OutputName": "VpcId",
    "RoleArn": "arn:aws:iam::111111111111:role/GetStackOutputRole",
    "Region": "us-west-2"
  }
}
```

#### YAML
<a name="intrinsic-function-reference-getstackoutput-example-cross-account-region.yaml"></a>

```
Fn::GetStackOutput:
  StackName: ProducerStack
  OutputName: VpcId
  RoleArn: arn:aws:iam::111111111111:role/GetStackOutputRole
  Region: us-west-2
```

## IAM role configuration
<a name="intrinsic-function-reference-getstackoutput-iam"></a>

When using the `RoleArn` parameter for cross-account references, the IAM role must have permission to describe stacks in the account that contains the referenced stack:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudformation:DescribeStacks"
      ],
      "Resource": "*"
    }
  ]
}
```

**Tip**  
For a more restrictive policy, scope the `Resource` to the specific stack ARN you want to reference.

The role must have a trust policy that grants `AssumeRole` permissions to the consuming stack's execution role:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::222222222222:role/CloudFormationExecutionRole"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## Supported functions
<a name="w2aac24c43c21"></a>

The following functions can be used within the parameter values of `Fn::GetStackOutput` (for example, to construct the `StackName` or `RoleArn`). The value of these functions can't depend on a resource.
+ `Fn::Base64`
+ `Fn::FindInMap`
+ `Fn::If`
+ `Fn::Join`
+ `Fn::Select`
+ `Fn::Sub`
+ `Ref`

`Fn::GetStackOutput` itself can be used in the following template positions:
+ Direct resource property value
+ Inside `Fn::Join`
+ Inside `Fn::If`
+ Inside `Fn::Select`

See [Known limitations](#intrinsic-function-reference-getstackoutput-limitations) below for positions that are not yet supported.

For example, you can use `Ref` to pass a parameter value as the stack name:

```
Parameters:
  SourceStackName:
    Type: String

Resources:
  MyResource:
    Type: AWS::EC2::Instance
    Properties:
      SubnetId:
        Fn::GetStackOutput:
          StackName: !Ref SourceStackName
          OutputName: SubnetId
```

## Known limitations
<a name="intrinsic-function-reference-getstackoutput-limitations"></a>

The following usage patterns are not supported in this release. All return an `InternalFailure` error. Support for these patterns will be added in a future update.
+ `Fn::GetStackOutput` inside an `Fn::Sub` variable map value
+ `Fn::GetStackOutput` inside `Fn::Base64`
+ `Fn::GetStackOutput` as a direct `Outputs` section value
+ `Fn::GetStackOutput` inside `Fn::Equals` in the `Conditions` section
+ `Fn::GetStackOutput` inside `Fn::ImportValue`

Use `Fn::GetStackOutput` directly as a resource property value or wrap it inside `Fn::Join`, `Fn::If`, or `Fn::Select`.

## Error handling
<a name="intrinsic-function-reference-getstackoutput-errors"></a>

CloudFormation validates `Fn::GetStackOutput` references during stack create or update operations. The following are common errors you may encounter:
+ *IAM role cannot be assumed* – Stack operation fails with an access denied error. Verify that the role can be assumed by the consuming stack's execution role.
+ *IAM role lacks DescribeStacks permission* – Stack operation fails with an access denied error. Verify the role's permissions policy includes `cloudformation:DescribeStacks`.
+ *Referenced stack does not exist* – Stack operation fails with a validation error indicating the stack was not found. If you included the `Region` parameter, check that this is the correct region for the stack you want to reference.
+ *Output key does not exist on the referenced stack* – Stack operation fails with a validation error indicating the output was not found.
+ *Referenced stack is in a Region that is not enabled for the destination account* – Stack operation fails. Ensure the target Region is enabled in the account that owns the referenced stack.
+ *Referenced Region is invalid* – Stack operation fails with a validation error.

### References between us-east-1 and opt-in Regions
<a name="intrinsic-function-reference-getstackoutput-errors-optin"></a>

You may encounter an error when implementing a reference between the `us-east-1` Region and an opt-in region. To avoid such errors, follow [this guide to update token compatibility for the global STS endpoint](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html).

## Using Fn::GetStackOutput with AWS Cloud Development Kit (AWS CDK)
<a name="intrinsic-function-reference-getstackoutput-cdk"></a>

The AWS Cloud Development Kit (AWS CDK) (CDK) supports `Fn::GetStackOutput` through the `Fn.getStackOutput()` method. When you have cross-region or cross-account references between CDK stacks, the CDK can now use `Fn::GetStackOutput` natively instead of generating custom resources with SSM parameters. This simplifies the synthesized templates and removes the need for the previous `crossRegionReferences` workaround.

For more information, see the [CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/).

## Comparison with Fn::ImportValue
<a name="intrinsic-function-reference-getstackoutput-comparison"></a>


| Capability | `Fn::ImportValue` | `Fn::GetStackOutput` | 
| --- | --- | --- | 
| Same account, same Region | Supported | Supported | 
| Cross-account | Not supported | Supported | 
| Cross-Region | Not supported | Supported | 
| Requires explicit Export | Yes | No | 
| Reference type | Strong (blocks deletion of exporting stack) | Weak (resolved at deploy time) | 
| Referential integrity | Yes | No | 

Use `Fn::ImportValue` when you need strong referential integrity within the same account and Region. Use `Fn::GetStackOutput` when you need cross-account or cross-Region references, or when you want to avoid managing explicit exports.

## Best practices
<a name="intrinsic-function-reference-getstackoutput-best-practices"></a>
+ *Protect referenced stacks and outputs.* Because `Fn::GetStackOutput` creates a weak reference, deleting the referenced stack does not prevent the consuming stack from being created or updated. However, subsequent operations that re-resolve the reference will fail. Use stack policies, deletion protection, or IAM policies to prevent accidental deletion of referenced stacks.
+ *Scope IAM roles narrowly.* When configuring the `RoleArn` for cross-account access, restrict the `DescribeStacks` permission to the specific stack ARN whenever possible.
+ *Be aware of resolution timing.* The referenced value is resolved at stack create or update time. If the source value changes, the consuming stack is not automatically updated. To pick up changes, perform an update on the consuming stack.