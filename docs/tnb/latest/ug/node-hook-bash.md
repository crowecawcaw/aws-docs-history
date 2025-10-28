# AWS.HookDefinition.Bash

Defines an AWS HookDefinition in `bash`.

## Syntax

```
tosca.nodes.AWS.HookDefinition.Bash:
  properties:
    implementation: String
    environment_variables: List
    execution_role: String
```

## Properties

`implementation`

The relative path to the hook definition. The format must be:
`./hooks/`script_name`.sh`

Required: Yes

Type: String

`environment_variables`

The environment variables for the hook bash script. Use the following
format:
``envName`=`envValue``
with the following regex patterns:

- For values without references: `^[a-zA-Z0-9]+[a-zA-Z0-9\-\_]*[a-zA-Z0-9]+=[a-zA-Z0-9]+[a-zA-Z0-9\-\_]*[a-zA-Z0-9]+$`
- For static references: `^[a-zA-Z0-9]+[a-zA-Z0-9\-\_]*[a-zA-Z0-9]+=\$\{[a-zA-Z0-9]+\.(properties|capabilities|requirements)(\.([a-zA-Z0-9\-_]+))+\}$`
- For dynamic references: `^[a-zA-Z0-9]+[a-zA-Z0-9\-\_]*[a-zA-Z0-9]+=\$\{[a-zA-Z0-9]+\.(name|id|arn)\}$`

Ensure that the
``envName`=`envValue``
value meets the following criteria:

- Do not use spaces.
- Start `envName` with a letter (A-Z or a-z) or
  number (0-9).
- Do not start the environment variable name with the following
  AWS TNB reserved keywords (case insensitive):
  - CODEBUILD
  - TNB
  - HOME
  - AWS

- You can use any number of letters (A-Z or a-z), numbers (0-9), and
  special characters `-` and `_` for `envName`
  and `envValue`.
- Each environment variable (each `envName`=`envValue`) must be less than 128 characters.

Example: `A123-45xYz=Example_789`

Required: No

Type: List

`execution_role`

The role for hook execution.

Required: Yes

Type: String

## Example

```
SampleHookScript:
  type: tosca.nodes.AWS.HookDefinition.Bash
  properties:
    implementation: "`./hooks/myhook.sh`"
    environment_variables:
      - "variable01=value01"
      - "variable02=value02"
    execution_role: "arn:aws:iam::${AWS::TNB::AccountId}:role/`SampleHookPermission`"
```
