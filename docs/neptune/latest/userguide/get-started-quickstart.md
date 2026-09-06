

# Quick start using AWS CloudShell
<a name="get-started-quickstart"></a>

This guide helps you get started quickly by using [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) to connect to and query your Neptune cluster directly from the AWS Management Console.

**Time to complete:** Approximately 2 minutes

**Cost:** CloudShell is available at no additional charge. Creating a Neptune cluster incurs charges. For pricing details, see [Amazon Neptune pricing](https://aws.amazon.com/neptune/pricing/).

## Prerequisites
<a name="get-started-quickstart-prereqs"></a>
+ An AWS account. If you don't have one, see [Setting up your AWS account](https://docs.aws.amazon.com/SetUp/).
+ A Neptune cluster with status **Available**. If you don't already have one, see [Launching a Neptune DB cluster using the AWS Management Console](manage-console-launch-console.md) to create one.

## Step 1: Connect to your Neptune cluster
<a name="get-started-quickstart-connect"></a>

Connect to your Neptune cluster using [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html). CloudShell automatically provisions a shell environment connected to your cluster's VPC. You don't need to configure security groups or set up notebooks to interact with the database.

**To connect to your cluster**

1. In the Neptune console, under **Clusters**, locate the cluster you created.

1. Select the check box next to your cluster.

1. Choose **Connect to cluster**.
**Note**  
This button becomes active after you select the check box next to your cluster and the cluster status shows as **Available**.

   The CloudShell **Run command** screen appears.

1. Choose **Run** to connect to the cluster. Provisioning the VPC environment takes a few seconds.

After you connect, the `graphsh` console appears, providing an interactive shell for running graph queries.

## Step 2: Insert and query data
<a name="get-started-quickstart-query"></a>

Now that you are connected to your cluster, run a few queries to get familiar with Amazon Neptune. The following examples use openCypher, one of the query languages supported by Neptune.

**To insert nodes and relationships**  
Run the following query to create two person nodes and a relationship:

```
CREATE (a:Person {name: 'Alice', age: 30}), (b:Person {name: 'Bob', age: 40}), (a)-[:KNOWS]->(b)
```

The output looks similar to the following:

```
╭────────╮
│ result │
├────────┤
│ []     │
╰────────╯
```

**To find nodes**  
Run the following query to return all person names in alphabetical order:

```
MATCH (p:Person) RETURN p.name AS name ORDER BY name
```

The output looks similar to the following:

```
╭───────╮
│ name  │
├───────┤
│ Alice │
│ Bob   │
╰───────╯
```

## Next steps
<a name="get-started-quickstart-next"></a>

You have completed this quick start. To continue learning, explore the following features:
+ [Overview of Amazon Neptune features](feature-overview.md) – Learn about the key capabilities of Amazon Neptune.
+ [Amazon Neptune Serverless](neptune-serverless.md) – Automatically scale your cluster capacity based on workload.
+ [Managing Your Amazon Neptune Database](manage-console.md) – Manage your clusters, instances, and configurations.

To avoid ongoing charges, delete the Neptune cluster if you created it only for this quick start. For instructions, see [Managing Your Amazon Neptune Database](manage-console.md).