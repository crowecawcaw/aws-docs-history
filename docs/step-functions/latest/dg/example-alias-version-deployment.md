# Example: Alias and version deployment in Step Functions

The following example of the
Canary
deployment technique shows how you can deploy a new state machine version with the
AWS Command Line Interface. In this example, the alias you create routes 20 percent of execution traffic to
the new version. It then routes the remaining 80 percent the earlier version. To deploy a
new state machine [version](concepts-state-machine-version.md "concepts-state-machine-version.md") and shift
execution traffic with an [alias](concepts-state-machine-alias.md "concepts-state-machine-alias.md"),
complete the following steps:

1. ###### Publish a version from the current state machine revision.

Use the **publish-state-machine-version** command in the AWS CLI
to publish a version from the current revision of a state machine called
``myStateMachine`:`

```
aws stepfunctions publish-state-machine-version --state-machine-arn arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine`
```

The response returns the `stateMachineVersionArn` of the version that
you published. For example,
`arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine`:1`. 2. ###### Create an alias that points to the state machine version.

Use the **create-state-machine-alias** command to create an
alias named `PROD` that points to version
1 of `myStateMachine`:

```
aws stepfunctions create-state-machine-alias --name PROD --routing-configuration "[{\"stateMachineVersionArn\":\"arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine`:`1`\",\"weight\":100}]"
```

3. ###### Verify that executions started by the alias use correct published
   version.

Start a new execution of
`myStateMachine` by providing the ARN
of the alias `PROD` in the
**start-execution** command:

```
aws stepfunctions start-execution
  --state-machine-arn arn:aws:states:`region`:`account-id`:stateMachineAlias:`myStateMachine`:PROD
  --input "{}"
```

If you provide the state machine ARN in the [StartExecution](../apireference/API_StartExecution.md "../apireference/API_StartExecution.md") request, it uses the most recent [revision](concepts-cd-aliasing-versioning.md#statemachinerev "concepts-cd-aliasing-versioning.md#statemachinerev") of the state machine instead of the version specified in your alias for starting the execution. 4. ###### Update the state machine definition and publish a new version.

Update `myStateMachine` and publish its
new version. To do this, use the optional `publish` parameter of the
**update-state-machine** command:

```
aws stepfunctions update-state-machine
    --state-machine-arn arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine`
    --definition $UPDATED_STATE_MACHINE_DEFINITION
    --publish

```

The response returns the `stateMachineVersionArn` for the new version.
For example,
`arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine`:2`. 5. ###### Update the alias to point to both the versions and set the alias' [routing configuration](concepts-state-machine-alias.md#alias-routing-config "concepts-state-machine-alias.md#alias-routing-config").

Use the **update-state-machine-alias** command to update the
routing configuration of the alias `PROD`. Configure the alias so
that 80 percent of the execution traffic goes to version 1 and the remaining 20
percent goes to version 2:

```
aws stepfunctions update-state-machine-alias --state-machine-alias-arn arn:aws:states:`region`:`account-id`:stateMachineAlias:`myStateMachine`:PROD --routing-configuration "[{\"stateMachineVersionArn\":\"arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine:1`\",\"weight\":80}, {\"stateMachineVersionArn\":\"arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine:2`\",\"weight\":20}]"
```

6. ###### Replace version 1 with version 2.

After
you verify that your new state machine version works correctly, you can deploy
the new state machine version. To do this, update the alias again to assign 100
percent of execution traffic to the new version.

Use the **update-state-machine-alias** command to set the routing
configuration of the alias `PROD` to 100 percent for version 2:

```
aws stepfunctions update-state-machine-alias --state-machine-alias-arn arn:aws:states:`region`:`account-id`:stateMachineAlias:myStateMachine:PROD --routing-configuration "[{\"stateMachineVersionArn\":\"arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine:2`\",\"weight\":100}]"
```

###### Tip

To roll back the deployment of version 2, edit the alias' routing configuration to
shift 100 percent of traffic to the newly deployed version.

```
aws stepfunctions update-state-machine-alias
  --state-machine-alias-arn arn:aws:states:`region`:`account-id`:stateMachineAlias:`myStateMachine`:PROD
  --routing-configuration "[{\"stateMachineVersionArn\":\"arn:aws:states:`region`:`account-id`:stateMachine:`myStateMachine`:1\",\"weight\":100}]"
```

You can use versions and aliases to perform other types of deployments. For instance,
you can perform a _rolling deployment_ of a new version of your state
machine. To do so, gradually increase the weighted percentage in the routing configuration of the alias that points to the new version.

You can also use versions and aliases to perform a _blue/green
deployment_. To do so, create an alias named `green` that runs the current version
1 of your state machine. Then, create another alias named `blue` that runs the new version, for example, `2`. To
test the new version, send execution traffic to the `blue` alias. When you're confident that
your new version works correctly, update the `green` alias to point to
your new version.
