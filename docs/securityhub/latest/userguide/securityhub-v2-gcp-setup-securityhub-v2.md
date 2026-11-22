

# Configuring Security Hub to integrate with Google Cloud Platform

After you complete the [prerequisite tasks](securityhub-v2-gcp-prereqs.md) and [configure your Google Cloud Platform (GCP) environment](securityhub-v2-gcp-setup-gcp.md), you can configure AWS Security Hub to integrate with GCP. To configure Security Hub to integrate with GCP, you create a connector. You can create the connector from a delegated administrator account or the management account. After you create the connector, the following events occur:

1. Security Hub validates the GCP credentials and connectivity to your GCP environment. This process can take several minutes.

1. Security Hub creates service-linked connectors in Security Hub CSPM and Amazon Inspector. These connectors ensure that posture management checks and vulnerability scanning match the scope you defined in Security Hub.

1. AWS Config begins discovering GCP resources using the federated identity credentials.

1. Security Hub automatically enables the CIS Google Cloud Platform Foundation Benchmark v4.0.0 standard in CSPM for your GCP resources.

1. Findings for resources with Cloud Audit Logs events typically appear within a few hours. The asset inventory can take several hours to reflect new resources. To validate inventory, use a long-lived resource and check its `ResourceDetailCaptureTime`. Full evaluation of all existing resources can take up to 24 hours.

