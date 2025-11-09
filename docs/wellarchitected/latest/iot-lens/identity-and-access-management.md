# Identity and access management

IoT devices frequently face elevated security risks. There are
several reasons for this. Devices are often provisioned with a
trusted identity. Devices may store or have access to strategic
customer or business data (such as the firmware itself). Devices
may be remotely accessible over the internet. Devices may be
subject to to direct physical tampering. To provide protection
against unauthorized access, you need to always begin with
implementing security at the device level. From a hardware
perspective, there are several solutions that you can implement to
reduce the risk of tampering with sensitive information on the
device such as:

- Hardware crypto modules
- Software-supported solutions including secure flash
- Physical function modules that cannot be cloned
- Up-to-date cryptographic libraries and standards including
  PKCS #11 and TLS 1.2/1.3

To secure device hardware, you should implement solutions so that
private keys and sensitive device identity information are unique
to a device and stored only in a secure hardware location on the
device. You should implement unique device identities using
public-private key pairs. An X.509 certificate containing a public
key represents the identity of the device. The corresponding
private key is used by the device to prove that it corresponds to
that identity. Implement hardware or software-based modules that
securely store and manage access to the device's private key
corresponding to its public key and X.509 certificate. FreeRTOS,
AWS IoT Greengrass, and the AWS IoT Device SDKs support this
through the use of PKCS#11. In addition to hardware security, IoT
devices must be given a valid identity, which will be used for
authentication and authorization in your IoT application.

During the lifetime of a device, you will need to be able to
manage certificate request, renewal and revocation, as well as
update device firmware and software. To handle these changes, you
must first have the ability to update a device in the field. The
ability to perform firmware updates, software updates and
configuration updates on hardware is a vital underpinning to a
well-architected IoT application. Through over the air (OTA)
updates, you can securely rotate device certificates before
expiry. OTA can also be used to update trusted certificate
authorities and update firmware and software.

For example, with AWS IoT, you first provision a X.509 certificate
identifying the device and then separately create the IoT
permissions for connecting to AWS IoT Core, publishing and
subscribing to messages, and receiving updates. This separation of
identity and permissions provides flexibility in managing your
device security. During the configuration of permissions, you can
make sure that the device has the correct identity
(authentication) as well as the right level of access control
(authorization) by creating an IoT policy that restricts access to
MQTT actions for each device.

Make sure that each device has its own unique X.509 certificate.
Each device should have a unique public-private key pair. The
private key should, if possible, be generated on the device and
never leave the secure storage area where it was generated on the
device. Devices should never share keys or certificates used for
identification (one certificate for one device rule). In addition
to using a single key or certificate per device, each device must
have its own unique thing identifier in the IoT registry. In AWS IoT Core, by default, the thing name is used as the basis for the
MQTT ClientID for MQTT connect. It is possible to separate Thing
name and ClientID if necessary.

Every X.509 certificate has an expiration. This includes
certificates representing certificate authorities, including root
certificate authorities. Devices must support the replacement of
trusted root and intermediate certificate authorities. Devices
must also support refresh and replacement of the certificate,
which represents the identity of the device. This helps to support
continued operation of the device including the ability to
authenticate to AWS IoT Core.

By creating this association where a unique key or certificate is
paired with each thing in AWS IoT Core, you can make sure that one
compromised certificate cannot inadvertently assume an identity of
another device. It also assists in logging (auditing),
troubleshooting and remediation of incidents. If the MQTT ClientID
and the thing name are different, you must plan to have a way to
correlate between thing name and ClientID. This is necessary to
work with log messages associated with device communication.

To support device identity updates, use AWS IoT Jobs. AWS IoT Jobs
is a managed service for distributing OTA updates and binaries to
your devices. AWS IoT Jobs is used to define a set of remote
operations that are sent to and executed on one or more devices
connected to AWS IoT Core. AWS IoT Jobs by default integrate
several best practices, including mutual authentication and
authorization, device tracking of update progress, logging or
auditing, and fleet-wide wide metrics for jobs that are scheduled
to be run across fleets of devices.

Use native provisioning mechanisms to onboard devices when they
already have a device key or certificate provisioned onto them.
For example, you can use just-in-time provisioning (JITP) or
just-in-time registration (JITR) that provisions devices when they
first connect to AWS IoT Core.

