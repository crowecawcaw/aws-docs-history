# Creating stacks using Direct Change mode

There are two requirements when launching stacks in CloudFormation using the
`AWSManagedServicesCloudFormationAdminRole`, in order for the stack to be managed by AMS:

- The template must contain an `AmsStackTransform`.
- The stack name must start with the prefix `stack-` followed by a 17 character alphanumeric string.

###### Note

To successfully use the `AmsStackTransform`, you must acknowledge that your stack template contains the `CAPABILITY_AUTO_EXPAND`
capability in order for CloudFormation (CFN) to create or update the stack. You do this by passing the `CAPABILITY_AUTO_EXPAND` as part of your
create-stack request. CFN rejects the request if this capability is not acknowledged when the `AmsStackTransform`
is included in the template. The CFN console ensures that you pass this capability if you have the transform in your template, but this can be missed
when you are interacting with CFN via their APIs.

You must pass this capability whenever you use the following CFN API calls:

- [CreateChangeSet](../../../AWSCloudFormation/latest/APIReference/API_CreateChangeSet.md "../../../AWSCloudFormation/latest/APIReference/API_CreateChangeSet.md")
- [CreateStack](../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md#API_CreateStack_RequestParameters "../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md#API_CreateStack_RequestParameters")
- [UpdateStack](../../../AWSCloudFormation/latest/APIReference/API_UpdateStack.md "../../../AWSCloudFormation/latest/APIReference/API_UpdateStack.md")
  When creating or updating a stack with DCM, the same validations and augmentations of CFN Ingest and Stack Update CTs are performed on the stack,
  for more information see
  [CloudFormation Ingest Guidelines, Best Practices, and Limitations](../appguide/cfn-author-templates.md "../appguide/cfn-author-templates.md").
  The exception to this is that the AMS default security groups (SGs) will not be attached to any stand-alone EC2 instances or EC2 instances in Auto Scaling groups (ASGs).
  When you create your CloudFormation template, with stand-alone EC2 instances or ASGs, you can attach the default SGs.

###### Note

IAM roles can now be created and managed with the `AWSManagedServicesCloudFormationAdminRole`.

The AMS default SGs have ingress and egress rules that allow the instances
to launch successfully and to be accessed later through SSH or RDP by AMS operations and you. If the you find that the AMS default security groups are too
permissive, you can create your own SGs with more restrictive rules and attach them to your instance, as long as it still allows you and AMS operations to access
the instance during incidents.

The AMS default security groups are the following:

- SentinelDefaultSecurityGroupPrivateOnly: Can be accessed in the CFN template through this SSM parameter
  `/ams/${VpcId}/SentinelDefaultSecurityGroupPrivateOnly`
- SentinelDefaultSecurityGroupPrivateOnlyEgressAll: Can be accessed in the CFN template through this SSM parameter
  `/ams/${VpcId}/SentinelDefaultSecurityGroupPrivateOnlyEgressAll`

## AMS Transform

Add a `Transform` statement to your CloudFormation template.
This adds a CloudFormation macro that validates and registers the stack with AMS at launch time.

**JSON** Example

```
"Transform": {
    "Name": "AmsStackTransform",
    "Parameters": {
      "StackId": {"Ref" : "AWS::`StackId`"}
    }
  }
```

**YAML** Example

```
Transform:
  Name: AmsStackTransform
  Parameters:
    StackId: !Ref 'AWS::`StackId`'
```

Also add the `Transform` statement when updating the template of an existing stack.

**JSON** Example

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description" : "`Create an SNS Topic`",
    "Transform": {
      "Name": "AmsStackTransform",
      "Parameters": {
        "StackId": {"Ref" : "AWS::`StackId`"}
     }
  },
  "Parameters": {
    "TopicName": {
      "Type": "String",
      "Default": "`HelloWorldTopic`"
    }
  },
  "Resources": {
    "SnsTopic": {
      "Type": "AWS::SNS::Topic",
      "Properties": {
        "TopicName": {"Ref": "`TopicName`"}
      }
    }
  }
}
```

**YAML** Example

```
AWSTemplateFormatVersion: '2010-09-09'
Description: `Create an SNS Topic`
Transform:
  Name: AmsStackTransform
  Parameters:
    StackId: !Ref 'AWS::`StackId`'
Parameters:
  TopicName:
    Type: String
    Default: `HelloWorldTopic`
Resources:
  SnsTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: !Ref `TopicName`
```

## Stack name

The stack name must start with the prefix `stack-` followed by a 17 character alphanumeric
string. This is to maintain compatibility with other AMS systems that operate on AMS stack IDs. 

The following are examples of ways to generate compatible stack IDs:

Bash:

```
echo "stack-$(env LC_CTYPE=C tr -dc 'a-z0-9' < /dev/urandom | head -c 17)"
```

Python:

```
import string
import random

'stack-' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=17))
```

Powershell:

```
"stack-" + ( -join ((0x30..0x39) + ( 0x61..0x7A) | Get-Random -Count 17  | % {[char]$_}) )
```
