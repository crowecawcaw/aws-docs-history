

# Emergency preparation tasks
<a name="emergency-access-prepare-configuration"></a>

To prepare your emergency access configuration, we recommend that you perform the following tasks before an emergency occurs.

1. Set up a direct IAM federation application in your IdP. If you are using Okta or other external IdPs as your identity source, see [One-time setup of a direct IAM federation application in Okta](emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.md). If you are using Active Directory as your identity source, see [One-time setup of a direct IAM federation application with ADFS](emergency-access-one-time-setup-direct-IAM-federation-application-in-adfs.md).

1. Create an IdP connection in the emergency access account that can be accessed during the event.

1. Create emergency access roles in the emergency access accounts as described in the mapping table above.

1. Create temporary operations roles with trust and permission policies in each of the workload accounts.

1. Create temporary operations groups in your IdP. The group names will depend on the names of the temporary operations roles.

1. Test direct IAM federation.

1. Disable the IdP federation application in your IdP to prevent regular usage.