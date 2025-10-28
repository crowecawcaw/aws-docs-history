# Create an AWS CloudHSM key store

You can create one or several AWS CloudHSM key stores in your account. Each AWS CloudHSM key store is
associated with one AWS CloudHSM cluster in the same AWS account and Region. Before you create your
AWS CloudHSM key store, you need to [assemble the prerequisites](#before-keystore "#before-keystore").
Then, before you can use your AWS CloudHSM key store, you must [connect it](connect-keystore.md "connect-keystore.md") to its AWS CloudHSM cluster.

###### Notes

KMS cannot communicate over IPv6 with AWS CloudHSM key stores.

If you try to create an AWS CloudHSM key store with all of the same property values as an existing
_disconnected_ AWS CloudHSM key store, AWS KMS does not create a new AWS CloudHSM key store, and it does not throw an exception or display an error.
Instead, AWS KMS recognizes the duplicate as the likely consequence of a retry, and it returns the ID of the existing AWS CloudHSM key store.

You do not have to connect your AWS CloudHSM key store immediately. You can leave it in a
disconnected state until you are ready to use it. However, to verify that it is configured
properly, you might want to [connect it](connect-keystore.md "connect-keystore.md"), [view its connection state](view-keystore.md "view-keystore.md"), and then [disconnect it](disconnect-keystore.md "disconnect-keystore.md").

###### Topics

- [Assemble the prerequisites](#before-keystore "#before-keystore")
- [Create a new AWS CloudHSM key store](#create-hsm-keystore "#create-hsm-keystore")

## Assemble the prerequisites

Each AWS CloudHSM key store is backed by an AWS CloudHSM cluster. To create an AWS CloudHSM key store, you must
specify an active AWS CloudHSM cluster that is not already associated with another key store. You
also need to create a dedicated crypto user (CU) in the cluster's HSMs that AWS KMS can use to
create and manage keys on your behalf.

Before you create an AWS CloudHSM key store, do the following:

**Select an AWS CloudHSM cluster**

Every AWS CloudHSM key store is [associated with exactly one
AWS CloudHSM cluster](keystore-cloudhsm.md#concept-cluster "keystore-cloudhsm.md#concept-cluster"). When you create AWS KMS keys in your AWS CloudHSM key store, AWS KMS creates the KMS key metadata,
such as an ID and Amazon Resource Name (ARN) in AWS KMS. It then creates the key material
in the HSMs of the associated cluster. You can [create a new AWS CloudHSM](../../../cloudhsm/latest/userguide/getting-started.md "../../../cloudhsm/latest/userguide/getting-started.md") cluster or use an
existing one. AWS KMS does not require exclusive access to the cluster.

The AWS CloudHSM cluster that you select is permanently associated with the AWS CloudHSM key
store. After you create the AWS CloudHSM key store, you can [change the cluster ID](update-keystore.md "update-keystore.md") of the associated cluster, but the cluster that you
specify must share a backup history with the original cluster. To use an unrelated
cluster, you need to create a new AWS CloudHSM key store.

The AWS CloudHSM cluster that you select must have the following characteristics:

- **The cluster must be active**.

You must create the cluster, initialize it, install the AWS CloudHSM client software
for your platform, and then activate the cluster. For detailed instructions, see
[Getting started with AWS CloudHSM](../../../cloudhsm/latest/userguide/getting-started.md "../../../cloudhsm/latest/userguide/getting-started.md") in the
_AWS CloudHSM User Guide_.

- **Mutual TLS (mTLS) is not enabled.**

KMS does not support mTLS for clusters. This setting must not be enabled.

- **The cluster must be in the same account and
  Region** as the AWS CloudHSM key store. You cannot associate an AWS CloudHSM key store
  in one Region with a cluster in a different Region. To create a key infrastructure
  in multiple Regions, you must create AWS CloudHSM key stores and clusters in each
  Region.
- **The cluster cannot be associated with another custom key
  store** in the same account and Region. Each AWS CloudHSM key store in the
  account and Region must be associated with a different AWS CloudHSM cluster. You cannot
  specify a cluster that is already associated with a custom key store or a cluster
  that shares a backup history with an associated cluster. Clusters that share a
  backup history have the same cluster certificate. To view the cluster certificate of
  a cluster, use the AWS CloudHSM console or the [DescribeClusters](../../../cloudhsm/latest/APIReference/API_DescribeClusters.md "../../../cloudhsm/latest/APIReference/API_DescribeClusters.md")
  operation.

If you [back up an AWS CloudHSM
cluster to a different Region](../../../cloudhsm/latest/userguide/copy-backup-to-region.md "../../../cloudhsm/latest/userguide/copy-backup-to-region.md"), it is considered to be different cluster,
and you can associate the backup with a custom key store in its Region. However,
KMS keys in the two custom key stores are not interoperable, even if they have the
same backing key. AWS KMS binds metadata to the ciphertext so it can be decrypted only
by the KMS key that encrypted it.

- The cluster must be configured with [private subnets](../../../cloudhsm/latest/userguide/create-subnets.md "../../../cloudhsm/latest/userguide/create-subnets.md") in **at least two Availability
  Zones** in the Region. Because AWS CloudHSM is not supported in all Availability
  Zones, we recommend that you create private subnets in all Availability Zones in the
  region. You cannot reconfigure the subnets for an existing cluster, but you can
  [create a cluster from a
  backup](../../../cloudhsm/latest/userguide/create-cluster-from-backup.md "../../../cloudhsm/latest/userguide/create-cluster-from-backup.md") with different subnets in the cluster configuration.

###### Important

After you create your AWS CloudHSM key store, do not delete any of the private
subnets configured for its AWS CloudHSM cluster. If AWS KMS cannot find all of the subnets
in the cluster configuration, attempts to [connect to the custom key store](connect-keystore.md "connect-keystore.md") fail with a
`SUBNET_NOT_FOUND` connection error state. For details, see [How to fix a connection failure](fix-keystore.md#fix-keystore-failed "fix-keystore.md#fix-keystore-failed").

- The [security group for the
  cluster](../../../cloudhsm/latest/userguide/configure-sg.md "../../../cloudhsm/latest/userguide/configure-sg.md")
  (`cloudhsm-cluster-`<cluster-id>`-sg`) must
  include inbound rules and outbound rules that allow TCP traffic over IPv4, on ports 2223-2225.
  The **Source** in the inbound rules and the
  **Destination** in the outbound rules must match the security
  group ID. These rules are set by default when you create the cluster. Do not delete
  or change them.
- **The cluster must contain at least two active
  HSMs** in different Availability Zones. To verify the number of HSMs, use
  the AWS CloudHSM console or the [DescribeClusters](../../../cloudhsm/latest/APIReference/API_DescribeClusters.md "../../../cloudhsm/latest/APIReference/API_DescribeClusters.md") operation. If necessary, you can [add an HSM](../../../cloudhsm/latest/userguide/add-remove-hsm.md#add-hsm "../../../cloudhsm/latest/userguide/add-remove-hsm.md#add-hsm").

**Find the trust anchor certificate**

When you create a custom key store, you must upload the trust anchor certificate for
the AWS CloudHSM cluster to AWS KMS. AWS KMS needs the trust anchor certificate to connect the
AWS CloudHSM key store to its associated AWS CloudHSM cluster.

Every active AWS CloudHSM cluster has a _trust anchor
certificate_. When you [initialize the cluster](../../../cloudhsm/latest/userguide/initialize-cluster.md#sign-csr "../../../cloudhsm/latest/userguide/initialize-cluster.md#sign-csr"), you
generate this certificate, save it in the `customerCA.crt` file, and
copy it to hosts that connect to the cluster.

**Create the `kmsuser` crypto user for AWS KMS**

To administer your AWS CloudHSM key store, AWS KMS logs into the [kmsuser crypto user](keystore-cloudhsm.md#concept-kmsuser "keystore-cloudhsm.md#concept-kmsuser") (CU) account in the
selected cluster. Before you create your AWS CloudHSM key store, you must create the
`kmsuser` CU. Then when you create your AWS CloudHSM key store, you provide the
password for `kmsuser` to AWS KMS. Whenever you connect the AWS CloudHSM key store to
its associated AWS CloudHSM cluster, AWS KMS logs in as the `kmsuser` and rotates the
`kmsuser` password

###### Important

Do not specify the `2FA` option when you create the
`kmsuser` CU. If you do, AWS KMS cannot log in and your AWS CloudHSM key store
cannot be connected to this AWS CloudHSM cluster. Once you specify 2FA, you cannot undo it.
Instead, you must delete the CU and recreate it.

###### Notes

The following procedures use the AWS CloudHSM Client SDK 5 command line tool, [CloudHSM CLI](../../../cloudhsm/latest/userguide/cloudhsm_cli.md "../../../cloudhsm/latest/userguide/cloudhsm_cli.md"). The CloudHSM CLI replaces
`key-handle` with `key-reference`.

On January 1, 2025, AWS CloudHSM will end support for the Client SDK 3 command line tools, the CloudHSM
Management Utility (CMU) and the Key Management Utility (KMU). For more information on the
differences between the Client SDK 3 command line tools and the Client SDK 5 command line
tool, see [Migrate from Client SDK 3 CMU and KMU to
Client SDK 5 CloudHSM CLI](../../../cloudhsm/latest/userguide/cloudhsm_cli-migrate-from-kmu-cmu.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-migrate-from-kmu-cmu.md") in the _AWS CloudHSM User Guide_.

1. Follow the getting started procedures as described in the [Getting started with CloudHSM
   Command Line Interface (CLI)](../../../cloudhsm/latest/userguide/cloudhsm_cli-getting-started.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-getting-started.md") topic of the
   _AWS CloudHSM User Guide_.
2. Use the [**user
   create**](../../../cloudhsm/latest/userguide/create-user-cloudhsm-cli.md "../../../cloudhsm/latest/userguide/create-user-cloudhsm-cli.md") command to create a CU named
   `kmsuser`.

The password must consist of 7-32 alphanumeric characters. It is case-sensitive
and cannot contain any special characters.

The following example command creates a `kmsuser` CU.

```
`aws-cloudhsm >` `user create --username kmsuser --role crypto-user`
`Enter password:
Confirm password:
{
 "error_code": 0,
 "data": {
 "username": "kmsuser",
 "role": "crypto-user"
 }
}`
```

[Show moreShow less](# "#")

## Create a new AWS CloudHSM key store

After [assembling the prerequisites](#before-keystore "#before-keystore"), you can create
a new AWS CloudHSM key store in the AWS KMS console or by using the [CreateCustomKeyStore](../APIReference/API_CreateCustomKeyStore.md "../APIReference/API_CreateCustomKeyStore.md")
operation.

When you create an AWS CloudHSM key store in the AWS Management Console, you can add and create the [prerequisites](#before-keystore "#before-keystore") as part of your workflow. However, the
process is quicker when you have assembled them in advance.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Custom key stores**, **AWS CloudHSM key stores**.
4. Choose **Create a key store**.
5. Enter a friendly name for the custom key store. The name must be unique among all
   custom key stores in your account.

###### Important

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output. 6. Select [an AWS CloudHSM cluster](keystore-cloudhsm.md#concept-cluster "keystore-cloudhsm.md#concept-cluster") for the AWS CloudHSM key
store. Or, to create a new AWS CloudHSM cluster, choose the **Create an AWS CloudHSM
cluster** link.

The menu displays the AWS CloudHSM clusters in your account and region that are not
already associated with an AWS CloudHSM key store. The cluster must [fulfill the requirements](#before-keystore "#before-keystore") for association with a
custom key store. 7. Choose **Choose file**, and then upload the trust anchor
certificate for the AWS CloudHSM cluster that you chose. This is the
`customerCA.crt` file that you created when you [initialized the
cluster](../../../cloudhsm/latest/userguide/initialize-cluster.md#sign-csr "../../../cloudhsm/latest/userguide/initialize-cluster.md#sign-csr"). 8. Enter the password of [the kmsuser
crypto user](keystore-cloudhsm.md#concept-kmsuser "keystore-cloudhsm.md#concept-kmsuser") (CU) that you created in the selected cluster. 9. Choose **Create**.
When the procedure is successful, the new AWS CloudHSM key store appears in the list of AWS CloudHSM
key stores in the account and Region. If it is unsuccessful, an error message appears that
describes the problem and provides help on how to fix it. If you need more help, see [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md").

If you try to create an AWS CloudHSM key store with all of the same property values as an existing
_disconnected_ AWS CloudHSM key store, AWS KMS does not create a new AWS CloudHSM key store, and it does not throw an exception or display an error.
Instead, AWS KMS recognizes the duplicate as the likely consequence of a retry, and it returns the ID of the existing AWS CloudHSM key store.

**Next**: New AWS CloudHSM key stores are not automatically
connected. Before you can create AWS KMS keys in the AWS CloudHSM key store, you must [connect the custom key store](connect-keystore.md "connect-keystore.md") to its associated
AWS CloudHSM cluster.

You can use the [CreateCustomKeyStore](../APIReference/API_CreateCustomKeyStore.md "../APIReference/API_CreateCustomKeyStore.md") operation to create a new AWS CloudHSM key store that is
associated with an AWS CloudHSM cluster in the account and Region. These examples use the
AWS Command Line Interface (AWS CLI), but you can use any supported programming language.

The `CreateCustomKeyStore` operation requires the following parameter
values.

- CustomKeyStoreName – A friendly name for the custom key store that is
  unique in the account.

###### Important

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

- CloudHsmClusterId – The cluster ID of an AWS CloudHSM cluster that [fulfills the requirements](#before-keystore "#before-keystore") for an AWS CloudHSM key
  store.
- KeyStorePassword – The password of `kmsuser` CU account in the
  specified cluster.
- TrustAnchorCertificate – The content of the
  `customerCA.crt` file that you created when you [initialized the cluster](../../../cloudhsm/latest/userguide/initialize-cluster.md "../../../cloudhsm/latest/userguide/initialize-cluster.md").
  The following example uses a fictitious cluster ID. Before running the command,
  replace it with a valid cluster ID.

```
`$` `aws kms create-custom-key-store
 --custom-key-store-name `ExampleCloudHSMKeyStore` \
 --cloud-hsm-cluster-id `cluster-1a23b4cdefg` \
 --key-store-password `kmsPswd` \
 --trust-anchor-certificate `<certificate-goes-here>``
```

If you are using the AWS CLI, you can specify the trust anchor certificate file, instead
of its contents. In the following example, the `customerCA.crt` file is
in the root directory.

```
`$` `aws kms create-custom-key-store
 --custom-key-store-name `ExampleCloudHSMKeyStore` \
 --cloud-hsm-cluster-id `cluster-1a23b4cdefg` \
 --key-store-password `kmsPswd` \
 --trust-anchor-certificate `file://customerCA.crt``
```

When the operation is successful, `CreateCustomKeyStore` returns the custom
key store ID, as shown in the following example response.

```
`{
 "CustomKeyStoreId": cks-1234567890abcdef0
}`
```

If the operation fails, correct the error indicated by the exception, and try again.
For additional help, see [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md").

If you try to create an AWS CloudHSM key store with all of the same property values as an existing
_disconnected_ AWS CloudHSM key store, AWS KMS does not create a new AWS CloudHSM key store, and it does not throw an exception or display an error.
Instead, AWS KMS recognizes the duplicate as the likely consequence of a retry, and it returns the ID of the existing AWS CloudHSM key store.

**Next**: To use the AWS CloudHSM key store, [connect it to its AWS CloudHSM cluster](connect-keystore.md "connect-keystore.md").
