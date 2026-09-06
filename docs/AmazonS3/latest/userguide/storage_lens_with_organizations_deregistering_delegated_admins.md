

# Deregistering a delegated administrator for S3 Storage Lens
<a name="storage_lens_with_organizations_deregistering_delegated_admins"></a>

After enabling trusted access, you can also deregister delegate administrator access to accounts in your organization. Delegated administrator accounts allow other accounts besides your [management account](https://docs.aws.amazon.com/managedservices/latest/userguide/management-account.html) to create organization-level dashboards. Only the management account of an organization can deregister accounts as delegated administrators for the organization.

You can deregister a delegated administrator by using the AWS Organizations AWS Management Console, REST API, AWS CLI, or AWS SDKS from the management account. For more information, see [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html) in the *AWS Organizations API Reference*.

When an account is deregistered as a delegated administrator, the account loses access to the following:
+ All read-only AWS Organizations API operations that provide visibility to the members and structures of your organization.
+ All organization-level dashboards created by the delegated administrator. Deregistering a delegated administrator also automatically stops all organization-level dashboards created by that delegated administrator from aggregating new storage metrics.
**Note**  
The deregistered delegated administrator will still be able to see the historic data for the disabled dashboards that they created if data is still available for querying.