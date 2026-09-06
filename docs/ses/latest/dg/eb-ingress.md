

# Ingress endpoints
<a name="eb-ingress"></a>

An ingress endpoint is the key infrastructure component in Mail Manager that receives, routes, and manages your email by utilizing policies and rules you configure to determine which emails should be rejected, which ones should be allowed, and which ones should be acted upon.

Each ingress endpoint has its own traffic policy to determine which emails to block or allow, and its own rule set to perform actions on the email you do allow in; therefore, by creating multiple ingress endpoints, you can delegate each one to manage and route specific types of email. This level of granularity will help you to build an email management system that's tailored to your business needs.

**Prerequisite workflow to create an ingress endpoint**  
At the time of creating your ingress endpoint, you must assign it a traffic policy and a rule set that have *already been created*. Therefore, the workflow for creating an ingress endpoint should be in the following order:

1. Start by creating a traffic policy to determine the email you want to block or allow. For details, see [Creating traffic policies and policy statements in the SES console](eb-filters.md#eb-filters-create-console).

1. Next, create a rule set to perform actions on the email you allow in. For details, see [Creating rule sets and rules in the SES console](eb-rules.md#eb-rules-create-console).

1. Finally, create your ingress endpoint and assign to it the traffic policy and rule set you just created or any others you previously created.

Once you create your ingress endpoint, you must configure it with the environment you're using to receive email, whether that be the configuration of an on-premise SMTP client or a web-based DNS domain host. This is discussed below in [Receiving email through the public endpoints](#eb-ingress-a-record).

## Configuring your environment to use an ingress endpoint
<a name="eb-ingress-config-endpoints"></a>

SES supports both public endpoints and Amazon Virtual Private Cloud (VPC) endpoints for ingress endpoints to accept incoming email. The following sections explain how to configure your ingress endpoint to use either of these options.

**Topics**
+ [Public endpoint configuration](#eb-ingress-a-record)
+ [VPC endpoint configuration](#eb-ingress-vpc-endpoint)

### Receiving email through the public endpoints
<a name="eb-ingress-a-record"></a>

**Using the "A" record**  
At the time you create an ingress endpoint, an "A" record for the endpoint will be generated and its value displayed on the ingress endpoint's summary screen in the SES console. The way you use the value of this record depends on the type of endpoint you created and your use case:
+ **Open endpoint** – Mail sent to your domain will resolve directly to your ingress endpoint—no authentication required.
  + Copy and paste the value of the "A" record either directly into the SMTP configuration of an on-premise SMTP client or into an MX record for your domain in your DNS configuration.
  + Supported port: 25
  + Supports STARTTLS: Yes
+ **Authenticated endpoint** – Mail sent to your domain has to come from authorized senders whom you’ve shared your SMTP credentials with, such as your on-premise email servers.
  + Copy and paste the value of the "A" record directly into the SMTP configuration of an on-premise SMTP client as well as your user name and password.
  + Supported ports: 25, 587 ([RFC 2476](https://www.ietf.org/rfc/rfc2476.txt))
  + Supports STARTTLS: Yes
+ **mTLS endpoint** – Mail sent to your domain must come from clients that present a TLS client certificate signed by one of the certificate authorities (CAs) in the ingress endpoint's trust store. See [Mutual TLS (mTLS) authentication for ingress endpoints](#eb-ingress-mtls).
  + Copy and paste the value of the "A" record directly into the SMTP configuration of an on-premise SMTP client.
  + Supported port: 25
  + Supports STARTTLS: Yes

If you're using an MX record in your configuration, keep in mind that while every DNS provider has different procedures and interfaces for configuring records, the key pieces of information you need to put into you DNS settings are listed in the following example:

All email sent to *recipient@marketing.example.com* will go to your ingress endpoint because you entered the ingress endpoint's "A" record as the value for an MX record in your domain’s DNS settings:
+ **Domain** – `marketing.example.com`
+ **MX record value** – `890123abcdef.ghijk.mail-manager-smtp.amazonaws.com` *(This is the "A" record value copied from your ingress endpoint.)*
+ **Priority** – `10`

**Connecting to the authenticated endpoint**  
For the authorized senders whom you’ve shared your SMTP credentials with in order to connect to your authenticated endpoint, the following protocols must be followed for the *username* and *password* in order to establish a successful connection to the server:
+ **Username** – This is the ingress endpoint ID and must be encoded in Base64. *(See [Step 11.](#find-ingress-id) in the console procedures to learn how to find the ingress endpoint ID.)*
+ **Password** – This is the one used during ingress endpoint creation and must be encoded in Base64.

The following example shows a typical SMTP AUTH server and client exchange establishing connection:

```
S: 250 AUTH LOGIN PLAIN
C: AUTH LOGIN
S: 334 VXNlcm5hbWU6
C: SW5ncmVzc1BvaW50
S: 334 UGFzc3dvcmQ6
C: SW5ncmVzc1Bhc3N3b3Jk
S: 235 Authentication successful
```

This example contains the following properties:
+ `S` means "Server"—the SMTP server accepting messages.
+ `C` means "Client"—the SMTP client establishing connection with the server and sending messages to server.
+ `250 AUTH LOGIN PLAIN` is a response from the server with AUTH methods supported, `AUTH LOGIN` or `AUTH PLAIN`, the sender could choose either of them, and send SMTP commands compliant with the SMTP Service Extension for Authentication specification [RFC 2554](https://www.ietf.org/rfc/rfc2554.txt). `AUTH LOGIN` is used here.
+ `334 VXNlcm5hbWU6` – Server prompting for the username in Base64.
+ `SW5ncmVzc1BvaW50` – Client responding with ingress endpoint ID in Base64.
+ `334 UGFzc3dvcmQ6` – Server prompting for the password in Base64.
+ `SW5ncmVzc1Bhc3N3b3Jk` – Client responding with ingress endpoint password in Base64.

### Receiving email through Amazon VPC endpoints
<a name="eb-ingress-vpc-endpoint"></a>

In addition to public ingress endpoints, you can use VPC endpoints with SES ingress endpoints for secure, private email ingestion within your private network infrastructure.

**Configuration differences compared to using public ingress endpoints**  

+ The "A" Record typically available for public endpoints is not provided.
+ You must connect to the ingress endpoint using DNS names provided by your VPC endpoint.
+ All connections use private networking within your VPC.

**Types of ingress endpoints supported through VPC endpoints**  
SES supports two types of ingress points through VPC endpoints:
+ **Open ingress endpoint** – Email sent to your domain route directly through the VPC endpoint without requiring sender authentication.

  Configuration requirements:
  + Create a private open ingress endpoint by associating it with a VPC endpoint ID you own.
  + Supported ports: 25, 587
  + Supports STARTTLS: Yes
+ **Authenticated ingress endpoint** – Mail sent to your domain has to come from authorized senders whom you’ve shared your SMTP credentials with, such as your on-premise email servers.

  Configuration requirements:
  + Create a private authenticated ingress endpoint by associating it with a VPC endpoint ID you own.
  + Supported ports: 25, 587 
  + Supports STARTTLS: Yes
  + Authentication uses the same base64-encoded username and password mechanism as public authenticated endpoints.
+ **mTLS ingress endpoint** – Mail sent to your domain must come from clients that present a TLS client certificate signed by one of the CAs in the ingress endpoint's trust store. See [Mutual TLS (mTLS) authentication for ingress endpoints](#eb-ingress-mtls).

  Configuration requirements:
  + Create a private mTLS ingress endpoint by associating it with a VPC endpoint ID you own.
  + Supported ports: 25, 587
  + Supports STARTTLS: Yes

**VPC endpoint requirements**  
To use a VPC endpoint with an SES ingress endpoint, the following requirements must be met:
+ The VPC endpoint must be active and available.
+ The VPC endpoint must be owned by the same AWS account as the ingress endpoint (cross-account access is not supported).
+ The VPC endpoint must be created for the appropriate service name based on the type of ingress endpoint:
  + **Open ingress endpoint** – `com.amazonaws.{{region}}.mail-manager-smtp.open`
  + **Authenticated ingress endpoint** – `com.amazonaws.{{region}}.mail-manager-smtp.auth`
  + **mTLS ingress endpoint** – `com.amazonaws.{{region}}.mail-manager-smtp.mtls`
  + **FIPS open ingress endpoint** – `com.amazonaws.{{region}}.mail-manager-smtp.open.fips`
  + **FIPS authenticated ingress endpoint** – `com.amazonaws.{{region}}.mail-manager-smtp.auth.fips`
  + **FIPS mTLS ingress endpoint** – `com.amazonaws.{{region}}.mail-manager-smtp.mtls.fips`

**Important configuration notes**  

+ **One-to-one relationship** – Each VPC endpoint can only be associated with a single ingress endpoint. You cannot use the same VPC endpoint for multiple ingress endpoints.
+ **No VPC endpoint policies** – Unlike other AWS services, VPC endpoints used with ingress endpoints do not support VPC endpoint policies. SES automatically verifies that the VPC endpoint owner and the ingress endpoint owner are the same AWS account.
+ **Private DNS only** – All DNS names provided by the VPC endpoint will be private DNS names accessible only within your VPC.
+ **Validation at creation time** – SES performs validation during resource creation to ensure the VPC endpoint meets all requirements.
+ **TLS policy must match VPC endpoint service** – When creating a private ingress endpoint, the TLS policy value must match the VPC endpoint service type. An ingress endpoint with a `FIPS` TLS policy must use a FIPS VPC endpoint service, and an ingress endpoint with a `REQUIRED` or `OPTIONAL` TLS policy must use a non-FIPS VPC endpoint service. They cannot be mixed.

**Connecting to your ingress endpoint through a VPC endpoint**  
After configuring your VPC endpoint and ingress endpoint:

1. Retrieve the DNS names generated for your VPC endpoint.

1. Configure your SMTP clients or email servers to use these DNS names for connection.

1. If using an authenticated endpoint, configure your SMTP clients with the appropriate base64-encoded credentials used with your authenticated ingress endpoint.

## SMTP credentials rotation for authenticated ingress endpoints
<a name="eb-ingress-credentials-rotation"></a>

When using an authenticated ingress endpoint, you may need to periodically rotate the SMTP password used by your sending clients. The rotation behavior depends on how you store your credentials: using AWS Secrets Manager or using SES managed storage.

**AWS Secrets Manager-based password storage**  
If you configured your authenticated ingress endpoint with a secret stored in AWS Secrets Manager, Mail Manager uses the `AWSCURRENT` version of the secret for authentication and also accepts the `AWSPREVIOUS` version. This means that both the old and new passwords are valid during and after rotation, giving your sending clients time to update their credentials.

The `AWSPREVIOUS` version does not expire on the Mail Manager side—it remains valid as long as it exists in AWS Secrets Manager. It is your responsibility to manage secret versions and expiration through AWS Secrets Manager.

To set up automatic rotation:

1. Configure [automatic rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.html) on your secret in AWS Secrets Manager.

1. When rotation occurs, AWS Secrets Manager moves the `AWSCURRENT` label to the new secret version and attaches `AWSPREVIOUS` to the former current version.

1. Mail Manager immediately accepts both versions, so sending clients can update their credentials without downtime.

For more information about AWS Secrets Manager rotation strategies, see [Rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*.

**SES managed password storage**  
If you set the password directly when creating the ingress endpoint (or update it using the `UpdateIngressPoint` API), Mail Manager supports the previous password for 14 days after the update. After 14 days, sending clients using the old password receive `Authentication failed` errors.

**Coordinating rotation with sending clients**  
When planning a credentials rotation, notify your sending application owners in advance and ensure they update their SMTP configurations within the grace period. For AWS Secrets Manager-based storage, the grace period lasts as long as the `AWSPREVIOUS` version exists. For SES managed storage, the grace period is 14 days.

**Note**  
For seamless credentials rotation with minimal client disruption, use AWS Secrets Manager-based password storage with automatic rotation configured.

## TLS policy for ingress endpoints
<a name="eb-ingress-tls-policy"></a>

The TLS policy for an ingress endpoint controls whether connecting SMTP clients are required to use TLS encryption when sending email to your endpoint. You can specify a TLS policy when creating an ingress endpoint using the `CreateIngressPoint` API, and change it later using the `UpdateIngressPoint` API. The default TLS policy depends on your region: `FIPS` is the default in US and Canada regions, and `REQUIRED` is the default in all other regions.

All ingress endpoint connections use opportunistic TLS through the STARTTLS command. The connection begins as plaintext and is upgraded to TLS if the connecting client supports it. Implicit TLS (TLS Wrapper), where the connection starts encrypted, is not supported.

The following TLS policy values are available:
+ **FIPS** – Requires TLS encryption using FIPS-validated cryptographic modules. This is the default in US and Canada regions and is only available in those regions.
+ **REQUIRED** – Connecting SMTP clients must use TLS encryption. Connections that do not use TLS are rejected. This is the default in regions outside of the US and Canada.
+ **OPTIONAL** – TLS encryption is supported but not required. Connecting SMTP clients can send email with or without TLS.

**Availability by ingress endpoint type**  
Not all TLS policy values are valid for every combination of ingress endpoint type and network configuration:
+ **FIPS** – Can be used with all ingress endpoint types (open, authenticated, and mTLS) on both public and private networks, but only in US and Canada regions. Once set, `FIPS` cannot be changed to another value through an update. If you need a different TLS policy, you must create a new ingress endpoint.
+ **REQUIRED** – Can be used with all ingress endpoint types in all regions. However, for authenticated and mTLS ingress endpoints on public networks, `REQUIRED` can only be set at creation time—it cannot be changed through an update. For open ingress endpoints (public or private) and authenticated or mTLS ingress endpoints on private networks, `REQUIRED` can be set at creation time and changed through an update. Note that `REQUIRED` is not available for authenticated or mTLS ingress endpoints on public networks in US and Canada regions, where `FIPS` is used instead.
+ **OPTIONAL** – Can be used with open ingress endpoints on both public and private networks, and with authenticated ingress endpoints on private networks. `OPTIONAL` is not available for mTLS ingress endpoints, and is not available for authenticated ingress endpoints on public networks.

**Rules for changing TLS policy**  
The following rules apply when updating the TLS policy on an existing ingress endpoint:
+ `FIPS` cannot be changed after creation.
+ For open ingress endpoints and authenticated ingress endpoints on private networks, you can switch between `REQUIRED` and `OPTIONAL`.
+ For mTLS ingress endpoints and authenticated ingress endpoints on public networks, the TLS policy cannot be changed after creation.

## Mutual TLS (mTLS) authentication for ingress endpoints
<a name="eb-ingress-mtls"></a>

Mutual TLS (mTLS) authentication requires connecting SMTP clients to present a TLS client certificate signed by one of the certificate authorities (CAs) in the ingress endpoint's trust store. Only clients with trusted certificates can send email to your endpoint.

To create an mTLS ingress endpoint, choose `MTLS` as the ingress endpoint type and provide a `TlsAuthConfiguration` containing a `TrustStore` in the `IngressPointConfiguration` parameter of the `CreateIngressPoint` API.

**Trust store configuration**  
The trust store defines which client certificates are accepted by your ingress endpoint. It contains the following fields:
+ **CAContent** (required) – A certificate authority (CA) certificate bundle in PEM format. This bundle contains the CA certificates used to validate client certificates. You can include multiple CA certificates in a single bundle, up to 500 KB.
+ **CrlContent** (optional) – A certificate revocation list (CRL) in PEM format. If provided, client certificates that appear on the CRL are rejected even if they are signed by a trusted CA. Up to 500 KB.
+ **KmsKeyArn** (optional) – The ARN of a AWS KMS customer managed key (CMK) used to encrypt the trust store data. If not specified, an AWS managed key is used. When using a CMK, the key policy must allow SES to use the key. See [KMS customer managed key (CMK) key policy for mTLS trust store](eb-policies.md#eb-policies-ingress-mtls-cmk).

Expired certificates are considered invalid and are not accepted in connections. SES also filters out expired CA certificates and expired certificate revocation lists (CRLs) from your trust store. If a CRL expires, the CA certificate associated with that CRL is also removed from the trust store, which means clients signed by that CA will no longer be able to connect until you provide an updated CRL.

**Using client certificate attributes in rule conditions**  
When a client connects to an mTLS ingress endpoint with a valid certificate, the certificate attributes (such as Common Name, serial number, and Subject Alternative Name fields) are made available for use in rule conditions as string expressions. This allows you to route, filter, or act on email based on the identity of the connecting client. For the full list of available attributes, see the [Rule conditions](eb-rules.md#rule-conditions) reference.

## Creating an ingress endpoint in the SES console
<a name="eb-ingress-create-console"></a>

The following procedure shows you how to use the **Ingress endpoint** page in the SES console to create ingress endpoints and manage the ones you've already created.

**To create an manage ingress endpoints using the console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation panel, choose **Ingress endpoints** under **Mail Manager**.

1. On the **Ingress endpoints** page, select **Create ingress endpoint**.

1. On the **Create new ingress endpoint** page, enter a unique name for your ingress endpoint.

1. Choose whether it will be an **Open**, **Authenticated**, or **mTLS** endpoint.
   + If you choose **Authenticated**, select either **SMTP password** and enter a password (to be shared with authorized senders), or **Secret** and select one of your secrets from **Secret ARN**. *If you select a previously created secret, it must contain the policies indicated in the following steps for creating a new secret.*
   + If you choose **mTLS**, you must provide a trust store configuration containing your CA certificate bundle. Optionally, you can also provide a certificate revocation list and a AWS KMS key. See [Mutual TLS (mTLS) authentication for ingress endpoints](#eb-ingress-mtls).
   + You have the option to create a new secret by choosing **Create new**—the AWS Secrets Manager console will open where you can continue to create a new key:

   1. Choose **Other type of secret** in **Secret type**.

   1. In **Key/value pair**, enter `password` for the key, and your actual password for the value.
**Note**  
For **Key**, you must only enter `password` (anything else will cause authentication to fail).

   1. Select **Add new key** to create a KMS customer managed key (CMK) in **Encryption key**—the AWS KMS console will open.

   1. Choose **Create key** on the **Customer manged keys** page.

   1. Keep the default values on the **Configure key** page and select **Next**.

   1. Enter a name for your key in **Alias** (optionally, you can add a description and tag), followed by **Next**.

   1. Select any users (other than yourself) or roles you want to permit to administer the key in **Key administrators** followed by **Next**.

   1. Select any users (other than yourself) or roles you want to permit to use the key in **Key users** followed by **Next**.

   1. Copy and paste the [KMS CMK policy](eb-policies.md#eb-policies-ingress-cmk) into the **Key policy** JSON text editor at the `"statement"` level by adding it as an additional statement separated by a comma. Replace the region and account number with your own.

   1. Choose **Finish**.

   1. Select your browser's tab where you have the AWS Secrets Manager **Store a new secret** page open and select the *refresh icon* (circular arrow) next to the **Encryption key** field, then click inside the field and select your newly created key.

   1. Enter a name in the **Secret name** field on the **Configure secret** page.

   1. Select **Edit permissions** in **Resource permissions**.

   1. Copy and paste the [Secrets resource policy](eb-policies.md#eb-policies-ingress-secrets) into the **Resource permissions** JSON text editor and replace the region and account number with your own. (Be sure to delete any example code in the editor.) 

   1. Choose **Save** followed by **Next**. 

   1. Optionally configure rotation followed by **Next**. 

   1. Review and store your new secret by choosing **Store**. 

   1. Select your browser's tab where you have the SES **Create new ingress endpoint** page open and choose **Refresh list**, then select your newly created secret in **Secret ARN**.

1. Select a rule set containing the rule actions you want to perform on the email you allow in.

1. Select a traffic policy to determine the email you want to block or allow.

1. Choose whether it will be a **Public** or **Private** network.
   + For a public network, choose either **IPv4** only or **Dualstack** (IPv4 and IPv6) addressing.
   + For a private network, select or enter a VPC endpoint that you've shared with authorized senders in the same account, such as IAM users or roles. Optionally, you can create a new VPC endpoint by choosing **Create VPC endpoint** to open the Amazon VPC console.

1. Select a TLS policy for your ingress endpoint. The default depends on your region—see [TLS policy](#eb-ingress-tls-policy) for details on available values and restrictions.

1. Select **Create ingress endpoint**.

1. In **General details**, "Provisioning" will be displayed while your ingress endpoint is being created—refresh the page until "Active" is displayed and the **ARecord** field contains a value. Copy the "A" record value and paste it into your DNS configuration or your SMTP client as discussed in [Public endpoint configuration](#eb-ingress-a-record).

1. Just above the **General details** container on the console, there is a large, unlabeled number prefixed by "inp" (also replicated in the breadcrumb trail at the top of the page), for example, **inp-1abc2de3fghi4jkl5mnop6qr**. This is referred to as the *ingress endpoint ID*, its value is used as the *username* to login to your ingress server. (You'll need to share this with your authorized senders to connect to your endpoint.)

1. You can view and manage the ingress endpoints you've already created from the **Ingress endpoints** page. If there's an ingress endpoint you want to remove, select it's radio button followed by **Delete**.

1. To edit an ingress endpoint, select its name to open its summary page:
   + You can change the endpoint's active status or TLS policy (for supported configurations) by choosing **Edit** in **General details** followed by **Save changes**.
   + You can select a different rule set or traffic policy by choosing **Edit** in either **Rule set** or **Traffic policy** followed by **Save changes**.