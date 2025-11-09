# Register a trust anchor

with CloudHSM CLI

Use the **cluster mtls register-trust-anchor** command in CloudHSM CLI to register a trust anchor for mutual TLS between client and AWS CloudHSM.

## User type

The following users can run this command.

- Admin

## Requirements

The AWS CloudHSM accepts trust anchors with the following key types:

| Key Type | Description                                                         |
| -------- | ------------------------------------------------------------------- |
| **EC**   | secp256r1 (P-256), secp384r1 (P-384), and secp521r1 (P-521) curves. |
| **RSA**  | 2048-bit, 3072-bit, and 4096-bit RSA keys.                          |

## Syntax

```
`aws-cloudhsm >` `help cluster mtls register-trust-anchor`
            `Register a trust anchor for mtls

Usage: cluster mtls register-trust-anchor [OPTIONS] --path [`<PATH>`...]

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --path `<PATH>` Filepath of the trust anchor to register
 --approval `<APPROVAL>` Filepath of signed quorum token file to approve operation
 -h, --help Print help`

```

## Example

In the following example, this command registers a trust anchor onto the HSM. The maximum number of trust anchors can be registered is two (2).

```
`aws-cloudhsm >` `cluster mtls register-trust-anchor --path /home/rootCA`
                `{
 "error_code": 0,
 "data": {
 "trust_anchor": {
 "certificate-reference": "0x01",
 "certificate": "`<PEM Encoded Certificate>`",
 "cluster-coverage": "full"
 }
 }
}`

```

You can then run the **list-trust-anchors** command to confirm that trust anchor has been registered onto the AWS CloudHSM:

```
`aws-cloudhsm >` `cluster mtls list-trust-anchors`
                `{
 "error_code": 0,
 "data": {
 "trust_anchors": [
 {
 "certificate-reference": "0x01",
 "certificate": "`<PEM Encoded Certificate>`",
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

**`<PATH>`**

Filepath of the trust anchor to register.

**Required**: Yes

###### Note

AWS CloudHSM supports registering intermediate certificates as trust anchor. In such cases, the entire PEM-encoded certificate chain file needs to be registered onto the HSM, with the certificates in hierarchical order.

AWS CloudHSM supports a certificate chain of 6980 bytes.

**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if quorum cluster service quorum value is greater than 1.

## Related topics

- [cluster mtls deregister-trust-anchor](cloudhsm_cli-cluster-mtls-deregister-trust-anchor.md "cloudhsm_cli-cluster-mtls-deregister-trust-anchor.md")
- [cluster mtls list-trust-anchors](cloudhsm_cli-cluster-mtls-list-trust-anchors.md "cloudhsm_cli-cluster-mtls-list-trust-anchors.md")
- [Setup mTLS (recommended)](getting-started-setup-mtls.md "getting-started-setup-mtls.md")
