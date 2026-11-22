

# Configuring Google Cloud Platform to integrate with Security Hub CSPM

After you complete the [prerequisite tasks](securityhub-gcp-prereqs.md), you can configure your Google Cloud Platform (GCP) environment to support integration with AWS Security Hub CSPM. To help you do this, the Security Hub CSPM console generates a setup script that is customized for your configuration.

**To generate the setup script**

1. Open the Security Hub CSPM console.

1. In the navigation pane, choose **Integrations**.

1. Choose **Add integration**. On the **Integrations catalog** tab, find the **GCP** card and choose **Add integration**. The **Add GCP integration** page opens. If a GCP connector already exists, the card shows **View configured integrations** instead.

1. In **Monitoring targets**, enter your **Organization ID** and choose the scope and locations to monitor.

1. In **Data connection**, choose **Help me generate a script**, enter the **Management project ID** and the **Issuer URL**, and then choose **Open setup script**. Copy or download the script.

To run the script, open [Google Cloud Shell](https://cloud.google.com/shell) on the Google Cloud website, or a terminal with the gcloud CLI installed, and authenticate with an account that has the permissions listed in the prerequisites:

```
$ gcloud auth login
```

The script also requires `jq` and the gcloud beta component. Edit the `CHANGEME` values at the top of the script only if the console did not fill them in for you.

**Important**  
The script labels your Pub/Sub subscriptions with the AWS account, the AWS Region you generated the script in, and the management project. AWS Config discovers the subscriptions by this label. You must create the connector in the same AWS Region. If you create it in a different Region, the connector reports a healthy status but receives no data.

When you run the script, it performs a series of tasks. The following sections describe each task that the script performs. If your organization restricts script execution, you can perform these tasks manually, using this topic as a guide. The script is idempotent: you can run it again to add projects or repair configuration drift, and it never deletes resources or revokes permissions. After you configure your GCP environment, you can [configure Security Hub CSPM to integrate with GCP](securityhub-gcp-setup-securityhub.md).

Steps 1–7 configure the resources that Security Hub CSPM uses: required APIs, workload identity federation, the service account, GCP IAM roles, Pub/Sub, Cloud Audit Logs export, and a Cloud Asset Inventory feed. If you also use Amazon Inspector for GCP, the Inspector setup adds its own resources; see [Integrating Amazon Inspector with Google Cloud Platform](https://docs.aws.amazon.com/inspector/latest/user/inspector-gcp.html) in the *Amazon Inspector User Guide*.

**Note**  
A single GCP service account is shared across AWS security services. If you also use Security Hub or Amazon Inspector for GCP, they use the same service account. You do not need to create separate service accounts for each AWS service.

Replace the placeholders in the commands in this topic with your own values. {{aws-account-id}} is your 12-digit AWS account ID, {{aws-region}} is the AWS Region code (for example, `us-east-1`), {{management-project}} is the GCP project that hosts the connector resources, {{project-number}} is its numeric project number, and {{organization-id}} is your numeric GCP organization ID.

**Topics**
+ [Step 1: Enable APIs](#securityhub-gcp-setup-gcp-api-permissions)
+ [Step 2: Configure workload identity federation](#securityhub-gcp-setup-gcp-federation)
+ [Step 3: Create a service account](#securityhub-gcp-setup-gcp-service-account)
+ [Step 4: Assign IAM roles](#securityhub-gcp-setup-gcp-iam)
+ [Step 5: Set up Pub/Sub](#securityhub-gcp-setup-gcp-pubsub)
+ [Step 6: Configure log export](#securityhub-gcp-setup-gcp-export)
+ [Step 7: Configure an asset feed](#securityhub-gcp-setup-gcp-asset-feed)

## Step 1: Enable GCP APIs
<a name="securityhub-gcp-setup-gcp-api-permissions"></a>

Enable the following APIs in the management project. These cover identity federation, Pub/Sub, logging, asset discovery, and the GCP services whose resources Security Hub CSPM evaluates. A read role on a service whose API is disabled returns an error instead of an empty inventory. The `gcloud services enable` command accepts a limited number of APIs in one call, so the script turns them on in two calls.

```
$ gcloud services enable \
  accesscontextmanager.googleapis.com apikeys.googleapis.com appengine.googleapis.com \
  artifactregistry.googleapis.com bigquery.googleapis.com cloudasset.googleapis.com \
  cloudfunctions.googleapis.com cloudkms.googleapis.com cloudresourcemanager.googleapis.com \
  compute.googleapis.com container.googleapis.com dataproc.googleapis.com \
  dlp.googleapis.com dns.googleapis.com eventarc.googleapis.com \
  --project {{management-project}}

$ gcloud services enable \
  firestore.googleapis.com iam.googleapis.com iamcredentials.googleapis.com \
  logging.googleapis.com monitoring.googleapis.com pubsub.googleapis.com \
  run.googleapis.com secretmanager.googleapis.com \
  serviceusage.googleapis.com sqladmin.googleapis.com sts.googleapis.com \
  storage.googleapis.com vpcaccess.googleapis.com \
  --project {{management-project}}
```

If a command fails with `UREQ_TOS_NOT_ACCEPTED`, accept the Google Cloud Terms of Service at [console.developers.google.com/terms/cloud](https://console.developers.google.com/terms/cloud) on the Google Cloud website, and run it again.

## Step 2: Configure workload identity federation
<a name="securityhub-gcp-setup-gcp-federation"></a>

Create a workload identity pool and an OIDC provider that trusts the token issuer of your AWS account. This lets AWS services authenticate to GCP without long-lived keys. One pool and provider serve every AWS Region for the account.

```
$ gcloud iam workload-identity-pools create connector-pool-{{aws-account-id}} \
  --location=global \
  --display-name="Config Connector Pool" \
  --project={{management-project}}
```

```
$ gcloud iam workload-identity-pools providers create-oidc connector-oidc-{{aws-account-id}} \
  --workload-identity-pool=connector-pool-{{aws-account-id}} \
  --location=global \
  --project={{management-project}} \
  --issuer-uri="https://{{uuid}}.tokens.sts.global.api.aws" \
  --allowed-audiences="https://sts.googleapis.com" \
  --attribute-mapping="google.subject=assertion.sub,attribute.aws_role=assertion.sub" \
  --attribute-condition="attribute.aws_role in ['arn:aws:iam::{{aws-account-id}}:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty']"
```

Key values:
+ **Issuer** – Your Token Issuer URL from IAM Outbound Identity Federation. This follows the format `https://{{uuid}}.tokens.sts.global.api.aws`.
+ **Audience** – `https://sts.googleapis.com`.
+ **Attribute condition** – The IAM role that can exchange a token. AWS Config authenticates using its service-linked role. The role ARN is the plain role ARN, not an assumed-role ARN. AWS creates the service-linked role automatically when you create the connector.

The following table lists the IAM roles that the provider admits, by capability.


| Capability | Role ARN admitted by the provider | 
| --- | --- | 
| Resource configuration discovery (AWS Config) | arn:aws:iam::{{aws-account-id}}:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty | 
| Vulnerability management (Amazon Inspector, if enabled) | Additional role ARNs documented in the Amazon Inspector User Guide. The Inspector setup script adds them to the same provider. | 

Note the provider resource name. You provide it as the **Workload identity pool provider** value when you create the connector in the Security Hub CSPM console:

```
projects/{{project-number}}/locations/global/workloadIdentityPools/connector-pool-{{aws-account-id}}/providers/connector-oidc-{{aws-account-id}}
```

## Step 3: Create a GCP service account
<a name="securityhub-gcp-setup-gcp-service-account"></a>

Create a service account in the management project. This service account is the identity that AWS uses in your GCP environment. It has no keys.

```
$ gcloud iam service-accounts create config-sa-{{aws-account-id}} \
  --project={{management-project}} \
  --display-name="Config Connector SA"
```

Note the **service account email**, `config-sa-{{aws-account-id}}@{{management-project}}.iam.gserviceaccount.com`. You provide this value when you create the connector in the Security Hub CSPM console.

Then allow each federated AWS role to impersonate the service account. Create one binding for each role ARN in the attribute condition from Step 2:

```
$ gcloud iam service-accounts add-iam-policy-binding \
  config-sa-{{aws-account-id}}@{{management-project}}.iam.gserviceaccount.com \
  --project={{management-project}} \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/{{project-number}}/locations/global/workloadIdentityPools/connector-pool-{{aws-account-id}}/attribute.aws_role/{{role-arn}}"
```

## Step 4: Assign GCP IAM roles
<a name="securityhub-gcp-setup-gcp-iam"></a>

The setup script grants the service account one custom role and four predefined roles at the **organization** scope. The grants are inherited by every project in the organization, so the service account can read resources even when the connector monitors only some projects.

First, create the custom role `securityHubConfigReader` at the organization. The role contains explicit `get`, `list`, and `getIamPolicy` permissions for the resource types that Security Hub CSPM records. It excludes data-plane reads such as Cloud Storage object data, BigQuery table rows, and Secret Manager secret values. The full permission list is the `CONFIG_READER_PERMISSIONS` array in the downloaded setup script; copy it into a role definition file and create the role:

```
$ gcloud iam roles create securityHubConfigReader \
  --organization={{organization-id}} \
  --title="Security Hub Config Reader" \
  --stage=GA \
  --permissions={{comma-separated-permissions-from-CONFIG_READER_PERMISSIONS}}
```

Then grant the following roles to the service account:
+ `organizations/{{organization-id}}/roles/securityHubConfigReader` – Read the configuration and IAM policy of each resource type that Security Hub CSPM records. Update the role when Security Hub CSPM adds support for new GCP resource types; running the setup script again does this for you.
+ `roles/cloudasset.viewer` – Resource discovery through Cloud Asset Inventory.
+ `roles/browser` – Read the organization, folder, and project hierarchy.
+ `roles/serviceusage.serviceUsageConsumer` – Call GCP APIs on behalf of the management project. This role also includes `serviceusage.services.use`, so it is not read-only.
+ `roles/pubsub.viewer` – Read Pub/Sub metadata. Subscriber access is granted on each subscription in Step 5, not at the organization.

```
$ gcloud organizations add-iam-policy-binding {{organization-id}} \
  --member="serviceAccount:config-sa-{{aws-account-id}}@{{management-project}}.iam.gserviceaccount.com" \
  --role="organizations/{{organization-id}}/roles/securityHubConfigReader" \
  --condition=None
```

Repeat the command for each role in the list.

## Step 5: Set up Pub/Sub
<a name="securityhub-gcp-setup-gcp-pubsub"></a>

AWS Config receives two streams from your GCP environment through Pub/Sub: Cloud Audit Logs events (Step 6) and resource change notifications from Cloud Asset Inventory (Step 7). Each stream has its own topic and a pull subscription. Topics are shared across AWS Regions; subscriptions are created for each AWS Region in which you create a connector.

Create the topics and subscriptions in the management project. The subscription must be a pull subscription with no message filter, and it must not expire.

```
$ gcloud pubsub topics create config-lifecycle-topic-{{aws-account-id}} \
  --project={{management-project}}
gcloud pubsub subscriptions create config-lifecycle-sub-{{aws-account-id}}-{{aws-region}} \
  --topic=config-lifecycle-topic-{{aws-account-id}} \
  --project={{management-project}} \
  --expiration-period=never

gcloud pubsub topics create config-cai-topic-{{aws-account-id}} \
  --project={{management-project}}
gcloud pubsub subscriptions create config-cai-sub-{{aws-account-id}}-{{aws-region}} \
  --topic=config-cai-topic-{{aws-account-id}} \
  --project={{management-project}} \
  --expiration-period=never
```

Label each subscription so that AWS Config can discover it, and grant the service account subscriber access on each subscription:

```
$ gcloud pubsub subscriptions update {{subscription-name}} \
  --project={{management-project}} \
  --update-labels="aws-config-discovery={{aws-account-id}}-{{aws-region}}-{{management-project}}"
gcloud pubsub subscriptions add-iam-policy-binding {{subscription-name}} \
  --project={{management-project}} \
  --member="serviceAccount:config-sa-{{aws-account-id}}@{{management-project}}.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"
```

Key configuration:
+ **Topic names** – `config-lifecycle-topic-{{aws-account-id}}` and `config-cai-topic-{{aws-account-id}}`.
+ **Subscription names** – `config-lifecycle-sub-{{aws-account-id}}-{{aws-region}}` and `config-cai-sub-{{aws-account-id}}-{{aws-region}}`.
+ **Label** – `aws-config-discovery={{aws-account-id}}-{{aws-region}}-{{management-project}}`. The label must be on the subscription itself. Without this exact value, the connector receives no data.

## Step 6: Configure Cloud Audit Logs export
<a name="securityhub-gcp-setup-gcp-export"></a>

Create an aggregated log sink at the organization level that routes Cloud Audit Logs from the organization and all of its projects to the lifecycle topic. The sink exports Admin Activity logs and Data Access logs, excluding high-volume entries that Security Hub CSPM does not use (Kubernetes lease renewals, container image reads, and service account token minting).

```
$ gcloud logging sinks create config-lifecycle-sink-{{aws-account-id}} \
  pubsub.googleapis.com/projects/{{management-project}}/topics/config-lifecycle-topic-{{aws-account-id}} \
  --organization={{organization-id}} \
  --include-children \
  --log-filter='(LOG_ID("cloudaudit.googleapis.com/activity") AND NOT protoPayload.methodName:"io.k8s.coordination.v1.leases.") OR (LOG_ID("cloudaudit.googleapis.com/data_access") AND NOT (protoPayload.methodName:"Docker-Get" OR protoPayload.methodName:"Docker-Head" OR protoPayload.methodName:"Docker-ServeBlob" OR protoPayload.methodName:"Docker-ListReferrers" OR protoPayload.methodName:"Docker-GetReferrers" OR protoPayload.methodName:"GenerateAccessToken"))'
```

Grant the sink's writer identity permission to publish to the topic. The writer identity is shown in the output of `gcloud logging sinks describe`.

```
$ gcloud pubsub topics add-iam-policy-binding config-lifecycle-topic-{{aws-account-id}} \
  --project={{management-project}} \
  --member="{{writer-identity}}" \
  --role="roles/pubsub.publisher"
```

Then enable Data Access audit logging for write operations across all services in the organization. Security Hub CSPM uses these events to detect resource changes. Do not exempt the connector service account or other principals from these logs; exempted activity is not reported.

```
$ gcloud organizations get-iam-policy {{organization-id}} --format=json > policy.json
# Add {"service": "allServices", "auditLogConfigs": [{"logType": "DATA_WRITE"}]} to auditConfigs in policy.json
gcloud organizations set-iam-policy {{organization-id}} policy.json
```

**Important**  
Enabling Data Access audit logs for all services and exporting all resource changes increases your Cloud Logging and Pub/Sub volume and costs.

## Step 7: Configure a Cloud Asset Inventory feed
<a name="securityhub-gcp-setup-gcp-asset-feed"></a>

Create an organization-level Cloud Asset Inventory feed that publishes resource configuration changes to the second topic. The feed covers all asset types except OS Config types, which are high volume and are not evaluated by Security Hub CSPM.

The feed publishes as the management project's Cloud Asset service agent. Create the agent and grant it publisher access before you create the feed:

```
$ gcloud beta services identity create --service=cloudasset.googleapis.com \
  --project={{management-project}}
gcloud projects add-iam-policy-binding {{management-project}} \
  --member="serviceAccount:service-{{project-number}}@gcp-sa-cloudasset.iam.gserviceaccount.com" \
  --role="roles/cloudasset.serviceAgent" --condition=None
gcloud pubsub topics add-iam-policy-binding config-cai-topic-{{aws-account-id}} \
  --project={{management-project}} \
  --member="serviceAccount:service-{{project-number}}@gcp-sa-cloudasset.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"
```

```
$ gcloud asset feeds create config-cai-feed-{{aws-account-id}} \
  --organization={{organization-id}} \
  --billing-project={{management-project}} \
  --asset-types=".*" \
  --content-type=resource \
  --condition-expression='!temporal_asset.asset.asset_type.startsWith("osconfig.googleapis.com/")' \
  --pubsub-topic=projects/{{management-project}}/topics/config-cai-topic-{{aws-account-id}}
```

**Note**  
After you complete Steps 1–7, allow 5–10 minutes for audit logs to start flowing. You can confirm delivery with the Pub/Sub `IncomingMessages` metric on the two topics.