**Topics**
+ [Create a connector](#securityhub-v2-gcp-setup-securityhub-v2-proc)
+ [Adjust the scope of a connector](#securityhub-v2-gcp-setup-securityhub-v2-manage)
+ [Verify the health of a connector](#securityhub-v2-gcp-setup-securityhub-v2-verify)
+ [Troubleshoot a connector](#securityhub-v2-gcp-setup-securityhub-v2-tshoot)
+ [Resource and finding identifiers](#securityhub-v2-gcp-setup-securityhub-v2-identifiers)

## Create a GCP connector
<a name="securityhub-v2-gcp-setup-securityhub-v2-proc"></a>

To create a GCP connector for your environment, complete the following steps by using the AWS Security Hub console or the API.

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1](https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1).

1. In the navigation pane, choose **Integrations**.

1. Choose **Add integration**. On the **Integrations catalog** tab, find the **GCP** card and choose **Add integration**. The **Add GCP integration** page opens.

1. In the **Security capabilities** section, choose whether you want the **Network reachability scanning** feature enabled. This feature is enabled by default for the account where you are enabling the GCP integration, and can be unchecked before completing your connector setup. If an organization policy is blocking this feature for your account, it does not appear as an option. For more information, see [Network Scanning in Security Hub](securityhub-v2-network-scanning.md).

1. In the **Monitoring targets** section, for **Organization ID**, enter your numeric GCP organization ID. You can find it in the GCP console under *IAM & Admin > Settings*, or by running `gcloud organizations list`.

1. Choose the scope and locations to monitor:
   + For **GCP scope selection**, choose **Organization** to monitor all current and future projects in the organization, or **Selected projects** to monitor only the projects that you specify. If you choose **Selected projects**, enter up to 100 project IDs.
   + For **Google Cloud location coverage**, choose **Record all locations** to monitor resources in every Google Cloud location, including locations added in the future, or **Choose specific locations** to monitor only the regions, zones, multi-regions, and dual-regions that you select. Selecting a region also selects all of its zones. Global resources, such as IAM service accounts and VPC networks, are always recorded regardless of your selection.
**Note**  
Selecting a region in the console also selects its zones. If you create or update the connector with the `CreateConnectorV2` or `UpdateConnectorV2` API operation, a region in the location list does not include its zones. List each zone that contains resources to monitor, for example `us-central1-a`. The API does not accept the value `global`.
**Note**  
If you already created a connector in Security Hub CSPM or Amazon Inspector for the same GCP organization, the scope of the connector in Security Hub must include the same projects and locations as the connector in Security Hub CSPM or Inspector.

1. In the **Data connection** section, choose **Help me generate a script** to have the console generate a setup script, or **I will create GCP resources myself** if you configured GCP manually.

   If you chose the script option, enter the **Management project ID** (the GCP project that hosts the workload identity federation pool) and the **Issuer URL** (the Token Issuer URL from IAM Outbound Identity Federation), and then choose **Open setup script**. Run the script in your GCP environment as described in [Configuring Google Cloud Platform to integrate with Security Hub](securityhub-v2-gcp-setup-gcp.md). The management project ID and issuer URL are used only to generate the script; they are not stored with the connector.

1. Under **Provide connector details**, paste the values that the setup script prints when it completes:
   + For **Service account email**, enter the email of the service account that the script created, in the format `config-sa-{{aws-account-id}}@{{management-project}}.iam.gserviceaccount.com`.
   + For **Workload identity pool provider**, enter the workload identity pool provider resource name, in the format `projects/{{project-number}}/locations/global/workloadIdentityPools/connector-pool-{{aws-account-id}}/providers/connector-oidc-{{aws-account-id}}`.

   Then choose **Create data connection**.

1. Configure additional settings by doing the following:
   + For **Name**, enter a unique name for the connector. The name can contain up to 50 alphanumeric characters and it can include hyphens.
**Note**  
The connector name cannot be changed after creation.
   + For **Description**, optionally enter a brief description of the connector. The description can contain up to 200 characters.
**Important**  
Names and descriptions are used to identify your content. Do not include sensitive, confidential, or personally identifiable information (PII) in them.

1. If the **IAM roles** section appears, create the listed IAM roles in your AWS account. For details, see [IAM roles for GCP VM scanning through Amazon Inspector](#securityhub-v2-gcp-setup-securityhub-v2-iam). Then select **I confirm that I have created the required IAM roles in my account.** You cannot connect until you select this checkbox.

1. Review the connector configuration.

1. When you finish entering and reviewing the settings, choose **Connect**.

### IAM roles for GCP VM scanning through Amazon Inspector
<a name="securityhub-v2-gcp-setup-securityhub-v2-iam"></a>

To enable VM scanning through Amazon Inspector, you must create the following IAM resources in your AWS account. The role names include your numeric GCP {{organization-id}}. The console lists the exact role names and permissions under **IAM roles** when you create the connector.

In each role name and policy, replace {{organization-id}} with your numeric GCP organization ID and {{account-id}} with your AWS account ID. These roles are the same roles that Amazon Inspector documents for its own GCP connector. For details, see [Configuring Amazon Inspector to integrate with Google Cloud Platform](https://docs.aws.amazon.com/inspector/latest/user/inspector-gcp-setup-inspector.html) in the *Amazon Inspector User Guide*.

**Inspector2VmScannerRole-{{organization-id}}**

Used by the Amazon Inspector VM Scanner agent running on Compute Engine VM instances to send scan telemetry to Amazon Inspector. This role trusts Google-signed ID tokens directly, so you don't need an IAM OIDC identity provider.

There is one trust policy for each way that the agent can get credentials. Use the one that you need:
+ `AllowListedServiceAccounts` trusts the service accounts that are attached to your VM instances. List the numeric unique ID of each service account in both `accounts.google.com:aud` and `accounts.google.com:sub`.
+ `AllowBridgeMinter` trusts the VM credential bridge that the setup script creates. With the bridge, new VM instances and service accounts need no change to the trust policy.

**Trust policy (service account allowlist):**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Sid": "AllowListedServiceAccounts",
          "Effect": "Allow",
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Principal": {
              "Federated": "accounts.google.com"
          },
          "Condition": {
              "StringEquals": {
                  "accounts.google.com:aud": [
                      "{{service-account-unique-id}}"
                  ],
                  "accounts.google.com:sub": [
                      "{{service-account-unique-id}}"
                  ],
                  "accounts.google.com:oaud": "api://AWSInspector"
              }
          }
      }
  ]
}
```

**Trust policy (VM credential bridge):**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Sid": "AllowBridgeMinter",
          "Effect": "Allow",
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Principal": {
              "Federated": "accounts.google.com"
          },
          "Condition": {
              "StringEquals": {
                  "accounts.google.com:oaud": "api://AWSInspector"
              },
              "StringLike": {
                  "accounts.google.com:email": "inspector-vmscan-{{account-id}}@*.iam.gserviceaccount.com"
              },
              "NumericEquals": {
                  "accounts.google.com:google/organization_number": "{{organization-id}}"
              }
          }
      }
  ]
}
```

**Permission policy (TelemetryPolicy):**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "inspector2-telemetry:*",
          "Resource": "*"
      }
  ]
}
```

**Tags:**
+ `inspector-managed` = `true`

**Inspector2SSMFederationRole-{{organization-id}}**

Enables OIDC federation to GCP for secure cross-cloud authentication. This role is assumed by the AssumeRole and DispatchRole, and by AWS Systems Manager, to obtain web identity tokens for GCP operations.

**Trust policy:**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Principal": {
              "AWS": "arn:aws:iam::{{account-id}}:root"
          },
          "Condition": {
              "ArnLike": {
                  "aws:PrincipalArn": [
                      "arn:aws:iam::{{account-id}}:role/Inspector2SSMAssumeRole-{{organization-id}}",
                      "arn:aws:iam::{{account-id}}:role/Inspector2SSMDispatchRole-{{organization-id}}"
                  ]
              },
              "StringEquals": {
                  "aws:PrincipalTag/caller": "SSM"
              }
          }
      },
      {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Principal": {
              "Service": [
                  "ssm.amazonaws.com"
              ]
          }
      }
  ]
}
```

