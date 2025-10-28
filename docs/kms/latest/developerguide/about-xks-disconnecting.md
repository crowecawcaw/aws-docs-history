# Disconnect an external key store

When you disconnect an external key store with [VPC endpoint service connectivity](choose-xks-connectivity.md#xks-vpc-connectivity "choose-xks-connectivity.md#xks-vpc-connectivity") from its external key store proxy, AWS KMS
deletes its interface endpoint to the VPC endpoint service and removes the network
infrastructure that it created to support the connection. No equivalent process is
required for external key stores with public endpoint connectivity. This action does not
affect the VPC endpoint service or any of its supporting components, and it does not
affect the external key store proxy or any external components.

While the external key store is disconnected, AWS KMS does not send any requests to the
external key store proxy. The connection state of the external key store is
`DISCONNECTED`. The KMS keys in the disconnected external key store are
in an [UNAVAILABLE key state](key-state.md "key-state.md") (unless they
are [pending deletion](deleting-keys.md "deleting-keys.md")), which means that they cannot
be used in cryptographic operations. However, you can still view and manage your
external key store and its existing KMS keys.

The disconnected state is designed to be temporary and reversible. You can reconnect
your external key store at any time. Typically, no reconfiguration is necessary.
However, if any properties of the associated external key store proxy have changed while
it was disconnected, such as rotation of its [proxy authentication credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential"), you must [edit the external key store settings](update-xks-keystore.md "update-xks-keystore.md") before
reconnecting.

###### Note

While a custom key store is disconnected, all attempts to create KMS keys in the custom key store or to use existing KMS keys in cryptographic operations will
fail. This action can prevent users from storing and accessing sensitive data.

To better estimate the effect of disconnecting your external key store, identify the
KMS keys in the external key store and [determine their past use](deleting-keys-determining-usage.md "deleting-keys-determining-usage.md").

You might disconnect an external key store for reasons such as the following:

- **To edit its properties.** You can edit the
  custom key store name, proxy URI path, and proxy authentication credential
  while the external key store is connected. However, to edit the proxy
  connectivity type, proxy URI endpoint, or VPC endpoint service name, you must
  first disconnect the external key store. For details, see [Edit external key store properties](update-xks-keystore.md "update-xks-keystore.md").
- **To stop all communication** between AWS KMS and
  the external key store proxy. You can also stop communication between AWS KMS and
  your proxy by disabling your endpoint or VPC endpoint service. In addition, your
  external key store proxy or key management software might provide additional
  mechanisms to prevent AWS KMS from communicating with the proxy or to prevent the
  proxy from accessing your external key manager.
- **To disable all KMS keys** in the external key
  store. You can [disable and re-enable
  KMS keys](enabling-keys.md "enabling-keys.md") in an external key store by using the AWS KMS console or the
  [DisableKey](../APIReference/API_DisableKey.md "../APIReference/API_DisableKey.md") operation.
  These operations complete quickly (subject to eventual consistency), but they
  act on one KMS key at a time. Disconnecting the external key store changes the
  key state of all KMS keys in the external key store to
  `Unavailable`, which prevents them from being used in any
  cryptographic operation.
- **To repair a failed connection attempt**. If an
  attempt to connect an external key store fails (the connection state of the
  custom key store is `FAILED`), you must disconnect the external key
  store before you try to connect it again.

## Disconnect your external key store

You can disconnect your external key store in the AWS KMS console or by using the [DisconnectCustomKeyStore](../APIReference/API_DisconnectCustomKeyStore.md "../APIReference/API_DisconnectCustomKeyStore.md") operation.

You can use the AWS KMS console to connect an external key store to its external key
store proxy. This process takes about 5 minutes to complete.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **External key stores**.
4. Choose the row of the external key store you want to disconnect.
5. From the **Key store actions** menu, choose
   **Disconnect**.
   When the operation completes, the connection state changes from
   **DISCONNECTING** to **DISCONNECTED**. If the
   operation fails, an error message appears that describes the problem and provides help
   on how to fix it. If you need more help, see [External key store connection errors](xks-troubleshooting.md#fix-xks-connection "xks-troubleshooting.md#fix-xks-connection").

To disconnect a connected external key store, use the [DisconnectCustomKeyStore](../APIReference/API_DisconnectCustomKeyStore.md "../APIReference/API_DisconnectCustomKeyStore.md") operation. If the operation is successful, AWS KMS returns an HTTP 200 response and a JSON
object with no properties. The process takes about
five minutes to complete. To find the connection state of the external key store, use
the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md") operation.

The examples in this section use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

This example disconnects an external key store with VPC endpoint service connectivity.
Before running this example, replace the example custom key store ID with a valid
one.

```
`$` `aws kms disconnect-custom-key-store --custom-key-store-id `cks-1234567890abcdef0``
```

To verify that the external key store is disconnected, use the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
operation. By default, this operation returns all custom keys stores in your account and
Region. But you can use either the `CustomKeyStoreId` and
`CustomKeyStoreName` parameter (but not both) to limit the response to
particular custom key stores. The `ConnectionState` value of
`DISCONNECTED` indicates that this example external key store is no
longer connected to its external key store proxy.

```
`$` `aws kms describe-custom-key-stores --custom-key-store-name `ExampleXksVpc``
`{
 "CustomKeyStores": [
 {
 "CustomKeyStoreId": "cks-9876543210fedcba9",
 "CustomKeyStoreName": "ExampleXksVpc",
 **"ConnectionState": "DISCONNECTED",**
 "CreationDate": "2022-12-13T18:34:10.675000+00:00",
 "CustomKeyStoreType": "EXTERNAL_KEY_STORE",
 "XksProxyConfiguration": {
 "AccessKeyId": "ABCDE98765432EXAMPLE",
 "Connectivity": "VPC_ENDPOINT_SERVICE",
 "UriEndpoint": "https://example-proxy-uri-endpoint-vpc",
 "UriPath": "/example/prefix/kms/xks/v1",
 "VpcEndpointServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-example"
 }
 }
 ]
}`
```
