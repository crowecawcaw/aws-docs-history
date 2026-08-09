# Amazon EC2 managed instances

An _Amazon EC2 managed instance_ is an EC2 instance that is
provisioned and managed by a designated service provider. Managed instances provide a
simplified way for running compute workloads on Amazon EC2 by allowing you to delegate
operational control of the instance to a service provider.

Delegated control is the only change introduced for managed instances. The technical
specifications and billing remain the same as non-managed EC2 instances. Because managed
instances allow you to delegate control to the service provider, you can benefit from the
service provider’s operational expertise and best practices. When an instance is managed,
the service provider is responsible for tasks such as provisioning the instance, configuring
software, scaling capacity, handling instance failures and replacements, and terminating the
instance.

You can’t directly modify the settings of a managed instance or terminate it. The service
and specific operations are determined by the agreement between you and the service
provider. However, you can add, modify, or remove tags from your managed instances, allowing
you to categorize them within your AWS environment.

The following AWS services offer managed instances:

- [EKS Auto
  Mode](../../../eks/latest/userguide/automode.md "../../../eks/latest/userguide/automode.md")
- [Amazon ECS managed
  instances](../../../AmazonECS/latest/developerguide/ManagedInstances.md "../../../AmazonECS/latest/developerguide/ManagedInstances.md")
- [WorkSpaces Core managed
  instances](../../../workspaces-core/latest/pg/deploy-instances.md "../../../workspaces-core/latest/pg/deploy-instances.md")
- [Lambda managed
  instances](../../../lambda/latest/dg/lambda-managed-instances.md "../../../lambda/latest/dg/lambda-managed-instances.md")
- [Amazon EC2 Fast
  Launch](win-ami-config-fast-launch.md "win-ami-config-fast-launch.md")
- [Bedrock
  AgentCore runtime instances](../../../bedrock-agentcore/latest/devguide/runtime-instances-how-it-works.md "../../../bedrock-agentcore/latest/devguide/runtime-instances-how-it-works.md")

###### Contents