If the devices cannot use X.509 certificates, or you have an
existing fleet of devices with a proprietary authentication or
access control mechanism, use custom authentication or
authorization mechanisms. One example of this is the use of bearer
tokens such as OAuth over JWT or SAML 2.0 tokens for
authenticating communications. For example, a device which sends a
JSON web token (JWT) generated by their identity provider in the
HTTP header or query string when it attempts to connect to AWS IoT Core. The signature, validity, issuer, and audience of the JWT (in
addition to other custom claims) must be validated by an AWS IoT
custom authorizer before the connection is established.

It is important to use a standard set of naming conventions when
designing device names and MQTT topics. For example, we recommend
using the same client identifier for the device as the IoT Thing
Name. This will also allow to include relevant routing information
for the device in the topic namespace.

Enable AWS IoT Device Defender audits to track device
configuration, device policies, and checking for expiring
certificates in an automated fashion. For example, AWS IoT Device Defender can run audits on a scheduled basis and initiate a
notification for expiring certificates. With the combination of
receiving notifications of revoked certificates or certificates
nearing expiration, you can automatically schedule an OTA update
using AWS IoT Jobs that can proactively rotate or refresh the
certificate.

| IOTSEC01: How do you associate IoT<br>identities and permissions with your devices? |
| ----------------------------------------------------------------------------------- |
|                                                                                     |

Your application is responsible for managing how your devices
authenticate and authorize their interactions. By creating a
process that makes sure devices have a unique identity and
identity-based permissions for accessing the IoT system, you
establish the greatest control for managing device interactions.

## IOTSEC01-BP01 Assign unique identities to each IoT device

When a device connects to other devices or cloud services, it
must establish trust by authenticating using credentials such as
X.509 certificates (with proof of having the private key) or
security tokens. You can find available options from the IoT
solution of your choice, and implement device registry and
identity stores to associate devices, metadata and user
permissions. The solution should enable each device (or Thing)
to have a unique name (or ThingName) in the device registry, and
the solution should make sure that each device has an associated
unique identity principal, such as an X.509 certificate or
security token. Identity principals, such as certificates,
should not be shared between devices. Detection of multiple
devices using the same identity credentials indicates an issue
that requires investigation. This could be due to improper
device setup or potential unauthorized cloning of device
credentials.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC01-BP01-01** _Use X.509 client
certificates to authenticate over TLS 1.2/1.3._

We recommend that each device be given a unique key or certificate
to enable fine-grained device management, including certificate
revocation. Devices must support rotation, refresh, and
replacement of certificates to support continued operation. For
example, AWS IoT Core supports AWS IoT-generated X.509
certificates or your own X.509 certificates for device
authentication.

**Prescriptive guidance
IOTSEC01-BP01-02** _Choose the appropriate
certificate vending mechanisms for your use case._

We recommend using native provisioning mechanisms to onboard
devices when they already have a device certificate (and
associated private key) on them. For example, you can use
just-in-time provisioning (JITP) or just-in-time registration
(JITR) that provisions devices when they first connect to AWS IoT.

**Prescriptive guidance
IOTSEC01-BP01-03** _Use security bearer tokens
only if necessary._

If the devices cannot use X.509 certificates, or you have an
existing fleet of devices with a proprietary access control
mechanism that requires use of bearer tokens such as OAuth with
JWT or SAML 2.0 tokens, use custom authentication mechanisms. For example,
when a device attempts to connect to AWS IoT, it sends a JWT
which was generated by their identity provider in the HTTP
header or query string of requests. The token is validated by
AWS IoT custom authorizer and the connection is established. All
communications must be performed over TLS-protected (encrypted)
connections using strong cipher-suites.

**Prescriptive guidance
IOTSEC01-BP01-04** _Use a consistent naming
convention that aligns MQTT topics with your device
identity._

It is important to use a standard set of naming conventions when
designing device names and MQTT topics. For example, we
recommend using the same client identifier (`ClientId`) for the
device as the IoT Thing Name (`ThingName`). This will also
simplify the design for including relevant routing information
for the device in the topic namespace.

| IOTSEC02: How do you secure your devices<br>and protect device credentials? |
| --------------------------------------------------------------------------- |
|                                                                             |

