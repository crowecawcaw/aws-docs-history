# Policy Actions

**Policy
actions for AWS Security Incident Response**

Support policy actions: Yes

Administrators can use AWS JSON policies to specify who has
access to what. That is, which
**principal** can perform
**actions** on what
**resources**, and under what
**conditions**.

The Action element of a JSON policy describes the actions that
you can use to allow or deny access in a policy. Policy actions
usually have the same name as the associated AWS API operation.
There are some exceptions, such as _permission-only
actions_ that don't have a matching API operation.
There are also some operations that require multiple actions in
a policy. These additional actions are called
_dependent actions_.

Include actions in a policy to grant permissions to perform the
associated operation.

To see a list of AWS Security Incident Response actions, see
Actions defined by AWS Security Incident Response in the
_Service Authorization Reference_.

Policy actions in AWS Security Incident Response use the
following prefix before the action:

AWS Security Incident Response -identity

To specify multiple actions in a single statement, separate them
with commas.

"Action": [
"AWS Security Incident Response -identity:action1",
"AWS Security Incident Response -identity:action2"
]

**Policy
resources for Amazon AWS Security Incident
Response**

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The Resource JSON policy element specifies the object or objects
to which the action applies. Statements must include either a
Resource or a NotResource element. As a best practice, specify a
resource using its
[Amazon
Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). You can do this for actions that
support a specific resource type, known as
_resource-level permissions_.

For actions that don't support resource-level permissions, such
as listing operations, use a wildcard (\*) to indicate that the
statement applies to all resources.

"Resource": "\*"
