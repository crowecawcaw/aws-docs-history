# Source configuration for Entrust IDaaS

## Integrating with Entrust IDaaS

Entrust Identity as a Service (IDaaS) is a cloud-based Identity and Access Management (IAM) platform that provides multi-factor authentication (MFA), single sign-on (SSO), adaptive risk-based authentication, and comprehensive audit logging across workforce, consumer, and citizen use cases. CloudWatch pipeline uses the Entrust IDaaS Administration REST API to retrieve identity and access events from your IDaaS tenant.

The Administration REST API provides access to two primary log categories. Authentication Logs capture user authentication events across multiple event types, including MFA, SSO, SAML, OIDC, and passwordless authentication methods. Management Logs track administrative actions and changes performed across various entity types such as users, groups, applications, tokens, and policies.

## Authenticating with Entrust IDaaS

To read the logs, the pipeline needs to authenticate with your Entrust IDaaS tenant. The plugin supports Administration API authentication using an `applicationId` and `sharedSecret`.

**Create an Administration API application**

- Go to your IDaaS Admin portal and navigate to Security → Applications.
- Choose + and select Administration API from the list of available applications.
- In the General tab, enter a name and description for your application, then choose Next.
- In the Setup tab, assign the role with the permissions required by your application, then choose Submit. The Entrust IDaaS Administration API requires the Super Administrator role to access audit log endpoints.
- In the Complete tab, choose Copy to copy your `applicationId` and `sharedSecret`, or download the JSON file.
- In AWS Secrets Manager, create a secret and store the `applicationId` under the key `client_id` and the `sharedSecret` under the key `client_secret`.
- Your IDaaS API base URL is `https://<hostname>` where `hostname` is taken from the credentials (for example, `https://entrust.us.trustedauth.com`).

## Configuring the CloudWatch Pipeline

To configure the pipeline to read audit logs from Entrust IDaaS, choose `entrust_idaas` as the data source. Fill in the required information such as your tenant `hostname` and the AWS Secrets Manager secret ARN for your credentials where `client_id` and `client_secret` are stored. After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and events that map to Authentication (3002) and Entity Management (3004).

**Authentication** contains the following events:

- AuthenticationAdminApiSuccessEvent
- AuthenticationDeniedEvent
- AuthenticationExternalSecondFactorBypassEvent
- AuthenticationExternalSuccessEvent
- AuthenticationFaceSuccessEvent
- AuthenticationFidoSuccessEvent
- AuthenticationFirstFactorExternalSuccessEvent
- AuthenticationFirstFactorIdpSuccessEvent
- AuthenticationFirstFactorPasswordSuccessEvent
- AuthenticationGridSuccessEvent
- AuthenticationGridWithTempAccessCodeSuccessEvent
- AuthenticationIdpSuccessEvent
- AuthenticationKbaSuccessEvent
- AuthenticationLockedEvent
- AuthenticationMagicLinkSuccessEvent
- AuthenticationOtpCreatedEvent
- AuthenticationOtpEmailSentEvent
- AuthenticationOtpNoCreditEvent
- AuthenticationOtpSentToAllEvent
- AuthenticationOtpSmsSentEvent
- AuthenticationOtpSuccessEvent
- AuthenticationOtpUnavailableEvent
- AuthenticationOtpVoiceSentEvent
- AuthenticationOtpWithTempAccessCodeSuccessEvent
- AuthenticationPasskeySuccessEvent
- AuthenticationPasswordSuccessEvent
- AuthenticationSecondFactorFaceSuccessEvent
- AuthenticationSecondFactorFIDOSuccessEvent
- AuthenticationSecondFactorGridSuccessEvent
- AuthenticationSecondFactorGridWithTempAccessCodeSuccessEvent
- AuthenticationSecondFactorKbaSuccessEvent
- AuthenticationSecondFactorMagicLinkSuccessEvent
- AuthenticationSecondFactorOtpSuccessEvent
- AuthenticationSecondFactorOtpWithTempAccessCodeSuccessEvent
- AuthenticationSecondFactorSmartCredentialPushSuccessEvent
- AuthenticationSecondFactorTempAccessCodeSuccessEvent
- AuthenticationSecondFactorTokenSuccessEvent
- AuthenticationSecondFactorTokenWithTempAccessCodeSuccessEvent
- AuthenticationSecondFactorUserCertificateSuccessEvent
- AuthenticationSmartCredentialPushSuccessEvent
- AuthenticationSmartLoginSuccessEvent
- AuthenticationTempAccessCodeSuccessEvent
- AuthenticationTokenPushSuccessEvent
- AuthenticationTokenSuccessEvent
- AuthenticationTokenWithTempAccessCodeSuccessEvent
- AuthenticationUserCertificateSuccessEvent
- MachineLockedEvent
- OidcAuthenticationFailedEvent
- OidcAuthenticationSuccessEvent
- SamlAuthenticationFailedEvent
- SamlAuthenticationSuccessEvent
- UserPasswordChangeFailedEvent
- UserPasswordChangeLockedEvent
- UserStepUpAuthenticationSuccessEvent
- VerificationDeniedEvent
- VerificationIdpSuccessEvent

