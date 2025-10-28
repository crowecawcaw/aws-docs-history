# Explore the cluster environment in AWS PCS

After you have logged into the cluster, you can run shell commands. For instance, you can
change users, work with data on shared filesystems, and interact with Slurm.

## Change user

If you have logged in to the cluster using Session Manager, you may be connected as
`ssm-user`. This is an special user that is created for Session Manager. Switch to
the default user on Amazon Linux 2 using the following command. You will not need to do this if
you connected using SSH.

```
sudo su - ec2-user
```

## Work with shared file systems

You can confirm that the EFS filesystem and FSx for Lustre file systems are available with
the command `df -h`. Output on your cluster should resemble the following:

```
[ec2-user@ip-10-3-6-103 ~]$ df -h
Filesystem                 Size  Used Avail Use% Mounted on
devtmpfs                   3.8G     0  3.8G   0% /dev
tmpfs                      3.9G     0  3.9G   0% /dev/shm
tmpfs                      3.9G  556K  3.9G   1% /run
tmpfs                      3.9G     0  3.9G   0% /sys/fs/cgroup
/dev/nvme0n1p1              24G   18G  6.6G  73% /
127.0.0.1:/                8.0E     0  8.0E   0% /home
10.3.132.79@tcp:/zlshxbev  1.2T  7.5M  1.2T   1% /shared
tmpfs                      780M     0  780M   0% /run/user/0
tmpfs                      780M     0  780M   0% /run/user/1000
```

The `/home` filesystem mounts 127.0.0.1 and has a very large capacity. This is
the EFS file system that you created earlier in the tutorial. Any files written here will
be available under `/home` on all nodes in the cluster.

The `/shared` filesystem mounts a private IP and has a capacity of 1.2 TB. This
is the FSx for Lustre file system that you created earlier in the tutorial. Any files
written here will be available under `/shared` on all nodes in the cluster.

## Interact with Slurm

###### Topics

- [List queues and nodes](getting-started_explore.md#getting-started_explore_slurm_queues "getting-started_explore.md#getting-started_explore_slurm_queues")
- [Show jobs](getting-started_explore.md#getting-started_explore_slurm_jobs "getting-started_explore.md#getting-started_explore_slurm_jobs")

### List queues and nodes

You can list the queues and the nodes they are associated with using `sinfo`.
Output from your cluster should resemble the following:

```
[ec2-user@ip-10-3-6-103 ~]$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
demo         up   infinite      4  idle~ compute-1-[1-4]
[ec2-user@ip-10-3-6-103 ~]$
```

Note the partition named `demo`. Its status is `up` and it has a
maximum of 4 nodes. It is associated with nodes in the `compute-1` node group. If you
edit the compute node group and increase the maximum number of instances to 8, the number of
nodes would read `8` and the node list would read `compute-1-[1-8]`. If
you created a second compute node group named `test` with 4 nodes, and added it to
the `demo` queue, those nodes would show up in the node list as well.

### Show jobs

You can list all jobs, in any state, on the system with `squeue`. Output from
your cluster should resemble the following:

```
[ec2-user@ip-10-3-6-103 ~]$ squeue
JOBID PARTITION NAME USER ST TIME NODES NODELIST(REASON)
```

Try running `squeue` again later, when you have a Slurm job pending or running.
