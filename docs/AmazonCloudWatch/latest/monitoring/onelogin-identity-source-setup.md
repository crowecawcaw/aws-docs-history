# Source configuration for OneLogin Identity

## Integrating with OneLogin Identity

OneLogin is a cloud-based identity and access management (IAM) platform that provides single sign-on (SSO), multi-factor authentication (MFA), and user provisioning capabilities. CloudWatch pipelines uses the OneLogin Events API to retrieve information about authentication events, user activities, policy decisions, and administrative changes across your OneLogin environment. The Events API enables access to event data through REST endpoints, allowing retrieval of security and access logs from your OneLogin account.

## Authenticating with OneLogin Identity

To read the logs, the pipeline needs to authenticate with your OneLogin account. For OneLogin, authentication is performed using OAuth2.

**Configure OAuth2 authentication for OneLogin**

- Log in to the OneLogin Admin Portal and navigate to Developers → API Credentials. Create a new API credential pair. Note the Client ID and Client Secret immediately.
- Assign the appropriate permissions. Select Read All or Manage All scope to make sure the credentials can access event log data.
- In AWS Secrets Manager, create a secret and store the Client ID under key `client_id` and the client secret under key `client_secret`.
- Note your Account ID (subdomain) from the OneLogin Admin Portal under Settings → Account Settings.

## Configuring the CloudWatch Pipeline

To configure the pipeline to read logs, choose OneLogin as the data source. Fill in the required information like subdomain and authentication credentials. Optionally, specify the Range duration format (for example, PT21H for the last 21 hours). After you create and activate the pipeline, event log data from OneLogin will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and OneLogin events that map to Account Change (3001), Authentication (3002), and Entity Management (3004).

**Account Change** contains the following events:

- User requested new password
- Changed password for user
- User deactivated
- Password request approved from user
- User locked
- User suspended
- User locked out of app
- OTP device unlocked for user
- User suspended in app
- User suspended in directory
- Unlocked user in directory
- User granted permission to manage role
- User permission to manage role revoked
- User enabled desktop SSO
- User disabled desktop SSO
- Admin changed password for user
- Redirected to an external site for password reset
- API - password updated for user
- API - user locked
- User suspended through API
- User locked through API
- User enabled adaptive login for account
- User disabled adaptive login for account
- Profile change password
- Manually added user to app
- Manually removed user from app
- Failed to change password for user
- User granted permission to manage role failed
- User permission to manage role revoked failed
- Smart password updated for user
- Smart password could not be updated for user
- API - password not updated for user

