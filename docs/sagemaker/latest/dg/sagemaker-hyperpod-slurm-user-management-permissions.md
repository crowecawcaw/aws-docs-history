

# How permissions work in the user management extension

The SageMaker HyperPod user management extension grants access only through groups. A group's `ssh` list names the node types where its members can log in over SSH, and its `sudo` list names the node types where they get passwordless sudo. A user has a permission on a node only if they belong to a group whose list includes that node's type. Permissions aren't granted to individual users: to give or remove access, change the user's groups or the group's rules. A local user's groups are their `groups` list. A directory user's groups are the directory groups that you list in `ldapGroups`.

**Important**  
After the extension writes SSH rules on a node, only members of the groups that target that node, and the `ubuntu` user, can log in to it over SSH. Other users, including directory users and accounts that you created another way, are refused unless another `AllowGroups` rule on the node allows them. An `AllowGroups` line from your lifecycle scripts still applies alongside the extension's rules, except for directory groups listed in mixed case, because the extension's SSSD reports group names in lowercase. To let only the extension control SSH access, remove that line. Before you add the extension to a cluster that people already use, make sure that every group that needs SSH access is in your configuration. AWS Systems Manager (SSM) sessions don't use SSH, so you can still connect with `aws ssm start-session`.

On a node type that no group targets with SSH, only the `ubuntu` user can log in over SSH.

## Example
<a name="sagemaker-hyperpod-slurm-user-management-permissions-example"></a>

The configuration in [Installing the extension](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-installing-the-extension) defines two groups, `hpc-users` and `cluster-admins`, and three users. The following table shows the resulting access on each node type.


| Node type | SSH access | sudo access | 
| --- | --- | --- | 
| Controller | admin-1, ubuntu | admin-1 | 
| Login | admin-1, user-1, user-2, ubuntu | admin-1 | 
| Compute | admin-1, user-1, user-2, ubuntu | admin-1 | 

To make user-2 an administrator, add `cluster-admins` to user-2's groups, without changing any rule. To stop regular users from logging in to compute nodes directly, change the `hpc-users` SSH target to `["login"]`. Users can still run jobs on compute nodes through Slurm, but workloads that start processes over SSH, such as some MPI launchers, need SSH access to compute nodes.

## Local users
<a name="sagemaker-hyperpod-slurm-user-management-permissions-local-users"></a>

To use SSH, for example from an IDE, a user adds their public key to `~/.ssh/authorized_keys` and must be in a group that grants SSH to the node type. The extension keeps keys already in that file. For SSM sessions that start as their own user, see [Mapping cluster users to IAM principals for access](sagemaker-hyperpod-slurm-user-management-iam-mapping.md).

## sudo access
<a name="sagemaker-hyperpod-slurm-user-management-permissions-sudo-access"></a>

A sudo rule gives the group's members passwordless sudo for all commands on the targeted node types. This is full root access, so grant it only to administrators.

## Reviewing who has access
<a name="sagemaker-hyperpod-slurm-user-management-permissions-reviewing-who-has-access"></a>

The extension's configuration is the cluster's access policy, so you can review access from the API without connecting to nodes. A principal with read-only permissions can do this. For an example policy, see [Prerequisites and IAM permissions for cluster extensions](sagemaker-hyperpod-slurm-extensions-prerequisites.md).

The following command lists the groups, local and directory, whose members get sudo on the controller. To check another node type or SSH access, change `controller` or `.sudo`.

```
aws sagemaker describe-cluster-extension \
    --cluster-arn arn:aws:sagemaker:{{us-west-2}}:{{111122223333}}:cluster/{{abcd1234efgh}} \
    --extension-arn {{extension-arn}} \
    --query ExtensionDetails.ConfigurationValues --output text |
  jq '[.userSources.localUsers.groups[]?, .userSources.ldap.ldapGroups[]?]
      | map(select(any(.sudo[]?; .nodeTypes | index("controller")))) | map(.name)'
```

Local groups list their members in `users`. For directory groups, check membership in your directory. If the status is `Active`, `ActiveCount` equals `TotalCount`, and there is no Health, every node runs this configuration.