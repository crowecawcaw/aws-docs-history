

# Configuring Google Cloud Platform to integrate with Amazon Inspector

The Google Cloud Platform (GCP) setup configures your environment so that Amazon Inspector and AWS Config can authenticate to GCP and receive resource change notifications. You run one setup script in your GCP environment. The same script sets up GCP for AWS Config, AWS Security Hub, AWS Security Hub CSPM, and Amazon Inspector. When you download it from the Amazon Inspector console, the file is named `inspector-gcp-setup.sh`. From the AWS Security Hub console, the file is named `securityhub-gcp-setup.sh`. To set up GCP for Amazon Inspector, run it with `ENABLE_INSPECTOR=true`.

You get the script from the Amazon Inspector console when you create the connector. After you enter your organization ID, management project ID, and token issuer URL, choose **Open setup script**. The console fills in these values. You can copy or download the script and run it in Google Cloud Shell. The console generates the script for up to 100 projects.

**Note**  
If you already ran the setup script for AWS Security Hub or AWS Security Hub CSPM without Amazon Inspector, run it again with `ENABLE_INSPECTOR=true`. The script keeps the existing setup, including the service account and workload identity federation, and adds the resources that Amazon Inspector needs.

## What the setup script does
<a name="inspector-gcp-setup-gcp-what-script-does"></a>

The setup script changes only GCP. It doesn't create IAM roles in your AWS account or turn on IAM outbound identity federation. You do those in AWS (see [Prerequisites for integrating Amazon Inspector with Google Cloud Platform](inspector-gcp-prereqs.md)).

Before it changes anything, the script runs the following checks. If a check fails, the script stops and changes nothing.
+ The management project and each VM project are active and belong to your organization.
+ You have the permissions that the script needs on the organization, the management project, and each VM project that you list.
+ Your organization doesn't exempt any principal from the audit logs that the script turns on.
+ No existing custom role with one of the script's role IDs has other permissions (see Step 4 and Step 5).

With `GCP_TARGET_PROJECTS=ALL_PROJECTS_IN_ORG`, the script finds the active projects in your organization itself, and skips with a warning any project that it can't read.

The following sections describe each task that the script performs, with the gcloud commands that it runs. If your organization restricts script execution, you can perform these tasks yourself, in this order, using this topic as a guide. In the commands, replace each placeholder with your value:
+ {{account-id}} – The 12-digit ID of the AWS account where you create the connectors.
+ {{aws-region}} – The AWS Region where you create the AWS Config connector for GCP, for example `us-east-1`.
+ {{token-issuer-url}} – The token issuer URL from IAM outbound identity federation in your AWS account. It has the format `https://{{uuid}}.tokens.sts.global.api.aws`.
+ {{organization-id}} – Your numeric GCP organization ID.
+ {{project-id}} – The ID of the management project, the GCP project in your organization that holds the service account, the workload identity pool, and the Pub/Sub topics.
+ {{project-number}} – The project number of the management project.
+ {{vm-project-id}} and {{vm-project-number}} – The ID and number of each project with Compute Engine VM instances that you want Amazon Inspector to scan. These are the projects that you list in `GCP_TARGET_PROJECTS`, or that the script finds when you use `ALL_PROJECTS_IN_ORG`. Steps for VM projects apply only if you use VM scanning.

To get a project number, run the following command.

```
$ gcloud projects describe {{project-id}} --format='value(projectNumber)'
```

## Step 1: Turn on the required APIs
<a name="inspector-gcp-setup-gcp-step-apis"></a>

Turn on the APIs that federation, Pub/Sub, audit logging, and resource discovery use in the management project. The `gcloud services enable` command accepts a limited number of APIs in one call, so the script turns them on in two calls.

```
$ gcloud services enable \
  accesscontextmanager.googleapis.com apikeys.googleapis.com appengine.googleapis.com \
  artifactregistry.googleapis.com bigquery.googleapis.com cloudasset.googleapis.com \
  cloudfunctions.googleapis.com cloudkms.googleapis.com cloudresourcemanager.googleapis.com \
  compute.googleapis.com container.googleapis.com dataproc.googleapis.com \
  dlp.googleapis.com dns.googleapis.com eventarc.googleapis.com \
  --project {{project-id}}

$ gcloud services enable \
  firestore.googleapis.com iam.googleapis.com iamcredentials.googleapis.com \
  logging.googleapis.com monitoring.googleapis.com orgpolicy.googleapis.com \
  pubsub.googleapis.com run.googleapis.com secretmanager.googleapis.com \
  serviceusage.googleapis.com sqladmin.googleapis.com sts.googleapis.com \
  storage.googleapis.com vpcaccess.googleapis.com \
  --project {{project-id}}
```

If a command fails with `UREQ_TOS_NOT_ACCEPTED`, accept the Google Cloud Terms of Service, and then run the command again.

**VM scanning only:** Turn on the OS Config API in the management project.

```
$ gcloud services enable osconfig.googleapis.com \
  --project={{project-id}} --quiet
```

Then, in each VM project, turn on the required APIs, set the `enable-osconfig=TRUE` project metadata, and turn on VM Manager.

