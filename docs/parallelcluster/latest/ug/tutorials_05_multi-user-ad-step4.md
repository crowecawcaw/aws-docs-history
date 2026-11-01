

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Connect to the cluster as a user
<a name="tutorials_05_multi-user-ad-step4"></a>

You can determine the status of the cluster with the following commands.

```
$ pcluster describe-cluster -n {{ad-cluster}} --region {{"region-id"}} --query "clusterStatus"
```

The output is as follows.

```
"CREATE_IN_PROGRESS" / "CREATE_COMPLETE"
```

When the status reaches `"CREATE_COMPLETE"`, log in with the created user name and password.

```
$ HEAD_NODE_IP=$(pcluster describe-cluster -n {{"ad-cluster"}} --region {{"region-id"}} --query headNode.publicIpAddress | xargs echo)
```

```
$ ssh {{user000}}@$HEAD_NODE_IP
```

You can log in without the password by providing the SSH key that was created for the new user at `/home/user000@HEAD_NODE_IP/.ssh/id_rsa`.

If the `ssh` command succeeded, you have successfully connected to the cluster as a user that's authenticated to use the Active Directory (AD).