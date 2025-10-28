# Amazon EC2 managed instances

An _Amazon EC2 managed instance_ is an EC2 instance that is
provisioned and managed by a designated service provider, such as Amazon EKS through [EKS Auto Mode](../../../eks/latest/userguide/automode.md "../../../eks/latest/userguide/automode.md").
Managed instances provide a simplified way for running compute workloads on Amazon EC2 by
allowing you to delegate operational control of the instance to a service provider.

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

###### Contents

- [Billing for managed instances](#billing-for-ec2-managed-instances "#billing-for-ec2-managed-instances")
- [Identify managed instances](#identify-ec2-managed-instances "#identify-ec2-managed-instances")
- [Get started with managed
  instances](#get-started-with-ec2-managed-instances "#get-started-with-ec2-managed-instances")

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

## Get started with managed

instances

For guidance on using managed instances, see [Automate cluster infrastructure with EKS
Auto Mode](../../../eks/latest/userguide/automode.md "../../../eks/latest/userguide/automode.md") in the _Amazon EKS User Guide_.
