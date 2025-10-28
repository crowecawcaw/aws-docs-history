**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Analyze security events on EKS with Amazon Detective

[Amazon Detective](https://aws.amazon.com/detective/ "https://aws.amazon.com/detective/") helps you analyze, investigate, and quickly identify the root cause of security findings or suspicious activities. Detective automatically collects log data from your AWS resources. It then uses machine learning, statistical analysis, and graph theory to generate visualizations that help you to conduct faster and more efficient security investigations. The Detective prebuilt data aggregations, summaries, and context help you to quickly analyze and determine the nature and extent of possible security issues. For more information, see the [Amazon Detective User Guide](../../../detective/latest/adminguide/what-is-detective.md "../../../detective/latest/adminguide/what-is-detective.md").

Detective organizes Kubernetes and AWS data into findings such as:

- Amazon EKS cluster details, including the IAM identity that created the cluster and the service role of the cluster. You can investigate the AWS and Kubernetes API activity of these IAM identities with Detective.
- Container details, such as the image and security context. You can also review details for terminated Pods.
- Kubernetes API activity, including both overall trends in API activity and details on specific API calls. For example, you can show the number of successful and failed Kubernetes API calls that were issued during a selected time range. Additionally, the section on newly observed API calls might be helpful to identify suspicious activity.
  Amazon EKS audit logs is an optional data source package that can be added to your Detective behavior graph. You can view the available optional source packages, and their status in your account. For more information, see [Amazon EKS audit logs for Detective](../../../detective/latest/adminguide/source-data-types-EKS.md "../../../detective/latest/adminguide/source-data-types-EKS.md") in the _Amazon Detective User Guide_.

## Use Amazon Detective with Amazon EKS

Before you can review findings, Detective must be enabled for at least 48 hours in the same AWS Region that your cluster is in. For more information, see [Setting up Amazon Detective](../../../detective/latest/adminguide/detective-setup.md "../../../detective/latest/adminguide/detective-setup.md") in the _Amazon Detective User Guide_.

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. From the left navigation pane, select **Search**.
3. Select **Choose type** and then select **EKS cluster**.
4. Enter the cluster name or ARN and then choose **Search**.
5. In the search results, choose the name of the cluster that you want to view activity for. For more information about what you can view, see [Overall Kubernetes API activity involving an Amazon EKS cluster](../../../detective/latest/userguide/profile-panel-drilldown-kubernetes-api-volume.md "../../../detective/latest/userguide/profile-panel-drilldown-kubernetes-api-volume.md") in the _Amazon Detective User Guide_.
