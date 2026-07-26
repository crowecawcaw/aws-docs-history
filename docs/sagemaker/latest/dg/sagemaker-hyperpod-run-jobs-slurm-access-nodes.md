# Accessing your SageMaker HyperPod cluster nodes

You can access your **InService** cluster through AWS Systems Manager (SSM)
by running the AWS CLI command `aws ssm start-session` with the SageMaker HyperPod
cluster host name in format of
`sagemaker-cluster:[cluster-id]_[instance-group-name]-[instance-id]`. You
can retrieve the cluster ID, the instance ID, and the instance group name from the [SageMaker HyperPod console](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-view-details-of-clusters "sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-view-details-of-clusters") or by running `describe-cluster` and
`list-cluster-nodes` from the [AWS CLI commands
for SageMaker HyperPod](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-list-cluster-nodes "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-list-cluster-nodes"). For example, if your cluster ID is
`aa11bbbbb222`, the cluster node name is `controller-group`,
and the cluster node ID is `i-111222333444555aa`, the SSM `start-session` command should be the following.

###### Note

Granting users access to HyperPod cluster nodes allows them to install
and operate user-managed software on the nodes. Ensure that you maintain the
principle of least-privilege permissions for users.

If you haven't set up AWS Systems Manager, follow the instructions provided at [Setting up AWS Systems Manager and Run As for cluster user access control](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-ssm "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-ssm").

