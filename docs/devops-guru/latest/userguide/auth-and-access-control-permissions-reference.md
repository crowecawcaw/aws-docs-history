# Amazon DevOps Guru permissions

reference

You can use AWS-wide condition keys in your DevOps Guru policies to express conditions.
For a list, see [IAM JSON Policy
Elements Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

You specify the actions in the policy's `Action` field. To specify an
action, use the `devops-guru:` prefix followed by the API operation name (for
example, `devops-guru:SearchInsights` and
`devops-guru:ListAnomalies`). To specify multiple actions in a single
statement, separate them with commas (for example, `"Action": [
 "devops-guru:SearchInsights", "devops-guru:ListAnomalies" ]`).

**Using wildcard characters**

You specify an Amazon Resource Name (ARN), with or without a wildcard character (\*),
as the resource value in the policy's `Resource` field. You can use a
wildcard to specify multiple actions or resources. For example,
`devops-guru:*` specifies all DevOps Guru actions and
`devops-guru:List*` specifies all DevOps Guru actions that begin with the word
`List`. The following example refers to all insights with a universally
unique identifier (UUID) that begins with `12345`.

```
arn:aws:devops-guru:us-east-2:123456789012:insight:12345*
```

You can use the following table as a reference when you are setting up [Authenticating with identities](security-iam.md#security_iam_authentication "security-iam.md#security_iam_authentication")
and writing permissions policies that you can attach to an IAM identity
(identity-based policies).

DevOps Guru API operations and required
permissions for actions| DevOps Guru API operations | Required permissions (API actions) | Resources |
| --- | --- | --- |
| `AddNotificationChannel` | `devops-guru:AddNotificationChannel`<br>Required to add a notification channel from DevOps Guru. A notification channel is used to notify you when DevOps Guru<br>generates an insight that contains information about how to improve your operations. | `*` |
| `RemoveNotificationChannel` | `devops-guru:RemoveNotificationChannel`<br>Required to remove a notification channel from DevOps Guru. A notification channel is used to notify you when DevOps Guru<br>generates an insight that contains information about how to improve your operations. | `*` |
| `ListNotificationChannels` | `devops-guru:ListNotificationChannels`<br>Required to return a list of notification channels configured for DevOps Guru. Each notification channel is used to notify you when<br>DevOps Guru generates an insight that contains information about how to improve your operations. The one notification type supported<br>is Amazon Simple Notification Service. | `*` |
| `UpdateResourceCollectionFilter` | `devops-guru:UpdateResourceCollectionFilter`<br>Required to update the list of CloudFormation stacks that are used to specify which AWS resources in your account are analyzed by DevOps Guru.<br>The analysis generates insights that include recommendations, operational metrics, and operational events that you can use to improve<br>the performance of your operations. This method also creates the IAM roles required for you to use CodeGuru OpsAdvisor. | `*` |
| `GetResourceCollectionFilter` | `devops-guru:GetResourceCollectionFilter`<br>Required to return the list of AWS CloudFormation stacks that are used to specify which AWS<br>resources in your account are analyzed by DevOps Guru. The analysis generates insights that include<br>recommendations, operational metrics, and operational events that you can use to improve the<br>performance of your operations. | `*` |
| `ListInsights` | `devops-guru:ListInsights`<br>Required to return a list of insights in your AWS account. You can specify which insights are returned by their<br>start time, status (`ongoing` or `any`), and type (`reactive` or `predictive`). | `*` |
| `DescribeInsight` | `devops-guru:DescribeInsight`<br>Required to return details about an insight that you specify using its ID. | `*` |
| `SearchInsights` | `devops-guru:SearchInsights`<br>Required to return a list of insights in your AWS account. You can specify which insights are returned by their<br>start time, filters, and type (`reactive` or `predictive`). | `*` |
| `ListAnomalies` | `devops-guru:ListAnomalies`<br>Required to return a list of the anomalies that belong to an insight that you specify using its ID. | `*` |
| `DescribeAnomaly` | `devops-guru:DescribeAnomaly`<br>Required to return details about an anomaly that you specify using its ID. | `*` |
| `ListEvents` | `devops-guru:ListEvents`<br>Required to return a list of the events emitted by the resources that are evaluated by<br>DevOps Guru. You can use filters to specify which events are returned. | `*` |
| `ListAnomalousLogs` | devops-guru:`ListAnomalousLogs`<br>Required to return a list of Amazon CloudWatch log groups that contain log<br>anomalies. These are used to generate insights in DevOps Guru.<br>Administrators should ensure that only users with permissions to<br>view CloudWatch logs have permissions to view anomalous CloudWatch logs. We<br>recommend that you use IAM policies to allow or deny access to the<br>`ListAnomalousLogs` operation. | `*` |
| `ListRecommendations` | `devops-guru:ListRecommendations`<br>Required to return a list of a specified insight's recommendations. Each recommendation includes a<br>list of metrics and a list of events that are related to the recommendations. | `*` |
| `DescribeAccountHealth` | `devops-guru:DescribeAccountHealth`<br>Required to return the number of open reactive insights, the<br>number of open proactive insights, and the number of metrics<br>analyzed in your AWS account. Use these numbers to gauge the<br>health of operations in your AWS account. | `*` |
| `DescribeAccountOverview` | `devops-guru:DescribeAccountOverview`<br>Required to return the following that happened during a time range:<br>the number of open reactive insights that were created, the number of open predictive<br>insights that were created, and the mean time to recover (MTTR) for all<br>reactive insights that were closed. | `*` |
| `DescribeResourceCollectionHealthOverview` | `devops-guru:DescribeResourceCollectionHealthOverview`<br>Required to return the number of open predictive insights, open reactive insights, and mean time to recover (MTTR)<br>for all insights for each CloudFormation stack specified in DevOps Guru. | `*` |
| `DescribeIntegratedService` | `devops-guru:DescribeIntegratedService`<br>Required to return the integration status of services that can be integrated with DevOps Guru. The one service that can be integrated with DevOps Guru<br>is AWS Systems Manager, which can be used to create an OpsItem for each generated insight. | `*` |
| `UpdateIntegratedServiceConfig` | `devops-guru:UpdateIntegratedServiceConfig`<br>Required to enable or disable integration with a service that can be integrated with DevOps Guru. The one service that can be integrated with<br>DevOps Guru is Systems Manager, which can be used to create an OpsItem for each generated insight. | `*` |
