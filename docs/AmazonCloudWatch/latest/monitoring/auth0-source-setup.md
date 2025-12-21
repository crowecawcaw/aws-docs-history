# Source configuration for Okta Auth0

## Integrating with Okta Auth0

Okta Auth0 is a flexible identity platform designed for modern application authentication and authorization. Auth0 provides developers with powerful tools to integrate secure login, user management, and access control into applications while maintaining scalability and customization. CloudWatch Pipeline uses the Auth0 Management API to retrieve Authentication (successful and failed logins), and API Activity logs from Auth0 log events.

## Authenticating with Okta Auth0

To read logs, the pipeline needs to authenticate with your Okta Auth0 tenant. Auth0 Management API access requires a Client ID and Client Secret belonging to a Machine-to-Machine (M2M) application.

**Generate Client Credentials** see API Settings for more details.

- Sign in to the Auth0 Dashboard using an admin account.
- Navigate to Applications → Applications.
- Select an existing Machine-to-Machine Application or create a new one.
- Ensure the application has the required scope permissions for the Management API, specifically: `read:logs`
- In the AWS Secrets Manager, create a secret and store the Client ID under the key `client_id` and the Client Secret under the key `client_secret`
- Identify your Auth0 Tenant Domain (for example: `yourtenant.us.auth0.com`) and give it in pipeline.

Once configured, the pipeline can authenticate using the Client Credentials flow and retrieve log events from Auth0.

## Configuring the CloudWatch Pipeline

To configure the pipeline to read logs, choose Okta Auth0 as the data source. Select the Source Type as Tenant and provide the required details such as your Auth0 Tenant Domain and Client Credentials. Once you create the pipeline, log data from Okta Auth0 will be collected and made available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and the Auth0 events that maps to Authentication (3002) and API Activity (6003)

**Authentication** contains the following events:

- f
- fu
- fp
- feccft
- fepft
- feacft
- fc
- fco
- fcoa
- fd
- ferrt
- fertft
- fsa
- limit_wc
- limit_sul
- limit_mu
- pwd_leak
- reset_pwd_leak
- signup_pwd_leak
- gd_auth_fail_email_verification
- gd_auth_failed
- gd_auth_rejected
- gd_otp_rate_limit_exceed
- gd_recovery_failed
- gd_recovery_rate_limit_exceed
- gd_webauthn_challenge_failed
- passkey_challenge_failed
- scp
- sv
- ss
- s
- fi
- fv
- feoobft
- feotpft
- fercft
- ss_sso_failure
- fepotpft
- fvr
- flo

[Show moreShow less](# "#")
**API Activity** contains the following events:

- api_limit
- limit_delegation
- mgmt_api_read
- sapi
- api_limit_warning