```
$ gcloud services enable \
  compute.googleapis.com osconfig.googleapis.com \
  progressiverollout.googleapis.com serviceusage.googleapis.com \
  iam.googleapis.com iamcredentials.googleapis.com \
  --project={{vm-project-id}} --quiet

$ gcloud compute project-info add-metadata --project={{vm-project-id}} \
  --metadata=enable-osconfig=TRUE --quiet

$ gcloud compute os-config project-feature-settings update --project={{vm-project-id}} \
  --patch-and-config-feature-set=full --quiet
```

The `iam.googleapis.com` and `iamcredentials.googleapis.com` APIs are for the VM credential bridge (see Step 8). The script turns them on only when it sets up the bridge, which it does by default. With `ENABLE_INSPECTOR_VM_BRIDGE=false`, leave them out.

The `add-metadata` command sets only the `enable-osconfig` key and keeps your other project metadata. GCP charges for VM Manager. For more information, see VM Manager pricing on the Google Cloud website.

## Step 2: Create a service account
<a name="inspector-gcp-setup-gcp-step-sa"></a>

Create a service account in the management project. AWS uses this service account to access your GCP environment through workload identity federation. Don't create keys for it.

```
$ gcloud iam service-accounts create config-sa-{{account-id}} \
  --project={{project-id}} \
  --display-name="Config Connector SA"
```

The service account email is `config-sa-{{account-id}}@{{project-id}}.iam.gserviceaccount.com`. You provide this value when you create the AWS Config connector for GCP.

**Note**  
Only the AWS roles in the next step can impersonate this service account. If another principal has the Workload Identity User or Service Account Token Creator role on the service account, the setup script stops. Remove that principal, and then run the script again.

## Step 3: Configure workload identity federation
<a name="inspector-gcp-setup-gcp-step-wif"></a>

Create a workload identity pool and an OIDC provider that trust your AWS token issuer, and let the listed AWS roles impersonate the service account. This establishes an OIDC trust between AWS and GCP. No service account keys or other long-lived credentials are created or stored.

```
$ gcloud iam workload-identity-pools create connector-pool-{{account-id}} \
  --location=global \
  --display-name="Config Connector Pool" \
  --project={{project-id}}

$ gcloud iam workload-identity-pools providers create-oidc connector-oidc-{{account-id}} \
  --workload-identity-pool=connector-pool-{{account-id}} --location=global \
  --project={{project-id}} \
  --issuer-uri="{{token-issuer-url}}" \
  --allowed-audiences="https://sts.googleapis.com" \
  --attribute-mapping="google.subject=assertion.sub,attribute.aws_role=assertion.sub" \
  --attribute-condition="attribute.aws_role in ['arn:aws:iam::{{account-id}}:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty', 'arn:aws:iam::{{account-id}}:role/aws-service-role/thirdparty.inspector2.amazonaws.com/AWSServiceRoleForAmazonInspector2ThirdParty']"
```

**VM scanning only:** Add the Amazon EC2 Systems Manager federation role to the attribute condition.

```
  --allowed-audiences="https://sts.googleapis.com" \
  --attribute-condition="attribute.aws_role in ['arn:aws:iam::{{account-id}}:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty', 'arn:aws:iam::{{account-id}}:role/aws-service-role/thirdparty.inspector2.amazonaws.com/AWSServiceRoleForAmazonInspector2ThirdParty', 'arn:aws:iam::{{account-id}}:role/Inspector2SSMFederationRole-{{organization-id}}']"
```

If the provider already exists, for example from an earlier AWS Security Hub or AWS Security Hub CSPM setup, run `gcloud iam workload-identity-pools providers update-oidc` with the same arguments and `--no-disabled`. Keep any role ARN that is already in the attribute condition. The pool must contain only this provider. If the pool has another provider, the setup script stops.

Then, for each role ARN in the attribute condition, let the role impersonate the service account. Replace {{role-arn}} with the role ARN.

```
$ gcloud iam service-accounts add-iam-policy-binding config-sa-{{account-id}}@{{project-id}}.iam.gserviceaccount.com \
  --project={{project-id}} \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/{{project-number}}/locations/global/workloadIdentityPools/connector-pool-{{account-id}}/attribute.aws_role/{{role-arn}}" \
  --condition=None --quiet
```

Key values:
+ **Issuer** – Your token issuer URL from IAM outbound identity federation.
+ **Audience** – `https://sts.googleapis.com`.
+ **Subject** – The ARN of an IAM role in your AWS account, not an assumed-role session ARN. The attribute mapping copies the subject to `attribute.aws_role`, and the attribute condition admits only the listed roles:
  + The `AWSServiceRoleForConfigThirdParty` service-linked role, which AWS Config uses.
  + The `AWSServiceRoleForAmazonInspector2ThirdParty` service-linked role, which Amazon Inspector uses. The script adds it with `ENABLE_INSPECTOR=true`.
  + `Inspector2SSMFederationRole-{{organization-id}}`, which Amazon EC2 Systems Manager uses to install the Amazon Inspector VM Scanner on your VMs. The script adds it when you list VM projects.
+ **Workload identity pool provider** – `projects/{{project-number}}/locations/global/workloadIdentityPools/connector-pool-{{account-id}}/providers/connector-oidc-{{account-id}}`. You provide this value when you create the AWS Config connector for GCP.

## Step 4: Grant read roles on the organization
<a name="inspector-gcp-setup-gcp-step-read-roles"></a>

