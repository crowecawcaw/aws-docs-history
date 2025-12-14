# Edit external key store properties

You can edit selected properties of an existing external key store.

You can edit some properties while the external key store is connected or disconnected.
For other properties, you must first [disconnect your
external key store](xks-connect-disconnect.md "xks-connect-disconnect.md") from its external key store proxy. The [connection state](xks-connect-disconnect.md#xks-connection-state "xks-connect-disconnect.md#xks-connection-state") of the external key store must be
`DISCONNECTED`. While your external key store is disconnected, you can manage
the key store and its KMS keys, but you cannot create or use KMS keys in the external
key store. To find the [connection state](xks-connect-disconnect.md#xks-connection-state "xks-connect-disconnect.md#xks-connection-state") of your
external key store, use the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md") operation or see the **General
configuration** section on the detail page for the external key store.

Before updating the properties your external key store, AWS KMS sends a [GetHealthStatus](keystore-external.md#concept-proxy-apis "keystore-external.md#concept-proxy-apis") request to the external key store
proxy using the new values. If the request succeeds, it indicates that you can connect and
authenticate to an external key store proxy with the updated property values. If the request
fails, the edit operation fails with an exception that identifies the error.

When the edit operation completes, the updated property values for your external key store
appear in the AWS KMS console and the `DescribeCustomKeyStores` response. However,
it can take up to five minutes for the changes to be fully effective.

If you edit your external key store in the AWS KMS console, you have the option to upload a
JSON-based [proxy configuration file](create-xks-keystore.md#proxy-configuration-file "create-xks-keystore.md#proxy-configuration-file") that
specifies the [proxy URI path](create-xks-keystore.md#require-path "create-xks-keystore.md#require-path") and [proxy authentication credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential"). Some external
key store proxies generate this file for you. For details, see the documentation for your
external key store proxy or external key manager.

###### Warning

The updated property values must connect your external key store to a proxy for the
same external key manager as the previous values, or for a backup or snapshot of the
external key manager with the same cryptographic keys. If your external key store
permanently loses its access to the external keys associated with its KMS keys,
ciphertext encrypted under those external keys is unrecoverable. In particular, changing
the proxy connectivity of an external key store can prevent AWS KMS from accessing your
external keys.

###### Tip

Some external key managers provide a simpler method for editing external key store
properties. For details, see your external key manager documentation.

You can change the following properties of an external key store.

| Editable external key store properties                                                                                                                                                                                                                                                                          | Any connection state                                   | Require Disconnected state                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| Custom key store name A required friendly name for a custom key<br>store.ImportantDo not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.                                                                             | Green checkmark icon indicating success or completion. |                                                        |
| [Proxy authentication<br>credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential") (XksProxyAuthenticationCredential)(You must<br>specify both the access key ID and the secret access key, even if you<br>are changing only one element.)                         | Green checkmark icon indicating success or completion. |                                                        |
| [Proxy URI path](create-xks-keystore.md#require-path "create-xks-keystore.md#require-path")<br>(XksProxyUriPath)                                                                                                                                                                                                | Green checkmark icon indicating success or completion. |                                                        |
| [Proxy connectivity](keystore-external.md#concept-xks-connectivity "keystore-external.md#concept-xks-connectivity")<br>(XksProxyConnectivity)(You must also update the proxy URI<br>endpoint. If you are changing to VPC endpoint service connectivity, you<br>must specify a proxy VPC endpoint service name.) |                                                        | Green checkmark icon indicating success or completion. |
| [Proxy URI endpoint](create-xks-keystore.md#require-endpoint "create-xks-keystore.md#require-endpoint")<br>(XksProxyUriEndpoint)If you change the proxy endpoint URI, you<br>might also need to change the associated TLS certificate.                                                                          |                                                        | Green checkmark icon indicating success or completion. |
| [Proxy VPC endpoint service<br>name](create-xks-keystore.md#require-vpc-service-name "create-xks-keystore.md#require-vpc-service-name") (XksProxyVpcEndpointServiceName)(This field is<br>required for VPC endpoint service connectivity)                                                                       |                                                        | Green checkmark icon indicating success or completion. |
| [VPC endpoint service owner](create-xks-keystore.md#require-vpc-service-name "create-xks-keystore.md#require-vpc-service-name") (XksProxyVpcEndpointServiceOwner)(This field is<br>required for VPC endpoint service connectivity)                                                                              |                                                        | Green checkmark icon indicating success or completion. |

## Edit your external key store's properties

You can edit your external key store's properties in the AWS KMS console or by using the
[UpdateCustomKeyStore](../APIReference/API_UpdateCustomKeyStore.md "../APIReference/API_UpdateCustomKeyStore.md")
operation.

When you edit a key store, you can change any of the editable values. Some
changes require that the external key store be disconnected from its external
key store proxy.

If you are editing the proxy URI path or proxy authentication credential, you
can enter the new values or upload an external key store [proxy configuration file](create-xks-keystore.md#proxy-configuration-file "create-xks-keystore.md#proxy-configuration-file") that
includes the new values.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **External key stores**.
4. Choose the key store you want to edit.
   1. If necessary, disconnect the external key store from its external key
      store proxy. From the **Key store actions** menu,
      choose **Disconnect**.

5. From the **Key store actions** menu, choose
   **Edit**.
6. Change one or more of the editable external key store properties. You
   can also upload an external key store [proxy configuration file](create-xks-keystore.md#proxy-configuration-file "create-xks-keystore.md#proxy-configuration-file")
   with values for the proxy URI path and proxy authentication
   credential.You can use a proxy configuration file even if some values
   specified in the file haven't changed.
7. Choose **Update external key store**.
8. Review the warning, and if you decide to continue, confirm the
   warning, and then choose **Update external key
   store**.

When the procedure is successful, a message describes the properties
that you edited. When it is unsuccessful, an error message appears that
describes the problem and provides help on how to fix it. 9. If necessary, reconnect the external key store. From the **Key
store actions** menu, choose
**Connect**.

You can leave the external key store disconnected. But while it is
disconnected, you cannot create KMS keys in the external key store or
use the KMS keys in the external key store in [cryptographic operations](manage-cmk-keystore.md#use-cmk-keystore "manage-cmk-keystore.md#use-cmk-keystore").
To change the properties of an external key store, use the [UpdateCustomKeyStore](../APIReference/API_UpdateCustomKeyStore.md "../APIReference/API_UpdateCustomKeyStore.md") operation. You can change multiple properties
of an external key store in the same operation. If the operation is successful, AWS KMS returns an HTTP 200 response and a JSON
object with no properties.

Use the `CustomKeyStoreId` parameter to identify the external key
store. Use the other parameters to change the properties. You cannot use a [proxy configuration file](create-xks-keystore.md#proxy-configuration-file "create-xks-keystore.md#proxy-configuration-file") with the
`UpdateCustomKeyStore` operation. The proxy configuration file is
supported only by the AWS KMS console. However, you can use the proxy
configuration file to help you determine the correct parameter values for your
external key store proxy.

The examples in this section use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

Before you begin, [if necessary](update-xks-keystore.md "update-xks-keystore.md"),
[disconnect the external key
store](xks-connect-disconnect.md "xks-connect-disconnect.md") from its external key store proxy. After updating, if
necessary, you can [reconnect the external
key store](xks-connect-disconnect.md "xks-connect-disconnect.md") to its external key store proxy. You can leave the external
key store in the disconnected state, but you must reconnect it before you can
create new KMS keys in the key store or use existing KMS keys in the key
store for cryptographic operations.

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

#### Change the name of the external key

store

The first example uses the [UpdateCustomKeyStore](../APIReference/API_UpdateCustomKeyStore.md "../APIReference/API_UpdateCustomKeyStore.md") operation to change the friendly name of
the external key store to `XksKeyStore`. The command uses the
`CustomKeyStoreId` parameter to identify the custom key store
and the `CustomKeyStoreName` to specify the new name for the
custom key store. Replace all example values with actual values for your
external key store.

```
`$` `aws kms update-custom-key-store --custom-key-store-id `cks-1234567890abcdef0` --new-custom-key-store-name `XksKeyStore``
```

#### Change the proxy authentication

credential

The following example updates the proxy authentication credential that
AWS KMS uses to authenticate to the external key store proxy. You can use a
command like this one to update the credential if it is rotated on your
proxy.

Update the credential on your external key store proxy first. Then use
this feature to report the change to AWS KMS. (Your proxy will briefly support
both the old and new credential so you have time to update your credential
in AWS KMS.)

You must always specify both the access key ID and the secret access key
in the credential, even if only one value is changed.

The first two commands set variables to hold the credential values. The
`UpdateCustomKeyStore` operations uses the
`CustomKeyStoreId` parameter to identify the external key
store. It uses the `XksProxyAuthenticationCredential` parameter
with its `AccessKeyId` and `RawSecretAccessKey` fields
to specify the new credential. Replace all example values with actual values
for your external key store.

```
`$` `accessKeyID=`access key id``
`$` `secretAccessKey=`secret access key``

`$` `aws kms update-custom-key-store --custom-key-store-id `cks-1234567890abcdef0` \
 --xks-proxy-authentication-credential \
 AccessKeyId=`$accessKeyId`,RawSecretAccessKey=`$secretAccessKey``
```

#### Change the proxy URI path

The following example updates the proxy URI path
(`XksProxyUriPath`). The combination of the proxy URI
endpoint and the proxy URI path must be unique in the AWS account and
Region. Replace all example values with actual values for your external key
store.

```
`$` `aws kms update-custom-key-store --custom-key-store-id `cks-1234567890abcdef0` \
 --xks-proxy-uri-path `/kms/xks/v1``
```

#### Change to VPC endpoint service

connectivity

The following example uses the [UpdateCustomKeyStore](../APIReference/API_UpdateCustomKeyStore.md "../APIReference/API_UpdateCustomKeyStore.md") operation to change the external key store
proxy connectivity type to `VPC_ENDPOINT_SERVICE`. To make this
change, you must specify the required values for VPC endpoint service
connectivity, including the VPC endpoint service name
(`XksProxyVpcEndpointServiceName`) and a proxy URI endpoint
(`XksProxyUriEndpoint`) value that includes the private DNS
name for the VPC endpoint service. Replace all example values with actual
values for your external key store.

```
`$` `aws kms update-custom-key-store --custom-key-store-id `cks-1234567890abcdef0` \
 --xks-proxy-connectivity "VPC_ENDPOINT_SERVICE" \
 --xks-proxy-uri-endpoint `https://myproxy-private.xks.example.com` \
 --xks-proxy-vpc-endpoint-service-name `com.amazonaws.vpce.us-east-1.vpce-svc-example``
```

#### Change to public endpoint

connectivity

The following example changes the external key store proxy connectivity
type to `PUBLIC_ENDPOINT`. When you make this change, you must
update the proxy URI endpoint (`XksProxyUriEndpoint`) value.
Replace all example values with actual values for your external key
store.

###### Note

VPC endpoint connectivity provides greater security than public
endpoint connectivity. Before changing to public endpoint connectivity,
consider other options, including locating your external key store proxy
on premises and using the VPC only for communication.

```
`$` `aws kms update-custom-key-store --custom-key-store-id `cks-1234567890abcdef0` \
 --xks-proxy-connectivity "PUBLIC_ENDPOINT" \
 --xks-proxy-uri-endpoint https://myproxy.xks.example.com`
```
