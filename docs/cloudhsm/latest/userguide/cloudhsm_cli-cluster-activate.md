# Activate a cluster with CloudHSM CLI

Use the **cluster activate** command in CloudHSM CLI to [activate a new cluster](activate-cluster.md "activate-cluster.md") in AWS CloudHSM. This command must be run
before the cluster can be used to perform cryptographic operations.

## User type

The following types of users can run this command.

- Unactivated admin

## Syntax

This command has no parameters.

```
`aws-cloudhsm >` `help cluster activate``Activate a cluster

This command will set the initial Admin password. This process will cause your CloudHSM cluster to
move into the ACTIVE state.

USAGE:
 cloudhsm-cli cluster activate [OPTIONS] [--password <PASSWORD>]

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error

 --password `<PASSWORD>`
 Optional: Plaintext activation password If you do not include this argument you will be prompted for it

 -h, --help
 Print help (see a summary with '-h')`
```

## Example

This command activates your cluster by setting the initial password for you admin user.

```
`aws-cloudhsm >` `cluster activate``Enter password:
Confirm password:
{
 "error_code": 0,
 "data": "Cluster activation successful"
}`
```

## Related topics

- [user create](cloudhsm_cli-user-create.md "cloudhsm_cli-user-create.md")
- [user delete](cloudhsm_cli-user-delete.md "cloudhsm_cli-user-delete.md")
- [user change-password](cloudhsm_cli-user-change-password.md "cloudhsm_cli-user-change-password.md")
