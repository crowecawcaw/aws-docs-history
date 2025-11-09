AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Step 3: Control

session access to managed nodes

You grant or revoke Session Manager access to managed nodes by using AWS Identity and Access Management (IAM)
policies. You can create a policy and attach it to an IAM user or group that
specifies which managed nodes the user or group can connect to. You can also specify
the Session Manager API operations the user or groups can perform on those managed nodes.

To help you get started with IAM permission policies for Session Manager, we've created
sample policies for an end user and an administrator user. You can use these
policies with only minor changes. Or, use them as a guide to create custom IAM
policies. For more information, see [Sample IAM
policies for Session Manager](getting-started-restrict-access-quickstart.md "getting-started-restrict-access-quickstart.md"). For information
about how to create IAM policies and attach them to users or groups, see [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and [Adding and
Removing IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
_IAM User Guide_.

###### About session ID ARN formats

When you create an IAM policy for Session Manager access, you specify a session ID
as part of the Amazon Resource Name (ARN). The session ID includes the user name
as a variable. To help illustrate this, here's the format of a Session Manager ARN and
an example:

```
arn:aws:ssm:`region-id`:`account-id`:session/`session-id`
```

For example:

```
arn:aws:ssm:us-east-2:123456789012:session/JohnDoe-1a2b3c4d5eEXAMPLE
```

For more information about using variables in IAM policies, see [IAM Policy
Elements: Variables](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md").

###### Topics

- [Start a default shell
  session by specifying the default session document in IAM policies](getting-started-default-session-document.md "getting-started-default-session-document.md")
- [Start a session with
  a document by specifying the session documents in IAM policies](getting-started-specify-session-document.md "getting-started-specify-session-document.md")
- [Sample IAM
  policies for Session Manager](getting-started-restrict-access-quickstart.md "getting-started-restrict-access-quickstart.md")
- [Additional sample
  IAM policies for Session Manager](getting-started-restrict-access-examples.md "getting-started-restrict-access-examples.md")
