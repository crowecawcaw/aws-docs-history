# Source configuration for Microsoft Entra ID

## Integrating with Microsoft Entra ID

Microsoft Entra ID (formerly Azure Active Directory) is Microsoft's cloud-based identity and access management service that helps organizations manage user identities and secure access to resources. CloudWatch Pipeline uses the Microsoft Graph API to retrieve comprehensive identity and security information from Microsoft Entra ID audit logs. The Microsoft Graph API provides access to three primary log types: Directory Audit Logs (tracking directory-level changes and administrative actions), Sign-In Logs (capturing user authentication events and activities), and Provisioning Logs (monitoring user and group provisioning operations).

## Authenticating with Microsoft Entra ID

To retrieve the Audit Logs EntraID, pipelines needs to authenticate with your account. The plugin supports OAuth2 Authentication. Follow the instructions in Microsoft Graph APIs and should have the Microsoft Entra ID P1 or P2 license.

- Register an application in Azure with Supported account types, Accounts in this organizational directory only (Single tenant). After registration is complete, note down the Application (client) ID and Directory (tenant) ID.
- Generate a new key for your application. Key is also known as client secret, which are used when exchanging an authorization code for an access token.
- In the AWS Secrets Manager, create a secret and store the Application (client) ID under the key `client_id` and the client secret under the key `client_secret`
- Specify the permissions your application requires to access the Microsoft Graph APIs. The permissions you need are:
  - AuditLog.Read.All: Required to read audit logs, sign-in logs, and provisioning logs
  - Directory.Read.All: Required to read directory data

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read Audit Logs from Microsoft EntraID, choose Microsoft EntraID as the data source. Fill in the required information like Tenant Id using Directory (tenant) ID. Once you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and Entra ID events that map to Authentication (3002), Account Change (3001), User Access Management (3005), and Entity Management (3004).

**Authentication** contains the following events with type in brackets:

- Invalid Username or Password (Sign-in)
- User Strong Auth ClientAuthN Required Interrupt (Sign-in)
- Pass Through User Mfa Error (Sign-in)
- Authentication Failed During Strong Auth (Sign-in)

**Account Change** contains the following events with type in brackets:

- Add user (Audit)
- Update user (Audit)
- Delete user (Audit)
- Hard delete user (Audit)
- Reset password (Audit)
- User changed default security info (Audit)
- Enable Strong Authentication (Audit)
- Disable Strong Authentication (Audit)

**User Access Management** contains the following events with type in brackets:

- Add eligible member to role (Audit)
- Remove eligible member from role (Audit)
- Add eligible member to role in PIM completed (Audit)
- Remove eligible member from role in PIM completed (Audit)
- Add member to role (Audit)
- Remove member from role (Audit)
- Remove permanent direct role assignment (Audit)
- Add permanent direct role assignment (Audit)
- Triggered PIM alert (Audit)
- Add delegated permission grant (Audit)
- Remove delegated permission grant (Audit)

**Entity Management** contains the following events with type in brackets:

- Create (Provisioning)
- Update (Provisioning)
- Add app role assignment to service principal (Audit)
- Remove app role assignment to service principal (Audit)
- Add service principal credentials (Audit)
- Remove service principal credentials (Audit)
- Update service principal (Audit)
- Add service principal (Audit)
- Hard delete service principal (Audit)
- Remove service principal (Audit)
- Consent to application (Audit)
- Add application (Audit)
- Add owner to application (Audit)
- Hard Delete application (Audit)
- Delete application (Audit)
- Update application (Audit)
- Update application – Certificates and secrets management (Audit)
- Add device (Audit)
- Update device (Audit)
- Delete device (Audit)
- Hard delete device (Audit)

[Show moreShow less](# "#")
