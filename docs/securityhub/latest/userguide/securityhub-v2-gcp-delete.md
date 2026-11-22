

# Deleting a Google Cloud Platform connector in Security Hub

After you create a Google Cloud Platform (GCP) connector in AWS Security Hub, you can delete it at any time. If you delete a connector, Security Hub stops performing posture management checks and vulnerability monitoring for your GCP environment. Security Hub also stops generating new findings and other data about your environment. Your existing findings are retained for 90 days. Resource inventory remains as it was when the connector was deleted and is removed after 90 days.

When you delete a connector, Security Hub automatically deletes the associated service-linked connectors in AWS Security Hub CSPM and Amazon Inspector. Security Hub does not delete the resources that the setup script created in your GCP environment. You must delete these manually, directly in GCP. For details, see [Clean up GCP resources](#securityhub-v2-gcp-delete-cleanup).

**To delete a GCP connector**

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1](https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1).

1. In the navigation pane, choose **Integrations**.

1. Select the connector that you want to delete.

1. Choose **Delete**.

1. When prompted, confirm that you want to delete the connector.

**Important**  
If you delete a connector and create a new one within 6 hours, resource detection may take up to 6 hours. Plan connector deletion and recreation accordingly.

## Clean up GCP resources
<a name="securityhub-v2-gcp-delete-cleanup"></a>

After you delete the connector, you can remove the resources that the setup script created. Resource names include your AWS account ID ({{aws-account-id}}) and, for subscriptions, the AWS Region ({{aws-region}}).

**Important**  
The workload identity pool, service account, topics, sinks, feed, and organization role bindings are shared by every connector for the same AWS account in every AWS Region, and by any Security Hub CSPM or Amazon Inspector connector for the same account. Delete them only if no other connector uses them. If you deleted a connector in one Region only, delete only that Region's subscriptions.

For the commands that delete each resource, see the Google Cloud documentation.
+ Remove the organization audit logging configuration for `allServices` `DATA_WRITE` (and `artifactregistry.googleapis.com` `DATA_READ` if you enabled vulnerability management) if you no longer need it. Deleting the connector does not revert these audit logging changes.
+ Delete the organization log sinks `config-lifecycle-sink-{{aws-account-id}}` and, if present, `inspector-pull-sink-{{aws-account-id}}`.
+ Delete the organization asset feed `config-cai-feed-{{aws-account-id}}`.
+ Delete the Pub/Sub topics and subscriptions in the management project: `config-lifecycle-topic-{{aws-account-id}}`, `config-cai-topic-{{aws-account-id}}`, their subscriptions ending in `-{{aws-region}}`, and the `inspector-pull-` topic and subscription if present.
+ Remove the organization IAM role bindings for the service account, and remove the `roles/cloudasset.serviceAgent` binding that the script granted to the Cloud Asset service agent on the management project.
+ Delete the organization custom roles `securityHubConfigReader`, `inspectorArtifactReader`, `inspectorFunctionSourceReader`, and `OSPolicySSMDeployer` if present and no other connector uses them. GCP does not let you reuse a deleted custom role ID for 37 days, so keep the roles if you plan to create a connector again.
+ Delete the service account `config-sa-{{aws-account-id}}`.
+ Delete the workload identity pool `connector-pool-{{aws-account-id}}` and its provider. If you enabled vulnerability management with VM scanning, also delete the pool `inspector-vm-bridge-{{aws-account-id}}` and the `inspector-vmscan-{{aws-account-id}}` service account in each VM project.
+ If you enabled VM scanning, delete the OS Config policy orchestrator `amazoninspector2-{{aws-account-id}}-{{aws-region}}`. After you delete the connector, the orchestrator remains with its action set to uninstall. Set its action to `DELETE`, wait until all of its policy assignments are gone, and then delete the orchestrator. If you delete the orchestrator first, its assignments remain as orphans.
+ If you enabled VM scanning, delete the IAM roles `Inspector2VmScannerRole-{{organization-id}}`, `Inspector2SSMFederationRole-{{organization-id}}`, `Inspector2SSMAssumeRole-{{organization-id}}`, and `Inspector2SSMDispatchRole-{{organization-id}}` in your AWS account.