# Install the EKS AWS Network Flow Monitor Agent add-on

Follow the steps in this section to install the AWS Network Flow Monitor Agent add-on for Amazon Elastic Kubernetes Service (Amazon EKS), to send
Network Flow Monitor metrics to the Network Flow Monitor backend from Kubernetes clusters. After you
complete the steps, AWS Network Flow Monitor Agent pods will be running on all of your Kubernetes cluster nodes.

If you use self-managed Kubernetes clusters, the installation steps to follow are in the previous section:
[Install agents for self-managed Kubernetes instances](CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks.md "CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks.md").

Be aware that Customer Managed prefix lists
[Customer Managed prefix lists](../../../vpc/latest/userguide/working-with-managed-prefix-lists.md "../../../vpc/latest/userguide/working-with-managed-prefix-lists.md") are not supported for Network Flow Monitor.

You can install the add-on by using the console or by using API commands with the AWS Command Line Interface.

###### Contents

- [Prerequisites for installing the add-on](#CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-prereq "#CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-prereq")
- [Install the add-on by using the console](#CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-console "#CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-console")
- [Install the add-on by using the CLI](#CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-cli "#CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-cli")
- [Configure for third party tools](CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party.md "CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party.md")

## Prerequisites for installing the add-on

Regardless of whether you use the console or the CLI to install the AWS Network Flow Monitor
Agent add-on, there are several requirements for installing the add-on with Kubernetes.

**Ensure that your version of Kubernetes is supported**
Network Flow Monitor agent installation requires Kubernetes Version 1.25, or a more recent version.

**Amazon EKS Pod Identity Agent add-on installation**
You can install the Amazon EKS Pod Identity Agent add-on in the console or by using the CLI.

Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that
Amazon EC2 instance profiles provide credentials to Amazon EC2 instances. Amazon EKS Pod Identity provides credentials to your
workloads with an additional Amazon EKS Auth API and an agent pod that runs on each node.

To learn more and see the steps for installing the Amazon EKS Pod Identity add-on, see [Set up the Amazon EKS Pod Identity Agent](../../../eks/latest/userguide/pod-id-agent-setup.md "../../../eks/latest/userguide/pod-id-agent-setup.md") in the Amazon EKS User Guide.

## Install the AWS Network Flow Monitor Agent add-on

by using the console

Follow the steps in this section to install and configure the AWS Network Flow Monitor Agent add-on
in the Amazon EKS console.

If you have already installed the add-on and have issues upgrading to a new version,
see [Troubleshoot issues in EKS agents installation](CloudWatch-NetworkFlowMonitor-troubleshooting.md#CloudWatch-NetworkFlowMonitor-troubleshooting.ec2-agent-installation "CloudWatch-NetworkFlowMonitor-troubleshooting.md#CloudWatch-NetworkFlowMonitor-troubleshooting.ec2-agent-installation").

Before you begin, make sure that you have installed the Amazon EKS Pod Identity Agent add-on. For more information,
see the [previous section](#NFMPodIdentity "#NFMPodIdentity").

###### To install the add-on using the console

1. In the AWS Management Console, navigate to the Amazon EKS console.
2. On the page for installing add-ons, in the list of add-ons, choose **AWS Network Flow Monitor Agent**.
3. Configure the add-on settings.
   1. For **Add-on access**, choose **EKS Pod Identity**.
   2. For the IAM role to use with the add-on, use a role that has the following AWS managed policy attached:
      [CloudWatchNetworkFlowMonitorAgentPublishPolicy](../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.md "../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.md"). This policy gives permission for an agent to send telemetry
      reports to the Network Flow Monitor endpoint. If you don't already have a role with the policy attached, create a role by
      choosing **Create recommended role**, and following the steps in the IAM console.
   3. Choose **Next**.

4. On the **Review and add** page, make sure that the add-on configuration looks correct, and then
   choose **Create**.

## Install the AWS Network Flow Monitor Agent add-on

by using the AWS Command Line Interface

Follow the steps in this section to install the AWS Network Flow Monitor Agent add-on for Amazon EKS by using the AWS Command Line Interface.

**1. Install the EKS Pod Identity Agent add-on**
Before you begin, make sure that you have installed the Amazon EKS Pod Identity Agent add-on. For more information,
see the [earlier section](#NFMPodIdentity "#NFMPodIdentity").

**2. Create the required IAM role**
The AWS Network Flow Monitor Agent add-on must have permission to send metrics to the Network Flow Monitor
backend. You must attach a role with the required permissions when you create the add-on. Create a role that has
the following AWS managed policy attached:
[CloudWatchNetworkFlowMonitorAgentPublishPolicy](../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.md "../../../aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorAgentPublishPolicy.md"). You need the ARN of this IAM role to
install the add-on.

**3. Install the AWS Network Flow Monitor Agent add-on**

To install the AWS Network Flow Monitor Agent add-on for your cluster, run the following command:

`aws eks create-addon --cluster-name `CLUSTER NAME`--addon-name aws-network-flow-monitoring-agent --region
`AWS REGION` --pod-identity-associations serviceAccount=aws-network-flow-monitor-agent-service-account,roleArn=`IAM ROLE ARN``

The result should be similar to the following:

```
{
    "addon": {
        "addonName": "aws-network-flow-monitoring-agent",
        "clusterName": "ExampleClusterName",
        "status": "CREATING",
        "addonVersion": "v1.0.0-eksbuild.1",
        "health": {
            "issues": []
        },
        "addonArn": "arn:aws:eks:us-west-2:000000000000:addon/ExampleClusterName/aws-network-flow-monitoring-agent/eec11111-bbbb-EXAMPLE",
        "createdAt": "2024-10-25T16:38:07.213000+00:00",
        "modifiedAt": "2024-10-25T16:38:07.240000+00:00",
        "tags": {},
         "podIdentityAssociations": [
            "arn:aws:eks:us-west-2:000000000000:podidentityassociation/ExampleClusterName/a-3EXAMPLE5555555"
         ]
    }
  }
```

**4. Make sure that the add-on is active**
Review the installed AWS Network Flow Monitor Agent add-on to ensure that it's active for your cluster. Run the following command to verify
that the status is `ACTIVE`:

`aws eks describe-addon --cluster-name `CLUSTER NAME`--addon-name aws-network-flow-monitoring-agent --region
`AWS REGION``

The result should be similar to the following:

```
{
    "addon": {
        "addonName": "aws-network-flow-monitoring-agent",
        "clusterName": "ExampleClusterName",
        "status": "ACTIVE",
        "addonVersion": "v1.0.0-eksbuild.1",
        "health": {
            "issues": []
        },
        "addonArn": "arn:aws:eks:us-west-2:000000000000:addon/ExampleClusterName/aws-network-flow-monitoring-agent/eec11111-bbbb-EXAMPLE",
        "createdAt": "2024-10-25T16:38:07.213000+00:00",
        "modifiedAt": "2024-10-25T16:38:07.240000+00:00",
        "tags": {},
         "podIdentityAssociations": [
            "arn:aws:eks:us-west-2:000000000000:podidentityassociation/ExampleClusterName/a-3EXAMPLE5555555"
         ]
    }
  }
```
