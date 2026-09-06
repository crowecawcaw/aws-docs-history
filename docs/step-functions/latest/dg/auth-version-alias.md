

# Authorization for versions and aliases in Step Functions workflows
<a name="auth-version-alias"></a>

To invoke Step Functions API actions with a version or an alias, you need appropriate permissions. To authorize a version or an alias to invoke an API action, Step Functions uses the state machine’s ARN instead of using the version ARN or alias ARN. You can also scope down the permissions for a specific version or alias. For more information, see [Scoping down permissions](#auth-scope-permission-version-alias).

You can use the following IAM policy example of a state machine named `{{myStateMachine}}` to invoke the [CreateStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachineAlias.html) API action to create a state machine alias.

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "states:CreateStateMachineAlias",
      "Resource": "arn:aws:states:{{us-east-1}}:{{123456789012}}:stateMachine:{{myStateMachine}}"
    }
  ]
}
```

When you set permissions to allow or deny access to API actions using state machine versions or aliases, consider the following:
+ If you use the `publish` parameter of the [CreateStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachine.html) and [UpdateStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html) API actions to publish a new state machine version, you also need the `ALLOW` permission on the [PublishStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_PublishStateMachineVersion.html) API action.
+ The [DeleteStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachine.html) API action deletes all versions and aliases associated with a state machine.

## Scoping down permissions for a version or alias
<a name="auth-scope-permission-version-alias"></a>

You can use a qualifier to further scope down the authorization permission needed by a version or an alias. A qualifier refers to a version number or an alias name. You use the qualifier to qualify a state machine. The following example is a state machine ARN that uses an alias named `PROD` as the qualifier.

```
arn:aws:states:{{region}}:{{account-id}}:stateMachine:{{myStateMachine}}:{{PROD}}
```

For more information about qualified and unqualified ARNs, see [Associating executions with a version or alias](execution-alias-version-associate.md).

You scope down the permissions using the optional context key named `states:StateMachineQualifier` in an IAM policy's `Condition` statement. For example, the following IAM policy for a state machine named `myStateMachine` denies access to invoke the [DescribeStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachine.html) API action with an alias named as `PROD` or the version `1`.

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "states:DescribeStateMachine",
      "Resource": "arn:aws:states:{{us-east-1}}:{{123456789012}}:stateMachine:{{myStateMachine}}",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "states:StateMachineQualifier": [
            "PROD",
            "1"
          ]
        }
      }
    }
  ]
}
```

The following list specifies the API actions on which you can scope down the permissions with the `StateMachineQualifier` context key.
+ [CreateStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachineAlias.html)
+ [DeleteStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineAlias.html)
+ [DeleteStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineVersion.html)
+ [DescribeStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachine.html)
+ [DescribeStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachineAlias.html)
+ [ListExecutions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html)
+ [ListStateMachineAliases](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachineAliases.html)
+ [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html)
+ [StartSyncExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html)
+ [UpdateStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachineAlias.html)