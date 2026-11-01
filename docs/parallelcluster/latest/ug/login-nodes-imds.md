

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Imds properties for login nodes
<a name="login-nodes-imds"></a>

Access to the login node's IMDS (and the instance profile credentials) is restricted to root user, cluster administrative user (`pc-cluster-admin` by default) and operating system specific default user (`ec2-user` on Amazon Linux 2023 and Red Hat, and `ubuntu` on Ubuntu 22.04 and Ubuntu 24.04) 

To restrict IMDS access, AWS ParallelCluster manages a chain of `iptables`. 

**Note**  
Any customization of `iptables` or `ip6tables` rules can interfere with the mechanism used to restrict IMDS access on the login node.See also [`Imds property setting`](HeadNode-v3.md#HeadNode-v3-Imds). 