# Install the CloudWatch agent with the

Amazon CloudWatch Observability EKS add-on or the Helm chart

###### Note

We recommend using Amazon Linux 2 nodes for full compatibility when using the Amazon CloudWatch
Observability Add-on. When using Amazon Linux 2023 nodes, dataplane and host logs vended by
Container Insights will not be available by default due to the change in the system
logging mechanism introduced in Amazon Linux 2023. Application logs will continue to work as
expected. For more information about Amazon Linux 2023 changes, see the [Amazon Linux 2023 User
Guide](../../../linux/al2023/ug/journald.md "../../../linux/al2023/ug/journald.md").

You can use either the Amazon CloudWatch Observability EKS add-on or the Amazon CloudWatch Observability
Helm chart to install the CloudWatch Agent and the Fluent-bit agent on an Amazon EKS cluster. You can
also use the Helm chart to install the CloudWatch Agent and the Fluent-bit agent on a Kubernetes
cluster that is not hosted on Amazon EKS.

Using either method on an Amazon EKS cluster enables both [Container Insights](ContainerInsights.md "ContainerInsights.md") with enhanced observability for Amazon EKS and [CloudWatch Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md") by
default. Both features help you to collect infrastructure metrics, application performance
telemetry, and container logs from the cluster.

With Container Insights with enhanced observability for Amazon EKS, Container Insights
metrics are charged per observation instead of being charged per metric stored or log
ingested. For Application Signals, billing is based on inbound requests to your
applications, outbound requests from your applications, and each configured service level
objective (SLO). Each inbound request received generates one application signal, and each
outbound request made generates one application signal. Every SLO creates two application
signals per measurement period. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Both methods enable Container Insights on both Linux and Windows worker nodes in the
Amazon EKS cluster. To enable Container Insights on Windows, you must use version 1.5.0 or later
of the Amazon EKS add-on or the Helm chart. Application Signals is not supported on
Windows in Amazon EKS clusters.

The Amazon CloudWatch Observability EKS add-on is supported on Amazon EKS clusters running with
Kubernetes version 1.23 or later.

When you install the add-on or the Helm chart, you must also grant IAM permissions to
enable the CloudWatch agent to send metrics, logs, and traces to CloudWatch. There are two ways to do
this:

- Attach a policy to the IAM role of your worker nodes. This option grants
  permissions to worker nodes to send telemetry to CloudWatch.
- Use an IAM role for service accounts for the agent pods, and attach the policy to
  this role. This works only for Amazon EKS clusters. This option gives CloudWatch access only to the
  appropriate agent pods.

###### Topics

- [Option 1: Install
  using EKS Pod Identity](#install-CloudWatch-Observability-EKS-pod-identity "#install-CloudWatch-Observability-EKS-pod-identity")
- [Option 2:
  Install with IAM permissions on worker nodes](#install-CloudWatch-Observability-EKS-addon-workernodes "#install-CloudWatch-Observability-EKS-addon-workernodes")
- [Option 3:
  Install using IAM service account role (applies only to using the add-on)](#install-CloudWatch-Observability-EKS-addon-serviceaccountrole "#install-CloudWatch-Observability-EKS-addon-serviceaccountrole")
- [Considerations for
  Amazon EKS Hybrid Nodes](#install-CloudWatch-Observability-EKS-addon-hybrid "#install-CloudWatch-Observability-EKS-addon-hybrid")
- [(Optional)
  Additional configuration](#install-CloudWatch-Observability-EKS-addon-configuration "#install-CloudWatch-Observability-EKS-addon-configuration")
- [Collect Java
  Management Extensions (JMX) metrics](#install-CloudWatch-Observability-EKS-addon-JMX-metrics "#install-CloudWatch-Observability-EKS-addon-JMX-metrics")
- [Enable Kueue metrics](#enable-Kueue-metrics "#enable-Kueue-metrics")
- [Appending
  OpenTelemetry collector configuration files](#install-CloudWatch-Observability-EKS-addon-OpenTelemetry "#install-CloudWatch-Observability-EKS-addon-OpenTelemetry")
- [Enabling APM through Application Signals for your Amazon EKS cluster](#Container-Insights-setup-EKS-appsignalsconfiguration "#Container-Insights-setup-EKS-appsignalsconfiguration")
- [Troubleshooting the
  Amazon CloudWatch Observability EKS add-on or the Helm chart](#Container-Insights-setup-EKS-addon-troubleshoot "#Container-Insights-setup-EKS-addon-troubleshoot")
- [Opt out of Application Signals](#Opting-out-App-Signals "#Opting-out-App-Signals")

## Option 1: Install

using EKS Pod Identity

If you use version 3.1.0 or later of the add-on, you can use EKS Pod Identity to grant
the required permissions to the add-on. EKS Pod Identity is the recommended option and
provides benefits such as least privilege, credential rotation, and auditability.
Additionally, using EKS Pod Identity allows you to install the EKS add-on as part of the
cluster creation itself.

To use this method, first follow the [EKS Pod
Identity association](../../../eks/latest/userguide/pod-id-association.md#pod-id-association-create/ "../../../eks/latest/userguide/pod-id-association.md#pod-id-association-create/") steps to create the IAM role and set up the EKS Pod
Identity agent.

Then install the Amazon CloudWatch Observability EKS add-on. To install the add-on, you can use
the AWS CLI, the Amazon EKS console, AWS CloudFormation, or Terraform.

AWS CLI

###### To use the AWS CLI to install the Amazon CloudWatch Observability EKS add-on

Enter the following commands. Replace
`my-cluster-name` with the name of your
cluster and replace `111122223333` with your account ID.
Replace `my-role` with the IAM role that you created in
the EKS Pod Identity association step.

```
aws iam attach-role-policy \
--role-name `my-role` \
--policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy

aws eks create-addon \
--addon-name amazon-cloudwatch-observability \
--cluster-name `my-cluster-name` \
--pod-identity-associations serviceAccount=cloudwatch-agent,roleArn=arn:aws:iam::`111122223333`:role/`my-role`
```

Amazon EKS console

###### To use the Amazon EKS console to add the Amazon CloudWatch Observability EKS add-on

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the left navigation pane, choose **Clusters**.
3. Choose the name of the cluster that you want to configure the Amazon CloudWatch
   Observability EKS add-on for.
4. Choose the **Add-ons** tab.
5. Choose **Get more add-ons**.
6. On the **Select add-ons** page, do the following:
   1. In the **Amazon EKS-addons** section, select the
      **Amazon CloudWatch Observability** check box.
   2. Choose **Next**.

7. On the **Configure selected add-ons settings** page, do the
   following:
   1. Select the **Version** you'd like to use.
   2. For **Add-on access**, select **EKS Pod
      Identity**
   3. If you don't have an IAM role configured, choose **Create
      recommended role**, then choose **Next** until
      you are at **Step 3 Name, review, and create**. You can
      change your role name if desired, otherwise, choose **Create
      Role**, and then return to the Add-on page and select the IAM
      role that you just created.
   4. (Optional) You can expand the **Optional configuration
      settings**. If you select **Override** for the
      **Conflict resolution method**, one or more of the
      settings for the existing add-on can be overwritten with the Amazon EKS add-on
      settings. If you don't enable this option and there's a conflict with your
      existing settings, the operation fails. You can use the resulting error
      message to troubleshoot the conflict. Before selecting this option, make
      sure that the Amazon EKS add-on doesn't manage settings that you need to
      self-manage.
   5. Choose **Next**.

8. On the **Review and add** page, choose
   **Create**. After the add-on installation is complete, you
   see your installed add-on.

AWS CloudFormation

###### To use AWS CloudFormation to install the Amazon CloudWatch Observability EKS add-on

1. First, run the following AWS CLI command to attach the necessary IAM policy
   to your IAM role. Replace `my-role` with the role
   that you created in the EKS Pod Identity association step.

```
aws iam attach-role-policy \
--role-name `my-role` \
--policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
```

2. Then create the following resource. Replace
   `my-cluster-name` with the name of
   your cluster, replace `111122223333` with your account
   ID, and replace `my-role` with the IAM role created
   in EKS Pod Identity association step. For more information, see [AWS::EKS::Addon](../../../AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.md").

```
{
    "Resources": {
        "EKSAddOn": {
            "Type": "AWS::EKS::Addon",
            "Properties": {
                "AddonName": "amazon-cloudwatch-observability",
                "ClusterName": "`my-cluster-name`",
                "PodIdentityAssociations": [
                    {
                        "ServiceAccount": "cloudwatch-agent",
                        "RoleArn": "arn:aws:iam::`111122223333`:role/`my-role`"
                    }
                ]
            }
        }
    }
}
```

Terraform

###### To use Terraform to install the Amazon CloudWatch Observability EKS add-on

1. Use the following. Replace
   `my-cluster-name` with the name of your
   cluster, replace `111122223333` with your account ID,
   and replace `my-service-account-role` with the IAM
   role created in EKS Pod Identity association step.

For more information, see [Resource: aws_eks_addon](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_addon "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_addon") in the Terraform documentation. 2. ```
resource "aws_iam_role_policy_attachment" "CloudWatchAgentServerPolicy" {
policy_arn = "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy"
role = "my-role"
}

resource "aws_eks_addon" "example" {
cluster_name = "my-cluster-name"
addon_name = "amazon-cloudwatch-observability"
pod_identity_associations {
roleArn = "arn:aws:iam::111122223333:role/my-role"
serviceAccount = "cloudwatch-agent"
}
}

```



##  Option 2:
 Install with IAM permissions on worker nodes


To use this method, first attach the **CloudWatchAgentServerPolicy**
 IAM policy to your worker nodes by entering the following command. In this command,
 replace `my-worker-node-role` with the IAM role used by your
 Kubernetes worker nodes.



```

aws iam attach-role-policy \
--role-name `my-worker-node-role` \
--policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy

```

Then install the Amazon CloudWatch Observability EKS add-on. To install the add-on, you can use
 the AWS CLI, the console, AWS CloudFormation, or Terraform.



AWS CLI
###### To use the AWS CLI to install the Amazon CloudWatch Observability EKS add-on


Enter the following command. Replace
 ``my-cluster-name`` with the name of your
 cluster.



```

aws eks create-addon --addon-name amazon-cloudwatch-observability --cluster-name `my-cluster-name`

```


Amazon EKS console
###### To use the Amazon EKS console to add the Amazon CloudWatch Observability EKS add-on

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the left navigation pane, choose **Clusters**.
3. Choose the name of the cluster that you want to configure the Amazon CloudWatch
 Observability EKS add-on for.
4. Choose the **Add-ons** tab.
5. Choose **Get more add-ons**.
6. On the **Select add-ons** page, do the following:


	1. In the **Amazon EKS-addons** section, select the
	 **Amazon CloudWatch Observability** check box.
	2. Choose **Next**.
7. On the **Configure selected add-ons settings** page, do the
 following:


	1. Select the **Version** you'd like to use.
	2. (Optional) You can expand the **Optional configuration
	 settings**. If you select **Override** for the
	 **Conflict resolution method**, one or more of the
	 settings for the existing add-on can be overwritten with the Amazon EKS add-on
	 settings. If you don't enable this option and there's a conflict with your
	 existing settings, the operation fails. You can use the resulting error
	 message to troubleshoot the conflict. Before selecting this option, make
	 sure that the Amazon EKS add-on doesn't manage settings that you need to
	 self-manage.
	3. Choose **Next**.
8. On the **Review and add** page, choose
 **Create**. After the add-on installation is complete, you
 see your installed add-on.


AWS CloudFormation
###### To use AWS CloudFormation to install the Amazon CloudWatch Observability EKS add-on


Replace ``my-cluster-name`` with the name
 of your cluster. For more information, see [AWS::EKS::Addon](../../../AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.md").



```

{
"Resources": {
"EKSAddOn": {
"Type": "AWS::EKS::Addon",
"Properties": {
"AddonName": "amazon-cloudwatch-observability",
"ClusterName": "`my-cluster-name`"
}
}
}
}

```


Helm chart
###### To use the `amazon-cloudwatch-observability` Helm chart

1. You must have Helm installed to use this chart. For more information about
 installing Helm, see the [Helm
 documentation](https://helm.sh/docs/ "https://helm.sh/docs/").
2. After you have installed Helm, enter the following commands. Replace
 `my-cluster-name` with the name of your cluster, and
 replace `my-cluster-region` with the Region that the
 cluster runs in.



```

helm repo add aws-observability https://aws-observability.github.io/helm-charts
helm repo update aws-observability
helm install --wait --create-namespace --namespace amazon-cloudwatch amazon-cloudwatch-observability aws-observability/amazon-cloudwatch-observability --set clusterName=`my-cluster-name` --set region=`my-cluster-region`

```


Terraform
###### To use Terraform to install the Amazon CloudWatch Observability EKS add-on


Replace ``my-cluster-name`` with the name
 of your cluster. For more information, see [Resource: aws\_eks\_addon](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_ad "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_ad").



```

resource "aws_eks_addon" "example" {
addon_name = "amazon-cloudwatch-observability"
cluster_name = "`my-cluster-name`"
}

```



##  Option 3:
 Install using IAM service account role (applies only to using the add-on)


This method is valid only if you are using the Amazon CloudWatch Observability EKS add-on.
 Before using this method, verify the following prerequisites:



* You have a functional Amazon EKS cluster with nodes attached in one of the
 AWS Regions that supports Container Insights. For the list of supported Regions, see
 [Container Insights](ContainerInsights.md "ContainerInsights.md").
* You have `kubectl` installed and configured for the cluster. For more
 information, see [Installing
 `kubectl`](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md") in the *Amazon EKS User Guide*.
* You have `eksctl` installed. For more information, see [Installing or updating
 `eksctl`](../../../eks/latest/userguide/eksctl.md "../../../eks/latest/userguide/eksctl.md") in the *Amazon EKS User Guide*.


AWS CLI
###### To use the AWS CLI to install the Amazon CloudWatch Observability EKS add-on using the
 IAM service account role

1. Enter the following command to create an OpenID Connect (OIDC) provider, if
 the cluster doesn't have one already. For more information, see [Configuring a
 Kubernetes service account to assume an IAM role](../../../eks/latest/userguide/associate-service-account-role.md "../../../eks/latest/userguide/associate-service-account-role.md") in the
 *Amazon EKS User Guide*.



```

eksctl utils associate-iam-oidc-provider --cluster `my-cluster-name` --approve

```
2. Enter the following command to create the IAM role with the
 **CloudWatchAgentServerPolicy** policy attached, and
 configure the agent service account to assume that role using OIDC. Replace
 `my-cluster-name` with the name of your cluster, and
 replace `my-service-account-role` with the name of the
 role that you want to associate the service account with. If the role doesn't
 already exist, `eksctl` creates it for you.



```

eksctl create iamserviceaccount \
 --name cloudwatch-agent \
 --namespace amazon-cloudwatch --cluster `my-cluster-name` \
 --role-name `my-service-account-role` \
 --attach-policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy \
 --role-only \
 --approve

```
3. Install the add-on by entering the following command. Replace
 `my-cluster-name` with the name of your cluster,
 replace `111122223333` with your account ID, and
 replace `my-service-account-role` with the IAM role
 created in the previous step.



```

aws eks create-addon --addon-name amazon-cloudwatch-observability --cluster-name `my-cluster-name` --service-account-role-arn arn:aws:iam::`111122223333`:role/`my-service-account-role`

```


Amazon EKS console
###### To use the console to install the Amazon CloudWatch Observability EKS add-on using the
 IAM service account role

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the left navigation pane, choose **Clusters**.
3. Choose the name of the cluster that you want to configure the Amazon CloudWatch
 Observability EKS add-on for.
4. Choose the **Add-ons** tab.
5. Choose **Get more add-ons**.
6. On the **Select add-ons** page, do the following:


	1. In the **Amazon EKS-addons** section, select the
	 **Amazon CloudWatch Observability** check box.
	2. Choose **Next**.
7. On the **Configure selected add-ons settings** page, do the
 following:


	1. Select the **Version** you'd like to use.
	2. For **Add-on access**, select **IAM roles for
	 service accounts (IRSA)**
	3. Select the IAM role in the **Add-on access**
	 box.
	4. (Optional) You can expand the **Optional configuration
	 settings**. If you select **Override** for the
	 **Conflict resolution method**, one or more of the
	 settings for the existing add-on can be overwritten with the Amazon EKS add-on
	 settings. If you don't enable this option and there's a conflict with your
	 existing settings, the operation fails. You can use the resulting error
	 message to troubleshoot the conflict. Before selecting this option, make
	 sure that the Amazon EKS add-on doesn't manage settings that you need to
	 self-manage.
	5. Choose **Next**.
8. On the **Review and add** page, choose
 **Create**. After the add-on installation is complete, you
 see your installed add-on.



## Considerations for
 Amazon EKS Hybrid Nodes


Node-level metrics aren't available for hybrid nodes because [Container Insights](ContainerInsights.md "ContainerInsights.md") depends on the
 availability of the [EC2 Instance Metadata Service](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") (IMDS) for node-level
 metrics. Cluster, workload, Pod, and container-level metrics are available
 for hybrid nodes.


After you install the add-on by following the steps in the previous sections, you must
 update the add-on manifest so that the agent can run successfully on hybrid nodes. Edit
 the `amazoncloudwatchagents` resource in the cluster to add the
 `RUN_WITH_IRSA` environment variable to match the following.



```

kubectl edit amazoncloudwatchagents -n amazon-cloudwatch cloudwatch-agent

```


```

apiVersion: v1
items: - apiVersion: cloudwatch.aws.amazon.com/v1alpha1
kind: AmazonCloudWatchAgent
metadata:
...
name: cloudwatch-agent
namespace: amazon-cloudwatch
...
spec:
...
env: - name: RUN_WITH_IRSA # <-- Add this
value: "True" # <-- Add this - name: K8S_NODE_NAME
valueFrom:
fieldRef:
fieldPath: spec.nodeName
...

```

## (Optional)
 Additional configuration


###### Topics

* [Opt out of
 collecting container logs](#CloudWatch-Observability-EKS-addon-OptOutContainerLogs "#CloudWatch-Observability-EKS-addon-OptOutContainerLogs")
* [Use a custom Fluent
 Bit configuration](#CloudWatch-Observability-EKS-addon-CustomFluentBit "#CloudWatch-Observability-EKS-addon-CustomFluentBit")
* [Manage Kubernetes
 tolerations for the installed pod workloads](#CloudWatch-Observability-EKS-addon-Tolerations "#CloudWatch-Observability-EKS-addon-Tolerations")
* [Opt out of
 accelerated compute metrics collection](#CloudWatch-Observability-EKS-addon-OptOutAccelerated "#CloudWatch-Observability-EKS-addon-OptOutAccelerated")
* [Use a custom CloudWatch
 agent configuration](#CloudWatch-Observability-EKS-addon-CustomAgentConfig "#CloudWatch-Observability-EKS-addon-CustomAgentConfig")
* [Manage admission webhook
 TLS certificates](#CloudWatch-Observability-EKS-addon-Webhook "#CloudWatch-Observability-EKS-addon-Webhook")
* [Collect Amazon EBS volume
 IDs](#CloudWatch-Observability-EKS-addon-VolumeIDs "#CloudWatch-Observability-EKS-addon-VolumeIDs")

### Opt out of
 collecting container logs


By default, the add-on uses Fluent Bit to collect container logs from all pods and
 then sends the logs to CloudWatch Logs. For information about which logs are collected, see [Setting up Fluent Bit](Container-Insights-setup-logs-FluentBit.md#Container-Insights-FluentBit-setup "Container-Insights-setup-logs-FluentBit.md#Container-Insights-FluentBit-setup").


###### Note

Neither the add-on or the Helm chart manage existing Fluentd or Fluent Bit
 resources in a cluster. You can delete the existing Fluentd or Fluent Bit resources
 before installing the add-on or Helm chart. Alternatively, to keep your existing setup
 and avoid having the add-on or the Helm chart from also installing Fluent Bit, you can
 disable it by following the instructions in this section.


To opt out of the collection of container logs if you are using the Amazon CloudWatch
 Observability EKS add-on, pass the following option when you create or update the
 add-on:



```

--configuration-values '{ "containerLogs": { "enabled": false } }'

```

To opt out of the collection of container logs if you are using the Helm chart, pass
 the following option when you create or update the add-on:



```

--set containerLogs.enabled=false

```

### Use a custom Fluent
 Bit configuration


Starting with version 1.7.0 of the Amazon CloudWatch Observability EKS add-on, you can modify
 the Fluent Bit configuration when you create or update the add-on or Helm chart. You
 supply the custom Fluent Bit configuration in the `containerLogs` root level
 section of the advanced configuration of the add-on or the value overrides in the Helm
 chart. Within this section, you supply the custom Fluent Bit configuration in the
 `config` section (for Linux) or `configWindows` section (for
 Windows). The `config` is further broken down into the following
 sub-sections:



* `service`– This section represents the `SERVICE`
 config to define the global behavior of the Fluent Bit engine.
* `customParsers`– This section represents any global
 `PARSER`s that you want to include that are capable of taking
 unstructured log entries and giving them a structure to make it easier for
 processing and further filtering.
* `extraFiles`– This section can be used to provide additional
 Fluent Bit `conf` files to be included. By default, the following 3
 `conf` files are included:.




	+ `application-log.conf`– A `conf` file for
	 sending application logs from your cluster to the log group
	 `/aws/containerinsights/`my-cluster-name`/application`
	 in CloudWatch Logs.
	+ `dataplane-log.conf`– A `conf` file for sending
	 logs corresponding to your cluster’s data plane components including the CRI
	 logs, kubelet logs, kube-proxy logs and Amazon VPC CNI logs to the log group
	 `/aws/containerinsights/`my-cluster-name`/dataplane`
	 in CloudWatch Logs.
	+ `host-log.conf`– A `conf` for sending logs from
	 `/var/log/dmesg`, `/var/log/messages`, and
	 `/var/log/secure` on Linux, and System `winlogs` on
	 Windows, to the log group
	 `/aws/containerinsights/`my-cluster-name`/host`
	 in CloudWatch.

###### Note

Provide the full configuration for each of these individual sections even if you
 are modifying only one field within a sub-section. We recommend that you use the
 default configuration provided below as a baseline and then modify it accordingly so
 that you don't disable functionality that is enabled by default. You can use the
 following YAML configuration when modifying the advanced config for the Amazon EKS add-on
 or when you supply value overrides for the Helm chart.


To find the `config` section for your cluster, see [aws-observability /
 helm-charts](https://github.com/aws-observability/helm-charts/releases "https://github.com/aws-observability/helm-charts/releases") on GitHub and find the release corresponding to the version of the
 add-on or Helm chart that you are installing. Then navigate to
 `/charts/amazon-cloudwatch-observability/values.yaml` to find the
 `config` section (for Linux) and `configWindows` section (for
 Windows) within the `fluentBit` section under
 `containerLogs`.


As an example, the default Fluent Bit configuration for version 1.7.0 can be found
 [here](https://github.com/aws-observability/helm-charts/blob/v1.7.0/charts/amazon-cloudwatch-observability/values.yaml#L44) "https://github.com/aws-observability/helm-charts/blob/v1.7.0/charts/amazon-cloudwatch-observability/values.yaml#L44)").


We recommend that you provide the `config` as YAML when you supply it
 using the Amazon EKS add-on’s advanced config or when you supply it as value overrides for
 your Helm installation. Be sure that the YAML conforms to the following
 structure.



```

containerLogs:
fluentBit:
config:
service: |
...
customParsers: |
...
extraFiles:
application-log.conf: |
...
dataplane-log.conf: |
...
host-log.conf: |
...

```

The following example `config` changes the global setting for the flush
 interval to be 45 seconds. Even though the only modification is to the
 `Flush` field, you must still provide the full `SERVICE`
 definition for the service sub-section. Because this example didn't specify overrides
 for the other sub-sections, the defaults are used for them.



```

containerLogs:
fluentBit:
config:
service: |
[SERVICE]
Flush 45
Grace 30
Log_Level error
Daemon off
Parsers_File parsers.conf
storage.path /var/fluent-bit/state/flb-storage/
storage.sync normal
storage.checksum off
storage.backlog.mem_limit 5M

```

The following example configuration includes an extra Fluent bit `conf`
 file. In this example, we are adding a custom `my-service.conf` under
 `extraFiles` and it will be included in addition to the three default
 `extraFiles`.



```

containerLogs:
fluentBit:
config:
extraFiles:
my-service.conf: |
[INPUT]
Name tail
Tag myservice.*
Path /var/log/containers/*myservice\*.log
DB /var/fluent-bit/state/flb_myservice.db
Mem_Buf_Limit 5MB
Skip_Long_Lines On
Ignore_Older 1d
Refresh_Interval 10

          [OUTPUT]
            Name                cloudwatch_logs
            Match               myservice.*
            region              ${AWS_REGION}
            log_group_name      /aws/containerinsights/${CLUSTER_NAME}/myservice
            log_stream_prefix   ${HOST_NAME}-
            auto_create_group   true

```

The next example removes an existing `conf` file entirely from
 `extraFiles`. This excludes the `application-log.conf` entirely
 by overriding it with an empty string. Simply omitting `application-log.conf`
 from `extraFiles` would instead imply to use the default, which is not what
 we are trying to achieve in this example. The same applies to removing any custom
 `conf` file that you might have previously added to
 `extraFiles`.



```

containerLogs:
fluentBit:
config:
extraFiles:
application-log.conf: ""

```

### Manage Kubernetes
 tolerations for the installed pod workloads


Starting with version 1.7.0 of the Amazon CloudWatch Observability EKS add-on, the add-on and
 the Helm chart by default set Kubernetes *tolerations* to tolerate
 all taints on the pod workloads that are installed by the add-on or the Helm chart. This
 ensures that daemonsets such as the CloudWatch agent and Fluent Bit can schedule pods on all
 nodes in your cluster by default. For more information about tolerations and taints, see
 [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/") in the Kubernetes documentation.


The default tolerations set by the add-on or the Helm chart are as follows:



```

tolerations:

- operator: Exists

```

You can override the default tolerations by setting the `tolerations`
 field at the root level when using the add-on advanced config or when you install or
 upgrade the Helm chart with value overrides. An example would look like the
 following:



```

tolerations:

- key: "key1"
  operator: "Exists"
  effect: "NoSchedule"

```

To omit tolerations completely, you can use a config that looks like the
 following:



```

tolerations: []

```

Any changes to tolerations apply to all pod workloads that are installed by the
 add-on or the Helm chart.


### Opt out of
 accelerated compute metrics collection


By default, Container Insights with enhanced observability collects metrics for
 Accelerated Compute monitoring, including NVIDIA GPU metrics, AWS Neuron metrics for
 AWS Trainium and AWS Inferentia, and AWS Elastic Fabric Adapter (EFA)
 metrics.


NVIDIA GPU metrics from Amazon EKS workloads are collected by default beginning with
 version `v1.3.0-eksbuild.1` of the EKS add-on or the Helm chart and version
 `1.300034.0` of the CloudWatch agent. For a list of metrics collected and
 prerequisites, see [NVIDIA GPU metrics](Container-Insights-metrics-enhanced-EKS.md#Container-Insights-metrics-EKS-GPU "Container-Insights-metrics-enhanced-EKS.md#Container-Insights-metrics-EKS-GPU").


AWS Neuron metrics for AWS Trainium and AWS Inferentia accelerators are
 collected by default beginning with version `v1.5.0-eksbuild.1` of the EKS
 add-on or the Helm chart, and version `1.300036.0` of the CloudWatch agent. For a
 list of metrics collected and prerequisites, see [AWS Neuron metrics for AWS
 Trainium and AWS Inferentia](Container-Insights-metrics-enhanced-EKS.md#Container-Insights-metrics-EKS-Neuron "Container-Insights-metrics-enhanced-EKS.md#Container-Insights-metrics-EKS-Neuron") .


AWS Elastic Fabric Adapter (EFA) metrics from Linux nodes on Amazon EKS clusters are
 collected by default beginning with version `v1.5.2-eksbuild.1` of the EKS
 add-on or the Helm chart and version `1.300037.0` of the CloudWatch agent. For a
 list of metrics collected and prerequisites, see [AWS Elastic Fabric Adapter (EFA)
 metrics](Container-Insights-metrics-enhanced-EKS.md#Container-Insights-metrics-EFA "Container-Insights-metrics-enhanced-EKS.md#Container-Insights-metrics-EFA") .


You can opt out of collecting these metrics by setting the
 `accelerated_compute_metrics` field in the CloudWatch agent configuration file to
 `false`. This field is in the `kubernetes` section of the
 `metrics_collected` section in the CloudWatch configuration file. The following
 is an example of an opt-out configuration. For more information about how to use custom
 CloudWatch agent configurations, see the following section, [Use a custom CloudWatch
 agent configuration](#CloudWatch-Observability-EKS-addon-CustomAgentConfig "#CloudWatch-Observability-EKS-addon-CustomAgentConfig").



```

{
"logs": {
"metrics_collected": {
"kubernetes": {
"enhanced_container_insights": true,
"accelerated_compute_metrics": false
}
}
}
}

```

### Use a custom CloudWatch
 agent configuration


To collect other metrics, logs or traces using the CloudWatch agent, you can specify a
 custom configuration while also keeping Container Insights and CloudWatch Application Signals
 enabled. To do so, embed the CloudWatch agent configuration file within the config key under
 the agent key of the advanced configuration that you can use when creating or updating
 the EKS add-on or the Helm chart. The following represents the default agent
 configuration when you do not provide any additional configuration.


###### Important

Any custom configuration that you provide using additional configuration settings
 overrides the default configuration used by the agent. Be cautious not to
 unintentionally disable functionality that is enabled by default, such as Container
 Insights with enhanced observability and CloudWatch Application Signals. In the scenario
 that you are required to provide a custom agent configuration, we recommend using the
 following default configuration as a baseline and then modifying it
 accordingly.



* For using the Amazon CloudWatch observability EKS add-on



```

--configuration-values '{
"agent": {
"config": {
"logs": {
"metrics_collected": {
"application_signals": {},
"kubernetes": {
"enhanced_container_insights": true
}
}
},
"traces": {
"traces_collected": {
"application_signals": {}
}
}
}
}  
}'

```
* For using the Helm chart



```

--set agent.config='{
"logs": {
"metrics_collected": {
"application_signals": {},
"kubernetes": {
"enhanced_container_insights": true
}
}
},
"traces": {
"traces_collected": {
"application_signals": {}
}
}
}'

```

The following example shows the default agent configuration for the CloudWatch agent on
 Windows. The CloudWatch agent on Windows does not support custom configuration.



```

{
"logs": {
"metrics_collected": {
"kubernetes": {
"enhanced_container_insights": true
},
}
}
}

```

### Manage admission webhook
 TLS certificates


The Amazon CloudWatch Observability EKS add-on and the Helm chart leverage Kubernetes  [admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/ "https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/") to validate and mutate `AmazonCloudWatchAgent`
 and `Instrumentation` custom resource (CR) requests, and optionally
 Kubernetes pod requests on the cluster if CloudWatch Application Signals is enabled. In
 Kubernetes, webhooks require a TLS certificate that the API server is configured to
 trust in order to ensure secure communication.


By default, the Amazon CloudWatch Observability EKS add-on and the Helm chart auto-generate a
 self-signed CA and a TLS certificate signed by this CA for securing the communication
 between the API server and the webhook server. This auto-generated certificate has a
 default expiry of 10 years and is not auto-renewed upon expiry. In addition, the CA
 bundle and the certificate are re-generated every time the add-on or Helm chart is
 upgraded or re-installed, thus resetting the expiry. If you want to change the default
 expiry of the auto-generated certificate, you can use the following additional
 configurations when creating or updating the add-on. Replace
 `expiry-in-days` with your desired expiry duration in days.



* Use this for the Amazon CloudWatch Observability EKS add-on



```

--configuration-values '{ "admissionWebhooks": { "autoGenerateCert": { "expiryDays": `expiry-in-days` } } }'

```
* Use this for the Helm chart



```

--set admissionWebhooks.autoGenerateCert.expiryDays=expiry-in-days

```

For a more secure and feature-rich certificate authority solution, the add-on has
 opt-in support for  [cert-manager](https://cert-manager.io/docs/ "https://cert-manager.io/docs/"), a
 widely-adopted solution for TLS certificate management in Kubernetes that simplifies the
 process of obtaining, renewing, managing and using those certificates. It ensures that
 certificates are valid and up to date, and attempts to renew certificates at a
 configured time before expiry. cert-manager also facilitates issuing certificates from a
 variety of supported sources, including [AWS Certificate Manager Private Certificate Authority](https://aws.amazon.com/private-ca/ "https://aws.amazon.com/private-ca/").


We recommend that you review best practices for management of TLS certificates on
 your clusters and advise you to opt in to cert-manager for production environments. Note
 that if you opt-in to enabling cert-manager for managing the admission webhook TLS
 certificates, you are required to pre-install cert-manager on your Amazon EKS cluster before
 you install the Amazon CloudWatch Observability EKS add-on or the Helm chart. For more
 information about available installation options, see  [cert-manager documentation](https://cert-manager.io/docs/installation/ "https://cert-manager.io/docs/installation/").
 After you install it, you can opt in to using cert-manager for managing the admission
 webhook TLS certificates using the following additional configuration.



* If you are using the Amazon CloudWatch Observability EKS add-on



```

--configuration-values '{ "admissionWebhooks": { "certManager": { "enabled": true } } }'

```
* If you are using the Helm chart



```

--set admissionWebhooks.certManager.enabled=true

```


```

--configuration-values '{ "admissionWebhooks": { "certManager": { "enabled": true } } }'

```

The advanced configuration discussed in this section will by default use a  [SelfSigned](https://cert-manager.io/docs/configuration/selfsigned/ "https://cert-manager.io/docs/configuration/selfsigned/")
 issuer.


### Collect Amazon EBS volume
 IDs


If you want to collect Amazon EBS volume IDs in the performance logs, you must add
 another policy to the IAM role that is attached to the worker nodes or to the service
 account. Add the following as an inline policy. For more information, see  [Adding and
 Removing IAM Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").



JSON





```

`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Action": [
 "ec2:DescribeVolumes"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```





## Collect Java
 Management Extensions (JMX) metrics


The CloudWatch agent supports Java Management Extensions (JMX) metrics collection on Amazon EKS.
 This allows you to collect additional metrics from Java applications running on Amazon EKS
 clusters enabling insight into performance, memory usage, traffic, and other critical
 metrics. For more information, see [Collect Java Management Extensions (JMX)
 metrics](CloudWatch-Agent-JMX-metrics.md "CloudWatch-Agent-JMX-metrics.md").


## Enable Kueue metrics


Beginning with version `v2.4.0-eksbuild.1` of the the CloudWatch Observability
 EKS add-on, Container Insights for Amazon EKS supports collecting Kueue metrics from Amazon EKS
 clusters. For more information about these metrics, see [Kueue metrics](Container-Insights-metrics-EKS.md#Container-Insights-metrics-Kueue "Container-Insights-metrics-EKS.md#Container-Insights-metrics-Kueue") .


If you are using the Amazon SageMaker AI Hyperpod Task Governance EKS add-on, you
 can skip the steps in the **Prerequisites** section and just follow the
 steps in [Enable the configuration flag](#enable-Kueue-metrics-flag "#enable-Kueue-metrics-flag").


### Prerequisites


Before you install Kueue in your Amazon EKS cluster, make the following updates in the
 manifest file:



1. Enable the optional cluster queue resource metrics for Kueue. To do this, modify
 the in-line `controller_manager_config.yaml` in the
 `kueue-system` ConfigMap. In the `metrics` section, add or
 uncomment the line `enableClusterQueueResources: true`.



```

apiVersion: v1
data:
controller_manager_config.yaml: |
apiVersion: config.kueue.x-k8s.io/v1beta1
kind: Configuration
health:
healthProbeBindAddress: :8081
metrics:
bindAddress: :8080
enableClusterQueueResources: true `<-- ADD/UNCOMMENT THIS LINE`

```
2. By default, all `k8s` services are available cluster-wide. Kueue
 creates a service `kueue-controller-manager-metrics-service` for exposing
 metrics. To prevent duplicate observations for metrics, modify this service to allow
 access only to the metrics service from the same node. To do this, add the line
 `internalTrafficPolicy: Local` to the
 `kueue-controller-manager-metrics-service` definition.



```

apiVersion: v1
kind: Service
metadata:
labels:
...
name: kueue-controller-manager-metrics-service
namespace: kueue-system
spec:
ports:

- name: https
  port: 8443
  protocol: TCP
  targetPort: https
  internalTrafficPolicy: Local `<-- ADD THIS LINE`
  selector:
  control-plane: controller-manager

```
3. Lastly, the `kueue-controller-manager` pod creates a
 `kube-rbac-proxy` container. This container currently has a high level
 of logging verbosity, which causes the cluster's bearer token to be logged by that
 container when the metrics scraper accesses the
 `kueue-controller-manager-metrics-service`. We recommend that you
 decrease this logging verbosity. The default value in the manifest distributed by
 Kueue is 10, we recommend to change it to 0.



```

apiVersion: apps/v1
kind: Deployment
metadata:
labels:
...
name: kueue-controller-manager
namespace: kueue-system
spec:
...
template:
...
spec:
containers:
... - args: - --secure-listen-address=0.0.0.0:8443 - --upstream=http://127.0.0.1:8080/ - --logtostderr=true - --v=0 `<-- CHANGE v=10 TO v=0`
image: gcr.io/kubebuilder/kube-rbac-proxy:v0.8.0
name: kube-rbac-proxy
...

```

### Enable the configuration flag


To enable the Kueue metrics, you must enable `kueue_container_insights`
 in the add-on additional configuration. You can do this either by using the AWS CLI to set
 up the EKS Observability add-on, or by using the Amazon EKS console.


After you have successfully installed the EKS Observability add-on with one of the
 following methods, you can view your Amazon EKS cluster metrics under the HyperPod console
 **Dashboard** tab.



AWS CLI
###### To enable Kueue metrics using the AWS CLI

* Enter the following AWS CLI command to install the add-on.



```

aws eks create-addon --cluster-name `cluster-name` --addon-name amazon-cloudwatch-observability --configuration-values "`configuration_json_file`"

```

The following is an example of the JSON file with the configuration
 values.



```

{
"agent": {
"config": {
"logs": {
"metrics_collected": {
"kubernetes": {
"kueue_container_insights": true,
"enhanced_container_insights": true
},
"application_signals": { }
}
},
"traces": {
"traces_collected": {
"application_signals": { }
}
}
},
},
}

```


Amazon EKS console
###### To enable Kueue metrics using the Amazon EKS console

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose the name of your cluster.
3. Choose **Add-ons**.
4. Find the **Amazon CloudWatch Observability** add-on in
 the list, and install it. When you do so, choose **Optional
 configuration** and include the following JSON configuration
 values.



```

{
"agent": {
"config": {
"logs": {
"metrics_collected": {
"kubernetes": {
"kueue_container_insights": true,
"enhanced_container_insights": true
},
"application_signals": { }
}
},
"traces": {
"traces_collected": {
"application_signals": { }
}
}
},
},
}

```



## Appending
 OpenTelemetry collector configuration files


The CloudWatch agent supports supplemental OpenTelemetry collector configuration files
 alongside its own configuration files. This feature allows you to use CloudWatch agent features
 such as CloudWatch Application Signals or Container Insights through the CloudWatch agent configuration and
 bring in your existing OpenTelemetry collector configuration with a single agent.


To prevent merge conflicts with pipelines automatically created by CloudWatch agent, we
 recommend that you add a custom suffix to each of the components and pipelines in your
 OpenTelemetry collector configuration. This will prevent clashing and merge
 conflicts.



* If you are using the Amazon CloudWatch Observability EKS add-on



```

--configuration-values file://values.yaml

```

or



```

--configuration-values '
agent:
otelConfig:
receivers:
otlp/custom-suffix:
protocols:
http: {}
exporters:
awscloudwatchlogs/custom-suffix:
log_group_name: "test-group"
log_stream_name: "test-stream"
service:
pipelines:
logs/custom-suffix:
receivers: [otlp/custom-suffix]
exporters: [awscloudwatchlogs/custom-suffix]
'

```
* If you are using the Helm chart



```

--set agent.otelConfig='
receivers:
otlp/custom-suffix:
protocols:
http: {}
exporters:
awscloudwatchlogs/custom-suffix:
log_group_name: "test-group"
log_stream_name: "test-stream"
service:
pipelines:
logs/custom-suffix:
receivers: [otlp/custom-suffix]
exporters: [awscloudwatchlogs/custom-suffix]
'

```

## Enabling APM through Application Signals for your Amazon EKS cluster


By default, OpenTelemetry (OTEL) based Application Performance Monitoring (APM) is enabled through Application Signals when installing either the
 CloudWatch Observability EKS add-on (V5.0.0 or greater) or the Helm chart. You can further customize specific settings using the advanced configuration for the Amazon EKS add-on or by overriding values with the Helm chart.


###### Note

If you use any OpenTelemetry (OTEL) based APM solution, enabling Application Signals affects your existing observability setup. Review your current implementation before proceeding.
 To maintain your existing APM setup after upgrading to V5.0.0 or later, see [Opt out of Application Signals](#Opting-out-App-Signals "#Opting-out-App-Signals").


**Application Signals Auto monitor**


Version 5.0.0 of the CloudWatch Observability Amazon EKS add-on and Helm chart introduces new
 functionality. You can now automatically enable Application Signals for all or specific
 service workloads in your EKS cluster through the Auto monitor configuration. The
 following `autoMonitor` settings can be specified within the
 `applicationSignals` section under the `manager` section of the
 advanced configuration.



* *monitorAllServices* – A boolean flag to enable (true)
 or disable (false) monitoring of all service workloads by Auto monitor. Defaults to
 true. Enabling this flag will ensure that all Kubernetes workloads (Deployments,
 DaemonSets, and StatefulSets) in the cluster that are mapped to a Kubernetes Service
 will be in scope for automatic enablement of Application Signals when they are brought
 up for the first time (or when restarted for existing workloads). The system excludes
 workloads in the `kube-system` and `amazon-cloudwatch`
 namespaces by default.
* *languages*  – A list of strings specifying the set of
 languages that Application Signals will try to automatically instrument your services
 with, when `monitorAllServices` is enabled. Defaults to all the [supported languages](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md").
* *restartPods* – A boolean flag controls whether
 workloads restart after configuration changes. Defaults to false. Enabling this flag
 to `true` controls whether Kubernetes workloads within Auto monitor scope
 restart automatically when saving configuration changes. Any settings on your
 Kubernetes workloads that influence the restart of the pods such as
 `updateStrategy` will be considered. Consider that restarting may cause
 service downtime.
* *customSelector* – Settings to select specific
 Kubernetes namespaces or workloads for Auto monitor.




	+ *java* – Specify workloads to automatically
	 instrument with Java
	+ *python* – Specify workloads to automatically
	 instrument with Python
	+ *nodejs* – Specify workloads to automatically
	 instrument with Node.js
	+ *dotnet* – Specify workloads to automatically
	 instrument with .NET
For each of the languages above, the following fields can be configured.




	+ *namespaces* – A list of strings specifying the
	 namespaces to be selected. Defaults to an empty list, that is []
	+ *deployments* – A list of strings specifying the
	 deployments to be selected. Specify in `namespace/deployment`format.
	 Defaults to an empty list, that is []
	+ *daemonsets* – A list of strings specifying the
	 daemonsets to be selected. Specify in `namespace/daemonset` format.
	 Defaults to an empty list, that is []
	+ *statefulsets* – A list of strings specifying the
	 statefulsets to be selected. Specify in `namespace/statefulset` format.
	 Defaults to an empty list, that is []
* *exclude* – Settings to exclude specific Kubernetes
 namespaces or workloads from Auto monitor. Excluding a workload takes precedence when
 the same workload is also within scope of `monitorAllServices` or
 `customSelector`.




	+ *java* – Specify workloads to exclude from being
	 automatically instrumented with Java
	+ *python* – Specify workloads to exclude from being
	 automatically instrumented with Python
	+ *nodejs* – Specify workloads to exclude from being
	 automatically instrumented with Node.js
	+ *dotnet* – Specify workloads to exclude from being
	 automatically instrumented with .NET
For each of the languages above, the following fields can be configured.




	+ *namespaces* – A list of strings specifying the
	 namespaces to be excluded. Defaults to an empty list, that is []
	+ *deployments* – A list of strings specifying the
	 deployments to be excluded. Specify in `namespace/deployment`format.
	 Defaults to an empty list, that is []
	+ *daemonsets* – A list of strings specifying the
	 daemonsets to be excluded. Specify in `namespace/daemonset` format.
	 Defaults to an empty list, that is []
	+ *statefulsets* – A list of strings specifying the
	 statefulsets to be excluded. Specify in `namespace/statefulset` format.
	 Defaults to an empty list, that is []

The following is an example configuration that automatically enables Application
 Signals for all existing and new service workloads on the cluster.



```

manager:
applicationSignals:
autoMonitor:
monitorAllServices: true
restartPods: true

```

The following is an example configuration that automatically enables Application
 Signals for any new service workload that is brought up and for any existing service
 workload that is explicitly restarted on the cluster.



```

manager:
applicationSignals:
autoMonitor:
monitorAllServices: true

```

The following is an example configuration that automatically enables Application
 Signals with Java for all existing and new pods corresponding to a workload in the
 `pet-warehouse` namespace.



```

manager:
applicationSignals:
autoMonitor:
restartPods: true
customSelector:
java:
namespaces: ["pet-warehouse"]

```

The following is an example configuration that automatically enables Application
 Signals with Python for all existing and new service workloads in the cluster excluding
 the `pet-clinic` deployment.



```

manager:
applicationSignals:
autoMonitor:
monitorAllServices: true
languages: ["python"]
restartPods: true
exclude:
python:
deployments: ["pet-warehouse/pet-clinic"]

```

The following is an example configuration that automatically enables Application
 Signals with Java for all service workloads in the cluster except for the ones in the
 `python-apps` namespace and further enables Application Signals with Python
 specifically for the `sample-python-app` deployment in the
 `python-apps` namespace.



```

manager:
applicationSignals:
autoMonitor:
monitorAllServices: true
languages: ["java"]
restartPods: true
customSelector:
python:
deployments: ["python-apps/sample-python-app"]
exclude:
java:
namespaces: ["python-apps"]

```

## Troubleshooting the
 Amazon CloudWatch Observability EKS add-on or the Helm chart


Use the following information to help troubleshoot problems with the Amazon CloudWatch
 Observability EKS add-on or the Helm chart


###### Topics

* [Updating and deleting the Amazon CloudWatch
 Observability EKS add-on or the Helm chart](#EKS-addon-troubleshoot-update "#EKS-addon-troubleshoot-update")
* [Verify the version of the CloudWatch agent
 used by the Amazon CloudWatch Observability EKS add-on or the Helm chart](#EKS-addon-troubleshoot-version "#EKS-addon-troubleshoot-version")
* [Handling a ConfigurationConflict when
 managing the add-on or the Helm chart](#EKS-addon-troubleshoot-conflict "#EKS-addon-troubleshoot-conflict")

### Updating and deleting the Amazon CloudWatch
 Observability EKS add-on or the Helm chart


For instructions about updating or deleting the Amazon CloudWatch Observability EKS add-on,
 see [Managing Amazon EKS add-ons](../../../eks/latest/userguide/managing-add-ons.md "../../../eks/latest/userguide/managing-add-ons.md"). Use `amazon-cloudwatch-observability` as
 the name of the add-on.


To delete the Helm chart in a cluster, enter the following command.



```

helm delete amazon-cloudwatch-observability -n amazon-cloudwatch --wait

```

### Verify the version of the CloudWatch agent
 used by the Amazon CloudWatch Observability EKS add-on or the Helm chart


The Amazon CloudWatch Observability EKS add-on and the Helm chart installs a custom resource
 of kind `AmazonCloudWatchAgent` that controls the behavior of the CloudWatch agent
 daemonset on the cluster, including the version of the CloudWatch agent being used. You can
 get a list of all the `AmazonCloudWatchAgent` custom resources installed on
 your cluster u by entering the following command:



```

kubectl get amazoncloudwatchagent -A

```

In the output of this command, you should be able to check the version of the CloudWatch
 agent. Alternatively, you can also describe the `amazoncloudwatchagent`
 resource or one of the `cloudwatch-agent-*` pods running on your cluster to
 inspect the image being used.


### Handling a ConfigurationConflict when
 managing the add-on or the Helm chart


When you install or update the Amazon CloudWatch Observability EKS add-on or the Helm chart,
 if you notice a failure caused by existing resources, it is likely because you already
 have the CloudWatch agent and its associated components such as the ServiceAccount, the
 ClusterRole and the ClusterRoleBinding installed on the cluster.


The error displayed by the add-on will include `Conflicts found when
 trying to apply. Will not continue due to resolve conflicts mode`,


The error displayed by the Helm chart will be similar to `Error:
 INSTALLATION FAILED: Unable to continue with install and invalid ownership
 metadata.`.


When the add-on or the Helm chart tries to install the CloudWatch agent and its associated
 components, if it detects any change in the contents, it by default fails the
 installation or update to avoid overwriting the state of the resources on the
 cluster.


If you are trying to onboard to the Amazon CloudWatch Observability EKS add-on and you see
 this failure, we recommend deleting an existing CloudWatch agent setup that you had previously
 installed on the cluster and then installing the EKS add-on or Helm chart. Be sure to
 back up any customizations you might have made to the original CloudWatch agent setup such as
 a custom agent configuration, and provide these to the add-on or Helm chart when you
 next install or update it. If you had previously installed the CloudWatch agent for onboarding
 to Container Insights, see [Deleting the CloudWatch agent and Fluent Bit
 for Container Insights](ContainerInsights-delete-agent.md "ContainerInsights-delete-agent.md") for more information.


Alternatively, the add-on supports a conflict resolution configuration option that
 has the capability to specify `OVERWRITE`. You can use this option to proceed
 with installing or updating the add-on by overwriting the conflicts on the cluster. If
 you are using the Amazon EKS console, you'll find the **Conflict resolution
 method** when you choose the **Optional configuration
 settings** when you create or update the add-on. If you are using the AWS CLI,
 you can supply the `--resolve-conflicts OVERWRITE` to your command to create
 or update the add-on.


## Opt out of Application Signals


Fine-tune your service monitoring preferences in the CloudWatch console or with the SDK.


For versions before 5.0.0, to disable Application Signals auto-monitoring, follow the procedure below:


**Using CLI or SDK**


The following configuration can be applied either as an advanced configuration to the EKS add-on or as a values override when using the helm chart.



```

{
"manager": {
"applicationSignals": {
"autoMonitor": {
"monitorAllServices": false
}
}
}
}

```

Restart your services for the changes to take effect.


**Using the console**


Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").

1. In the navigation pane, under **Application Signals (APM)**, choose **Services**.
2. Choose **Enable Application Signals** to view the enablement page.
3. Clear the **Auto-Monitor** checkbox for each service you don't want to monitor.
4. Restart your services for the changes to take effect.
```