Grant read access to the service account on your organization. Grants on the organization apply to every project in it, including projects that you create later. These grants are the same with or without `ENABLE_INSPECTOR`.

First, create the organization custom role `securityHubConfigReader`. It holds the get, list, and `getIamPolicy` permissions for the resource types that AWS Config records. It doesn't grant reads of Cloud Storage object data, BigQuery table rows, or Secret Manager secret values. Some of its permissions return resource configuration that you set, such as instance metadata and environment variables. Replace {{permissions}} with the permissions in the `CONFIG_READER_PERMISSIONS` list of the setup script, separated by commas.

```
$ gcloud iam roles create securityHubConfigReader \
  --organization={{organization-id}} \
  --title="Security Hub Config Reader" \
  --description="Read-only resource-configuration access for AWS Security Hub. Excludes Cloud Storage object bytes, BigQuery table rows and Secret Manager secret values. Resource configuration, such as instance metadata and service environment variables, is readable." \
  --permissions="{{permissions}}" \
  --stage=GA --quiet
```

The role ID is the default of `CONFIG_READER_ROLE`. If your organization already has a role with this ID and it has other permissions, the script stops. Use a different role ID instead.

Then grant the custom role and the following predefined roles to the service account. Run the following command once for each role. Replace {{role-name}} with the role.

```
$ gcloud organizations add-iam-policy-binding {{organization-id}} \
  --member="serviceAccount:config-sa-{{account-id}}@{{project-id}}.iam.gserviceaccount.com" \
  --role="{{role-name}}" \
  --condition=None --quiet
```

```
organizations/{{organization-id}}/roles/securityHubConfigReader
roles/cloudasset.viewer
roles/serviceusage.serviceUsageConsumer
roles/browser
roles/pubsub.viewer
```

Service Usage Consumer isn't a read-only role. Its `serviceusage.services.use` permission lets the service account use API quota in, and bill API usage to, any project in your organization.

## Step 5: Create the Amazon Inspector custom roles
<a name="inspector-gcp-setup-gcp-step-inspector-roles"></a>

With `ENABLE_INSPECTOR=true`, the script creates the following organization custom roles and grants them to the service account:
+ `inspectorArtifactReader` – Holds only the `artifactregistry.repositories.downloadArtifacts` permission. Amazon Inspector uses it to download the manifests and layers of your Artifact Registry container images.
+ `inspectorFunctionSourceReader` – Holds only the `cloudfunctions.functions.sourceCodeGet` permission. Amazon Inspector uses it to download the deployed source of your Cloud Run functions, and needs no other permission for this. It's a custom role because no predefined role grants this permission without also granting permission to deploy functions.

```
$ gcloud iam roles create inspectorArtifactReader \
  --organization={{organization-id}} \
  --title="Inspector Artifact Reader" \
  --description="Download Artifact Registry image manifests and layers for Amazon Inspector scanning." \
  --permissions="artifactregistry.repositories.downloadArtifacts" \
  --stage=GA --quiet

$ gcloud organizations add-iam-policy-binding {{organization-id}} \
  --member="serviceAccount:config-sa-{{account-id}}@{{project-id}}.iam.gserviceaccount.com" \
  --role="organizations/{{organization-id}}/roles/inspectorArtifactReader" \
  --condition=None --quiet

$ gcloud iam roles create inspectorFunctionSourceReader \
  --organization={{organization-id}} \
  --title="Inspector Function Source Reader" \
  --description="Download Cloud Functions source for Amazon Inspector scanning." \
  --permissions="cloudfunctions.functions.sourceCodeGet" \
  --stage=GA --quiet

$ gcloud organizations add-iam-policy-binding {{organization-id}} \
  --member="serviceAccount:config-sa-{{account-id}}@{{project-id}}.iam.gserviceaccount.com" \
  --role="organizations/{{organization-id}}/roles/inspectorFunctionSourceReader" \
  --condition=None --quiet
```

**VM scanning only:** The script also creates the organization custom role `OSPolicySSMDeployer` and grants it to the service account. Amazon EC2 Systems Manager uses this role to create OS policies that install the Amazon Inspector VM Scanner on your VMs.

```
$ gcloud iam roles create OSPolicySSMDeployer \
  --organization={{organization-id}} \
  --title="OS Policy SSM Deployer" \
  --description="Can manage VM metadata, read VM properties, and create/manage OS Policy assignments for SSM deployment" \
  --permissions="cloudasset.assets.searchAllResources,compute.instances.get,compute.instances.list,compute.instances.setLabels,compute.instances.setMetadata,compute.projects.get,compute.regions.get,compute.zoneOperations.get,iam.serviceAccounts.actAs,osconfig.inventories.get,osconfig.inventories.list,osconfig.osPolicyAssignments.create,osconfig.osPolicyAssignments.update,osconfig.osPolicyAssignments.get,osconfig.osPolicyAssignments.list,osconfig.osPolicyAssignments.delete,osconfig.osPolicyAssignmentReports.list,osconfig.osPolicyAssignmentReports.get,osconfig.policyOrchestrators.create,osconfig.policyOrchestrators.update,osconfig.policyOrchestrators.get,osconfig.policyOrchestrators.list,osconfig.policyOrchestrators.delete,osconfig.operations.get,osconfig.operations.list,resourcemanager.projects.get,serviceusage.services.get,serviceusage.services.list" \
  --stage=GA --quiet

$ gcloud organizations add-iam-policy-binding {{organization-id}} \
  --member="serviceAccount:config-sa-{{account-id}}@{{project-id}}.iam.gserviceaccount.com" \
  --role="organizations/{{organization-id}}/roles/OSPolicySSMDeployer" \
  --condition=None --quiet
```