Your IoT devices and identity credentials (certificates, private
keys, or tokens) must be secured throughout their lifecycle. To
support device authenticity, your IoT hardware must securely
store, manage, and restrict access to the identities that the
device uses to authenticate itself with the cloud. By securing
your devices and storing your device credentials safely, you can
reduce the risk of unauthorized users misusing device
credentials.

## IOTSEC02-BP01 Use a separate hardware or a secure area on your devices to store credentials

A secure element (SE) is any hardware feature you can use to
protect information on the device. A common use of an SE is to
securely store the device's identity. Secure storage at rest
helps reduce the risk of unauthorized use of the device
identity. Never store or cache device credentials outside of the
SE. If supported, generate public or private key pairs using the
SE, and generate the Certificate Signing Requests (CSRs) on the
device. With this method, the private key never leaves the SE.
If this is not possible, generate and transmit the credentials
to the SE in a secure manufacturing facility with Common
Criteria EAL certification. Import or install the private key
material into the SE in the secure facility. Securely handling a
device's identity helps make sure that your hardware and
application are resilient to potential security issues that
occur in unprotected systems. A SE provides encrypted storage of
private information (such as cryptographic keys) at rest and can
be implemented as separate specialized hardware or as part of a
system on a chip (SoC).

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC02-BP01-01** _Use tamper-resistant
hardware that offloads the cryptographic operations for
encryption and communication from the IoT
application._

Device credentials must always reside in a SE, which facilitates
usage of the credentials. Using the SE to facilitate the use of
device credentials further limits the risk of unauthorized use.
As an example, AWS IoT Greengrass supports using a SE to store
AWS IoT certificates and private keys.

**Prescriptive guidance
IOTSEC02-BP01-02** _Use cryptographic API
operations provided by the secure element hardware for
protecting the secrets on the device._

Only access security modules using the latest security
protocols. For example, in FreeRTOS, use the PKCS#11 APIs
provided in the corePKCS11 library for protecting secrets.

**Prescriptive guidance
IOTSEC02-BP01-03** _Use the AWS Partner Device
Catalog to find AWS Partners that offer hardware security
modules._

If you are getting devices that have not been deployed in the
field, AWS recommends reviewing the AWS Partner Device Catalog
to find AWS IoT hardware partners that either implement a SE or
trusted platform module (TPM). Use AWS IoT Partners that offer
qualified SEs for storing IoT device identities.

## IOTSEC02-BP02 Use a trusted platform module (TPM) to implement cryptographic controls

Generally, a TPM is used to hold, secure, and manage
cryptographic keys and certificates for services such as disk
encryption, Root of Trust booting, verifying the authenticity of
hardware (as well as software), and password management. The TPM
has the following characteristics:

1. TPM is a dedicated crypto-processor to help make sure the
   device boots into a secure and trusted state.
2. The TPM chip contains the manufacturer's keys and software
   for device encryption.
3. The Trusted Computing Group (TCG) defines
   hardware-roots-of-trust as part of the Trusted Platform
   Module (TPM) specification.

A hardware identity refers to an immutable, unique identity for
a platform that is inseparable from the platform. A hardware
embedded cryptographic key, also referred to as a hardware root
of trust, can be an effective device identifier. Vendors such as
Microchip, Texas Instruments, and many others have TPM-based
hardware solutions.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC02-BP02-01** _Perform cryptographic
operations inside the TPM to avoid a third party gaining
unauthorized access._

Store all secret keys from the manufacturer required for secure
boot, such as attestation keys, storage keys, and application
keys, in the secure enclave of the chip. For example, a device
running AWS IoT Greengrass can be used with an Infineon OPTIGA
TPM.

**Prescriptive guidance
IOTSEC02-BP02-02** _Use a trusted execution
environment (TEE) along with a TPM to act as a baseline defense
against rootkits._

TEE is a separate execution environment that provides security
services and isolates access to hardware and software security
resources from the host operating system and applications.
Various hardware architectures support TEE such as:

1. ARM TrustZone divides hardware into secure and non-secure
   worlds. TrustZone is a separate microprocessor from the
   non-secure microprocessor core.
