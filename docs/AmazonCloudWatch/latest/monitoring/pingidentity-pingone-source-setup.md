# Source configuration for PingIdentity PingOne

## Integrating with PingIdentity PingOne

PingOne is Ping Identity's cloud-based identity-as-a-service (IDaaS) platform that provides identity and access management capabilities. CloudWatch Pipeline uses the PingOne Audit Logs API to retrieve information about authentication events, user activities, policy decisions, and administrative changes across your PingOne environment. The Audit Logs API enables access to event data through REST endpoints, allowing retrieval of security and access logs from your PingOne organization.

## Authenticating with PingIdentity PingOne

To read the logs, the pipeline needs to authenticate with your PingOne environment. For PingOne, authentication is performed using OAuth2.

**Configure OAuth2 authentication for PingOne**

- Log in to the PingOne Console and navigate to Applications → Applications. Create a new application of type Worker. Note the Client ID and Environment ID.
- Generate a new Client Secret from the Configuration tab. Copy the secret immediately.
- In AWS Secrets Manager, create a secret and store the Client ID under key `client_id` and the client secret under key `client_secret`.
- Assign Environment Admin and Application Owner roles to the application.
- Identify your PingOne Region (NA, EU, AP, AU, CA, SG).
- Note the Environment ID from Settings → Environment → Properties.

## Configuring the CloudWatch Pipeline

To configure the pipeline to read logs, choose PingOne as the data source. Fill in the required information like Environment ID. Optionally, specify the Region (defaults to NA) and the Range duration format (for example, PT21H for the last 21 hours). The default range is 0 hours, and the maximum is 90 days. After you create and activate the pipeline, audit log data from PingOne will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and PingOne events that map to Account Change (3001), Authentication (3002), and Entity Management (3004).

**Account Change** contains the following events:

- USER.CREATED
- USER.INVITED
- USER.REINVITED
- USER.INVITE\_ACCEPTED
- PASSWORD.FORCE\_CHANGE
- PASSWORD.RECOVERY
- PASSWORD.RESET
- USER.INVITE\_REVOKED
- USER.DELETED
- USER.LOCKED
- MFA\_SETTINGS.UPDATED
- PASSWORD.UNLOCKED
- USER.UNLOCKED

**Authentication** contains the following events:

- AUTHENTICATION.CREATED
- RADIUS\_SESSION.CREATED
- SESSION.CREATED
- SESSION.UPDATED
- SESSION.DELETED
- USER.SLO\_FAILURE
- USER.SLO\_PARTIAL\_LOGOUT
- USER.SLO\_REQUESTED
- USER.SLO\_SUCCESS
- USER.KERBEROS\_FAILED
- USER.KERBEROS\_SUCCEEDED
- DEVICE.ACTIVATION\_OTP\_FAILED
- DEVICE.ACTIVATION\_OTP\_INVALID
- DEVICE\_PAYLOAD.CHECK\_INVALID
- DEVICE\_PAYLOAD.CHECK\_SUCCESS
- OTP.CHECK\_FAILED
- OTP.CHECK\_INVALID
- OTP.CHECK\_SUCCESS
- PASSWORD.CHECK\_FAILED
- PASSWORD.CHECK\_SUCCEEDED

**Entity Management** contains the following events:

