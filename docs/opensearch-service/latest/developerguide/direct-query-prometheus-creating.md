# Creating an Amazon Managed Service for Prometheus data source

To create an Amazon Managed Service for Prometheus data source, you need an active workspace and an IAM role that grants OpenSearch Service the necessary permissions to query your metrics.

## Prerequisites

Before you connect the data source, make sure you have the following:

- **Prometheus workspace** – An active Amazon Managed Service for Prometheus workspace. Note your Workspace ID and the AWS Region it resides in.
- **IAM role** – An AWS Identity and Access Management role with a trust policy that allows the `directquery.opensearchservice.amazonaws.com` service principal to assume it.

## Connecting the data source

After your prerequisites are met, you can connect the data source using the OpenSearch Service console.

###### To set up an Amazon Managed Service for Prometheus data source

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. In the left navigation pane, go to **Central management** and choose **Connected data sources**.
3. Choose **Connect new data source**.
4. Choose **Amazon Managed Service for Prometheus** as the data source type.
5. Choose **Next**.
6. Under **Data connection details**, enter a name and an optional description.
7. Under **IAM roles**, choose how to manage access:
   - To automatically create a role for this data source:
     1. Select **Create a new role**.
     2. Enter a name for the IAM role.
     3. Select one or more workspaces to define which data can be queried.

   - To use an existing role that you manage yourself:
     1. Select **Use an existing role**.
     2. Select an existing role from the drop-down menu.###### Note

When using your own role, make sure it has all necessary permissions by attaching required policies from the IAM console. For more information, see [Required permissions for manually created IAM roles](#direct-query-prometheus-manual-role-permissions "#direct-query-prometheus-manual-role-permissions"). 8. (Optional) Under **Access policy**, configure an access policy for the data source. Access policies control whether a request to the OpenSearch Service direct query data source is accepted or rejected. If you don't configure an access policy, only the data source owner has access. You can configure the access policy to enable cross-account access, allowing principals in other AWS accounts to access the data source.

You can create an access policy using the visual editor or by providing a JSON policy document. With the visual editor, you can allow or deny access by specifying a principal AWS account ID, account ARN, IAM user ARN, IAM role ARN, source IP address, or CIDR block. The visual editor supports up to 10 elements. To define a policy with more than 10 elements, use the JSON editor.

You can also choose **Import policy** to import an existing access policy from another data source. 9. (Optional) Under **Tags**, add tags to your data source. 10. Choose **Next**. 11. Under **Set up OpenSearch**, choose how to set up OpenSearch UI:

    1. If no OpenSearch UI application exists in your account, create a new OpenSearch application. If an existing OpenSearch application exists, select it.
    2. If you create a new application, create a new observability workspace. If you selected an existing application, create a new observability workspace or select an existing one. Amazon Managed Service for Prometheus is only available in the observability workspace.

12. Choose **Next**.
13. Review your choices and choose **Edit** if you need to make any changes.
14. Choose **Connect** to set up the data source. Stay on this page while your data source is created. When it's ready, you're taken to the data source details page.

### Next steps

###### Visit OpenSearch UI

After you create a data source, OpenSearch Service provides you with an OpenSearch UI application URL. You use this to configure who has access to OpenSearch UI and analyze your Amazon Managed Service for Prometheus data using Discover Metrics with PromQL.

### Additional resources

#### Required permissions for manually created IAM roles

When creating a data source, you choose an IAM role to manage access to your data. You have two options:

- Create a new IAM role automatically
- Use an existing IAM role that you created manually

If you use a manually created role, you need to attach the correct permissions to the role. The permissions must allow access to the specific data source and allow OpenSearch Service to assume the role. This is required so that OpenSearch Service can securely access and interact with your data.

The following sample policy demonstrates the least-privilege permissions required to create and manage a data source. If you have broader permissions, such as `aps:*` or the `AdministratorAccess` policy, these permissions encompass the least-privilege permissions in the sample policy.

In the following sample policy, replace the `placeholder` text with your own information.

###### Sample IAM policy

Attach the following permissions to your IAM role to allow OpenSearch Service to fetch metric metadata and execute queries:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AmazonOpenSearchDirectQueryPrometheusAccess",
            "Effect": "Allow",
            "Action": [
                "aps:DeleteAlertManagerSilence",
                "aps:GetAlertManagerSilence",
                "aps:GetAlertManagerStatus",
                "aps:GetLabels",
                "aps:GetMetricMetadata",
                "aps:GetSeries",
                "aps:ListAlertManagerAlertGroups",
                "aps:ListAlertManagerAlerts",
                "aps:ListAlertManagerReceivers",
                "aps:ListAlertManagerSilences",
                "aps:ListAlerts",
                "aps:QueryMetrics",
                "aps:PutAlertManagerSilences",
                "aps:DescribeAlertManagerDefinition",
                "aps:CreateRuleGroupsNamespace",
                "aps:DeleteRuleGroupsNamespace",
                "aps:ListRuleGroupsNamespaces",
                "aps:DescribeRuleGroupsNamespace",
                "aps:PutRuleGroupsNamespace"
            ],
            "Resource": "arn:aws:aps:`region`:`account-id`:workspace/`workspace-id`",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "directquery.opensearchservice.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "AmazonOpenSearchDirectQueryPrometheusListAccess",
            "Effect": "Allow",
            "Action": [
                "aps:ListWorkspaces"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "directquery.opensearchservice.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

###### Sample trust policy

Attach the following trust policy to your IAM role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "TrustPolicyForAmazonOpenSearchDirectQueryService",
            "Effect": "Allow",
            "Principal": {
                "Service": "directquery.opensearchservice.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": "arn:aws:opensearch:`region`:`account-id`:datasource/`data-source-name`"
                },
                "StringEquals": {
                    "aws:SourceAccount": "`account-id`"
                }
            }
        }
    ]
}
```