```
`$` `aws ssm start-session \
 --target sagemaker-cluster:`aa11bbbbb222`_`controller-group`-`i-111222333444555aa` \
 --region `us-west-2``
`Starting session with SessionId: s0011223344aabbccdd`
`root@ip-111-22-333-444:/usr/bin#`
```

Note that this initially connects you as the root user. Before running jobs, switch to
the `ubuntu` user by running the following command.

```
`root@ip-111-22-333-444:/usr/bin#` `sudo su - ubuntu`
`ubuntu@ip-111-22-333-444:/usr/bin#`
```

For advanced settings for practical use of HyperPod clusters, see the following
topics.

###### Topics

- [Additional tips for accessing your SageMaker HyperPod cluster nodes](#sagemaker-hyperpod-run-jobs-slurm-access-nodes-tips "#sagemaker-hyperpod-run-jobs-slurm-access-nodes-tips")
- [Setting up a multi-user environment](#sagemaker-hyperpod-run-jobs-slurm-access-nodes-multi-user "#sagemaker-hyperpod-run-jobs-slurm-access-nodes-multi-user")

## Additional tips for accessing your SageMaker HyperPod cluster nodes

**Use the `easy-ssh.sh` script provided by
HyperPod for simplifying the connection process**

To make the previous process into a single line command, the HyperPod team
provides the [`easy-ssh.sh`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/easy-ssh.sh "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/easy-ssh.sh") script that retrieves your cluster
information, aggregates them into the SSM command, and connects to the compute node.
You don't need to manually look for the required HyperPod cluster information as
this script runs `describe-cluster` and `list-cluster-nodes`
commands and parses the information needed for completing the SSM command. The
following example commands show how to run the [`easy-ssh.sh`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/easy-ssh.sh "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/easy-ssh.sh") script. If it runs successfully, you'll be
connected to the cluster as the root user. It also prints a code snippet to set up SSH by adding the HyperPod cluster as a remote host
through an SSM proxy. By setting up SSH, you can connect your local development environment such as Visual Studio
Code with the HyperPod cluster.

```
`$` `chmod +x easy-ssh.sh`
`$` `./easy-ssh.sh -c `<node-group> <cluster-name>``
`Cluster id: `<cluster_id>`
Instance id: `<instance_id>`
Node Group: `<node-group>`
Add the following to your ~/.ssh/config to easily connect:

`$` cat <<EOF >> ~/.ssh/config
Host `<cluster-name>`
 User ubuntu
 ProxyCommand sh -c "aws ssm start-session --target sagemaker-cluster:`<cluster_id>`_`<node-group>`-`<instance_id>` --document-name AWS-StartSSHSession --parameters 'portNumber=%p'"
EOF

Add your ssh keypair and then you can do:

$ ssh `<cluster-name>`

aws ssm start-session --target sagemaker-cluster:`<cluster_id>`_`<node-group>`-`<instance_id>`

Starting session with SessionId: s0011223344aabbccdd`
`root@ip-111-22-333-444:/usr/bin#`
```

Note that this initially connects you as the root user. Before running jobs,
switch to the `ubuntu` user by running the following command.

```
`root@ip-111-22-333-444:/usr/bin#` `sudo su - ubuntu`
`ubuntu@ip-111-22-333-444:/usr/bin#`
```

**Set up for easy access with SSH by using the HyperPod compute
node as a remote host**

To further simplify access to the compute node using SSH from a local machine, the
`easy-ssh.sh` script outputs a code snippet of setting up the
HyperPod cluster as a remote host as shown in the previous section. The code snippet
is auto-generated to help you directly add to the `~/.ssh/config` file on
your local device. The following procedure shows how to set up for easy access using
SSH through the SSM proxy, so that you or your cluster users can directly run
`ssh `<cluster-name>`` to connect to the
HyperPod cluster node.

1. On your local device, add the HyperPod compute node with a user name as a
   remote host to the `~/.ssh/config` file. The following command
   shows how to append the auto-generated code snippet from the
   `easy-ssh.sh` script to the `~/.ssh/config` file.
   Make sure that you copy it from the auto-generated output of the
   `easy-ssh.sh` script that has the correct cluster
   information.

```
`$` `cat <<EOF >> ~/.ssh/config
Host `<cluster-name>`
 User `ubuntu`
 ProxyCommand sh -c "aws ssm start-session --target sagemaker-cluster:`<cluster_id>`_`<node-group>`-`<instance_id>` --document-name AWS-StartSSHSession --parameters 'portNumber=%p'"
EOF`
```

2. On the HyperPod cluster node, add the public key on your local device to
   the `~/.ssh/authorized_keys` file on the HyperPod cluster
   node.

   1. Print the public key file on your local machine.

   ```
   `$` `cat ~/.ssh/id_rsa.pub`
   ```

   This should return your key. Copy the output of this command.

   (Optional) If you don't have a public key, create one by running
   the following command.

   ```
   `$` `ssh-keygen -t rsa -q -f "$HOME/.ssh/id_rsa" -N ""`
   ```
   2. Connect to the cluster node and switch to the user to add the key.
      The following command is an example of accessing as the
      `ubuntu` user. Replace `ubuntu` to the
      user name for which you want to set up the easy access with
      SSH.

   ```
   `$` `./easy-ssh.sh -c `<node-group> <cluster-name>``
   `$` `sudo su - `ubuntu``
   `ubuntu@ip-111-22-333-444:/usr/bin#`
   ```
   3. Open the `~/.ssh/authorized_keys` file and add the
      public key at the end of the file.

   ```
   `ubuntu@ip-111-22-333-444:/usr/bin#` `vim ~/.ssh/authorized_keys`
   ```

After you finish setting up, you can connect to the HyperPod cluster node as the
user by running a simplified SSH command as follows.

```
`$` `ssh `<cluster-name>``
`ubuntu@ip-111-22-333-444:/usr/bin#`
```

Also, you can use the host for remote development from an IDE on your local
device, such as [Visual
Studio Code Remote - SSH](https://code.visualstudio.com/docs/remote/ssh "https://code.visualstudio.com/docs/remote/ssh").

## Setting up a multi-user environment

To create and manage users for a multi-user environment (including mapping users
to IAM principals and integrating with Active Directory), see [User management on a SageMaker HyperPod Slurm cluster](sagemaker-hyperpod-slurm-user-management.md "sagemaker-hyperpod-slurm-user-management.md").