**Permission policy (FederationPolicy):**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Effect": "Allow",
          "Action": [
              "sts:GetWebIdentityToken",
              "sts:TagGetWebIdentityToken"
          ],
          "Resource": "*",
          "Condition": {
              "ForAnyValue:StringEquals": {
                  "sts:IdentityTokenAudience": [
                      "https://sts.googleapis.com"
                  ]
              }
          }
      }
  ]
}
```

**Tags:**
+ `caller` = `SSM`
+ `inspector-managed` = `true`

**Inspector2SSMAssumeRole-{{organization-id}}**

Executes AWS Systems Manager Automation to install the Amazon Inspector VM Scanner agent on Compute Engine VM instances. This role assumes the FederationRole, retrieves automation documents, starts and reads automation executions, and reports install results to AWS Systems Manager.

**Trust policy:**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Principal": {
              "Service": [
                  "ssm.amazonaws.com"
              ]
          },
          "Condition": {
              "StringEquals": {
                  "aws:SourceAccount": "{{account-id}}"
              }
          }
      }
  ]
}
```

**Permission policy (AssumeRolePolicy):**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": "arn:aws:iam::{{account-id}}:role/Inspector2SSMFederationRole-{{organization-id}}"
      },
      {
          "Effect": "Allow",
          "Action": "iam:PassRole",
          "Resource": "arn:aws:iam::{{account-id}}:role/Inspector2SSMAssumeRole-{{organization-id}}",
          "Condition": {
              "StringEquals": {
                  "iam:PassedToService": [
                      "ssm.amazonaws.com"
                  ]
              }
          }
      },
      {
          "Effect": "Allow",
          "Action": "iam:PassRole",
          "Resource": "arn:aws:iam::{{account-id}}:role/AmazonEC2RunCommandRoleForManagedInstances",
          "Condition": {
              "StringEquals": {
                  "iam:PassedToService": [
                      "ssm.amazonaws.com"
                  ]
              }
          }
      },
      {
          "Effect": "Allow",
          "Action": [
              "ssm:CreateActivation",
              "ssm:DeleteActivation",
              "ssm:DescribeActivations",
              "ssm:DescribeInstanceInformation",
              "ssm:PutConfigurePackageResult",
              "iam:ListRoleTags"
          ],
          "Resource": "*"
      },
      {
          "Effect": "Allow",
          "Action": "ssm:AddTagsToResource",
          "Resource": [
              "arn:aws:ssm:*:{{account-id}}:activation/*",
              "arn:aws:ssm:*:{{account-id}}:managed-instance/*"
          ]
      },
      {
          "Effect": "Allow",
          "Action": "ssm:GetDocument",
          "Resource": [
              "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnGcp",
              "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnGcp-VerifyInstallation",
              "arn:aws:ssm:*:*:document/AWS-InstallSSMAgentOnGCP",
              "arn:aws:ssm:*::document/AmazonInspector2-InspectorVmScanner"
          ]
      },
      {
          "Effect": "Allow",
          "Action": "ssm:StartAutomationExecution",
          "Resource": [
              "arn:aws:ssm:*:*:document/AWS-InstallSSMAgentOnGCP-*",
              "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnGcp-*",
              "arn:aws:ssm:*:*:automation-definition/AWS-InstallDistributorPackageOnGcp-VerifyInstallation:*",
              "arn:aws:ssm:*:{{account-id}}:automation-execution/*"
          ]
      },
      {
          "Effect": "Allow",
          "Action": [
              "ssm:GetAutomationExecution",
              "ssm:DescribeAutomationExecutions",
              "ssm:DescribeAutomationStepExecutions"
          ],
          "Resource": "arn:aws:ssm:*:{{account-id}}:automation-execution/*"
      },
      {
          "Effect": "Allow",
          "Action": "ssm:GetCloudConnector",
          "Resource": "*"
      }
  ]
}
```

**Tags:**
+ `caller` = `SSM`
+ `inspector-managed` = `true`

**Inspector2SSMDispatchRole-{{organization-id}}**

Dispatches Amazon Inspector VM Scanner agent installation via AWS Systems Manager Automation. This role starts automation executions and passes the AssumeRole to AWS Systems Manager.

**Trust policy:**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Principal": {
              "Service": [
                  "ssm.amazonaws.com"
              ]
          },
          "Condition": {
              "StringEquals": {
                  "aws:SourceAccount": "{{account-id}}"
              }
          }
      }
  ]
}
```

