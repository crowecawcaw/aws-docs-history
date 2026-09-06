

# Registering a delegated administrator for S3 Storage Lens
<a name="storage_lens_with_organizations_registering_delegated_admins"></a>

You can create organization-level dashboards by using your organization’s management account or delegated administrator accounts. Delegated administrator accounts allow other accounts besides your management account to create organization-level dashboards. Only the management account of an organization can register and deregister other accounts as delegated administrators for the organization.

After enabling trusted access, you can register delegate administrator access to accounts in your organization by using the AWS Organizations REST API, AWS CLI, or SDKs from the [management account](https://docs.aws.amazon.com/managedservices/latest/userguide/management-account.html). (For more information, see [RegisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html) in the *AWS Organizations API Reference*.) When an account is registered as a delegated administrator, the account receives authorization to access all read-only AWS Organizations API operations. This provides visibility to the members and structures of your organization so that they can create S3 Storage Lens dashboards on your behalf.

**Note**  
Before you can designate a delegated administrator by using the AWS Organizations REST API, AWS CLI, or SDKs, you must call the [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html) operation.