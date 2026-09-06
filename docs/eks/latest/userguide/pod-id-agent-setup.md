

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Set up the Amazon EKS Pod Identity Agent
<a name="pod-id-agent-setup"></a>

Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.

Amazon EKS Pod Identity provides credentials to your workloads with an additional *EKS Auth* API and an agent pod that runs on each node.

**Tip**  
You do not need to install the EKS Pod Identity Agent on EKS Auto Mode Clusters. This capability is built into EKS Auto Mode.

## Considerations
<a name="pod-id-agent-considerations"></a>
+ By default, the EKS Pod Identity Agent is pre-installed on EKS Auto Mode clusters. To learn more, see [Automate cluster infrastructure with EKS Auto Mode](automode.md).
+ By default, the EKS Pod Identity Agent listens on an `IPv4` and `IPv6` address for pods to request credentials. The agent uses the loopback (localhost) IP address `169.254.170.23` for `IPv4` and the localhost IP address `[fd00:ec2::23]` for `IPv6`.
+ If you disable `IPv6` addresses, or otherwise prevent localhost `IPv6` IP addresses, the agent can’t start. To start the agent on nodes that can’t use `IPv6`, follow the steps in [Disable `IPv6` in the EKS Pod Identity Agent](pod-id-agent-config-ipv6.md) to disable the `IPv6` configuration.

## Creating the Amazon EKS Pod Identity Agent
<a name="pod-id-agent-add-on-create"></a>

### Agent prerequisites
<a name="pod-id-agent-prereqs"></a>

**Important**  
The nodes where the EKS Pod Identity Agent runs must be able to access the EKS Auth API. If you are using private subnets for your nodes, you must set up an AWS PrivateLink interface endpoint for the EKS Auth API. For more information, see [Access Amazon EKS using AWS PrivateLink](vpc-interface-endpoints.md).
+ An existing Amazon EKS cluster. To deploy one, see [Get started with Amazon EKS](getting-started.md). The cluster version and platform version must be the same or later than the versions listed in [EKS Pod Identity cluster versions](pod-identities.md#pod-id-cluster-versions).
+ The node role has permissions for the agent to do the `AssumeRoleForPodIdentity` action in the EKS Auth API. You can use the [AWS managed policy: AmazonEKSWorkerNodePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksworkernodepolicy) or add a custom policy similar to the following:

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "eks-auth:AssumeRoleForPodIdentity"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

  This action can be limited by tags to restrict which roles can be assumed by pods that use the agent.
+ The nodes can reach and download images from Amazon ECR. The container image for the add-on is in the registries listed in [View Amazon container image registries for Amazon EKS add-ons](add-ons-images.md).

  Note that you can change the image location and provide `imagePullSecrets` for EKS add-ons in the **Optional configuration settings** in the AWS Management Console, and in the `--configuration-values` in the AWS CLI.

### Setup agent with AWS console
<a name="setup_agent_with_shared_aws_console"></a>

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. In the left navigation pane, select **Clusters**, and then select the name of the cluster that you want to configure the EKS Pod Identity Agent add-on for.

1. Choose the **Add-ons** tab.

1. Choose **Get more add-ons**.

1. Select the box in the top right of the add-on box for EKS Pod Identity Agent and then choose **Next**.

1. On the **Configure selected add-ons settings** page, select any version in the **Version** dropdown list.

1. (Optional) Expand **Optional configuration settings** to enter additional configuration. For example, you can provide an alternative container image location and `ImagePullSecrets`. The JSON Schema with accepted keys is shown in **Add-on configuration schema**.

   Enter the configuration keys and values in **Configuration values**.

1. Choose **Next**.

1. Confirm that the EKS Pod Identity Agent pods are running on your cluster.

   ```
   kubectl get pods -n kube-system | grep 'eks-pod-identity-agent'
   ```

   An example output is as follows.

   ```
   eks-pod-identity-agent-gmqp7                                          1/1     Running   1 (24h ago)   24h
   eks-pod-identity-agent-prnsh                                          1/1     Running   1 (24h ago)   24h
   ```

   You can now use EKS Pod Identity associations in your cluster. For more information, see [Assign an IAM role to a Kubernetes service account](pod-id-association.md).

### Setup agent with AWS CLI
<a name="setup_agent_with_shared_aws_cli"></a>

1. Run the following AWS CLI command. Replace `my-cluster` with the name of your cluster.

   ```
   aws eks create-addon --cluster-name my-cluster --addon-name eks-pod-identity-agent --addon-version v1.0.0-eksbuild.1
   ```
**Note**  
The EKS Pod Identity Agent doesn’t use the `service-account-role-arn` for *IAM roles for service accounts*. You must provide the EKS Pod Identity Agent with permissions in the node role.

1. Confirm that the EKS Pod Identity Agent pods are running on your cluster.

   ```
   kubectl get pods -n kube-system | grep 'eks-pod-identity-agent'
   ```

   An example output is as follows.

   ```
   eks-pod-identity-agent-gmqp7                                          1/1     Running   1 (24h ago)   24h
   eks-pod-identity-agent-prnsh                                          1/1     Running   1 (24h ago)   24h
   ```

   You can now use EKS Pod Identity associations in your cluster. For more information, see [Assign an IAM role to a Kubernetes service account](pod-id-association.md).