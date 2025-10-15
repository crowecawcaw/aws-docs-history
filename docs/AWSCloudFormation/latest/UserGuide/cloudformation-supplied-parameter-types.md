# Specify existing resources at
 runtime with CloudFormation-supplied parameter types

When creating your template, you can create parameters that require users to input
 identifiers of existing AWS resources or Systems Manager parameters by using specialized parameter
 types provided by CloudFormation. 

###### Topics

* [Overview](#cloudformation-supplied-parameter-types-overview "#cloudformation-supplied-parameter-types-overview")
* [Example](#cloudformation-supplied-parameter-types-example "#cloudformation-supplied-parameter-types-example")
* [Considerations](#cloudformation-supplied-parameter-types-considerations "#cloudformation-supplied-parameter-types-considerations")
* [Supported AWS-specific
 parameter types](#aws-specific-parameter-types-supported "#aws-specific-parameter-types-supported")
* [Supported Systems Manager parameter
 types](#systems-manager-parameter-types-supported "#systems-manager-parameter-types-supported")
* [Unsupported Systems Manager
 parameter types](#systems-manager-parameter-types-unsupported "#systems-manager-parameter-types-unsupported")

## Overview


In CloudFormation, you can use parameters to customize your stacks by providing input
 values during stack creation or update. This feature makes your templates reusable and
 flexible across different scenarios. 


Parameters are defined in the `Parameters` section of a CloudFormation
 template. Each parameter has a name and a type, and can have additional settings such as
 a default value and allowed values. For more information, see [CloudFormation template Parameters
 syntax](parameters-section-structure.md "parameters-section-structure.md"). 


The parameter type determines the kind of input value the parameter can accept. For
 example, `Number` only accepts numeric values, while `String`
 accepts text input. 


CloudFormation provides several additional parameter types that you can use in your
 templates to reference existing AWS resources and Systems Manager parameters. 


These parameter types fall into two categories:



* AWS-specific parameter types –
 CloudFormation provides a set of parameter types that help catch invalid values when
 creating or updating a stack. When you use these parameter types, anyone who
 uses your template must specify valid values from the AWS account and Region
 they're creating the stack in.


If they use the AWS Management Console, CloudFormation provides a prepopulated list of existing
 values from their account and Region. This way, the user doesn't have to
 remember and correctly type a specific name or ID. Instead, they just select
 values from a drop-down list. In some cases, they can even search for values by
 ID, name, or `Name` tag value.
* Systems Manager parameter types – CloudFormation also
 provides parameter types that correspond to existing parameters in Systems Manager
 Parameter Store. When you use these parameter types, anyone who uses your
 template must specify a Parameter Store key as the value of the Systems Manager parameter
 type, and CloudFormation then retrieves the latest value from Parameter Store to use
 in their stack. This can be useful when you need to frequently update
 applications with new property values, such as new Amazon Machine Image (AMI)
 IDs. For information about the Parameter Store, see [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html").

Once your parameters are defined in the `Parameters` section, you can
 reference parameter values throughout your CloudFormation template using the
 `Ref` function.


## Example


The following example shows a template that uses the following parameter types. 



* `AWS::EC2::VPC::Id`
* `AWS::EC2::Subnet::Id`
* `AWS::EC2::KeyPair::KeyName`
* `AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>`

To create a stack from this template, you must specify an existing VPC ID, subnet ID,
 and key pair name from your account. You can also specify an existing Parameter Store
 key that references the desired AMI ID or keep the default value of
 ``/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2``.
 This public parameter is an alias for the regional AMI ID for the latest Amazon Linux 2
 AMI. For more information about public parameters, see [Discovering public parameters in Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-finding-public-parameters.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-finding-public-parameters.html") in the
 *AWS Systems Manager User Guide*.



### JSON



```
{
    "Parameters": {
        "VpcId": {
            "Description": ID of an existing Virtual Private Cloud (VPC).,
            "Type": AWS::EC2::VPC::Id
        },
        "PublicSubnetId": {
            "Description": ID of an existing public subnet within the specified VPC.,
            "Type": AWS::EC2::Subnet::Id
        },
        "KeyName": {
            "Description": Name of an existing EC2 key pair to enable SSH access to the instance.,
            "Type": AWS::EC2::KeyPair::KeyName
        },
        "AMIId": {
            "Description": Name of a Parameter Store parameter that stores the ID of the Amazon Machine Image (AMI).,
            "Type": AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>,
            "Default": /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
        }
    },
    "Resources": {
        "InstanceSecurityGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Enable SSH access via port 22",
                "VpcId": { "Ref": "VpcId" },
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 22,
                        "ToPort": 22,
                        "CidrIp": "0.0.0.0/0"
                    }
                ]
            }
        },
        "Ec2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "KeyName": { "Ref": "KeyName" },
                "ImageId": { "Ref": "AMIId" },
                "NetworkInterfaces": [
                    {
                        "AssociatePublicIpAddress": "true",
                        "DeviceIndex": "0",
                        "SubnetId": { "Ref": "PublicSubnetId" },
                        "GroupSet": [{ "Ref": "InstanceSecurityGroup" }]
                    }
                ]
            }
        }
    },
    "Outputs": {
        "InstanceId": {
            "Value": { "Ref": "Ec2Instance" }
        }
    }
}
```



### YAML



```
Parameters:
  VpcId:
    Description: ID of an existing Virtual Private Cloud (VPC).
    Type: AWS::EC2::VPC::Id
  PublicSubnetId:
    Description: ID of an existing public subnet within the specified VPC.
    Type: AWS::EC2::Subnet::Id
  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instance.
    Type: AWS::EC2::KeyPair::KeyName
  AMIId:
    Description: Name of a Parameter Store parameter that stores the ID of the Amazon Machine Image (AMI).
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
Resources:
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access via port 22
      VpcId: !Ref VpcId
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
  Ec2Instance:
    Type: AWS::EC2::Instance
    Properties:
      KeyName: !Ref KeyName
      ImageId: !Ref AMIId
      NetworkInterfaces:
        - AssociatePublicIpAddress: "true"
          DeviceIndex: "0"
          SubnetId: !Ref PublicSubnetId
          GroupSet:
            - !Ref InstanceSecurityGroup
Outputs:
  InstanceId:
    Value: !Ref Ec2Instance
```


### AWS CLI command
 to create the stack


The following [create-stack](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html") command creates a stack based on the
 example template. 



```
aws cloudformation create-stack --stack-name `MyStack` \
  --template-body `file://sampletemplate.json` \
  --parameters \
ParameterKey="VpcId",ParameterValue="`vpc-a123baa3`" \
ParameterKey="PublicSubnetId",ParameterValue="`subnet-123a351e`" \
ParameterKey="KeyName",ParameterValue="`MyKeyName`" \
ParameterKey="AMIId",ParameterValue="`MyParameterKey`"
```

To use a parameter type that accepts a list of strings , such as
 `List<AWS::EC2::Subnet::Id>`, you must escape the commas inside
 the `ParameterValue` with a double backslash, as shown in the following
 example.



```
--parameters ParameterKey="SubnetIDs",ParameterValue="`subnet-5ea0c127\\,subnet-6194ea3b\\,subnet-c87f2be0`"
```

## Considerations


It's strongly recommended that you use dynamic references to restrict access to
 sensitive configuration definitions, such as third-party credentials. For more
 information, see [Get values stored in other services using dynamic
 references](dynamic-references.md "dynamic-references.md").


If you want to allow template users to specify values from different AWS accounts,
 don't use AWS-specific parameter types. Instead, define parameters of type
 `String` or `CommaDelimitedList`. 


There are a few things to keep in mind with Systems Manager parameter types:



* You can see the resolved parameter values on the stack's
 **Parameters** tab in the console, or by running [describe-stacks](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stacks.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stacks.html") or [describe-change-set](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-change-set.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-change-set.html"). Remember, these values are
 set when the stack is created or updated, so they might be different from the
 latest values in Parameter Store.
* For stack updates, when you use the **Use existing value**
 option (or set `UsePreviousValue` to true), this means that you want
 to keep using the same Parameter Store key, not its value. CloudFormation always
 retrieves the latest value.
* If you specify any allowed values or other constraints, CloudFormation validates
 them against the parameter keys you specify, but not their values. You should
 validate the values in Parameter Store itself.
* When you create or update stacks and create change sets, CloudFormation uses
 whatever value exists in Parameter Store at the time. If a specified parameter
 doesn't exist in Parameter Store under the caller's AWS account, CloudFormation
 returns a validation error.
* When you execute a change set, CloudFormation uses the values that are specified
 in the change set. You should review these values before executing the change
 set because they might change in Parameter Store between the time that you
 create the change set and run it.
* For Parameter Store parameters stored in the same AWS account, you must
 provide the parameter name. For Parameter Store parameters shared by another
 AWS account, you must provide the full parameter ARN.

## Supported AWS-specific
 parameter types


CloudFormation supports the following AWS-specific types:




`AWS::EC2::AvailabilityZone::Name`

An Availability Zone, such as `us-west-2a`.



`AWS::EC2::Image::Id`

An Amazon EC2 image ID, such as `ami-0ff8a91507f77f867`. Note that
 the CloudFormation console doesn't show a drop-down list of values for this
 parameter type.



`AWS::EC2::Instance::Id`

An Amazon EC2 instance ID, such as `i-1e731a32`.



`AWS::EC2::KeyPair::KeyName`

An Amazon EC2 key pair name.



`AWS::EC2::SecurityGroup::GroupName`

A default VPC security group name, such as `my-sg-abc`.



`AWS::EC2::SecurityGroup::Id`

A security group ID, such as `sg-a123fd85`.



`AWS::EC2::Subnet::Id`

A subnet ID, such as `subnet-123a351e`.



`AWS::EC2::Volume::Id`

An Amazon EBS volume ID, such as `vol-3cdd3f56`.



`AWS::EC2::VPC::Id`

A VPC ID, such as `vpc-a123baa3`.



`AWS::Route53::HostedZone::Id`

An Amazon Route 53 hosted zone ID, such as `Z23YXV4OVPL04A`.



`List<AWS::EC2::AvailabilityZone::Name>`

An array of Availability Zones for a region, such as `us-west-2a,
 us-west-2b`.



`List<AWS::EC2::Image::Id>`

An array of Amazon EC2 image IDs, such as `ami-0ff8a91507f77f867,
 ami-0a584ac55a7631c0c`. Note that the CloudFormation console doesn't
 show a drop-down list of values for this parameter type.



`List<AWS::EC2::Instance::Id>`

An array of Amazon EC2 instance IDs, such as `i-1e731a32,
 i-1e731a34`.



`List<AWS::EC2::SecurityGroup::GroupName>`

An array of default VPC security group names, such as `my-sg-abc,
 my-sg-def`.



`List<AWS::EC2::SecurityGroup::Id>`

An array of security group IDs, such as `sg-a123fd85,
 sg-b456fd85`.



`List<AWS::EC2::Subnet::Id>`

An array of subnet IDs, such as `subnet-123a351e,
 subnet-456b351e`.



`List<AWS::EC2::Volume::Id>`

An array of Amazon EBS volume IDs, such as `vol-3cdd3f56,
 vol-4cdd3f56`.



`List<AWS::EC2::VPC::Id>`

An array of VPC IDs, such as `vpc-a123baa3,
 vpc-b456baa3`.



`List<AWS::Route53::HostedZone::Id>`

An array of Amazon Route 53 hosted zone IDs, such as `Z23YXV4OVPL04A,
 Z23YXV4OVPL04B`.




## Supported Systems Manager parameter
 types


CloudFormation supports the following Systems Manager parameter types:




`AWS::SSM::Parameter::Name`

The name of a Systems Manager parameter key. Use this parameter type only to check
 that a required parameter exists. CloudFormation won't retrieve the actual value
 associated with the parameter. 



`AWS::SSM::Parameter::Value<String>`

A Systems Manager parameter whose value is a string. This corresponds to the
 `String` parameter type in Parameter Store.



`AWS::SSM::Parameter::Value<List<String>>` or
 `AWS::SSM::Parameter::Value<CommaDelimitedList>`

A Systems Manager parameter whose value is a list of strings. This corresponds to
 the `StringList` parameter type in Parameter Store.



`AWS::SSM::Parameter::Value<`AWS-specific parameter
 type`>`

A Systems Manager parameter whose value is an AWS-specific parameter type. 


For example, the following specifies the
 `AWS::EC2::KeyPair::KeyName` type:



* `AWS::SSM::Parameter::Value<AWS::EC2::KeyPair::KeyName>`


`AWS::SSM::Parameter::Value<List<`AWS-specific
 parameter type`>>`

A Systems Manager parameter whose value is a list of AWS-specific parameter types. 


For example, the following specifies a list of
 `AWS::EC2::KeyPair::KeyName` types:



* `AWS::SSM::Parameter::Value<List<AWS::EC2::KeyPair::KeyName>>`



## Unsupported Systems Manager
 parameter types


CloudFormation doesn't support the following Systems Manager parameter type:



* Lists of Systems Manager parameter types—for example:
 `List<AWS::SSM::Parameter::Value<String>>`

In addition, CloudFormation doesn't support defining template parameters as
 `SecureString` Systems Manager parameter types. However, you can specify secure
 strings as parameter *values* for certain resources. For more
 information, see [Get values stored in other services using dynamic
 references](dynamic-references.md "dynamic-references.md").