2. Intel Boot Guard is a hardware-based mechanism that provides
   a verified boot, which cryptographically verifies the
   initial boot block or uses a measuring process for
   validation.

**Prescriptive guidance
IOTSEC02-BP02-03** _Use physical unclonable
function (PUF) technology for cryptographic
operations._

A PUF technology is a physical object that provides a physically
defined digital fingerprint to serve as a unique identifier for
an IoT device. As a different class of security primitive, PUFs
normally have a relatively simple structure. It makes them ideal
candidates for affordable security solutions for IoT networks.
Generally, a hardware root of trust based on PUF is virtually
impossible to duplicate, clone, or predict. This makes them
suitable for applications such as secure key generation and
storage, device authentication, flexible key provisioning, and
chip asset management. Refer to
[AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices/ "https://partners.amazonaws.com/qualified-devices/") which has various device solutions
with PUFs such as LPC54018 IoT Solution by NXP.

## IOTSEC02-BP03 Use protected boot and persistent storage encryption

When a device performs a secure boot, it validates that the
device is not running unauthorized code from the filesystem.
This helps make sure that the boot process starts from a trusted
combination of hardware and software, and continues until the
host operating system has fully booted and applications are
running.

Choose devices with TPM (or TEE) for new deployments. Secure
boot also makes sure that if even a single bit in the software
boot-loader or application firmware is modified after
deployment, the modified firmware will not be trusted, and the
device will refuse to run this untrusted code.

Full disk encryption makes sure that the storage and
cryptographic elements are secured in absence of a TPM or SE.
The disk controller needs to make sure that read accesses to the
disk are transparently decrypted and write operations are
encrypted at runtime.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC02-BP03-01** _Boot devices using a
cryptographically verified operating system image._

Use digitally signed binaries that have been verified using an
immutable root of trust, such as a master root key (MRK) that's
stored securely in a non-modifiable memory, to boot devices.

**Prescriptive guidance
IOTSEC02-BP03-02** _Create separate filesystem
partitions for the boot-loader and the applications._

As an example, configure the device boot-loader to use a
read-only partition, and applications to use a separate writable
partition for separation of concerns and reducing risks.

**Prescriptive guidance
IOTSEC02-BP03-03** _Use encryption utilities
provided by the host operating system to encrypt the writable
filesystem._

For example, use crypt utilities for Linux such as dm-crypt or
GPG, and use BitLocker or Amazon EFS for Microsoft Windows.

**Prescriptive guidance
IOTSEC02-BP03-04** _Use services that can push
signed application code from a trusted source to the
device._

You can use AWS IoT Jobs to push signed software binaries from
the cloud to the device. For microcontrollers using FreeRTOS,
make sure that the firmware images are signed before deployment.
Signature verification should also verify that the signer of the
package is trusted and the signer's certificate and any
intermediate certificate authorities' certificates have not been
revoked.

| IOTSEC03: How do you authenticate and<br>authorize user access to your IoT application? |
| --------------------------------------------------------------------------------------- |
|                                                                                         |

Although many applications focus on the device aspect of IoT, in
almost all industries using IoT, there is also a human component
that needs the ability to communicate to and receive
notifications from devices.

For example, consumer IoT generally requires users to onboard
their devices by associating them with an online account.
Industrial IoT typically entails the ability to analyze hardware
telemetry in near real time. In either case, it is essential to
determine how your application will identify, authenticate, and
authorize users that require the ability to interact with the
solution and with particular devices.

Controlling user access to your IoT assets begins with identity.
Your IoT application must have in place a store (typically a
user registry or identity provider) that keeps track of a user's
identity and also how a user authenticates using that identity.
The identity store may include additional user attributes that
can be used at authorization time. For example, the user's group
memberships.

When using AWS to authenticate and authorize IoT application
users, you have several options to implement your identity store
and how that store maintains user attributes. For your own
applications, use Amazon Cognito for your identity store. Amazon Cognito provides a standard mechanism to express identity and to
authenticate users. Amazon Cognito enables usage of user
identity in a way that can be directly consumed by your app and
other AWS services in order to make authorization decisions. 
When using AWS IoT, you can choose from several identity and
authorization services including Amazon Cognito Identity Pools,
AWS IoT policies, and AWS IoT custom authorizer to validate
tokens (such as JWT or SAML 2.0) for authenticating users.
Amazon Cognito supports federation to third party identity
providers using the OpenID Connect (OIDC) and SAML 2.0
protocols.

