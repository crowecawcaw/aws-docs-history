

# Action reference
<a name="action-ref"></a>

The following is the action definition YAML reference for your custom actions. You can define inputs, outputs, and resource integrations in the action definition YAML file. Once the action is defined, it can be referenced in your CI workflow file.

Choose a YAML property in the following code to see a description of it.

**Note**  
Most of the YAML properties that follow have corresponding UI elements in the visual editor. To look up a UI element, use **Ctrl\+F**. The element will be listed with its associated YAML property.

```
SchemaVersion: 1.0 
Name: MyAction   # Name of the action - string
Id: my-action   # String
Description: This is my action.   # String
Version: 1.0.0   # SEMVER

Configuration:
    {{Param1}}:
        Description: {{'First parameter'}}
        Required: {{true | false}}
        DisplayName: {{'Param1'}}
        Type: {{number | boolean | string}}
    {{Param2}}:
        Description: {{'Second parameter'}}
        Required: {{true | false}}
        Default: {{'Second value'}}
        DisplayName: {{'Param with space'}}
        Type: {{number | boolean | string}}

SupportedComputeType: 
    - {{'EC2'}}
    - {{'LAMBDA'}}

# Whether the action requires an environment
# Automatically pulls in the connection/role fields
Environment:
    Required: {{true | false}}
    Connection:
        Required: {{true | false}}

# Whether the action requires any input sources/artifacts
# If required is true, then action expects at least one Inputs -> Sources
# or Inputs -> Artifacts
      
Inputs:
    Sources:
        Required: {{true | false}}
    Artifacts:
        Required: {{true | false}}      
Outputs:   # Top 10 variables selected (if more than 10 produced)
    Variables:
        variable-name-1:
            Description: {{'Output variable description.'}}    
Runs:
    # Node
    Using: {{'node16' | 'node18'}}
    Main: {{'index.js'}}
    Pre: {{'setup.js'}}
    Post: {{'cleanup.js'}}
```

## Configuration
<a name="action.configuration"></a>

(**Configuration**)

(Required) A section where you can define the configuration properties of the action. 

Corresponding UI: **Configuration** tab

## Description
<a name="action.configuration.description"></a>

