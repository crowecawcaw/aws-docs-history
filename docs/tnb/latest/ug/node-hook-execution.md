

# AWS.HookExecution
<a name="node-hook-execution"></a>

A lifecycle hook provides you with the ability to run your own scripts as part of your infrastructure and network instantiation.

## Syntax
<a name="node-hook-execution-syntax"></a>

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
<a name="node-hook-execution-capabilities"></a><a name="node_hook_execution"></a>`execution`

Properties for the hook execution engine that runs the hook scripts.

 `type`    
The hook execution engine type.  
Required: No  
Type: String  
Possible values: `CODE_BUILD` 

## Requirements
<a name="node-hook-execution-requirements"></a>

 `definition`    
An [AWS.HookDefinition.Bash](node-hook-bash.md) node.  
Required: Yes  
Type: String

 `vpc`    
An [AWS.Networking.VPC](node-vpc.md) node.  
Required: Yes  
Type: String

## Example
<a name="node-hook-execution-example"></a>

```
SampleHookExecution:
  type: tosca.nodes.AWS.HookExecution
  requirements:
    definition: SampleHookScript
    vpc: SampleVPC
```