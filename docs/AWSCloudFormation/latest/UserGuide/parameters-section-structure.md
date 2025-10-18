# CloudFormation template Parameters
 syntax

Use the optional `Parameters` section to customize your templates. With
 parameters, you can input custom values to your template each time you create or update a stack.
 By using parameters in your templates, you can build reusable and flexible templates that can be
 tailored to specific scenarios. 

By defining parameters of the appropriate type, you can choose from a list of identifiers of
 existing resources when you use the console to create your stack. For more information, see
 [Specify existing resources at
 runtime with CloudFormation-supplied parameter types](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md").

Parameters are a popular way to specify property values of stack resources. However, there
 may be settings that are region dependent or are somewhat complex for users to figure out
 because of other conditions or dependencies. In these cases, you might want to put some logic in
 the template itself so that users can specify simpler values (or none at all) to get the results
 that they want, such as by using a mapping. For more information, see [CloudFormation template Mappings
 syntax](mappings-section-structure.md "mappings-section-structure.md").


## Syntax


You declare parameters in a template's `Parameters` section, which uses the
 following general syntax:



### JSON



```
"Parameters" : {
  "`ParameterLogicalID`" : {
    "`Description`": "`Information about the parameter`",
    "Type" : "`DataType`",
    "`Default`" : "`value`",
    "`AllowedValues`" : ["`value1`", "`value2`"]
  }
}
```



### YAML



```
Parameters:
  `ParameterLogicalID`:
    `Description`: `Information about the parameter`
    Type: `DataType`
    `Default`: `value`
    `AllowedValues`:
      - `value1`
      - `value2`
```


A parameter contains a list of attributes that define its value and constraints against
 its value. The only required attribute is `Type`, which can be `String`,
 `Number`, or a CloudFormation-supplied parameter type. You can also add a
 `Description` attribute that describes what kind of value you should specify. The
 parameter's name and description appear in the **Specify Parameters** page
 when you use the template in the **Create Stack** wizard.


###### Note

By default, the CloudFormation console lists input parameters alphabetically by their
 logical ID. To override this default ordering and group related parameters together, you can
 use the `AWS::CloudFormation::Interface` metadata key in your template. For more
 information, see [Organizing CloudFormation parameters with
 AWS::CloudFormation::Interface metadata](aws-cloudformation-interface.md "aws-cloudformation-interface.md").


For parameters with default values, CloudFormation uses the default values unless users
 specify another value. If you omit the default attribute, users are required to specify a
 value for that parameter. However, requiring the user to input a value does not ensure that
 the value is valid. To validate the value of a parameter, you can declare constraints or
 specify an AWS-specific parameter type.


For parameters without default values, users must specify a key name value at stack
 creation. If they don’t, CloudFormation fails to create the stack and throws an exception:



```
Parameters: [KeyName] must have values
```

## Properties




`AllowedPattern`

A regular expression that represents the patterns to allow for `String`
 or `CommaDelimitedList` types. When applied on a parameter of type
 `String`, the pattern must match the entire parameter value provided. When
 applied to a parameter of type `CommaDelimitedList`, the pattern must match
 each value in the list.


*Required*: No



`AllowedValues`

An array containing the list of values allowed for the parameter. When applied to a
 parameter of type `String`, the parameter value must be one of the allowed
 values. When applied to a parameter of type `CommaDelimitedList`, each value
 in the list must be one of the specified allowed values.


*Required*: No


###### Note

If you're using YAML and you want to use `Yes` and `No`
 strings for `AllowedValues`, use single-quotes to prevent the YAML parser
 from considering these boolean values.



`ConstraintDescription`

A string that explains a constraint when the constraint is violated. For example,
 without a constraint description, a parameter that has an allowed pattern of
 `[A-Za-z0-9]+` displays the following error message when the user specifies
 an invalid value:


`Malformed input-Parameter MyParameter must match pattern
 [A-Za-z0-9]+`


By adding a constraint description, such as *must only contain letters
 (uppercase and lowercase) and numbers*, you can display the following
 customized error message:


`Malformed input-Parameter MyParameter must only contain uppercase and
 lowercase letters and numbers`


*Required*: No



`Default`

A value of the appropriate type for the template to use if no value is specified
 when a stack is created. If you define constraints for the parameter, you must specify a
 value that adheres to those constraints.


*Required*: No



`Description`

A string of up to 4000 characters that describes the parameter.


*Required*: No



`MaxLength`

An integer value that determines the largest number of characters you want to allow
 for `String` types.


*Required*: No



`MaxValue`

A numeric value that determines the largest numeric value you want to allow for
 `Number` types.


*Required*: No



`MinLength`

An integer value that determines the smallest number of characters you want to allow
 for `String` types.


*Required*: No



`MinValue`

A numeric value that determines the smallest numeric value you want to allow for
 `Number` types.


*Required*: No



`NoEcho`

Whether to mask the parameter value to prevent it from being displayed in the
 console, command line tools, or API. If you set the `NoEcho` attribute to
 `true`, CloudFormation returns the parameter value masked as asterisks (\*\*\*\*\*)
 for any calls that describe the stack or stack events, except for information stored in
 the locations specified below.


*Required*: No


###### Important

Using the `NoEcho` attribute does not mask any information stored in the following:


* The `Metadata` template section. CloudFormation does not transform, modify, or redact any
 information you include in the `Metadata` section. For more information, see 
 [Metadata](metadata-section-structure.md "metadata-section-structure.md").
* The `Outputs` template section. For more information, see
 [Outputs](outputs-section-structure.md "outputs-section-structure.md").
* The `Metadata` attribute of a resource definition. For more information, see
 [`Metadata` attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-metadata.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-metadata.html").
We strongly recommend you do not use these mechanisms to include sensitive information, such as
 passwords or secrets.


###### Important

Rather than embedding sensitive information directly in your CloudFormation templates, we recommend you use dynamic parameters in the stack template to
reference sensitive information that is stored and managed outside of CloudFormation, such as in the AWS Systems Manager Parameter Store or AWS Secrets Manager.

For more information, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best practice.


###### Important

We strongly recommend against including `NoEcho` parameters, or any
 sensitive data, in resource properties that are part of a resource's primary
 identifier.

When a `NoEcho` parameter is included in a property that forms a
 primary resource identifier, CloudFormation may use the *actual plaintext
 value* in the primary resource identifier. This resource ID may appear in
 any derived outputs or destinations.

To determine which resource properties comprise a resource type's primary
 identifier, refer to the resource reference documentation for that resource in the
 [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html"). In the **Return values** section, the
 `Ref` function return value represents the resource properties that
 comprise the resource type's primary identifier.



`Type`

The data type for the parameter (`DataType`).


*Required*: Yes


CloudFormation supports the following parameter types:




`String`

A literal string. You can use the following attributes to declare constraints:
 `MinLength`, `MaxLength`, `Default`,
 `AllowedValues`, and `AllowedPattern`. 


For example, users could specify `"MyUserName"`.



`Number`

An integer or float. CloudFormation validates the parameter value as a number;
 however, when you use the parameter elsewhere in your template (for example, by
 using the `Ref` intrinsic function), the parameter value becomes a
 string.


You can use the following attributes to declare constraints:
 `MinValue`, `MaxValue`, `Default`, and
 `AllowedValues`.


For example, users could specify `"8888"`.



`List<Number>`

An array of integers or floats that are separated by commas. CloudFormation
 validates the parameter value as numbers; however, when you use the parameter
 elsewhere in your template (for example, by using the `Ref` intrinsic
 function), the parameter value becomes a list of strings.


For example, users could specify `"80,20"`, and a `Ref`
 would result in `["80","20"]`.



`CommaDelimitedList`

An array of literal strings that are separated by commas. The total number of
 strings should be one more than the total number of commas. Also, each member
 string is space trimmed.


For example, users could specify `"test,dev,prod"`, and a
 `Ref` would result in `["test","dev","prod"]`.



AWS-specific parameter types

AWS values such as Amazon EC2 key pair names and VPC IDs. For more information,
 see [Specify existing
 resources at runtime](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md").



Systems Manager parameter types

Parameters that correspond to existing parameters in Systems Manager Parameter Store.
 You specify a Systems Manager parameter key as the value of the Systems Manager parameter type, and
 CloudFormation retrieves the latest value from Parameter Store to use for the stack.
 For more information, see [Specify existing
 resources at runtime](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md").






## General requirements for
 parameters


The following requirements apply when using parameters:



* You can have a maximum of 200 parameters in a CloudFormation template.
* Each parameter must be given a logical name (also called logical ID) that must be
 alphanumeric and unique among all logical names within the template.
* Each parameter must be assigned a parameter type that's supported by CloudFormation. For
 more information, see [Type](#parameters-section-structure-properties-type "#parameters-section-structure-properties-type").
* Each parameter must be assigned a value at runtime for CloudFormation to successfully
 provision the stack. You can optionally specify a default value for CloudFormation to use
 unless another value is provided.
* Parameters must be declared and referenced from within the same template. You can
 reference parameters from the `Resources` and `Outputs` sections of
 the template.

## Examples


###### Topics

* [Simple string parameter](#parameters-section-structure-example-1 "#parameters-section-structure-example-1")
* [Password parameter](#parameters-section-structure-example-2 "#parameters-section-structure-example-2")
* [Referencing parameters](#parameters-section-structure-example-3 "#parameters-section-structure-example-3")
* [Comma-delimited list
 parameter](#parameters-section-structure-example-4 "#parameters-section-structure-example-4")
* [Return a value from a
 comma-delimited list parameter](#parameters-section-structure-example-5 "#parameters-section-structure-example-5")

### Simple string parameter


The following example declares a parameter named `InstanceTypeParameter` of
 type `String`. This parameter lets you specify the Amazon EC2 instance type for the
 stack. If no value is provided during stack creation or update, CloudFormation uses the default
 value of `t2.micro`.



#### JSON



```
"Parameters" : {
  "InstanceTypeParameter" : {
    "Description" : "Enter t2.micro, m1.small, or m1.large. Default is t2.micro.",
    "Type" : "String",
    "Default" : "t2.micro",
    "AllowedValues" : ["t2.micro", "m1.small", "m1.large"]
  }
}
```



#### YAML



```
Parameters:
  InstanceTypeParameter:
    Description: Enter t2.micro, m1.small, or m1.large. Default is t2.micro.
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - m1.small
      - m1.large
```


### Password parameter


The following example declares a parameter named `DBPwd` of type
 `String` with no default value. The `NoEcho` property is set to
 `true` to prevent the parameter value from being displayed in stack
 descriptions. The minimum length that can be specified is `1`, and the maximum
 length that can be specified is `41`. The pattern allows lowercase and uppercase
 alphabetical characters and numerals. This example also illustrates the use of a regular
 expression for the `AllowedPattern` property.



#### JSON



```
"Parameters" : {
  "DBPwd" : {
    "NoEcho" : "true",
    "Description" : "The database admin account password",
    "Type" : "String",
    "MinLength" : "1",
    "MaxLength" : "41",
    "AllowedPattern" : "^[a-zA-Z0-9]*$"
  }
}
```



#### YAML



```
Parameters: 
  DBPwd: 
    NoEcho: true
    Description: The database admin account password
    Type: String
    MinLength: 1
    MaxLength: 41
    AllowedPattern: ^[a-zA-Z0-9]*$
```


### Referencing parameters


You use the `Ref` intrinsic function to reference a parameter, and CloudFormation
 uses the parameter's value to provision the stack. You can reference parameters from the
 `Resources` and `Outputs` sections of the same template.


In the following example, the `InstanceType` property of the EC2 instance
 resource references the `InstanceTypeParameter` parameter value:



#### JSON



```
"Ec2Instance" : {
  "Type" : "AWS::EC2::Instance",
  "Properties" : {**"InstanceType" : { "Ref" : "InstanceTypeParameter" },**
    "ImageId" : "ami-0ff8a91507f77f867"
  }
}
```



#### YAML



```
Ec2Instance:
  Type: AWS::EC2::Instance
  Properties:**InstanceType:
 Ref: InstanceTypeParameter**
    ImageId: ami-0ff8a91507f77f867
```


### Comma-delimited list
 parameter


The `CommaDelimitedList` parameter type can be useful when you need to
 provide multiple values for a single property. The following example declares a parameter
 named `DbSubnetIpBlocks` with a default value of three CIDR blocks separated by
 commas.



#### JSON



```
"Parameters" : {
  "DbSubnetIpBlocks": {
    "Description": "Comma-delimited list of three CIDR blocks",
    "Type": "CommaDelimitedList",
    "Default": "10.0.48.0/24, 10.0.112.0/24, 10.0.176.0/24"
  }
}
```



#### YAML



```
Parameters: 
  DbSubnetIpBlocks: 
    Description: "Comma-delimited list of three CIDR blocks"
    Type: CommaDelimitedList
    Default: "10.0.48.0/24, 10.0.112.0/24, 10.0.176.0/24"

```


### Return a value from a
 comma-delimited list parameter


To refer to a specific value in a parameter's comma-delimited list, use the
 `Fn::Select` intrinsic function in the `Resources` section of your
 template. Pass the index value of the object that you want and a list of objects, as shown
 in the following example.



#### JSON



```
{
    "Parameters": {
        "VPC": {
            "Type": "String",
            "Default": "vpc-123456"
        },
        "VpcAzs": {
            "Type": "CommaDelimitedList",
            "Default": "us-west-2a, us-west-2b, us-west-2c"
        },
        "DbSubnetIpBlocks": {
            "Type": "CommaDelimitedList",
            "Default": "172.16.0.0/26, 172.16.0.64/26, 172.16.0.128/26"
        }
    },
    "Resources": {
        "DbSubnet1": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {**"AvailabilityZone": {
 "Fn::Select": [
 0,
 { 
 "Ref": "VpcAzs" 
 }
 ]
 },**
                "VpcId": {
                    "Ref": "VPC"
                },**"CidrBlock": {
 "Fn::Select": [
 0,
 { "Ref": "DbSubnetIpBlocks" }
 ]
 }**
            }
        },
        "DbSubnet2": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {**"AvailabilityZone": {
 "Fn::Sub": [
 "${AWS::Region}${AZ}",
 {
 "AZ": {
 "Fn::Select": [
 1,
 { "Ref": "VpcAzs" }
 ]
 }
 }
 ]
 },**
                "VpcId": {
                    "Ref": "VPC"
                },**"CidrBlock": {
 "Fn::Select": [
 1,
 { "Ref": "DbSubnetIpBlocks" }
 ]
 }**
            }
        },
        "DbSubnet3": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {**"AvailabilityZone": {
 "Fn::Sub": [
 "${AWS::Region}${AZ}",
 {
 "AZ": {
 "Fn::Select": [
 2,
 { "Ref": "VpcAzs" }
 ]
 }
 }
 ]
 },**
                "VpcId": {
                    "Ref": "VPC"
                },
 **"CidrBlock": {
 "Fn::Select": [
 2,
 { "Ref": "DbSubnetIpBlocks" }
 ]
 }**
            }
        }
    }
}
```



#### YAML



```
Parameters:
  VPC:
    Type: String
    Default: vpc-123456
  VpcAzs:
    Type: CommaDelimitedList
    Default: us-west-2a, us-west-2b, us-west-2c
  DbSubnetIpBlocks:
    Type: CommaDelimitedList
    Default: 172.16.0.0/26, 172.16.0.64/26, 172.16.0.128/26
Resources:
  DbSubnet1:
    Type: AWS::EC2::Subnet
    Properties:**AvailabilityZone: !Select
 - 0 
 - !Ref VpcAzs**
      VpcId: !Ref VPC**CidrBlock: !Select
 - 0
 - !Ref DbSubnetIpBlocks**
  DbSubnet2:
    Type: AWS::EC2::Subnet
    Properties:**AvailabilityZone: !Sub
 - ${AWS::Region}${AZ}
 - AZ: !Select
 - 1
 - !Ref VpcAzs**
      VpcId: !Ref VPC
 **CidrBlock: !Select
 - 1
 - !Ref DbSubnetIpBlocks**
  DbSubnet3:
    Type: AWS::EC2::Subnet
    Properties:**AvailabilityZone: !Sub
 - ${AWS::Region}${AZ}
 - AZ: !Select
 - 2
 - !Ref VpcAzs**
      VpcId: !Ref VPC**CidrBlock: !Select
 - 2
 - !Ref DbSubnetIpBlocks**
```


## Related resources


CloudFormation also supports the use of dynamic references to specify property values
 dynamically. For example, you might need to reference secure strings stored in Systems Manager Parameter
 Store. For more information, see [Get values stored in other services using dynamic
 references](dynamic-references.md "dynamic-references.md").


You can also use pseudo parameters within a `Ref` or a `Sub`
 function to dynamically populate values. For more information, see [Get AWS values using pseudo parameters](pseudo-parameter-reference.md "pseudo-parameter-reference.md").