(Configuration/Param/**Description**)

(Required)

Provide a description of the action.

Corresponding UI: *none*

## Required
<a name="action.configuration.required"></a>

(Configuration/Param/**Required**)

(Required)

Specify whether the parameter is required. Set to `true` or `false`.

Corresponding UI: *none*

## Default
<a name="action.configuration.default"></a>

(Configuration/Param/**Default**)

(Optional)

Specify the default value of the parameter.

Corresponding UI: *none*

## DisplayName
<a name="action.configuration.displayname"></a>

(Configuration/Param/**DisplayName**)

(Optional)

Set the display name of the parameter.

Corresponding UI: *none*

## Type
<a name="action.configuration.type"></a>

(Configuration/Param/**Type**)

(Optional)

The type of parameter. You can use one of the following values (default is string):
+ Number (whole number)
+ Boolean (`TRUE` or `FALSE`)
+ String

Corresponding UI: *none*

## SupportedComputeTypes
<a name="action.supportedcomputetypes"></a>

(**SupportedComputeType**)

(Optional)

Specify the compute types to use for the action. You can specify the following types:
+ EC2
+ Lambda

If you don't define **SupportedComputeTypes**, the corresponding UI will show all available options (EC2 and Lambda). Otherwise, the UI will display the specified compute types.

Corresponding UI: Configuration tab/**Compute type**

## Environment
<a name="action.environment"></a>

(**Environment**)

(Optional)

Specify the CodeCatalyst environment to use with the action.

For more information about environments, see [Working with environments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments.html) and [Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments-creating-environment.html).

Corresponding UI: Configuration tab/**Environment**

## Connection
<a name="action.environment.connection"></a>

(**Connection**)

(Optional)

If you define the `Connection` field in your action definition YAML file, action users will be able to leverage the default connection and role capabilities that come with an environment by specifying the environment name in the workflow YAML. If you don’t include this connection field in your action definition YAML file, then the action users will need to specify the connection and the role they want to use with their environment.

**Tip**  
By defining the `Connection` field in your action definition YAML file, action users would only need to set the `Environment` in the action, and the connection and role are automatically applied to the action if the `Environment` is configured with a default connection and role.

For more information about account connections, see [Allowing access to AWS resources with connected AWS accounts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account.html).

For information about how to associate an account connection with your environment, see [Creating an environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments-creating-environment.html).

Corresponding UI: Configuration tab/Environment/**What's in my `my-environment`**

## Inputs
<a name="actions.inputs"></a>

(**Inputs**)

(Optional)

The `Inputs` section defines the data that an action needs during a workflow run.

**Note**  
A maximum of four inputs (one source and three artifacts) are allowed per build action or test action. Variables don't count towards this total.

If you need to refer to files residing in different inputs (say a source and an artifact), the source input is the primary input, and the artifact is the secondary input. References to files in secondary inputs take a special prefix to distiguish them from the primary. For details, see [ Example: Referencing files within an artifact](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-artifacts.html#workflows-working-artifacts-ex-ref-file).

Corresponding UI: **Inputs** tab

## Sources
<a name="actions.inputs.sources"></a>

(Inputs/**Sources**)

(Required)

Specify the labels that represent the source repositories that will be needed by the action. Currently, the only supported label is `WorkflowSource`, which represents the source repository where your workflow definition file is stored.

If you omit a source, then you must specify at least one input artifact under `action-name/Inputs/Artifacts`.

For more information, see [Working with sources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-sources.html).

Corresponding UI: *none*

## Artifacts - input
<a name="actions.inputs.artifacts"></a>

(Inputs/**Artifacts**)

(Optional)

Specify artifacts from previous actions that you want to provide as input to this action. These artifacts must already be defined as output artifacts in previous actions.

If you do not specify any input artifacts, then you must specify at least one source repository under `action-name/Inputs/Sources`.

Corresponding UI: Inputs tab/**Artifacts - optional**

## Outputs
<a name="actions.outputs"></a>

(**Outputs**)

(Optional)

Defines the data that is output by the action during a workflow run. If more than 10 output variables are produced, the top 10 variables are selected.

Corresponding UI: **Outputs** tab

## Variables - output
<a name="actions.outputs.variables"></a>

(Outputs/**Variables**)

(Optional)

Specify the variables that you want the action to export so that they are available for use by the subsequent actions.

For more information about variables, including examples, see [Working with variables](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables.html). 

Corresponding UI: Outputs tab/Variables/**Add variable**

## variable-name-1
<a name="actions.outputs.variable"></a>

(Outputs/Variables/**variable-name-1**)

(Optional)

Specify the name of a variable that you want the action to export.

Corresponding UI: *none*

## Description
<a name="actions.outputs.description"></a>

(Outputs/Variables/Time/**Description**)

(Optional)

Provide a description of the output variable.

Corresponding UI: *none*

## Runs
<a name="actions.runs"></a>

(**Runs**)

(Required)

Defines the runtime environment and main entry point for the action.

Corresponding UI: *none*

## Using
<a name="actions.runs.using"></a>

Runs/(**Using**)

(Required)

Specify the type of runtime environment. Currently, Node 16 and Node 18 are the options.

Corresponding UI: *none*

## Main
<a name="actions.runs.main"></a>

Runs/(**Main**)

(Optional)

Specify the file for the entry point of a Node.js application. This file contains your action code. Required if Node 16 or Node 18 runtime is specified for [Using](#actions.runs.using).

Corresponding UI: *none*

## Pre
<a name="actions.runs.pre"></a>

Runs/(**Pre**)

(Optional)

Allows you to run a script at the beginning of the action run. Can be defined if Node 16 or Node 18 runtime is specified for [Using](#actions.runs.using).

Corresponding UI: *none*

## Post
<a name="actions.runs.post"></a>

Runs/(**Post**)

(Optional)

Allows your to run a script at the end of the action run. Can be defined if Node 16 or Node 18 runtime is specified for [Using](#actions.runs.using).

Corresponding UI: *none*