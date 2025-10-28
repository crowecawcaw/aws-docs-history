# AWS.HookExecution

A lifecycle hook provides you with the ability to run your own scripts as part of your
infrastructure and network instantiation.

## Syntax

```
tosca.nodes.AWS.HookExecution:
  capabilities:
    execution:
      properties:
        type: String
  requirements:
    definition: String
    vpc: String
```

## Capabilities

###### `execution`

Properties for the hook execution engine that runs the hook scripts.

`type`

The hook execution engine type.

Required: No

Type: String

Possible values: `CODE_BUILD`

## Requirements

`definition`

An [AWS.HookDefinition.Bash](node-hook-bash.md "node-hook-bash.md")
node.

Required: Yes

Type: String

`vpc`

An [AWS.Networking.VPC](node-vpc.md "node-vpc.md") node.

Required: Yes

Type: String

## Example

```
SampleHookExecution:
  type: tosca.nodes.AWS.HookExecution
  requirements:
    definition: SampleHookScript
    vpc: SampleVPC
```
