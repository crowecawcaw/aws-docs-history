

# Amazon Verified Permissions policy templates and template-linked policies
<a name="policy-templates"></a>

In Verified Permissions, policy templates are policies with placeholders for the `principal`, `resource`, or both. Policy templates alone can't be used to handle authorization requests. To handle authorization requests, a *template-linked policy* must be created based on a policy template. Policy templates allow a policy to be defined once and then used with multiple principals and resources. Updates to the policy template are reflected across all policies that use the template. For more information, see [Cedar policy templates](https://docs.cedarpolicy.com/policies/templates.html) in the Cedar policy language Reference Guide.

You can optionally assign a policy template name to a policy template. Policy template names must be unique within the policy store and prefixed with `name/`. You can use a policy template name in place of the policy template ID in control plane operations that accept a `policyTemplateId` parameter. Only `GetPolicyTemplate` and `ListPolicyTemplates` return the name in the output. The following example uses a policy template name to retrieve a policy template with `GetPolicyTemplate`.

```
$ aws verifiedpermissions get-policy-template \
    --policy-template-id name/example-policy-template \
    --policy-store-id PSEXAMPLEabcdefg111111
```

For example, the following policy template provides `Read`, `Edit`, and `Comment` permissions for the principal and resource that use the policy template.

```
permit(
  principal == ?principal,
  action in [Action::"Read", Action::"Edit", Action::"Comment"],
  resource == ?resource
);
```

If you were to create a policy named `Editor` based on this template, when a principal is designated as an editor for a specific resource, your application would create a policy that provides permissions for the principal to read, edit, and comment on the resource.

Unlike static policies, template-linked policies are dynamic. Take the previous example, if you were to remove the `Comment` action from the policy template, any policy linked to, or based on, that template would be updated accordingly and the principals specified in the policies would no longer be able to comment on the corresponding resources.

For more template-linked policy examples, see [Amazon Verified Permissions example template-linked policies](policy-templates-example-policies.md).