

# Deleting a Google Cloud Platform connector in Security Hub CSPM

After you create a Google Cloud Platform (GCP) connector in AWS Security Hub CSPM, you can delete it at any time. If you delete a connector, Security Hub CSPM stops performing posture management checks for your GCP environment. Security Hub CSPM also stops generating new findings about your environment. Your existing findings are retained for 90 days. Resource inventory remains as it was when the connector was deleted and is removed after 90 days.

When you delete a connector, note the following:
+ Security Hub CSPM doesn't delete the resources that the setup script created in your GCP environment. You must delete these manually, directly in GCP. For details, see [Clean up GCP resources](#securityhub-gcp-delete-cleanup).
+ If the connector is a customer-managed connector and a service-linked connector also exists, deleting the customer-managed connector does not affect the service-linked connector. Security Hub CSPM continues to receive posture management findings through the service-linked connector.
+ Existing findings transition to an archived state within 3-5 days and are deleted after the 90-day retention period.

**To delete a GCP connector**

1. Open the Security Hub CSPM console.

1. In the navigation pane, choose **Integrations**.

1. Select your connector.

1. Choose **Delete**.

1. When prompted, confirm that you want to delete the connector.

## Clean up GCP resources
<a name="securityhub-gcp-delete-cleanup"></a>

After you delete the connector, you can remove the resources that the setup script created. Resource names include your AWS account ID ({{aws-account-id}}) and, for subscriptions, the AWS Region ({{aws-region}}).

**Important**  
The workload identity pool, service account, topics, sinks, feed, and organization role bindings are shared by every connector for the same AWS account in every AWS Region, and by any Security Hub or Amazon Inspector connector for the same account. Delete them only if no other connector uses them. If you deleted a connector in one Region only, delete only that Region's subscriptions.

For the commands that delete each resource, see the Google Cloud documentation.
+ Remove the organization audit logging configuration for `allServices` `DATA_WRITE` if you no longer need it. Deleting the connector does not revert this audit logging change.
+ Delete the organization log sink `config-lifecycle-sink-{{aws-account-id}}`.
+ Delete the organization asset feed `config-cai-feed-{{aws-account-id}}`.
+ Delete the Pub/Sub topics and subscriptions in the management project: `config-lifecycle-topic-{{aws-account-id}}`, `config-cai-topic-{{aws-account-id}}`, and their subscriptions ending in `-{{aws-region}}`.
+ Remove the organization IAM role bindings for the service account, and remove the `roles/cloudasset.serviceAgent` binding that the script granted to the Cloud Asset service agent on the management project.
+ Delete the organization custom role `securityHubConfigReader` if no other connector uses it. GCP does not let you reuse a deleted custom role ID for 37 days, so keep the role if you plan to create a connector again.
+ Delete the service account `config-sa-{{aws-account-id}}`.
+ Delete the workload identity pool `connector-pool-{{aws-account-id}}` and its provider.
+ If you also set up Amazon Inspector for GCP, its setup script adds more resources, including additional custom roles, a Pub/Sub route, and OS Config resources. See [Deleting a Google Cloud Platform connector in Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/inspector-gcp-delete.html) in the *Amazon Inspector User Guide* before you delete shared resources.