The role IDs are the defaults of `INSPECTOR_ARTIFACT_READER_ROLE`, `INSPECTOR_FUNCTION_SOURCE_ROLE`, and `INSPECTOR_VM_DEPLOYER_ROLE`. If your organization already has a role with one of these IDs and it has other permissions, the script stops. Use a different role ID instead. These IDs and `CONFIG_READER_ROLE` must name four different roles.

**VM scanning only:** Create the OS Config and Progressive Rollout service identities for your organization and for each VM project. VM Manager uses these Google-managed identities to run OS policy orchestrators. If the management project isn't one of your VM projects, also create its OS Config service identity.

```
$ gcloud beta services identity create --service=osconfig.googleapis.com \
  --organization={{organization-id}} --billing-project={{project-id}} --quiet

$ gcloud beta services identity create --service=progressiverollout.googleapis.com \
  --organization={{organization-id}} --billing-project={{project-id}} --quiet

$ gcloud beta services identity create --service=osconfig.googleapis.com \
  --project={{vm-project-id}} --quiet

$ gcloud beta services identity create --service=progressiverollout.googleapis.com \
  --project={{vm-project-id}} --quiet

$ gcloud beta services identity create --service=osconfig.googleapis.com \
  --project={{project-id}} --quiet
```

Then grant each service identity its service agent role on the organization.

```
$ gcloud organizations add-iam-policy-binding {{organization-id}} \
  --member="serviceAccount:service-org-{{organization-id}}@gcp-sa-osconfig.iam.gserviceaccount.com" \
  --role="roles/osconfig.serviceAgent" \
  --condition=None --billing-project={{project-id}} --quiet

$ gcloud organizations add-iam-policy-binding {{organization-id}} \
  --member="serviceAccount:service-org-{{organization-id}}@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
  --role="roles/osconfig.rolloutServiceAgent" \
  --condition=None --billing-project={{project-id}} --quiet

$ gcloud organizations add-iam-policy-binding {{organization-id}} \
  --member="serviceAccount:service-org-{{organization-id}}@gcp-sa-progrollout.iam.gserviceaccount.com" \
  --role="roles/progressiverollout.serviceAgent" \
  --condition=None --billing-project={{project-id}} --quiet
```

Also grant the same roles on each VM project to that project's service identities.

```
$ gcloud projects add-iam-policy-binding {{vm-project-id}} \
  --member="serviceAccount:service-{{vm-project-number}}@gcp-sa-osconfig.iam.gserviceaccount.com" \
  --role="roles/osconfig.serviceAgent" \
  --condition=None --quiet

$ gcloud projects add-iam-policy-binding {{vm-project-id}} \
  --member="serviceAccount:service-{{vm-project-number}}@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
  --role="roles/osconfig.rolloutServiceAgent" \
  --condition=None --quiet

$ gcloud projects add-iam-policy-binding {{vm-project-id}} \
  --member="serviceAccount:service-{{vm-project-number}}@gcp-sa-progrollout.iam.gserviceaccount.com" \
  --role="roles/progressiverollout.serviceAgent" \
  --condition=None --quiet
```

On each VM project other than the management project, also grant the rollout role to the management project's OS Config rollout service agent. When the connector covers a list of projects, the OS policy orchestrator is in the management project, and this agent creates the OS policy assignments in your other VM projects.

```
$ gcloud projects add-iam-policy-binding {{vm-project-id}} \
  --member="serviceAccount:service-{{project-number}}@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
  --role="roles/osconfig.rolloutServiceAgent" \
  --condition=None --quiet
```

## Step 6: Set up Pub/Sub
<a name="inspector-gcp-setup-gcp-step-pubsub"></a>

AWS Config and Amazon Inspector receive resource changes and image pulls through Pub/Sub topics and pull subscriptions in the management project. The script creates the following topics and subscriptions:


| Stream | Topic | Subscription | 
| --- | --- | --- | 
| Resource changes from audit logs | config-lifecycle-topic-{{account-id}} | config-lifecycle-sub-{{account-id}}-{{aws-region}} | 
| Resource changes from Cloud Asset Inventory | config-cai-topic-{{account-id}} | config-cai-sub-{{account-id}}-{{aws-region}} | 
| Artifact Registry image pulls (with ENABLE\_INSPECTOR=true) | inspector-pull-topic-{{account-id}} | inspector-pull-sub-{{account-id}}-{{aws-region}} | 

For each stream, create the topic and a pull subscription that never expires, label the subscription for discovery, and grant the service account the Subscriber role on the subscription only. Replace {{topic}} and {{subscription}} with the names in the table.

