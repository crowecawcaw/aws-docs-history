# Identity and access management

| CMSEC_3: How do you manage the identities of your vehicles and individual<br>ECUs? |
| ---------------------------------------------------------------------------------- |
|                                                                                    |

When working with connected vehicles, you must determine how you will manage the identities of your vehicles and individual
Electronic Control Units (ECUs). These identities can come in different forms and are used to authenticate and authorize access
to a variety of services in the connected vehicle environment. This includes other vehicles, charging stations, backend services,
OTA servers, and more. For example, an ECU can be uniquely identified with a private key (usually stored in a secure hardware module
such as a TPM or an HSM) and an X.509 certificate corresponding to that private key. These X.509 certificates may have subject names or
extensions with vehicle and ECU information such as VIN or ECU ID.

There are important considerations when provisioning, rotating, revoking, and managing the lifecycle of certificates on ECUs. Each ECU
can have several X.509 certificates, each used for different purposes such as an attestation certificate (or birth certificate) used
to authenticate an ECU, and one or more operational certificates. These operational certificates are used to authenticate to connected
vehicle services. For example, when the ECU connects to a connected vehicle service using Mutual TLS, it can present its client
certificate and cryptographically prove that it possesses the private key. The TLS server can validate the certificate to authenticate
that the connection originates from the ECU that owns the private key.

In addition to X.509 certificates, vehicles and ECUs may use other forms of identities such as tokens, API credentials, and HTTP cookies.
For example, a user signs in to a streaming music application on the in-vehicle infotainment (IVI) system and after the user's authorization,
the music application receives an OIDC Access Token that is used to authenticate requests to the backend APIs of the streaming music service.
In another example, an ECU may exchange its operational certificate for a set of time-limited cloud API credentials used to invoke cloud service APIs
such as uploading video or telemetry data.

The following best practices can help you manage identities for your vehicles and
ECUs.

**[CMSEC\_BP3.1] Securely manage the lifecycle of identities and
credentials for your vehicles and ECUs**

It is important to check that each request or action on a
connected vehicle service is authenticated and authorized. The
security depends on appropriately managing the lifecycle
stages of the identities and credentials for your vehicles and
ECUs:

- **Provision**

