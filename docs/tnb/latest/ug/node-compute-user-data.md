# AWS.Compute.UserData

AWS TNB supports launching Amazon EC2 instances with custom user data, through the UserData
node in Network Service Descriptor (NSD). For more information about custom user data, see
[User data and shell
scripts](../../../AWSEC2/latest/UserGuide/user-data.md#user-data-shell-scripts "../../../AWSEC2/latest/UserGuide/user-data.md#user-data-shell-scripts") in the _Amazon EC2 User Guide_.

During network instantiation, AWS TNB provides the Amazon EC2 instance registration to the
cluster through a user-data script. When custom user data is also provided, AWS TNB
merges both scripts and passes them on as a [multimime](../../../AWSEC2/latest/UserGuide/user-data.md#user-data-mime-multi "../../../AWSEC2/latest/UserGuide/user-data.md#user-data-mime-multi")
script to Amazon EC2. The custom user-data script is run prior to the Amazon EKS registration
script.

To use custom variables in the user-data script, add an exclamation mark `!`
after the open curly brace `{`. For example, to use `MyVariable` in
the script, enter: `{!MyVariable}`

###### Note

- AWS TNB supports user-data scripts up to 7 KB in size.
- Because AWS TNB uses CloudFormation to process and render the `multimime`
  user-data script, ensure that the script adheres to all CloudFormation rules.

## Syntax

```
tosca.nodes.AWS.Compute.UserData:
  properties:
    implementation: String
    content_type: String
```

## Properties

`implementation`

The relative path to the user data script definition. The format must be:
`./scripts/script_name.sh`

Required: Yes

Type: String

`content_type`

Content type of the user data script.

Required: Yes

Type: String

Possible values: `x-shellscript`

## Example

```
ExampleUserData:
  type: tosca.nodes.AWS.Compute.UserData
  properties:
    content_type: `"text/x-shellscript"`
    implementation: `"./scripts/customUserData.sh"`
```