- [Billing for managed instances](#billing-for-ec2-managed-instances "#billing-for-ec2-managed-instances")
- [Identify managed instances](#identify-ec2-managed-instances "#identify-ec2-managed-instances")
- [Managed resource visibility settings](#managed-resource-visibility-settings "#managed-resource-visibility-settings")
- [Get started with managed instances](#get-started-with-ec2-managed-instances "#get-started-with-ec2-managed-instances")

## Billing for managed instances

An Amazon EC2 managed instance incurs the same base charge as a non-managed Amazon EC2 instance,
plus a separate fee for the service provider. This additional fee is charged by the
service provider managing your instance and is billed separately. It covers the cost of
services provided for operating and maintaining your managed instance.

All [Amazon EC2 purchasing options](instance-purchasing-options.md "instance-purchasing-options.md") are available for managed instances,
including On-Demand Instances, Reserved Instances, Spot Instances, and Savings Plans. By sourcing your compute directly from EC2
and then providing it to your service provider, you benefit from any existing Reserved Instances or
Savings Plans applied to your account, ensuring that you're using the most cost-effective
compute capacity available.

For example, when using Amazon EKS Auto Mode, you pay the standard EC2 instance rate for
the underlying instances, plus an additional charge from Amazon EKS for managing the
instances on your behalf. If you then decide to sign up for a [Savings Plans](../../../savingsplans/latest/userguide/what-is-savings-plans.md "../../../savingsplans/latest/userguide/what-is-savings-plans.md"), the EC2 instance rate is reduced by the Savings Plans, while
the additional charge from Amazon EKS remains unchanged.

## Identify managed instances

Managed instances are identified by a **true** value in the
**Managed** field. The service provider is identified in the
**Operator** field (in the console) or `Principal` field
(in the CLI).

Use the following procedures to identify managed instances.

Console

###### To identify a managed instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance you want to check.
4. On the **Details** tab (if you selected the
   checkbox) or in the summary area (if you selected the instance ID),
   find the **Managed** field.

   - A value of **true** indicates a managed
     instance.
   - A value of **false** indicates a
     non-managed instance.

5. If **Managed** is set to
   **true**, the **Operator**
   field displays a value identifying the service provider responsible
   for managing the instance. For example, a value of
   **eks.amazonaws.com** identifies Amazon EKS as the
   service provider.

AWS CLI

###### To identify a managed instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command and specify the instance
ID.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query Reservations[].Instances[].Operator
```

The following is example output. If `Managed` is
`true`, the instance is a managed instance and a
`Principal` is included. The principal is the service
provider that manages the instance. For example, a value of
`eks.amazonaws.com` identifies Amazon EKS as the service
provider.

```
[
    {
        "Managed": true,
        "Principal": "eks.amazonaws.com"
    }
]
```

###### To find your managed instances

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command and specify the
`operator.managed` filter with a value of
`true`. The `--query` option displays only the
IDs of the managed instances.

```
aws ec2 describe-instances \
    --filters "Name=operator.managed,Values=true" \
    --query Reservations[*].Instances[].InstanceId
```

PowerShell

###### To identify a managed instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

```
(Get-EC2Instance -InstanceId `i-1234567890abcdef0`).Instances.Operator
```

The following is example output.

```
Managed Principal
------- ---------
True    eks.amazonaws.com
```

###### To find your managed instances

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet. This example displays only the IDs of the managed instances.

```
(Get-EC2Instance -Filter @{Name="operator.managed"; Values="true"}).Instances.InstanceId
```

## Managed resource visibility settings

You can control whether resources that AWS services provision on your behalf
appear in your Amazon EC2 console views and API list operations.

### What is managed resource visibility?

AWS services such as Amazon EKS, Amazon ECS, WorkSpaces Core, AWS Lambda, and Amazon Bedrock
AgentCore provision and operate Amazon EC2 instances directly within your account. These
services assume responsibility for scaling, OS patches, security updates, and
lifecycle management. The resulting Amazon EC2 instances, Amazon EC2 launch templates, Amazon EBS
volumes, snapshots, and network interfaces (ENIs) appear alongside your
customer-managed resources in the Amazon EC2 console and APIs. Managed resource
visibility settings give you control over whether these managed resources surface
in your resource views.

### Affected resource types

| Resource type               | Services that provision these resources                                                                                                         | Description                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Amazon EC2 instances        | Amazon EKS worker nodes, Amazon ECS container instances, AWS Lambda execution<br>environments, Amazon WorkSpaces Core, Amazon Bedrock AgentCore | Primary resource type affected by visibility settings |
| Amazon EC2 launch templates | Amazon EKS, Amazon ECS, Amazon WorkSpaces Core, Amazon Bedrock AgentCore                                                                        | Launch templates created by managed services          |
| Amazon EBS volumes          | Amazon EKS, Amazon ECS, Amazon WorkSpaces Core, Amazon Bedrock AgentCore,<br>Amazon EC2 Fast Launch                                             | Volumes attached to managed instances                 |
| Amazon EBS snapshots        | Amazon EC2 Fast Launch                                                                                                                          | Snapshots managed by Amazon EC2 Fast Launch           |
| Network interfaces (ENIs)   | Amazon EKS, Amazon ECS, AWS Lambda, Amazon WorkSpaces Core, Amazon Bedrock<br>AgentCore                                                         | Network interfaces provisioned for managed workloads  |

###### Note

By default, Amazon EC2 hides managed resources for accounts that did not have managed resources before visibility settings became available. For accounts that already had managed resources, Amazon EC2 sets the visibility setting to **Visible** to preserve existing workflows. The visibility setting applies to all managed resources in a Region, regardless of when they were created. You can change visibility settings at any time.

### Why configure visibility settings

Configuring visibility settings lets you tailor how managed resources appear across
your operational tooling. Common use cases include:

- Simplify governance by reducing resource counts in compliance dashboards to
  only customer-managed resources.
- Reduce noise in observability tools that aggregate Amazon EC2 metrics across all
  instances in an account.
- Prevent false positives in cloud security posture management (CSPM)
  scanners (for example, Qualys) that flag managed resources as
  customer misconfigurations.
- With managed instances, AWS is responsible for the configuration,
  patching, and health of Amazon EC2 instances. By controlling visibility, you
  can better articulate the shared responsibility model to end users.

###### Note

Visibility settings control resource display in AWS console views and API
list operations. They do not affect billing, resource operation, or actual access
permissions. Hidden resources remain fully operational and billable.

### Configure managed resource visibility

You can configure the visibility of managed resources by using the Amazon EC2 console
or the AWS CLI.

Console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Dashboard**.
3. On the **Account attributes** card, under
   **Settings**, choose **Managed
   resources**.
4. Choose **Modify**.
5. Under **Default visibility**, choose one
   of the following options:

   - **Hidden (default)** – Hides
     all managed resources.
   - **Visible** – Shows all
     managed resources.

6. Choose **Modify visibility**.

AWS CLI

###### Get current visibility settings

Use the [get-managed-resource-visibility](../../../cli/latest/reference/ec2/get-managed-resource-visibility.md "../../../cli/latest/reference/ec2/get-managed-resource-visibility.md") command to retrieve the
current visibility configuration:

```
aws ec2 get-managed-resource-visibility
```

Example response:

```
{
    "visibility": {
        "defaultVisibility": "hidden"
    }
}
```

###### Hide all managed resources

Use the [modify-managed-resource-visibility](../../../cli/latest/reference/ec2/modify-managed-resource-visibility.md "../../../cli/latest/reference/ec2/modify-managed-resource-visibility.md") command to hide all
managed resources regardless of operator:

```
aws ec2 modify-managed-resource-visibility \
    --default-visibility "hidden"
```

### Discover hidden managed resources

When you turn off visibility, you can still access managed resources. The following
methods surface them on demand:

1. **Service-specific consoles**: Navigate to the
   respective AWS service console (for example, the Amazon EKS console) to view instances
   provisioned for that service. The service console provides full details on
   all resources the service manages in your account.
2. **Direct API queries**: Use the
   `describe-instances` API with a specific
   `instance-id` parameter. Direct queries with known instance IDs
   return results regardless of visibility settings. Visibility settings only
   affect list and filter operations. You can also use
   `describe-instances` with the
   `include-managed-resources` parameter to discover managed
   instances.

###### Note

The same direct-query-by-ID behavior applies to all affected resource types.
You can use `describe-volumes`, `describe-launch-templates`, and
`describe-network-interfaces` with specific resource IDs to access
hidden managed resources of those types.

### Billing considerations

Managed resource visibility settings have no effect on billing. Hidden managed
instances continue to appear in billing data because they are resources running
within your account, provisioned on your behalf, and remain fully billable regardless
of visibility configuration.

Hidden resources remain visible in:

- AWS bills
- AWS Cost and Usage Reports

###### Important

Managed instances are provisioned in your account and consume compute
resources. Hiding them from console views does not reduce costs. Review
service-specific billing documentation (for example, [Amazon EKS Pricing](https://aws.amazon.com/eks/pricing/ "https://aws.amazon.com/eks/pricing/"), [Amazon ECS Pricing](https://aws.amazon.com/ecs/pricing/ "https://aws.amazon.com/ecs/pricing/")) for details on managed instance
charges.

### Limitations

- Visibility settings apply to the entire account and affect all IAM
  principals uniformly.
- You cannot selectively show or hide managed resources by resource type
  or by the service that created them. For example, you cannot choose to
  show managed instances created by Amazon EKS while hiding those created by
  Lambda, Amazon ECS, or Amazon WorkSpaces.

## Get started with managed instances

To get started with managed instances, see the documentation for your preferred
service provider:

- [Automate cluster infrastructure
  with EKS Auto Mode](../../../eks/latest/userguide/automode.md "../../../eks/latest/userguide/automode.md") in the _Amazon EKS User
  Guide_
- [Amazon ECS managed
  instances](../../../AmazonECS/latest/developerguide/ManagedInstances.md "../../../AmazonECS/latest/developerguide/ManagedInstances.md") in the _Amazon ECS Developer
  Guide_
- [Deploy managed
  instances](../../../workspaces-core/latest/pg/deploy-instances.md "../../../workspaces-core/latest/pg/deploy-instances.md") in the _WorkSpaces Core
  Planning Guide_
- [Lambda managed
  instances](../../../lambda/latest/dg/lambda-managed-instances.md "../../../lambda/latest/dg/lambda-managed-instances.md") in the _Lambda Developer
  Guide_
- [Amazon EC2 Fast
  Launch](win-ami-config-fast-launch.md "win-ami-config-fast-launch.md") in this guide
- [Bedrock
  AgentCore runtime instances](../../../bedrock-agentcore/latest/devguide/runtime-instances-how-it-works.md "../../../bedrock-agentcore/latest/devguide/runtime-instances-how-it-works.md") in the _Amazon
  Bedrock AgentCore Developer Guide_
