

# Enabling split cost allocation data

**Note**  
Split cost allocation data is not available in Cost Explorer. It is available in legacy Cost and Usage Reports (CUR) and Cost and Usage Report 2.0 (CUR 2.0) with Data Exports.

It is a prerequisite to opt in to split cost allocation data through the Cost Management preferences.

**To opt in to split cost allocation data**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Management preferences**.

1. Under **General**, in the **Split cost allocation data** section, select one or more of the following:
   + **Amazon Elastic Container Service (Amazon ECS)** to opt in to Amazon ECS only.
   + **Amazon Elastic Kubernetes Service (Amazon EKS)** to opt in to Amazon EKS only. For Amazon EKS, choose between the following:
     + **Resource requests**: This allocates your Amazon EC2 by Kubernetes pod CPU and memory resources only. This will encourage application teams to only provision what they need.
     + **Amazon Managed Service for Prometheus**: This allocates your Amazon EC2 costs by the higher of Kubernetes pod CPU and memory resource requests and actual utilization. This ensures each application team pays for what they use. To learn more about setting up Amazon Managed Service for Prometheus, see [Setting up](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-setting-up.html) in the *Amazon Managed Service for Prometheus user guide*. 

       Prerequisite: You must enable all features in AWS Organizations. To learn more, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *Organizations user guide*.
     + **Amazon CloudWatch Container Insights**: This provides more granular cost visibility for your clusters running multiple application containers using shared EC2 instances, enabling better cost allocation for the shared costs of your EKS clusters.
   + **AWS Parallel Computing Service (PCS)** to opt in to AWS PCS only.
   + **Networking flexible cost allocation** to include allocated usage for NAT gateways, Amazon EC2 instances, and VPC peering connections with a networking flexible cost allocation policy. For more information, see [Split cost allocation data for networking](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html#split-cost-allocation-data-networking).
   + **Amazon S3** to include allocated storage and request charges for general purpose buckets. This option requires that you first enable Billing and Cost Management publishing on an S3 Storage Lens advanced tier dashboard. For more information, see [Split cost allocation data for Amazon S3](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html#split-cost-allocation-data-s3) and [Estimating Amazon S3 costs by prefix with S3 Storage Lens and AWS Cost and Usage Reports](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-cost-and-usage-reports.html) in the *Amazon S3 User Guide*.

**Note**  
Only the management account of an organization and standalone accounts can opt in through AWS Cost Management preferences. The management account's setting applies to every member account. Member accounts can view split cost allocation data for usage billed to their account in their own reports.
If you choose resource requests, only the pods configured with memory and CPU requests are used by split cost allocation data. Pods that haven't requested any usage won't see any split cost data.
If you choose Amazon Managed Service for Prometheus, you need to enable all features in AWS Organizations. For more information, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html). In addition, split cost allocation data creates a new service-linked role, which enables access to AWS services and resources used or managed by split cost allocation data.
For accelerated computing instances, only the Resource request option is supported. Neither Amazon Managed Service for Prometheus nor Amazon CloudWatch Container Insights are supported for these instances. When using accelerated computing instances, the system will default to Resource request to compute accelerator, CPU, and memory costs, even if other measurement options are enabled.
Only AWS PCS clusters that run Slurm 25.11 or later produce split cost allocation data.
When you opt in to AWS PCS, split cost allocation data prepares the granular cost data for only the current month and each month thereafter.
Split cost allocation data for AWS PCS is available in all AWS Regions where AWS PCS is available, except the AWS GovCloud (US) Regions. For the list of Regions, see [Endpoints and service quotas for AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/service-endpoints-quotas.html).

After you opt in, you can include split cost allocation data for shared resources when you create a report or edit an existing report.

**To include cost and usage data in your report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Legacy Pages**, choose **Cost and Usage Reports**.

1. Whether creating a new report or editing an existing report, in the **Specify report details** page, under **Report content**, select **Split cost allocation data**.

To identify the networking resource whose charge is allocated and the resource that generated the usage, or the Amazon S3 prefix and its bucket, also select **Include resource IDs** under **Report content**. For CUR 2.0, select **Split cost allocation data** and **Include resource IDs** when you create or edit the export. For more information, see [Creating exports](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-standard.html).

**Note**  
You can also use the AWS CUR API or the AWS Command Line Interface (CLI) to manage your split cost allocation data preferences.

Split cost allocation data applies to the management account and all member accounts. It covers Amazon ECS and Amazon EKS container objects, AWS PCS Slurm jobs, Amazon S3 prefixes and their buckets, and networking resources with a networking flexible cost allocation policy.

For containers, split cost allocation data scans for tasks and containers after you opt in. It ingests telemetry for your container workloads and prepares granular cost data for the current month.

For AWS PCS, split cost allocation data ingests the resource requests for your AWS PCS jobs and prepares granular cost data for the current month and each month thereafter.

**Note**  
It can take up to 24 hours for the data to be visible in AWS CUR.

For information about managing access to Billing and Cost Management console pages, see [﻿Overview of managing access permissions](https://docs.aws.amazon.com/cost-management/latest/userguide/control-access-billing.html).

For information regarding AWS Cost Management preferences and controlling access to Cost Explorer, see [﻿Controlling access to Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-access.html).