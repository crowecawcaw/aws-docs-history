

# User management extension

The SageMaker HyperPod user management extension (`sagemaker-user-management`) manages users, groups, and their SSH and sudo access on every node of your Slurm cluster, including nodes that you add later and nodes that HyperPod replaces. You declare who exists and what they can do, and you don't need to connect to nodes or run scripts to add or remove a user.

The extension supports two user sources, which you can use alone or together:
+ **Local users (`localUsers`):** You list users and groups in the extension's configuration. The extension creates them as POSIX accounts with the same user ID (UID) and group ID (GID) on every node, and gives each user a user private group (UPG) with the same name. It also creates home directories on your shared file system, generates an SSH key pair in each user's home directory so that users can connect between nodes without a password, and registers users with Slurm accounting.
+ **Active Directory (`ldap`):** The extension configures SSSD on every node to resolve users and groups from an Active Directory directory over LDAPS, for example AWS Directory Service for Microsoft Active Directory. It doesn't create local accounts for directory users. You manage directory users and their group membership in the directory. For more information, see [Integrate HyperPod clusters with Active Directory](sagemaker-hyperpod-slurm-user-management-active-directory.md).

**Important**  
The user management extension controls which users and groups exist on your cluster, which nodes they can log in to, and who has sudo.  
Anyone who can call `UpdateClusterExtension` for this extension can grant themselves or others root access on the cluster's nodes. Grant `CreateClusterExtension`, `UpdateClusterExtension`, and `DeleteClusterExtension` only to cluster administrators, and never to the cluster's execution role. For more information, see [Who should have extension permissions](sagemaker-hyperpod-slurm-extensions-prerequisites.md#sagemaker-hyperpod-slurm-extensions-prerequisites-who-should-have-extension-permissions).

## Prerequisites
<a name="sagemaker-hyperpod-slurm-user-management-extension-prerequisites"></a>
+ **Cluster extension prerequisites:** Meet the prerequisites in [Prerequisites and IAM permissions for cluster extensions](sagemaker-hyperpod-slurm-extensions-prerequisites.md), including a cluster that uses continuous provisioning and a HyperPod default AMI released on or after November 2, 2026.
+ **A shared file system for home directories:** Mount a shared file system on every node, and set `sharedFilesystemMount` to it. If you don't set it, the extension uses an NFS file system at `/home`, then Amazon FSx for Lustre at `/fsx`, then each node's local disk. On local disk, each node has its own home directory and SSH key, so users can't connect between nodes. When home directories aren't on FSx for Lustre at `/fsx`, each user also gets a data directory at `/fsx/{{username}}`, where {{username}} is the user's name.
+ **Root access from the controller to the shared file system:** The controller node creates and removes home directories on the shared file system. If the file system squashes root, allow the controller to reach it as root. For FSx for Lustre, add the controller node to the file system's `NoSquashNids` setting. For more information, see [Lustre root squash](https://docs.aws.amazon.com/fsx/latest/LustreGuide/root-squash.html) in the *Amazon FSx for Lustre User Guide*. For FSx for OpenZFS, add an NFS client configuration with the `no_root_squash` option for the controller node. For more information, see [Creating an Amazon FSx for OpenZFS volume](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/creating-volumes.html) in the *Amazon FSx for OpenZFS User Guide*. Both settings replace the existing list, so include the entries that you already have. A replaced controller node can get a new IP address, so we recommend that you use the subnet's CIDR range rather than a single IP address. Without root access, the extension can't create or remove home directories, and the operation fails on the controller.
+ **Slurm accounting:** `slurmctld` must be running on the controller. If the cluster uses `slurmdbd`, it must respond within 2 minutes, or the controller fails with `DependencyUnreachable`. Without `slurmdbd`, the extension skips Slurm accounting.
+ **Planned UIDs and GIDs:** Choose IDs from 2000 to 60000 that don't collide with existing accounts on the nodes or with IDs that you use elsewhere on the shared file system. If you use Active Directory with `ldapIdMapping` set to `DISABLED`, the IDs must also not collide with the directory's `uidNumber` and `gidNumber` values. Keep each UID and GID fixed for the life of the cluster. We recommend that you don't reuse an ID after you delete it. If you do, the new user gets the previous user's files on the shared file system, and nodes that haven't removed the old account yet can conflict with the new one.
+ **Active Directory prerequisites:** If you use Active Directory, see the prerequisites in [Prerequisites](sagemaker-hyperpod-slurm-user-management-active-directory.md#sagemaker-hyperpod-slurm-user-management-active-directory-prerequisites).

### Execution role permissions
<a name="sagemaker-hyperpod-slurm-user-management-extension-execution-role-permissions"></a>

Local users need no execution role permissions beyond the prerequisites for cluster extensions. For Active Directory, see [Prerequisites](sagemaker-hyperpod-slurm-user-management-active-directory.md#sagemaker-hyperpod-slurm-user-management-active-directory-prerequisites).

## Installing the extension
<a name="sagemaker-hyperpod-slurm-user-management-extension-installing-the-extension"></a>

Install the user management extension to manage users, groups, and their SSH and sudo access through an API instead of scripts on each node. Use the console or the AWS CLI.

**To install the user management extension with the console**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On your cluster's details page, choose the **Extensions** tab.

1. On the **Amazon SageMaker HyperPod user management** card, choose **Actions**, and then choose **Custom install**.

1. On **Configure settings**, under **User sources**, choose **Local users**, **Directory (LDAP)**, or both.

1. If you chose **Directory (LDAP)**, under **Directory connection**, enter the **LDAPS URIs**, **Search base**, and **Bind DN**, and choose the **Bind password secret ARN** and the **CA certificate secret ARN**. (Optional) Enter a **Domain** and expand **Advanced settings**.

1. (Optional) Enter a **Home directory base path**, such as `/fsx`. If you leave it blank, the extension detects a shared file system.

1. Choose **Next**. (Optional) If you chose **Local users**, add groups and users on **Add local groups and users**, and then choose **Next**.

1. On **Review and install**, check the settings, and then choose **Install extension**.

The card shows **Creating**, and then **Active**. To add or change users and groups later, choose **Manage users** on the card.

**Quick install** installs the extension with local users and no users or groups. This restricts SSH to the `ubuntu` user until you add users with SSH access.

**To install the user management extension with local users by using the AWS CLI**

In the commands, replace {{us-west-2}}, {{111122223333}}, {{abcd1234efgh}}, and {{extension-arn}} with your AWS Region, account ID, cluster ID, and extension ARN.

1. Prepare a configuration file in JSON format with your groups and users. The following example creates an administrators group, a users group, and three users. For all settings, see [User management extension configuration](sagemaker-hyperpod-slurm-user-management-config.md).

   ```json
   {
    "sharedFilesystemMount": "/fsx",
    "userSources": {
      "localUsers": {
        "groups": [
          { "name": "hpc-users", "gid": 3001,
            "ssh": [ { "nodeTypes": ["login", "compute"] } ] },
          { "name": "cluster-admins", "gid": 3002,
            "ssh":  [ { "nodeTypes": ["controller", "login", "compute"] } ],
            "sudo": [ { "nodeTypes": ["controller", "login", "compute"] } ] }
        ],
        "users": [
          { "username": "admin-1", "uid": 2001, "groups": ["cluster-admins", "hpc-users"] },
          { "username": "user-1",  "uid": 2002, "groups": ["hpc-users"] },
          { "username": "user-2",  "uid": 2003, "groups": ["hpc-users"] }
        ]
      }
    }
   }
   ```

1. Run `create-cluster-extension` to install the extension. The configuration is required.

   ```
   aws sagemaker create-cluster-extension \
      --cluster-arn arn:aws:sagemaker:{{us-west-2}}:{{111122223333}}:cluster/{{abcd1234efgh}} \
      --extension-name sagemaker-user-management \
      --configuration-values "$(jq -c . users-config.json)"
   ```

   This returns the ARN of the extension. Save it for later changes.

1. Run `describe-cluster-extension` until the status is `Active` and `ActiveCount` equals `TotalCount`.

   ```
   aws sagemaker describe-cluster-extension \
      --cluster-arn arn:aws:sagemaker:{{us-west-2}}:{{111122223333}}:cluster/{{abcd1234efgh}} \
      --extension-arn {{extension-arn}} \
      --query '{Status: ExtensionDetails.Status, Nodes: NodeSummary, Health: Health}'
   ```

   If the status becomes `CreateFailed`, Health names the setting that the nodes couldn't apply. For more information, see [Troubleshooting](sagemaker-hyperpod-slurm-user-management-manage.md#sagemaker-hyperpod-slurm-user-management-manage-troubleshooting).

1. Connect to a login node through AWS Systems Manager (SSM), and check the users and groups. For how to connect, see [Accessing your SageMaker HyperPod cluster nodes](sagemaker-hyperpod-run-jobs-slurm-access-nodes.md).

   ```
   $ id user-1
   uid=2002(user-1) gid=2002(user-1) groups=2002(user-1),3001(hpc-users)
   $ getent group hpc-users
   hpc-users:x:3001:admin-1,user-1,user-2
   $ ls -ld /fsx/user-1
   ```

   On the controller node, you can check the Slurm association, which is with the `root` account.

   ```
   $ sacctmgr show assoc user=user-1 format=account,user
   ```

1. Give your users access to the cluster. Map each user's AWS Identity and Access Management (IAM) principal to their Linux user, so that their SSM session starts as that user. For more information, see [Mapping cluster users to IAM principals for access](sagemaker-hyperpod-slurm-user-management-iam-mapping.md). To use SSH, each user adds their own public key to `~/.ssh/authorized_keys`.

1. As a user, run a job on a compute node to test access.

   ```
   $ srun -N1 id
   ```

**Tip**  
`ConfigurationValues` can be up to 10,240 characters, which fits about 40–60 users with groups. Send the file minified, for example `--configuration-values "$(jq -c . users-config.json)"`. For more users, use Active Directory.

## New and replaced nodes
<a name="sagemaker-hyperpod-slurm-user-management-extension-new-and-replaced-nodes"></a>

When HyperPod adds or replaces a node, the extension creates every user and group on it, with the same UIDs, GIDs, and home directories on the shared file system. You don't need to do anything.

**Note**  
A node that HyperPod adds or replaces can accept Slurm jobs for 1–2 minutes before the extension creates the users on it. A job that's scheduled on that node during this time, for a user who doesn't exist there yet, can fail. Resubmit the job.

## Logs and health checks
<a name="sagemaker-hyperpod-slurm-user-management-extension-logs-and-health-checks"></a>

The extension logs each run on a node to the `SageMakerUserManagement/{{instance-group-name}}/{{instance-id}}` log stream in your cluster's log group.

The extension also checks the following on each node. An unhealthy node makes the extension `Degraded`, and appears in Health in the `describe-cluster-extension` response with the code `ExtensionUnhealthy` and the message of the check that failed. The extension doesn't repair these problems. Fix the cause on the node. When the node reports healthy again, the status returns to `Active` without an API call. To apply the extension's software and configuration to the node again, run `update-cluster-extension` with a corrected or changed configuration.

The extension's own health log records the following codes. A healthy node reports `Healthy`. Otherwise it reports the code of the first component that isn't healthy.


| Component | Code | Status | Meaning | 
| --- | --- | --- | --- | 
| directory | SSSDNotRunning | Unhealthy | SSSD isn't running, so directory users can't log in on this node. | 
| directory | DirectoryOffline | Unhealthy | SSSD can't reach the directory, so only users in its cache can log in. Reported as unknown at first, and as unhealthy if it's still offline at the next check. | 
| homes | HomeShareMissing | Unhealthy | The file system that holds home directories isn't mounted. Reported as unknown at first, and as unhealthy if it's still missing at the next check. | 
| homes | HomeShareChanged | Unhealthy | Home directories would now go on a different file system. | 
| ssh | SSHDropInMissing | Unhealthy | The extension's SSH rules file was removed from the node. | 
| ssh | SSHNotApplied | Unhealthy | The node's SSH server doesn't apply the extension's rules. | 
| sudo | SudoersMissing | Unhealthy | The extension's sudo rules file was removed from the node. | 
| any | CheckFailed | Unknown | The extension couldn't run a check on this node. It tries again at the next check. | 
| node | NodeStarting | Unknown | The node started less than 10 minutes ago, so its checks wait for its file systems and SSSD. | 

An unknown result doesn't make the extension `Degraded`.

## Limitations
<a name="sagemaker-hyperpod-slurm-user-management-extension-limitations"></a>

The following list describes the extension's limitations. To see the versions that you can install, run `list-cluster-extension-versions`.
+ Every account is created on every node. You can limit where a group grants SSH and sudo access, but not where an account is created.
+ SSH and sudo access is targeted by node type. You can't target a specific instance group or instance type.
+ A sudo rule grants passwordless sudo for all commands. You can't limit it to specific commands.
+ Users can't join reserved system groups such as `docker`, `sudo`, `wheel`, or `adm`. For the full list, see [Reserved names](sagemaker-hyperpod-slurm-user-management-config.md#sagemaker-hyperpod-slurm-user-management-config-reserved-names).
+ A cluster can use one Active Directory domain.
+ Directory users don't get Slurm associations automatically. Add them with `sacctmgr` if your Slurm configuration requires associations.
+ You can't choose the Slurm account for a local user. Each local user gets an association under Slurm's `root` account, which grants no login or sudo access. Limits on `root` apply to these users together, and they share its fairshare. You can set per-user limits with `sacctmgr`.
+ The extension doesn't map IAM principals to Linux users. To have each person's SSM session start as their own Linux user, see [Mapping cluster users to IAM principals for access](sagemaker-hyperpod-slurm-user-management-iam-mapping.md).
+ The configuration has no setting for a local user's own SSH public key. Users add their own keys to `~/.ssh/authorized_keys` in their home directory.
+ The extension doesn't add users to the `docker` group, because membership is equivalent to root. To run containers, use Enroot with Pyxis (`srun --container-image`), or add a user to the group yourself with `sudo usermod -aG docker {{username}}`.
+ UIDs and user names are checked for uniqueness on the nodes, not when you make the request. Two users with the same UID pass the API check and then fail on every node.
+ Deleting the extension keeps users, groups, and home directories on the nodes, but removes the SSH rules, so SSH is no longer limited to the groups that you granted. For more information, see [Delete the extension](sagemaker-hyperpod-slurm-user-management-manage.md#sagemaker-hyperpod-slurm-user-management-manage-delete-the-extension).

## Shared responsibility
<a name="sagemaker-hyperpod-slurm-user-management-extension-shared-responsibility"></a>

You define the policy: which users and groups exist, their IDs, and which groups get SSH and sudo access on which node types. When you use Active Directory, you also own the directory, its group membership, and its credentials. HyperPod applies what you declare to every node and keeps the nodes in sync. It doesn't make access decisions of its own.

## Migrating from user management scripts
<a name="sagemaker-hyperpod-slurm-user-management-extension-migrating-from-user-management-scripts"></a>

If you created users with `create_users.sh`, with the add-users extension script, or with `add_users.sh` in the base lifecycle scripts, you can move to the user management extension without recreating your users. When the extension finds an existing account with the same user name, UID, and home directory as a user in your configuration, it takes over that account and doesn't change it. The account keeps its home directory, files, and SSH keys.

**Note**  
The add-users extension script is a lifecycle script that runs with the `OnInitComplete` option. It isn't a cluster extension.

### Move users that you created with scripts
<a name="sagemaker-hyperpod-slurm-user-management-extension-move-users-that-you-created-with-scripts"></a>

1. List your existing users. On the controller node, find each user's name, UID, and home directory, for example with `getent passwd {{username}}`. If you used a `shared_users.txt` file, it has the same information.

1. Write a configuration with the same values. Set `username` and `uid` to the existing values. Set `homeDirectory` to the existing home directory if it isn't `{{mount}}/{{username}}`. Give each group an explicit `gid`, and keep existing GIDs. For example, a user that the add-users extension script created with the home directory `/fsx/users/user-1`:

   ```json
   { "username": "user-1", "uid": 2002, "homeDirectory": "/fsx/users/user-1", "groups": ["hpc-users"] }
   ```

1. Keep your users' SSH access. After you install the extension, only the groups that you grant SSH access to can log in over SSH. Add every user to a group with `ssh` targets for the node types that they use.

1. Install the extension, as described in [Installing the extension](#sagemaker-hyperpod-slurm-user-management-extension-installing-the-extension). Keep an SSM session open while you test SSH, and check that each user can log in and run a job.

1. Stop the scripts from running on new nodes. Otherwise both the script and the extension create users on nodes that join the cluster.
   + For the add-users extension script, remove `add_users.sh` from your `OnInitComplete` script, or set `ENABLE_ADD_USERS="false"` in `run_extensions.sh`.
   + For the base lifecycle scripts, empty or delete `shared_users.txt` in the Amazon S3 location of your lifecycle scripts. The base scripts have no setting to turn off user creation, but `add_users.sh` skips new nodes when the file is empty or missing. This also stops `setup_user_associations.sh` from adding those users to Slurm's `root` account. The extension adds its own association for them.
   + `create_users.sh` runs only when you run it, so there's nothing to turn off.

   For how to update lifecycle scripts on an existing cluster, see [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md).

If the extension finds an account with the same name but a different UID, or a UID that belongs to a different account, it stops on that node before it changes anything, and the extension's status becomes `CreateFailed` or `UpdateFailed`. Correct your configuration and update the extension.

Slurm associations that your scripts created, such as a `slurm_account` from `shared_users.yaml`, stay in place. The extension adds an association with Slurm's `root` account.

Users that you created with `create_users.sh` are in the `docker` group. The extension leaves existing memberships in place, but doesn't add new users to it.

### Move a directory setup from the base lifecycle scripts
<a name="sagemaker-hyperpod-slurm-user-management-extension-move-a-directory-setup-from-the-base-lifecycle-scripts"></a>

If you set `enable_sssd = True` in the base lifecycle scripts, do the following.

1. Create the two Secrets Manager secrets, and give the execution role access to them, as described in [Prerequisites](sagemaker-hyperpod-slurm-user-management-active-directory.md#sagemaker-hyperpod-slurm-user-management-active-directory-prerequisites) on the Integrating with Active Directory page. The extension reads the bind password from Secrets Manager, instead of the obfuscated password in `config.py`. If your current bind account can do more than read the directory, replace it with a dedicated, read-only account first.

1. List the groups from your `ssh_allow_groups` and `sudoers_groups` settings in `ldapGroups`, with matching `ssh` and `sudo` targets. Groups such as `ClusterAdmin` and `ClusterDev` had access by default with the base lifecycle scripts. With the extension, each group needs its own entry.

1. Install or update the extension with the `ldap` source. Map your `SssdConfig` settings as follows:
   + `ldap_uri` becomes `ldapUri`, as a list.
   + `ssh_auth_method` becomes `sshAuthMethod` (`PUBLIC_KEY` or `PASSWORD`).
   + `override_homedir` becomes `ldap.sharedFilesystemMount`. Set it to the directory in `override_homedir`, for example `/fsx` for `/fsx/%u`. If you don't set it, directory users get new, empty home directories.

   Other settings keep their names, in camel case.

1. Set `enable_sssd = False` in `config.py`, so that new nodes don't run both setups. The extension replaces the SSSD configuration that the script wrote. It doesn't remove the script's sudo rules file for the cluster administrators group (`/etc/sudoers.d/100-ldap-cluster-admin`). Remove it if you no longer want those rules.