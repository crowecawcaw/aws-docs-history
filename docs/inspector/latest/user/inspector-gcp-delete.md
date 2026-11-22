

# Deleting a Google Cloud Platform connector in Amazon Inspector

You can delete a Google Cloud Platform (GCP) connector when you no longer want Amazon Inspector to scan resources in that GCP organization.

## What happens when you delete a connector
<a name="inspector-gcp-delete-what-happens"></a>

When you delete a GCP connector:
+ Amazon Inspector stops scanning all GCP resources associated with the connector.
+ Existing findings for those GCP resources are closed.
+ Those GCP resources no longer appear in the Coverage view.
+ If a service-linked connector exists (created through AWS Security Hub), deleting a customer-managed connector doesn't affect the service-linked connector. Amazon Inspector continues scanning through the service-linked connector.
+ If VM scanning is turned on for the connector, Amazon Inspector sets the OS policy that installs the Amazon Inspector VM scanner to uninstall. VM Manager then removes the scanner package, its configuration, and its logs from each VM in scope. Removing the scanner is best effort. To check, view the OS policy compliance of your VMs in VM Manager.

## What stays in GCP and AWS
<a name="inspector-gcp-delete-what-stays"></a>

Amazon Inspector doesn't delete resources in your GCP environment or the IAM roles in your AWS account. After you delete the connector, the following remain:
+ The resources that the setup script created, including the workload identity pool and provider, the service account, Pub/Sub topics and subscriptions, log sinks, the Cloud Asset Inventory feed, custom roles, and audit logging settings.
+ If you set up VM scanning: the OS policy orchestrator `amazoninspector2-{{account-id}}-{{aws-region}}` and its assignments (set to uninstall), VM Manager in your VM projects, which GCP continues to charge for, and the four `Inspector2*-{{organization-id}}` IAM roles. For the roles, see [Configuring Amazon Inspector to integrate with Google Cloud Platform](inspector-gcp-setup-inspector.md).

If you turn on VM scanning again from the same AWS account and AWS Region, Amazon Inspector reuses the OS policy orchestrator. Delete the old orchestrator first in the following cases:
+ You turn on VM scanning for the same GCP environment from a different AWS account or AWS Region. The new connector gets its own orchestrator, and the old orchestrator's OS policy assignments keep applying their uninstall policy to the same VM instances and can remove the Amazon Inspector VM Scanner that the new connector installs. Delete the old assignments as well as the old orchestrator.
+ You switch between **All projects** and a list of projects. With **All projects**, the orchestrator is in your GCP organization. With a list of projects, it is in the management project. The Amazon Inspector VM Scanner install fails until you delete the orchestrator in the other location. Its OS policy assignments can stay, because the orchestrator in the new location takes them over.

To delete an orchestrator and its OS policy assignments, change the orchestrator's action to delete. After it deletes the assignments, delete the orchestrator. For instructions, see the VM Manager documentation on the Google Cloud website.

**Note**  
AWS Config shares the workload identity pool and provider, the service account, the topics, subscriptions, log sinks, asset feed, and the organization audit logging settings with AWS Security Hub or AWS Security Hub CSPM. Don't delete them while those services use them.

## Deleting a connector
<a name="inspector-gcp-delete-procedure"></a>

**To delete a GCP connector**

1. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home).

1. In the navigation pane, choose **Integrations**.

1. Select the GCP connector you want to delete.

1. Choose **Delete**.

1. In the confirmation dialog box, enter **delete**, and then choose **Delete connector**.

You can also delete a connector by using the `inspector2:DeleteConnector` API operation.

**Important**  
If you delete a connector and create a new one within 6 hours, resource detection can take up to 6 hours. Plan connector deletion and recreation accordingly.