An alternative to using AWS IAM-based role permissions for user
interaction with an IoT solution is to define a separate
authorization layer for the application which uses Amazon Verified Permissions. Verified Permissions allows for the
definition of fine-grained access control policies for accessing
resources which are specific to an application. Principals used
in AVP policy statements can be defined from Amazon Cognito user pools.

## IOTSEC03-BP01 Implement authentication and authorization for users accessing IoT resources

This practice provides users with secure access to connected IoT
devices and equipment through different channels such as web or
mobile devices. Without valid authentication and authorization,
devices can be subjected to risks of unauthorized access.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC03-BP01-01** _Implement an identity
store to authenticate users of your IoT application._

Implement an identity and access management solution for end
users. This solution should allow end users with temporary,
role-based credentials to access the IoT solution. For example,
you can use a service like Amazon Cognito to create user pools
for authentication. Or, you can use Amazon Cognito integration
with SAML 2.0 or OAuth 2.0 compliant identity providers for
authentication as well. If you host your own identity store, use
AWS IoT custom authorizers to validate tokens such as JWT and
SAML 2.0 for authenticating users. AVP can be used to define
fine-grained access control policies to specify who (identity)
can perform what actions on which resources (application, data,
and devices).

**Prescriptive guidance
IOTSEC03-BP01-02** _Grant least privilege
access_

Authorization is the process of granting permissions to perform
some operation or access some information by an authenticated
identity. If using AWS IAM credentials, you grant permissions to
your users in AWS IoT Core using data plane and control plane
IAM policies through the Identity broker. AWS IoT control plane
APIs allow you to perform administrative tasks like creating or
updating certificates, things, and rules. AWS IoT data plane
APIs allow you send data to and receive data from AWS IoT Core.

For example, if you are using Amazon Cognito, use federated
identities for user authentication and Amazon Cognito identity pools to
establish IAM credentials. If you are using a different Identity
provider than Amazon Cognito, use AWS IoT custom authorizers to
invoke lambda functions that will create the required IAM
policies. To define fine-grained permissions for Amazon Cognito
users, use AVP to define authorization policies in which the
principal is the Amazon Cognito user or group.

**Prescriptive guidance
IOTSEC03-BP01-03** _Adopt least privilege when
assigning user permissions._

Adopt the least privilege principle and assign only the minimum
required permissions to each IAM role that is used in the
solution. This applies to both user and service (For example,
Lambda function) roles that are defined in the solution.

For example, with Amazon Cognito Identity Pools this can be
achieved by setting up role-based access through IAM policies
for authenticated users like consumers or administrators as well
as unauthenticated users. Consumers or unauthenticated users
should not be allowed to run adminstrative actions against IoT
services, such as detaching policies, deleting certificate
authorities (CAs), or deleting certificates.

## IOTSEC03-BP02 Decouple access to your IoT infrastructure from the IoT applications

For implementing the decoupled view of telemetry for your users,
use a mobile service such as AWS AppSync or Amazon API Gateway.
With both of these AWS services, you can create an abstraction
layer that decouples your IoT data stream from your user's
device data notification stream. By creating a separate view of
your data for your external users in an intermediary datastore,
you can use AWS AppSync to receive user-specific notifications
based only on the allowed data in your intermediary store.
Examples of intermediate data stores are Amazon DynamoDB, Amazon Relational Database Service, and Amazon OpenSearch Service. In
addition to using external data stores with AWS AppSync, you can
define user specific notification topics that can be used to
push specific views of your IoT data to your external users.

If an external user needs to communicate directly to an AWS IoT
endpoint, make sure that the user identity is either an
authorized Amazon Cognito Federated Identity that is associated
to an authorized Amazon Cognito Identity Pool role and a
fine-grained IoT policy, or uses AWS IoT custom authorizer,
where the authorization is managed by your own authorization
service. With either approach, associate a fine-grained policy
to each user that limits what the user can connect as, publish
to, subscribe from, and receive messages from concerning MQTT
communication.

