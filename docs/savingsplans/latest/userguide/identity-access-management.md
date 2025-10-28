# Identity and Access Management for

Savings Plans

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. As an administrator, you can create roles under your AWS account that
your users can assume. You control the permissions that your users have to perform tasks
using AWS resources. You can use IAM at no additional charge.

By default, users don't have permissions for Savings Plans resources and operations. To allow
users to manage Savings Plans resources, you must create a role to delegate permissions to a user.
Follow the instructions in [Creating
a role for a user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User
Guide_.

## Policy structure

An IAM policy is a JSON document that consists of one or more statements. Each
statement is structured as follows.

```
{
  "Statement":[{
    "Effect":"`effect`",
    "Action":"`action`",
    "Resource":"`arn`",
    "Condition":{
      "`condition`":{
        "`key`":"`value`"
        }
      }
    }
  ]
}
```

There are various elements that make up a statement:

- **Effect:** The _effect_ can be
  `Allow` or `Deny`. By default, users don't have
  permission to use resources and API actions, so all requests are denied. An
  explicit allow overrides the default. An explicit deny overrides any
  allows.
- **Action**: The _action_ is the specific
  API action for which you are granting or denying permission.
- **Resource**: The resource that's affected by the action.
  Some Amazon EC2 API actions allow you to include specific resources in your policy
  that can be created or modified by the action. To specify a resource in the
  statement, you need to use its Amazon Resource Name (ARN). For more information,
  see [Actions Defined by Savings Plans](../../../IAM/latest/UserGuide/list_awssavingsplans.md#awssavingsplans-actions-as-permissions "../../../IAM/latest/UserGuide/list_awssavingsplans.md#awssavingsplans-actions-as-permissions").
- **Condition**: Conditions are optional. They can be used to
  control when your policy is in effect. For more information, see [Condition Keys for Savings Plans](../../../IAM/latest/UserGuide/list_awssavingsplans.md#awssavingsplans-policy-keys "../../../IAM/latest/UserGuide/list_awssavingsplans.md#awssavingsplans-policy-keys").

## AWS managed policies

The managed policies created by AWS grant the required permissions for common use
cases. After you create a role that your user can assume, you can attach your policy to
it, based on the access needed. Each policy grants access to all or some of the API
actions for Savings Plans.

The following are the AWS managed polices for Savings Plans:

- **AWSSavingsPlansFullAccess**–Grants full access to
  Savings Plans.
- **AWSSavingsPlansReadOnlyAccess**–Grants read-only
  access to Savings Plans.

## Example policies

In an IAM policy statement, you can specify any API action from any service that
supports IAM. For Savings Plans, use the following prefix with the name of the API action:
`savingsplans:`. For example:

- `savingsplans:CreateSavingsPlan`
- `savingsplans:DescribeSavingsPlans`

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": ["savingsplans:*action1*", "savingsplans:*action2*"]
```

You can also specify multiple actions using wildcards. For example, you can specify
all Savings Plans API actions whose name begins with the word "Describe" as follows:

```
"Action": "savingsplans:Describe*"
```

To specify all Savings Plans API actions, use the \* wildcard as follows:

```
"Action": "savingsplans:*"
```
