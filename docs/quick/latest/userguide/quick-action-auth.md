# Authentication methods

Amazon Quick supports multiple authentication methods, each designed for specific use cases and security requirements.

## Managed authentication (3LO)

Three-Legged OAuth (3LO) is the recommended authentication method for personal access to third-party services.

**Key features of 3LO:**

- No initial configuration required.
- User-specific authentication.
- Secure credential storage.
- Automatic token refresh.
- 90-day refresh token lifecycle.

**3LO setup process:**

1. Select connector.
2. Choose managed authentication.
3. Complete service provider login.
4. Grant requested permissions.
5. Confirm connection.

## Custom user-based authentication

For scenarios that require specific organizational control or custom configuration.

**Required information:**

- Client ID.
- Client Secret.
- Domain URL.
- Authorization URL.
- Token URL.
- Redirect URL.

**Configuration steps:**

1. Obtain credentials from service provider.
2. Configure authentication settings.
3. Validate connection.
4. Test access permissions.

When configuring user-based authentication in the Amazon Quick console, obtain the proper credentials from your service provider and configure your authentication settings. Then validate the connection and test your access permissions.

## API key authentication

Used primarily for automated workflows and system-level access.

**Key features:**

- Simple token-based authentication.
- Single credential management.
- Service-level permissions.
- Suitable for automated processes.

**Setup requirements:**

When setting up API Key authentication, ensure that you have the following:

- Valid API key from service.
- Appropriate service permissions.
- Secret storage configuration.

## Service-to-service authentication

For automated workflows that require complex authentication.

**Configuration requirements:**

- Client ID.
- Client Secret.
- Domain URL.
- Token URL.
- Service-specific parameters.
