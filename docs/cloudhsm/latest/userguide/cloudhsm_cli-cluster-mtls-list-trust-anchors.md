# List trust anchors with

CloudHSM CLI

Use the **cluster mtls list-trust-anchors** command in CloudHSM CLI to list all the trust anchors which can be used for mutual TLS between client and AWS CloudHSM.

## User type

The following users can run this command.

- All users. You do not need to be logged in to run this command.

## Syntax

```
`aws-cloudhsm >` `help cluster mtls list-trust-anchors`
            `List all trust anchors for mtls

Usage: cluster mtls list-trust-anchors [OPTIONS]

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 -h, --help Print help`

```

## Example

###### Example

In the following example, this command lists all the registered trust anchors from the AWS CloudHSM.

```
`aws-cloudhsm >` `cluster mtls list-trust-anchors`
                `{
 "error_code": 0,
 "data": {
 "trust_anchors": [
 {
 "certificate-reference": "0x01",
 "certificate": "`<PEM Encoded Certificate 1>`",
 "cluster-coverage": "full"
 },
 {
 "certificate-reference": "0x02",
 "certificate": "`<PEM Encoded Certificate 2>`",
 "cluster-coverage": "full"
 }
 ]
 }
}`

```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

## Related topics

- [cluster mtls reregister-trust-anchor](cloudhsm_cli-cluster-mtls-register-trust-anchor.md "cloudhsm_cli-cluster-mtls-register-trust-anchor.md")
- [cluster mtls deregister-trust-anchor](cloudhsm_cli-cluster-mtls-deregister-trust-anchor.md "cloudhsm_cli-cluster-mtls-deregister-trust-anchor.md")
- [Setup mTLS (recommended)](getting-started-setup-mtls.md "getting-started-setup-mtls.md")
