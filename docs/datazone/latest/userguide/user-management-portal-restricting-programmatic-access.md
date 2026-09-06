

# Restricting access to Amazon DataZone
<a name="user-management-portal-restricting-programmatic-access"></a>

**Restricting programmatic access to Amazon DataZone** - for IAM users or roles, making programmatic API calls, access can be restricted via IAM policies. If you want to revoke any already issued short term credentials for roles, you can use the [IAM revoke session mechanism](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html) on the role or on the [Service Control Policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

**Restricting login access to the Amazon DataZone data portal ** - to restrict login access to the Amazon DataZone data portal, for IAM users or roles, IAM policies can restrict access to the `datazone:GetUserPortalLoginUrl` action. For SSO users and groups, restrict access to the Amazon DataZone data portal by setting the Amazon DataZone user profile status to **Deactivated**. If your domain is configured with implicit assignment and the user has not previously used Amazon DataZone, you will need to remove the user from the identity provider.