```
$ gcloud pubsub topics create {{topic}} --project={{project-id}}

$ gcloud pubsub subscriptions create {{subscription}} \
  --topic={{topic}} --project={{project-id}} \
  --expiration-period=never

$ gcloud pubsub subscriptions update {{subscription}} \
  --project={{project-id}} \
  --update-labels="aws-config-discovery={{account-id}}-{{aws-region}}-{{project-id}}" \
  --expiration-period=never

$ gcloud pubsub subscriptions add-iam-policy-binding {{subscription}} \
  --project={{project-id}} \
  --member="serviceAccount:config-sa-{{account-id}}@{{project-id}}.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber" \
  --quiet
```

Key configuration:
+ **Subscription type** – Pull, with no message filter, no export configuration, and no expiration. If an existing subscription is a push or export subscription, has a filter, or is detached from its topic, the setup script stops.
+ **Label** – `aws-config-discovery` with the value `{{account-id}}-{{aws-region}}-{{project-id}}`. AWS Config finds the subscriptions by this label, so you don't provide topic or subscription names to AWS Config.
+ **Role assignment** – Pub/Sub Subscriber (`roles/pubsub.subscriber`) on each subscription.

**Important**  
The label includes the AWS Region. Create the AWS Config connector for GCP in {{aws-region}}. A connector in another Region looks for a different label, finds no subscription, and shows as healthy but discovers nothing. The topics are shared across Regions. Each Region has its own subscriptions.

## Step 7: Configure log sinks, the asset feed, and audit logs
<a name="inspector-gcp-setup-gcp-step-logs"></a>

Route resource changes and image pulls in your organization to the Pub/Sub topics, and then turn on the audit logs that the routes use.

**Resource changes from audit logs:**

Create an organization log sink that includes all projects in the organization and routes Admin Activity and Data Access audit log entries to the lifecycle topic.

```
$ gcloud logging sinks create config-lifecycle-sink-{{account-id}} \
  pubsub.googleapis.com/projects/{{project-id}}/topics/config-lifecycle-topic-{{account-id}} \
  --organization={{organization-id}} --include-children \
  --log-filter='(LOG_ID("cloudaudit.googleapis.com/activity") AND NOT protoPayload.methodName:"io.k8s.coordination.v1.leases.") OR (LOG_ID("cloudaudit.googleapis.com/data_access") AND NOT (protoPayload.methodName:"Docker-Get" OR protoPayload.methodName:"Docker-Head" OR protoPayload.methodName:"Docker-ServeBlob" OR protoPayload.methodName:"Docker-ListReferrers" OR protoPayload.methodName:"Docker-GetReferrers" OR protoPayload.methodName:"GenerateAccessToken"))'
```

Then get the sink's writer identity and grant it the Publisher role on the topic. Replace {{writer-identity}} with the value that the first command prints, including its `serviceAccount:` prefix.

```
$ gcloud logging sinks describe config-lifecycle-sink-{{account-id}} \
  --organization={{organization-id}} --format='value(writerIdentity)'

$ gcloud pubsub topics add-iam-policy-binding config-lifecycle-topic-{{account-id}} \
  --project={{project-id}} \
  --member="{{writer-identity}}" --role="roles/pubsub.publisher" \
  --quiet
```

**Resource changes from Cloud Asset Inventory:**

Create the Cloud Asset service agent of the management project, and grant it its service agent role and the Publisher role on the asset feed topic. The first command prints the agent's email, which is `service-{{project-number}}@gcp-sa-cloudasset.iam.gserviceaccount.com`.

```
$ gcloud beta services identity create --service=cloudasset.googleapis.com \
  --project={{project-id}} --format='value(email)'

$ gcloud projects add-iam-policy-binding {{project-id}} \
  --member="serviceAccount:service-{{project-number}}@gcp-sa-cloudasset.iam.gserviceaccount.com" \
  --role="roles/cloudasset.serviceAgent" \
  --condition=None --quiet

$ gcloud pubsub topics add-iam-policy-binding config-cai-topic-{{account-id}} \
  --project={{project-id}} \
  --member="serviceAccount:service-{{project-number}}@gcp-sa-cloudasset.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher" \
  --quiet
```

Then create an organization Cloud Asset Inventory feed for all asset types except the OS Config asset types.

```
$ gcloud asset feeds create config-cai-feed-{{account-id}} \
  --organization={{organization-id}} --billing-project={{project-id}} \
  --asset-types=".*" \
  --content-type=resource \
  --condition-expression='!temporal_asset.asset.asset_type.startsWith("osconfig.googleapis.com/")' \
  --pubsub-topic="projects/{{project-id}}/topics/config-cai-topic-{{account-id}}" --quiet
```

**Artifact Registry image pulls (with `ENABLE_INSPECTOR=true`):**

Create an organization log sink that routes Artifact Registry image pulls to the image pull topic. Amazon Inspector uses the pulls to keep images that are still in use in scan scope. Then grant the sink's writer identity the Publisher role on the topic, as for the first sink.