By decoupling the IoT infrastructure from the end-user IoT
applications, you can build an additional layer of security and
reliability.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC03-BP02-01** _Use an API layer between
the application and IoT layer._

Build an application interface layer to insulate the IoT data
plane from end users. Fundamentally, the primary interface to
IoT data plane is MQTT topics. Protecting the data plane
essentially means protecting the MQTT topics from unwanted
communication.

For example, use Amazon API Gateway or AWS AppSync to provide a
REST or GraphQL API interface between the end user application
and the IoT layer. With this design, an API implementation,
often built using an AWS Lambda function, would communicate with
devices using the IoT data plane. This insulates the operations
on the IoT data plane from the end user interaction performed at
the REST or GraphQL API interfaces. Fine-grained permissions for
using the API interfaces can be defined using AVP.

| IOTSEC04: How do you apply least<br>privilege to principals that interact with your IoT<br>application? |
| ------------------------------------------------------------------------------------------------------- |
|                                                                                                         |

After registering a device and establishing its identity, it may
be necessary to add additional device information needed for
monitoring, metrics, telemetry, or command and control. Each
resource (for example, device, background task, service, API,
and user) requires its own assignment of access control rules.
By reducing the actions that a device or user can take in your
application, and making sure that each resource is secured
separately, you reduce the risks to your system in case a single
identity is compromised.

In AWS IoT, create fine-grained permissions by using a
consistent set of naming conventions in the IoT registry. The
first convention is to use the same unique identifier for a
device. Match the MQTT ClientID and AWS IoT thing name. By using
the same unique identifier in all these locations, you can
easily create an initial set of IoT permissions that can apply
to your devices using
[AWS IoT Thing Policy variables](../../../iot/latest/developerguide/thing-policy-variables.md "../../../iot/latest/developerguide/thing-policy-variables.md"). The second naming convention
is to embed the unique identifier of the device into the device
certificate. Continuing with this approach, store the unique
identifier as the `CommonName` naming element in the subject name
of the certificate so that
[Certificate Policy VariablesX.509 Certificate AWS IoT Core policy
variables](../../../iot/latest/developerguide/cert-policy-variables.md "../../../iot/latest/developerguide/cert-policy-variables.md") can be used to bind IoT permissions to each
unique device principal.

By using policy variables, you can create a few IoT policies
that can be applied to your device certificates while
maintaining least privilege. For example, the IoT policy below
would restrict devices to connect only using the unique
identifier of the device which is stored in the common name as
its MQTT ClientID (see policy variable inserted into Resource
name) and only if the certificate is attached to the device.
This policy also restricts a device to only publish on its
individual shadow (see policy variable inserted into MQTT
topic):

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Connect"
 ],
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:client/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish"
 ],
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/things/*/shadow/update"
 ]
 }
 ]
}`

```

Attach your device identity (certificate or Amazon Cognito
Federated Identity) to the thing in the AWS IoT registry using
[`AttachThingPrincipal`](../../../iot/latest/apireference/API_AttachThingPrincipal.md "../../../iot/latest/apireference/API_AttachThingPrincipal.md")
and attach the policy to principals using
[`AttachPolicy`](../../../iot/latest/apireference/API_AttachPolicy.md "../../../iot/latest/apireference/API_AttachPolicy.md").

Although these scenarios apply to a single device communicating
with its own set of topics and device shadows, there are
scenarios where a single device needs to act upon the state or
topics of other devices. For example, you may be operating an
edge appliance in an industrial setting, creating a home gateway
to manage coordinating automation in the home, or allowing a
user to gain access to a different set of devices based on their
specific role. For these use cases, leverage a known entity,
such as a group identifier or the identity of the edge gateway
as the prefix for all of the devices that communicate to the
gateway. By making all of the endpoint devices use the same
prefix, you can make use of wildcards, `"*"`, in your
IoT policies. This approach balances MQTT topic security with
manageability.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": ["iot:Publish"],
 "Resource": ["arn:aws:iot:us-east-1:123456789012:topic/$aws/things/edgegateway123-*/shadow/update"]
 }]
}`

```