[Show moreShow less](# "#")
**Entity Management** contains the following events:

- ACTIVESYNC
- AD\_CONNECTOR\_DIRECTORIES
- AGENTS
- APPLICATIONS
- ARCHIVES
- AUTHENTICATIONFLOWS
- AUTHORIZATIONGROUPS
- AZURE\_DIRECTORIES
- BLACKLISTEDPASSWORDS
- BULKENROLLMENTS
- BULKGROUPS
- BULKHARDWARETOKENS
- BULKIDENTITYGUARD
- BULKSMARTCARDS
- BULKUSERS
- CAS
- CERTIFICATES
- CLAIMS
- CONTACTVERIFICATION
- CONTEXTRULES
- CREATETENANT
- CREDENTIALDESIGNS
- CUSTOMIZATIONVARIABLES
- DIGITALIDCERTIFICATES
- DIGITALIDCONFIGCERTTEMPS
- DIGITALIDCONFIGS
- DIGITALIDCONFIGSANS
- DIGITALIDCONFIGVARIABLES
- DIRECTORIES
- DIRECTORYATTRIBUTES
- DIRECTORYCONNECTIONS
- DIRECTORYPASSWORD
- DIRECTORYSEARCHATTRIBUTES
- DIRECTORYSYNC
- DOMAINCONTROLLERCERTS
- EMAILTEMPLATES
- EMAILVARIABLES
- ENROLLMENTDESIGNS
- ENROLLMENTS
- ENTITLEMENTS
- EXPECTEDLOCATIONS
- EXPORTREPORTS
- FACE
- FIDOTOKENS
- GATEWAYCSRS
- GATEWAYS
- GRIDCONTENTS
- GRIDS
- GROUPPOLICIES
- GROUPS
- HIGH\_AVAILABILITY\_GROUPS
- HOSTNAMESETTINGS
- IDENTITYPROVIDERS
- IDPROOFING
- IDPROOFINGLICENSE
- INTELLITRUSTDESKTOPS
- IPLISTS
- ISSUANCE
- MAGICLINKCONTENTS
- MAGICLINKS
- OAUTHROLES
- ORGANIZATIONS
- OTPPROVIDERS
- OTPS
- PIVCONTENTSIGNER
- PKIAASCREDENTIALS
- POLICYOVERRIDE
- PREFERREDOTPPROVIDERS
- PRINTERS
- PUSHCREDENTIALS
- QUESTIONS
- RATELIMITING
- REPORTS
- RESOURCESERVERAPIS
- RESOURCESERVERSCOPES
- RISKENGINES
- ROLES
- SCDEFNPIVAPPLETCONFIGS
- SCDEFNS
- SCDEFNVARIABLES
- SCHEDULEDTASKS
- SCIMPROVISIONINGS
- SENDAZUREAD
- SENDEMAIL
- SENDSCIM
- SERVICEPROVIDERACCOUNTS
- SERVICEPROVIDERS
- SETTINGS
- SMARTCARDS
- SMARTCREDENTIALS
- SMARTCREDENTIALSSIGNATURE
- SPCLIENTCREDENTIALS
- SPENTITLEMENTS
- SPIDENTITYPROVIDERS
- SPMANAGEMENTPLATFORM
- SPROLES
- SPUSERMGMT
- SUBSCRIBERS
- TEMPACCESSCODECONTENTS
- TEMPACCESSCODES
- TEMPLATES
- TENANTS
- TOKENACTIVATIONCONTENTS
- TOKENS
- TRANSACTIONITEMS
- TRANSACTIONRULES
- USERATTRIBUTES
- USERATTRIBUTEVALUES
- USERKBACHALLENGES
- USERLOCATIONS
- USERMACHINES
- USEROAUTHTOKENS
- USERPASSWORDS
- USERQUESTIONANSWERS
- USERQUESTIONS
- USERRBASETTINGS
- USERS
- USERSITEROLES
- USERSPROLES
- WORDSYNONYMS

[Show moreShow less](# "#")
