

# Multi-team environments

In a multi-team environment, several teams share a single Amazon Managed Workflows for Apache Airflow environment. Each team has its own DAG folder in Amazon S3, and IAM Identity Center groups control which teams a user can access. Amazon MWAA multi-team environments are based on the Apache Airflow multi-team feature. For more information, see [Multi-Team](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/multi-team.html) on the Apache Airflow website.

**Important**  
Amazon MWAA multi-team support is based on the Apache Airflow multi-team feature. This Apache Airflow feature is experimental and in preview as of Apache Airflow version 3.3.1. The feature is not complete, and its behavior and APIs can change in breaking ways, or be removed, between releases without notice. We recommend that you use multi-team environments with caution and that you don't rely on them for production-critical workloads. For more information, see [Experimental features](https://airflow.apache.org/docs/apache-airflow/stable/installation/supported-versions.html#experimental-features) on the Apache Airflow website.

**Regional availability**  
Amazon MWAA is gradually releasing IAM Identity Center integration and multi-team environments to AWS Regions. If these features aren't available in your Region yet, the Amazon MWAA console doesn't show the **Identity Center configuration** and **Teams** settings, and you can't configure teams from the console.

**Contents**
+ [Prerequisites](#multi-team-prerequisites)
+ [Key concepts](#multi-team-concepts)
  + [Teams](#multi-team-concepts-teams)
  + [Global and team DAG folders](#multi-team-concepts-dag-folders)
  + [DAG visibility](#multi-team-concepts-dag-visibility)
  + [Team isolation and the `airflow:TeamNames` condition key](#multi-team-concepts-access-control)
  + [Security considerations for DAG authors](#multi-team-concepts-security)
+ [Choosing a multi-team environment or separate environments](#multi-team-choosing)
+ [Limitations](#multi-team-limitations)
+ [Next steps](#multi-team-next-steps)

## Prerequisites
<a name="multi-team-prerequisites"></a>
+ The environment runs Apache Airflow version 3.3.1 or later.
+ IAM Identity Center integration is enabled on the environment. For more information, see [Using IAM Identity Center with Amazon Managed Workflows for Apache Airflow](identity-center-integration.md).
+ Each team has an IAM Identity Center group whose display name exactly matches the team name. For example, a team named `data-engineering` needs an IAM Identity Center group with the display name `data-engineering`. Matching is case-sensitive, so a team named `data-engineering` doesn't match a group named `Data-Engineering`.

## Key concepts
<a name="multi-team-concepts"></a>

The following concepts describe how teams, DAG folders, and access control work together in a multi-team environment.

### Teams
<a name="multi-team-concepts-teams"></a>

A *team* is a named group with its own DAG folder in Amazon S3. You can configure up to 20 teams per environment. Team names must meet the following requirements:
+ Between 3 and 50 characters long.
+ Starts with a letter or number.
+ Contains only letters (`a-z`, `A-Z`), numbers (`0-9`), hyphens (`-`), and underscores (`_`).
+ Unique within the environment.

Each team maps to the IAM Identity Center group with the same display name. When a user signs in, Amazon MWAA uses the user's IAM Identity Center group memberships to determine which teams they belong to. If no IAM Identity Center group matches a team name, the team has no members, and no users can access it.

### Global and team DAG folders
<a name="multi-team-concepts-dag-folders"></a>

A multi-team environment has two kinds of DAG folders:
+ **Global DAG folder** – The DAG folder that you specify when you create the environment. All users can see and run the DAGs in this folder. Put DAGs that several teams need here.
+ **Team DAG folders** – Each team has its own folder in Amazon S3. Only members of the team can see and run the DAGs in it. A team folder can be in the environment's bucket or in a different bucket. If you use a different bucket, the environment's execution role must have permission to read from it. For more information, see [Amazon MWAA execution role](mwaa-create-role.md).

You configure plugins and the `requirements.txt` file at the environment level, and they apply to all teams.

DAG folders can't overlap. A team folder can't be inside the global folder or another team's folder, and the global folder can't be inside a team folder. Amazon MWAA compares folder paths as Amazon S3 prefixes, so the trailing slash matters:
+ `s3://amzn-s3-demo-bucket/dags/` and `s3://amzn-s3-demo-bucket/dags/team-a/` overlap, because the first path is a prefix of the second.
+ `s3://amzn-s3-demo-bucket/dags/` and `s3://amzn-s3-demo-bucket/dags-team-a/` don't overlap.
+ `s3://amzn-s3-demo-bucket/teams/team-a/` and `s3://amzn-s3-demo-bucket/teams/team-b/` don't overlap.

If folders overlap, the Amazon MWAA console shows a validation error, and the API rejects the request.

### DAG visibility
<a name="multi-team-concepts-dag-visibility"></a>

When you sign in to the Apache Airflow UI in a multi-team environment, you see the DAGs in the global DAG folder and the DAGs of the teams you belong to. You can't see or access the DAGs of other teams.

### Team isolation and the `airflow:TeamNames` condition key
<a name="multi-team-concepts-access-control"></a>

How you control access to DAGs and other Apache Airflow resources depends on whether the environment has teams. Don't confuse the `airflow:TeamNames` IAM condition key with teams. The condition key is available in every environment that uses IAM Identity Center, but you don't need it to isolate teams.

Environments with teams  
When you add teams, Amazon MWAA turns on the Apache Airflow multi-team mode. Each DAG, connection, and variable either belongs to a team or is shared by all users. Apache Airflow isolates resources automatically based on this association. A user can access shared resources and the resources of the teams whose IAM Identity Center groups they belong to. You don't need to add `airflow:TeamNames` conditions to your policies for this isolation.  
The user's Permission Set policy must still allow access to the Apache Airflow resources. You can use `airflow:TeamNames` to narrow access further, but a policy can't give a user access to a team they don't belong to.

Environments without teams  
Apache Airflow multi-team mode is off, and resources don't belong to teams. The `airflow:TeamNames` condition key still contains the display names of the IAM Identity Center groups that the user belongs to. If you want finer-grained access control without adding teams, use `airflow:TeamNames` in your Permission Set policies. For example, combine it with the `airflow:ResourceType` and `airflow:ResourceId` condition keys so that only members of a specific IAM Identity Center group can access specific DAGs.

For how Apache Airflow associates resources with teams, see [Multi-Team](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/multi-team.html) on the Apache Airflow website. For policy examples, see [Using IAM Identity Center with Amazon Managed Workflows for Apache Airflow](identity-center-integration.md) and [Accessing an Amazon MWAA environment](access-policies.md).

### Security considerations for DAG authors
<a name="multi-team-concepts-security"></a>

Team isolation controls what users can see and do in the Apache Airflow UI and Apache Airflow REST API. It isn't a security boundary between the people who write DAG code. All teams in an environment share the following resources:
+ The environment's execution role
+ The DAG processor, schedulers, and workers that parse and run DAG code
+ The Apache Airflow metadata database
+ Plugins and Python dependencies

DAG code from every team runs with the same IAM permissions. DAG code that any team writes can access anything that the execution role can access, including other teams' DAG folders. It can also affect the DAGs, connections, variables, and data of other teams.

**Important**  
Write access to DAG folders is administrator-equivalent. Anyone who can write to the global DAG folder, to any team DAG folder, or to the plugins or `requirements.txt` file in Amazon S3 can run code in the environment with the execution role's permissions. Treat write access to these Amazon S3 prefixes as administrator access to the whole environment and to all of its teams, not only to one team.  
Grant write access to these prefixes only to people and pipelines that you trust with every team's resources. For example, use a CI/CD pipeline with a review step to publish DAGs instead of giving users direct write access to Amazon S3. If teams don't trust each other's DAG authors, use separate environments.

For more recommendations, see [Security best practices for multi-team environments](security-best-practices.md#security-bp-multi-team).

## Choosing a multi-team environment or separate environments
<a name="multi-team-choosing"></a>

A multi-team environment is a good fit when teams can share the same Apache Airflow version and environment configuration. It provides the following:
+ **Lower cost** – Teams share one environment's infrastructure instead of each paying for their own.
+ **Simpler management** – You configure environment settings, networking, and the Apache Airflow version once for all teams.
+ **Central governance** – The same security policies, monitoring, and compliance settings apply to all teams.
+ **DAG isolation** – Each team manages its own DAGs, and users can't see the DAGs of other teams in the Apache Airflow UI. This isolation doesn't protect teams from each other's DAG code. For more information, see [Security considerations for DAG authors](#multi-team-concepts-security).

Use separate Amazon MWAA environments when teams need any of the following:
+ Different Apache Airflow versions.
+ Different network configurations or VPCs.
+ Separate compute, such as their own workers and DAG processors.
+ Different plugins or Python dependencies.
+ Different compliance or security requirements.
+ Independent scaling.

## Limitations
<a name="multi-team-limitations"></a>

Multi-team environments have the following limitations:
+ **Experimental feature** – Multi-team support is based on an Apache Airflow experimental feature that is in preview and still evolving. Some functionality is incomplete, and behavior can change without notice in future releases. Use multi-team environments with caution.
+ **Shared compute** – All teams share the same DAG processor and workers. Teams are isolated only by DAG folder and access control. A team's workload can affect the performance of other teams.
+ **Shared execution role** – All teams use the environment's execution role. DAG code from any team runs with the same IAM permissions, and you can't assign a different execution role to a team.
+ **Shared metadata database** – All teams share the same SQL database instance containing Airflow metadata. A team's workload disproportionally loading the database can affect the performance of other teams.
+ **Shared plugins and Python dependencies** – All teams use the same plugins and the same `requirements.txt` file.
+ **IAM Identity Center dependency** – Teams require IAM Identity Center integration. After you enable IAM Identity Center integration on an environment, you can't disable it, even if you remove all teams.
+ **No renaming** – You can't rename a team. To change a team's name, remove the team and add a new one.
+ **Version downgrade** – You can't downgrade an environment that has teams to an Apache Airflow version earlier than 3.3.1. To downgrade, first remove all teams.
+ **Team quota** – An environment can have up to 20 teams. You can't increase this quota.

## Next steps
<a name="multi-team-next-steps"></a>

To add, change, or remove teams, see [Managing teams](managing-teams.md).