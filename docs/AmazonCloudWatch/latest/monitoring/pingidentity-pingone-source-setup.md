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

To configure the pipeline to read logs, choose PingOne as the data source. Fill in the required information like Environment ID. Optionally, specify the Region (defaults to NA) and the Range duration format (for example, PT21H for the last 21 hours). The default range is 0 hours, and the maximum is 90 days. Once you create and activate the pipeline, audit log data from PingOne will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and PingOne events that map to Account Change (3001), Authentication (3002), and Entity Management (3004).

**Account Change** contains the following events:

- USER.CREATED
- USER.INVITED
- USER.REINVITED
- USER.INVITE_ACCEPTED
- PASSWORD.FORCE_CHANGE
- PASSWORD.RECOVERY
- PASSWORD.RESET
- USER.INVITE_REVOKED
- USER.DELETED
- USER.LOCKED
- MFA_SETTINGS.UPDATED
- PASSWORD.UNLOCKED
- USER.UNLOCKED

**Authentication** contains the following events:

- AUTHENTICATION.CREATED
- RADIUS_SESSION.CREATED
- SESSION.CREATED
- SESSION.UPDATED
- SESSION.DELETED
- USER.SLO_FAILURE
- USER.SLO_PARTIAL_LOGOUT
- USER.SLO_REQUESTED
- USER.SLO_SUCCESS
- USER.KERBEROS_FAILED
- USER.KERBEROS_SUCCEEDED
- DEVICE.ACTIVATION_OTP_FAILED
- DEVICE.ACTIVATION_OTP_INVALID
- DEVICE_PAYLOAD.CHECK_INVALID
- DEVICE_PAYLOAD.CHECK_SUCCESS
- OTP.CHECK_FAILED
- OTP.CHECK_INVALID
- OTP.CHECK_SUCCESS
- PASSWORD.CHECK_FAILED
- PASSWORD.CHECK_SUCCEEDED

**Entity Management** contains the following events:

- ACTION.CREATED
- AGREEMENT.CREATED
- AGREEMENT_LANGUAGE.CREATED
- AGREEMENT_LANGUAGE_REVISION.CREATED
- APPLICATION.CREATED
- AUTHORIZE_POLICY.CREATED
- CERTIFICATE.CREATED
- DEVICE.CREATED
- DEVICE_AUTHENTICATION_POLICY.CREATED
- FIDO_POLICY.CREATED
- FLOW.CREATED
- FLOW_DEFINITION.CREATED
- FLOW_EXECUTION.CREATED
- GROUP.CREATED
- IDENTITY_PROVIDER.CREATED
- IDP_ATTRIBUTE.CREATED
- INSTANT_MESSAGING_DELIVERY_SETTINGS.CREATED
- KEY.CREATED
- LICENSE.CREATED
- NOTIFICATION.CREATED
- NOTIFICATION_POLICY.CREATED
- ORGANIZATION.CREATED
- POLICY.CREATED
- RISK_POLICY_SET.CREATED
- SAML_ATTRIBUTE.CREATED
- SCHEMA_ATTRIBUTE.CREATED
- SIGN_ON_POLICY_ASSIGNMENT.CREATED
- VERIFY_POLICY.CREATED
- CERTIFICATE.READ
- KEY.READ
- SECRET.READ
- ACTION.UPDATED
- ADMIN_CONFIGURATION.UPDATED
- AGREEMENT.UPDATED
- AGREEMENT_LANGUAGE.UPDATED
- AGREEMENT_LANGUAGE_REVISION.UPDATED
- APPLICATION.UPDATED
- AUTHORIZE_POLICY.UPDATED
- CERTIFICATE.UPDATED
- DEVICE.NICKNAME_UPDATED
- DEVICE.UPDATED
- DEVICE_AUTHENTICATION_POLICY.UPDATED
- FIDO_POLICY.UPDATED
- FLOW.UPDATED
- FLOW_DEFINITION.UPDATED
- FLOW_EXECUTION.UPDATED
- GROUP.UPDATED
- IDENTITY_PROVIDER.UPDATED
- IDP_ATTRIBUTE.UPDATED
- INSTANT_MESSAGING_DELIVERY_SETTINGS.UPDATED
- KEY.UPDATED
- LICENSE.UPDATED
- NOTIFICATION.UPDATED
- NOTIFICATION_POLICY.UPDATED
- NOTIFICATIONS_SETTINGS.UPDATED
- ORGANIZATION.UPDATED
- POLICY.UPDATED
- RISK_POLICY_SET.ORDER_UPDATED
- RISK_POLICY_SET.UPDATED
- SAML_ATTRIBUTE.UPDATED
- SCHEMA_ATTRIBUTE.UPDATED
- SECRET.UPDATED
- SETTINGS.UPDATED
- SIGN_ON_POLICY_ASSIGNMENT.UPDATED
- USER.QUOTA_RESET
- USER.UPDATED
- VERIFY_POLICY.UPDATED
- ACTION.DELETED
- AGREEMENT.DELETED
- AGREEMENT_LANGUAGE.DELETED
- AGREEMENT_LANGUAGE_REVISION.DELETED
- APPLICATION.DELETED
- AUTHORIZE_POLICY.DELETED
- CERTIFICATE.DELETED
- DEVICE.DELETED
- DEVICE_AUTHENTICATION_POLICY.DELETED
- FIDO_POLICY.DELETED
- FLOW.DELETED
- FLOW_DEFINITION.DELETED
- GROUP.DELETED
- IDENTITY_PROVIDER.DELETED
- IDP_ATTRIBUTE.DELETED
- INSTANT_MESSAGING_DELIVERY_SETTINGS.DELETED
- KEY.DELETED
- LICENSE.DELETED
- NOTIFICATION_POLICY.DELETED
- ORGANIZATION.DELETED
- POLICY.DELETED
- RISK_POLICY_SET.DELETED
- SAML_ATTRIBUTE.DELETED
- SCHEMA_ATTRIBUTE.DELETED
- SIGN_ON_POLICY_ASSIGNMENT.DELETED
- VERIFY_POLICY.DELETED
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
