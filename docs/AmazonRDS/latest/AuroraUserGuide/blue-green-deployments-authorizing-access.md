# Authorizing access to Amazon Aurora

blue/green deployment operations

Users must have the required permissions to perform operations related to blue/green
deployments. You can create IAM policies that grant users and roles permission to perform
specific API operations on the specified resources they need. You can then attach those
policies to the IAM permission sets or roles that require those permissions. For more information,
see [Identity and access management for Amazon Aurora](UsingWithRDS.md "UsingWithRDS.md").

The user who creates a blue/green deployment must have permissions to perform the following RDS operations:

- `rds:CreateBlueGreenDeployment`
- `rds:AddTagsToResource`
- `rds:CreateDBCluster`
- `rds:CreateDBInstance`
- `rds:CreateDBClusterEndpoint`
  The user who switches over a blue/green deployment must have permissions to perform the following RDS operations:

- `rds:SwitchoverBlueGreenDeployment`
- `rds:ModifyDBCluster`
- `rds:PromoteReadReplicaDBCluster`
  The user who deletes a blue/green deployment must have permissions to perform the following RDS
  operations:

- `rds:DeleteBlueGreenDeployment`
- `rds:DeleteDBCluster`
- `rds:DeleteDBInstance`
- `rds:DeleteDBClusterEndpoint`
  Aurora
  provisions and modifies resources in the staging environment on your behalf. These resources
  include DB instances that use an internally defined naming convention. Therefore, attached IAM
  policies can't contain partial resource name patterns such as `my-db-prefix-*`.
  Only wildcards (\*) are supported. In general, we recommend using resource tags and other
  supported attributes to control access to these resources, rather than wildcards. For more
  information, see [Actions, resources, and
  condition keys for Amazon RDS](../../../service-authorization/latest/reference/list_amazonrds.md "../../../service-authorization/latest/reference/list_amazonrds.md").

## Additional permissions for Aurora Global Database Blue/Green Deployments

When creating blue/green deployments for Aurora Global Database clusters, in addition to the above listed permission, users need the following permissions to perform operations to manage the global cluster topology.

The user who creates a blue/green deployment must have permissions to perform the following RDS operations:

- `rds:CreateGlobalCluster`

The user who switches over a blue/green deployment must have permissions to perform the following RDS operations:

- `rds:ModifyGlobalCluster`
- `rds:PromoteReadReplicaDBCluster`

The user who deletes a blue/green deployment must have permissions to perform the following RDS operations:

- `rds:DeleteGlobalCluster`
