# Emergency preparation tasks

To prepare your emergency access configuration, we recommend that you perform the
following tasks before an emergency occurs.

1. Set up a direct IAM federation application in your IdP. For more information, see [One-time setup of a direct IAM federation application in Okta](emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.md "emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.md").
2. Create an IdP connection in the emergency access account that can be accessed during the event.
3. Create emergency access roles in the emergency access accounts as described in the mapping
   table above.
4. Create temporary operations roles with trust and permission policies in each of the workload accounts.
5. Create temporary operations groups in your IdP. The group names will depend on the names of
   the temporary operations roles.
6. Test direct IAM federation.
7. Disable the IdP federation application in your IdP to prevent regular usage.
