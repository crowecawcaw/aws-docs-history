**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# View costs by Pod in AWS billing with split cost allocation

## Cost monitoring using AWS split cost allocation data for Amazon EKS

You can use AWS split cost allocation data for Amazon EKS to get granular cost visibility for your Amazon EKS clusters. This enables you to analyze, optimize, and chargeback cost and usage for your Kubernetes applications. You allocate application costs to individual business units and teams based on Amazon EC2 CPU and memory resources consumed by your Kubernetes application. Split cost allocation data for Amazon EKS gives visibility into cost per Pod, and enables you to aggregate the cost data per Pod using namespace, cluster, and other Kubernetes primitives. The following are examples of Kubernetes primitives that you can use to analyze Amazon EKS cost allocation data.

- Cluster name
- Deployment
- Namespace
- Node
- Workload Name
- Workload Type

[User-defined cost allocation tags](https://console.aws.amazon.com/costmanagement/home#/tags "https://console.aws.amazon.com/costmanagement/home#/tags") are also supported. For more information about using split cost allocation data, see [Understanding split cost allocation data](../../../cur/latest/userguide/split-cost-allocation-data.md "../../../cur/latest/userguide/split-cost-allocation-data.md") in the AWS Billing User Guide.

## Set up Cost and Usage Reports

You can turn on Split Cost Allocation Data for EKS in the Cost Management Console, AWS Command Line Interface, or the AWS SDKs.

Use the following for _Split Cost Allocation Data_:

1. Opt in to Split Cost Allocation Data. For more information, see [Enabling split cost allocation data](../../../cur/latest/userguide/enabling-split-cost-allocation-data.md "../../../cur/latest/userguide/enabling-split-cost-allocation-data.md") in the AWS Cost and Usage Report User Guide.
2. Include the data in a new or existing report.
3. View the report. You can use the Billing and Cost Management console or view the report files in Amazon Simple Storage Service.