In the preceding example, the IoT operator would associate the
policy with the edge gateway with the identifier,
edgegateway123. The permissions in this policy would then allow
the edge appliance to publish to other Device Shadows that are
managed by the edge gateway. This is accomplished by enforcing
that connected devices to the gateway all have a thing name that
is prefixed with the identifier of the gateway. For example, a
downstream motion sensor would have the identifier
`edgegateway123-motionsensor1`, and therefore can now be managed
by the edge gateway while still restricting permissions.

## IOTSEC04-BP01 Assign least privilege access to devices

Permissions (or policies) allow an authenticated identity to
perform various control plane and data plane operations against
AWS IoT Core, such as creating devices or certificates via the
control plane, and connecting, publishing, or subscribing via
the data plane.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC04-BP01-01** _Grant least privilege
access to reduce the scope and impact of the potential
events._

Use granular device permissions to enable least privilege
access, which can help limit the impact of an error or
misconfiguration. Define a mechanism so that devices can only
communicate with specific resources such as MQTT topics. If
permissions are generated dynamically, make sure that similar
practices are followed. For example, create an AWS IoT policy as
a JSON document that contains a statement with the following:

1. `Effect`, which specifies whether the action is allowed or
   denied.
2. `Action`, which specifies the action the policy is allowing or
   denying.
3. `Resource`, which specifies the resource or resources upon
   which the action is allowed or denied.

**Prescriptive guidance
IOTSEC04-BP01-02** _Consider scaling granular
permissions across the IoT fleet._

Reuse permissions across principals where possible rather than
creating specific permissions for each individual principal.
This helps you avoid creating redundant permissions per device
and streamlines applying similar permission changes across
multiple devices.

For example, consider an AWS IoT policy allows access based on
various thing attributes such as `ThingName`, `ThingTypeName`, and `Thing
 Attributes`. To allow a device to access its own
information, use a policy variable rather than specifying a
specific ClientId value and creating a IoT policy for each
device.

- Recommended:
  `arn:aws:iot:us-east-1:123456789012:client/${iot:Connection.Thing.ThingName}`

- Not recommended:
  `arn:aws:iot:us-east-1:123456789012:client/foo.`

As another example, consider an AWS IoT policy also allows
access based on various certificate attributes such as `Subject`,
`Issuer`, `Subject Alternate Name`, `Issuer Alternate Name`, and
others. Again, use a policy variable rather than specifying a
specific `CertificateId` and creating a IoT policy for each
device.

- Recommended:
  `arn:aws:iot:us-east-1:123456789012:topic/${iot:CertificateId}`
- Not recommended:
  `arn:aws:iot:us-east-1:123456789012:topic/xxxxxxxxxxx`

| IOTSEC05: How do you manage device<br>certificates, including installation, validation, revocation,<br>and rotation? |
| -------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                      |

To authenticate IoT device to AWS IoT Core and authenticate AWS IoT Core to an IoT device, AWS IoT Core supports TLS-based
mutual authentication using X.509 certificates. TLS-based mutual
authentication authenticates both client and server to one
another during the TLS handshake processing of setting up an
encrypted TLS communications channel.

To enable TLS-based mutual authentication, device makers must
provision a unique identity, including a unique private key and
X.509 certificate, into each device. Certificates are relatively
long-lived identifiers of principals and are managed using a
customer-owned Certificate Authority (CA), a third-party CA, or
the AWS IoT Core CA. Any hosted CA chosen must provide you the
ability to create (activate), revoke (deactivate), validate, and
refresh or rotate certificates. Authentication using
certificates requires, at authentication time, that the
principal identified by the certificate can prove that it holds
the private key associated with the public key found in the
certificate.

Authenticated identities are the focal point of device trust and
authorization to your IoT application. It's vital to be able to
manage identities, such as certificates, centrally. Valid
certificates are those which are not revoked, expired, made
inactive, and not issued by a CA which has had its certificate
revoked or invalidated. As part of a well-architected
application, you must have a process for identifying any invalid
certificates and have an automated response in place to take
some action to address the finding.

In addition to the ability of capturing the events where an
invalid certificate is presented, your devices should also have
a secondary means of establishing secure communications to your
IoT system if mutually-authenticated TLS communications is not
possible. This may involve manual, local interaction with the
device, either by a consumer or service technician.

