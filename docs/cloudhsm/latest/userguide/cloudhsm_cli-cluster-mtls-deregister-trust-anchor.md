# Deregister a trust

anchor with CloudHSM CLI

Use the **cluster mtls deregister-trust-anchor** command in CloudHSM CLI to deregister a trust anchor for mutual TLS between client and AWS CloudHSM.

## User type

The following users can run this command.

- Admin

## Requirements

- To run this command, you must be logged in as a admin user.

## Syntax

```
`aws-cloudhsm >` `help cluster mtls deregister-trust-anchor`
            `Deregister a trust anchor for mtls

Usage: cluster mtls deregister-trust-anchor [OPTIONS] --certificate-reference [`<CERTIFICATE_REFERENCE>`...]

Options:
 --certificate-reference `<CERTIFICATE_REFERENCE>` A hexadecimal or decimal certificate reference
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --approval `<APPROVAL>` Filepath of signed quorum token file to approve operation
 -h, --help Print help`

```

## Example

###### Example

In the following example, this command removes a trust anchor from the HSM.

```
`aws-cloudhsm >` `cluster mtls deregister-trust-anchor --certificate-reference 0x01`
                `{
 "error_code": 0,
 "data": {
 "message": "Trust anchor with reference 0x01 deregistered successfully"
 }
}`

```

You can then run the **list-trust-anchors** command to confirm that trust anchor has been deregistered from the AWS CloudHSM:

```
`aws-cloudhsm >` `cluster mtls list-trust-anchors`
                `{
 "error_code": 0,
 "data": {
 "trust_anchors": []
 }
}`

```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<CERTIFICATE_REFERENCE>`**

A hexadecimal or decimal certificate reference.

**Required**: Yes

###### Warning

After you deregister a trust anchor in the cluster, all existing mTLS connections using the client certificate signed by that trust anchor will be dropped.

**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if quorum cluster service quorum value is greater than 1.

## Related topics

- [cluster mtls reregister-trust-anchor](cloudhsm_cli-cluster-mtls-register-trust-anchor.md "cloudhsm_cli-cluster-mtls-register-trust-anchor.md")
- [cluster mtls list-trust-anchors](cloudhsm_cli-cluster-mtls-list-trust-anchors.md "cloudhsm_cli-cluster-mtls-list-trust-anchors.md")
- [Setup mTLS (recommended)](getting-started-setup-mtls.md "getting-started-setup-mtls.md")
