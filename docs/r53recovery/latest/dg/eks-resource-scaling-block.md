

# Amazon EKS resource scaling execution block
<a name="eks-resource-scaling-block"></a>

The EKS resource scaling execution block enables you to scale EKS resources as part of your multi-Region recovery process. When you configure the execution block, you define a percentage of capacity to scale, relative to the capacity in the Region that is being deactivated. 

## Configure EKS access entry permissions
<a name="eks-resource-scaling-block-permissions"></a>

Before you can add a step for EKS resource scaling, you must provide Region switch with the necessary permissions to take actions with the Kubernetes resources in your EKS clusters. To provide access for Region switch, you must create an EKS access entry for the IAM role that Region switch uses for plan execution, by using the following Region switch access policy: `arn:aws:eks::aws:cluster-access-policy/AmazonARCRegionSwitchScalingPolicy`

### Region switch EKS access policy
<a name="eks-resource-scaling-block-permissions.policy"></a>

The following information provides details about the EKS access policy.

**Name:** `AmazonARCRegionSwitchScalingPolicy`

**Policy ARN:** `arn:aws:eks::aws:cluster-access-policy/AmazonARCRegionSwitchScalingPolicy`


| Kubernetes API groups | Kubernetes resources | Kubernetes verbs (permissions) | 
| --- | --- | --- | 
| \* | \*/scale | get, update | 
| \* | \*/status | get | 
| autoscaling | horizontalpodautoscalers | get, patch | 

### Create an EKS access entry for Region switch
<a name="eks-resource-scaling-block-permissions.create"></a>

The following example describes how to create the required access entry and access policy associations so that Region switch can take specific actions for your Kubernetes resources. In this example, the permissions apply to the namespace {{my-namespace1}} in the EKS cluster {{my-cluster}} for the IAM role `arn:aws:iam::555555555555:role/{{my-role}}`. 

When you configure these permissions, make sure that you take these steps for both EKS clusters in your execution block.

**Prerequisite**  
Before you get started, change the authentication mode of the cluster to either `API_AND_CONFIG_MAP` or `API`. Changing the authorization mode adds the API for access entries. For more information, see [Change authentication mode to use access entries](https://docs.aws.amazon.com/eks/latest/userguide/setting-up-access-entries.html) in the Amazon EKS User Guide.

**Create the access entry**  
The first step is to create the access entry by using an AWS CLI command similar to the following:  

```
aws eks create-access-entry --cluster-name {{my-cluster}} --principal-arn
									arn:aws:iam::555555555555:user/{{my-user}} --type STANDARD
```
For more information, see [Create access entries](https://docs.aws.amazon.com/eks/latest/userguide/creating-access-entries.html) in the Amazon EKS User Guide.

**Create the access entry association**  
Next, create the association to the Region switch access policy by using an AWS CLI command similar to the following:  

```
aws eks associate-access-policy --cluster-name {{my-cluster}} --principal-arn arn:aws:iam::555555555555:role/{{my-role}} \
										--access-scope type=namespace,namespaces={{my-namespace1}} --policy-arn
										arn:aws:eks::aws:cluster-access-policy/AmazonARCRegionSwitchScalingPolicy
```
For more information, see [Associate access policies with access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html) in the Amazon EKS User Guide.

Make sure to repeat these steps with the second EKS cluster in your execution block, in the other Region, to ensure that both clusters can be accessed by Region switch.

## Configuration
<a name="eks-resource-scaling-block-config"></a>

**Important**  
Before you add an EKS resource scaling step, first, make sure that you have the configured the correct permissions. For more information, see [Configure EKS access entry permissions](#eks-resource-scaling-block-permissions). Also make sure that you have the correct IAM policy in place. For more information, see [Amazon EKS resource scaling execution block sample policy](security_iam_region_switch_eks.md).

Note that Region switch currently supports the following ReplicaSet resources: apps/v1, Deployment, and apps/v1.

For the execution block configuration, enter the following values.

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Application name: **Enter the name of your EKS application for example, *myApplication*.

1. **Kubernetes resource kind: **Enter the resource kind for the application, for example, *Deployment*.

1. **Resource for *Region*: **For each Region, enter information for the EKS cluster, including the EKS cluster ARN, resource namespace, and so on.

1. **Percentage to match the activated Region's capacity: ** Enter the desired percentage of running pods in the source Region to match in the activated Region.

1. **Capacity monitoring approach: **The only option for capacity monitoring is already selected, **Max running capacity sampled over 24 hours**.

   This capacity monitoring approach uses the `ReplicaCount` value for EKS service requests. For more information, see [Learn about ARC zonal shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the Amazon Elastic Kubernetes Service User Guide.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

## How it works
<a name="eks-resource-scaling-block-how"></a>

During a plan execution, Region switch retrieves the sampled maximum number of replicas over the previous 24 hours for the target resource in the Region you're activating. Then, it computes the desired replica count for the destination resource by using the following formula: `ceil(percentToMatch * Source replica count)`

If the destination ready replica count is lower than the desired value, Region switch scales the destination resource replica value to the desired capacity. It waits for the replicas to become ready, leveraging your node auto-scaler to increase node capacity if necessary. 

If the optional `hpaName` field is not empty, Region switch patches the HorizontalPodAutoscaler to prevent any automatic scaledown during or after the execution by using the following patch: `{"spec":{"behavior":{"scaleDown":{"selectPolicy":"Disabled"}}}}` 

Make sure to configure any drift-correcting tool, such as GitOps tooling, to ignore the replica field for the resources in the patch, as well as the HorizontalPodAutoscaler field.