

# Migrating from the classic hosted UI to managed login
<a name="migrate-classic-hosted-ui-to-managed-login"></a>

If your user pool currently uses the classic hosted UI, you can migrate it to managed login. Managed login and the classic hosted UI are the two branding versions. You set the branding version on the user pool domain, and your choice applies to all app clients that use that domain, so migrating switches every app client on the domain at the same time. Managed login adds a visual branding editor, passkey sign-in, and additional authentication features. The classic hosted UI uses file-based branding and is available in all feature plans. For a feature-by-feature comparison, see [User pool managed login](cognito-user-pools-managed-login.md).

**Important**  
Managed login and its branding editor require the Essentials or Plus feature plan. The classic hosted UI is available in all plans, including Lite. Confirm your feature plan before you migrate. See [User pool managed login](cognito-user-pools-managed-login.md).

At a high level, moving an existing user pool from the classic hosted UI to managed login involves the following steps. Review each step against your current configuration before you switch:

1. Confirm your user pool is on a feature plan that supports managed login. See [User pool managed login](cognito-user-pools-managed-login.md).

1. Set the branding version on your user pool domain to managed login. The branding version is a domain setting, so it applies to all app clients that use that domain.

1. Set up your branding in the visual branding editor. Managed login uses a different branding model from the classic hosted UI's file-based CSS and logo customization, so review your existing branding against the branding editor as part of the switch. See [Apply branding to managed login pages](managed-login-branding.md).

1. Test the sign-in, sign-up, multi-factor authentication (MFA), and password-reset flows on the managed login pages before you direct production traffic to them.

**Note**  
This page summarizes the migration at a conceptual level. The detailed setup and branding procedures it refers to are the authoritative source for each step.