A well-architected IoT solution establishes a certificate
revocation list (CRL) that tracks all revoked device
certificates or certificate authorities (CAs). Use your own
trusted CA for on-boarding devices and synchronize the CRL in
the device and in your IoT application on a regular basis. Your
IoT application must reject connections from identities
(certificates or tokens) that are no longer valid.

With AWS, you do not need to manage your entire PKI on-premises.
Use AWS Certificate Manager (ACM) or AWS Private Certificate Authority (PCA) to host your CA in the cloud. Or, you can work
with an APN Partner to add preconfigured secure elements to your
IoT device hardware specification. ACM has the capability to
export a certificate revocation list (CRL) to a file in an S3
bucket. The CRL can be used to programmatically revoke
certificates configured in AWS IoT Core.

Another state for certificates is to be near their expiry date
but still valid. The device certificate must be valid for at
least the service lifetime of the device. If a device
certificate is nearing its expiration date and the device is to
remain in operation, then your IoT application must take some
action to update the device certificate with a certificate that
has a later expiration date. Use the AWS IoT Jobs or OTA to
perform the necessary operations to carry out this refresh. Be
sure to log information about the certificate refresh operations
performed for auditing purposes.

Enable AWS IoT Device Defender audits related to device and CA
certificate expiry. Device Defender produces an audit log of
certificates that are set to expire within 30 days. Use this
list to programmatically update devices before certificates are
no longer valid. You may also choose to build your own expiry
store to manage certificate expiry dates and programmatically
query, identify, and trigger an IoT Jobs and OTA for device
certificate replacement or renewal.

## IOTSEC05-BP01 Perform certificate lifecycle management

Certificate lifecycle includes different phases such as
creation, activation, refresh or rotation, revocation,
deactivation, or expiry. An automated workflow can be put in
place to identify certificates that need attention, along with
remediation actions.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC05-BP01-01** _Document your plan for
managing certificates._

As explained earlier, X.509 certificates help to authenticate
devices and AWS IoT Core to one another and to set up encrypted
communications between the edge and cloud. Planning the
lifecycle management of device certificates is essential. Enable
auditing and monitoring for compromise or expiration of your
device certificates. Determine how frequently you need to
refresh/rotate device certificates, audit cloud or
device-related configurations and permissions to make sure that
security measures are in place. For example, use AWS IoT Device Defender to monitor the health of the device certificates and
different configurations across your fleet. AWS IoT Device Defender can work in conjunction with AWS IoT Jobs to help
enable refresh/rotation of certificates which are nearing their
expiration.

**Prescriptive guidance
IOTSEC05-BP01-02** _Use certificates signed by
your trusted intermediate CA for on-boarding devices_

As a best practice, the all-root CA keys must be locked and
protected to secure the chain of trust. Device certificates
should be generated using an intermediate CA to sign the device
certificates. Define a process to programmatically manage
intermediate CA certificates as well. For example, enable AWS IoT Device Defender Audit to report on your intermediate CAs
that are revoked but device certificates are still active or if
the CA certificate quality is low. You can thereafter use a
security automation workflow using mitigation actions in AWS IoT Device Defender to resolve the issues.

**Prescriptive guidance
IOTSEC05-BP01-03** _Secure provisioning claims
(just-in-time provisioning or registration) private keys and
disable the certificate in case of misuse and record the event
for further investigation._

- Monitor provisioning claims for private keys when using just
  in time provisioning or just-in-time registration.
- Be sure to monitor usage on the device as well as in AWS IoT Core.
- For example:
  - Use AWS IoT CloudWatch metrics and logs to monitor for
    indications of misuse. If you detect misuse, disable the
    provisioning claim certificate so it cannot be used for
    device provisioning.
  - Use AWS IoT Device Defender to identify security issues
    and deviations from best practices.

### Resources

- [Getting started
  with AWS IoT Device Defender](../../../iot/latest/developerguide/vulnerability-analysis-and-management.md "../../../iot/latest/developerguide/vulnerability-analysis-and-management.md")
- [Just-in-Time
  Registration of Device Certificates on AWS IoT](https://aws.amazon.com/blogs/iot/just-in-time-registration-of-device-certificates-on-aws-iot/ "https://aws.amazon.com/blogs/iot/just-in-time-registration-of-device-certificates-on-aws-iot/")
