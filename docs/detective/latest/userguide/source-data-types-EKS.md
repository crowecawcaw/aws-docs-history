# Amazon EKS audit logs

Amazon EKS audit logs is an optional data source package that can be added to your Detective behavior
graph. You can view the available optional source packages, and their status in your account,
from the **Settings** page in the console or through the Detective API.

A 30 day free trial is provided for this data source. To learn more see [Free trial for optional data sources](free-trial-overview.md#free-trial-datasource "free-trial-overview.md#free-trial-datasource").

Enabling Amazon EKS audit logs allows Detective to add in-depth information about resources created
with Amazon EKS to your behavior graph. This data source enhances the information provided about the
following entity types: EKS Cluster, Kubernetes Pod, Container Image and Kubernetes subject.

Additionally, If you have enabled EKS audit logs as a data source in Amazon GuardDuty you will be
able to see details for Kubernetes findings from GuardDuty. For more info on enabling this data
source in GuardDuty see [Kubernetes protection in
Amazon GuardDuty](../../../guardduty/latest/ug/kubernetes-protection.md "../../../guardduty/latest/ug/kubernetes-protection.md").

###### Note

This data source is enabled by default for new behavior graphs created after July 26, 2022.
For behavior graphs created before July 26, 2022 it must be enabled manually.

###### \*\*Adding or removing Amazon EKS audit logs as an optional data

source:\*\*

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. From the navigation panel under **Settings**, choose
   **General**.
3. Under **Source packages**, select **EKS audit logs** to
   enable this data source. If it is already enabled, select it again to stop ingesting
   **EKS audit logs** into your behavior graph.
