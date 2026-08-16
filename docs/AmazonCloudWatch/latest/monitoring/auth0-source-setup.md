# Source configuration for Okta Auth0

## Integrating with Okta Auth0

Okta Auth0 is a flexible identity platform designed for modern application authentication and authorization. Auth0 provides developers with powerful tools to integrate secure login, user management, and access control into applications while maintaining scalability and customization. CloudWatch Pipeline uses the Auth0 Management API to retrieve Authentication (successful and failed logins), and API Activity logs from Auth0 log events.

## Authenticating with Okta Auth0

To read logs, the pipeline needs to authenticate with your Okta Auth0 tenant. Auth0 Management API access requires a Client ID and Client Secret belonging to a Machine-to-Machine (M2M) application.

**Generate Client Credentials** see API Settings for more details.

- Sign in to the Auth0 Dashboard using an admin account.
- Navigate to Applications → Applications.
- Select an existing Machine-to-Machine Application or create a new one.
- Make sure the application has the required scope permissions for the Management API, specifically: `read:logs`
- In the AWS Secrets Manager, create a secret and store the Client ID under the key `client_id` and the Client Secret under the key `client_secret`
- Identify your Auth0 Tenant Domain (for example: `yourtenant.us.auth0.com`) and give it in pipeline.

Once configured, the pipeline can authenticate using the Client Credentials flow and retrieve log events from Auth0.

## Configuring the CloudWatch Pipeline

To configure the pipeline to read logs, choose Okta Auth0 as the data source. Select the Source Type as Tenant and provide the required details such as your Auth0 Tenant Domain and Client Credentials. After you create the pipeline, log data from Okta Auth0 will be collected and made available in the selected CloudWatch Logs log group.

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
- limit\_wc
- limit\_sul
- limit\_mu
- pwd\_leak
- reset\_pwd\_leak
- signup\_pwd\_leak
- gd\_auth\_fail\_email\_verification
- gd\_auth\_failed
- gd\_auth\_rejected
- gd\_otp\_rate\_limit\_exceed
- gd\_recovery\_failed
- gd\_recovery\_rate\_limit\_exceed
- gd\_webauthn\_challenge\_failed
- passkey\_challenge\_failed
- scp
- sv
- ss
- s
- fi
- fv
- feoobft
- feotpft
- fercft
- ss\_sso\_failure
- fepotpft
- fvr
- flo

[Show moreShow less](# "#")
**API Activity** contains the following events:

- api\_limit
- limit\_delegation
- mgmt\_api\_read
- sapi
- api\_limit\_warning
