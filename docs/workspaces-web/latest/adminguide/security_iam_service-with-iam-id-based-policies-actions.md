# Policy actions

for WorkSpaces Secure Browser

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of WorkSpaces Secure Browser actions, see [Actions defined by Amazon WorkSpaces Secure Browser](../../../service-authorization/latest/reference/list_amazonworkspacesweb.md#amazonworkspacesweb-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonworkspacesweb.md#amazonworkspacesweb-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in WorkSpaces Secure Browser use the following prefix before the action:

```
workspaces-web
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "workspaces-web:`action1`",
      "workspaces-web:`action2`"
         ]
```

To view examples of WorkSpaces Secure Browser identity-based policies, see [Identity-based policy
examples for Amazon WorkSpaces Secure Browser](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
