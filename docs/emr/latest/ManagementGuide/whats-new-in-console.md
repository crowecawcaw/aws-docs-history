# Managing Amazon EMR clusters with the console

The console offers an updated interface that
provides you with an intuitive way to manage your Amazon EMR environment and gives you convenient
access to documentation, product information, and other resources.

## Console capabilities

The Amazon EMR console is available at the following URL:

- Console URL –
  [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr")

The following table lists the main Amazon EMR console components status.

| Amazon EMR console component                                  | Console |
| ------------------------------------------------------------- | ------- |
| EMR Studio                                                    | ✔      |
| Create and manage clusters                                    | ✔      |
| Block public access                                           | ✔      |
| Monitor Amazon CloudWatch Events                              | ✔      |
| Security configurations                                       | ✔      |
| Virtual clusters (Amazon EMR on EKS)                          | ✔      |
| View and manage your Amazon Virtual Private Cloud<br>subnets1 | ✔      |
| Notebooks2                                                    | ✔      |

1 In the console, you can view and manage your Amazon VPC
subnets within the **Networking** section when you create a cluster.

2 EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

## Summary of differences

This section outlines the capabilities of the Amazon EMR
console experience. These capabilities fall into the following categories:

- [Cluster compatibility in the console](#whats-new-cluster-compatibility "#whats-new-cluster-compatibility")
- [Creating clusters](#console-diff-cluster-create "#console-diff-cluster-create")
- [Viewing or editing cluster details](#console-diff-cluster-details "#console-diff-cluster-details")
- [Viewing and searching for clusters](#console-diff-cluster-list "#console-diff-cluster-list")
- [Differences when you work with security
  configurations](#console-diff-security "#console-diff-security")

### Cluster compatibility in the console

In some cases, a cluster that you created might not be
compatible with the console. The following list describes compatibility
requirements for the Amazon EMR console.

- The console supports clusters created in Amazon EMR releases 5.20.1 and
  later.
- You can clone clusters that use automatic scaling in the console, but
  you can only create new clusters if you want to manually scale them or use
  managed scaling.

To create and work with clusters of release 5.20.1 and earlier, you
can use the AWS Command Line Interface (AWS CLI) or the AWS SDK.

### Creating clusters

| Capability                                                                                                                               | Console                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Terminology: Amazon EMR cluster node types                                                                                               | Primary, core, task                                                                                                                                                                                                                                                           |
| [Amazon EMR supported<br>releases](../ReleaseGuide/emr-release-components.md "../ReleaseGuide/emr-release-components.md")1               | Amazon EMR release 5.20.1 and later                                                                                                                                                                                                                                           |
| [Quickly<br>launching a cluster](emr-launch-with-quick-options.md "emr-launch-with-quick-options.md")                                    | Use the **Create cluster\*<br>• button under the<br>**Summary\*<br>• panel. Your cluster name can't contain the characters <, >, $,                                                                                                                                           | , or ` (backtick). |
| [Configuring a Spot<br>provisioning timeout](emr-provisioning-timeout.md "emr-provisioning-timeout.md")                                  | Define a timeout period for provisioning<br>instances for each fleet in your cluster.                                                                                                                                                                                         |
| [Service roles and Amazon EC2<br>instance profile role](emr-iam-roles.md#emr-iam-roles-summary "emr-iam-roles.md#emr-iam-roles-summary") | The console doesn't create default roles; you must create<br>roles with the [IAM<br>Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") or select an already-created IAM<br>role                                                              |
| [Cluster<br>visibility](emr-managed-policy-fullaccess-v2.md "emr-managed-policy-fullaccess-v2.md")                                       | From within the Amazon EMR console, you can't make a<br>cluster visible to all a users; your IAM policy determines cluster<br>access                                                                                                                                          |
| [Networking<br>• configure<br>private subnets](emr-plan-vpc-subnet.md "emr-plan-vpc-subnet.md")                                          | You must configure Amazon S3 endpoints and NAT gateways<br>from their respective [Amazon S3](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/")<br>and [Amazon VPC](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/") consoles |
| [EMR File System consistent view (EMRFS CV)](../ReleaseGuide/emr-plan-consistent-view.md "../ReleaseGuide/emr-plan-consistent-view.md")  | With the release of Amazon S3 strong read-after-write consistency<br>on December 1, 2020, you don't need to use EMRFS CV with your<br>EMR clusters                                                                                                                            |
| [Debugging](emr-plan-debugging.md "emr-plan-debugging.md")                                                                               | You can debug jobs using the Application UI<br>interface on the cluster details page                                                                                                                                                                                          |

1 You can't create or edit clusters using releases
earlier than Amazon EMR 5.20.1 in the console, but any existing clusters created
using releases earlier than 5.20.1 will continue to work. To create and edit
clusters with Amazon EMR releases earlier than 5.20.1, use the API or CLI. You can view
all clusters using the console, but consoles created earlier than 5.20.1 might not be compatible newer features.

### Viewing and searching for clusters

The following table highlights how you can use the Amazon EMR console
to view view and search for clusters.

###### Note

Applying a data filter to the cluster list queries the entire database. But when you enter a text string into the
search box, the search only applies to the results that the list has loaded
client side.

| Capability              | Console                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Viewing cluster details | You can select the \*_Cluster ID_<br>• to view<br>exhaustive cluster details like configuration options,<br>persistent application UIs, and logs. |
| Searching for clusters  | Use a single search field to enter text search queries and to<br>create and apply data filters like "Status = Any active status".                 |
| Finding failed clusters | To search for failed clusters, apply the filter<br>**Status\*<br>• = **Terminated with<br>errors\*\*.                                             |

### Viewing or editing cluster details

| Capability                                                                                                                                                                                                               | Console                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Viewing the instances in your instance groups and instance<br>fleets, along with scaling, provisioning, resizing, and<br>termination options                                                                             | View instance options and details in the<br>**Instances\*<br>• tab. View termination options<br>in the **Properties\*<br>• tab.                                                           |
| Viewing app UIs, logs, and configurations<br>([Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/") UI, Spark History service, Apache Tez UI,<br>YARN timeline server) | View cluster configurations in the<br>**Configurations\*<br>• tab. Launch a live,<br>persistent, application UI to see the logs for an application<br>from the **Applications\*<br>• tab. |
| Exporting a cluster to CLI                                                                                                                                                                                               | Option available from cluster detail and list view Actions<br>menus as "View command for cloning cluster"                                                                                 |

### Differences when you work with security

configurations

| Capability                                                                                                                                                                                                                                                                            | Console                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Cloning security configurations                                                                                                                                                                                                                                                       | ✔                      |
| [Federated governance using Trino and Apache Ranger](https://aws.amazon.com/blogs/big-data/enable-federated-governance-using-trino-and-apache-ranger-on-amazon-emr/ "https://aws.amazon.com/blogs/big-data/enable-federated-governance-using-trino-and-apache-ranger-on-amazon-emr/") | ✔                      |
| [Using a runtime role<br>to submit work to a<br>cluster](emr-steps-runtime-roles.md "emr-steps-runtime-roles.md")1                                                                                                                                                                    | ✔                      |
| [Authorizing access to EMR<br>File System (EMRFS) data](emr-emrfs-iam-roles.md "emr-emrfs-iam-roles.md")                                                                                                                                                                              | Amazon S3 access points |
| AWS Lake Formation access controls                                                                                                                                                                                                                                                    | Runtime roles           |

1 To pass a role during step submission, your cluster
must use a security configuration with an IAM permissions policy attached so that
the a user can pass only the approved roles and your jobs can access Amazon EMR
resources. For more information, see [Runtime roles for Amazon EMR steps](emr-steps-runtime-roles.md "emr-steps-runtime-roles.md").
