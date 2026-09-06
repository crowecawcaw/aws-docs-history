

# Creating users on a Slurm cluster on SageMaker HyperPod
<a name="sagemaker-hyperpod-slurm-user-management-create-users"></a>

There are three ways to create POSIX users across the nodes of a Slurm cluster on SageMaker HyperPod. They differ in *when* users are created and *how much* lifecycle configuration you have to manage. Choose the option that matches your cluster and workflow, listed here from easiest to most advanced.


| Option | Best for | Lifecycle configuration required | When users are created | Behavior on scale-up or node replacement | 
| --- | --- | --- | --- | --- | 
| [Option A: Add users with the create users utility script](#sagemaker-hyperpod-multi-user-method-1-create-users) | Adding users to a cluster that is already InService, without touching lifecycle configuration | None | On demand, whenever you run the script | Manual. Users are not applied automatically; re-run the script whenever nodes are added or replaced (automatically or manually). | 
| [Option B: Add users with the `add-users` extension script](#sagemaker-hyperpod-multi-user-method-2-add-users-extension) | AMI-based lifecycle configured clusters that provision users automatically | Add users extension scripts | Automatically during node provisioning — during cluster creation, adding nodes (scale-up), AMI updates, node replacements. | Automatic. The extension runs on each new node during provisioning, using the user file in the lifecycle scripts Amazon S3 bucket. | 
| [Option C: Add users with the base lifecycle scripts](#sagemaker-hyperpod-multi-user-method-3-base-lcs) | Clusters that already use the full custom base lifecycle script set | Full custom lifecycle script set | Automatically during node provisioning — during cluster creation, adding nodes (scale-up), AMI updates, node replacements. | Automatic. The base lifecycle script runs on each new node during provisioning, using the user file in the lifecycle scripts Amazon S3 bucket. | 

All three options use scripts that the SageMaker HyperPod service team provides in the [Awsome Distributed Training](https://github.com/awslabs/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod) repository on the GitHub website.

**Topics**
+ [Option A: Add users with the create users utility script](#sagemaker-hyperpod-multi-user-method-1-create-users)
+ [Option B: Add users with the `add-users` extension script](#sagemaker-hyperpod-multi-user-method-2-add-users-extension)
+ [Option C: Add users with the base lifecycle scripts](#sagemaker-hyperpod-multi-user-method-3-base-lcs)

## Option A: Add users with the create users utility script
<a name="sagemaker-hyperpod-multi-user-method-1-create-users"></a>

This is the simplest option and requires no lifecycle configuration. Use it when your cluster is already **InService** and you want to add users right now. Run the [create\_users.sh](https://github.com/awslabs/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/utils/create_users.sh) utility script on the GitHub website on the controller node to create users across every node in a single run. The script auto-detects the other nodes from the cluster configuration files, creates the users over SSH, and configures compute nodes in parallel to scale to large clusters. The script supports three modes for specifying users, selected by the arguments you pass and the files present in the current directory, in the following priority order:
+ **Command line mode** — you pass user names as arguments and the script auto-assigns UIDs. This is the quickest way to add users.
+ **File mode** — the script reads user definitions from a `shared_users.txt` (CSV) or `shared_users.yaml` (YAML) file in the current directory.
+ **Interactive mode** — the script prompts you for user names and, optionally, UIDs.

**Important**  
In every mode, `create_users.sh` creates users only on the nodes that exist when you run it. This includes file mode with a local `shared_users.txt` or `shared_users.yaml`. Users are **not** automatically recreated on nodes added later by scale-up or node replacement. Those are provisioning events in which the new node boots with a fresh root volume that has no POSIX accounts. (Home directories and SSH keys on the shared file system survive, but the user accounts themselves do not.) Re-run `create_users.sh` after the new nodes are added to bring them in line.  
Re-running the script is safe. Run it on the controller node; it discovers the other cluster nodes and applies users across the whole cluster in one run. It is idempotent per node: it creates a user only where missing, leaving nodes that already have the user unchanged — so re-running after adding nodes affects only the new nodes.  
To have new nodes receive users automatically, the user file must be part of the cluster's lifecycle configuration so it runs during provisioning: store a `shared_users.txt` or `shared_users.yaml` file in your lifecycle scripts Amazon S3 bucket and use it with the [Option B: Add users with the `add-users` extension script](#sagemaker-hyperpod-multi-user-method-2-add-users-extension) or the [Option C: Add users with the base lifecycle scripts](#sagemaker-hyperpod-multi-user-method-3-base-lcs). `create_users.sh` helps by appending every user it creates to `shared_users.txt` and offering to upload it to Amazon S3, but on its own — in any mode — it does not make users persist across provisioning events.

For each user, the script:
+ Creates a POSIX user with a consistent UID on every node.
+ Creates a home directory on the shared file system (auto-detecting OpenZFS at `/home` or Amazon FSx for Lustre at `/fsx`).
+ Generates an SSH key pair on the shared file system for passwordless inter-node SSH.
+ Adds the user to the `docker` group (and, optionally, grants sudo access).
+ Registers the user with Slurm accounting on the controller so they can submit jobs.
+ Appends the new users to a `shared_users.txt` file and optionally uploads it to Amazon S3, so you can reuse it with the other options.

**Prerequisites**  
Before you begin, verify the following requirements are met.
+ The cluster is **InService** and you can connect to the controller node. See [Accessing your SageMaker HyperPod cluster nodes](sagemaker-hyperpod-run-jobs-slurm-access-nodes.md).
+ `jq` is installed on the controller node.
+ SSH access is available from the controller node to all other nodes (HyperPod configures this for the default user).

**To add users with the `create_users.sh` utility script**  
Complete the following steps.

1. Connect to the controller node and download the script. Make sure you run it with sudo permissions.

   ```
   $ curl -O https://raw.githubusercontent.com/awslabs/awsome-distributed-training/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/utils/create_users.sh
   chmod +x create_users.sh
   ```

1. Run the script using one of its three modes, which it selects by priority from the arguments you pass and the files in the current directory: command line arguments first, then a user file, then interactive prompts. Every mode runs the same sequence: create the users on the current node, set up SSH keypairs on the shared file system, create the users on all remaining nodes (compute nodes in parallel), register them with Slurm accounting on the controller, append them to `shared_users.txt`, and offer to upload that file to Amazon S3.

   The three modes are described in the following examples, each adding two users (`user1` and `user2`).

**Command line mode**  
Pass the user names as arguments. The script auto-assigns UIDs and prompts whether the new users should be sudoers. This is the quickest way to add users.

   ```
   $ sudo ./create_users.sh user1 user2
   ```

   The script validates the user names, then prompts for sudoer access:

   ```
   ========================================
    Step 1: User Configuration
   ========================================
     Users from CLI args: user1 user2
       ✓ user1 — will be created (auto-assign UID)
       ✓ user2 — will be created (auto-assign UID)
     Make these user(s) sudoer(s)? (y/N): n
   ```

   It then creates the users on the current node, sets up SSH keypairs, creates them on the compute nodes, registers them with Slurm accounting on the controller, and writes `shared_users.txt`, prompting you at the end to upload that file to Amazon S3.

**File mode**  
Create a user file in the same directory as the script, then run the script with no arguments. The script reads the user definitions, validates them (creating only users that don't already exist and skipping UID conflicts), and creates the users across all nodes. The script accepts two file formats.

   For `shared_users.txt`, use a CSV file with one user per line in the format `username,uid,home_directory`:

   ```
   user1,2001,/fsx/user1
   user2,2002,/fsx/user2
   ```

   Alternatively, for `shared_users.yaml`, use a YAML file with either a simple list of users or users organized into groups. Parsing this format requires PyYAML on the node. The following is the simple list format:

   ```
   users:
     - username: user1
       uid: 2001
     - username: user2
       uid: 2002
   ```

   If both files are present, `shared_users.txt` takes precedence. Run the script with no arguments:

   ```
   $ sudo ./create_users.sh
   ```

   The script validates the file entries, confirms creation, prompts for sudoer access, and offers to add users that are not in the file. It then creates `user1` and `user2` on all nodes with the UIDs from the file (2001 and 2002), sets up SSH keypairs, registers them with Slurm accounting, and updates `shared_users.txt`.

**Interactive mode**  
Run the script with no arguments and no user file present. The script prompts you for the user names and, optionally, the UIDs to assign:

   ```
   $ sudo ./create_users.sh
   ```

   ```
   ========================================
    Step 1: User Configuration
   ========================================
     No shared_users.txt or shared_users.yaml found.
     Entering interactive mode...
   
     Enter username(s), comma-separated (e.g. 'sean' or 'sean,alice,bob'): user1,user2
     Specify UIDs? (Enter for auto-assign, or comma-separated UIDs): 2001,2002
     Make these user(s) sudoer(s)? (y/N): n
   ```

   After you answer the prompts, the script creates `user1` and `user2` on all nodes with the UIDs you entered, sets up SSH keypairs, registers them with Slurm accounting, and updates `shared_users.txt`.

1. Test a user by switching to it and running a command across the cluster.

   ```
   $ sudo su - user1 && ssh $(srun hostname)
   ```

**Note**  
The script is idempotent. Users that already exist are skipped, and existing SSH keys and Slurm accounting associations are left in place, so it is safe to re-run.

## Option B: Add users with the `add-users` extension script
<a name="sagemaker-hyperpod-multi-user-method-2-add-users-extension"></a>

Use this option when your cluster uses **AMI-based configuration** and you want users to be provisioned automatically. With the extension lifecycle option, SageMaker HyperPod runs the full AMI-based configuration first, then runs your extension script. The service team provides a ready-to-use [add-users](https://github.com/awslabs/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/Extensions/add-users) extension in the Extensions folder of the Awsome Distributed Training repository on the GitHub website. Because the extension runs during node provisioning, users are created automatically when the cluster is created and again on any new nodes added during scale-out.

For more information about setting up extensions:
+ To set up extensions using the AWS console, see **Lifecycle configuration - optional** under [Custom setup](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-slurm-console.html#smcluster-getting-started-slurm-console-create-cluster-custom).
+ To set up extensions using the API, see **Option B: Extend AMI-based configuration with OnInitComplete** under [Create your cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-slurm-cli.html#smcluster-getting-started-slurm-cli-create-cluster).

The `add-users` extension creates POSIX users with consistent UIDs, sets up home directories on the shared file system, generates SSH key pairs for passwordless inter-node SSH, and registers users with Slurm accounting on the controller. It accepts two input formats:
+ `shared_users.txt` — the same CSV format used by the base lifecycle scripts (`username,uid,/fsx/username`). All users are added to the `root` Slurm account.
+ `shared_users.yaml` — a YAML format that additionally supports organizing users into groups with per-group Slurm accounts and file system mounts. Groups are organizational only; they do not create Linux groups.

The following is an example `shared_users.yaml` using the groups format:

```
groups:
  - name: research
    slurm_account: research
    users:
      - username: user1
        uid: 2001
      - username: user2
        uid: 2002
  - name: platform
    slurm_account: platform
    users:
      - username: user3
        uid: 3001
```

**To add users with the `add-users` extension at cluster creation**  
Complete the following steps.

1. Copy the appropriate sample file in the `add-users` directory and edit it with your users:

   ```
   $ cp shared_users_sample.yaml shared_users.yaml
   ```

1. Upload the `add-users` directory to your lifecycle scripts Amazon S3 bucket (the bucket path must start with `s3://sagemaker-`):

   ```
   $ aws s3 cp add-users/ s3://DOC-EXAMPLE-BUCKET/add-users/ --recursive
   ```

1. Specify the extension in the `LifeCycleConfig` block of your `CreateCluster` request, using `add_users.sh` as the `OnInitComplete` script:

   ```
   "LifeCycleConfig": {
       "OnInitComplete": "add_users.sh",
       "SourceS3Uri": "s3://DOC-EXAMPLE-BUCKET/add-users/"
   }
   ```

**Tip**  
If your cluster needs multiple capabilities in addition to user creation (for example, observability), upload the entire Extensions folder and use the `run_extensions.sh` orchestrator as your extension script. It provides simple boolean toggles such as `ENABLE_ADD_USERS="true"` to enable each capability. For details, see [Getting started with SageMaker HyperPod using the AWS CLI](smcluster-getting-started-slurm-cli.md).

**To add users to an existing cluster after creation**  
Because the extension runs only during node provisioning, adding users to nodes that are already running requires you to run the extension manually.

1. Update your user file with the new users (keep the existing users in the file) and upload it to Amazon S3:

   ```
   $ aws s3 cp add-users/shared_users.yaml s3://DOC-EXAMPLE-BUCKET/add-users/shared_users.yaml
   ```

1. Connect to the controller node and pull the scripts to the shared file system:

   ```
   $ sudo mkdir -p /fsx/cluster-scripts/add-users
   sudo aws s3 cp s3://DOC-EXAMPLE-BUCKET/add-users/ /fsx/cluster-scripts/add-users/ --recursive
   sudo chmod +x /fsx/cluster-scripts/add-users/*.sh
   ```

1. Run the extension on the controller:

   ```
   $ sudo bash /fsx/cluster-scripts/add-users/add_users.sh
   ```

1. Run the extension on the compute nodes with `srun`:

   ```
   $ sudo srun --partition={{partition-name}} bash /fsx/cluster-scripts/add-users/add_users.sh
   ```

The scripts skip existing users and create only new ones; they are idempotent.

## Option C: Add users with the base lifecycle scripts
<a name="sagemaker-hyperpod-multi-user-method-3-base-lcs"></a>

Use this option only if your cluster already uses the full custom base lifecycle script set, where your scripts own the entire provisioning sequence. This is the most advanced option because you manage the complete lifecycle script set rather than a single extension. The service team provides the [add\_users.sh](https://github.com/awslabs/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/add_users.sh) script on the GitHub website as one script within the base-config lifecycle script set. During cluster creation, cluster update, or cluster software update, the lifecycle script runner (`lifecycle_script.py`) runs `add_users.sh`, which reads a `shared_users.txt` file and creates the users and their home directories.

In this option, `add_users.sh` handles POSIX user and home directory creation only. SSH keypair generation for passwordless inter-node SSH is a separate module in the base lifecycle script set (for example, `gen-keypair-ubuntu.sh`), which the lifecycle script runner invokes as part of the full set. Make sure the SSH key module is included in your lifecycle script set so that users get keypairs on the shared file system.

For more information about setting up the full custom lifecycle script set:
+ To set up lifecycle scripts using the AWS console, see **Lifecycle configuration - optional** under [Custom setup](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-slurm-console.html#smcluster-getting-started-slurm-console-create-cluster-custom).
+ To set up lifecycle scripts using the API, see **Option C: Full custom control with OnCreate** under [Create your cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-getting-started-slurm-cli.html#smcluster-getting-started-slurm-cli-create-cluster).

**To create users during Slurm cluster creation**  
Complete the following steps.

1. Download the [base-config](https://github.com/awslabs/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config) lifecycle script set from the GitHub website. With this option, you upload the entire base-config folder as your lifecycle script set, not just `add_users.sh`.

1. In the base-config folder, create or edit a text file named `shared_users.txt` in the following format. The first column is the user name, the second column is the unique user ID, and the third column is the user directory in the Amazon FSx shared space.

   ```
   username1,uid1,/fsx/username1
   username2,uid2,/fsx/username2
   ...
   ```

   `add_users.sh` reads `shared_users.txt` from the same folder, so the file must be inside base-config alongside the script.

1. Upload the entire base-config folder to the Amazon S3 bucket for your HyperPod lifecycle scripts. While cluster creation, cluster update, or cluster software update is in progress, the lifecycle script runner runs `add_users.sh`, which reads `shared_users.txt` and sets up the users and their home directories.

**Note**  
`add_users.sh` automatically detects the shared file system: if OpenZFS is mounted at `/home` it creates home directories there; otherwise it uses the Amazon FSx for Lustre path.