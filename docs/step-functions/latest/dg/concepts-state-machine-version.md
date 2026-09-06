

# State machine versions in Step Functions workflows
<a name="concepts-state-machine-version"></a>

A *version* is a numbered, **immutable** snapshot of a state machine. You publish versions from the most recent revision made to that state machine. Each version has a unique Amazon Resource Name (ARN) which is a combination of state machine ARN and the version number separated by a colon (:). The following example shows the format of a state machine version ARN.

```
arn:{{partition}}:states:{{region}}:{{account-id}}:stateMachine:{{myStateMachine}}:1
```

To start using state machine versions, you must publish the first version. After you publish a version, you can invoke the [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) API action with the version ARN. You can't edit a version, but you can update a state machine and publish a new version. You can also publish multiple versions of your state machine.

![Fuzzy illustrative diagram showing how versions are immutable snapshots of state machines.](http://docs.aws.amazon.com/step-functions/latest/dg/images/versioning-concept.png)


When you publish a new version of your state machine, Step Functions assigns it a version number. Version numbers start at 1 and increase monotonically for each new version. Version numbers aren't reused for a given state machine. If you delete version 10 of your state machine and then publish a new version, Step Functions publishes it as version 11.

The following properties are the same for all versions of a state machine:
+ All versions of a state machine share the same type [(Standard or Express)](choosing-workflow-type.md).
+ You can't change the name or creation date of a state machine between versions.
+ Tags apply globally to state machines. You can manage tags for state machines using the [TagResource](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UntagResource.html) API actions.

State machines also contain properties that are a part of each version and [revision](concepts-cd-aliasing-versioning.md#statemachinerev), but these properties can differ between two given versions or revisions. These properties include [State machine definition](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html#StepFunctions-UpdateStateMachine-request-definition), [IAM role](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html#StepFunctions-UpdateStateMachine-request-roleArn), [tracing configuration](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html#StepFunctions-UpdateStateMachine-request-tracingConfiguration), and [logging configuration](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html#StepFunctions-UpdateStateMachine-request-loggingConfiguration).

## Publishing a state machine version (Console)
<a name="procedure-create-versions"></a>

You can publish up to 1000 versions of a state machine. To request an increase to this soft limit, use the **Support Center** page in the [AWS Management Console](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html). You can manually delete unused versions from the console or by invoking the [DeleteStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineVersion.html) API action.

**To publish a state machine version**

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/), and then choose an existing state machine.

1. On the **State machine detail** page, choose **Edit**.

1. Edit the state machine definition as required, and then choose **Save**.

1. Choose **Publish version**.

1. (Optional) In the **Description** field of the dialog box that appears, enter a brief description about the state machine version.

1. Choose **Publish**.

**Note**  
When you publish a new version of your state machine, Step Functions assigns it a version number. Version numbers start at 1 and increase monotonically for each new version. Version numbers aren't reused for a given state machine. If you delete version 10 of your state machine and then publish a new version, Step Functions publishes it as version 11.

## Managing versions with Step Functions API operations
<a name="manage-versions-with-api"></a>

Step Functions provides the following API operations to publish and manage state machine versions:
+ [PublishStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_PublishStateMachineVersion.html) – Publishes a version from the current [revision](concepts-cd-aliasing-versioning.md#statemachinerev) of a state machine.
+ [UpdateStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html) – Publishes a new state machine version if you update a state machine and set the `publish` parameter to `true` in the same request.
+ [CreateStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachine.html) – Publishes the first revision of the state machine if you set the `publish` parameter to `true`.
+ [ListStateMachineVersions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachineVersions.html) – Lists versions for the specified state machine ARN.
+ [DescribeStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachine.html) – Returns the state machine version details for a version ARN specified in `stateMachineArn`.
+ [DeleteStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineVersion.html) – Deletes a state machine version.

To publish a new version from the current revision of a state machine called `{{myStateMachine}}` using the AWS Command Line Interface, use the `publish-state-machine-version` command:

```
aws stepfunctions publish-state-machine-version --state-machine-arn arn:aws:states:{{region}}:{{account-id}}:stateMachine:{{myStateMachine}}
```

The response returns the `stateMachineVersionArn`. For example, the previous command returns a response of`arn:aws:states:{{region}}:{{account-id}}:stateMachine:{{myStateMachine}}:1`.

**Note**  
When you publish a new version of your state machine, Step Functions assigns it a version number. Version numbers start at 1 and increase monotonically for each new version. Version numbers aren't reused for a given state machine. If you delete version 10 of your state machine and then publish a new version, Step Functions publishes it as version 11.

## Running a state machine version from the console
<a name="procedure-run-version"></a>

To start using state machine versions, you must first publish a version from the current state machine [revision](concepts-cd-aliasing-versioning.md#statemachinerev). To publish a version, use the Step Functions console or invoke the [PublishStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_PublishStateMachineVersion.html) API action. You can also invoke the [UpdateStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachineAlias.html) API action with an optional parameter named `publish` to update a state machine and publish its version.

You can start executions of a version by using the console or by invoking the [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) API action and providing the version ARN. You can also use an [alias](concepts-state-machine-alias.md) to start executions of a version. Based on its [routing configuration](concepts-state-machine-alias.md#alias-routing-config), an alias routes traffic to a specific version.

If you start a state machine execution without using a version, Step Functions uses the most recent revision of the state machine for the execution. For information about how Step Functions associates an execution with a version, see [Associating executions with a version or alias](execution-alias-version-associate.md).

**To start an execution using a state machine version**

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/), and then choose an existing state machine that you've published one or more versions for. To learn how to publish a version, see [Publishing a state machine version (Console)](#procedure-create-versions).

1. On the **State machine detail** page, choose the **Versions** tab.

1. In the **Versions** section, do the following:

   1. Select the version that you want to start the execution with.

   1. Choose **Start execution**.

1. (Optional) In the **Start execution** dialog box, enter a name for the execution.

1. (Optional) , enter the execution input, and then choose **Start execution**.