**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable EKS zonal shift to avoid impaired Availability Zones

Amazon Application Recovery Controller (ARC) helps you manage and coordinate recovery for your applications across Availability Zones (AZs) and works with many services, including Amazon EKS. With EKS support for ARC zonal shift, you can shift in-cluster network traffic away from an impaired AZ. You can also authorize AWS to monitor the health of your AZs and temporarily shift network traffic away from an unhealthy AZ on your behalf.

**How to use EKS zonal shift:**

1. Enable your EKS cluster with Amazon Application Recovery Controller (ARC). This is done at the cluster level using the Amazon EKS Console, the AWS CLI, CloudFormation, or eksctl.
2. Once enabled, you can manage zonal shifts or zonal autoshifts using the ARC Console, the AWS CLI, or the zonal shift and zonal autoshift APIs.
   Note that after you register an EKS cluster with ARC, you still need to configure ARC. For example, you can use the ARC console to configure zonal autoshift.

For more detailed information about how EKS zonal shift works, and how to design your workloads to handle impaired availability zones, see [Learn about Amazon Application Recovery Controller (ARC) zonal shift in Amazon EKS](zone-shift.md "zone-shift.md").

## Considerations

- EKS Auto Mode does not support Amazon Application Recovery Controller, zonal shift, and zonal autoshift.
- We recommend waiting at least 60 seconds between zonal shift operations to ensure proper processing of each request.

When attempting to perform zonal shifts in quick succession (within 60 seconds of each other), the Amazon EKS service may not properly process all shift requests. This is due to the current polling mechanism that updates the cluster’s zonal state. If you need to perform multiple zonal shifts, ensure there is adequate time between operations for the system to process each change.

## What is Amazon Application Recovery Controller?

Amazon Application Recovery Controller (ARC) helps you prepare for and accomplish faster recovery for applications running on AWS. Zonal shift enables you to quickly recover from Availability Zone (AZ) impairments, by temporarily moving traffic for a supported resource away from an AZ, to healthy AZs in the AWS Region.

[Learn more about Amazon Application Recovery Controller (ARC)](../../../r53recovery/latest/dg/what-is-route53-recovery.md "../../../r53recovery/latest/dg/what-is-route53-recovery.md")

## What is zonal shift?

Zonal shift is a capability in ARC that allows you to move traffic for a resource like an EKS cluster or an Elastic Load Balancer away from an Availability Zone in an AWS Region to quickly mitigate an issue and quickly recover your application. You might choose to shift traffic, for example, because a bad deployment is causing latency issues, or because the Availability Zone is impaired. A zonal shift requires no advance configuration steps.

[Learn more about ARC zonal shift](../../../r53recovery/latest/dg/arc-zonal-shift.md "../../../r53recovery/latest/dg/arc-zonal-shift.md")

## What is zonal autoshift?

Zonal autoshift is a capability in ARC that you can enable to authorize AWS to shift traffic away from an AZ for supported resources, on your behalf, to healthy AZs in the AWS Region. AWS starts an autoshift when internal telemetry indicates that there is an impairment in one AZ in a Region that could potentially impact customers. The internal telemetry incorporates metrics from multiple sources, including the AWS network, and the Amazon EC2 and Elastic Load Balancing services.

AWS ends autoshifts when indicators show that there is no longer an issue or potential issue.

[Learn more about ARC zonal autoshift](../../../r53recovery/latest/dg/arc-zonal-autoshift.md "../../../r53recovery/latest/dg/arc-zonal-autoshift.md")

## What does EKS do during an autoshift?

EKS updates networking configurations to avoid directing traffic to impaired AZs. Additionally, if you are using Managed Node Groups, EKS will only launch new nodes in the healthy AZs during a zonal shift. When the shift expires or gets cancelled, the networking configurations will be restored to include the AZ that was previously detected as unhealthy.

[Learn more about EKS zonal shift](zone-shift.md "zone-shift.md").

## Register EKS cluster with Amazon Application Recovery Controller (ARC) (AWS console)

1. Find the name and region of the EKS cluster you want to register with ARC.
2. Navigate to the [EKS console](https://console.aws.amazon.com/eks "https://console.aws.amazon.com/eks") in that region, and select your cluster.
3. On the **Cluster info** page, select the **Overview** tab.
4. Under the **Zonal shift** heading, select the **Manage** button.
5. Select **enable** or **disable** for _EKS zonal shift_.

Now your EKS cluster is registered with ARC.

If you want AWS to detect and avoid impaired availability zones, you need to configure ARC zonal autoshift. For example, you can do this in the ARC console.

## Next Steps

- Learn how to [enable zonal autoshift](../../../r53recovery/latest/dg/arc-zonal-autoshift.md "../../../r53recovery/latest/dg/arc-zonal-autoshift.md").
- Learn how to manually [start a zonal shift](../../../r53recovery/latest/dg/arc-zonal-shift.md "../../../r53recovery/latest/dg/arc-zonal-shift.md").
