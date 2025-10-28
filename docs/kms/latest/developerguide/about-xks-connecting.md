# Connect an external key store

When your external key store is connected to its external key store proxy, you can
[create KMS keys in your external key store](create-cmk-keystore.md "create-cmk-keystore.md") and use its existing
KMS keys in [cryptographic operations](manage-cmk-keystore.md#use-cmk-keystore "manage-cmk-keystore.md#use-cmk-keystore").

The process that connects an external key store to its external key store proxy
differs based on the connectivity of the external key store.

- When you connect an external key store with [public endpoint connectivity](keystore-external.md#concept-xks-connectivity "keystore-external.md#concept-xks-connectivity"),
  AWS KMS sends a [GetHealthStatus request](keystore-external.md#concept-proxy-apis "keystore-external.md#concept-proxy-apis")
  to the external key store proxy to validate the [proxy URI endpoint](create-xks-keystore.md#require-endpoint "create-xks-keystore.md#require-endpoint"), [proxy URI
  path](create-xks-keystore.md#require-path "create-xks-keystore.md#require-path"), and [proxy authentication
  credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential"). A successful response from the proxy confirms that the
  [proxy URI endpoint](create-xks-keystore.md#require-endpoint "create-xks-keystore.md#require-endpoint") and [proxy URI path](create-xks-keystore.md#require-path "create-xks-keystore.md#require-path") are accurate and accessible,
  and that the proxy authenticated the request signed with the [proxy authentication credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential") for
  the external key store.
- When you connect an external key store with [VPC endpoint service connectivity](choose-xks-connectivity.md#xks-vpc-connectivity "choose-xks-connectivity.md#xks-vpc-connectivity") to
  its external key store proxy, AWS KMS does the following:

      + Confirms that the domain for the private DNS name specified in
       the [proxy URI endpoint](create-xks-keystore.md#require-endpoint "create-xks-keystore.md#require-endpoint")
       is [verified](vpc-connectivity.md#xks-private-dns "vpc-connectivity.md#xks-private-dns").
      + Creates an interface endpoint from an AWS KMS VPC to your VPC endpoint
       service.
      + Creates a private hosted zone for the private DNS name specified in
       the proxy URI endpoint
      + Sends a [GetHealthStatus
       request](keystore-external.md#concept-proxy-apis "keystore-external.md#concept-proxy-apis") to the external key store proxy. A successful
       response from the proxy confirms that the [proxy URI endpoint](create-xks-keystore.md#require-endpoint "create-xks-keystore.md#require-endpoint") and [proxy URI path](create-xks-keystore.md#require-path "create-xks-keystore.md#require-path") are accurate and
       accessible, and that the proxy authenticated the request signed with the
       [proxy authentication
       credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential") for the external key store.

  The connect operation begins the process of connecting your custom key store,
  but connecting an external key store it its external proxy takes approximately
  five minutes. A success response from the connect operation does not indicate
  that the external key store is connected. To confirm that the connection was
  successful, use the AWS KMS console or the [DescribeCustomKeyStores](../APIReference/DescribeCustomKeyStores.md "../APIReference/DescribeCustomKeyStores.md") operation to view the [connection state](xks-connect-disconnect.md#xks-connection-state "xks-connect-disconnect.md#xks-connection-state") of external your key
  store.

When the connection state is `FAILED`, a connection error code is displayed
in the AWS KMS console and is added to the `DescribeCustomKeyStore` response.
For help interpreting connection error codes, see [Connection error codes for external key
stores](xks-troubleshooting.md#xks-connection-error-codes "xks-troubleshooting.md#xks-connection-error-codes").

## Connect and reconnect to your external key store

You can connect, or reconnect, your external key store in the AWS KMS console or by using the [ConnectCustomKeyStore](../APIReference/API_ConnectCustomKeyStore.md "../APIReference/API_ConnectCustomKeyStore.md")
operation.

You can use the AWS KMS console to connect an external key store to its external key
store proxy.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **External key stores**.
4. Choose the row of the external key store you want to connect.

If the [connection state](xks-connect-disconnect.md#xks-connection-state "xks-connect-disconnect.md#xks-connection-state") of the
external key store is **FAILED**, you must [disconnect the external key
store](disconnect-keystore.md#disconnect-keystore-console "disconnect-keystore.md#disconnect-keystore-console") before you connect it. 5. From the **Key store actions** menu, choose
**Connect**.
The connection process typically takes about five minutes to complete.When the
operation completes, the [connection state](xks-connect-disconnect.md#xks-connection-state "xks-connect-disconnect.md#xks-connection-state")
changes to **CONNECTED**.

If the connection state is **Failed**, hover over the connection
state to see the _connection error code_, which
explains the cause of the error. For help responding to a connection error code, see
[Connection error codes for external key
stores](xks-troubleshooting.md#xks-connection-error-codes "xks-troubleshooting.md#xks-connection-error-codes"). To connect an external key store with
a **Failed** connection state, you must first [disconnect the custom key store](disconnect-keystore.md#disconnect-keystore-console "disconnect-keystore.md#disconnect-keystore-console").

To connect a disconnected external key store, use the [ConnectCustomKeyStore](../APIReference/API_ConnectCustomKeyStore.md "../APIReference/API_ConnectCustomKeyStore.md")
operation.

Before connecting, the [connection state](xks-connect-disconnect.md#xks-connection-state "xks-connect-disconnect.md#xks-connection-state") of
the external key store must be `DISCONNECTED`. If the current connection
state is `FAILED`, [disconnect the external
key store](about-xks-disconnecting.md#disconnect-xks-api "about-xks-disconnecting.md#disconnect-xks-api"), and then connect it.

The connection process takes about five minutes to complete. Unless it fails quickly,
`ConnectCustomKeyStore` returns an HTTP 200 response and a JSON object
with no properties. However, this initial response does not indicate that the connection
was successful. To determine whether the external key store is connected, see the
connection state in the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md") response.

The examples in this section use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

To identify the external key store, use its custom key store ID. You can find the ID
on the **Custom key stores** page in the console or by using the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
operation. Before running this example, replace the example ID with a valid one.

```
`$` `aws kms connect-custom-key-store --custom-key-store-id `cks-1234567890abcdef0``
```

The `ConnectCustomKeyStore` operation does not return the
`ConnectionState` in its response. To verify that the external key store
is connected, use the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md") operation. By default, this operation returns all
custom keys stores in your account and Region. But you can use either the
`CustomKeyStoreId` or `CustomKeyStoreName` parameter (but not
both) to limit the response to particular custom key stores. A
`ConnectionState` value of `CONNECTED` indicates that the
external key store is connected to its external key store proxy.

```
`$` `aws kms describe-custom-key-stores --custom-key-store-name `ExampleXksVpc``
`{
 "CustomKeyStores": [
 {
 "CustomKeyStoreId": "cks-9876543210fedcba9",
 "CustomKeyStoreName": "ExampleXksVpc",
 **"ConnectionState": "CONNECTED"**,
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

If the `ConnectionState` value in the `DescribeCustomKeyStores`
response is `FAILED`, the `ConnectionErrorCode` element indicates
the reason for the failure.

In the following example, the `XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND` value
for the `ConnectionErrorCode` indicates that AWS KMS can't find the VPC
endpoint service that it uses to communicate with the external key store proxy. Verify
that the `XksProxyVpcEndpointServiceName` is correct, the AWS KMS service
principal is an allowed principal on the Amazon VPC endpoint service, and that the VPC
endpoint service does not require acceptance of connection requests. For help responding
to a connection error code, see [Connection error codes for external key
stores](xks-troubleshooting.md#xks-connection-error-codes "xks-troubleshooting.md#xks-connection-error-codes").

```
`$` `aws kms describe-custom-key-stores --custom-key-store-name `ExampleXksVpc``
`{
 "CustomKeyStores": [
 {
 "CustomKeyStoreId": "cks-9876543210fedcba9",
 "CustomKeyStoreName": "ExampleXksVpc",
 **"ConnectionState": "FAILED",
 "ConnectionErrorCode": "XKS\_VPC\_ENDPOINT\_SERVICE\_NOT\_FOUND",**
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
