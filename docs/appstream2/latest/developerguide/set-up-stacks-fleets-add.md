# Provide Access to Users in Amazon AppStream 2.0

After you create a stack with an associated fleet, you can provide access to users
through the AppStream 2.0 user pool, SAML 2.0 [single sign-on (SSO)], or the AppStream 2.0 API. For
more information, see [User Pool Administration in Amazon AppStream 2.0](user-pool-admin.md "user-pool-admin.md")
and [Amazon AppStream 2.0 Integration with SAML 2.0](external-identity-providers.md "external-identity-providers.md").

###### Note

Users in the AppStream 2.0 user pool can't be assigned to stacks with fleets that are
joined to an Active Directory domain.

After you provide your users with access to AppStream 2.0, they can start AppStream 2.0 streaming
sessions by using a web browser or by using the AppStream 2.0 client application for a
supported device. If you provide access to users through the AppStream 2.0 user pool, they must
use a web browser for streaming sessions. If you use SAML 2.0 or the AppStream 2.0 API, you can
make the AppStream 2.0 client available to them. The AppStream 2.0 client is a native application that
is designed for users who require additional functionality during their AppStream 2.0 streaming
sessions. For more information, see [Provide Access Through the AppStream 2.0 Client](client-application.md "client-application.md").
