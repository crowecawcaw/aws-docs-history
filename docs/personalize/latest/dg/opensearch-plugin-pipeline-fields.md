# Fields for the `personalized_search_ranking` response processor

When you create a search pipeline for the Amazon Personalize Search Ranking plugin, you specify a `personalized_search_ranking` response processor with the
following fields.

- **campaign_arn (required)** – Specify the Amazon Resource Name (ARN) of the Amazon Personalize
  campaign to use to personalize results.
- **item_id_field (optional)** – If the `_id` field for an indexed
  document in OpenSearch doesn't correspond with your Amazon Personalize itemIds, specify the name of the field that does. By
  default, the plugin assumes that the `_id` data matches the itemId in your Amazon Personalize data.
- **recipe (required)** – Specify the name of the Amazon Personalize recipe to use. To use the plugin, you can
  specify `aws-personalized-ranking-v2` or `aws-personalized-ranking`.
- **weight (required)** – Specify the emphasis that the response processor puts
  on personalization when it re-ranks results. Specify a value within a range of 0.0–1.0. The closer to
  `1.0` that it is, the more likely it is that results from Amazon Personalize rank higher. If you specify
  `0.0`, no personalization occurs and OpenSearch takes precedence.
- **tag (optional)** – Specify an identifier for the processor.
- **iam_role_arn (required for OpenSearch Service, optional for open source OpenSearch)** –
  For OpenSearch Service, provide the Amazon Resource Name (ARN) for the role that you created when [setting up
  permissions](opensearch-granting-access-managed.md "opensearch-granting-access-managed.md") for OpenSearch Service to access your Amazon Personalize resources.
  If your OpenSearch Service and Amazon Personalize resources exist in different accounts, specify the role that grants
  `AssumeRole` permissions for OpenSearch Service. For more information, see [Configuring permissions when resources are in different
  accounts](configuring-multiple-accounts.md "configuring-multiple-accounts.md").

For open source OpenSearch, if you use multiple roles to restrict permissions for different groups of users in
your organization, specify the ARN of the role that has permission to access Amazon Personalize. If you use only the AWS
credentials in your OpenSearch keystore, you can omit this field.

- **aws_region (required)** – The AWS Region where you created your Amazon Personalize
  campaign.
- **ignore_failure (optional)** – Specify whether the plugin ignores any
  processor failures. For values, specify `true` or `false`. For your production environments, we
  recommend that you specify `true` to avoid any interruptions for query responses. For test environments,
  you can specify `false` to view any errors that the plugin generates.
- **external_account_iam_role_arn** – If you use OpenSearch Service, and your Amazon Personalize and OpenSearch Service
  resources exist in different accounts, specify the ARN of the role that has permission to access your Amazon Personalize resources.
  This role must exist in the same account as your Amazon Personalize resources. For more information, see [Configuring permissions when resources are in different
  accounts](configuring-multiple-accounts.md "configuring-multiple-accounts.md").
  For an OpenSearch Service code sample, see [Creating a pipeline in Amazon OpenSearch Service](managed-opensearch-plugin-pipeline-example.md "managed-opensearch-plugin-pipeline-example.md"). For an open source OpenSearch example, see [Creating a pipeline in open source OpenSearch](opensearch-plugin-pipeline-example.md "opensearch-plugin-pipeline-example.md").
