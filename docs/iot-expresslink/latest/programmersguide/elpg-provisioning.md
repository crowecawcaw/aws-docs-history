# 12 Provisioning and Onboarding

All ExpressLink modules will be equipped with a pre-provisioned hardware root of trust
(on chip or external secure element, secure enclave, TPM, iSIM). This will provide the
necessary unique identifier (UID) of the module, a key pair (public, private) and will
hold a certificate that is signed by a CA shared with AWS as part of ExpressLink program.
This certificate will be used to transfer the module public key to the AWS endpoint upon
activation.

## 12.1 ExpressLink Modules Activation

Upon first use, or following a complete factory reset, each ExpressLink module is
ready to establish a connection according to the model's specific connectivity
capabilities (Wi-Fi, Cellular, ...). In case of Wi-Fi modules, this is possible only
after the end-user has provided the module with the proper Wi-Fi credentials for a
local, compatible Wi-Fi Access Point (router).

### 12.1.1 ExpressLink Staging Account Authentication

Each ExpressLink module is ready to establish a connection with a default
AWS IoT ExpressLink staging account. The connection is mutually authenticated
using the ExpressLink birth certificate (and an AWS server certificate) and
upgraded to a secure socket connection (Mutual TLS).

### 12.1.2 ExpressLink Staging Account Endpoint

During the qualification process, AWS assigns each ExpressLink manufacturing
partner a dedicated staging account and the associated, unique AWS endpoint
(URL).

