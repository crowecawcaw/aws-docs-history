

# Troubleshooting License Manager
<a name="troubleshooting"></a>

The following information can help you troubleshoot issues when using AWS License Manager. Before you start, confirm that your License Manager setup meets the requirements stated in [Settings in License Manager](settings.md).

## Management account cannot disassociate resources from a self-managed license
<a name="issue3"></a>

If a member account of an Organization deletes the `AWSServiceRoleForAWSLicenseManagerMemberAccountRole` Service Linked Role (SLR) in its account, and there are member-owned resources associated with a self-managed license, the management account is prevented from disassociating licenses from those member-account resources. This means that the member account resources will continue to consume licenses from the management account pool. To allow the management account to disassociate resources, restore the SLR.

This behavior accounts for cases when a customer prefers not to allow the management account to perform some actions affecting member-account resources.

## Systems Manager Inventory is out of date
<a name="stale-inventory"></a>

Systems Manager stores data in its Inventory data for 30 days. During this period, License Manager counts a managed instance as active even if it is not pingable. After inventory data has been purged from Systems Manager, License Manager marks the instance as inactive and updates local inventory data. To keep managed instance counts accurate, we recommend manually deregistering instances in Systems Manager so that License Manager can run cleanup operations.

## Apparent persistence of a de-registered AMI
<a name="deregistered_ami"></a>

License Manager purges stale associations between resources and self-managed licenses once every few hours. If an AMI associated with a self-managed license is deregistered through Amazon EC2, The AMI may briefly continue to appear in the License Manager resource inventory before being purged.

## New child account instances are slow to appear in resource inventory
<a name="inventory_delay_1"></a>

When cross-account support is enabled, it can take up to 24 hours for newly added child account instances to appear in the management account resource inventory.

## After enabling cross-account mode, child account instances are slow to appear
<a name="inventory_delay_2"></a>

When you enable cross-account mode in License Manager, instances in child accounts may take anywhere from a few minutes to a few hours to appear in the resource inventory. The time depends on the number of child accounts and the number of instances in each child account. 

## Cross-account discovery cannot be disabled
<a name="cross_account-permanent"></a>

After an account is configured for cross-account discovery, it is impossible to revert to single-account discovery.

## Child account user cannot associate shared self-managed license with an instance
<a name="associating_child_account"></a>

When this occurs and cross-account discovery has been enabled, check for the following:
+ The child account has been removed from the organization.
+ The child account has been removed from the resource share created in the management account.
+ The self-managed license has been removed from the resource share.

## Linking AWS Organizations accounts fails
<a name="organizations_blocked"></a>

If the **Settings** page reports this error, it means that an account is not a member of an organization for the following reasons:
+ A child account was removed from the organization.
+ A customer turned off access to License Manager from organization console of the management account.