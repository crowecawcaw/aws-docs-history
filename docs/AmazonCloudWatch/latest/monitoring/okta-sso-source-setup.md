

# Source configuration for Okta SSO
<a name="okta-sso-source-setup"></a>

## Integrating with Okta SSO
<a name="okta-sso-integration"></a>

CloudWatch Pipeline uses the Okta System Log API to retrieve Authentication, API Activity, Detection Finding and Entity Management events from your Okta SSO tenant.

## Authenticating with Okta SSO
<a name="okta-sso-authentication"></a>

To read the logs, the pipeline needs to authenticate with your Okta SSO tenant. For Okta SSO, authentication is performed using the OAuth 2.0 Client Credentials (JWT Assertion) flow through an Okta API Services application.

**Generate the private/public key pair for authentication**
+ Sign in to the Okta Admin Console using an administrator account.
+ Navigate to Applications → Applications.
+ Select an existing API Services Application or create a new one.
+ Under General → Client Credentials, upload a public key or generate a new key. This key pair will be used to authenticate using a signed JWT assertion.
+ Make sure the application has the required OAuth scopes assigned, specifically: `okta.logs.read`
+ Admin Roles → Edit assignments → Role(Select Read-only Administrator)
+ Copy the Client ID of the application.
+ Store the client\_id and client\_secret(private key) in AWS Secrets Manager: `client_id` and `client_secret(private_key)` (the RSA private key used to sign the JWT assertion)
+ Identify your Okta Organization URL and configure in the pipeline (for example: `https://yourdomain.okta.com`).

Once configured, the pipeline can authenticate using Okta's OAuth 2.0 Client Credentials (JWT Assertion) flow and begin retrieving audit log events from the Okta System Log API.

## Configuring the CloudWatch Pipeline
<a name="okta-sso-pipeline-config"></a>

To configure the pipeline to read logs, choose Okta SSO as the data source. Fill in the required information like Okta Domain name. After you create and activate the pipeline, audit log data from Okta SSO will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="okta-sso-ocsf-events"></a>

This integration supports OCSF schema version v1.5.0 and Okta events that map to Authentication (3002), API Activity (6003), Detection Finding (2004), and Entity Management (3004).

**Authentication** contains the following events:
+ user.authentication.auth
+ user.authentication.auth\_via\_AD\_agent
+ user.authentication.auth\_via\_IDP
+ user.authentication.auth\_via\_LDAP\_agent
+ user.authentication.auth\_via\_inbound\_SAML
+ user.authentication.auth\_via\_inbound\_delauth
+ user.authentication.auth\_via\_iwa
+ user.authentication.auth\_via\_mfa
+ user.authentication.auth\_via\_radius
+ user.authentication.auth\_via\_richclient
+ user.authentication.auth\_via\_social
+ user.authentication.authenticate
+ user.authentication.sso
+ user.session.start
+ user.session.impersonation.grant
+ app.oauth2.signon
+ user.session.impersonation.initiate
+ user.authentication.universal\_logout
+ user.session.clear
+ user.session.end
+ user.authentication.slo
+ user.authentication.universal\_logout.scheduled
+ user.session.expire
+ user.session.impersonation.end
+ user.authentication.verify
+ policy.evaluate\_sign\_on
+ user.mfa.attempt\_bypass
+ user.mfa.okta\_verify
+ user.mfa.okta\_verify.deny\_push
+ user.mfa.okta\_verify.deny\_push\_upgrade\_needed
+ user.mfa.factor.activate
+ user.mfa.factor.deactivate
+ user.mfa.factor.reset\_all
+ user.mfa.factor.suspend
+ user.mfa.factor.unsuspend
+ user.mfa.factor.update
+ user.session.impersonation.extend
+ user.session.impersonation.revoke
+ user.session.access\_admin\_app
+ user.session.context.change
+ application.policy.sign\_on.deny\_access
+ user.authentication.auth\_unconfigured\_identifier
+ user.authentication.dsso\_via\_non\_priority\_source
+ app.oauth2.invalid\_client\_credentials
+ policy.auth\_reevaluate.fail

**API Activity** contains the following events:
+ oauth2.claim.created
+ oauth2.scope.created
+ security.trusted\_origin.create
+ system.api\_token.create
+ workflows.user.table.view
+ app.oauth2.as.key.rollover
+ app.saml.sensitive.attribute.update
+ system.api\_token.update
+ oauth2.claim.updated
+ oauth2.scope.updated
+ security.events.provider.deactivate
+ system.api\_token.revoke
+ oauth2.claim.deleted
+ oauth2.scope.deleted

**Detection Finding** contains the following events:
+ security.attack.start
+ security.breached\_credential.detected
+ security.request.blocked
+ security.threat.detected
+ security.zone.make\_blacklist
+ system.rate\_limit.violation
+ user.account.report\_suspicious\_activity\_by\_enduser
+ user.risk.change
+ user.risk.detect
+ zone.make\_blacklist
+ security.attack.end

**Entity Management** contains the following events:
+ iam.role.create
+ system.idp.lifecycle.create
+ application.lifecycle.create
+ group.lifecycle.create
+ user.lifecycle.create
+ policy.lifecycle.create
+ zone.create
+ oauth2.as.created
+ event\_hook.created
+ inline\_hook.created
+ pam.security\_policy.create
+ iam.resourceset.create
+ pam.secret.create
+ analytics.reports.export.download
+ app.audit\_report.download
+ system.idp.lifecycle.read\_client\_secret
+ app.oauth2.client.read\_client\_secret
+ pam.secret.reveal
+ pam.service\_account.password.reveal
+ support.org.update
+ system.idp.lifecycle.update
+ application.lifecycle.update
+ policy.lifecycle.update
+ user.account.update\_profile
+ user.account.update\_password
+ user.account.reset\_password
+ group.profile.update
+ zone.update
+ group.privilege.grant
+ group.privilege.revoke
+ iam.resourceset.bindings.add
+ user.account.privilege.grant
+ user.account.privilege.revoke
+ pki.cert.lifecycle.revoke
+ iam.resourceset.update
+ iam.role.update
+ pam.security\_policy.update
+ oauth2.as.updated
+ event\_hook.updated
+ inline\_hook.updated
+ pam.secret.update
+ iam.resourceset.bindings.delete
+ iam.role.delete
+ pam.security\_policy.delete
+ policy.lifecycle.delete
+ user.lifecycle.delete.initiated
+ application.lifecycle.delete
+ group.lifecycle.delete
+ zone.delete
+ oauth2.as.deleted
+ event\_hook.deleted
+ inline\_hook.deleted
+ iam.resourceset.delete
+ pam.secret.delete
+ device.enrollment.create
+ credential.register
+ credential.revoke
+ policy.lifecycle.activate
+ system.feature.enable
+ event\_hook.activated
+ inline\_hook.activated
+ system.feature.disable
+ application.lifecycle.activate
+ user.lifecycle.activate
+ zone.activate
+ oauth2.as.activated
+ system.log\_stream.lifecycle.activate
+ policy.lifecycle.deactivate
+ security.authenticator.lifecycle.deactivate
+ application.lifecycle.deactivate
+ user.lifecycle.deactivate
+ zone.deactivate
+ event\_hook.deactivated
+ inline\_hook.deactivated
+ system.log\_stream.lifecycle.deactivate
+ oauth2.as.deactivated
+ user.account.lock
+ user.account.lock.limit
+ user.lifecycle.suspend
+ device.lifecycle.suspend
+ user.account.unlock
+ user.lifecycle.unsuspend
+ device.lifecycle.unsuspend
+ user.lifecycle.reactivate