```
$ gcloud logging sinks create inspector-pull-sink-{{account-id}} \
  pubsub.googleapis.com/projects/{{project-id}}/topics/inspector-pull-topic-{{account-id}} \
  --organization={{organization-id}} --include-children \
  --log-filter='logName:"cloudaudit.googleapis.com%2Fdata_access" AND protoPayload.serviceName="artifactregistry.googleapis.com" AND protoPayload.methodName="Docker-GetManifest" AND (protoPayload.authenticationInfo.principalEmail:* OR protoPayload.authenticationInfo.principalSubject:*) AND NOT (protoPayload.authenticationInfo.principalEmail:"@container-analysis.iam.gserviceaccount.com" OR protoPayload.authenticationInfo.principalEmail:"@gcp-sa-artifactregistry.iam.gserviceaccount.com" OR protoPayload.authenticationInfo.principalEmail:"@gcp-sa-containerscanning.iam.gserviceaccount.com" OR protoPayload.authenticationInfo.principalEmail:"@gcp-sa-ondemandscanning.iam.gserviceaccount.com" OR protoPayload.authenticationInfo.principalEmail:"@gcp-sa-containersec.iam.gserviceaccount.com" OR protoPayload.authenticationInfo.principalEmail=~"^config-sa-[0-9]+@")'

$ gcloud logging sinks describe inspector-pull-sink-{{account-id}} \
  --organization={{organization-id}} --format='value(writerIdentity)'

$ gcloud pubsub topics add-iam-policy-binding inspector-pull-topic-{{account-id}} \
  --project={{project-id}} \
  --member="{{writer-identity}}" --role="roles/pubsub.publisher" \
  --quiet
```

If a sink already exists, run `gcloud logging sinks update` with the same arguments and `--no-disabled`. A sink must be enabled and must have no active exclusions. The setup script enables a disabled sink. If a sink has an active exclusion, the script stops.

**Audit logs:**

Turn on audit logs after the topics, subscriptions, sinks, feed, and role grants are in place. Turn on `DATA_WRITE` audit logs for all services. With `ENABLE_INSPECTOR=true`, also turn on `DATA_READ` audit logs for Artifact Registry. To do this, get your organization's IAM policy.

```
$ gcloud organizations get-iam-policy {{organization-id}} --format=json > policy.json
```

In `policy.json`, add the following entries to `auditConfigs`. If an entry for the service already exists, add the log type to its `auditLogConfigs`. Keep everything else in the policy, including the `etag`. Don't add `exemptedMembers`.

```json
{"service": "allServices", "auditLogConfigs": [{"logType": "DATA_WRITE"}]},
{"service": "artifactregistry.googleapis.com", "auditLogConfigs": [{"logType": "DATA_READ"}]}
```

Then set the updated policy.

```
$ gcloud organizations set-iam-policy {{organization-id}} policy.json --format=none --quiet
```

**Note**  
An exempted principal's activity isn't logged, so AWS Config and Amazon Inspector miss it. The script never removes an exemption. If your organization exempts a principal from a required audit log, the script stops before it changes anything. The script can't see exemptions on folders or projects, so check those yourself.

## Step 8: Set up the VM credential bridge
<a name="inspector-gcp-setup-gcp-step-bridge"></a>

**VM scanning only:** The script sets up the VM credential bridge unless you set `ENABLE_INSPECTOR_VM_BRIDGE=false`. The Amazon Inspector VM Scanner on each VM uses the bridge to get AWS credentials through a service account in the VM's project, so the Amazon Inspector VM scanner role in AWS doesn't need to list your VMs' service accounts. For the AWS side, see [Configuring Amazon Inspector to integrate with Google Cloud Platform](inspector-gcp-setup-inspector.md).

The bridge uses these resources. Don't rename them. The Amazon Inspector VM Scanner uses these exact names, and the script stops if they're changed.
+ In each VM project, the service account `inspector-vmscan-{{account-id}}`, with no roles and no keys.
+ In the management project, the workload identity pool `inspector-vm-bridge-{{account-id}}` with the OIDC provider `compute-engine-vm`.

First, in each VM project, create the service account. The script does this right after it sets up VM Manager in the project (see Step 1).

```
$ gcloud iam service-accounts create inspector-vmscan-{{account-id}} \
  --project={{vm-project-id}} \
  --display-name="Amazon Inspector VM scan minter, account {{account-id}}" \
  --description="Signs the token Amazon Inspector VM scanners in this project exchange for AWS credentials. Grant it no roles and create no keys." \
  --quiet
```

Don't create keys for this service account, and don't grant any other principal a role on it. If the service account has a user-managed key or an IAM binding that the script didn't create, the script lists each one with the command that removes it, continues, and exits with status `4`.

Then, in the management project, create the workload identity pool and the OIDC provider. The provider accepts Compute Engine VM identity tokens from the VM projects in its attribute condition.

```
$ gcloud iam workload-identity-pools create inspector-vm-bridge-{{account-id}} \
  --location=global --project={{project-id}} \
  --display-name="Amazon Inspector VM bridge" \
  --description="Exchanges Compute Engine VM identity tokens for Amazon Inspector VM scanning." \
  --quiet

$ gcloud iam workload-identity-pools providers create-oidc compute-engine-vm \
  --workload-identity-pool=inspector-vm-bridge-{{account-id}} --location=global \
  --project={{project-id}} \
  --issuer-uri="https://accounts.google.com" \
  --allowed-audiences="https://iam.googleapis.com/projects/{{project-number}}/locations/global/workloadIdentityPools/inspector-vm-bridge-{{account-id}}/providers/compute-engine-vm" \
  --attribute-mapping="google.subject=assertion.sub,attribute.project_id=assertion.google.compute_engine.project_id,attribute.project_number=string(int(assertion.google.compute_engine.project_number)),attribute.instance_id=assertion.google.compute_engine.instance_id,attribute.sa_email=assertion.email" \
  --attribute-condition="attribute.project_number in ['{{vm-project-number-1}}', '{{vm-project-number-2}}'] && attribute.instance_id != ''" \
  --display-name="Compute Engine VM tokens" \
  --description="Admits only Compute Engine VM identity tokens for Amazon Inspector VM scanning." \
  --quiet
```

