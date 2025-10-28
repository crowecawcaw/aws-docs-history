# IAM policy structure

The following topics explain the structure of an IAM policy.

###### Topics

- [Policy syntax](#policy-syntax "#policy-syntax")
- [API actions for AWS Batch](#UsingWithbatch_Actions "#UsingWithbatch_Actions")
- [Amazon Resource Names for AWS Batch](#batch_ARN_Format "#batch_ARN_Format")
- [Confirm that users have the required
  permissions](#check-required-permissions "#check-required-permissions")

## Policy syntax

An IAM policy is a JSON document that consists of one or more statements. Each statement
is structured as follows.

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

There are four primary elements that make up a statement:

- **Effect**: The _effect_ can be `Allow` or `Deny`.
  By default, users don't have permission to use resources and API actions. So, all requests are denied. An explicit
  allow overrides the default. An explicit deny overrides any allows.
- **Action**: The _action_ is the specific API action
  that you're granting or denying permission for. For instructions on how to specify the
  _action_, see [API actions for AWS Batch](#UsingWithbatch_Actions "#UsingWithbatch_Actions").
- **Resource**: The resource that's affected by the action. With some
  AWS Batch API actions, you can include specific resources in your policy that can be created or
  modified by the action. To specify a resource in the statement, use its Amazon Resource Name
  (ARN). For more information, see [Supported resource-level permissions for AWS Batch API
  actions](batch-supported-iam-actions-resources.md "batch-supported-iam-actions-resources.md") and [Amazon Resource Names for AWS Batch](#batch_ARN_Format "#batch_ARN_Format"). If the AWS Batch API operation currently doesn't support
  resource-level permissions, include a wildcard (\*) to specify that all resources can be
  affected by the action.
- **Condition**: Conditions are optional. They can be used to control when your policy is in
  effect.

For more information about example IAM policy statements for AWS Batch, see [Resource: Example policies for AWS Batch](ExamplePolicies_BATCH.md "ExamplePolicies_BATCH.md").

## API actions for AWS Batch

In an IAM policy statement, you can specify any API action from any service that supports
IAM. For AWS Batch, use the following prefix with the name of the API action:
`batch:` (for example, `batch:SubmitJob` and
`batch:CreateComputeEnvironment`).

To specify multiple actions in a single statement, separate each action with a
comma.

```
"Action": ["batch:*action1*", "batch:*action2*"]
```

You can also specify multiple actions by including a wildcard (\*). For example, you can
specify all actions with a name that begins with the word "Describe."

```
"Action": "batch:Describe*"
```

To specify all AWS Batch API actions, include a wildcard (\*).

```
"Action": "batch:*"
```

For a list of AWS Batch actions, see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") in the
_AWS Batch API Reference_.

## Amazon Resource Names for AWS Batch

Each IAM policy statement applies to the resources that you specify using their Amazon
Resource Names (ARNs).

An Amazon Resource Name (ARN) has the following general syntax:

```
arn:aws:[*service*]:[*region*]:[*account*]:*resourceType*/*resourcePath*
```

_service_

The service (for example, `batch`).

_region_

The AWS Region for the resource (for example, `us-east-2`).

_account_

The AWS account ID, with no hyphens (for example, `123456789012`).

_resourceType_

The type of resource (for example, `compute-environment`).

_resourcePath_

A path that identifies the resource. You can use a wildcard (\*) in your paths.

AWS Batch API operations currently support resource-level permissions on several API
operations. For more information, see [Supported resource-level permissions for AWS Batch API
actions](batch-supported-iam-actions-resources.md "batch-supported-iam-actions-resources.md"). To specify all resources, or if a specific
API action doesn't support ARNs, include a wildcard (\*) in the `Resource`
element.

```
"Resource": "*"
```

## Confirm that users have the required

permissions

Before you put an IAM policy into production, make sure that it grants users the
permissions to use the specific API actions and resources that they need.

To do this, first create a user for testing purposes and attach the IAM policy to the test user. Then, make a
request as the test user. You can make test requests in the console or with the AWS CLI.

###### Note

You can also test your policies by using the [IAM Policy Simulator](https://policysim.aws.amazon.com/home/index.jsp?# "https://policysim.aws.amazon.com/home/index.jsp?#"). For
more information about the policy simulator, see [Working with the IAM Policy
Simulator](../../../IAM/latest/UserGuide/policies_testing-policies.md "../../../IAM/latest/UserGuide/policies_testing-policies.md") in the _IAM User Guide_.

If the policy doesn't grant the user the permissions that you expected, or is overly
permissive, you can adjust the policy as needed. Retest until you get the desired results.

###### Important

It can take several minutes for policy changes to propagate before they take effect.
Therefore, we recommend that you allow at least five minutes to pass before you test your
policy updates.

If an authorization check fails, the request returns an encoded message with diagnostic
information. You can decode the message using the `DecodeAuthorizationMessage`
action. For more information, see [DecodeAuthorizationMessage](../../../STS/latest/APIReference/API_DecodeAuthorizationMessage.md "../../../STS/latest/APIReference/API_DecodeAuthorizationMessage.md") in the _AWS Security Token Service API Reference_, and [decode-authorization-message](../../../cli/latest/reference/sts/decode-authorization-message.md "../../../cli/latest/reference/sts/decode-authorization-message.md")
in the _AWS CLI Command Reference_.
