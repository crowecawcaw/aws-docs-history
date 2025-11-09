# Create an external key store

You can create one or many external key stores in each AWS account and Region. Each
external key store must be associated with an external key manager outside of AWS, and an
external key store proxy (XKS proxy) that mediates communication between AWS KMS and your
external key manager. For details, see [Choose an external key store proxy connectivity
option](choose-xks-connectivity.md "choose-xks-connectivity.md"). Before you begin, [confirm that you need an external key
store](keystore-external.md#do-i-need-xks "keystore-external.md#do-i-need-xks"). Most customer can use KMS keys backed by AWS KMS key material.

###### Tip

Some external key managers provide a simpler method for creating an external key
store. For details, see your external key manager documentation.

Before you create your external key store, you need to [assemble the prerequisites](#xks-requirements "#xks-requirements"). During the creation process, you specify the
properties of your external key store. Most importantly, you indicate whether your external
key store in AWS KMS uses a [public
endpoint](choose-xks-connectivity.md#xks-connectivity-public-endpoint "choose-xks-connectivity.md#xks-connectivity-public-endpoint") or a [VPC endpoint service](choose-xks-connectivity.md#xks-vpc-connectivity "choose-xks-connectivity.md#xks-vpc-connectivity") to
connect to its external key store proxy. You also specify the connection details, including
the URI endpoint of the proxy and the path within that proxy endpoint where AWS KMS sends API
requests to the proxy.

###### Considerations

- KMS cannot communicate over IPv6 with External key stores.
- If you use public endpoint connectivity, make sure that AWS KMS can communicate
  with your proxy over the internet using an HTTPS connection. This includes
  configuring TLS on the external key store proxy and ensuring that any firewalls
  between AWS KMS and the proxy allow IPv4 traffic to and from port 443 on the proxy.
  While creating an external key store with public endpoint connectivity, AWS KMS tests
  the connection by sending a status request to the external key store proxy. This
  test verifies that the endpoint is reachable and that your external key store proxy
  will accept a request signed with your [external key store proxy authentication credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential"). If this test request
  fails, the operation to create the external key store fails.
- If you use VPC endpoint service connectivity, make sure that the network load
  balancer, private DNS name, and VPC endpoint service are configured correctly and
  operational. If the external key store proxy isn't in the VPC, you need to ensure
  that the VPC endpoint service can communicate with the external key store proxy.
  (AWS KMS tests VPC endpoint service connectivity when you [connect the external key store](xks-connect-disconnect.md "xks-connect-disconnect.md") to its
  external key store proxy.)
- AWS KMS records [Amazon CloudWatch metrics and dimensions](monitoring-cloudwatch.md#kms-metrics "monitoring-cloudwatch.md#kms-metrics")
  especially for external key stores. Monitoring graphs based on some of these metrics
  appear in the AWS KMS console for each external key store. We strongly recommend that
  you use these metrics to create alarms that monitor your external key store. These
  alarms alert you to early signs of performance and operational problems before they
  occur. For instructions, see [Monitor external key stores](xks-monitoring.md "xks-monitoring.md").
- External key stores are subject to [resource
  quotas](resource-limits.md#cks-resource-quota "resource-limits.md#cks-resource-quota"). Use of KMS keys in an external key store are subject to [request quotas](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores"). Review these quotas before
  designing your external key store implementation.

###### Note

Review your configuration for circular dependencies that might prevent it from
working.

For example, if you create your external key store proxy using AWS resources, make
sure that operating the proxy does not require the availability of a KMS key in an
external key store that is accessed via that proxy.

All new external key stores are created in a disconnected state. Before you can create
KMS keys your external key store, you must [connect
it](about-xks-connecting.md "about-xks-connecting.md") to its external key store proxy. To change the properties of your external key
store, [edit your external key store
settings](update-xks-keystore.md "update-xks-keystore.md").

###### Topics

- [Assemble the prerequisites](#xks-requirements "#xks-requirements")
- [Create a new external key store](#create-xks "#create-xks")

## Assemble the prerequisites

Before you create an external key store, you need to assemble the required components,
including the [external key manager](keystore-external.md#concept-ekm "keystore-external.md#concept-ekm") that you will use
to support the external key store and the [external key
store proxy](keystore-external.md#concept-xks-proxy "keystore-external.md#concept-xks-proxy") that translates AWS KMS requests into a format that your external
key manager can understand.

The following components are required for all external key stores. In addition to
these components, you need to provide the components to support the [external key store proxy connectivity
option](choose-xks-connectivity.md "choose-xks-connectivity.md") that you choose.

###### Tip

Your external key manager might include some of these components, or they might be
configured for you. For details, see your external key manager documentation.

If you are creating your external key store in the AWS KMS console, you have the
option to upload a JSON-based [proxy
configuration file](#proxy-configuration-file "#proxy-configuration-file") that specifies the [proxy
URI path](#require-path "#require-path") and [proxy authentication
credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential"). Some external key store proxies generate this file for you.
For details, see the documentation for your external key store proxy or external key
manager.

### External key manager

Each external key store requires at least one [external
key manager](keystore-external.md#concept-ekm "keystore-external.md#concept-ekm") instance. This can be a physical or virtual hardware security
module (HSM), or key management software.

You can use a single key manager, but we recommend at least two related key
manager instances that share cryptographic keys for redundancy. The external key
store does not require exclusive use of the external key manager. However, the
external key manager must have the capacity to handle the expected frequency of
encryption and decryption requests from the AWS services that use KMS keys in
the external key store to protect your resources. Your external key manager should
be configured to handle up to 1800 requests per second and to respond within the 250
millisecond timeout for each request. We recommend that you locate the external key
manager close to an AWS Region so that the network round-trip time (RTT) is 35
milliseconds or less.

If your external key store proxy allows it, you can change the external key
manager that you associate with your external key store proxy, but the new external
key manager must be a backup or snapshot with the same key material. If the external
key that you associate with a KMS key is no longer available to your external key
store proxy, AWS KMS cannot decrypt the ciphertext encrypted with the
KMS key.

The external key manager must be accessible to the external key store proxy. If
the [GetHealthStatus](keystore-external.md#xks-concepts "keystore-external.md#xks-concepts") response from the proxy
reports that all external key manager instances are `Unavailable`, all
attempts to create an external key store fail with an [XksProxyUriUnreachableException](xks-troubleshooting.md#fix-xks-proxy "xks-troubleshooting.md#fix-xks-proxy").

### External key store proxy

You must specify an [external key store
proxy](keystore-external.md#concept-xks-proxy "keystore-external.md#concept-xks-proxy") (XKS proxy) that conforms to the design requirements in the [AWS KMS External Key Store Proxy API Specification](https://github.com/aws/aws-kms-xksproxy-api-spec/ "https://github.com/aws/aws-kms-xksproxy-api-spec/"). You can develop or buy an
external key store proxy, or use an external key store proxy provided by or built
into your external key manager. AWS KMS recommends that your external key store proxy
be configured to handle up to 1800 requests per second and respond within the 250
millisecond timeout for each request. We recommend that you locate the external key
manager close to an AWS Region so that the network round-trip time (RTT) is 35
milliseconds or less.

You can use an external key store proxy for more than one external key store, but
each external key store must have a unique URI endpoint and path within the external
key store proxy for its requests.

If you are using VPC endpoint service connectivity, you can locate your external
key store proxy in your Amazon VPC, but that is not required. You can locate your proxy
outside of AWS, such as in your private data center, and use the VPC endpoint
service only to communicate with the proxy.

### Proxy authentication credential

To create an external key store, you must specify your external key store proxy
authentication credential (`XksProxyAuthenticationCredential`).

You must establish an [authentication
credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential") (`XksProxyAuthenticationCredential`) for AWS KMS on
your external key store proxy. AWS KMS authenticates to your proxy by signing its
requests using the [Signature
Version 4 (SigV4) process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") with the external key store proxy
authentication credential. You specify the authentication credential when you create
your external key store and [you can change
it](update-xks-keystore.md "update-xks-keystore.md") at any time. If your proxy rotates your credential, be sure to update
the credential values for your external key store.

The proxy authentication credential has two parts. You must provide both parts for
your external key store.

- Access key ID: Identifies the secret access key. You can provide this ID
  in plain text.
- Secret access key: The secret part of the credential. AWS KMS encrypts the
  secret access key in the credential before storing it.

The SigV4 credential that AWS KMS uses to sign requests to the external key store
proxy are unrelated to any SigV4 credentials associated with any AWS Identity and Access Management
principals in your AWS accounts. Do not reuse any IAM SigV4 credentials for your
external key store proxy.

### Proxy connectivity

To create an external key store, you must specify your external key store proxy
connectivity option (`XksProxyConnectivity`).

AWS KMS can communicate with your external key store proxy by using a [public endpoint](choose-xks-connectivity.md#xks-connectivity-public-endpoint "choose-xks-connectivity.md#xks-connectivity-public-endpoint") or an [Amazon Virtual Private Cloud (Amazon VPC) endpoint service](choose-xks-connectivity.md#xks-vpc-connectivity "choose-xks-connectivity.md#xks-vpc-connectivity"). While
a public endpoint is simpler to configure and maintain, it might not meet the
security requirements for every installation. If you choose the Amazon VPC endpoint
service connectivity option, you must create and maintain the required components,
including an Amazon VPC with at least two subnets in two different Availability Zones, a
VPC endpoint service with a network load balancer and target group, and a private
DNS name for the VPC endpoint service.

You can [change the proxy connectivity
option](update-xks-keystore.md "update-xks-keystore.md") for your external key store. However, you must ensure that the
continued availability of the key material associated with the KMS keys in your
external key store. Otherwise, AWS KMS cannot decrypt any ciphertext encrypted with
those KMS keys.

For help deciding which proxy connectivity option is best for your external key
store, see [Choose an external key store proxy connectivity
option](choose-xks-connectivity.md "choose-xks-connectivity.md"). For help creating an configuring VPC
endpoint service connectivity, see [Configure VPC endpoint service connectivity](vpc-connectivity.md "vpc-connectivity.md").

### Proxy URI endpoint

To create an external key store, you must specify the endpoint
(`XksProxyUriEndpoint`) that AWS KMS uses to send requests to the
external key store proxy.

The protocol must be HTTPS. AWS KMS communicates over IPv4 on port 443. Do not specify the port in the proxy URI endpoint value.

- [Public endpoint
  connectivity](choose-xks-connectivity.md#xks-connectivity-public-endpoint "choose-xks-connectivity.md#xks-connectivity-public-endpoint") — Specify the publicly available endpoint for
  your external key store proxy. This endpoint must be reachable before you
  create your external key store.
- [VPC endpoint service
  connectivity](choose-xks-connectivity.md#xks-vpc-connectivity "choose-xks-connectivity.md#xks-vpc-connectivity") — Specify `https://` followed by
  the private DNS name of the VPC endpoint service.

The TLS server certificate configured on the external key store proxy must match
the domain name in the external key store proxy URI endpoint and be issued by a
certificate authority supported for external key stores. For a list, see [Trusted Certificate Authorities](https://github.com/aws/aws-kms-xksproxy-api-spec/blob/main/TrustedCertificateAuthorities "https://github.com/aws/aws-kms-xksproxy-api-spec/blob/main/TrustedCertificateAuthorities"). Your certificate authority will
require proof of domain ownership before issuing the TLS certificate.

The subject common name (CN) on the TLS certificate must match the private DNS
name. For example, if the private DNS name is
`myproxy-private.xks.example.com`, the CN on the TLS certificate must be
`myproxy-private.xks.example.com` or `*.xks.example.com`.

You can [change your proxy URI endpoint](update-xks-keystore.md "update-xks-keystore.md"),
but be sure that the external key store proxy has access to the key material
associated with the KMS keys in your external key store. Otherwise, AWS KMS cannot
decrypt any ciphertext encrypted with those KMS keys.

**Uniqueness requirements**

- The combined proxy URI endpoint (`XksProxyUriEndpoint`) and
  proxy URI path (`XksProxyUriPath`) value must be unique in the
  AWS account and Region.
- External key stores with public endpoint connectivity can share the same
  proxy URI endpoint, provided that they have different proxy URI path
  values.
- An external key store with public endpoint connectivity cannot use the
  same proxy URI endpoint value as any external key store with VPC endpoint
  services connectivity in the same AWS Region, even if the key stores are
  in different AWS accounts.
- Each external key store with VPC endpoint connectivity must have its own
  private DNS name. The proxy URI endpoint (private DNS name) must be unique
  in the AWS account and Region.

### Proxy URI path

To create an external key store, you must specify the base path in your external
key store proxy to the [required proxy
APIs](keystore-external.md#concept-proxy-apis "keystore-external.md#concept-proxy-apis"). The value must start with `/` and must end with
/kms/xks/v1 where `v1` represents the version of the AWS KMS
API for the external key store proxy. This path can include an optional prefix
between the required elements such as `/example-prefix/kms/xks/v1`.
To find this value, see the documentation for your external key store proxy.

AWS KMS sends proxy requests to the address specified by the concatenation of the
proxy URI endpoint and proxy URI path. For example, if the proxy URI endpoint is
`https://myproxy.xks.example.com` and the proxy URI path is
`/kms/xks/v1`, AWS KMS sends its proxy API requests to
`https://myproxy.xks.example.com/kms/xks/v1`.

You can [change your proxy URI path](update-xks-keystore.md "update-xks-keystore.md"), but
be sure that the external key store proxy has access to the key material associated
with the KMS keys in your external key store. Otherwise, AWS KMS cannot decrypt any
ciphertext encrypted with those KMS keys.

**Uniqueness requirements**

- The combined proxy URI endpoint (`XksProxyUriEndpoint`) and
  proxy URI path (`XksProxyUriPath`) value must be unique in the
  AWS account and Region.

### VPC endpoint service

Specifies the name of the Amazon VPC endpoint service that is used to communicate with
your external key store proxy. This component is required only for external key
stores that use VPC endpoint service connectivity. For help setting up and
configuring your VPC endpoint service for an external key store, see [Configure VPC endpoint service connectivity](vpc-connectivity.md "vpc-connectivity.md").

The VPC endpoint service must have the following properties:

- The VPC endpoint service can reside in the same or a different
  AWS account as the external key store.
  - The VPC endpoint service must reside in the same AWS Region as
    the external key store.
  - You'll need to provide the AWS account ID of the VPC endpoint
    service if it resides in a different AWS account.

- It must have a network load balancer (NLB) connected to at least two
  subnets, each in a different Availability Zone.
- The _allow principals list_ for the VPC
  endpoint service must include the AWS KMS service principal for the Region:
  `cks.kms.`<region>`.amazonaws.com`,
  such as
  `cks.kms.`us-east-1`.amazonaws.com`.
  - If your Amazon VPC endpoint service is owned by a different AWS account other than the AWS account owning the external key store (XKS), you’ll also need to allow XKS access to the VPC endpoint service.
    To do so, [allowlist the XKS AWS account ID as a principal](../../../vpc/latest/privatelink/configure-endpoint-service.md#add-remove-permissions "../../../vpc/latest/privatelink/configure-endpoint-service.md#add-remove-permissions") for the Amazon VPC endpoint

  service.

- It must not require acceptance of connection requests.
- It must have a private DNS name within a higher level public domain. For
  example, you could have a private DNS name of myproxy-private.xks.example.com in
  the public `xks.example.com` domain.

The private DNS name for an external key store with VPC endpoint service
connectivity must be unique in its AWS Region.

- The [domain verification status](vpc-connectivity.md#xks-private-dns "vpc-connectivity.md#xks-private-dns") of
  the private DNS name domain must be `verified`.
- The TLS server certificate configured on the external key store proxy must
  specify the private DNS hostname at which the endpoint is reachable.

**Uniqueness requirements**

- External key stores with VPC endpoint connectivity can share an
  `Amazon VPC`, but each external key store must have its own
  VPC endpoint service and private DNS name.

### Proxy configuration file

A _proxy configuration file_ is an optional
JSON-based file that contains values for the [proxy URI
path](#require-path "#require-path") and [proxy authentication
credential](#require-credential "#require-credential") properties of your external key store. When creating or [editing an external key store](update-xks-keystore.md "update-xks-keystore.md") in the AWS KMS
console, you can upload a proxy configuration file to supply configuration values
for your external key store. Using this file avoids typing and pasting errors, and
ensures that the values in your external key store match the values in your external
key store proxy.

Proxy configuration files are generated by the external key store proxy. To learn
whether your external key store proxy offers a proxy configuration file, see your
external key store proxy documentation.

The following is an example of a well-formed proxy configuration file with
fictitious values.

```
{
  "XksProxyUriPath": "/example-prefix/kms/xks/v1",
  "XksProxyAuthenticationCredential": {
    "AccessKeyId": "ABCDE12345670EXAMPLE",
    "RawSecretAccessKey": "0000EXAMPLEFA5FT0mCc3DrGUe2sti527BitkQ0Zr9MO9+vE="
  }
}
```

You can upload a proxy configuration file only when creating or editing an
external key store in the AWS KMS console. You cannot use it with the [CreateCustomKeyStore](../APIReference/API_CreateCustomKeyStore.md "../APIReference/API_CreateCustomKeyStore.md") or
[UpdateCustomKeyStore](../APIReference/API_UpdateCustomKeyStore.md "../APIReference/API_UpdateCustomKeyStore.md") operations, but you can use the values in the
proxy configuration file to ensure that your parameter values are correct.

## Create a new external key store

Once you've assembled the necessary prerequisites, you can create a new external key
store in the AWS KMS console or by using the [CreateCustomKeyStore](../APIReference/API_CreateCustomKeyStore.md "../APIReference/API_CreateCustomKeyStore.md")
operation.

Before creating an external key store, [choose your proxy connectivity type](choose-xks-connectivity.md "choose-xks-connectivity.md") and ensure that you have created
and configured all of the [required
components](#xks-requirements "#xks-requirements"). If you need help finding any of the required values,
consult the documentation for your external key store proxy or key management
software.

###### Note

When you create an external key store in the AWS Management Console, you can upload a
JSON-based _proxy configuration file_ with
values for the [proxy URI path](#require-path "#require-path") and [proxy authentication credential](#require-credential "#require-credential").
Some proxies generate this file for you. It is not required.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **External key stores**.
4. Choose **Create external key store**.
5. Enter a friendly name for the external key store. The name must be
   unique among all external key stores in your account.

###### Important

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output. 6. Choose your [proxy
connectivity](#require-connectivity "#require-connectivity") type.

Your proxy connectivity choice determines the [components required](#xks-requirements "#xks-requirements") for your
external key store proxy. For help making this choice, see [Choose an external key store proxy connectivity
option](choose-xks-connectivity.md "choose-xks-connectivity.md").

    1. Select **Cross-account VPC endpoint service**
     if your VPC endpoint service resides in a different
     AWS account. Then enter the AWS account ID for the VPC
     endpoint owner in the **VPC endpoint service owner
     account ID** field.
    2. Choose or enter the name of the [VPC endpoint
     service](#require-vpc-service-name "#require-vpc-service-name") for this external key store. This step only
     appears when your external key store proxy connectivity type is
     **VPC endpoint service**.


    The VPC endpoint service and its VPCs must fulfill the
     requirements for an external key store. For details, see [Assemble the prerequisites](#xks-requirements "#xks-requirements").

7. Choose or enter the name of the [VPC endpoint service](#require-vpc-service-name "#require-vpc-service-name") for
   this external key store. This step appears only when your external key
   store proxy connectivity type is **VPC endpoint
   service**.

The VPC endpoint service and its VPCs must fulfill the requirements
for an external key store. For details, see [Assemble the prerequisites](#xks-requirements "#xks-requirements"). 8. Enter your [proxy URI endpoint](#require-endpoint "#require-endpoint").
The protocol must be HTTPS. AWS KMS communicates over IPv4 on port 443. Do not specify the port in the proxy URI endpoint value.

If AWS KMS recognizes the VPC endpoint service that you specified in the
previous step, it completes this field for you.

For public endpoint connectivity, enter a publicly available endpoint
URI. For VPC endpoint connectivity, enter `https://` followed
by the private DNS name of the VPC endpoint service. 9. To enter the values for the [proxy URI
path](#require-path "#require-path") prefix and [proxy
authentication credential](#require-credential "#require-credential"), upload a proxy configuration file,
or enter the values manually.

    * If you have an optional [proxy configuration
     file](#proxy-configuration-file "#proxy-configuration-file") that contains values for your [proxy URI path](#require-path.title "#require-path.title") and [proxy authentication
     credential](#require-credential "#require-credential"), choose **Upload configuration
     file**. Follow the steps to upload the file.


    When the file is uploaded, the console displays the values
     from the file in editable fields. You can change the values now
     or [edit these values](update-xks-keystore.md "update-xks-keystore.md")
     after the external key store is created.


    To display the value of the secret access key, choose
     **Show secret access key**.
    * If you don't have a proxy configuration file, you can enter
     the proxy URI path and proxy authentication credential values
     manually.


    	1. If you don't have a proxy configuration file, you can
    	 enter your proxy URI manually. The console supplies the
    	 required **/kms/xks/v1** value.


    	If your [proxy URI
    	 path](#require-path "#require-path") includes an optional prefix, such as the
    	 `example-prefix` in
    	 `/`example-prefix`/kms/xks/v1`,
    	 enter the prefix in the **Proxy URI path
    	 prefix** field. Otherwise, leave the field
    	 empty.
    	2. If you don't have a proxy configuration file, you can
    	 enter your [proxy
    	 authentication credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential") manually. Both the
    	 access key ID and secret access key are required.




    		+ In **Proxy credential: Access key
    		 ID**, enter the access key ID of the
    		 proxy authentication credential. The access key ID
    		 identifies the secret access key.
    		+ In **Proxy credential: Secret access
    		 key**, enter the secret access key of the
    		 proxy authentication credential.
    	To display the value of the secret access key, choose
    	 **Show secret access key**.


    	This procedure does not set or change the
    	 authentication credential you established on your
    	 external key store proxy. It just associates these
    	 values with your external key store. For information
    	 about setting, changing, and your rotating proxy
    	 authentication credential, see the documentation for
    	 your external key store proxy or key management
    	 software.


    	If your proxy authentication credential changes, [edit the credential
    	 setting](update-xks-keystore.md "update-xks-keystore.md") for your external key store.

10. Choose **Create external key store**.
    When the procedure is successful, the new external key store appears in the
    list of external key stores in the account and Region. If it is unsuccessful, an
    error message appears that describes the problem and provides help on how to fix
    it. If you need more help, see [CreateKey errors for the external
    key](xks-troubleshooting.md#fix-external-key-create "xks-troubleshooting.md#fix-external-key-create").

**Next**: New external key stores are not
automatically connected. Before you can create AWS KMS keys in your external
key store, you must [connect the external
key store](xks-connect-disconnect.md "xks-connect-disconnect.md") to its external key store proxy.

You can use the [CreateCustomKeyStore](../APIReference/API_CreateCustomKeyStore.md "../APIReference/API_CreateCustomKeyStore.md") operation to create a new external key store.
For help finding the values for the required parameters, see the documentation
for your external key store proxy or key management software.

###### Tip

You cannot upload a [proxy
configuration file](#proxy-configuration-file "#proxy-configuration-file") when using the
`CreateCustomKeyStore` operation. However, you can use the
values in the proxy configuration file to ensure that your parameter values
are correct.

To create an external key store, the `CreateCustomKeyStore`
operation requires the following parameter values.

- `CustomKeyStoreName` – A friendly name for the
  external key store that is unique in the account.

###### Important

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

- `CustomKeyStoreType` — Specify
  `EXTERNAL_KEY_STORE`.
- [XksProxyConnectivity](#require-connectivity "#require-connectivity") – Specify
  `PUBLIC_ENDPOINT` or
  `VPC_ENDPOINT_SERVICE`.
- [XksProxyAuthenticationCredential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential") —
  Specify both the access key ID and the secret access key.
- [XksProxyUriEndpoint](#require-endpoint "#require-endpoint") — The endpoint that
  AWS KMS uses to communicate with your external key store proxy.
- [XksProxyUriPath](#require-path "#require-path")
  — The path within the proxy to the proxy APIs.
- [XksProxyVpcEndpointServiceName](#require-vpc-service-name "#require-vpc-service-name") —
  Required only when your `XksProxyConnectivity` value is
  `VPC_ENDPOINT_SERVICE`.

###### Note

If you use AWS CLI version 1.0, run the following command before specifying a
parameter with an HTTP or HTTPS value, such as the `XksProxyUriEndpoint`
parameter.

```
aws configure set cli_follow_urlparam false
```

Otherwise, AWS CLI version 1.0 replaces the parameter value with the content found
at that URI address, causing the following error:

```
Error parsing parameter '--xks-proxy-uri-endpoint': Unable to retrieve
https:// : received non 200 status code of 404
```

The following examples use fictitious values. Before running the command,
replace them with valid values for your external key store.

Create an external key store with public endpoint connectivity.

```
`$` `aws kms create-custom-key-store
 --custom-key-store-name `ExampleExternalKeyStorePublic` \
 --custom-key-store-type EXTERNAL_KEY_STORE \
 --xks-proxy-connectivity PUBLIC_ENDPOINT \
 --xks-proxy-uri-endpoint `https://myproxy.xks.example.com` \
 --xks-proxy-uri-path `/kms/xks/v1` \
 --xks-proxy-authentication-credential AccessKeyId=`<value>`,RawSecretAccessKey=`<value>``
```

Create an external key store with VPC endpoint service connectivity.

```
`$` `aws kms create-custom-key-store
 --custom-key-store-name `ExampleExternalKeyStoreVPC` \
 --custom-key-store-type EXTERNAL_KEY_STORE \
 --xks-proxy-connectivity VPC_ENDPOINT_SERVICE \
 --xks-proxy-vpc-endpoint-service-name `com.amazonaws.vpce.us-east-1.vpce-svc-example` \
 --xks-proxy-uri-endpoint `https://myproxy-private.xks.example.com` \
 --xks-proxy-uri-path `/kms/xks/v1` \
 --xks-proxy-authentication-credential AccessKeyId=`<value>`,RawSecretAccessKey=`<value>``
```

When the operation is successful, `CreateCustomKeyStore` returns
the custom key store ID, as shown in the following example response.

```
`{
 "CustomKeyStoreId": cks-1234567890abcdef0
}`
```

If the operation fails, correct the error indicated by the exception, and try
again. For additional help, see [Troubleshooting external key stores](xks-troubleshooting.md "xks-troubleshooting.md").

**Next**: To use the external key store, [connect it to its external key store
proxy](xks-connect-disconnect.md "xks-connect-disconnect.md").
