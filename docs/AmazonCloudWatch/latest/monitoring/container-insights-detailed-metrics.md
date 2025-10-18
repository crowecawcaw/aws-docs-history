# Container Insights with enhanced
 observability for Amazon EKS

On November 6, 2023, a new version of Container Insights was released. This version
 supports enhanced observability for Amazon EKS clusters running on Amazon EC2 and can collect more
 detailed metrics from these clusters. After installation, it automatically collects detailed
 infrastructure telemetry and container logs for your Amazon EKS clusters. You can then use curated,
 immediately usable dashboards to drill down into application and infrastructure telemetry. 

Container Insights with enhanced observability for Amazon EKS collects granular health,
 performance, and status metrics up to the container level, and also control plane metrics. For
 more information about the additional metrics and dimensions collected, see [Amazon EKS and Kubernetes Container
 Insights with enhanced observability metrics](Container-Insights-metrics-enhanced-EKS.md "Container-Insights-metrics-enhanced-EKS.md").

If you installed Container Insights by using the CloudWatch agent on an Amazon EKS cluster on Amazon EC2
 after November 6, 2023, you have Container Insights with enhanced observability for Amazon EKS.
 Otherwise, you can upgrade an Amazon EKS cluster to this new version by following the instructions
 in [Upgrading to Container Insights
 with enhanced observability for Amazon EKS in CloudWatch](Container-Insights-upgrade-enhanced.md "Container-Insights-upgrade-enhanced.md").

Container Insights supports CloudWatch cross-account observability. You use a single monitoring
 account to monitor and troubleshoot your applications that span multiple AWS accounts within
 a single Region. For more information, see [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

Container Insights with enhanced observability for Amazon EKS also supports Windows worker
 nodes.

Container Insights with enhanced observability for Amazon EKS is not supported on
 Fargate.

###### Note

You can find whether you have clusters that can be upgraded to Container Insights with
 enhanced observability for Amazon EKS by navigating to the Container Insights console. To do so,
 choose **Insights**, **Container Insights** in the
 navigation pane of the CloudWatch console. In the Container Insights console, a banner informs you
 if you have any Amazon EKS clusters that can be upgraded, and links to the upgrade page.
