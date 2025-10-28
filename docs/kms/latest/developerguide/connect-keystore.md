# Connect an AWS CloudHSM key store

New AWS CloudHSM key stores are not connected. Before you can create and use AWS KMS keys in
your AWS CloudHSM key store, you need to connect it to its associated AWS CloudHSM cluster. You can connect
and disconnect your AWS CloudHSM key store at any time, and [view
its connection state](view-keystore.md#view-keystore-console "view-keystore.md#view-keystore-console").

You are not required to connect your AWS CloudHSM key store. You can leave an AWS CloudHSM key store in a
disconnected state indefinitely and connect it only when you need to use it. However, you might
want to test the connection periodically to verify that the settings are correct and it can be
connected.

###### Note

AWS CloudHSM key stores have a `DISCONNECTED` connection state only when the key store has never been connected or you explicitly disconnect it. If your AWS CloudHSM key store connection state
is `CONNECTED` but you are having trouble using it, make sure that its
associated AWS CloudHSM cluster is active and contains at least one active HSMs. For help with
connection failures, see [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md").

When you connect an AWS CloudHSM key store, AWS KMS finds the associated AWS CloudHSM cluster, connects to
it, logs into the AWS CloudHSM client as the [kmsuser
crypto user](keystore-cloudhsm.md#concept-kmsuser "keystore-cloudhsm.md#concept-kmsuser") (CU), and then rotates the `kmsuser` password. AWS KMS remains
logged into the AWS CloudHSM client as long as the AWS CloudHSM key store is connected.

To establish the connection, AWS KMS creates a [security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") named
`kms-`<custom key store ID>`` in the virtual private
 cloud (VPC) of the cluster. The security group has a single rule that allows inbound traffic
 from the cluster security group. AWS KMS also creates an [elastic network interface](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md") (ENI)
 in each Availability Zone of the private subnet for the cluster. AWS KMS adds the ENIs to the
 `kms-`<cluster ID>`` security group and the security
group for the cluster. The description of each ENI is `KMS managed ENI for cluster
 `<cluster-ID>``.

The connection process can take an extended amount of time to complete; up to 20 minutes.

Before you connect the AWS CloudHSM key store, verify that it meets the requirements.

- Its associated AWS CloudHSM cluster must contain at least one active HSM. To find the number of
  HSMs in the cluster, view the cluster in the AWS CloudHSM console or use the [DescribeClusters](../../../cloudhsm/latest/APIReference/API_DescribeClusters.md "../../../cloudhsm/latest/APIReference/API_DescribeClusters.md") operation. If
  necessary, you can [add an HSM](../../../cloudhsm/latest/userguide/add-remove-hsm.md "../../../cloudhsm/latest/userguide/add-remove-hsm.md").
- The cluster must have a [kmsuser crypto
  user](create-keystore.md#kmsuser-concept "create-keystore.md#kmsuser-concept") (CU) account, but that CU cannot be logged into the cluster when you connect
  the AWS CloudHSM key store. For help with logging out, see [How to log out and reconnect](fix-keystore.md#login-kmsuser-2 "fix-keystore.md#login-kmsuser-2").
- The connection state of the AWS CloudHSM key store cannot be `DISCONNECTING` or
  `FAILED`. To view the connection state, use the AWS KMS console or the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
  response. If the connection state is `FAILED`, disconnect the custom key store,
  fix the problem, and then connect it.
  For help with connection failures, see [How to fix a connection failure](fix-keystore.md#fix-keystore-failed "fix-keystore.md#fix-keystore-failed").

When your AWS CloudHSM key store is connected, you can [create
KMS keys in it](create-cmk-keystore.md "create-cmk-keystore.md") and use existing KMS keys in [cryptographic operations](manage-cmk-keystore.md#use-cmk-keystore "manage-cmk-keystore.md#use-cmk-keystore").

## Connect and reconnect to your AWS CloudHSM key store

You can connect, or reconnect, your AWS CloudHSM key store in the AWS KMS console or by using the [ConnectCustomKeyStore](../APIReference/API_ConnectCustomKeyStore.md "../APIReference/API_ConnectCustomKeyStore.md") operation.

To connect an AWS CloudHSM key store in the AWS Management Console, begin by selecting the AWS CloudHSM key store
from the **Custom key stores** page. The connection process can take up to
20 minutes to complete.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **AWS CloudHSM key stores**.
4. Choose the row of the AWS CloudHSM key store you want to connect.

If the connection state of the AWS CloudHSM key store is **Failed**, you
must [disconnect the custom key store](disconnect-keystore.md#disconnect-keystore-console "disconnect-keystore.md#disconnect-keystore-console")
before you connect it. 5. From the **Key store actions** menu, choose
**Connect**.
AWS KMS begins the process of connecting your custom key store. It finds the associated
AWS CloudHSM cluster, builds the required network infrastructure, connects to it, logs into the
AWS CloudHSM cluster as the `kmsuser` CU, and rotates the `kmsuser` password.
When the operation completes, the connection state changes to
**Connected**.

If the operation fails, an error message appears that describes the reason for the
failure. Before you try to connect again, [view the connection
state](view-keystore.md "view-keystore.md") of your AWS CloudHSM key store. If it is **Failed**, you must [disconnect the custom key store](disconnect-keystore.md#disconnect-keystore-console "disconnect-keystore.md#disconnect-keystore-console") before you
connect it again. If you need help, see [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md").

**Next:**
[Create a KMS key in an AWS CloudHSM key store](create-cmk-keystore.md "create-cmk-keystore.md").

To connect a disconnected AWS CloudHSM key store, use the [ConnectCustomKeyStore](../APIReference/API_ConnectCustomKeyStore.md "../APIReference/API_ConnectCustomKeyStore.md") operation.
The associated AWS CloudHSM cluster must contain at least one active HSM and the connection state
cannot be `FAILED`.

The connection process takes an extended amount of time to complete; up to 20 minutes.
Unless it fails quickly, the operation returns an HTTP 200 response and a JSON object with
no properties. However, this initial response does not indicate that the connection was
successful. To determine the connection state of the custom key store, see the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
response.

The examples in this section use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

To identify the AWS CloudHSM key store, use its custom key store ID. You can find the ID on the
**Custom key stores** page in the console or by using the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
operation with no parameters. Before running this example, replace the example ID with a
valid one.

```
`$` `aws kms connect-custom-key-store --custom-key-store-id `cks-1234567890abcdef0``
```

To verify that the AWS CloudHSM key store is connected, use the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
operation. By default, this operation returns all custom keys stores in your account and
Region. But you can use either the `CustomKeyStoreId` or
`CustomKeyStoreName` parameter (but not both) to limit the response to
particular custom key stores. The `ConnectionState` value of
`CONNECTED` indicates that the custom key store is connected to its AWS CloudHSM
cluster.

###### Note

The `CustomKeyStoreType` field was added to the
`DescribeCustomKeyStores` response to distinguish AWS CloudHSM key stores from
external key stores.

```
`$` `aws kms describe-custom-key-stores --custom-key-store-id `cks-1234567890abcdef0``
`{
 "CustomKeyStores": [
 "CustomKeyStoreId": "cks-1234567890abcdef0",
 "CustomKeyStoreName": "ExampleCloudHSMKeyStore",
 "CloudHsmClusterId": "cluster-1a23b4cdefg",
 "CustomKeyStoreType": "AWS_CLOUDHSM",
 "TrustAnchorCertificate": "`<certificate string appears here>`",
 "CreationDate": "1.499288695918E9",
 **"ConnectionState": "CONNECTED"**
 ],
}`
```

If the `ConnectionState` value is failed, the
`ConnectionErrorCode` element indicates the reason for the failure. In this
case, AWS KMS could not find an AWS CloudHSM cluster in your account with the cluster ID
`cluster-1a23b4cdefg`. If you deleted the cluster, you can [restore it from a backup](../../../cloudhsm/latest/userguide/create-cluster-from-backup.md "../../../cloudhsm/latest/userguide/create-cluster-from-backup.md") of the
original cluster and then [edit the cluster ID](update-keystore.md "update-keystore.md") for the
custom key store. For help responding to a connection error code, see [How to fix a connection failure](fix-keystore.md#fix-keystore-failed "fix-keystore.md#fix-keystore-failed").

```
`$` `aws kms describe-custom-key-stores --custom-key-store-id `cks-1234567890abcdef0``
`{
 "CustomKeyStores": [
 "CustomKeyStoreId": "cks-1234567890abcdef0",
 "CustomKeyStoreName": "ExampleKeyStore",
 "CloudHsmClusterId": "cluster-1a23b4cdefg",
 "CustomKeyStoreType": "AWS_CLOUDHSM",
 "TrustAnchorCertificate": "`<certificate string appears here>`",
 "CreationDate": "1.499288695918E9",
 **"ConnectionState": "FAILED"**
 **"ConnectionErrorCode": "CLUSTER\_NOT\_FOUND"**
 ],
}`
```
