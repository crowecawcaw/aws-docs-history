

# Configuring Security Hub CSPM to integrate with Google Cloud Platform

After you complete the [prerequisite tasks](securityhub-gcp-prereqs.md) and [configure your Google Cloud Platform (GCP) environment](securityhub-gcp-setup-gcp.md), you can configure AWS Security Hub CSPM to integrate with GCP. To configure Security Hub CSPM to integrate with GCP, you create a connector. After you create the connector, the following events occur:

1. Security Hub CSPM validates the GCP credentials and connectivity to your GCP environment. This process can take several minutes.

1. AWS Config begins discovering and recording configuration data for your GCP resources.

1. Security Hub CSPM begins generating posture management findings for your GCP resources after resource data collection completes.

**Note**  
If you already created a connector in Security Hub, a service-linked connector was automatically created in Security Hub CSPM. You do not need to create a separate customer-managed connector unless you require a different scope.

**Topics**
+ [Create a connector](#securityhub-gcp-setup-securityhub-proc)
+ [Enable standards and controls](#securityhub-gcp-setup-securityhub-standards)
+ [Adjust the scope of a connector](#securityhub-gcp-setup-securityhub-manage)
+ [Verify the health of a connector](#securityhub-gcp-setup-securityhub-verify)
+ [Troubleshoot a connector](#securityhub-gcp-setup-securityhub-tshoot)
+ [Resource identifiers](#securityhub-gcp-setup-securityhub-identifiers)
+ [Available controls](#securityhub-gcp-controls)

## Create a GCP connector
<a name="securityhub-gcp-setup-securityhub-proc"></a>

To create a GCP connector for your environment, complete the following steps by using the AWS Security Hub CSPM console or the API.

1. Open the Security Hub CSPM console.

1. In the navigation pane, choose **Integrations**.

1. Choose **Add integration**. On the **Integrations catalog** tab, find the **GCP** card and choose **Add integration**. The **Add GCP integration** page opens. If a GCP connector already exists, the card shows **View configured integrations** instead.

1. In the **Security standard selection** section, keep **Configure all GCP security standards** (recommended), or choose **Customize GCP security standards** and select at least one standard. A standard that you do not select is disabled for the account.

1. In the **Monitoring targets** section, for **Organization ID**, enter your numeric GCP organization ID. You can find it in the GCP console under *IAM & Admin > Settings*, or by running `gcloud organizations list`.

1. Choose the scope and locations to monitor:
   + For **GCP scope selection**, choose **Organization** to monitor all current and future projects in the organization, or **Selected projects** to monitor only the projects that you specify. If you choose **Selected projects**, enter up to 100 project IDs.
   + For **Google Cloud location coverage**, choose **Record all locations** to monitor resources in every Google Cloud location, including locations added in the future, or **Choose specific locations** to monitor only the regions, zones, multi-regions, and dual-regions that you select. Selecting a region also selects all of its zones. Global resources are always recorded regardless of your selection.
**Note**  
Some GCP resources aren't located in a specific region. Examples include VPC networks, firewall rules, IAM service account keys, API keys, Cloud DNS zones, and organization-level resources such as folders. GCP reports the location of these resources as `global`, and Security Hub CSPM evaluates and generates findings for the global resources that it records.
**Note**  
Selecting a region in the console also selects its zones. If you create or update the connector with the `CreateConnector` or `UpdateConnector` API operation, a region in the location list does not include its zones. List each zone that contains resources to monitor, for example `us-central1-a`. The API does not accept the value `global`.

1. In the **Data connection** section, choose **Help me generate a script** to have the console generate a setup script, or **I will create GCP resources myself** if you configured GCP manually.

   If you chose the script option, enter the **Management project ID** (the GCP project that hosts the workload identity federation pool) and the **Issuer URL** (the Token Issuer URL from IAM Outbound Identity Federation), and then choose **Open setup script**. Run the script in your GCP environment as described in [Configuring Google Cloud Platform to integrate with Security Hub CSPM](securityhub-gcp-setup-gcp.md). The management project ID and issuer URL are used only to generate the script; they are not stored with the connector.

1. Under **Provide connector details**, paste the values that the setup script prints when it completes:
   + For **Service account email**, enter the email of the service account that the script created, in the format `config-sa-{{aws-account-id}}@{{management-project}}.iam.gserviceaccount.com`.
   + For **Workload identity pool provider**, enter the workload identity pool provider resource name, in the format `projects/{{project-number}}/locations/global/workloadIdentityPools/connector-pool-{{aws-account-id}}/providers/connector-oidc-{{aws-account-id}}`.

   Then choose **Create data connection**.

1. (Optional) Expand **Tags - optional** and add tags to the connector. A tag is a label that you assign to an AWS resource. You can use tags to search and filter your resources or track your AWS costs.

1. In the **Connector details** section, do the following:
   + For **Name**, enter a unique name for the connector. The name can contain up to 50 alphanumeric characters and it can include hyphens (‐).
**Important**  
Names and descriptions are used to identify your content, and we recommend you do not include sensitive, confidential, or personally identifiable information (PII) in them.
   + For **Description**, optionally enter a brief description of the connector. The description can contain up to 200 characters.

1. Review your configuration in the **GCP integration summary** section, and then choose **Connect**.

After you create the connector, Security Hub CSPM validates your GCP credentials and begins resource discovery. On the **Configured integrations** tab, **Enablement status** shows **Enabled**. **Health status** changes to **Connected** after the first health check, typically within about 10 minutes.

## Enabling standards and controls
<a name="securityhub-gcp-setup-securityhub-standards"></a>

When you create the connector in the console, Security Hub CSPM enables the GCP security standards that you select when you choose **Connect**. If you create the connector with the API, enable the GCP standards separately. For general information about enabling standards and managing controls, see [Enabling standards](https://docs.aws.amazon.com/securityhub/latest/userguide/enable-standards.html) and [Enabling and disabling controls](https://docs.aws.amazon.com/securityhub/latest/userguide/enable-controls-overview.html).

**Available standards**
+ **CIS Google Cloud Platform Foundation Benchmark v4.0.0** - A widely adopted security benchmark that defines best practices for securing GCP environments. Each control evaluates a specific aspect of your GCP configuration (for example, storage bucket encryption, firewall rules, identity and access settings).

GCP standards have their own set of controls, separate from AWS controls. There are no cross-cloud controls that evaluate both AWS and GCP resources in a single check.

**Enabling a standard**

You can enable GCP standards through the Security Hub CSPM console or through the API/CLI. Navigate to **Standards** in the Security Hub CSPM console and enable the desired standard. Alternatively, use the CLI:

```
$ aws securityhub batch-enable-standards \
  --standards-subscription-requests '[{"StandardsArn": "{{Standard-ARN}}"}]' \
  --region {{your-aws-region}}
```

**Note**  
You can enable GCP standards before or after creating the connector - they are not coupled. However, findings will only be generated once both the connector and the standard are active and resource data has been collected.

**Managing individual controls**

Once a standard is enabled (typically within seconds), you can view and manage individual controls:
+ **View controls:** Use the Security Hub CSPM console (Standards > select standard > Controls) or the `list-standards-control-associations` API.
+ **Disable a control:** If a specific control is not applicable to your environment, you can disable it.
+ **Configure custom parameters:** Some controls accept custom input parameters (for example, password length thresholds). These can be configured through the `update-security-control` API.

**Important notes**
+ GCP standards apply uniformly across your entire connector scope. You cannot enable different standards or controls for different GCP projects within the same connector.
+ **Controls depend on resource data availability.** Each control evaluates a specific GCP resource type. If AWS Config has not yet collected configuration data for a particular resource type, the control may generate FAILED or default PASS findings. These findings will automatically update to accurate evaluations as resource data arrives. Do not treat initial compliance scores as accurate until resource data collection is complete.
+ Custom input parameters for security controls can be configured even before creating a connector - they persist independently.
+ Controls evaluating project-level settings produce one finding per GCP project rather than per individual resource.
+ Multicloud standards cannot be included in Central Configuration policies. You must manage GCP standard enablement independently in each AWS account and AWS Region.

## Adjust the scope of a GCP connector
<a name="securityhub-gcp-setup-securityhub-manage"></a>

After you create a GCP connector, you can adjust the scope of the connector by changing the GCP projects or Google Cloud locations that it monitors. If you adjust the scope, changes can take a few hours to take effect. Full evaluation of newly added GCP projects can take up to 24 hours.

Before you adjust the scope, note the following:
+ The scope of a customer-managed connector cannot exceed the scope of any existing service-linked connector in the same account and Region.
+ When you expand the scope, Security Hub CSPM begins generating findings for new resources after AWS Config collects their configuration data.
+ When you reduce the scope, existing findings for removed resources transition to an archived state.

## Verify the health of a GCP connector
<a name="securityhub-gcp-setup-securityhub-verify"></a>

You can check the health of a GCP connector at any time. In the Security Hub CSPM console, choose **Integrations**, and then choose the **Configured integrations** tab. Confirm that **Health status** is **Connected** and **Enablement status** is **Enabled**.

Findings for resources with Cloud Audit Logs events typically appear within a few hours. The resource inventory can take several hours to reflect new resources. To validate inventory, use a long-lived resource and check its `ResourceDetailCaptureTime`. Full evaluation of all existing resources can take up to 24 hours.

**Note**  
Connector health status is eventually consistent, and health checks run periodically. When Security Hub CSPM can no longer authenticate to your GCP environment, **Health status** changes to **Failed** or **Degraded**, typically within an hour, with an actionable message. After you fix the issue, the status can take up to 24 hours to return to **Connected**.  
A **Failed** or **Degraded** status after a recent fix does not necessarily indicate an ongoing problem.
The health check does not detect every failure. A Pub/Sub backlog, a stale resource feed, or a problem that cached credentials mask can leave the status at **Connected**. For real-time visibility into recording failures, check the CloudWatch metrics for AWS Config and the Pub/Sub subscription metrics in GCP.

## Troubleshoot a GCP connector
<a name="securityhub-gcp-setup-securityhub-tshoot"></a>

If **Health status** is not **Connected**, open the integration details page and choose **Get diagnostic tools**. Copy or download the diagnostic script and run it in Google Cloud Shell. The script only reads your configuration and makes no changes. Fix each check that fails, and then use the following information to diagnose and resolve common problems.

**Health status is Failed or Degraded**  
This issue typically occurs if workload identity federation is not configured correctly in GCP, and AWS cannot exchange its token for GCP credentials.  
To address this issue, verify that the OIDC provider's issuer matches your Token Issuer URL, that its audience is `https://sts.googleapis.com`, and that its attribute condition lists the role ARNs for your AWS account exactly as shown in [Step 2: Configure workload identity federation](securityhub-gcp-setup-gcp.md#securityhub-gcp-setup-gcp-federation). Also verify that the pool, the provider, and the service account are all enabled, and that the service account has a `roles/iam.workloadIdentityUser` binding for each role.

**Health status is Connected but no findings appear**  
This issue most often occurs if the connector was created in a different AWS Region than the one the setup script was generated for, or if no GCP standard is enabled. AWS Config discovers Pub/Sub subscriptions by a label that includes the AWS Region, and a mismatch means no subscription is found.  
To address this issue, confirm that at least one GCP standard is enabled. Then confirm that each subscription has the label `aws-config-discovery={{aws-account-id}}-{{aws-region}}-{{management-project}}` with the Region in which you created the connector. If you created the connector in a different Region, run the setup script again from that Region. Also confirm that the subscriptions are pull subscriptions with no message filter, that they are attached to their topics, and that the service account has `roles/pubsub.subscriber` on each one.

**No resource changes are detected**  
This issue can occur if the organization log sink or the Cloud Asset Inventory feed is not delivering messages.  
To address this issue, verify that the sink `config-lifecycle-sink-{{aws-account-id}}` is enabled, has no active exclusions, and that its writer identity has `roles/pubsub.publisher` on the lifecycle topic. Verify that the feed `config-cai-feed-{{aws-account-id}}` exists on the organization and targets the asset topic. Check the Pub/Sub `IncomingMessages` metric on both topics. Also verify that Data Access audit logging is enabled for all services on the organization and that no principals relevant to the integration are exempted.

**Unable to record some GCP resources**  
The error can occur for any of the following reasons:  
+ A required GCP API is not enabled in the management project.
+ The service account's organization role bindings were removed or do not cover all required roles.
+ A project in the connector scope is not part of the organization.
To address the error, do the following:  

1. To confirm that your environment meets all requirements, review [Prerequisites for Google Cloud Platform](securityhub-gcp-prereqs.md#securityhub-gcp-prereqs-gcp).

1. Confirm that all APIs listed in [Step 1: Enable GCP APIs](securityhub-gcp-setup-gcp.md#securityhub-gcp-setup-gcp-api-permissions) are enabled.

1. Verify that the service account has the `securityHubConfigReader` custom role and the other roles listed in [Step 4: Assign GCP IAM roles](securityhub-gcp-setup-gcp.md#securityhub-gcp-setup-gcp-iam) at the organization scope.

**The setup script stopped with an error**  
The setup script checks the state of every resource before changing it, and stops with a message that names the problem and the command that fixes it. Common causes are missing permissions on the organization or management project, a resource with the expected name that was created by another tool, or an audit-log exemption that affects the integration.  
After you fix the reported problem, run the script again. Re-running the script is safe: it creates only what is missing and never deletes resources or revokes permissions.

**The setup script finished but reported that setup is incomplete**  
The setup script configures the resources and then verifies the organization audit configuration. It exits with status 3 and prints `Security Hub GCP setup INCOMPLETE` when a principal in your organization is exempt from an audit log event that the integration needs. The script never removes an audit logging exemption that you configured. To address this issue, remove the listed `exemptedMembers` entries from the organization audit configuration, and then run the script again.

## How Security Hub CSPM handles resource identifiers
<a name="securityhub-gcp-setup-securityhub-identifiers"></a>

By enabling your GCP integration for AWS Security Hub CSPM, resource identifiers from other cloud providers will be stored in AWS Config, AWS Security Hub CSPM, and other AWS services (as needed) as metadata related to the management of the corresponding resource configuration data collected from the other cloud providers. Such resource identifiers do not constitute Your Content, and we recommend you do not include sensitive, confidential, or personally identifiable information in them.

The following identifiers from your connected cloud environment are stored and used by AWS to provide multicloud security capabilities:
+ **Resource identifiers:** Google Organization ID, Project ID, Location, Resource ID (IDs or Names, Resource Type)

Relationships among these identifiers - including how resources relate to one another and how findings relate to resources - are also stored as service metadata. AWS uses these identifiers for resource correlation, associating findings to resources, service operational logging, and de-duplication.

## Available controls for GCP
<a name="securityhub-gcp-controls"></a>

After you enable the CIS Google Cloud Platform Foundation Benchmark v4.0.0 standard, the following 69 controls evaluate your GCP resources.


**Available GCP controls**  

| Control title | Resource type | Standard | 
| --- | --- | --- | 
| GCP API keys should not exist | apikeys.googleapis.com/V2Key | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP API keys should be restricted to specified hosts and apps | apikeys.googleapis.com/V2Key | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP API keys should be restricted to only the APIs an application needs | apikeys.googleapis.com/V2Key | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP API keys should be rotated every 90 days | apikeys.googleapis.com/V2Key | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| App Engine versions should enforce HTTPS on all reachable URL handlers | appengine.googleapis.com/Version | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| BigQuery datasets should be encrypted with a customer-managed encryption key | bigquery.googleapis.com/Dataset | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| BigQuery datasets should not be anonymously or publicly accessible | bigquery.googleapis.com/Dataset | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| BigQuery tables should be encrypted with a customer-managed encryption key | bigquery.googleapis.com/Table | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for MySQL instances should have the 'local\_infile' flag set to 'off' | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for MySQL instances should have the 'skip\_show\_database' flag set to 'on' | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for PostgreSQL instances should have 'log\_connections' set to 'on' | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for PostgreSQL instances should have 'log\_disconnections' set to 'on' | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for PostgreSQL instances should have 'log\_error\_verbosity' set to 'default' | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for PostgreSQL instances should have 'log\_statement' set | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for SQL Server instances should not have 'contained database authentication' set to 'on' | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for SQL Server instances should have the '3625' trace flag set to 'on' | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for PostgreSQL instances should have 'log\_min\_messages' at an appropriate severity level | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL instances should require SSL/TLS for all incoming connections | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for SQL Server instances should not have the 'user options' database flag configured | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for PostgreSQL instances should have 'log\_min\_error\_statement' set to 'error' or stricter | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for SQL Server instances should have the remote access flag set to off | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for PostgreSQL instances should have the cloudsql.enable\_pgaudit flag set to on | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL database instances should have automated backups enabled | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for PostgreSQL instances should have the log\_min\_duration\_statement flag set to -1 | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for SQL Server instances should have the external scripts enabled flag set to off | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL instances should not permit 0.0.0.0/0 or ::/0 in authorized networks | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL instances should not have a public IP address | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud SQL for SQL Server instances should have the 'user connections' database flag set to a non-limiting value | sqladmin.googleapis.com/DatabaseInstance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud Storage buckets should have Uniform Bucket-Level Access enabled | storage.googleapis.com/Bucket | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine projects should have OS Login enabled | compute.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should have Shielded VM enabled | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| VPC networks should not be the pre-created default network | compute.googleapis.com/Network | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should not have public IP addresses | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should have interactive serial console access disabled | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should block project-wide SSH keys | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| VPC networks should not be legacy networks | compute.googleapis.com/Network | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| VPC subnetworks should have VPC Flow Logs enabled | compute.googleapis.com/Subnetwork | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should not use the default service account with full access to all Cloud APIs | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Backend services with an application load balancer scheme should have request logging enabled | compute.googleapis.com/BackendService | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should not use the default service account | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Instance group-backed backend services with Identity-Aware Proxy enabled should restrict VPC firewall ingress to Google IP ranges | compute.googleapis.com/BackendService | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| VPC networks should have Cloud DNS logging enabled | compute.googleapis.com/Network | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine firewall rules should restrict SSH access from the internet | compute.googleapis.com/Firewall | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine firewall rules should restrict RDP access from the internet | compute.googleapis.com/Firewall | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should have IP forwarding disabled | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should have Confidential Computing enabled | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Compute Engine instances should have OS Login enabled | compute.googleapis.com/Instance | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| HTTPS load balancer target proxies should use an SSL policy that forbids weak cipher suites and requires at least TLS 1.2 | compute.googleapis.com/TargetHttpsProxy | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| SSL proxy load balancer target proxies should use an SSL policy that forbids weak cipher suites and requires at least TLS 1.2 | compute.googleapis.com/TargetSslProxy | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Dataproc clusters should be encrypted with a customer-managed encryption key | dataproc.googleapis.com/Cluster | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects with BigQuery data should have a Sensitive Data Protection discovery scan configured | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud DNS managed zones should not use RSASHA1 for the DNSSEC zone-signing key | dns.googleapis.com/ManagedZone | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud DNS public zones should have DNSSEC enabled | dns.googleapis.com/ManagedZone | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud DNS public zones should not use RSASHA1 for the DNSSEC key-signing key | dns.googleapis.com/ManagedZone | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Service account keys should be system-managed | iam.googleapis.com/ServiceAccountKey | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have Cloud Asset Inventory enabled | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Service account user-managed keys should be rotated within 90 days | iam.googleapis.com/ServiceAccountKey | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud KMS keys should have a rotation period no longer than the configured maximum | cloudkms.googleapis.com/CryptoKey | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Cloud KMS keys should be scheduled to rotate within the configured maximum number of days | cloudkms.googleapis.com/CryptoKey | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a log metric filter and alert for audit configuration changes | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a log metric filter and alert for VPC network changes | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a log metric filter and alert for project ownership changes | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a log metric filter and alert for custom role changes | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a log metric filter and alert for VPC firewall rule changes | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a log metric filter and alert for VPC network route changes | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a log metric filter and alert for Cloud Storage IAM permission changes | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a log metric filter and alert for Cloud SQL instance configuration changes | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| GCP projects should have a project-level logging sink that captures all log entries | cloudresourcemanager.googleapis.com/Project | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 
| Log-sink Cloud Storage buckets should have a locked retention policy | logging.googleapis.com/LogSink | CIS Google Cloud Platform Foundation Benchmark v4.0.0 | 