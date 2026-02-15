# Set the mTLS enforcement level

with CloudHSM CLI

Use the **cluster mtls set-enforcement** command in CloudHSM CLI to set the enforcement level of the usage of mutual TLS between client and AWS CloudHSM.

## User type

The following users can run this command.

- Admin with username as admin

## Requirements

To run this command:

- At least one trust anchor has been successfully registered onto the AWS CloudHSM.
- Configure the CloudHSM CLI with the right private key and client certificate, and start CloudHSM CLI under a mutual TLS connection.
- You must be logged in as the default admin with username "admin". Any other admin user will not be able to run this command.

## Syntax

```
`aws-cloudhsm >` `help cluster mtls set-enforcement`
            `Set mtls enforcement policy in the cluster

Usage: cluster mtls set-enforcement [OPTIONS] --level [`<LEVEL>`...]

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --level `<LEVEL>` Level to be set for mtls in the cluster [possible values: none, cluster]
 --approval `<APPROVAL>` Filepath of signed quorum token file to approve operation
 -h, --help Print help`

```

## Example

###### Example

In the following example, this command set the mtls enforcement level of the AWS CloudHSM to be cluster. The set-enforcement command can only be performed in a mutual TLS connection and logged in as the admin user with username as admin, see [set the mTLS enforcement for AWS CloudHSM](getting-started-setup-mtls.md#getting-start-setup-mtls-enforcement "getting-started-setup-mtls.md#getting-start-setup-mtls-enforcement").

```
`aws-cloudhsm >` `cluster mtls set-enforcement --level cluster`
                `{
 "error_code": 0,
 "data": {
 "message": "Mtls enforcement level set to Cluster successfully"
 }
}`

```

You can then run the **get-enforcement** command to confirm that enforcement level has been set to cluster:

```
`aws-cloudhsm >` `cluster mtls get-enforcement`
                `{
 "error_code": 0,
 "data": {
 "mtls-enforcement-level": "cluster"
 }
}`

```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<LEVEL>`**

Level to be set for mtls in the cluster.

**Valid values**

- **cluster**: Enforce the usage of mutual TLS between client and AWS CloudHSM in the cluster.

- **none**: Do not enforce the usage of mutual TLS between client and AWS CloudHSM in the cluster.

**Required**: Yes

###### Warning

After you enforce mTLS usage in the cluster, all existing non-mTLS connections will be dropped and you can only connect to the cluster with mTLS certificates.

**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if quorum cluster service quorum value is greater than 1.

## Related topics

- [cluster mtls get-enforcement](cloudhsm_cli-cluster-mtls-get-enforcement.md "cloudhsm_cli-cluster-mtls-get-enforcement.md")
- [Setup mTLS (recommended)](getting-started-setup-mtls.md "getting-started-setup-mtls.md")
