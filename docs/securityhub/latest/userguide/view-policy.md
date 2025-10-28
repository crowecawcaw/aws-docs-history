# Reviewing the status and details of configuration

policies

The delegated AWS Security Hub CSPM administrator can view configuration policies for an
organization and their details. This includes which accounts and organizational units (OUs) a policy is associated with.

For background information about the benefits of central configuration and how it works, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md "central-configuration-intro.md").

Choose your preferred method, and follow the steps to view your configuration policies.

Security Hub CSPM console

###### To view configuration policies (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region. 2. In the navigation pane, choose
**Settings** and **Configuration**. 3. Choose the **Policies** tab for an overview of your configuration policies. 4. Select a configuration policy, and choose **View details** to see additional details about it, including which accounts and OUs it's associated with.

Security Hub CSPM API
To view a summary list of all your configuration policies, use the [ListConfigurationPolicies](../../1.0/APIReference/API_ListConfigurationPolicies.md "../../1.0/APIReference/API_ListConfigurationPolicies.md") operation of the Security Hub CSPM API. If you
use the AWS CLI, run the [list-configuration-policies](../../../cli/latest/reference/securityhub/list-configuration-policies.md "../../../cli/latest/reference/securityhub/list-configuration-policies.md") command.
The delegated Security Hub CSPM administrator account should invoke the operation in the home Region.

```
`$` `aws securityhub list-configuration-policies \
--max-items `5` \
--starting-token `U2FsdGVkX19nUI2zoh+Pou9YyutlYJHWpn9xnG4hqSOhvw3o2JqjI23QDxdf``
```

To view details about a specific configuration policy, use the [GetConfigurationPolicy](../../1.0/APIReference/API_GetConfigurationPolicy.md "../../1.0/APIReference/API_GetConfigurationPolicy.md") operation. If you use the AWS CLI,
run the [get-configuration-policy](../../../cli/latest/reference/securityhub/get-configuration-policy.md "../../../cli/latest/reference/securityhub/get-configuration-policy.md"). The delegated administrator
account should invoke the operation in the home Region. Provide the Amazon Resource Name (ARN) or ID of
the configuration policy whose details you want to see.

```
`$` `aws securityhub get-configuration-policy \
--identifier "`arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"`
```

To view a summary list of all your configuration policies and their account associations, use the
use the [ListConfigurationPolicyAssociations](../../1.0/APIReference/API_ListConfigurationPolicyAssociations.md "../../1.0/APIReference/API_ListConfigurationPolicyAssociations.md") operation. If you use the AWS CLI, run
the [list-configuration-policy-associations](../../../cli/latest/reference/securityhub/list-configuration-policy-associations.md "../../../cli/latest/reference/securityhub/list-configuration-policy-associations.md") command. The
delegated administrator account should invoke the operation in the home Region. Optionally, you can provide pagination parameters or filter the
results by a specific policy ID, association type, or association status.

```
`$` `aws securityhub list-configuration-policy-associations \
--filters '{"AssociationType": "`APPLIED`"}'`
```

To view associations for a specific account, use the [GetConfigurationPolicyAssociation](../../1.0/APIReference/API_GetConfigurationPolicyAssociation.md "../../1.0/APIReference/API_GetConfigurationPolicyAssociation.md") operation. If you use the AWS CLI,
run the [get-configuration-policy-association](../../../cli/latest/reference/securityhub/get-configuration-policy-association.md "../../../cli/latest/reference/securityhub/get-configuration-policy-association.md") command. The
delegated administrator account should invoke the operation in the home Region. For `target`, provide the account number, OU ID, or root ID.

```
`$` `aws securityhub get-configuration-policy-association \
--target '{"AccountId": "`123456789012`"}'`
```

## Reviewing the association status of a configuration policy

The following central configuration API operations return a field called `AssociationStatus`:

