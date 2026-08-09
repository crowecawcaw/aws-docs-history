# Create a cluster in AWS PCS

In AWS PCS, a cluster is a persistent resource for managing resources and running workloads.
You create a cluster for a specific scheduler (AWS PCS currently supports Slurm) in a subnet of a
new or existing VPC. The cluster accepts and schedules jobs, and also launches the compute nodes
(EC2 instances) that process those jobs.

###### To create your cluster

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters") and
   choose **Create cluster**.
2. In the **Cluster details** section, enter the following fields:

   - **Cluster name** – Enter `get-started`
   - **Scheduler** – Select **Slurm Version 25.11**
   - **Controller size** – Select **Small**. The
     controller size sets the capacity of the managed Slurm controller; **Small**
     is enough for a demonstration cluster.

3. In the **Networking** section, select values for the following fields:

   - **VPC** – Choose the VPC named
     `hpc-networking:Large-Scale-HPC`
   - **Subnet** – Select the subnet where the name starts with
     `hpc-networking:PrivateSubnetA`. The controller runs in a private subnet
     because it does not need to be reachable from the internet.
   - **Security groups** – Select the cluster security group named
     `cluster-getstarted-sg`

4. Choose **Create cluster**.

###### Note

The **Status** field shows **Creating** while the cluster is being
provisioned. Cluster creation can take several minutes.
