# Amazon Verified Permissions policy templates and template-linked

policies

In Verified Permissions, policy templates are policies with placeholders for the `principal`,
`resource`, or both. Policy templates alone can't be used to handle authorization
requests. To handle authorization requests, a _template-linked policy_
must be created based on a policy template. Policy templates allow a policy to be defined once and then used with
multiple principals and resources. Updates to the policy template are reflected across all policies
that use the template. For more information, see [Cedar policy templates](https://docs.cedarpolicy.com/policies/templates.html "https://docs.cedarpolicy.com/policies/templates.html") in the
Cedar policy language Reference Guide.

For example, the following policy template provides `Read`, `Edit`,
and `Comment` permissions for the principal and resource that use the policy
template.

```
permit(
  principal == ?principal,
  action in [Action::"Read", Action::"Edit", Action::"Comment"],
  resource == ?resource
);
```

If you were to create a policy named `Editor` based on this template, when a
principal is designated as an editor for a specific resource, your application would create
a policy that provides permissions for the principal to read, edit, and comment on the
resource.

Unlike static policies, template-linked policies are dynamic. Take the previous example,
if you were to remove the `Comment` action from the policy template, any policy
linked to, or based on, that template would be updated accordingly and the principals
specified in the policies would no longer be able to comment on the corresponding
resources.

For more template-linked policy examples, see [Amazon Verified Permissions example template-linked policies](policy-templates-example-policies.md "policy-templates-example-policies.md").
