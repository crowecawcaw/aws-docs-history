# Show quorum values using CloudHSM CLI

Use the **quorum token-sign list-quorum-values** command in CloudHSM CLI to lists the quorum values set in your AWS CloudHSM cluster.

## User type

The following users can run this command.

- All users. You do not need to be logged in to run this command.

## Syntax

```
`aws-cloudhsm >` `help quorum token-sign list-quorum-values``List current quorum values

Usage: quorum token-sign list-quorum-values

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 -h, --help Print help`
```

## Example

This command lists quorum values set in your AWS CloudHSM cluster for each service.

**hsm1.medium**:

```
`aws-cloudhsm >` `quorum token-sign list-quorum-values``{
 "error_code": 0,
 "data": {
 "user": 1,
 "quorum": 1
 }
}`
```

**hsm2m.medium**:

```
`aws-cloudhsm >` `quorum token-sign list-quorum-values``{
 "error_code": 0,
 "data": {
 "user": 1,
 "quorum": 1,
 "cluster": 1
 }
}`
```

## Related topics

- [Service names and types that support quorum authentication](quorum-auth-chsm-cli-service-names.md "quorum-auth-chsm-cli-service-names.md")
- [Setup mTLS (recommended)](getting-started-setup-mtls.md "getting-started-setup-mtls.md")
