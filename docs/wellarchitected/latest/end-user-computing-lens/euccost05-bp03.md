# EUCCOST05-BP03 Rightsize your EUC resources

Choosing the right Amazon WorkSpaces bundle or Amazon WorkSpaces Applications instance type for your EUC
workloads is important to operate your EUC environment in a cost-effective manner. The
chosen configuration needs to support the hardware requirements of your applications, while
at the same time avoiding over-provisioning resources.

Capture metrics in an existing reference environment (physical
machines or virtual desktops) to understand how the existing
resources are being used. This data helps you choose the right
bundles and instance types with AWS EUC services. To capture
these metrics, use tools like
[Microsoft
Performance Monitor](https://techcommunity.microsoft.com/t5/ask-the-performance-team/windows-performance-monitor-overview/ba-p/375481 "https://techcommunity.microsoft.com/t5/ask-the-performance-team/windows-performance-monitor-overview/ba-p/375481") or third-party solutions like

[Liquidware
Stratusphere UX](https://www.liquidware.com/products/stratusphere-ux "https://www.liquidware.com/products/stratusphere-ux") and

[Control-Up DX
solutions](https://www.controlup.com/ "https://www.controlup.com/").  

Once your workload is in production, continually monitor relevant metrics, helping you
react to changing requirements by adjusting the bundle and instance type.  [Monitor
your WorkSpaces health using the WorkSpaces CloudWatch automatic dashboard](../../../workspaces/latest/adminguide/cloudwatch-dashboard.md "../../../workspaces/latest/adminguide/cloudwatch-dashboard.md"), which provides
insight into the performance of your WorkSpaces resources and helps you identify performance
issues. [Amazon WorkSpaces Applications fleet usage, instance, and session Performance Metrics](../../../appstream2/latest/developerguide/monitoring.md "../../../appstream2/latest/developerguide/monitoring.md") are available in
the WorkSpaces Applications console and Amazon CloudWatch.

**Level of risk exposed if this best
practice is not established:** Medium

 

## Implementation guidance

AWS EUC services offer a variety of different bundles and instance types, including
GPU-enabled choices. Assuming you have captured and analyzed your metrics in an existing
reference environment, you can map your workloads to the most cost-effective Amazon WorkSpaces or
WorkSpaces Applications bundles and instance types. If you have use cases that require a GPU and are
heavily utilized (high number of hours per month), consider using WorkSpaces Applications, which gives you
a more granular choice of GPU-enabled instances. Use the [AWS Pricing Calculator](https://calculator.aws/#/ "https://calculator.aws/#/") or the [Amazon WorkSpaces Applications Pricing](https://aws.amazon.com/appstream2/pricing/?nc1=h_ls "https://aws.amazon.com/appstream2/pricing/?nc1=h_ls") tool to determine which of
the two solutions is more cost-effective for your specific workload.