**Permission policy (DispatchPolicy):**

```json
{
  "Version":"2012-10-17",			 	 	 
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "iam:PassRole",
          "Resource": "arn:aws:iam::{{account-id}}:role/Inspector2SSMAssumeRole-{{organization-id}}",
          "Condition": {
              "StringEquals": {
                  "iam:PassedToService": [
                      "ssm.amazonaws.com"
                  ]
              }
          }
      },
      {
          "Effect": "Allow",
          "Action": "ssm:StartAutomationExecution",
          "Resource": [
              "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnGcp",
              "arn:aws:ssm:*:{{account-id}}:automation-execution/*"
          ]
      },
      {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": "arn:aws:iam::{{account-id}}:role/Inspector2SSMFederationRole-{{organization-id}}"
      },
      {
          "Effect": "Allow",
          "Action": [
              "ssm:DescribeInstanceInformation",
              "ssm:ListCloudConnectors",
              "ssm:GetCloudConnector",
              "iam:ListRoleTags"
          ],
          "Resource": "*"
      }
  ]
}
```

**Tags:**
+ `caller` = `SSM`
+ `inspector-managed` = `true`

**Prerequisites for VM scanning**

Each project that contains VMs to scan must be included when you run the GCP setup script, which enables VM Manager and configures the OS Config service agents in that project. Each Compute Engine VM instance that you want to scan must have an attached service account and must run a supported operating system. VM Manager can take up to 24 hours to apply the OS policy that installs the agent. To exclude a VM instance from scanning, apply the label `amazoninspectorvmexclusion` with any value. For details, see [Configuring Amazon Inspector to integrate with Google Cloud Platform](https://docs.aws.amazon.com/inspector/latest/user/inspector-gcp-setup-inspector.html) in the *Amazon Inspector User Guide*.

After you create the connector, Security Hub begins monitoring your GCP environment. You can check the status of the connector on the **Integrations** page.

## Adjust the scope of a GCP connector
<a name="securityhub-v2-gcp-setup-securityhub-v2-manage"></a>

After you create a GCP connector, you can adjust the scope of the connector by changing the GCP projects or Google Cloud locations that it monitors. Scope changes can take a few hours to take effect. Full evaluation of newly added GCP projects can take up to 24 hours.

Before you adjust the scope of a connector, note the following:
+ When you change the scope of a connector in Security Hub, the associated service-linked connectors in Security Hub CSPM and Amazon Inspector are automatically updated to match.
+ The scope of a Security Hub connector can never be less than any existing customer-managed connector in Security Hub CSPM or Amazon Inspector for the same GCP organization.
+ If you add projects to the connector scope and vulnerability management is enabled, the console prompts you to re-run the setup script so that it configures VM scanning in the new projects. Re-running the script does not change your existing configuration.

## Verify the health of a GCP connector
<a name="securityhub-v2-gcp-setup-securityhub-v2-verify"></a>

You can check the health of a GCP connector at any time to confirm that Security Hub is receiving data from your GCP environment.

**To verify the health of a connector**

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1](https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1).