- `BatchGetConfigurationPolicyAssociations`
- `GetConfigurationPolicyAssociation`
- `ListConfigurationPolicyAssociations`
- `StartConfigurationPolicyAssociation`

This field is returned both when the underlying configuration is a configuration policy and when it's self-managed behavior.

The value of `AssociationStatus` tells you whether a policy association is
pending or in a state of success or failure for a specific account. It can take up to 24
hours for the status to change from `PENDING` to `SUCCESS` or
`FAILED`. A status of `SUCCESS` means that all settings
specified in the configuration policy are associated with the account. A status of
`FAILED` means that one or more settings specified in the configuration
policy failed to associate with the account. Despite a `FAILED` status, the account could
be partially configured in accordance with the policy. For example, you might try to
associate an account with a configuration policy that enables Security Hub CSPM, enables AWS Foundational Security Best Practices,
and disables CloudTrail.1. The initial two settings could succeed, but the CloudTrail.1
setting could fail. In this example, the association status is `FAILED` even
though some settings were correctly configured.

The association status of a parent OU or the root depends on the
status of its children. If the association status of all the children is `SUCCESS`, the association status of the parent
is `SUCCESS`. If the association status of one or more children is `FAILED`, the association status of the parent
is `FAILED`.

The value of `AssociationStatus` depends on the association status of the policy in all relevant Regions.
If the association succeeds in the home Region and all linked Regions, the value of
`AssociationStatus` is `SUCCESS`. If the association fails in one or more of these Regions, the value of `AssociationStatus`
is `FAILED`.

The following behavior also impacts the value of `AssociationStatus`:

- If the target is a parent OU or the root, it has an `AssociationStatus` of `SUCCESS` or
  `FAILED` only when all of the children have a `SUCCESS` or `FAILED` status. If the
  association status of a child account or OU changes (for example, when a linked Region is added or removed) after you first associate the parent with a configuration, the change doesn't update the
  association status of the parent unless you invoke the `StartConfigurationPolicyAssociation` API again.
- If the target is an account, it has an `AssociationStatus` of `SUCCESS`
  or `FAILED` only if the association has a result of
  `SUCCESS` or `FAILED` in the home Region and all
  linked Regions. If the association status of a target account changes (for
  example, when a linked Region is added or removed) after you first associate it
  with a configuration, its association status is updated. However, the change
  doesn't update the association status of the parent unless you invoke the
  `StartConfigurationPolicyAssociation` API again.

If you add a new linked Region, Security Hub CSPM replicates your existing associations that are in a `PENDING`,
`SUCCESS`, or `FAILED` state in the new Region.

Even when the association status is `SUCCESS`, the enablement status of a standard that is part of the
policy can transition into an incomplete state. In that case, Security Hub CSPM can't generate findings for the standard's controls. For more
information, see [Checking the status of a standard](enable-standards.md#standard-subscription-status "enable-standards.md#standard-subscription-status").

## Troubleshooting association failure

In AWS Security Hub CSPM, a configuration policy association might fail for the following common reasons.

- **Organizations management account isn't a member** – If you want to
  associate a configuration policy with the Organizations management account, that account
  must already have AWS Security Hub CSPM enabled. This makes the management account a member account in the organization.
- **AWS Config isn't enabled or properly configured** – To enable standards in a configuration policy, AWS Config must be enabled and configured
  to record relevant resources.
- **Must associate from delegated administrator account** – You can only associate a policy with target accounts and OUs when you're signed in to
  the delegated Security Hub CSPM administrator account.
- **Must associate from home Region** – You can only associate a policy with target accounts and OUs when you're signed in to
  your home Region.
- **Opt-in Region not enabled** – Policy association fails for a member
  account or OU in a linked Region if it's an opt-in Region that the delegated administrator hasn't enabled. You can retry after enabling
  the Region from the delegated administrator account.
- **Member account suspended** – Policy association fails if you try to
  associate a policy with a suspended member account.
