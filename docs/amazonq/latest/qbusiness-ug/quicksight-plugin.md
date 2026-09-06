

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Using the Quick plugin to get insights from structured data
<a name="quicksight-plugin"></a>

**Note**  
The Quick plugin feature is in preview and is subject to change.

The Quick plugin is a fully integrated plugin that gives an Amazon Q Business application access to insights and external databases through [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html). Quick is a business intelligence service that provides insights from your structured data, such as databases, data lakes, and data warehouses.

With the Quick plugin for Amazon Q Business, end users can get answers from this structured data directly in an Amazon Q Business application. You don't have to index or reformat this structured data, and you don't need to migrate it to Amazon Q Business.

For example, an end user might ask "What was the revenue per month for my business for 2023?" in their Amazon Q Business chat application. They would get answers based on your unstructured data in Amazon Q Business and, below this response, Quick answers based on structured data.

The response from QuickSight can include a multi-visual answer that includes an AI-generated narrative that summarizes key insights, and supporting visuals and interactive graphs to add context. If these visuals don't exist already, Quick can generate them on the fly based on the user's question and the available data in Quick and external databases.

To enable the plugin, you use Amazon Q Business to link your Amazon Quick account with your application and grant it permission to communicate with Quick. If you use the console, you can create the Quick account in Amazon Q Business. If you already have a Quick account, you can enable the plugin with the console or the [CreatePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreatePlugin.html) API operation. 

After you create resources in Quick (including datasets, topics, and, optionally, dashboards), end users automatically start getting insights based on your structured data. 

**Important**  
The Quick plugin is fully integrated with Amazon Q Business, and won't appear in the list of plugins in the web experience. For every user prompt, it automatically queries Quick. For information about pausing the plugin, see [Pausing integration with Quick](quicksight-plugin-pausing-integration.md).

**Note**  
If your [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html) settings allow Amazon Q to automatically orchestrate end user chat queries across plugins and data sources, an Quick plugin will only activate if:  
No other plugin actions (read or write requests requiring additional end user input through forms) are detected, or, in progress.
No end user authentication requests are pending.

**Topics**
+ [Pricing](#quicksight-plugin-pricing)
+ [Guidelines and requirements](#quicksight-plugin-req)
+ [Service access role](#quicksight-plugin-service-access-role)
+ [Configuring an Amazon Q Business application to use the plugin](quicksight-plugin-configuring-application.md)
+ [Getting data insights from Amazon Quick answers](quicksight-plugin-getting-data-insights.md)
+ [Pausing integration with Quick](quicksight-plugin-pausing-integration.md)

## Pricing
<a name="quicksight-plugin-pricing"></a>

When you set up the integration with Quick, you assign one or more IAM Identity Center groups the Quick Admin Pro role. This role grants users access to all Generative BI capabilities in Amazon Quick. Your Quick administrator is responsible for adding and managing user permissions and configuring your Quick account.

The Quick Admin Pro role incurs additional costs. For more information about pricing, see [Amazon Quick pricing](https://aws.amazon.com/quicksight/pricing/). For more information about Pro roles in Amazon Quick, see [Get started with Generative BI](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html).

When you link a Quick account and an Amazon Q Business application, the following groups get Pro subscription benefits at no additional cost:
+ Quick Admin Pro groups are added to the Amazon Q Business Pro subscription.
+ Existing Amazon Q Business Pro groups are assigned the Quick Reader Pro role.

## Guidelines and requirements
<a name="quicksight-plugin-req"></a>
+ You must use IAM Identity Center for authentication for both Quick and Amazon Q Business. If your Amazon Q Business application doesn't use IAM Identity Center, you must create a new one that does. For information about creating an IAM Identity Center integrated application, see [Configuring an Amazon Q Business application using AWS IAM Identity Center](create-application.md). 
+ Your Amazon Q Business application and Amazon Quick account must be in the same AWS Region.
+ To get answers from QuickSight in your web experience, you must add at least one index to your Amazon Q Business application. To learn how to add an index, see [creating an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html). 
+ If you don't have a Quick account, you can create the account from the Amazon Q Business console when you configure your application to communicate with Quick.
+ You must authorize Amazon Q Business to communicate with Amazon Quick with a service role. For more information, see [Service access role](#quicksight-plugin-service-access-role).
+ The IAM role for your Amazon Q Business web experience must have `quicksight:GenerateEmbedUrlForRegisteredUserWithIdentity` permissions. For a policy example, see [IAM role for an Amazon Q Business web experience using IAM Identity Center](web-experience-iam-role-idc.md).

## Service access role
<a name="quicksight-plugin-service-access-role"></a>

When you link your Quick account in the Amazon Q Business console, you specify an AWS Identity and Access Management (IAM) role that authorizes Amazon Q Business to communicate with Amazon Quick. In the console, you can choose to create this role with the correct permissions automatically configured. Or you can manually create it. 
+  The role's permissions policy must grant `quicksight:PredictQAResults` for Amazon Quick topics and, if you create them, dashboards. For a permissions policy example, see [AWS managed policy: QBusinessQuicksightPluginPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazonq-quicksight-policy).
+ The role's trust policy must grant Amazon Q Business `AssumeRole` and `SetContext`permissions as follows. 

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "QBusinessQuicksightManagedPolicyTrustPolicy",
              "Effect": "Allow",
              "Principal": {
                  "Service": "qbusiness.amazonaws.com"
              },
              "Action": [
                  "sts:AssumeRole",
                  "sts:SetContext"
              ],
              "Condition": {
                  "StringEquals": {
                      "aws:SourceAccount": "111122223333"
                  },
                  "ArnLike": {
                      "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/{{application-id}}"
                  }
              }
          }
      ]
  }
  ```

------