[Show moreShow less](# "#")
**Authentication** contains the following events:

- User logged into OneLogin
- User logged out of OneLogin
- User logged into app
- User logged out of app
- User authenticated by RADIUS configuration
- User authenticated through API
- User successfully authenticated with VLDAP
- User signed in into OneLogin through social network
- User successfully authenticated with VLDAP (OneLogin Desktop Mac)
- API - user logged out
- API - verify factor called
- API - confirm OTP for user succeeded
- User was force logged out
- User successfully logged in on a trusted device
- User successfully logged in through OneLogin Desktop
- User denied auth through OTP push request
- User challenged for OTP
- User reauthenticated into app
- User verified OTP device
- OIDC password for app success
- API - trigger factor for user succeeded
- OIDC implicit flow for app success
- OIDC authorization code for app success
- OIDC get code for app success
- OIDC validate token for app success
- User failed authentication
- User failed to log into app
- User rejected by RADIUS configuration
- Failed to login to app through IDP
- Could not authenticate to app
- User failed authentication through API
- User failed authentication with VLDAP
- User authentication policy does not allow sign-in through social network
- User failed authentication with VLDAP (OneLogin Desktop Mac)
- API - user failed to log out
- API - verify factor failed
- API - confirm OTP for user failed
- User failed to log in on a trusted device
- User failed to login through OneLogin Desktop
- User failed to authenticate through OneLogin Desktop
- User failed OTP challenge
- OIDC implicit flow for app failed
- OIDC authorization code for app failed
- OIDC password for app failed
- OIDC validate token for app failed
- OIDC general fail
- OIDC get code for app failed

[Show moreShow less](# "#")
**Entity Management** contains the following events:

- Assigned role to user
- User was created
- User updated
- User deactivated
- User was activated
- User was deleted
- OTP device registered for user
- OTP device deregistered for user
- Updated credit card
- User provisioned in app
- User updated in app
- User suspended in app
- User reactivated in app
- User deleted in app
- Account granted permission to privilege
- Account revoked permission to privilege
- User granted permission to privilege
- User permission to privilege revoked
- Added trusted IDP
- Removed trusted IDP
- Modified trusted IDP
- User provisioned in directory
- User updated by directory
- User suspended in directory
- User reactivated in directory
- User deleted in directory
- Deleted secure note
- Updated user login information
- Attempted to update login information
- Changed the default trusted IDP
- User added to role
- User removed from role
- Created policy
- Updated policy
- Deleted policy
- Created proxy agent
- Deleted proxy agent
- Created RADIUS configuration
- Updated RADIUS configuration
- Deleted RADIUS configuration
- Enabled VPN
- Updated VPN settings
- Disabled VPN
- Enabled embedding
- Updated embedding settings
- Disabled embedding
- Created authentication factor
- Updated authentication factor
- Deleted authentication factor
- Updated security questions
- Updated desktop SSO settings
- Enabled desktop SSO
- Disabled desktop SSO
- Created certificate
- Deleted certificate
- Created API credential
- Deleted API credential
- Enabled API credential
- Disabled API credential
- Enabled virtual LDAP
- Disabled virtual LDAP
- Updated virtual LDAP settings
- Enabled branding
- Disabled branding
- Updated branding
- Deleted mapping
- Disabled mapping
- Enabled mapping
- Updated mapping
- Deleted custom user fields
- Updated company info
- Updated account settings
- Deleted directory
- Deleted connector instance from directory
- Created self registration
- Updated self registration
- Deleted self registration
- Created payment record
- Updated payment record
- Deleted payment record
- Updated terms and conditions for policy
- Manually updated user login for app
- User was created by trusted IDP
- Directory external ID was updated for user
- Directory external ID was deleted for user
- Updated broadcaster
- Deleted broadcaster
- API - roles added to user
- API - roles removed for user
- API - user updated
- API - user deleted
- API - user created
- Updated directory
- OUs were updated for directory
- User suspended through API
- User reactivated through API
- App was updated
- Connector was created
- Connector was updated
- Connector was deleted
- Parameter was created
- Parameter was updated
- Parameter was deleted
- Deleted device for OneLogin Desktop
- Revoked user certificate
- Revoked device certificate
- App was created through API
- App was updated through API
- App was destroyed through API
- Sandbox deleted
- Sandbox created
- Sandbox updated
- User deleted security factor
- User renamed security factor
- Created RADIUS attribute
- Updated RADIUS attribute
- Deleted RADIUS attribute
- Role created
- Role deleted
- SMTP configuration updated
- Smart hook created
- Smart hook updated
- Smart hook deleted
- Smart hook environment variable created
- Smart hook environment variable updated
- Smart hook environment variable deleted
- API - privilege was created
- Created privilege
- API - privilege was updated
- Updated privilege
- API - privilege was deleted
- Deleted privilege
- API - privilege was assigned to user
- Assigned privilege to user
- API - privilege removed from user
- Removed privilege from user
- API - privilege assigned to role
- Assigned privilege to role
- API - privilege removed from role
- Removed privilege from role
- Report created
- Report updated
- Report destroyed
- Created group
- Updated group
- Destroyed group
- Created secure note
- API - app rules create success
- API - app rules update success
- API - app rules delete success
- API - roles update success
- Credit card update failed
- User could not be updated
- User could not be deleted in app
- User could not be updated in app
- User not updated in app
- API - user not deleted
- API - user not updated
- API - user not created
- Connector could not be created
- Connector could not be updated
- Connector could not be deleted
- Parameter could not be created
- Parameter could not be updated
- Parameter could not be deleted
- App failed to create through API
- App failed to update through API
- App failed to destroy through API
- Failed to delete sandbox
- Failed to create sandbox
- Failed to update sandbox
- Smart hook update failed
- Smart hook environment variable update failed
- API - app rules create failed
- API - app rules update failed
- API - app rules delete failed
- User added to role failed
- Role created failed
- Role deleted failed
- API - roles update failed

[Show moreShow less](# "#")
