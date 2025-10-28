After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Creating a Managed kdb Insights cluster

You can either use the console or the [CreateKxCluster](../management-api/API_CreateKxCluster.md "../management-api/API_CreateKxCluster.md") API to
create a cluster. When you create a cluster from the console, you choose one of the following
cluster types available in FinSpace – [General
purpose](kdb-cluster-types.md#kdb-clusters-gp "kdb-cluster-types.md#kdb-clusters-gp"), [Tickerplant](kdb-cluster-types.md#kdb-clusters-tp "kdb-cluster-types.md#kdb-clusters-tp"), [HDB](kdb-cluster-types.md#kdb-clusters-hdb "kdb-cluster-types.md#kdb-clusters-hdb"), [RDB](kdb-cluster-types.md#kdb-clusters-rdb "kdb-cluster-types.md#kdb-clusters-rdb"), and
[Gateway](kdb-cluster-types.md#kdb-clusters-gw "kdb-cluster-types.md#kdb-clusters-gw"). The create cluster workflow includes a
step-wise wizard, where you will add various details based on the cluster type you choose. The
fields on each page can differ based on various selections throughout the cluster creation
process.

## Prerequisites

Before you proceed, complete the following prerequisites:

- If you want to run clusters on a scaling group, [create a scaling group](create-scaling-groups.md "create-scaling-groups.md").
- If you want to run a TP, GP, or RDB cluster on e scaling group [create a volume](create-volumes.md "create-volumes.md").
- If you want to run an HDB type cluster on a scaling group, [create a dataview](managing-kdb-dataviews.md#create-kdb-dataview "managing-kdb-dataviews.md#create-kdb-dataview").

######

Topics

- [Opening the cluster wizard](create-cluster-tab.md "create-cluster-tab.md")
- [Step 1: Add cluster details](create-cluster-step1.md "create-cluster-step1.md")
- [Step 2: Add code](create-cluster-step2.md "create-cluster-step2.md")
- [Step 3: Configure VPC settings](create-cluster-step3.md "create-cluster-step3.md")
- [Step 4: Configure data and storage](create-cluster-step4.md "create-cluster-step4.md")
- [Step 5: Review and create](create-cluster-step5.md "create-cluster-step5.md")
