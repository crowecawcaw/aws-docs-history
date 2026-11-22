

# Prerequisites for integrating Security Hub with Google Cloud Platform

Before you integrate Google Cloud Platform (GCP) with AWS Security Hub, complete the following tasks in your AWS and GCP environments. This helps ensure that you and Security Hub have the resources and permissions that you need to monitor your GCP resources.

**Topics**
+ [Prerequisites for AWS](#securityhub-v2-gcp-prereqs-aws)
+ [Prerequisites for GCP](#securityhub-v2-gcp-prereqs-gcp)

## Prerequisites for AWS
<a name="securityhub-v2-gcp-prereqs-aws"></a>

Verify that you have the following in your AWS account:

**AWS Security Hub enabled**  
Security Hub must be enabled in the AWS account and AWS Region where you want to create the connector. You must enable Security Hub before creating a GCP connector.

**AWS Security Hub CSPM enabled**  
Security Hub CSPM must be enabled in the same AWS account and AWS Region. The GCP integration relies on Security Hub CSPM for resource configuration evaluation.

**Console IAM permissions**  
The IAM principal creating the connector must have the following permissions:  
+ `config:GetConnector`
+ `config:ListConnectors`
+ `config:PutConnector`
+ `securityhub:BatchDisableStandards`
+ `securityhub:BatchEnableStandards`
+ `securityhub:CreateConnectorV2`
+ `securityhub:DeleteConnectorV2`
+ `securityhub:DescribeHub`
+ `securityhub:DescribeStandards`
+ `securityhub:EnableSecurityHub`
+ `securityhub:GetConnector`
+ `securityhub:GetConnectorV2`
+ `securityhub:GetEnabledStandards`
+ `securityhub:ListConnectors`
+ `securityhub:ListConnectorsV2`
+ `securityhub:ListTagsForResource`
+ `securityhub:TagResource`
+ `securityhub:UntagResource`
+ `securityhub:UpdateConnectorV2`
If vulnerability management is available, the principal also needs `inspector2:ListConnectors`. The console shows this policy under **View permissions** on the **Add GCP integration** page.

**IAM Outbound Identity Federation enabled**  
You must enable IAM Outbound Identity Federation in your AWS account. This feature allows AWS services to authenticate to external identity providers (such as GCP IAM) using federated credentials rather than long-lived secrets.  
After enabling Outbound Identity Federation, note the **Token Issuer URL**. This URL follows the format:  

```
https://{{uuid}}.tokens.sts.global.api.aws
```
You will need this URL when configuring workload identity federation in GCP.

**AWS Region chosen**  
Decide which AWS Region you will create the connector in before you generate the setup script. The script configures GCP resources for that specific Region, and the connector must be created in the same Region.

## Prerequisites for Google Cloud Platform
<a name="securityhub-v2-gcp-prereqs-gcp"></a>

Verify that you have the following in your GCP environment:

**GCP organization and management project**  
You must have a GCP organization. Security Hub grants read access, exports audit logs, and subscribes to resource changes at the organization level, so projects that are not part of an organization cannot be monitored.  
You also need a *management project* in the organization that hosts the connector resources: the workload identity pool, the service account, and the Pub/Sub topics and subscriptions. The management project must have billing enabled and the IAM API (`iam.googleapis.com`) turned on before you run the setup script. The script turns on the other APIs that it needs. You can use an existing project or create a dedicated one.

**Cloud Audit Logs**  
Security Hub detects resource changes from Cloud Audit Logs. Admin Activity logs are always enabled in GCP. The setup script also enables Data Access audit logs for write operations across all services in the organization, which adds Cloud Logging volume and cost.  
Do not exempt the connector service account or other principals from audit logging. Activity by exempted principals is not reported, and the setup script stops if it finds an exemption that affects the integration.

**Permissions to run the setup script**  
The account that runs the setup script needs the following roles. In many organizations, the GCP administrator and the AWS security administrator are different people. The GCP setup can be completed independently using the generated setup script.  
On the **organization**:  
+ **Organization Administrator** (`roles/resourcemanager.organizationAdmin`) – to grant IAM roles to the service account at the organization scope and to update the organization's Data Access audit logging configuration.
+ **Cloud Asset Owner** (`roles/cloudasset.owner`) – to create the organization asset feed.
+ **Logs Configuration Writer** (`roles/logging.configWriter`) – to create the organization log sinks.
+ **Organization Role Administrator** (`roles/iam.organizationRoleAdmin`) – to create the `securityHubConfigReader` custom role, and the additional custom roles that Amazon Inspector uses when vulnerability management is enabled.
On the **management project**: **Owner**, or the combination of **Service Usage Admin**, **Security Admin**, **Workload Identity Pool Admin**, **Service Account Admin**, and **Pub/Sub Admin**.  
If you enable VM scanning through Amazon Inspector, additional permissions are required on each project that contains VMs. For details, see [Integrating Amazon Inspector with Google Cloud Platform](https://docs.aws.amazon.com/inspector/latest/user/inspector-gcp.html) in the *Amazon Inspector User Guide*.

**Command-line tools**  
To run the setup script, you need the gcloud CLI with the `beta` component installed, `jq`, and a `timeout` command that supports `--foreground` (GNU coreutils, or `gtimeout` on macOS). [Google Cloud Shell](https://cloud.google.com/shell) on the Google Cloud website includes all of these. You must also have accepted the Google Cloud Terms of Service.

After you complete these tasks, you are ready to [configure your GCP environment](securityhub-v2-gcp-setup-gcp.md).