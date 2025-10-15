# Organizing CloudFormation parameters with
 `AWS::CloudFormation::Interface` metadata

`AWS::CloudFormation::Interface` is a metadata key that defines how parameters
 are grouped and sorted in the CloudFormation console. By default, the console lists input parameters
 in alphabetical order by their logical IDs when you create or update stacks in the console. By
 using this key, you can define your own parameter grouping and ordering so that users can
 efficiently specify parameter values. For example, you could group all EC2-related parameters in
 one group and all VPC-related parameters in another group.

In the metadata key, you can specify the groups to create, the parameters to include in each
 group, and the order in which the console shows each parameter within its group. 

You can also define labels for parameters. A label is a friendly name or description that
 the console displays instead of a parameter's logical ID. Labels are useful for helping users
 understand the values to specify for each parameter. For example, you could label a
 `KeyPair` parameter `Select an EC2 key pair`.

All parameters that you reference in the metadata key must be declared in the
 `Parameters` section of the template.

###### Note

Only the CloudFormation console uses the `AWS::CloudFormation::Interface` metadata
 key. AWS CLI and API calls don't use this key.


## Syntax


To declare this entity in your CloudFormation template, use the following syntax:



### JSON



```
"Metadata" : {
  "AWS::CloudFormation::Interface" : {
    "ParameterGroups": [
      {
        "Label": {
          "default": "`Group Label`"
        },
        "Parameters": [
          "`Parameter1`",
          "`Parameter2`"
        ]
      }
    ],
    "ParameterLabels": {
      "`Parameter1`": {
        "default": "`Friendly Name for Parameter1`"
      }
    }
  }
}
```



### YAML



```
Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: `Group Label`
        Parameters:
          - `Parameter1`
          - `Parameter2`
    ParameterLabels:
      `Parameter1`:
        default: `Friendly Name for Parameter1`
```


## Properties




`ParameterGroups`

A list of parameter group types, where you specify group names, the parameters in
 each group, and the order in which the parameters are shown.


*Required*: No




`Label`

A name for the parameter group.


*Required*: No



`default`

The default label that the CloudFormation console uses to name a parameter
 group.


*Required*: No


*Type*: String



`Parameters`

A list of case-sensitive parameter logical IDs to include in the group.
 Parameters must already be defined in the `Parameters` section of the
 template. A parameter can be included in only one parameter group.


The console lists the parameters that you don't associate with a parameter
 group in alphabetical order in the `Other parameters` group.


*Required*: No


*Type*: List of String values





`ParameterLabels`

A mapping of parameters and their friendly names that the CloudFormation console shows
 when a stack is created or updated.


*Required*: No




Parameter label

A label for a parameter. The label defines a friendly name or description that
 the CloudFormation console shows on the **Specify Parameters** page
 when a stack is created or updated. The parameter label must be the case-sensitive
 logical ID of a valid parameter that has been declared in the
 `Parameters` section of the template.


*Required*: No



`default`

The default label that the CloudFormation console uses to name a parameter.


*Required*: No


*Type*: String






## Example


The following example defines two parameter groups: `Network Configuration` and
 `Amazon EC2 Configuration`. The `Network Configuration` group includes
 the `VPCID`, `SubnetId`, and `SecurityGroupID` parameters,
 which are defined in the `Parameters` section of the template (not shown). The
 order in which the console shows these parameters is defined by the order in which the
 parameters are listed, starting with the `VPCID` parameter. The example similarly
 groups and orders the `Amazon EC2 Configuration` parameters.


The example also defines a label for the `VPCID` parameter. The console will
 show **Which VPC should this be deployed to?** instead of the parameter's
 logical ID (`VPCID`).



### JSON



```
"Metadata" : {
  "AWS::CloudFormation::Interface" : {
    "ParameterGroups" : [
      {
        "Label" : { "default" : "Network Configuration" },
        "Parameters" : [ "VPCID", "SubnetId", "SecurityGroupID" ]
      },
      {
        "Label" : { "default":"Amazon EC2 Configuration" },
        "Parameters" : [ "InstanceType", "KeyName" ]
      }
    ],
    "ParameterLabels" : {
      "VPCID" : { "default" : "Which VPC should this be deployed to?" }
    }
  }
}
```



### YAML



```
Metadata: 
  AWS::CloudFormation::Interface: 
    ParameterGroups: 
      - Label: 
          default: "Network Configuration"
        Parameters: 
          - VPCID
          - SubnetId
          - SecurityGroupID
      - Label: 
          default: "Amazon EC2 Configuration"
        Parameters: 
          - InstanceType
          - KeyName
    ParameterLabels: 
      VPCID: 
        default: "Which VPC should this be deployed to?"
```


### Parameter groups in the console


Using the metadata key from this example, the following figure shows how the console
 displays parameter groups when a stack is created or updated: **Parameter groups in the console**




![Console showing parameter groups for this example.](../../../images/AWSCloudFormation/latest/UserGuide/images/console-create-stack-parameter-groups.png)
