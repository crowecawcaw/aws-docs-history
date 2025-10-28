# Use AMS SSP to provision Amazon EMR in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon EMR capabilities directly in your AMS managed account. Amazon EMR is the industry-leading cloud big data platform for processing vast amounts of data using open
source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto. With
Amazon EMR you can run Petabyte-scale analysis at less than half of the cost of traditional on-premises solutions
and over 3x faster than standard Apache Spark. For short-running jobs, you can spin up and spin down clusters
and pay per second for the instances used. For long-running workloads, you can create highly available
clusters that automatically scale to meet demand.

You can create one or more instances of the Amazon EMR clusters in either AMS multi-account landing zone or
single-account landing zone accounts to support both transient and persistent Amazon EMR clusters. You can also
enable Kerberos authentication to enable authenticate users from on-premises Active
Directory domain.

You can leverage multiple data stores with the Amazon EMR clusters to support use-case
specific Hadoop tools and libraries. The Amazon EMR clusters can be created using OnDemand or
Spot instances and configure autoscaling to manage capacity and reduce the cost.

The cluster log files can be archived to an Amazon S3 bucket for logging and debugging. You can also access
the web interfaces hosted in the Amazon EMR cluster to support hadoop administration requirements or note book
experiences for customers.

To learn more, see [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/").

## Amazon EMR in AWS Managed Services FAQ

**Q: How do I request access to Amazon EMR in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM roles to your account:

- `customer_emr_cluster_instance_profile`
- `customer_emr_cluster_autoscaling_role`
- `customer_emr_console_role`
- `customer_emr_cluster_service_role`

After it's provisioned in your account, you must onboard the customer_emr_console_role in your federation solution.

**Q: What are the restrictions to using Amazon EMR in my AMS account?**

While creating Amazon EMR on an EC2 cluster from the AWS console, we advise you to use the **Create Cluster – Advanced** option. Amazon EMR clusters
must be created by adding the tag with the Key **"for-use-with-amazon-emr-managed-policies"** with Value **"true"**. Select the
following configurations in the **Security** options:

- Select custom roles for your cluster:
  - EMR Role : customer_emr_cluster_service_role
  - EC2 Instance Profile : customer_emr_cluster_instance_profile
  - Auto Scaling Role : customer_emr_cluster_autoscaling_role

- EC2 Security groups:
  - Master : ams-emr-master-security-group
  - Core & Task : ams-emr-worker-security-group
  - Service Access : ams-emr-serviceaccess-security-group

**Q: What are the prerequisites or dependencies to using Amazon EMR in my AMS account?**

AMS creates default security groups for the Amazon EMR master, worker, and services nodes.

The launch templates and security groups to be used with Amazon EMR clusters must have the tag key **"for-use-with-amazon-emr-managed-policies"** with
value **"true"**.

The default Amazon EMR cluster instance profile enables access to the resources such as s3 buckets and dynamodb tables with their names containing "emr".
You can request additional IAM policies to use any additional resources to be used with Amazon EMR. The following resource ARN's can be used with Amazon EMR
jobs using the **customer_emr_cluster_instance_profile**:

- arn:aws:dynamodb:\*:\*:table/\*emr\*
- arn:aws:kinesis:\*:\*:stream/\*emr\*
- arn:aws:sns:\*:\*:\*emr\*arn:aws:sqs:\*:\*:\*emr\*
- arn:aws:sqs:\*:\*:\*emr\*
- arn:aws:sqs:\*:\*:AWS-ElasticMapReduce-\*
- arn:aws:sdb:\*:\*:domain:\*emr\*
- arn:aws:s3:::\*emr\*

If kerberos authentication is required for the Amazon EMR cluster:

- Provide the realm name to be used for each kerberized Amazon EMR cluster
  and the on-premise Active Directory IP addresses.
- Infrastructure requirements:

**Multi-Account Landing Zone (MALZ)**: Submit an RFC to create a new Managed application account or a new
VPC in an existing application account.

**Single-Account Landing Zone (SALZ)**: Submit an RFC to create a new subnet in your VPC.

- Configure the incoming trust for the cluster’s realm on the on-premise Active Directory.
- Submit an RFC to configure DNS zones for the realm in the Managed AD.
- Realm configuration:

**MALZ**: Submit a Management | Other | Other | Update (ct-0xdawir96cy7k) RFC to update the VPC DHCP option set to
use the realm name for domain name suffix.

**SALZ**: Submit a Management | Other | Other | Update (ct-0xdawir96cy7k) RFC to generate a new Amazon EMR AMI to use
the specific realm for domain name suffix.

To deploy Amazon EMR studio, the role `customer_emr_cluster_service_role` has a prerequisite for an Amazon Simple Storage Service bucket. To create the bucket, use the automated CT `ct-1a68ck03fn98r` (Deployment | Advanced stack components | S3 storage | Create). When you use this automated CT to create an Amazon S3 bucket for Amazon EMR, the bucket name must begin with the prefix `customer-emr-*`. And, you must create the bucket in the same AWS Region as the Amazon EMR cluster.
