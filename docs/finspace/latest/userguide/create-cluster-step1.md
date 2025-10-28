After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Step 1: Add cluster details

Specify details for each of the following sections on **Add cluster details** page.

## Cluster details

1.  Choose from one of the following types of clusters that you want to
    add.

        * **(HDB) Historical Database**
        * **(RDB) Realtime Database**
        * **Gateway**
        * **General purpose**
        * **Tickerplant**

    For more information about cluster types, see [Managed kdb Insights clusters](finspace-managed-kdb-clusters.md "finspace-managed-kdb-clusters.md").

###### Note

    * Currently, you can only create dedicated HDB clusters and all cluster
     types that are running on a scaling group directly from the console. To
     create other types of clusters, you need to first create a [Support case](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/"), and
     then proceed with steps in this tutorial.
    * The parameters that are displayed on the **Step 5:
     Configure data and storage** page will change based on the
     cluster type and running mode that you select in this step.

2. Add a unique name and a brief description for your cluster.
3. For `Release label`, choose the package version to run
   in the cluster.
4. (Optional) Choose the IAM role that defines a set of permissions
   associated with this cluster. This is an execution role that will be
   associated with the cluster. You can use this role to control access
   to other clusters in your Managed kdb environment.

## Cluster running mode

1. Choose if you want to add this cluster as a dedicated cluster or as a part of scaling groups.
   - **Run on kdb scaling group** – Allows you to share a single set of compute with multiple clusters.
   - **Run as a dedicated cluster** – Allows you to run each process on its own compute hose.

2. If you choose **Run as a dedicated cluster**, you also need to provide the Availability Zones where you want to create a
   cluster.
   1. Choose **AZ mode** to specify the number of Availability Zones where you want to create a
      cluster. You can choose from one of the following options:
      - **Single** – Allows you to create a
        cluster in one Availability Zone that you select. If you choose
        this option, you must specify only one Availability Zone value
        and only one subnet in the next step. The subnet must reside in
        one of the three AZs that your kdb environment uses, and the
        Availability Zone must align with one of the three AZs.
      - **Multiple** – Allows you to create a
        cluster with nodes automatically allocated across all the
        Availability Zones that are used by your Managed kdb
        environment. This option provides resiliency for node or cache
        failures in a Single-AZ. If you choose this option, you must
        specify three subnets, one in each of the three AZs that your
        kdb environment uses.

   ###### Note

   For the **General purpose** and
   **Tickerplant** type cluster, you can only choose
   Single-AZ. 2. Choose the Availability Zone IDs that include the subnets you want
   to add.

## Scaling group details

###### Note

This section is only available when you choose to add cluster as a part of scaling groups.

Choose the name of the scaling group where you want to create this cluster. The
drop down shows the metadata for each scaling group along with their names to help you
decide which one to pick. If a scaling group is not available, choose **Create
kdb scaling group** to add a new one. For more information, see [Creating a Managed kdb scaling group](create-scaling-groups.md "create-scaling-groups.md").

## Node details

In this section, you can choose the capacity configuration for your clusters. The
fields in this section vary for dedicated and scaling group clusters.

Scaling group cluster
You can decide the memory and CPU usage that will be shared with the
instances for your scaling group clusters by providing the following
information.

1. Under **Node details**, for **Node
   count**, enter the number of instances in a cluster.

###### Note

For a **General purpose** and **Tickerplant** type cluster, the
node count is fixed at 1. 2. Enter the memory reservation and limits per node. Specifying the memory limit is optional. The memory limit should be equal to or greater than the memory reservation. 3. (Optional) Enter the number of vCPUs that you want to reserve for each node of this scaling group cluster.

Dedicated cluster
For a dedicated cluster you can provide an initial node count and choose
the capacity configuration from a pre-defined list of node types. For example,
the node type `kx.s.large` allows you to use two vCPUs and 12 GiB of
memory for your instance.

1. Under **Node details**, for **Initial node
   count**, enter the number of instances in a cluster.

###### Note

For a **General purpose** and **Tickerplant** type cluster, the
node count is fixed at 1. 2. For **Node type**, choose the memory and storage
capabilities for your cluster instance. You can choose from one of the
following options:

    * `kx.s.large` – The node type with a
     configuration of 12 GiB memory and 2 vCPUs.
    * `kx.s.xlarge` – The node type with a
     configuration of 27 GiB memory and 4 vCPUs.
    * `kx.s.2xlarge` – The node type with a
     configuration of 54 GiB memory and 8 vCPUs.
    * `kx.s.4xlarge` – The node type with a
     configuration of 108 GiB memory and 16 vCPUs.
    * `kx.s.8xlarge` – The node type with a
     configuration of 216 GiB memory and 32 vCPUs.
    * `kx.s.16xlarge` – The node type with a
     configuration of 432 GiB memory and 64 vCPUs.
    * `kx.s.32xlarge` – The node type with a
     configuration of 864 GiB memory and 128 vCPUs.

## Auto-scaling

###### Note

This section is only available when you add an HDB cluster type as a dedicated cluster.

Specify details to scale in or scale out the based on service utilization. For more information, see [Auto scaling](kdb-cluster-types.md#kdb-cluster-hdb-autoscaling "kdb-cluster-types.md#kdb-cluster-hdb-autoscaling").

1. Enter a minimum node count. Valid numbers: 1–5.
2. Enter a maximum node count. Valid numbers: 1–5.
3. Choose the metrics to auto scale your cluster. Currently, FinSpace only supports CPU
   utilization.
4. Enter the cooldown time before initiating another scaling event.

## Tags

1. (Optional) Add a new tag to assign to your kdb cluster. For more
   information, see [AWS tags](create-an-amazon-finspace-environment.md#aws-tags "create-an-amazon-finspace-environment.md#aws-tags").

###### Note

You can only add up to 50 tags to your cluster. 2. Choose **Next** for next step of the wizard.
