# Generate a quorum token using CloudHSM CLI

Use the **quorum token-sign generate** command in CloudHSM CLI to generate a token for a quorum authorized service.

There is a limit to obtaining one active token per user per service on an HSM cluster for services user and quorum. This limit does not apply to tokens related to key services.

###### Note

Only Admins and Crypto Users may generate specific service tokens. For more information about service types and names, see [Service names and types that support quorum authentication](quorum-auth-chsm-cli-service-names.md "quorum-auth-chsm-cli-service-names.md")

**Admin Services**: Quorum authentication is used for admin privileged services like creating users, deleting users,
changing user passwords, setting quorum values, and deactivating quorum and MFA capabilities.

**Crypto User Services**: Quorum authentication is used for crypto-user privileged services associated with a
specific key like signing with a key, sharing/unsharing a key, wrapping/unwrapping a key, and setting a key's attribute. The quorum value of an associated key is
configured when the key is generated, imported, or unwrapped. The quorum value must be equal to or less than the number of users that the key is associated with,
which includes users that the key is shared with and the key owner.

Each service type is further broken down into a qualifying service name, which contains a specific set of quorum supported service operations that can be performed.

| Service name   | Service type | Service operations                                                                                               |
| -------------- | ------------ | ---------------------------------------------------------------------------------------------------------------- |
| user           | Admin        | • user create<br>• user delete<br>• user change-password<br>• user change-mfa                                    |
| quorum         | Admin        | • quorum token-sign set-quorum-value                                                                             |
| cluster1       | Admin        | • cluster mtls register-trust-anchor<br>• cluster mtls deregister-trust-anchor<br>• cluster mtls set-enforcement |
| key-management | Crypto User  | • key wrap<br>• key unwrap<br>• key share<br>• key unshare<br>• key set-attribute                                |
| key-usage      | Crypto User  | • key sign                                                                                                       |

[1] Cluster service is exclusively available on hsm2m.medium

## User type

The following users can run this command.

- Admin
- Crypto user (CU)

## Syntax

```
`aws-cloudhsm >` `help quorum token-sign generate``Generate a token

Usage: quorum token-sign generate --service `<SERVICE>` --token `<TOKEN>`

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
 - registration:
 Registration service is used for registering a public key for quorum authentication
 - key-usage:
 Key usage service is used for executing quorum authenticated key usage operations
 - key-management:
 Key management service is used for executing quorum authenticated key management operations

 --token `<TOKEN>`
 Filepath where the unsigned token file will be written
 -h, --help Print help`
```

## Example

This command will write one unsigned token per HSM in your cluster to the file specified by `token`.

###### Example : Write one unsigned token per HSM in your cluster

```
`aws-cloudhsm >` `quorum token-sign generate --service user --token /home/tfile``{
 "error_code": 0,
 "data": {
 "filepath": "/home/tfile"
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<SERVICE>`**

Specifies the quorum authorized service for which to generate a token. This parameter is required.

**Valid values**

- **user**: The user management service that is used for executing quorum authorized user management operations.

- **quorum**: The quorum management service that is used for setting quorum authorized quorum values for any quorum authorized service.

- **cluster**: The cluster management service that is used for executing quorum for cluster wide configuration managements like mtls enforcement, mtls registration and mtls deregistration.

- **registration**: Generates an unsigned token for use in registering a public key for quorum authorization.

- **key-usage**: Generates an unsigned token that is used for executing quorum authorized key usage operations.

- **key-management**: Generates an unsigned token that is used for executing quorum authorized key management operations.

**Required**: Yes

**`<TOKEN>`**

Filepath where the unsigned token file will be written.

**Required**: Yes

## Related topics

- [Service names and types that support quorum authentication](quorum-auth-chsm-cli-service-names.md "quorum-auth-chsm-cli-service-names.md")
