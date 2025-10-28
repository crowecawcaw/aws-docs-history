# Setting up the SageMaker HyperPod

observability add-on

The following list describes the prerequisites for setting up the
observability add-on.

To have metrics for your Amazon SageMaker HyperPod (SageMaker HyperPod) cluster sent to a
Amazon Managed Service for Prometheus workspace and to optionally view them in Amazon Managed Grafana, first attach the
following managed policies and permissions to your console role.

- To use Amazon Managed Grafana, enable AWS IAM Identity Center (IAM Identity Center) in an AWS Region where
  Amazon Managed Grafana is available. For instructions, see [Getting
  started with IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the
  _AWS IAM Identity Center User Guide_. For a list of AWS Regions
  where Amazon Managed Grafana is available, see [Supported Regions](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md#AMG-supported-Regions "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md#AMG-supported-Regions") in the _Amazon Managed Grafana User
  Guide_.
- Create at least one user in IAM Identity Center.
- Ensure that the [Amazon EKS Pod Identity Agent](../../../eks/latest/userguide/workloads-add-ons-available-eks.md#add-ons-pod-id "../../../eks/latest/userguide/workloads-add-ons-available-eks.md#add-ons-pod-id") add-on is installed in your Amazon EKS
  cluster. The Amazon EKS Pod Identity Agent add-on makes it possible for the
  SageMaker HyperPod observability add-on to get the credentials to interact
  with Amazon Managed Service for Prometheus and CloudWatch Logs. To check whether your Amazon EKS cluster has the
  add-on, go to the Amazon EKS console, and check your cluster's
  **Add-ons** tab. For information about how to
  install the add-on if it's not installed, see [Create add-on (AWS Management Console)](../../../eks/latest/userguide/creating-an-add-on.md#_create_add_on_console "../../../eks/latest/userguide/creating-an-add-on.md#_create_add_on_console") in the _Amazon EKS User Guide_.
- Ensure that you have at least one node in your SageMaker HyperPod cluster
  before installing SageMaker HyperPod observability add-on. The smallest Amazon EC2
  instance type that works in this case is `4xlarge`. This
  minimum node size requirement ensures that the node can accommodate all
  the pods that the SageMaker HyperPod observability add-on creates alongside
  any other already running pods on the cluster.
- Add the following policies and permissions to your role.

      + [AWS
       managed policy: AmazonSageMakerHyperPodObservabilityAdminAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md "security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md")
      + [AWS managed policy:
       AWSGrafanaWorkspacePermissionManagementV2](../../../grafana/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2 "../../../grafana/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2")
      + [AWS managed policy:
       AmazonSageMakerFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md")
      + Additional permissions to set up required IAM roles for
       Amazon Managed Grafana and Amazon Elastic Kubernetes Service add-on access:



      ```
      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Sid": "CreateRoleAccess",
                  "Effect": "Allow",
                  "Action": [
                      "iam:CreateRole",
                      "iam:CreatePolicy",
                      "iam:AttachRolePolicy",
                      "iam:ListRoles"
                  ],
                  "Resource": [
                      "arn:aws:iam::*:role/service-role/AmazonSageMakerHyperPodObservabilityGrafanaAccess*",
                      "arn:aws:iam::*:role/service-role/AmazonSageMakerHyperPodObservabilityAddonAccess*",
                      "arn:aws:iam::*:policy/service-role/HyperPodObservabilityAddonPolicy*",
                      "arn:aws:iam::*:policy/service-role/HyperPodObservabilityGrafanaPolicy*"
                  ]
              }
          ]
      }
      ```
      + Additional permissions needed to manage IAM Identity Center users for
       Amazon Managed Grafana:



      ```
      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Sid": "SSOAccess",
                  "Effect": "Allow",
                  "Action": [
                      "sso:ListProfileAssociations",
                      "sso-directory:SearchUsers",
                      "sso-directory:SearchGroups",
                      "sso:AssociateProfile",
                      "sso:DisassociateProfile"
                  ],
                  "Resource": [
                      "*"
                  ]
              }
          ]
      }
      ```

  After you ensure that you have met the above prerequisites, you can install
  the observability add-on.

###### To quickly install the observability add-on

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Go to your cluster's details page.
3. On the **Dashboard** tab, locate the add-on named
   **HyperPod Monitoring &
   Observability**, and choose **Quick
   install**.

###### To do a custom-install of the observability add-on

1. Go to your cluster's details page.
2. On the **Dashboard** tab, locate the add-on named
   **HyperPod Monitoring &
   Observability**, and choose **Custom
   install**.
3. Specify the metrics categories that you want to see. For more
   information about these metrics categories, see [SageMaker HyperPod cluster
   metrics](hyperpod-observability-cluster-metrics.md "hyperpod-observability-cluster-metrics.md").
4. Specify whether you want to enable Amazon CloudWatch Logs.
5. Specify whether you want the service to create a new Amazon Managed Service for Prometheus
   workspace.
6. To be able to view the metrics in Amazon Managed Grafana dashboards, check the box
   labeled **Use an Amazon Managed Grafana workspace**. You can specify
   your own workspace or let the service create a new one for you.

###### Note

Amazon Managed Grafana isn't available in all AWS Regions in which Amazon Managed Service for Prometheus
is available. However, you can set up a Grafana workspace in any
AWS Region and configure it to get metrics data from a Prometheus
workspace that resides in a different AWS Region. For information,
see [Use
AWS data source configuration to add Amazon Managed Service for Prometheus as a data
source](../../../grafana/latest/userguide/AMP-adding-AWS-config.md "../../../grafana/latest/userguide/AMP-adding-AWS-config.md") and [Connect to Amazon Managed Service for Prometheus and
open-source Prometheus data sources](../../../grafana/latest/userguide/prometheus-data-source.md "../../../grafana/latest/userguide/prometheus-data-source.md").
