

# Policy actions for WorkSpaces Secure Browser
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.



To see a list of WorkSpaces Secure Browser actions, see [Actions defined by Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesweb.html#amazonworkspacesweb-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in WorkSpaces Secure Browser use the following prefix before the action:

```
workspaces-web
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "workspaces-web:{{action1}}",
      "workspaces-web:{{action2}}"
         ]
```





To view examples of WorkSpaces Secure Browser identity-based policies, see [Identity-based policy examples for Amazon WorkSpaces Secure Browser](security_iam_id-based-policy-examples.md).