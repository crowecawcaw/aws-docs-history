# Working with parameter versions in

Parameter Store

Each time you edit the value of a parameter, Parameter Store, a tool in AWS Systems Manager creates
a new _version_ of the parameter and retains the
previous versions. When you initially create a parameter, Parameter Store assigns version
`1` to that parameter. When you change the value of the parameter,
Parameter Store automatically increments the version number by one. You can view the
details, including the values, of all versions in a parameter's history.

You can also specify the version of a parameter to use in API commands and SSM
documents; for example: `ssm:MyParameter:3`. You can specify a parameter
name and a specific version number in API calls and SSM documents. If you don't
specify a version number, the system automatically uses the latest version. If you
specify the number for a version that doesn't exist, the system returns an error
rather than falling back to the latest or default version of the parameter.

You can use parameter versions to see the number of times a parameter changed over
a period of time. Parameter versions also provide a layer of protection if a
parameter value is accidentally changed.

You can create and maintain up to 100 versions of a parameter. After you have
created 100 versions of a parameter, each time you create a new version, the oldest
version of the parameter is removed from history to make room for the new version.

An exception to this is when there are already 100 parameter versions in history,
and a parameter label is assigned to the oldest version of a parameter. In this
case, that version isn't removed from history, and the request to create a new
parameter version fails. This safeguard is to prevent parameter versions with
mission critical labels assigned to them from being deleted. To continue creating
new parameters, first move the label from the oldest version of the parameter to a
newer one for use in your operations. For information about moving parameter labels,
see [Moving a parameter
label using the console](sysman-paramstore-labels.md#sysman-paramstore-labels-console-move "sysman-paramstore-labels.md#sysman-paramstore-labels-console-move") and [Moving a parameter label
using the AWS CLI](sysman-paramstore-labels.md#sysman-paramstore-labels-cli-move "sysman-paramstore-labels.md#sysman-paramstore-labels-cli-move").

The following procedures show you how to edit a parameter and then verify that you
created a new version. You can use the `get-parameter` and
`get-parameters` commands to view parameter versions. For examples on
using these commands, see [GetParameter](../APIReference/API_GetParameter.md#API_GetParameter_Examples "../APIReference/API_GetParameter.md#API_GetParameter_Examples") and [GetParameters](../APIReference/API_GetParameters.md#API_GetParameters_Examples "../APIReference/API_GetParameters.md#API_GetParameters_Examples") in the _AWS Systems Manager API Reference_

###### Topics

- [Creating a new version of a
  parameter using the console](#sysman-paramstore-version-console "#sysman-paramstore-version-console")
- [Referencing a parameter
  version](#reference-parameter-version "#reference-parameter-version")

## Creating a new version of a

parameter using the console

You can use the Systems Manager console to create a new version of a parameter and view
the version history of a parameter.

###### To create a new version of a parameter

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Parameter Store**.
3. Choose the name of a parameter that you created earlier. For
   information about creating a new parameter, see [Creating Parameter Store parameters in
   Systems Manager](sysman-paramstore-su-create.md "sysman-paramstore-su-create.md").
4. Choose **Edit**.
5. In the **Value** box, enter a new value, and then
   choose **Save changes**.
6. Choose the name of the parameter you just updated. On the
   **Overview** tab, verify that the version number
   incremented by 1, and verify the new value.
7. To view the history of all versions of a parameter, choose the
   **History** tab.

## Referencing a parameter

version

You can reference specific parameter versions in commands, API calls, and SSM
documents by using the following format:
ssm:``parameter-name`:`version-number``.

In the following example, the Amazon Elastic Compute Cloud (Amazon EC2) `run-instances
 command` uses version 3 of the parameter `golden-ami`.

Linux & macOS

```
aws ec2 run-instances \
    --image-id resolve:ssm:/golden-ami:3 \
    --count 1 \
    --instance-type t2.micro \
    --key-name `my-key-pair` \
    --security-groups `my-security-group`
```

Windows

```
aws ec2 run-instances ^
    --image-id resolve:ssm:/golden-ami:3 ^
    --count 1 ^
    --instance-type t2.micro ^
    --key-name `my-key-pair` ^
    --security-groups `my-security-group`
```

###### Note

Using `resolve` and a parameter value only works with the
`--image-id` option and a parameter that contains an
Amazon Machine Image (AMI) as its value. For more information, see [Using native parameter support in
Parameter Store for Amazon Machine Image IDs](parameter-store-ec2-aliases.md "parameter-store-ec2-aliases.md").

Here is an example for specifying version 2 of a parameter named
`MyRunCommandParameter` in an SSM document.

YAML

```
---
schemaVersion: '2.2'
description: Run a shell script or specify the commands to run.
parameters:
  commands:
    type: String
    description: "(Required) Specify a shell script or a command to run."
    displayType: textarea
    default: "{{ssm:MyRunCommandParameter:2}}"
mainSteps:
- action: aws:runShellScript
  name: RunScript
  inputs:
    runCommand:
    - "{{commands}}"
```

JSON

```
{
    "schemaVersion": "2.2",
    "description": "Run a shell script or specify the commands to run.",
    "parameters": {
        "commands": {
            "type": "String",
            "description": "(Required) Specify a shell script or a command to run.",
            "displayType": "textarea",
            "default": "{{ssm:MyRunCommandParameter:2}}"
        }
    },
    "mainSteps": [
        {
            "action": "aws:runShellScript",
            "name": "RunScript",
            "inputs": {
                "runCommand": [
                    "{{commands}}"
                ]
            }
        }
    ]
}
```
