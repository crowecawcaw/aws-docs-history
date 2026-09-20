

# Applying resilience policies across accounts
<a name="next-gen-org-policies"></a>

A management account or delegated administrator can apply resilience policies across member accounts by associating a policy with a system and then associating services in member accounts to that system. The system-level policy is applied to all associated services.

1. Create a resilience policy in the management account or DA account.

1. Create a system and associate the policy with it.

1. Associate services from member accounts to the system.

The system-level policy applies to all services associated with that system, regardless of which member account owns the service.

You can also share a policy directly with your organization instead of applying it through a system. A shared policy is visible in every member account, and service owners choose whether to apply it to their services. Share a policy directly when service teams own the decision to adopt it. Associate the policy with a system when you want it applied to every associated service, regardless of which account owns the service. For more information, see [Sharing a policy across your organization](next-gen-policy-sharing.md).