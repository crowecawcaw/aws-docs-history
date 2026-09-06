

# Applying resilience policies across accounts
<a name="next-gen-org-policies"></a>

A management account or delegated administrator can apply resilience policies across member accounts by associating a policy with a system and then associating services in member accounts to that system. The system-level policy is applied to all associated services.

1. Create a resilience policy in the management account or DA account.

1. Create a system and associate the policy with it.

1. Associate services from member accounts to the system.

The system-level policy applies to all services associated with that system, regardless of which member account owns the service.