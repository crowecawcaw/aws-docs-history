

# Policy size per resource
<a name="policy-size-per-resource"></a>

Verified Permissions limits the total size of all policies that reference the same resource. This limit is the *Policy size per resource* quota, and its default value is 200,000 bytes. When you call `CreatePolicy` or `UpdatePolicy`, Verified Permissions calculates the new total for the referenced resource. If the new total exceeds the quota, the request fails with a `ServiceQuotaExceededException`.

Policies that don't specify a resource apply to all resources. These policies share a separate total for the `"unspecified"` resource, which is limited to the same quota value.

For the list of all Verified Permissions quotas, see [Quotas for Amazon Verified Permissions](quotas.md).

**Topics**
+ [How policy sizes are calculated](#policy-size-per-resource-calculation)
+ [Staying within the quota](#policy-size-per-resource-manage)
+ [Template-linked policy size example](#policy-size-per-resource-example)

## How policy sizes are calculated
<a name="policy-size-per-resource-calculation"></a>

Each policy contributes to the total for a resource as follows:
+ **Static policies** – A static policy contributes its full size. This is the same value that is measured against the *Policy size* quota.
+ **Template-linked policies** – A template-linked policy contributes the combined length of the principal and resource used to instantiate it. If you don't specify the principal or resource, its length is counted as 0. The size of the policy template body itself doesn't count toward this quota.

Each policy also adds a fixed overhead of up to a few hundred bytes to the total. Template-linked policies add more overhead than static policies.

## Staying within the quota
<a name="policy-size-per-resource-manage"></a>

If your application approaches the *Policy size per resource* quota, consider the following strategies:
+ **Use the appropriate policy type.** If many policies grant similar permissions on the same resource, policy templates might reduce your policy store's storage consumption. Each template-linked policy stores only its principal and resource. The policy template stores the shared statement once, but each linked policy also carries a fixed storage overhead. Templates only pay for themselves when the shared statement is large enough to offset that overhead, roughly 200 bytes or more. Below that threshold, individual static policies consume less space. For more information, see [Amazon Verified Permissions policy templates and template-linked policies](policy-templates.md).
+ **Specify principals and resources in the policy scope.** Policies that don't specify a resource share a single total for the `"unspecified"` resource across the policy store. Scoping each policy to a specific resource spreads your policies across separate totals, one for each resource.
+ **Group your principals and resources.** Instead of writing a policy for each principal, write a policy for a group and add principals to the group. Grouping resources into containers can similarly reduce the number of policies that reference a single resource.
+ **Request a quota increase.** You can request an increase to this quota if your policy design meets certain constraints. To qualify, your policies must specify the principal or resource in the policy scope. An increase might also reduce the number of hierarchy parents that your principals and resources can have. Even with an increased quota, a 200,000-byte sub-limit still applies to policies that reference the same principal and the same resource. You cannot request an increase to this sub-limit.

## Template-linked policy size example
<a name="policy-size-per-resource-example"></a>

To find how template-linked policies contribute to the *Policy size per resource* quota, add the length of the principal and the length of the resource. If you don't specify a resource, Verified Permissions counts its size toward the `"unspecified"` resource total.

Review the following template:

```
permit (
  principal in ?principal,
  action in
    [MyApplication::Action::"ContentManagement",
     MyApplication::Action::"AccountAdministration",
     MyApplication::Action::"BillingOperations"],
  resource in ?resource
)
when {
  resource has authorizedTenantIds &&
  principal has tenantId &&
  resource.authorizedTenantIds.contains(principal.tenantId)
};
```

Create the following policies from that template:

```
TemplateLinkedPolicy {
  policyId: "policy1",
  templateId: "template1",
  principal: User::"alice",
  resource: Photo::"car.jpg"
}

TemplateLinkedPolicy {
  policyId: "policy2",
  templateId: "template1",
  principal: User::"bob",
  resource: Photo::"boat.jpg"
}

TemplateLinkedPolicy {
  policyId: "policy3",
  templateId: "template1",
  principal: User::"jane",
  resource: Photo::"car.jpg"
}

TemplateLinkedPolicy {
  policyId: "policy4",
  templateId: "template1",
  principal: User::"jane",
  resource
}
```

Calculate the size of those policies by counting the bytes in the `principal` and `resource` for each one. Verified Permissions measures size in UTF-8 bytes. Characters in the printable ASCII range count as 1 byte each, but other characters can use more. The following examples use only ASCII characters, so each character counts as 1 byte. These calculations exclude the fixed overhead. Your actual totals will be higher.

The size of `policy1` is the length of the principal `User::"alice"` (13) plus the length of the resource `Photo::"car.jpg"` (16). The total is 13 \+ 16 = 29 bytes.

The size of `policy2` is the length of the principal `User::"bob"` (11) plus the length of the resource `Photo::"boat.jpg"` (17). The total is 11 \+ 17 = 28 bytes.

The size of `policy3` is the length of the principal `User::"jane"` (12) plus the length of the resource `Photo::"car.jpg"` (16). The total is 12 \+ 16 = 28 bytes.

The size of `policy4` is the length of the principal `User::"jane"` (12) plus the length of the resource (0). The total is 12 \+ 0 = 12 bytes.

Because `policy2` is the only policy that references the resource `Photo::"boat.jpg"`, the total resource size is 28 bytes.

Because `policy1` and `policy3` both reference the resource `Photo::"car.jpg"`, the total resource size is 29 \+ 28 = 57 bytes.

Because `policy4` is the only policy that references the `"unspecified"` resource, the total resource size is 12 bytes.