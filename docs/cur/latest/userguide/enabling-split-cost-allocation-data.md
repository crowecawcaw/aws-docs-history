# Enabling split cost allocation

data

###### Note

Split cost allocation data is not available in Cost Explorer. It is available in legacy
Cost and Usage Reports (CUR) and Cost and Usage Report 2.0 (CUR 2.0) with Data Exports.

It is a prerequisite to opt in to split cost allocation data through the Cost
Management preferences.

###### To opt in to split cost allocation data

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management
   preferences**.
3. Under **General**, in the **Split cost allocation
   data** section, choose between the following:
   - **Amazon Elastic Container Service (Amazon ECS)** to opt in to Amazon ECS
     only.
   - **Amazon Elastic Kubernetes Service (Amazon EKS)** to opt in to Amazon EKS only.
     For Amazon EKS, choose between the following:
     - **Resource requests**: This allocates
       your Amazon EC2 by Kubernetes pod CPU and memory resources only.
       This will encourage application teams to only provision what
       they need.
     - **Amazon Managed Service for Prometheus**: This allocates your Amazon EC2
       costs by the higher of Kubernetes pod CPU and memory
       resource requests and actual utilization. This ensures each
       application team pays for what they use. To learn more about
       setting up Amazon Managed Service for Prometheus, see [Setting up](../../../prometheus/latest/userguide/AMP-setting-up.md "../../../prometheus/latest/userguide/AMP-setting-up.md") in the _Amazon Managed Service for Prometheus user
       guide_.

     Prerequisite: You must enable all features in AWS Organizations. To
     learn more, see [Enabling all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in
     the _Organizations user guide_.
     - **Amazon CloudWatch Container Insights**: This
       provides more granular cost visibility for your clusters
       running multiple application containers using shared EC2
       instances, enabling better cost allocation for the shared
       costs of your EKS clusters.

###### Note

- Only regular and payer accounts have access to the AWS Cost Management preferences and can
  opt in to split cost allocation data. Once opted in, member accounts can view
  the data in the Cost and Usage Reports.
- If you choose resource requests, only the pods configured with memory and CPU requests are
  used by split cost allocation data. Pods that haven't requested any
  usage won't see any split cost data.
- If you choose Amazon Managed Service for Prometheus, you need to enable all
  features in AWS Organizations. For more information, see [Enabling all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md"). In addition, split cost
  allocation data creates a new service-linked role, which enables access to AWS
  services and resources used or managed by split cost allocation data.
- For accelerated computing instances, only the Resource request option
  is supported. Neither Amazon Managed Service for Prometheus nor Amazon CloudWatch Container Insights
  are supported for these instances. When using accelerated computing
  instances, the system will default to Resource request to compute
  accelerator, CPU, and memory costs, even if other measurement options
  are enabled.
  Once you’ve opted in, you can choose to have cost and usage data for
  container-level resources included in your report during step one of report creation
  or later by editing the report details.

###### To include cost and usage data in your report

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy
   Pages**, choose **Cost and Usage Reports**.
3. Whether creating a new report or editing an existing report, in the
   **Specify report details** page, under **Report
   content**, select **Split cost allocation
   data**.

###### Note

You can also use the AWS CUR API or the AWS Command Line Interface (CLI) to manage your split
cost allocation data preferences.

Split cost allocation data enables cost visibility for all Amazon ECS and Amazon EKS container objects
across your entire consolidated billing family (payer and linked accounts). Once
activated, split cost allocation data automatically scans for tasks and containers.
It ingests the telemetry usage data for your container workloads and prepares the
granular cost data for the current month.

###### Note

It can take up to 24 hours for the data to be visible in AWS CUR.

For information about managing access to Billing and Cost Management console pages, see [﻿Overview of managing access permissions](../../../cost-management/latest/userguide/control-access-billing.md "../../../cost-management/latest/userguide/control-access-billing.md").

For information regarding AWS Cost Management preferences and controlling access to Cost Explorer, see
[﻿Controlling access to Cost Explorer](../../../cost-management/latest/userguide/ce-access.md "../../../cost-management/latest/userguide/ce-access.md").
