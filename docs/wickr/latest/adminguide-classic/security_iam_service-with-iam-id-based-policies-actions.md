This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Policy actions

for Wickr

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Wickr actions, see [Actions Defined by AWS Wickr](../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-actions-as-permissions "../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in Wickr use the following prefix before the action:

```
wickr
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "wickr:`action1`",
      "wickr:`action2`"
         ]
```

To view examples of Wickr identity-based policies, see [Identity-based policy examples for
AWS Wickr](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
