

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use Amazon Q Developer on the Amazon EKS console
<a name="amazon-q-integration"></a>

Amazon Elastic Kubernetes Service (EKS) integrates with Amazon Q to provide AI-powered troubleshooting directly in the AWS Management Console. This integration helps you quickly investigate and resolve cluster, control plane, node, and workload issues with AI assistance from Amazon Q.

## How it works
<a name="_how_it_works"></a>

The Amazon EKS console displays **Inspect with Amazon Q** buttons contextually alongside errors or issues throughout the console. When you click this button, Amazon Q automatically analyzes the issue and opens a chat panel on the right side of the console with investigation results, root cause analysis, and suggested mitigation steps.

The integration appears in the following locations within the Amazon EKS console:
+  **Cluster health** - Investigate cluster health issues and status messages in the Cluster health tab in observability dashboard
+  **Control plane** - Troubleshoot control plane component errors and warnings in Control plane monitoring in observability dashboard
+  **Upgrade insights** - Analyze potential upgrade blockers and compatibility issues in Upgrade insights in observability dashboard
+  **Node health** - Investigate node-level issues affecting cluster capacity in Node health issues in observability dashboard
+  **Workloads** - Analyze Kubernetes events on pods indicating failures or issues

## Using Amazon Q for troubleshooting
<a name="_using_amazon_q_for_troubleshooting"></a>

 **To investigate an issue with Amazon Q** 

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose the name of the cluster to investigate.

1. When you encounter an error message or issue indicator, look for the **Inspect with Amazon Q** button. The button appears contextually next to the issue or in the error status details view.

1. Choose **Inspect with Amazon Q**.

1. Amazon Q automatically investigates the issue and displays the analysis in a chat panel on the right side of the console.

1. Review the investigation results, including root cause analysis and suggested mitigation steps.

1. You can continue the conversation by asking Amazon Q follow-up questions about the issue.

 **Note** The Amazon Q integration only appears when there is an error, warning, or issue requiring investigation. It does not appear when resources are healthy.

## Considerations
<a name="_considerations"></a>

Consider the following when using Amazon Q with Amazon EKS:
+  **Read-only operations** - The Amazon Q integration performs only read operations on your cluster resources. It does not make any mutating or write actions to your cluster configuration or workloads.
+  **Cross-region processing** - Amazon Q may process data across AWS regions to provide AI-powered analysis. For more information about cross-region processing, see [Cross-region processing](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/cross-region-processing.html) in the *Amazon Q Developer User Guide*.
+  ** AWS Management Console only** - This integration is available only through the AWS Management Console. It is not available through the AWS CLI, AWS APIs, or infrastructure as code tools.

## Learn more
<a name="_learn_more"></a>

For more information about using Amazon Q, see [Chat with Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-with-q.html) in the *Amazon Q Developer User Guide*.