1. In the navigation pane, choose **Integrations** and select your GCP connector.

1. On the **Configured integrations** tab, verify that **Health status** is **Connected** and **Enablement status** is **Enabled**. The first health check runs about 10 minutes after you create the connector. If a column shows a different value, see [Troubleshoot a GCP connector](#securityhub-v2-gcp-setup-securityhub-v2-tshoot).

1. Navigate to **Findings** and add the filter **Cloud provider** = **GCP** to confirm that findings are generated for your GCP resources. In the `GetFindingsV2` API operation, filter on `resources.provider` = `GCP`.

1. Check the **Security standards** page to confirm the CIS Google Cloud Platform Foundation Benchmark v4.0.0 standard shows controls in PASSED or FAILED status (not all NO\_DATA).

**Note**  
Connector health status is eventually consistent, and health checks run periodically. When Security Hub can no longer authenticate to your GCP environment, **Health status** changes to **Failed** or **Degraded**, typically within an hour, with an actionable message. After you fix the issue, the status can take up to 24 hours to return to **Connected**.  
The health check does not detect every failure. A Pub/Sub backlog, a stale resource feed, or a problem that cached credentials mask can leave the status at **Connected**. For real-time visibility into recording failures, check the CloudWatch metrics for AWS Config and the Pub/Sub subscription metrics in GCP.
A **Failed** or **Degraded** status after a recent fix does not necessarily indicate an ongoing problem.

## Troubleshoot a GCP connector
<a name="securityhub-v2-gcp-setup-securityhub-v2-tshoot"></a>

If you experience issues with your connector, review the following common issues and resolutions.

If **Health status** shows **Failed** or **Degraded**, choose the status, and then choose **Get diagnostic tools**. Copy or download the diagnostic script and run it in Google Cloud Shell. The script only reads your configuration and makes no changes. Fix each check that fails, and then use the following information.

**Health status is Failed or Degraded**  
This issue typically occurs if workload identity federation is not configured correctly in GCP, and AWS cannot exchange its token for GCP credentials.  
To address this issue, verify that the OIDC provider's issuer matches your Token Issuer URL, that its allowed audiences include `https://sts.googleapis.com`, and that its attribute condition lists the role ARNs for your AWS account exactly as shown in [Step 2: Configure workload identity federation](securityhub-v2-gcp-setup-gcp.md#securityhub-v2-gcp-setup-gcp-federation). Also verify that the pool, the provider, and the service account are all enabled, and that the service account has a `roles/iam.workloadIdentityUser` binding for each role.

**Health status is Connected but no findings or resources appear**  
This issue most often occurs if the connector was created in a different AWS Region than the one the setup script was generated for. AWS Config discovers Pub/Sub subscriptions by a label that includes the AWS Region, and a mismatch means no subscription is found.  
To address this issue, confirm that each subscription has the label `aws-config-discovery={{aws-account-id}}-{{aws-region}}-{{management-project}}` with the Region in which you created the connector. If you created the connector in a different Region, run the setup script again from that Region. Also confirm that the subscriptions are pull subscriptions with no message filter, that they are attached to their topics, and that the service account has `roles/pubsub.subscriber` on each one.

**No resource changes are detected**  
This issue can occur if the organization log sink or the Cloud Asset Inventory feed is not delivering messages.  
To address this issue, verify that the sink `config-lifecycle-sink-{{aws-account-id}}` is enabled, has no active exclusions, and that its writer identity has `roles/pubsub.publisher` on the lifecycle topic. Verify that the feed `config-cai-feed-{{aws-account-id}}` exists on the organization and targets the asset topic. Check the Pub/Sub `IncomingMessages` metric on both topics. Also verify that Data Access audit logging is enabled for all services on the organization and that no principals relevant to the integration are exempted.

**All controls show NO\_DATA**  
This issue can occur if the connector is disabled or if AWS Config cannot reach your GCP environment.  
To address this issue, verify that the connector is enabled and that the service account has the `securityHubConfigReader` custom role and the other roles listed in [Step 4: Assign GCP IAM roles](securityhub-v2-gcp-setup-gcp.md#securityhub-v2-gcp-setup-gcp-iam) at the organization scope.

**Unable to record some GCP resources**  
The error can occur for any of the following reasons:  
+ A required GCP API is not enabled in the management project.
+ The service account's organization role bindings were removed or do not cover all required roles.
+ A project in the connector scope is not part of the organization.
To address the error, do the following:  

1. To confirm that your environment meets all requirements, review [Prerequisites for Google Cloud Platform](securityhub-v2-gcp-prereqs.md#securityhub-v2-gcp-prereqs-gcp).

1. Confirm that all APIs listed in [Step 1: Enable GCP APIs](securityhub-v2-gcp-setup-gcp.md#securityhub-v2-gcp-setup-gcp-api-permissions) are enabled.

1. Verify the service account's role bindings at the organization scope.

**VM scanning fails with CREATE\_ASSOCIATION\_FAILED**  
This issue occurs if VM scanning reports `CREATE_ASSOCIATION_FAILED` and the error names the `AWS-InstallDistributorPackageOnGcp` or `AWS-InstallSSMAgentOnGCP` document as missing. The AWS-owned AWS Systems Manager document is not yet available in the AWS Region of the connector.  
To address this issue, in the AWS Systems Manager console for the connector's AWS Region, verify that the `AWS-InstallDistributorPackageOnGcp` and `AWS-InstallSSMAgentOnGCP` documents are listed under **Owned by Amazon**. After the document is available, retry VM scanning, or delete and recreate the connector.

**The setup script stopped with an error**  
The setup script checks the state of every resource before changing it, and stops with a message that names the problem and the command that fixes it. Common causes are missing permissions on the organization or management project, a resource with the expected name that was created by another tool, or an audit-log exemption that affects the integration.  
After you fix the reported problem, run the script again. Re-running the script is safe: it creates only what is missing and never deletes resources or revokes permissions.

**The setup script finished but reported that setup is incomplete**  
The setup script configures the resources and then verifies the organization audit configuration. It exits with status 3 and prints `Security Hub GCP setup INCOMPLETE` when a principal in your organization is exempt from an audit log event that the integration needs. The script never removes an audit logging exemption that you configured. To address this issue, remove the listed `exemptedMembers` entries from the organization audit configuration, and then run the script again.  
The script exits with status 4 when a VM scanning service account (`inspector-vmscan-{{aws-account-id}}`) in one of your VM projects has a user-managed key or an IAM binding that the script did not create. The *Needs attention* list at the end of the output names each one and gives the command that removes it. Remove them, and then run the script again.

## How Security Hub handles resource and finding identifiers
<a name="securityhub-v2-gcp-setup-securityhub-v2-identifiers"></a>

By enabling your GCP integration for AWS Security Hub, resource and security finding identifiers from other cloud providers are stored in AWS Config, Security Hub, and other AWS services (as needed) as metadata related to the management of the corresponding resource configuration and security finding data collected from the other cloud providers. Such identifiers do not constitute Your Content. Do not include sensitive, confidential, or personally identifiable information in them.

The following identifiers from your connected cloud environment are stored and used by AWS to provide multicloud security capabilities:
+ **Resource identifiers:** Google Organization ID, Project ID, Location, Resource ID (IDs or Names, Resource Type)
+ **Security Finding identifiers:** the unique identifiers assigned to each security finding generated by the detecting service.

Relationships among these identifiers - including how resources relate to one another and how findings relate to resources - are also stored as service metadata. AWS uses these identifiers for resource correlation, associating findings to resources, service operational logging, and de-duplication.