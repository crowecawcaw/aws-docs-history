# Update a quorum value using CloudHSM CLI

Use the **quorum token-sign set-quorum-value** command in CloudHSM CLI to set a new quorum value for a quorum authorized service.

## User type

The following users can run this command.

- Admin

## Syntax

```
`aws-cloudhsm >` `help quorum token-sign set-quorum-value``Set a quorum value

Usage: quorum token-sign set-quorum-value [OPTIONS] --service `<SERVICE>` --value `<VALUE>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error

 --service `<SERVICE>`
 Service the token will be used for

 Possible values:
 - user:
 User management service is used for executing quorum authenticated user management operations
 - quorum:
 Quorum management service is used for setting quorum values for any quorum service
 - cluster:
 Cluster management service is used for executing quorum for cluster wide configuration managements like mtls enforcement, mtls registration and mtls deregistration

 --value `<VALUE>`
 Value to set for service

 --approval `<APPROVAL>`
 Filepath of signed quorum token file to approve operation

 -h, --help
 Print help (see a summary with '-h')`
```

## Example

###### Example

In the following example, this command writes one unsigned token per HSM in your cluster to the file specified by token. When you are prompted, sign the tokens in the file.

```
`aws-cloudhsm >` `quorum token-sign set-quorum-value --service quorum --value 2``{
 "error_code": 0,
 "data": "Set Quorum Value successful"
}`
```

You can then run the **list-quorum-values** command to confirm that the quorum value for the quorum management service has been set:

**hsm1.medium**:

```
`aws-cloudhsm >` `quorum token-sign list-quorum-values``{
 "error_code": 0,
 "data": {
 "user": 1,
 "quorum": 2
 }
}`
```

**hsm2m.medium**:

```
`aws-cloudhsm >` `quorum token-sign list-quorum-values``{
 "error_code": 0,
 "data": {
 "user": 1,
 "quorum": 2,
 "cluster": 1
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<APPROVAL>`**

The filepath of the signed token file to be approved on the HSM.

**`<SERVICE>`**

Specifies the quorum authorized service for which to generate a token. This parameter is required. For more information about service types and names, see [Service names and types that support quorum authentication](quorum-auth-chsm-cli-service-names.md "quorum-auth-chsm-cli-service-names.md").

**Valid values**

- **user**: The user management service. Service used for executing quorum authorized user management operations.

- **quorum**: The quorum management service. Service used for setting a quorum authorized quorum values for any quorum authorized service.

- **cluster**: The cluster management service that is used for executing quorum for cluster wide configuration managements like mtls enforcement, mtls registration and mtls deregistration.

- **registration**: Generates a unsigned token for use in registering a public key for quorum authorization.

**Required**: Yes

**`<VALUE>`**

Specifies The quorum value to be set. The maximum quorum value is eight (8).

**Require**: Yes

## Related topics

- [quorum token-sign list-quorum-values](cloudhsm_cli-qm-token-list-qm.md "cloudhsm_cli-qm-token-list-qm.md")
- [Service names and types that support quorum authentication](quorum-auth-chsm-cli-service-names.md "quorum-auth-chsm-cli-service-names.md")
- [Setup mTLS (recommended)](getting-started-setup-mtls.md "getting-started-setup-mtls.md")