Key values:
+ **Issuer** – `https://accounts.google.com`. If your organization limits the allowed workload identity issuers, it must allow this issuer.
+ **Audience** – The full resource name of the provider, with the `https://iam.googleapis.com/` prefix.
+ **Attribute condition** – List the project number of each VM project. The condition admits only VM identity tokens from these projects. If the list doesn't fit in the 4,096 characters that GCP allows for a condition (about 250 projects), the script uses `attribute.project_number != '' && attribute.instance_id != ''` instead, which admits the identity token of any Compute Engine VM. Each service account binding still lets VMs sign only as their own project's service account.

If the provider already exists, the script runs `gcloud iam workload-identity-pools providers update-oidc` with the same issuer, audience, attribute mapping, and attribute condition, and `--no-disabled`. The script keeps the project numbers that are already in the condition and adds the numbers of the VM projects in this run. So when you add VM projects, you can list only the new ones. The pool must contain only this provider. If the pool has another provider, or the provider has a condition that the script didn't write, the script stops before it changes any VM project or bridge resource, and prints what to do.

Finally, in each VM project, let the project's VMs sign tokens as its service account.

```
$ gcloud iam service-accounts add-iam-policy-binding inspector-vmscan-{{account-id}}@{{vm-project-id}}.iam.gserviceaccount.com \
  --project={{vm-project-id}} \
  --role="roles/iam.serviceAccountOpenIdTokenCreator" \
  --member="principalSet://iam.googleapis.com/projects/{{project-number}}/locations/global/workloadIdentityPools/inspector-vm-bridge-{{account-id}}/attribute.project_id/{{vm-project-id}}" \
  --condition=None --quiet
```

The member is every Compute Engine VM in that project, identified through the bridge pool. With `ENABLE_INSPECTOR_VM_BRIDGE=false`, the script skips this step but doesn't remove a bridge that an earlier run set up.

**Important**  
With the VM credential bridge, the Amazon Inspector VM Scanner agent gets its AWS credentials through the minter service account in its project. The setup script binds the token creator role on each minter only to the VM instances in that project. To maintain this configuration:  
Keep the token creator role on each minter bound only to the member above. A binding to the whole pool (`.../workloadIdentityPools/inspector-vm-bridge-{{account-id}}/*`) or to another wildcard member could let a VM instance in any project get the agent's AWS credentials.
Review the IAM policies on the VM project and on its parent folders and organization, including inherited grants. A principal with the `iam.serviceAccounts.getOpenIdToken` permission at any of these levels can also sign tokens as the minter. Service Account OpenID Connect Identity Token Creator and Service Account Token Creator both include this permission. The setup script doesn't check these grants.

## Running the setup script
<a name="inspector-gcp-setup-gcp-running"></a>

Before you run the script, make sure that you meet the prerequisites in [Prerequisites for integrating Amazon Inspector with Google Cloud Platform](inspector-gcp-prereqs.md). You need the gcloud CLI with the beta component, `jq`, a `timeout` command that supports `--foreground` (GNU coreutils, or `gtimeout` on macOS), and a gcloud session signed in with `gcloud auth login`. Google Cloud Shell has `jq` and a suitable `timeout`. The IAM API (`iam.googleapis.com`) must be turned on in the management project before you run the script. The script is tested with gcloud CLI version 580.0.0. With an older version, the script prints a warning and continues.

Each gcloud call that the script makes has a time limit of 600 seconds. If a call takes longer, the script stops with an error that names the call. Run the script again. If the same call keeps timing out, raise the limit with the `SETUP_GCLOUD_TIMEOUT_SECS` environment variable, for example `SETUP_GCLOUD_TIMEOUT_SECS=1200 bash inspector-gcp-setup.sh`.

<a name="inspector-gcp-setup-gcp-permissions"></a>The person who runs the script needs the following permissions:
+ **On the organization** – Permission to get and set the organization's IAM policy (for example, Organization Administrator), Cloud Asset Owner, Logs Configuration Writer, and Organization Role Administrator (`roles/iam.organizationRoleAdmin`). With VM projects, also permission to create OS Config and Progressive Rollout service identities on the organization.
+ **On the management project** – Owner, or all of Service Usage Admin, Security Admin, Workload Identity Pool Admin, Service Account Admin, and Pub/Sub Admin. You also need permission to read the project's ancestry. Billing must be enabled on the project.
+ **On each VM project** – Permission to get the project (`resourcemanager.projects.get`), Service Usage Admin, permission to get and set the project's IAM policy (for example, Project IAM Admin), the `compute.projects.get`, `compute.projects.setCommonInstanceMetadata`, and `compute.globalOperations.get` permissions, and `osconfig.projectFeatureSettings.update` (for example, OS Config Project Feature Settings Editor). Billing must be enabled on each VM project.

  With the VM credential bridge (the default), also Service Account Admin (`roles/iam.serviceAccountAdmin`), to create, re-enable, and bind the bridge service account, and a role with the `iam.serviceAccountKeys.list` permission (for example, Service Account Viewer, `roles/iam.serviceAccountViewer`), to check that the service account has no keys. When you use `ALL_PROJECTS_IN_ORG`, grant these two roles on the organization.