- ACTION.CREATED
- AGREEMENT.CREATED
- AGREEMENT\_LANGUAGE.CREATED
- AGREEMENT\_LANGUAGE\_REVISION.CREATED
- APPLICATION.CREATED
- AUTHORIZE\_POLICY.CREATED
- CERTIFICATE.CREATED
- DEVICE.CREATED
- DEVICE\_AUTHENTICATION\_POLICY.CREATED
- FIDO\_POLICY.CREATED
- FLOW.CREATED
- FLOW\_DEFINITION.CREATED
- FLOW\_EXECUTION.CREATED
- GROUP.CREATED
- IDENTITY\_PROVIDER.CREATED
- IDP\_ATTRIBUTE.CREATED
- INSTANT\_MESSAGING\_DELIVERY\_SETTINGS.CREATED
- KEY.CREATED
- LICENSE.CREATED
- NOTIFICATION.CREATED
- NOTIFICATION\_POLICY.CREATED
- ORGANIZATION.CREATED
- POLICY.CREATED
- RISK\_POLICY\_SET.CREATED
- SAML\_ATTRIBUTE.CREATED
- SCHEMA\_ATTRIBUTE.CREATED
- SIGN\_ON\_POLICY\_ASSIGNMENT.CREATED
- VERIFY\_POLICY.CREATED
- CERTIFICATE.READ
- KEY.READ
- SECRET.READ
- ACTION.UPDATED
- ADMIN\_CONFIGURATION.UPDATED
- AGREEMENT.UPDATED
- AGREEMENT\_LANGUAGE.UPDATED
- AGREEMENT\_LANGUAGE\_REVISION.UPDATED
- APPLICATION.UPDATED
- AUTHORIZE\_POLICY.UPDATED
- CERTIFICATE.UPDATED
- DEVICE.NICKNAME\_UPDATED
- DEVICE.UPDATED
- DEVICE\_AUTHENTICATION\_POLICY.UPDATED
- FIDO\_POLICY.UPDATED
- FLOW.UPDATED
- FLOW\_DEFINITION.UPDATED
- FLOW\_EXECUTION.UPDATED
- GROUP.UPDATED
- IDENTITY\_PROVIDER.UPDATED
- IDP\_ATTRIBUTE.UPDATED
- INSTANT\_MESSAGING\_DELIVERY\_SETTINGS.UPDATED
- KEY.UPDATED
- LICENSE.UPDATED
- NOTIFICATION.UPDATED
- NOTIFICATION\_POLICY.UPDATED
- NOTIFICATIONS\_SETTINGS.UPDATED
- ORGANIZATION.UPDATED
- POLICY.UPDATED
- RISK\_POLICY\_SET.ORDER\_UPDATED
- RISK\_POLICY\_SET.UPDATED
- SAML\_ATTRIBUTE.UPDATED
- SCHEMA\_ATTRIBUTE.UPDATED
- SECRET.UPDATED
- SETTINGS.UPDATED
- SIGN\_ON\_POLICY\_ASSIGNMENT.UPDATED
- USER.QUOTA\_RESET
- USER.UPDATED
- VERIFY\_POLICY.UPDATED
- ACTION.DELETED
- AGREEMENT.DELETED
- AGREEMENT\_LANGUAGE.DELETED
- AGREEMENT\_LANGUAGE\_REVISION.DELETED
- APPLICATION.DELETED
- AUTHORIZE\_POLICY.DELETED
- CERTIFICATE.DELETED
- DEVICE.DELETED
- DEVICE\_AUTHENTICATION\_POLICY.DELETED
- FIDO\_POLICY.DELETED
- FLOW.DELETED
- FLOW\_DEFINITION.DELETED
- GROUP.DELETED
- IDENTITY\_PROVIDER.DELETED
- IDP\_ATTRIBUTE.DELETED
- INSTANT\_MESSAGING\_DELIVERY\_SETTINGS.DELETED
- KEY.DELETED
- LICENSE.DELETED
- NOTIFICATION\_POLICY.DELETED
- ORGANIZATION.DELETED
- POLICY.DELETED
- RISK\_POLICY\_SET.DELETED
- SAML\_ATTRIBUTE.DELETED
- SCHEMA\_ATTRIBUTE.DELETED
- SIGN\_ON\_POLICY\_ASSIGNMENT.DELETED
- VERIFY\_POLICY.DELETED
- DEVICE.UNBLOCKED
- DEVICE.BLOCKED
- NOTIFICATION.REJECTED
- DEVICE.ACTIVATED
- DEVICE.LOCKED
- DEVICE.UNLOCKED
- ROLE.CREATED
- ROLE.UPDATED
- ROLE.DELETED

[Show moreShow less](# "#")
