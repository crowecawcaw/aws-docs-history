# Source configuration for Okta SSO

## Integrating with Okta SSO

CloudWatch Pipeline uses the Okta System Log API to retrieve Authentication, API Activity, Detection Finding and Entity Management events from your Okta SSO tenant.

## Authenticating with Okta SSO

To read the logs, the pipeline needs to authenticate with your Okta SSO tenant. For Okta SSO, authentication is performed using the OAuth 2.0 Client Credentials (JWT Assertion) flow through an Okta API Services application.

**Generate the private/public key pair for authentication**

- Sign in to the Okta Admin Console using an administrator account.
- Navigate to Applications → Applications.
- Select an existing API Services Application or create a new one.
- Under General → Client Credentials, upload a public key or generate a new key. This key pair will be used to authenticate using a signed JWT assertion.
- Ensure the application has the required OAuth scopes assigned, specifically: `okta.logs.read`
- Admin Roles → Edit assignments → Role(Select Read-only Administrator)
- Copy the Client ID of the application.
- Store the client_id and client_secret(private key) in AWS Secrets Manager: `client_id` and `client_secret(private_key)` (the RSA private key used to sign the JWT assertion)
- Identify your Okta Organization URL and configure in the pipeline (for example: `https://yourdomain.okta.com`).

Once configured, the pipeline can authenticate using Okta's OAuth 2.0 Client Credentials (JWT Assertion) flow and begin retrieving audit log events from the Okta System Log API.

## Configuring the CloudWatch Pipeline

To configure the pipeline to read logs, choose Okta SSO as the data source. Fill in the required information like Okta Domain name. Once you create and activate the pipeline, audit log data from Okta SSO will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and Okta events that map to Authentication (3002), API Activity (6003), Detection Finding (2004), and Entity Management (3004).

**Authentication** contains the following events:

- user.authentication.auth
- user.authentication.auth_via_AD_agent
- user.authentication.auth_via_IDP
- user.authentication.auth_via_LDAP_agent
- user.authentication.auth_via_inbound_SAML
- user.authentication.auth_via_inbound_delauth
- user.authentication.auth_via_iwa
- user.authentication.auth_via_mfa
- user.authentication.auth_via_radius
- user.authentication.auth_via_richclient
- user.authentication.auth_via_social
- user.authentication.authenticate
- user.authentication.sso
- user.session.start
- user.session.impersonation.grant
- app.oauth2.signon
- user.session.impersonation.initiate
- user.authentication.universal_logout
- user.session.clear
- user.session.end
- user.authentication.slo
- user.authentication.universal_logout.scheduled
- user.session.expire
- user.session.impersonation.end
- user.authentication.verify
- policy.evaluate_sign_on
- user.mfa.attempt_bypass
- user.mfa.okta_verify
- user.mfa.okta_verify.deny_push
- user.mfa.okta_verify.deny_push_upgrade_needed
- user.mfa.factor.activate
- user.mfa.factor.deactivate
- user.mfa.factor.reset_all
- user.mfa.factor.suspend
- user.mfa.factor.unsuspend
- user.mfa.factor.update
- user.session.impersonation.extend
- user.session.impersonation.revoke
- user.session.access_admin_app
- user.session.context.change
- application.policy.sign_on.deny_access
- user.authentication.auth_unconfigured_identifier
- user.authentication.dsso_via_non_priority_source
- app.oauth2.invalid_client_credentials
- policy.auth_reevaluate.fail

[Show moreShow less](# "#")
**API Activity** contains the following events:

- oauth2.claim.created
- oauth2.scope.created
- security.trusted_origin.create
- system.api_token.create
- workflows.user.table.view
- app.oauth2.as.key.rollover
- app.saml.sensitive.attribute.update
- system.api_token.update
- oauth2.claim.updated
- oauth2.scope.updated
- security.events.provider.deactivate
- system.api_token.revoke
- oauth2.claim.deleted
- oauth2.scope.deleted

**Detection Finding** contains the following events:

- security.attack.start
- security.breached_credential.detected
- security.request.blocked
- security.threat.detected
- security.zone.make_blacklist
- system.rate_limit.violation
- user.account.report_suspicious_activity_by_enduser
- user.risk.change
- user.risk.detect
- zone.make_blacklist
- security.attack.end

**Entity Management** contains the following events:

- iam.role.create
- system.idp.lifecycle.create
- application.lifecycle.create
- group.lifecycle.create
- user.lifecycle.create
- policy.lifecycle.create
- zone.create
- oauth2.as.created
- event_hook.created
- inline_hook.created
- pam.security_policy.create
- iam.resourceset.create
- pam.secret.create
- analytics.reports.export.download
- app.audit_report.download
- system.idp.lifecycle.read_client_secret
- app.oauth2.client.read_client_secret
- pam.secret.reveal
- pam.service_account.password.reveal
- support.org.update
- system.idp.lifecycle.update
- application.lifecycle.update
- policy.lifecycle.update
- user.account.update_profile
- user.account.update_password
- user.account.reset_password
- group.profile.update
- zone.update
- group.privilege.grant
- group.privilege.revoke
- iam.resourceset.bindings.add
- user.account.privilege.grant
- user.account.privilege.revoke
- pki.cert.lifecycle.revoke
- iam.resourceset.update
- iam.role.update
- pam.security_policy.update
- oauth2.as.updated
- event_hook.updated
- inline_hook.updated
- pam.secret.update
- iam.resourceset.bindings.delete
- iam.role.delete
- pam.security_policy.delete
- policy.lifecycle.delete
- user.lifecycle.delete.initiated
- application.lifecycle.delete
- group.lifecycle.delete
- zone.delete
- oauth2.as.deleted
- event_hook.deleted
- inline_hook.deleted
- iam.resourceset.delete
- pam.secret.delete
- device.enrollment.create
- credential.register
- credential.revoke
- policy.lifecycle.activate
- system.feature.enable
- event_hook.activated
- inline_hook.activated
- system.feature.disable
- application.lifecycle.activate
- user.lifecycle.activate
- zone.activate
- oauth2.as.activated
- system.log_stream.lifecycle.activate
- policy.lifecycle.deactivate
- security.authenticator.lifecycle.deactivate
- application.lifecycle.deactivate
- user.lifecycle.deactivate
- zone.deactivate
- event_hook.deactivated
- inline_hook.deactivated
- system.log_stream.lifecycle.deactivate
- oauth2.as.deactivated
- user.account.lock
- user.account.lock.limit
- user.lifecycle.suspend
- device.lifecycle.suspend
- user.account.unlock
- user.lifecycle.unsuspend
- device.lifecycle.unsuspend
- user.lifecycle.reactivate

[Show moreShow less](# "#")