To run the GCP setup script:

1. Open the script and set the inputs at the top of the file. Replace each `CHANGEME` value. The script stops if a required input still has its `CHANGEME` value.

1. Run the script with `bash`, for example `bash inspector-gcp-setup.sh` for a script that you downloaded from the Amazon Inspector console.

1. When the script finishes, copy the connector parameters that it prints. You use them to create the AWS Config connector for GCP.

1. Create the Amazon Inspector connector (see [Configuring Amazon Inspector to integrate with Google Cloud Platform](inspector-gcp-setup-inspector.md)).

The script has the following inputs.


| Input | Description | 
| --- | --- | 
| AWS\_ACCOUNT\_ID | The 12-digit ID of the AWS account where you create the connectors. | 
| AWS\_REGION | The AWS Region where you create the AWS Config connector for GCP, for example us-east-1. | 
| ISSUER\_URL | The token issuer URL from IAM outbound identity federation, in the format https://{{uuid}}.tokens.sts.global.api.aws. | 
| GCP\_PROJECT\_ID | The ID of the management project. | 
| GCP\_ORGANIZATION\_ID | Your numeric GCP organization ID. | 
| GCP\_TARGET\_PROJECTS | The projects with VMs to scan, as a comma-separated list of project IDs, for example app-prod,app-dev. Use project IDs, not project numbers. Each project must be active and in your organization, or the script stops before it changes anything. To set up every active project in your organization that you can read, use ALL\_PROJECTS\_IN\_ORG. The script then skips, with a warning, any project that it can't read or set up, for example a project without billing. The console's project list can't produce ALL\_PROJECTS\_IN\_ORG, so edit the value in the script to use it. To skip VM setup, leave it empty or use NONE. The script uses this input only with ENABLE\_INSPECTOR=true. | 
| ENABLE\_CSPM | true or false. Set to true if you use AWS Security Hub CSPM. This input doesn't change what the script creates in GCP. | 
| ENABLE\_INSPECTOR | true or false. Set to true to set up GCP for Amazon Inspector. | 
| ENABLE\_INSPECTOR\_VM\_BRIDGE | true (default) or false. The script stops with an error for any other value. It takes effect only with VM setup, that is, with ENABLE\_INSPECTOR=true and VM projects in GCP\_TARGET\_PROJECTS. With true, the script sets up the VM credential bridge (see Step 8). With false, the script skips the bridge, but doesn't remove a bridge that an earlier run set up. The console doesn't set this input, so a script from the console uses true. | 
| CONFIG\_READER\_ROLE | The ID of the read access custom role (see Step 4). The default is securityHubConfigReader. Change it only if your organization already uses this ID for another role. | 
| INSPECTOR\_ARTIFACT\_READER\_ROLE | The ID of the image download custom role. The default is inspectorArtifactReader. Change it only if your organization already uses this ID for another role. | 
| INSPECTOR\_FUNCTION\_SOURCE\_ROLE | The ID of the function source custom role. The default is inspectorFunctionSourceReader. Change it only if your organization already uses this ID for another role. | 
| INSPECTOR\_VM\_DEPLOYER\_ROLE | The ID of the VM deployment custom role. The default is OSPolicySSMDeployer. Change it only if your organization already uses this ID for another role. | 

When the script finishes, it prints the following connector parameters. Use them when you create the AWS Config connector for GCP.
+ The AWS Region where you must create the connector (`AWS_REGION`).
+ `organizationIdentifier` – Your organization ID.
+ `projectIdentifier` – The management project ID.
+ `serviceAccountEmail` – The service account email.
+ `workloadIdentityPoolProvider` – The workload identity pool provider.

The script exits with one of the following codes:
+ `0` – Setup is complete.
+ `1` – Setup failed. The script prints the reason.
+ `3` – The script configured the resources, but a principal became exempt from a required audit log after the script's pre-check, so some activity isn't logged. The script lists the exempt principals. Remove the exemptions, and then run the script again.
+ `4` – Setup is complete, but a VM credential bridge service account (`inspector-vmscan-{{account-id}}`) has a user-managed key or an IAM binding that the script didn't create. Someone other than that project's VMs can get the Amazon Inspector VM Scanner's AWS credentials. The script lists each key and binding with the command that removes it. Remove them, and then run the script again. If both `3` and `4` apply, the script exits with `3`.

**Important**  
Run the script again after you add a project with VM instances to scan, add an AWS Config connector for GCP in another AWS Region, or remove an audit log exemption. That includes a project that you create in your GCP organization or move into it, even if you use `ALL_PROJECTS_IN_ORG`. The script sets up only the projects that are in your organization when it runs. Until you run it again, the project is missing the VM Manager setup, service agent roles, and VM credential bridge that VM scanning needs. With a list of projects, add the project to `GCP_TARGET_PROJECTS`.  
You don't need to run the script again when you add locations to the connector, or when you add projects for Artifact Registry image scanning or Cloud Run function scanning, because the script grants that access on the organization.  
Running the script again is safe. It keeps the existing setup and doesn't remove access or resources, even if you turn off a feature.