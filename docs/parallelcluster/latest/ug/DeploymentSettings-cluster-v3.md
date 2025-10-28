# `DeploymentSettings` section

###### Note

`DeploymentSettings` is added starting with AWS ParallelCluster version 3.4.0.

**(Optional)** Specifies the deployment settings configuration.

```
DeploymentSettings:
  LambdaFunctionsVpcConfig:
    SecurityGroupIds:
      - `string`
    SubnetIds:
      - `string`
  DisableSudoAccessForDefaultUser: Boolean
  DefaultUserHome: `string` # 'Shared' or 'Local'
```

## `DeploymentSettings`

properties

### `LambdaFunctionsVpcConfig`

**(Optional)** Specifies the AWS Lambda functions VPC configurations.
For more information, see [AWS Lambda VPC configuration in AWS ParallelCluster](lambda-vpc-v3.md "lambda-vpc-v3.md").

```
LambdaFunctionsVpcConfig:
  SecurityGroupIds:
    - `string`
  SubnetIds:
    - `string`
```

#### `LambdaFunctionsVpcConfig properties`

`SecurityGroupIds` (**Required**,
`[String]`)

The list of Amazon VPC security group IDs that are attached to the Lambda functions.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`SubnetIds` (**Required**,
`[String]`)

The list of subnet IDs that are attached to the Lambda functions.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

The subnets and security groups must be in the same VPC.

###

DisableSudoAccessForDefaultUser property

###### Note

This config Option is only supported with Slurm Clusters.

(Optional) If `True` , the sudo privileges of the default User will be disabled.
This applies to all the nodes in the cluster.

```
# Main DeploymentSettings section in config yaml(applies to HN, CF and LN)
DeploymentSettings:
  DisableSudoAccessForDefaultUser: True
```

To update the value of `DisableSudoAccessForDefaultUser`, you must stop
the compute fleet and all login nodes.

[Update policy: The compute
fleet and login nodes must be stopped for this setting to be changed for an
update.](using-pcluster-update-cluster-v3.md#update-policy-compute-login-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-login-v3")

### DefaultUserHome

property

When set to `Shared`, the cluster will use the default setup and share the
default user’s directory across the cluster by `/home/<default user>`.

When set to `Local`, the head node, login nodes, and compute nodes will each
have a separate local default user directory stored in `local/home/<default user>`.
