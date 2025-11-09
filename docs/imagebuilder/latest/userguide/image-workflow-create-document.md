# Create a YAML workflow document

The YAML format definition document configures input, output, and workflow steps for the
build and test stages of the image build process. You can start from templates that include
standardized steps, or you can start from scratch to define your own workflow. Whether you
use a template or start from scratch, you can customize the workflow to fit your needs.

## Structure of a YAML workflow document

The YAML workflow document that Image Builder uses to perform image build and test actions is structured
as follows.

- [Workflow document identification](#wfdoc-struct-ident "#wfdoc-struct-ident")
- [Workflow document input parameters](#wfdoc-struct-param "#wfdoc-struct-param")
- [Workflow document steps](#wfdoc-struct-step "#wfdoc-struct-step")
- [Workflow document outputs](#wfdoc-struct-output "#wfdoc-struct-output")

### Workflow document identification

Uniquely identifies the workflow. This section can include the following attributes.

| Field         | Description                                 | Type   | Required |
| ------------- | ------------------------------------------- | ------ | -------- |
| name          | The name of the workflow document.          | String | No       |
| description   | The document description.                   | String | No       |
| schemaVersion | The document schema version, currently 1.0. | String | Yes      |

**Example**

```
`---
name: sample-test-image
description: Workflow for a sample image, with extra configuration options exposed through workflow parameters.
schemaVersion: 1.0`
```

### Workflow document input parameters

This part of the workflow document defines input parameters that the caller can specify.
If you don't have any parameters, you can leave this section out. If you do specify
parameters, each parameter can include the following attributes.

| Field       | Description                                                                                                                                                                      | Type                             | Required | Constraints                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------- |
| name        | The name of the parameter.                                                                                                                                                       | String                           | Yes      |                                                                                                                            |
| description | The parameter description.                                                                                                                                                       | String                           | No       |                                                                                                                            |
| default     | The default value of the parameter, if no value is provided. If you<br>don't include a default value in the parameter definition, the parameter<br>value is required at runtime. | Matches the parameter data type. | No       |                                                                                                                            |
| type        | The data type of the parameter. If you don't include the data<br>type in the parameter definition, the parameter type defaults to a<br>string value required at runtime.         | String                           | Yes      | The data type of the parameter must be one of the following:<br>• `string`<br>• `integer`<br>• `boolean`<br>• `stringList` |

**Example**

Specify the parameter in the workflow document.

```
`parameters:
 - name: waitForActionAtEnd
 type: boolean
 default: true
 description: "Wait for an external action at the end of the workflow"`
```

Use the parameter value in the workflow document.

```
`$.parameters.waitForActionAtEnd`
```

### Workflow document steps

Specifies up to 15 step actions for the workflow. Steps run in the order
that they're defined within the workflow document. In case of failure,
a rollback runs in reverse order, starting with the step that failed, and
working backward through prior steps.

Each step can refer to the output of any prior step actions. This is known
as _chaining, or referencing_. To refer to output from a
prior step action, you can use a JSONPath selector. For example:

```
`$.stepOutputs.`step-name`.`output-name``
```

For more information, see [Use dynamic variables in your workflow document](wfdoc-dynamic-vars.md "wfdoc-dynamic-vars.md").

###### Note

Even though the step itself doesn't have an output attribute, any
output from a step action is included in `stepOutput` for
the step.

Each step can include the following attributes.

| Field                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Type    | Required | Default value                                                      | Constraints                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------- |
| action                                                                              | The workflow action that this step performs.                                                                                                                                                                                                                                                                                                                                                                                                                                          | String  | Yes      |                                                                    | Must be a supported step action for Image Builder workflow documents.                                                                                                                                                                                                                                                                                                                                                 |
| `if`, followed by a set of conditional statements that modify<br>the `if` operator. | Conditional statements add flow of control decision points to the body of<br>your workflow steps.                                                                                                                                                                                                                                                                                                                                                                                     | Dict    | No       |                                                                    | Image Builder supports the following conditional statements as modifiers to the<br>`if` operator:<br>• Branching conditions and modifiers: `if`, `and`,<br>`or`, `not`.<br>Branching conditions are specified on a line by themselves.<br>• Comparison operators: `booleanEquals`, `numberEquals`,<br>`numberGreaterThan`, `numberGreaterThanEquals`,<br>`numberLessThan`, `numberLessThanEquals`,<br>`stringEquals`. |
| description                                                                         | The step description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String  | No       |                                                                    | Empty strings are not allowed. If included, length must be<br>1-1024 characters.                                                                                                                                                                                                                                                                                                                                      |
| inputs                                                                              | Contains parameters that the step action needs to run. You can specify<br>key values as static values, or with a JSONPath variable that resolves to<br>the correct data type.                                                                                                                                                                                                                                                                                                         | Dict    | Yes      |                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| name                                                                                | The name of the step. This name must be unique within the<br>workflow document.                                                                                                                                                                                                                                                                                                                                                                                                       | String  | Yes      |                                                                    | Length must be between 3-128 characters.<br>Can include alphanumeric characters and `_`. No spaces.                                                                                                                                                                                                                                                                                                                   |
| onFailure                                                                           | Configures the action to take if the step fails, as follows.<br>Behavior<br>• `Abort` – Fails the step, fails the workflow, and<br>doesn't run any remaining steps after the step that failed. If rollback<br>is enabled, the rollback begins with the step that failed, and continues<br>until all steps that allow it are rolled back.<br>• `Continue` – Fails the step, but continues to<br>run remaining steps after the step that failed. In this case, there is<br>no rollback. | String  | No       | `Abort`                                                            | `Abort`                                                                                                                                                                                                                                                                                                                                                                                                               | `Continue` |
| rollbackEnabled                                                                     | Configures whether the step will be rolled back if a failure<br>occurs. You can use a static Boolean value or a dynamic JSONPath<br>variable that resolves to a Boolean value.                                                                                                                                                                                                                                                                                                        | Boolean | No       | `true`                                                             | `true`                                                                                                                                                                                                                                                                                                                                                                                                                | `false`    | or a JSONPath<br>variable that resolves to true or false. |
| timeoutSeconds                                                                      | The maximum time, in seconds, that the step runs before failing and<br>retrying, if retries apply.                                                                                                                                                                                                                                                                                                                                                                                    | Integer | No       | Depends on the default defined for the step action, if applicable. | Between 1-86400 seconds (24 hrs maximum)                                                                                                                                                                                                                                                                                                                                                                              |

**Example**

```
`steps:
 - name: LaunchTestInstance
 action: LaunchInstance
 onFailure: Abort
 inputs:
 waitFor: "ssmAgent"

 - name: ApplyTestComponents
 action: ExecuteComponents
 onFailure: Abort
 inputs:
 instanceId.$: "$.stepOutputs.LaunchTestInstance.instanceId"

 - name: TerminateTestInstance
 action: TerminateInstance
 onFailure: Continue
 inputs:
 instanceId.$: "$.stepOutputs.LaunchTestInstance.instanceId"

 - name: WaitForActionAtEnd
 action: WaitForAction
 if:
 booleanEquals: true
 value: "$.parameters.waitForActionAtEnd"`
```

### Workflow document outputs

Defines outputs for the workflow. Each output is a key value pair
that specificies the name of the output and the value. You can use
outputs to export data at runtime that subsequent workflows can use.
This section is optional.

Each output that you define includes the following attributes.

| Field | Description                                                                                                                                                                                                                                               | Type   | Required |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- |
| name  | The name of the output. The name must be unique across the<br>workflows that you include in your pipeline.                                                                                                                                                | String | Yes      |
| value | The value for the output. The value of the string can be a<br>dyanmic variable, such as an output file from a step action.<br>For more information, see [Use dynamic variables in your workflow document](wfdoc-dynamic-vars.md "wfdoc-dynamic-vars.md"). | String | Yes      |

**Example**

Create an output image ID for the workflow document with step output
from the `createProdImage` step.

```
`outputs:
 - name: 'outputImageId'
 value: '$.stepOutputs.createProdImage.imageId'`
```

Refer to the workflow output in the next workflow.

```
`$.workflowOutputs.outputImageId`
```