This is the process of installing identities into your vehicles and ECUs. See
CM-S01 Vehicle and User Provisioning from scenarios section. Typically, this begins at
the manufacturing process where a unique Attestation X.509 certificate (also called a
Birth Certificate) is issued for the ECU to prove its authenticity and provenance. The
private key for the certificate can be generated within an on-board secure hardware
module such as a TPM or HSM, a Certificate Sign Request (CSR) is generated and presented
to a Certificate Authority (CA) that issues a certificate. The CA can be part of a
Private Key Infrastructure (PKI) owned and operated by the OEM or the supplier of the
ECU. For more information see [this blog
post](https://aws.amazon.com/blogs/iot/securing-modern-connected-vehicle-platforms-with-aws-iot/ "https://aws.amazon.com/blogs/iot/securing-modern-connected-vehicle-platforms-with-aws-iot/") that discusses provisioning certificates using AWS IoT. Additionally,
the ECU can have one or more operational certificates that are used to authenticate to
connected vehicle services. It is important to verify that the process of requesting and
issuing certificates is authenticated, authorized, and audited to check that only
genuine ECUs are issued certificates. If you are unable to generate private keys in an
on-board secure module and must generate private keys on a server, see that access to
these private keys is restricted and tracked as the security of client certificate-based
authentication relies on protecting the private keys. You have the option to design,
build and operate your own PKI and CAs, or you can take advantage of [AWS Private Certificate Authority](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md") (AWS PCA) that allows you to create private certificate authority
(CA) hierarchies, including root and subordinate CAs, without the investment and
maintenance costs of operating an on-premises CA.

- **Enroll or register**

After certificates are issued and installed in ECUs, you may also need to enroll or
register the certificates with your backend services. For example, you can register the
ECU's certificate in an asset database associated with the ECU ID (serial number) and
corresponding authorization policies that are applied to requests from that ECU. You can
build your own asset database using a self-hosted database or an [AWS managed cloud database service](https://aws.amazon.com/products/databases/ "https://aws.amazon.com/products/databases/"). If you are
using [AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") to connect your ECUs to
the cloud, IoT Core provides a built-in [registry for Things](../../../iot/latest/developerguide/thing-registry.md "../../../iot/latest/developerguide/thing-registry.md") and
their [registered X.509
certificates](../../../iot/latest/developerguide/register-device-cert.md "../../../iot/latest/developerguide/register-device-cert.md"). Each certificate registered in IoT Core can be associated with
an [IoT
Core Policy](../../../iot/latest/developerguide/iot-policies.md "../../../iot/latest/developerguide/iot-policies.md") (either directly or via [Thing Groups](../../../iot/latest/developerguide/thing-groups.md "../../../iot/latest/developerguide/thing-groups.md")) that
authorizes actions that the ECU can perform on the IoT Core service such as allowing
connections, publishing or subscribing to certain [MQTT topics](../../../iot/latest/developerguide/topics.md "../../../iot/latest/developerguide/topics.md"). IoT Core also allows
you to register certificates the first time an ECU connects using [Just-in-time-Registration](../../../iot/latest/developerguide/auto-register-device-cert.md "../../../iot/latest/developerguide/auto-register-device-cert.md") by registering the Certificate Authority (CA) that
issued the certificate.

- **Validate**

Client certificates presented by ECUs are validated by the connected vehicle
service as part of the mutual TLS handshake. This process includes checking that the
certificate has not expired, validating the certificate chain to verify the certificate
is issued by a trusted Certificate Authority, checking for certificate revocation (see
below), and checking the certificate against an asset database to check that it is an
authentic and active ECU. AWS IoT verifies that a [client
certificate is active](../../../iot/latest/developerguide/activate-or-deactivate-device-cert.md "../../../iot/latest/developerguide/activate-or-deactivate-device-cert.md") when it authenticates a connection. You can create and
register client certificates without activating them so they can't be used until you
want to use them. You can also deactivate active client certificates to disable them
temporarily.

- **Renew**

Each X.509 certificate has a validity period (determined by the Not Before and Not
After fields) that is checked by servers before accepting the certificate as valid. One
strategy to avoid renewing is to issue certificates with a long validity period - such
as 100 years - that is beyond the expected service lifetime of the ECU using the
certificate. This strategy then relies entirely on the revocation process (see below) to
manage the validity of certificates. A second strategy is to issue certificates with a
medium validity period - typically 1 to 3 years. A third strategy is to issue
short-lived certificates - typically a few hours or days - especially for cases where it
is important to prevent tracking and attribution that can happen with static long-lived
certificates. In the latter two strategies, it is important to have a secure process for
renewing certificates **before** they expire. This process
must be secured to the same degree as the process used to originally issue and provision
certificates. On AWS, [AWS IoT Device Defender](../../../iot/latest/developerguide/device-defender.md "../../../iot/latest/developerguide/device-defender.md") periodically
audits client certificates registered in IoT Core and publishes findings for [certificates that are expiring](../../../iot/latest/developerguide/audit-chk-device-cert-approaching-expiration.md "../../../iot/latest/developerguide/audit-chk-device-cert-approaching-expiration.md") within the next 30 days. You can send the
findings to a remediation workflow in [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/"), using Lambda functions and [IoT Jobs](../../../iot/latest/developerguide/iot-jobs.md "../../../iot/latest/developerguide/iot-jobs.md") to trigger the ECU to
generate a new CSR, issue a new certificate, and send the new certificate to the ECU.
Once the ECU has successfully installed and tested the new operational certificate, the
workflow can revoke the old expiring certificate in IoT Core.

- **Revoke**

When you detect a security issue with a certificate (such as the private key is
compromised) or are notified that the ECU has been replaced, you may choose to
permanently revoke the certificates associated with the ECU. Certificates are revoked by
invoking the CA that issued the certificate. The CA publishes the revocation status of
certificates via Certificate Revocation Lists (CRLs) or via Online Certificate Status
Protocol (OCSP) or both. Connected vehicle services that validate client certificates
must check whether the certificate is revoked using the CA's supported method before
accepting the certificate as valid. [AWS Private CA supports both CRL and
OCSP](../../../privateca/latest/userguide/revocation-setup.md "../../../privateca/latest/userguide/revocation-setup.md") as revocation methods, and this [blog post](https://aws.amazon.com/blogs/security/choosing-the-right-certificate-revocation-method-in-acm-private-ca/ "https://aws.amazon.com/blogs/security/choosing-the-right-certificate-revocation-method-in-acm-private-ca/") helps you choose the best method for your use-cases. You can also
revoke a certificate that was previously registered in IoT Core and this denies
connections that use that certificate.

- **Retire**

Finally, when the ECU has reached its end of life or has been replaced and you no
longer want the certificates to be trusted, you can choose revoke the certificate (see
above) and delete the certificate from your asset database. This will help validate that
no future connections or requests from the ECU are accepted by connected vehicle
services. IoT Core allows you to delete a [Thing](../../../iot/latest/apireference/API_DeleteThing.md "../../../iot/latest/apireference/API_DeleteThing.md") and [certificates](../../../iot/latest/apireference/API_DeleteCertificate.md "../../../iot/latest/apireference/API_DeleteCertificate.md").

**[CMSEC\_BP3.2] Design and securely operate a PKI for vehicle
identities**

The previous section described how vehicle identities are often X.509 certificates issued by a
vehicle Private Key Infrastructure (PKI). The security of a scheme that relies on X.509
certificates for authentication and authorization depends on the security of the PKI that
issues the certificates. It is important to start by documenting your policies and practices
for operating your PKI including details of your Certificate Authority (CA) structure,
policies for the validity period of your CAs, the process for succession of CAs, description
of the administrative permissions and controls, roles and responsibilities. You can capture
this information in two documents, known as Certification Policy (CP) and Certification
Practices Statement (CPS). Refer to [RFC
3647](https://www.ietf.org/rfc/rfc3647.txt "https://www.ietf.org/rfc/rfc3647.txt") for a framework for capturing important information about your PKI
operations.

Minimize the use of the root CA to only issue certificates for intermediate CAs. Store the
private key of the root CA in a secure Hardware Security Module (HSM) and tightly control
physical and logical access.

In some circumstances, as an OEM you may need to share parts of your PKI with suppliers and vendors.
example, you may create an intermediate CA for a supplier and allow that supplier to issue attestation and
operational certificates that are embedded in ECUs during manufacturing. In this case, you are relying on the policies and
processes of your supplier for the security of the ECU's identities. Review the supplier's Certification Policy (CP) and Certification Practices Statement (CPS)
to check that these meet your overall PKI requirements.

You can use [AWS Private CA](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md") to create, manage, and operate a vehicle PKI on AWS. PCA allows you to
create a [CA structure with multiple levels and gives you fine-grained control over each CA](https://aws.amazon.com/blogs/security/how-to-secure-an-enterprise-scale-acm-private-ca-hierarchy-for-automotive-and-manufacturing/ "https://aws.amazon.com/blogs/security/how-to-secure-an-enterprise-scale-acm-private-ca-hierarchy-for-automotive-and-manufacturing/")
and whether and how it is shared with other entities such as suppliers.

**[CMSEC\_BP3.3] Design a mechanism to tie various vehicle identities
together as necessary**

As described in CMSEC_BP3.2, a vehicle will have several identities, multiple
identities per ECU and multiple identities for the vehicle. Based on your application needs,
you may require the ability to tie these identities together so that you can map an
authenticated ECU identity to its ECU ID or serial number, and to the vehicle's VIN where
the ECU is installed. You can maintain an asset database that stores a record of the
different identities and their relationships. Because this database stores sensitive
information that can be used to identify, relate, and track identities, the database must be
secured and all accesses to the database must be authenticated, authorized, and audited. To
protect the privacy of your vehicles, owners and operators, check that only authorized staff
have access to this database and unauthorized or unusual query patterns are detected and
alerts are sent to the data owners. The asset database must be updated with changes such as
when certificates are renewed (see above) and ECUs are replaced in repair shops. Verify that
only authorized staff are allowed to update the database and changes are tracked and
associated with authorized work orders or repair bills of material.

**[CMSEC\_BP3.4] Define a mechanism for how your vehicles will be
identified towards external entities**

You may have use-cases where you need to send information about your vehicles and ECUs to
external entities such as business partners (dealers, suppliers, repair shops, and vehicle
insurance providers or example). Consider designing a mechanism that maps stable unique
identifiers, such as VIN and ECU Serial Number (ESN), to anonymized or temporary identities
so that you can preserve the privacy of your vehicles, owners, and operators and prevent
unauthorized or unintended sharing of information with your partners. You may choose to
create a mapping database that stores the mapping from stable identifiers to the anonymized
or temporary identifiers sent to your partners. Validate that such a mapping database has
strong authentication, access control, audit and logging.

On AWS, you can choose from a number of [fully managed purpose-built database services](https://aws.amazon.com/products/databases/ "https://aws.amazon.com/products/databases/") to store mappings.

| CMSEC_4: How do you manage the identities of the owners, drivers, and operators<br>of your vehicles and map them to the vehicle's identities? |
| --------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                               |

Connected vehicle services often need information on the identities of users: owners, drivers, and operators of the
vehicles to provide service features corresponding to the user. For example, a vehicle is being driven by a teenaged family
member that is not the vehicle owner. The vehicle IVI invokes a personalization service to get the preferences of both the
owner and the family member to apply personalized preferences and restrictions. The teenaged driver is restricted to a top
speed limit configured by the vehicle owner but is able to see their favorite music applications on the IVI home screen.

To implement such features, the vehicle ECUs must recognize and identify the current driver, and the connected vehicle service
must authenticate and authorize requests based on the identities of the current driver and owner and other contextual
information such as the time of the day.

Consider the following best practices when managing the identities of owners, drivers and
operators of your vehicles.

**[CMSEC\_BP4.1] Design an authentication mechanism for users of your
vehicles**

Design an authentication mechanism for users of your vehicles based on the
sensitivity and risk of the actions being performed. For example, unlocking a vehicle is a
high-risk action and should require the use of a physical key fob or a digital key from an
application on a phone. Setting IVI home screen preferences may be a low-risk action and may
be acceptable to use factors such as facial recognition of the driver. This allows physical
key fobs to be shared between family members but still recognizes the current driver of the
vehicle. The driver of a delivery vehicle that is part of a fleet is authenticated using an
application on a hand-held scanner device. The fleet operator uses the identity to track the
driver of each vehicle and the routes taken for safety, efficiency, and audit purposes.

In contrast to vehicle ECUs that are typically authenticated and authorized using X.509
certificates (see CMSEC3_BP5 regarding designing a PKI for vehicle identities), users are
usually authenticated using tokens. Consider using an identity provider that supports widely
adopted identity standards such as [OpenID
Connect](https://openid.net/connect/ "https://openid.net/connect/") (built on [OAuth 2.0](https://oauth.net/2/ "https://oauth.net/2/")) to
authenticate your users and generate tokens. OpenID Connect identity providers issue [JSON Web Tokens (JWT)](https://jwt.io/ "https://jwt.io/") that are cryptographically signed by
the identity provider and delivered to the in-vehicle ECUs that make requests to connected
vehicle services on behalf of the user. The ECUs provide the Java Web Tokens (JWTs) as part
of the request for example in the HTTPS request header and the tokens can be validated on
the connected vehicle service to authenticate the request, and the request is authorized
based on claims and scopes in the token. Because tokens are used directly to authenticate
requests to services, check that tokens are stored securely on ECUs and are not exposed to
unauthorized users. Consider the token lifecycle, using short-lived tokens to limit the
impact of an exposed token, use refresh tokens to obtain new tokens without requiring user
interaction, and revoke the token when you detect that a token is compromised.

Because the in-vehicle user interfaces such as the IVI may be limited in terms of user input
capabilities - lacking a physical keyboard for example asking the user to type a long,
complex password on a touch-screen may be impractical and error prone. In such cases,
consider implementing the OAuth 2.0 [Device Authorization grant](https://www.rfc-editor.org/rfc/rfc8628 "https://www.rfc-editor.org/rfc/rfc8628") (also called Device Flow) that allows devices that
have no built-in browser or limited input capability to get an access token by using a
browser on a different device such as a mobile phone or desktop. The user interacts with the
browser on the phone or desktop to authenticate to the identity provider and grant access to
the IVI.

You can build and operate your own identity provider or use a cloud SaaS identity provider.
[_Amazon Cognito_](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/") is a fully
managed identity provider that allows you to add user sign-up and sign-in features and
control access to your web and mobile applications. [Amazon Cognito user pools](../../../cognito/latest/developerguide/cognito-user-identity-pools.md "../../../cognito/latest/developerguide/cognito-user-identity-pools.md")
provides an identity store that scales to millions of users, supports social and enterprise
identity federation, and offers advanced security features to protect your consumers and
business. You can implement [Device Authorization grant using Cognito and AWS Lambda](https://aws.amazon.com/blogs/security/implement-oauth-2-0-device-grant-flow-by-using-amazon-cognito-and-aws-lambda/ "https://aws.amazon.com/blogs/security/implement-oauth-2-0-device-grant-flow-by-using-amazon-cognito-and-aws-lambda/"). AWS services such as
[Application Load Balancer](../../../elasticloadbalancing/latest/application/listener-authenticate-users.md "../../../elasticloadbalancing/latest/application/listener-authenticate-users.md") (ALB), [API Gateway](../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md "../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md"), [AppSync](../../../appsync/latest/devguide/security-authz.md "../../../appsync/latest/devguide/security-authz.md"), and [IoT
Core](../../../iot/latest/developerguide/cognito-identities.md "../../../iot/latest/developerguide/cognito-identities.md") can authenticate and authorize requests using tokens issued by Cognito User
Pools.

**[CMSEC\_BP4.2] Consider patterns for mapping a user's identity to the
vehicle's identities**

The connected vehicle service will often need to map between
the user's identity and vehicle's identities to provide
service features. For example, a personalization service needs
to know the identity of the current driver, the owner, and of
the vehicle's ECUs to respond with the corresponding policies
and preferences.

One approach is to combine two authentication schemes:

- **Vehicle ECUs:** Use X.509 client certificates to
  authenticate vehicle ECUs when they connect to a connected vehicle service using mTLS,
  and
- **Users:** Send JWT access or ID tokens in the request
  (over mTLS) as HTTPS headers or the MQTT payload to authenticate users to a connected
  vehicle service.
  This approach inherently maps the user's identity to the vehicle ECU's identity and your backend service can validate each
  identity cryptographically. The backend service can use the ECU's identity to query an asset database for information such as the
  owner or operator of the vehicle.

Consider how mapping information is updated over the lifecycle of the vehicle. For example, information about the owner of a vehicle
must be updated in the asset database when a vehicle is sold.

Validate that access to the mapping between users and vehicles is stored securely and access to this mapping is restricted to
applications and administrators on a need-to-know basis.

| CMSEC_5: How do you manage the identities of your business partners, such as<br>dealers, suppliers, service providers, or other third parties? |
| ---------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                |

Connected vehicle services operate in a rich environment with multiple business partners such as dealers, suppliers,
repair shops, and service providers, to name only a few. In addition to managing the identities of your vehicles and users
it is equally important to manage the identities of your business partners that interact with connected vehicle services.
For example, a dealer for an OEM uses a connected vehicle service to set the owner for a vehicle when a vehicle is sold. As
this operation has security and safety implications, the dealer must be authenticated and authorized to perform this operation,
and all actions must be logged and audited.

Consider the following best practices to manage the identities of your business partners.

**[CMSEC\_BP5.1] Separate identities of your external partners from
internal employees and contractors**

It is very common for a single connected vehicle service to have multiple types of users that interact with it: vehicle
drivers, owners, business partners, employees, and contractors. Consider creating strict segregation boundaries between the
identities of your employees and contractors on one side, and business partners on the other.

You can implement this separate by creating separate identity provider pools (also called domains, directories, or tenants - the
terminology depends on the identity provider software or service you are using) for the two types of users. This approach has the following benefits:

- Each identity provider pool can have different security policies such as whether
  user sign-ups are allowed, password strengths enforced, and the use of multi-factor
  authentication (MFA).
- You can configure federation for the employee identity
  pool only to your corporate identity provider, allowing
  your employees to single-sign on to your custom
  applications.
- User tokens contain a unique issuer element and are signed
  by a key that is unique to the identity provider pool.
  This provides a cryptographic way to validate that a
  particular identity originates from a particular pool.
  On AWS, you can separate different types of users into separate [Cognito User Pools](../../../cognito/latest/developerguide/cognito-user-identity-pools.md "../../../cognito/latest/developerguide/cognito-user-identity-pools.md") and configure each pool with different properties and
  policies.

**[CMSEC\_BP5.2] Verify that application authorization is based on the
type of identity**

The simplest way to implement this is to segregate the identities into separate identity provider pools and have each connected
vehicle service API explicitly trust each identity provider pool to authenticate users from that pool. For example, your dealer-facing
APIs trust the dealer identity pool, but your employee facing APIs trust only the employee identity pool. A token issued to a dealer
from the dealer identity pool cannot be used to authenticate requests to the employee APIs, because the token validation fails.

A single API resource that trusts both the employee and business partner identity pools should be considered an exception. The
configuration and code of such an API must be closely reviewed to check that authorization is appropriately granted to each type of user.

As you design your application authorization scheme, verify that only information contained in a cryptographically verified token
(such as a JWT) or information queried from a trusted backend database is used for the authorization decision. Do not rely on
information for authorization that can be spoofed such as query parameters, the request body, or unsigned browser cookies that cannot
be cryptographically verified by the server for authenticity and integrity.

On AWS, you services such as [Application Load Balancer](../../../elasticloadbalancing/latest/application/listener-authenticate-users.md "../../../elasticloadbalancing/latest/application/listener-authenticate-users.md") (ALB), [API Gateway](../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md "../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md"), [AppSync](../../../appsync/latest/devguide/security-authz.md "../../../appsync/latest/devguide/security-authz.md"), and [IoT
Core](../../../iot/latest/developerguide/cognito-identities.md "../../../iot/latest/developerguide/cognito-identities.md") can be configured to authenticate tokens issued by specific Cognito User
Pools. With API Gateway, you can also implement custom authorization logic using [_Lambda authorizers_](../../../apigateway/latest/developerguide/apigateway-use-lambda-authorizer.md "../../../apigateway/latest/developerguide/apigateway-use-lambda-authorizer.md").

| CMSEC_6: How do you manage access permissions to vehicle functions? |
| ------------------------------------------------------------------- |
|                                                                     |

In the context of connected vehicle services, privileged actions are those that are initiated from the backend and can impact the safety and
security of the vehicle. For example, an owner speaks to a customer support agent in a call center and requests a remote unlock of their vehicle
because they lost their physical key fob. In another example, the driver of a vehicle authorizes the OEM's support engineers to remotely diagnose
and fix issues with their vehicle. As is evident in both these examples, the actions initiated from connected vehicle services backends can directly
impact the safety, security, and operation of the vehicle. Permissions to perform these actions must be carefully managed and audited.

The first step is to identify the use-cases that involve restricted or administrative actions
and focus on implementing the following best practices to manage accesses to those
actions:

**[CMSEC\_BP6.1] Define a process for support staff to gain permissions
to perform administrative actions on vehicle functions**

The process that your support staff (such as engineers, and customer support agents)
follow to gain permissions to perform administrative actions must require appropriate
approvals and traceability to the context of the request, for example, the customer support
case ID or trouble ticket that corresponds to the access request. Access to human actors
must be granted for a limited time and for specific actions on specific ECUs: such as grant
the ability to remotely collect logs and diagnostic data from a specific vehicle's battery
management ECU for the next 30 minutes. Access must be granted only after obtaining required
approvals from managers and after passing validation rules: such as verify that the ECU ID
in the support case is the same as the ECU ID for which access is being requested, and the
support engineer is indeed on call for the current shift, and they belong to the appropriate
security groups in your directory. For highly sensitive and impactful actions, consider
implementing quorum approval processes (also called M of N approvals) where multiple
managers or peers must review and approve an access request before access permissions are
granted. It is recommended that this process is automated and based on requestor
entitlements to avoid the risk of collusion.

**[CMSEC\_BP6.2] Implement fine-grained audit logging of every
privileged action on vehicles**

Validate that every privileged action on vehicles, whether initiated by a human actor or by an
automated system, is logged with details such as the identity of the human or system actor,
the timestamp, the action performed, the target of the action (for example, ECU ID, and
Vehicle ID) and the result of the action. Verify also that each step in the process to gain
access is also logged (request, review, approval, grant), so it can be audited and tracked.
Design a mechanism that protects the integrity of access audit logs by denying permissions
to modify, delete or overwrite log events, and by appending cryptographic signatures to log
events that can be used to verify their integrity. You must also check that the log events
are indexed and searchable for later audit and analysis.

A centralized logging solution is needed that aggregates and indexes such audit log events
from your fleet of compute servers. You can deploy and manage a log collection and indexing
solution or you can use a managed SaaS service. [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") enables you to
centralize the logs from all of your systems, applications, and AWS services that you use,
in a single, highly scalable service. You can then easily view them, search them for
specific error codes or patterns, filter them based on specific fields, or archive them
securely for future analysis. CloudWatch Logs also supports querying your logs with a powerful query
language, auditing and masking sensitive data in logs, and generating metrics from logs
using filters or an embedded log format. (See CMSEC_BP11.1)

**[CMSEC\_BP6.3] Alert on unauthorized attempts to access privileged
actions on high-risk ECUs**

In addition to generating fine-grained audit log events for every privileged action
(see above), consider creating automated alert notifications when unauthorized attempts to
access privileged actions on high-risk ECUs such as the IVI or Head Unit. For example, you
can create a rule that triggers an alert notification when a single support staff performs
privileged actions on multiple ECUs in a short period of time. This can trigger your Vehicle
Security Operations Center (VSOC) to investigate the alert to determine if this is a case
of compromised credentials or identity being used in an unauthorized manner. (See CMSEC_BP22.1)

| CMSEC_7: How do you verify that vehicles are granted least privilege access to<br>perform actions on your backend systems? |
| -------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                            |

As your vehicle ECUs make requests to connected vehicle services, you must check that each ECU is authorized to
perform the smallest set of actions that it needs to fulfill its function. For example, you may want to authorize an ECU to
publish telemetry data to a MQTT topic named with its ECU ID, and to subscribe to real-time road condition updates from another
topic if the vehicle owner has subscribed to a premium service.

Consider the following best practices to grant least privilege authorization to ECUs:

**[CMSEC\_BP7.1] Authorize every action taken by a vehicle ECU
individually.**

Validate that every action taken by a vehicle's ECU on your connected vehicle services is authorized individually. You can use the
identity of the ECU you defined in CMSEC_3 to define the baseline policies that grant specific actions to the ECU. You can enhance these
policies to grant or deny other actions based on dynamic context conditions such as the time of the day, location of the vehicle, and
state of subscription services.

You may consider externalizing the authorization policy evaluation logic into a shared, centralized policy evaluation service where policies
can be written in a domain specific language (DSL) such as [Cedar](https://www.cedarpolicy.com/en "https://www.cedarpolicy.com/en"), that is easier to
author, understand and audit than programming language code. [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/ "https://aws.amazon.com/verified-permissions/")
is a scalable permissions management and fine-grained authorization service for the applications that you build. Amazon Verified Permissions uses the Cedar
open-source policy language This pattern splits the responsibilities for authorization: the connected vehicle service is responsible for gathering the
identity and context information and providing it to the policy evaluation service. The policy evaluation service implements the logic to parse the policy
DLS and respond with a allow or deny decision to the connected vehicle service. This pattern also splits the responsibilities of the team that authors
policies in the DLS from the developers that write the code for your connected vehicle service, allowing each team to be more efficient and deploy
changes at their own pace.

You can authorize requests on the connected vehicle services backends based on scopes in
access tokens, or fields from X.509 certificates. Several AWS services offer built-in
authorization features allowing you to define policies that control access to the service's
data plane. [AWS IoT Core](../../../iot/latest/developerguide/what-is-aws-iot.md "../../../iot/latest/developerguide/what-is-aws-iot.md") allows you to define [IoT Core Policies](../../../iot/latest/developerguide/iot-policies.md "../../../iot/latest/developerguide/iot-policies.md") that control
the actions a device connected to IoT Core can perform. You can attach policies to each
client X.509 certificate and to [Thing Groups](../../../iot/latest/developerguide/thing-groups.md "../../../iot/latest/developerguide/thing-groups.md") to control access
at multiple levels. [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") provides
[multiple ways
to control access to a REST API](../../../apigateway/latest/developerguide/apigateway-control-access-to-api.md "../../../apigateway/latest/developerguide/apigateway-control-access-to-api.md"). Specifically, the API Gateway [Lambda
authorizer](../../../apigateway/latest/developerguide/apigateway-use-lambda-authorizer.md "../../../apigateway/latest/developerguide/apigateway-use-lambda-authorizer.md") allows you to implement your custom business logic in Lambda function
code and return a policy that API Gateway will cache and use to authorize future requests. [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/ "https://aws.amazon.com/verified-permissions/") is a scalable, fine-grained
permissions management and authorization service for custom applications. The service
centralizes fine-grained permissions for custom applications and helps developers authorize
user actions within applications. Amazon Verified Permissions uses the [_Cedar_](https://www.cedarpolicy.com/ "https://www.cedarpolicy.com/") policy language to
define fine-grained permissions for application users.

| CMSEC_8: How do you validate that your backend systems have least privilege<br>access to perform actions on vehicle functions? |
| ------------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                |

As you design connected vehicle service backend systems, validate that each system is only granted the smallest set of
permissions to perform actions on vehicles. This is especially important for CMSEC_7 regarding privileged access, as this is
critical for backend systems that initiate privileged actions on vehicles because it can impact the safety, security, and operations of the vehicle.

Consider the following best practices:

**[CMSEC\_BP8.1] Verify your backend systems are authenticated and
authorized for every action on vehicle functions.**

Implement secure authentication and authorization of every request from a backend system that results in actions on vehicles.
For example, a customer support uses a customer support application to initiate remote door unlock on behalf of the vehicle owner
who has lost their keys. In this scenario, check that the customer support agent is authenticated and authorized to perform the action,
and verify that the support application is authenticated and authorized to perform the unlock action on a connected vehicle service.

In another example, your software administrator has scheduled the roll-out of an Over the Air software update to a fleet of vehicles.
An OTA service executes this update by sending commands to each vehicle in the fleet to download the update files securely from an update service.
The OTA service must be authenticated and authorized before it is allowed to such a command to a vehicle ECU.

In both of the previous examples, one service interacts with another service to perform an
action on a vehicle. This is a type of machine-to-machine communication where the calling
service must be authenticated and authorized by the called service. You can choose several
approaches to [authenticate machine-to-machine application scenarios](https://aws.amazon.com/blogs/security/approaches-for-authenticating-external-applications-in-a-machine-to-machine-scenario/ "https://aws.amazon.com/blogs/security/approaches-for-authenticating-external-applications-in-a-machine-to-machine-scenario/").

On AWS, you can choose [AWS Signature v4 (sigv4)](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md")
that is supported by all AWS API endpoints, and can be used to authenticate and [authorize requests to your custom APIs created in API Gateway](../../../apigateway/latest/developerguide/http-api-vs-rest.md#http-api-vs-rest.differences.authorization "../../../apigateway/latest/developerguide/http-api-vs-rest.md#http-api-vs-rest.differences.authorization"). You can use [sigv4 with
AWS IoT Core](../../../iot/latest/developerguide/protocols.md "../../../iot/latest/developerguide/protocols.md") to authenticate and authorize actions such as publish and subscribe to
MQTT topics using MQTT over WebSocket. If the backend service is deployed to AWS, you can
associate an IAM Role with the AWS compute service (for example, [Amazon EC2](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md"), [Lambda functions](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md"), [Amazon ECS](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md"), Amazon EKS) that provides temporary security credentials that can be used by
the backend service to sign sigv4 requests. If the backend service is deployed outside
AWS, consider using [IAM Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md") as the
mechanism to obtain temporary security credentials in exchange for X.509
certificates.

**[CMSEC\_BP8.2] Implement fine-grained audit logging of actions
performed by your backends on vehicle functions**

It is important to implement fine-grained audit logging of actions performed by your backend services on vehicle functions.
Having such an audit log will help you with operational troubleshooting and as security incident response investigations.

You can implement audit logging in your connected vehicle service by emitting log events when actions are invoked. You can
centrally aggregate and store these log events in a Security Incident and Event Management (SIEM) system that indexes the
events and allows you to search and create dashboards and visualizations of these events.

On AWS, consider enabling the built-in logging features of AWS services that you use to
implement your backend services. Enable [AWS IoT logging](../../../iot/latest/developerguide/configure-logging.md "../../../iot/latest/developerguide/configure-logging.md") to
deliver [log
entries](../../../iot/latest/developerguide/cwl-format.md "../../../iot/latest/developerguide/cwl-format.md") to [_CloudWatch Logs_](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") for
events on the IoT service such as a connect, publish, subscribe, and many others. You can
enable [CloudWatch logs for your custom APIs
in API Gateway](../../../apigateway/latest/developerguide/set-up-logging.md "../../../apigateway/latest/developerguide/set-up-logging.md") to get both execution logging and access logging events delivered to
CloudWatch Logs. Consider ingesting these log events from CloudWatch Logs into your SIEM tool to be indexed and
analyzed. Or consider implementing the [centralized
logging with OpenSearch](../../../solutions/latest/centralized-logging-with-opensearch/welcome.md "../../../solutions/latest/centralized-logging-with-opensearch/welcome.md") solution.