`12.1.2.1`   The assigned staging account endpoint
is set as the "factory default" for the Endpoint configuration parameter (see
[Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") ).

### 12.1.3 ExpressLink Birth Certificate

Each ExpressLink device must be provided with an X.509 certificate that conforms
to the following specification:

`12.1.3.1`  

The Serial Number must contain
the device Unique ID (a unique, nonsequential 128-bit or larger number) also
assigned as the ExpressLink module ThingName configuration.

`12.1.3.2`  

The certificate signature is
provided by a Certificate Authority that has been registered by the vendor
with AWS IoT Core for the exclusive use of the vendor ExpressLink modules.

`12.1.3.3`  

The expiration date is set
to no less than 10 years from the device certificate issue.

### 12.1.4 ExpressLink staging account device registration

Using the staging account endpoint, the ExpressLink module proceeds to login to
the AWS IoT Core MQTT broker. If successful, an automated process (JITP or similar)
creates a thing and associated policies using an ExpressLink template and appends
it to the staging account registry.

## 12.2 ExpressLink Evaluation Kits Quick Connect Flow

ExpressLink Evaluation Kits are able to use the ExpressLink staging account to
deliver a fast, out-of-box experience. As soon as connected they are able to publish
data to an ExpressLink MQTT topic ("data") and subscribe to any ExpressLink MQTT
topic ("state"). AWS provides a simple web application (Quick Connect) to all
ExpressLink users to visualize the data published by the Host processor (using
animated graphs) and to send customizable commands back to their Host processors.

![Figure 5 - ExpressLink evaluation kit Quick Connect flow](images/QuickConnect_Visualizer.r.png)

Figure 5 - ExpressLink evaluation kit Quick Connect flow

Developers are also able to register their ExpressLink modules to their private
developer's accounts and proceed to application development with a few simple, manual
steps, including:

- extracting the device certificate
- uploading it to their private accounts
- updating the ExpressLink endpoint

### 12.2.1 Workshop Default Wi-Fi Credentials (Optional)

To reduce the number of configuration steps (and time) required to establish a Wi-Fi connection,
a default set of Wi-Fi credentials can be provided in the configuration dictionary at Factory Reset.

Using default Wi-Fi credentials can be convenient in workshop, classroom or seminar environments
avoiding a number (10+) of user to attempt simultaneously to use a CONFMODE (Bluetooth)
connection and greatly simplifying the room set up.

If implemented, the manufacturer will document such credentials in the module datasheet.

## 12.3 ExpressLink Production Onboarding Flow

Onboarding is the process of creating a "thing" corresponding to each physical
device in the customer account registry in order to provide access to the account's
IoT core services. Each thing must be associated with a valid certificate and access
policy document.

In a production flow, ExpressLink customers can use any of a number of automated
onboarding techniques as required by their application, including:

- Pre-registration, where the modules' certificates are obtained before
  assembly and uploaded to the customer account in advance.
- End of (assembly) Line registration, where module certificates are collected
  after product assembly and individually uploaded to the customer's AWS account.
- End of Line batch registration, where module certificates are collected after
  product assembly and shipped in batches to the customer for upload into the
  AWS account.
- Just in Time Registration, where the device onboards to the customer account
  at first connection. (This requires pre-registration of the module manufacturer's
  CA to the customer account.)
- Late-binding, where the end product user performs the product onboarding (often
  simultaneously with the user's own registration, although the two steps should not
  be confused).

### 12.3.1 ExpressLink Late Binding (Onboarding by Claim) flow example

A late binding onboarding flow can be initiated by the end-user after purchasing
the finished product when they connect it for the first time and register the
product. The end-user can be directed to a web application devised by the
OEM/customer (for example, a toaster manufacturer) that will guide the user through
the following steps:

1. Enter Wi-Fi credentials (only for Wi-Fi modules)– this is required
   to access the AWS cloud. To accomplish this, the host can activate a
   CONFMODE for credential entry or the host can directly manipulate the
   configuration dictionary (SSID, Passphrase).
2. Access the ExpressLink staging account for the first time.
3. Claim the ExpressLink module (identified by ThingName) from the
   staging account.
4. Transfer the certificate to the OEM account registry (thing creation).
5. Update the ExpressLink module Endpoint (to point to the OEM account).
6. Disconnect and reconnect the ExpressLink Device to the OEM account.

Steps 1 and 2 are facilitated by the staging account assigned to each manufacturer
and managed by AWS. Steps 3 and 4 require the customer to implement a claim
mechanism that interacts with the AWS managed staging account. Step 5 is
facilitated by a specific device feature as described in
[21.3.2 ExpressLink onboarding
states and transitions](#elpg-provisioning-onboarding-states "#elpg-provisioning-onboarding-states").

Additional steps to register the user, create an end-user (application) account,
collect user identifiable information (user name and password) and bind it to the
ExpressLink thing are left to the OEM application.

### 21.3.2 ExpressLink onboarding

states and transitions

The configuration parameter Endpoint (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2 "elpg-configuration-dictionary.md#elpg-table2") ) controls the onboarding state of the device. The
device is in the _staging_ state when the Endpoint parameter
(string) matches the factory default value that corresponds to an AWS-managed
staging account assigned to each manufacturer. The device is in the
_onboarded_ state when the Endpoint parameter has been modified
to point to a customer account (endpoint) by a host that directly updated the
configuration dictionary using a CONF command (see
[6.2.1 CONF KEY={value}   »Assignment«](elpg-configuration-dictionary.md#elpg-assignment-conf "elpg-configuration-dictionary.md#elpg-assignment-conf")) or
by means of the following remote update process:

`12.3.2.1`   When (and only when) in the
_staging_ state, a connected ExpressLink module automatically
subscribes ONLY to the endpoint-update topic:
**`ThingName`/expresslink_config**.
Then, when it receives a message on the update topic with the following format:
**{"Endpoint" : "value"}**, the module
updates the Endpoint configuration parameter with the requested new value.

`12.3.2.2`   The host can retrieve the MSG event
produced (GET0) and use it to implement additional optional features, such as to
alert the user of the device of a successful onboarding (registration).

`12.3.2.3`   The module will also automatically
disconnect. The related CONLOST event will inform the host that it must re-establish
a new connection, this time to the newly assigned endpoint.

`12.3.2.4`   The host can query the state of the
module using the CONNECT? command and inspecting the second numerical parameter
provided in the response (see [4.7.1 CONNECT?   »Request the connection status«](elpg-commands.md#elpg-connectq-command "elpg-commands.md#elpg-connectq-command")) without having to inspect the contents of the
Endpoint configuration parameter (or knowing or assuming the default Endpoint value
to compare against).

`12.3.2.5`   When (and only when) in the
_onboarded_ state, a connected ExpressLink module subscribes
automatically to several AWS-reserved topics as required to support OTA and
other core ExpressLink functionality. In the same way, features dependent on the
AWS IoT Device Defender and AWS IoT Device Shadow services are supported only when a
module is in the _onboarded_ state.

![Figure 6 - ExpressLink onboarding states diagram](images/image5.png)

Figure 6 - ExpressLink onboarding states diagram

 

Once onboarded, all ExpressLink modules behave as fully owned devices and
connect to the customer/OEM account as the ExpressLink things are transferred to
the chosen OEM registry. It is the responsibility of the OEM to manage the product
life cycle, use the OTA services to apply module updates (with images provided by
the ExpressLink module vendor) and apply host processor application updates as
needed.

## 12.4 End-User change, product re-registration

This is a normal occurrence in the life of many products when they are resold or
disposed of. If required, ExpressLink modules can be reset to factory settings to
reactivate the onboarding process from the beginning and eliminate any previous
owner association.

## 12.5 Handling onboarding failures

The onboarding process can fail at various points due to end-user, host application,
or network errors. We envision the following scenarios:

- Onboarding process failure: if the OEM misconfigures the account
  policies this would prevent the device certificate from being moved into
  the target account. The AWS IoT API will report this type of error to
  OEM developers during testing.
- Onboarding process failure: if the ExpressLink claim and removal from the
  staging account fails this would leave it in the staging account while a new
  thing is created in the OEM account and the ExpressLink module is redirected
  to the new endpoint. Staging account periodic cleaning and fraud detection
  sweeps will clear the anomaly in a short time.
- Endpoint Update failure: if the device does not receive the ExpressLink
  endpoint update message it remains in the staging account and fails to
  connect to the target OEM account within a given amount of time. The binding
  process (web application) can be designed to timeout and guide the user to
  repeat the procedure until successful.
- Accidental product factory reset: in this case, the ExpressLink device will
  rejoin the staging account as soon as connectivity is regained, and the
  onboarding process can be restarted at any time. The OEM application will be
  able to detect that an already registered device is re-applying to onboarding
  and could possibly help to restore the product status and/or report the error
  to developers.
