

# Security considerations and best practices

Keep the following security considerations in mind when you configure WebAuthn redirection.
+ The user's authenticator creates and stores the private key for each credential, and the key never leaves the local device. The streaming instance receives only the signed response.
+ WebAuthn credentials are bound to the website's origin (relying party ID). Redirection does not change which sites a credential works for.
+ On Windows fleets, keep the process compatibility list as short as your applications require. Each listed process can initiate WebAuthn requests to the user's authenticator.
+ On Linux fleets, a managed browser policy installs the Amazon DCV WebAuthn redirection extension. Users cannot disable it while the feature is enabled on the stack.
+ WebAuthn redirection requires the user to be physically present at the local device to touch the authenticator. It does not support unattended or scripted authentication.

**Best practices**
+ Start with the default process compatibility list and add processes only when a specific application needs them.
+ Test with pilot users on each image and client platform you support before enabling the feature on production stacks.
+ If your identity provider enforces FIDO2 for sign-in, confirm that users connect from a supported Windows or macOS client. The web client cannot complete WebAuthn ceremonies.
+ Review the process compatibility list when you update images, because you might need to add newly installed applications.