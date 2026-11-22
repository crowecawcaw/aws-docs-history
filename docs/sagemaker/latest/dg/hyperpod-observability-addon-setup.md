

# Setting up the SageMaker HyperPod observability add-on

The following list describes the prerequisites for setting up the observability add-on.

To have metrics for your Amazon SageMaker HyperPod (SageMaker HyperPod) cluster sent to Amazon CloudWatch or to an Amazon Managed Service for Prometheus workspace and to optionally view them in Amazon Managed Grafana, first attach the following managed policies and permissions to your console role.
+ To use Amazon Managed Grafana, enable AWS IAM Identity Center (IAM Identity Center) in an AWS Region where Amazon Managed Grafana is available. For instructions, see [Getting started with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the *AWS IAM Identity Center User Guide*. For a list of AWS Regions where Amazon Managed Grafana is available, see [Supported Regions](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html#AMG-supported-Regions) in the *Amazon Managed Grafana User Guide*.
+ Create at least one user in IAM Identity Center.
+ Ensure that the [Amazon EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/workloads-add-ons-available-eks.html#add-ons-pod-id) add-on is installed in your Amazon EKS cluster. The Amazon EKS Pod Identity Agent add-on makes it possible for the SageMaker HyperPod observability add-on to get the credentials to interact with CloudWatch, Amazon Managed Service for Prometheus, and CloudWatch Logs. To check whether your Amazon EKS cluster has the add-on, go to the Amazon EKS console, and check your cluster's **Add-ons** tab. For information about how to install the add-on if it's not installed, see [Create add-on (AWS Management Console)](https://docs.aws.amazon.com/eks/latest/userguide/creating-an-add-on.html#_create_add_on_console) in the *Amazon EKS User Guide*.

  When you create a SageMaker HyperPod cluster in the SageMaker AI console and choose to create a new Amazon EKS cluster, the console installs the Amazon EKS Pod Identity Agent add-on in the new Amazon EKS cluster. The console doesn't install the add-on or check for it when you install the observability add-on on an existing cluster. To check for the add-on with the AWS CLI, run the following command. Replace {{my-eks-cluster}} with the name of your Amazon EKS cluster. If the add-on isn't installed, the command returns a `ResourceNotFoundException` error.

  ```
  aws eks describe-addon \
      --cluster-name {{my-eks-cluster}} \
      --addon-name eks-pod-identity-agent
  ```

  To install the add-on with the AWS CLI, run the following command.

  ```
  aws eks create-addon \
      --cluster-name {{my-eks-cluster}} \
      --addon-name eks-pod-identity-agent
  ```
**Note**  
The Amazon EKS Pod Identity Agent is required for standard instance groups. For Restricted Instance Groups (RIG), the Pod Identity Agent is not available due to network isolation constraints. The cluster's instance group execution IAM role is used to interact with Amazon Managed Service for Prometheus. For information about how to configure that role, see [Additional prerequisites for Restricted Instance Groups](#hyperpod-observability-addon-rig-prerequisites).
+ Ensure that you have at least one node in your SageMaker HyperPod cluster before installing SageMaker HyperPod observability add-on. The smallest Amazon EC2 instance type that works in this case is `4xlarge`. This minimum node size requirement ensures that the node can accommodate all the pods that the SageMaker HyperPod observability add-on creates alongside any other already running pods on the cluster.
+ Add the following policies and permissions to your role.
  + [AWS managed policy: AmazonSageMakerHyperPodObservabilityAdminAccess](security-iam-awsmanpol-AmazonSageMakerHyperPodObservabilityAdminAccess.md)
  + [AWS managed policy: AWSGrafanaWorkspacePermissionManagementV2](https://docs.aws.amazon.com/grafana/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2)
  + [AWS managed policy: AmazonSageMakerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html)
  + Additional permissions to set up required IAM roles for Amazon Managed Grafana and Amazon Elastic Kubernetes Service add-on access:

------
#### [ JSON ]

****  

    ```json
    {
        "Version":"2012-10-17",		 	 	 
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

------
  + Additional permissions needed to manage IAM Identity Center users for Amazon Managed Grafana:

------
#### [ JSON ]

****  

    ```json
    {
        "Version":"2012-10-17",		 	 	 
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

------

## Additional prerequisites for Restricted Instance Groups
<a name="hyperpod-observability-addon-rig-prerequisites"></a>

If your cluster contains Restricted Instance Groups, the instance group execution role must have permissions to write metrics to Amazon Managed Service for Prometheus. To send metrics to Amazon CloudWatch, the execution role needs `cloudwatch:PutMetricData`, which the AWS managed policy `AmazonSageMakerClusterInstanceRolePolicy` allows. When you use **Quick setup** to create your cluster with observability enabled, these permissions are added to the execution role automatically.

If you are using **Custom setup** or adding observability to an existing RIG cluster, ensure that the execution role for each Restricted Instance Group has the following permissions:

```json
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "PrometheusAccess",
            "Effect": "Allow",
            "Action": "aps:RemoteWrite",
            "Resource": "arn:aws:aps:{{us-east-1}}:{{account_id}}:workspace/{{workspace-ID}}"
        }
    ]
}
```

Replace {{us-east-1}}, {{account\_id}}, and {{workspace-ID}} with your AWS Region, account ID, and Amazon Managed Service for Prometheus workspace ID.

After you ensure that you have met the above prerequisites, you can install the observability add-on.

**To quickly install the observability add-on**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Go to your cluster's details page.

1. On the **Dashboard** tab, locate the add-on named **HyperPod Monitoring & Observability**, and choose **Quick install**.

**Quick install** sends metrics to Amazon CloudWatch when the newest version of the add-on supports CloudWatch, and installs that version. Otherwise, or if the console can't read the configuration schema of the add-on, **Quick install** creates an Amazon Managed Service for Prometheus workspace and sends the metrics to it.

**To do a custom-install of the observability add-on**

1. Go to your cluster's details page.

1. On the **Dashboard** tab, locate the add-on named **HyperPod Monitoring & Observability**, and choose **Custom install**.

1. Specify the metrics categories that you want to see. For more information about these metrics categories, see [SageMaker HyperPod cluster metrics](hyperpod-observability-cluster-metrics.md).

1. Specify whether you want to enable Amazon CloudWatch Logs.

1. Under **Metric store**, choose where the add-on sends metrics:
   + **Amazon CloudWatch**—The add-on sends metrics to Amazon CloudWatch. This is the default for a new installation.
   + **Amazon Managed Service for Prometheus**—The add-on sends metrics to an Amazon Managed Service for Prometheus workspace. Specify whether you want the service to create a new Amazon Managed Service for Prometheus workspace.

   The console shows the metric store option when the newest add-on version for your cluster supports it, and it installs that version.

1. To be able to view the metrics in Amazon Managed Grafana dashboards, check the box labeled **Use an Amazon Managed Grafana workspace**. You can specify your own workspace or let the service create a new one for you. 
**Note**  
Amazon Managed Grafana isn't available in all AWS Regions in which Amazon Managed Service for Prometheus is available. However, you can set up a Grafana workspace in any AWS Region and configure it to get metrics data from a Prometheus workspace that resides in a different AWS Region. For information, see [Use AWS data source configuration to add Amazon Managed Service for Prometheus as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/AMP-adding-AWS-config.html) and [Connect to Amazon Managed Service for Prometheus and open-source Prometheus data sources](https://docs.aws.amazon.com/grafana/latest/userguide/prometheus-data-source.html). 

1. Under **Permissions and access**, for **HyperPod observability IAM role**, choose **Create and use new service role** or **Use existing service role**.

   For the permissions that the role needs, see [Permissions for the observability add-on role](#hyperpod-observability-addon-setup-permissions).

## Configuring the observability add-on with the AWS CLI
<a name="hyperpod-observability-addon-setup-cli"></a>

To choose the metric store from the AWS CLI, pass configuration values to the `aws eks create-addon` or `aws eks update-addon` command. The add-on accepts the following configuration values for the metric store.


**Configuration values for the metric store**  

| Key | Description | Add-on version | 
| --- | --- | --- | 
| metricsDestination | The metric store. Valid values are `cloudwatch` and `amp`.<br />If you don't specify this key, the add-on sends metrics to Amazon Managed Service for Prometheus when you specify `ampWorkspace`, and to Amazon CloudWatch when you don't. | v1.5.0-eksbuild.1 and later | 
| ampWorkspace.prometheusEndpoint | The endpoint of your Amazon Managed Service for Prometheus workspace, for example `https://aps-workspaces.{{us-west-2}}.amazonaws.com/workspaces/{{ws-11111111-2222-3333-4444-555555555555}}/`. Specify the workspace endpoint, not the remote write URL. This key is required when you specify `ampWorkspace`.<br />When `metricsDestination` is `cloudwatch`, don't specify `ampWorkspace`. When `metricsDestination` is `amp`, `ampWorkspace` is required. | All | 
| ampWorkspace.arn | The Amazon Resource Name (ARN) of your Amazon Managed Service for Prometheus workspace. | All | 

Versions earlier than `v1.5.0-eksbuild.1` reject `metricsDestination`.

The following configuration values send metrics to Amazon CloudWatch. Use add-on version `v1.5.0-eksbuild.1` or later.

```json
{
    "metricsDestination": "cloudwatch"
}
```

The following configuration values send metrics to an Amazon Managed Service for Prometheus workspace. All versions of the add-on accept them. In version `v1.5.0-eksbuild.1` and later, you can also add `"metricsDestination": "amp"`.

```json
{
    "ampWorkspace": {
        "prometheusEndpoint": "https://aps-workspaces.{{us-west-2}}.amazonaws.com/workspaces/{{ws-11111111-2222-3333-4444-555555555555}}/",
        "arn": "arn:aws:aps:{{us-west-2}}:{{111122223333}}:workspace/{{ws-11111111-2222-3333-4444-555555555555}}"
    }
}
```

To install the add-on with Amazon CloudWatch as the metric store, run the following AWS CLI command. Replace {{my-eks-cluster}} with the name of your Amazon EKS cluster and {{role-arn}} with the ARN of the IAM role for the add-on. For the permissions that the role needs, see [Permissions for the observability add-on role](#hyperpod-observability-addon-setup-permissions).

```
aws eks create-addon \
    --cluster-name {{my-eks-cluster}} \
    --addon-name amazon-sagemaker-hyperpod-observability \
    --addon-version v1.5.0-eksbuild.1 \
    --configuration-values '{"metricsDestination":"cloudwatch"}' \
    --pod-identity-associations serviceAccount=hyperpod-observability-operator-otel-collector,roleArn={{role-arn}}
```

When you run `aws eks update-addon`, pass the full configuration that you want in `--configuration-values`, not only the keys that you change. To change one setting of an installed add-on, do the following steps:

1. Get the current configuration values, and save them in a file.

   ```
   aws eks describe-addon \
       --cluster-name {{my-eks-cluster}} \
       --addon-name amazon-sagemaker-hyperpod-observability \
       --query addon.configurationValues \
       --output text > config.json
   ```

   If the file contains `None`, replace its content with `{}`.

1. Edit `config.json`. Keep the keys that you don't change.

1. Send the complete file to the add-on. Replace {{v1.5.0-eksbuild.1}} with the version of the installed add-on or a later version.

   ```
   aws eks update-addon \
       --cluster-name {{my-eks-cluster}} \
       --addon-name amazon-sagemaker-hyperpod-observability \
       --addon-version {{v1.5.0-eksbuild.1}} \
       --configuration-values file://config.json
   ```

For example, an add-on that sends metrics to Amazon Managed Service for Prometheus can have the following configuration values:

```json
{
    "ampWorkspace": {
        "prometheusEndpoint": "https://aps-workspaces.{{us-west-2}}.amazonaws.com/workspaces/{{ws-11111111-2222-3333-4444-555555555555}}/",
        "arn": "arn:aws:aps:{{us-west-2}}:{{111122223333}}:workspace/{{ws-11111111-2222-3333-4444-555555555555}}"
    },
    "metricsProvider": {
        "nodeMetrics": {
            "level": "ADVANCED"
        },
        "logging": {
            "enabled": true
        }
    }
}
```

To change the metric store of the same add-on from Amazon Managed Service for Prometheus to Amazon CloudWatch, remove `ampWorkspace`, and set `metricsDestination` to `cloudwatch`. Make sure that the add-on role allows `cloudwatch:PutMetricData`.

```json
{
    "metricsDestination": "cloudwatch",
    "metricsProvider": {
        "nodeMetrics": {
            "level": "ADVANCED"
        },
        "logging": {
            "enabled": true
        }
    }
}
```

To change the metric store from Amazon CloudWatch back to Amazon Managed Service for Prometheus, set `metricsDestination` to `amp`, and specify `ampWorkspace` again. Make sure that the add-on role allows `aps:RemoteWrite` on the ARN of your workspace. A role that the console created for Amazon CloudWatch doesn't allow this action on your workspace. Add a statement for the workspace to the role, or use a new role.

After you change the metric store, the add-on sends new metrics only to the new metric store. It doesn't copy the metrics that are already in the old metric store. Metrics in an Amazon Managed Service for Prometheus workspace stay there for the retention period of the workspace.

If the configuration of the add-on has an Amazon Managed Grafana workspace (`amgWorkspace`), the console replaces the SageMaker HyperPod dashboards in that workspace with the dashboards for the new metric store. This happens the next time that you open the observability page of the cluster in the SageMaker AI console. The console overwrites the dashboards that have the same UID.

## Permissions for the observability add-on role
<a name="hyperpod-observability-addon-setup-permissions"></a>

The observability add-on gets credentials through Amazon EKS Pod Identity. The Pod Identity association links the IAM role for the add-on to the service account `hyperpod-observability-operator-otel-collector`. The role needs the following actions for the features that you use.


**Actions for the observability add-on role**  

| Feature | Action | 
| --- | --- | 
| Metrics in Amazon CloudWatch | cloudwatch:PutMetricData | 
| Metrics in Amazon Managed Service for Prometheus | aps:RemoteWrite | 

The add-on recommends the AWS managed policies [CloudWatchAgentServerPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchAgentServerPolicy.html) and [AmazonPrometheusRemoteWriteAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonPrometheusRemoteWriteAccess.html) for this role. `CloudWatchAgentServerPolicy` allows `cloudwatch:PutMetricData`. `AmazonPrometheusRemoteWriteAccess` allows `aps:RemoteWrite`.

When you choose **Create and use new service role** in the console, the console creates a role that allows `cloudwatch:PutMetricData`.

If you use your own policy instead, add a statement like the following. Replace {{111122223333}} with your account ID.

```json
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "CloudwatchMetricsAccess",
            "Effect": "Allow",
            "Action": "cloudwatch:PutMetricData",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{111122223333}}"
                }
            }
        }
    ]
}
```