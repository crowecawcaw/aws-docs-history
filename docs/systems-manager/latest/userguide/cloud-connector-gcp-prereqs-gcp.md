

# GCP prerequisites
<a name="cloud-connector-gcp-prereqs-gcp"></a>

Complete the following steps in your GCP environment. You need the following values from the AWS prerequisites:
+ **Issuer URL** – The AWS OIDC issuer URL from the previous section.
+ **Subject** – The ARN of the Systems Manager GCP federation role, for example: `arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/SSM-GCPRole-{{CONNECTOR_NAME}}`

If you don't record with AWS Config, skip the steps marked (AWS Config recording only).

Run the following commands in Google Cloud Shell or any terminal that has `gcloud` installed. Replace the following placeholders with your own values:
+ {{HOST\_PROJECT\_ID}} – The host project ID.
+ {{HOST\_PROJECT\_NUMBER}} – The host project number. To find it, run `gcloud projects describe {{HOST_PROJECT_ID}} --format='value(projectNumber)'`.
+ {{TARGET\_PROJECT\_ID}} – A target project ID. The host project can also be a target.
+ {{ACCOUNT\_ID}} – Your AWS account ID.
+ {{AWS\_REGION}} – The AWS Region (for example, `us-east-1`).
+ {{CONNECTOR\_NAME}} – The name part of your Systems Manager GCP federation role, `SSM-GCPRole-{{CONNECTOR_NAME}}`. Use the same role that you pass to `--role-arn` in [Step 2: Create a Systems Manager Cloud Connector](cloud-connector-gcp-create-ssm-connector.md).

**To set up the GCP side of the federation**

1. 

**Enable the required APIs in the host project**

   ```
   gcloud services enable iam.googleapis.com iamcredentials.googleapis.com sts.googleapis.com cloudresourcemanager.googleapis.com compute.googleapis.com cloudasset.googleapis.com osconfig.googleapis.com progressiverollout.googleapis.com serviceusage.googleapis.com pubsub.googleapis.com --project={{HOST_PROJECT_ID}}
   ```

   If you don't record with AWS Config, you can leave out `pubsub.googleapis.com`.

1. 

**Allow cross-project service account usage**

   The connector service account is created in the host project and used in the target projects. Check the `iam.disableCrossProjectServiceAccountUsage` organization policy constraint:

   ```
   gcloud resource-manager org-policies describe iam.disableCrossProjectServiceAccountUsage --project={{HOST_PROJECT_ID}} --effective
   ```

   If the constraint is enforced, ask your organization policy administrator to stop enforcing it on the host project:

   ```
   gcloud resource-manager org-policies disable-enforce iam.disableCrossProjectServiceAccountUsage --project={{HOST_PROJECT_ID}}
   ```

   You can skip this step if the host project is your only target.

1. 

**Create a Workload Identity Pool**

   Replace {{POOL\_ID}} with a pool ID (for example, `connector-pool-{{ACCOUNT_ID}}`).

   ```
   gcloud iam workload-identity-pools create {{POOL_ID}} --project={{HOST_PROJECT_ID}} --location=global --display-name="AWS SSM Connector"
   ```

1. 

**Create an OIDC provider that trusts AWS**

   Replace {{PROVIDER\_ID}} with a provider ID (for example, `connector-oidc`) and {{AWS\_OIDC\_ISSUER\_URL}} with the AWS OIDC issuer URL from the AWS prerequisites. Systems Manager and AWS Config both request tokens for the `https://sts.googleapis.com` audience, so the provider allows only that audience.

   ```
   gcloud iam workload-identity-pools providers create-oidc {{PROVIDER_ID}} --project={{HOST_PROJECT_ID}} --location=global --workload-identity-pool={{POOL_ID}} --issuer-uri="{{AWS_OIDC_ISSUER_URL}}" --allowed-audiences="https://sts.googleapis.com" --attribute-mapping="google.subject=assertion.sub" --attribute-condition="assertion.sub in ['arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/SSM-GCPRole-{{CONNECTOR_NAME}}', 'arn:aws:iam::{{ACCOUNT_ID}}:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty']"
   ```

   If you don't record with AWS Config, list only the Systems Manager GCP federation role ARN in `--attribute-condition`.

   Wait for the provider state to become `ACTIVE`:

   ```
   gcloud iam workload-identity-pools providers describe {{PROVIDER_ID}} --project={{HOST_PROJECT_ID}} --location=global --workload-identity-pool={{POOL_ID}} --format='value(state)'
   ```

1. 

**Create the connector service account**

   Replace {{SERVICE\_ACCOUNT\_ID}} with a service account ID. The resulting email is `{{SERVICE_ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com`.

   ```
   gcloud iam service-accounts create {{SERVICE_ACCOUNT_ID}} --project={{HOST_PROJECT_ID}} --display-name="AWS Systems Manager Connector"
   ```

1. 

**Allow the federation role to impersonate the connector service account**

   ```
   gcloud iam service-accounts add-iam-policy-binding {{SERVICE_ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com --project={{HOST_PROJECT_ID}} --role="roles/iam.workloadIdentityUser" --member="principal://iam.googleapis.com/projects/{{HOST_PROJECT_NUMBER}}/locations/global/workloadIdentityPools{{/POOL_ID/}}subject/arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/SSM-GCPRole-{{CONNECTOR_NAME}}"
   ```

1. 

**Set up each target project**

   Repeat this step for each target project, including the host project if it has VMs.

   Enable the APIs and the full VM Manager feature set:

   ```
   gcloud services enable osconfig.googleapis.com compute.googleapis.com progressiverollout.googleapis.com serviceusage.googleapis.com --project={{TARGET_PROJECT_ID}}
   
   gcloud compute project-info add-metadata --project={{TARGET_PROJECT_ID}} --metadata=enable-osconfig=TRUE
   
   gcloud compute os-config project-feature-settings update --project={{TARGET_PROJECT_ID}} --patch-and-config-feature-set=full
   ```

   Create the OS Policy Orchestrator service agents and grant their roles. Replace {{TARGET\_PROJECT\_NUMBER}} with the target project number.

   ```
   gcloud beta services identity create --service=osconfig.googleapis.com --project={{TARGET_PROJECT_NUMBER}}
   
   gcloud beta services identity create --service=progressiverollout.googleapis.com --project={{TARGET_PROJECT_NUMBER}}
   
   gcloud projects add-iam-policy-binding {{TARGET_PROJECT_ID}} --member="serviceAccount:service-{{TARGET_PROJECT_NUMBER}}@gcp-sa-osconfig.iam.gserviceaccount.com" --role="roles/osconfig.serviceAgent" --condition=None
   
   gcloud projects add-iam-policy-binding {{TARGET_PROJECT_ID}} --member="serviceAccount:service-{{TARGET_PROJECT_NUMBER}}@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" --role="roles/osconfig.rolloutServiceAgent" --condition=None
   
   gcloud projects add-iam-policy-binding {{TARGET_PROJECT_ID}} --member="serviceAccount:service-{{TARGET_PROJECT_NUMBER}}@gcp-sa-progrollout.iam.gserviceaccount.com" --role="roles/progressiverollout.serviceAgent" --condition=None
   ```

   If the target project is not the host project, also grant the host project's rollout agent in the target project:

   ```
   gcloud projects add-iam-policy-binding {{TARGET_PROJECT_ID}} --member="serviceAccount:service-{{HOST_PROJECT_NUMBER}}@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" --role="roles/osconfig.rolloutServiceAgent" --condition=None
   ```

   Create the OS Policy deployer custom role `awsSsmVmRunCommand`:

   ```
   gcloud iam roles create awsSsmVmRunCommand --project={{TARGET_PROJECT_ID}} --title="AWS SSM OS Policy Deployer" --description="Allows AWS Systems Manager to manage OS Policy assignments on GCP VMs" --stage=GA --permissions="cloudasset.assets.searchAllResources,compute.instances.get,compute.instances.list,compute.instances.setLabels,compute.instances.setMetadata,compute.projects.get,compute.regions.get,compute.zoneOperations.get,osconfig.inventories.get,osconfig.inventories.list,osconfig.osPolicyAssignments.create,osconfig.osPolicyAssignments.update,osconfig.osPolicyAssignments.get,osconfig.osPolicyAssignments.list,osconfig.osPolicyAssignments.delete,osconfig.osPolicyAssignmentReports.list,osconfig.osPolicyAssignmentReports.get,osconfig.policyOrchestrators.create,osconfig.policyOrchestrators.update,osconfig.policyOrchestrators.get,osconfig.policyOrchestrators.list,osconfig.policyOrchestrators.delete,osconfig.operations.get,osconfig.operations.list,resourcemanager.projects.get,serviceusage.services.get,serviceusage.services.list"
   ```
**Note**  
The `compute.instances.setMetadata` permission lets Systems Manager write the hybrid activation to each VM's metadata (it also allows editing startup scripts). Grant it only in projects that you want Systems Manager to manage.

   Grant the custom role to the connector service account:

   ```
   gcloud projects add-iam-policy-binding {{TARGET_PROJECT_ID}} --member="serviceAccount:{{SERVICE_ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com" --role="projects/{{TARGET_PROJECT_ID}}/roles/awsSsmVmRunCommand" --condition=None
   ```

   Grant the connector service account use of the service accounts that your VMs run as. First, list them:

   ```
   gcloud compute instances list --project={{TARGET_PROJECT_ID}} --flatten="serviceAccounts[]" --format='value(serviceAccounts.email)'
   ```

   For each service account, and for the default Compute Engine service account (`{{TARGET_PROJECT_NUMBER}}-compute@developer.gserviceaccount.com`), run the following command. Replace {{VM\_SERVICE\_ACCOUNT\_EMAIL}} with the service account email.

   ```
   gcloud iam service-accounts add-iam-policy-binding {{VM_SERVICE_ACCOUNT_EMAIL}} --member="serviceAccount:{{SERVICE_ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com" --role="roles/iam.serviceAccountUser" --condition=None
   ```

1. 

**Create a service account for AWS Config (AWS Config recording only)**

   ```
   gcloud iam service-accounts create aws-config-{{ACCOUNT_ID}} --project={{HOST_PROJECT_ID}} --display-name="AWS Config"
   ```

1. 

**Allow AWS Config to impersonate its service account (AWS Config recording only)**

   The subject is the AWS Config service-linked role ARN, which is created automatically when you create the AWS Config connector in a later step.

   ```
   gcloud iam service-accounts add-iam-policy-binding aws-config-{{ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com --project={{HOST_PROJECT_ID}} --role="roles/iam.workloadIdentityUser" --member="principal://iam.googleapis.com/projects/{{HOST_PROJECT_NUMBER}}/locations/global/workloadIdentityPools{{/POOL_ID/}}subject/arn:aws:iam::{{ACCOUNT_ID}}:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty"
   ```

1. 

**Grant AWS Config discovery roles in the host project (AWS Config recording only)**

   Run the following command for each of these roles: `roles/cloudasset.viewer`, `roles/browser`, and `roles/serviceusage.serviceUsageConsumer`. Replace {{ROLE}} with each role.

   ```
   gcloud projects add-iam-policy-binding {{HOST_PROJECT_ID}} --member="serviceAccount:aws-config-{{ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com" --role="{{ROLE}}" --condition=None
   ```

1. 

**Grant AWS Config read roles in each target project (AWS Config recording only)**

   Grant the following roles to the AWS Config service account on each target project by running `add-iam-policy-binding` for each role: `roles/cloudasset.viewer`, `roles/serviceusage.serviceUsageConsumer`, `roles/browser`, `roles/pubsub.viewer`, `roles/artifactregistry.reader`, `roles/bigquery.metadataViewer`, `roles/cloudfunctions.viewer`, `roles/compute.viewer`, `roles/container.clusterViewer`, `roles/dns.reader`, `roles/eventarc.viewer`, `roles/datastore.viewer`, `roles/iam.serviceAccountViewer`, `roles/logging.viewer`, `roles/run.viewer`, `roles/secretmanager.viewer`, `roles/cloudsql.viewer`, and `roles/storage.bucketViewer`.

   ```
   gcloud projects add-iam-policy-binding {{TARGET_PROJECT_ID}} --member="serviceAccount:aws-config-{{ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com" --role="{{ROLE}}" --condition=None
   ```

1. 

**Create a Pub/Sub topic and subscription (AWS Config recording only)**

   AWS Config finds the subscription by its `aws-config-discovery` label. Replace {{PUBSUB\_TOPIC}} with a topic name (for example, `aws-config-{{ACCOUNT_ID}}`).

   ```
   gcloud pubsub topics create {{PUBSUB_TOPIC}} --project={{HOST_PROJECT_ID}}
   
   gcloud pubsub subscriptions create {{PUBSUB_TOPIC}}-aws-config-{{AWS_REGION}} --topic={{PUBSUB_TOPIC}} --project={{HOST_PROJECT_ID}} --labels="aws-config-discovery={{ACCOUNT_ID}}-{{AWS_REGION}}-{{HOST_PROJECT_ID}}" --expiration-period=never
   
   gcloud pubsub subscriptions add-iam-policy-binding {{PUBSUB_TOPIC}}-aws-config-{{AWS_REGION}} --project={{HOST_PROJECT_ID}} --member="serviceAccount:aws-config-{{ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com" --role="roles/pubsub.subscriber"
   ```

1. 

**Export audit logs to the topic (AWS Config recording only)**

   Complete this step for each target project.

   ```
   gcloud logging sinks create aws-config-{{ACCOUNT_ID}} pubsub.googleapis.com/projects/{{HOST_PROJECT_ID}}/topics/{{PUBSUB_TOPIC}} --project={{TARGET_PROJECT_ID}} --log-filter='LOG_ID("cloudaudit.googleapis.com/activity") AND NOT protoPayload.methodName:"io.k8s.coordination.v1.leases."'
   ```

   Grant the sink writer identity permission to publish to the topic:

   ```
   SINK_WRITER=$(gcloud logging sinks describe aws-config-{{ACCOUNT_ID}} --project={{TARGET_PROJECT_ID}} --format='value(writerIdentity)')
   
   gcloud pubsub topics add-iam-policy-binding {{PUBSUB_TOPIC}} --project={{HOST_PROJECT_ID}} --member="$SINK_WRITER" --role="roles/pubsub.publisher"
   ```

1. 

**(Organization scope only) Grant organization-level roles**

   Complete this step only if you target an entire GCP organization. Replace {{ORGANIZATION\_ID}} with the numeric organization ID. Do the following:
   + Create the organization OS Policy Orchestrator agents by using `--organization={{ORGANIZATION_ID}}`.
   + Grant the organization service agents their roles (`service-org-{{ORGANIZATION_ID}}@gcp-sa-osconfig`, `-osconfig-rollout`, and `-progrollout`).
   + Grant the connector service account `roles/osconfig.policyOrchestratorAdmin` and `roles/cloudasset.viewer` on the organization.
   + (AWS Config recording only) Grant the AWS Config service account `roles/cloudasset.viewer`, `roles/browser`, and `roles/serviceusage.serviceUsageConsumer` on the organization.
   + Complete the target-project setup for each project in the organization. The AWS Config read roles and the audit log export apply only when you record with AWS Config.

   To list the active projects in the organization, use the following command:

   ```
   gcloud asset search-all-resources --scope=organizations/{{ORGANIZATION_ID}} --asset-types=cloudresourcemanager.googleapis.com/Project --query="state:ACTIVE" --format='value(additionalAttributes.projectId)'
   ```

After completing the GCP setup, note the following values. You need them when creating the Cloud Connector:
+ **Host project ID** – The project that hosts the Workload Identity Pool and service accounts.
+ **Workload Identity Pool provider** – The full resource name (`projects/{{HOST_PROJECT_NUMBER}}/locations/global/workloadIdentityPools{{/POOL_ID/}}providers/{{PROVIDER_ID}}`).
+ **Service account email** – The connector service account email.
+ **Config service account email** – The AWS Config service account email. (AWS Config recording only)
+ **Pub/Sub topic** – `projects/{{HOST_PROJECT_ID}}/topics/{{PUBSUB_TOPIC}}`. (AWS Config recording only)
+ **Project IDs** – The GCP projects you want to manage.
+ **Organization ID** – Required if you target an entire organization. Also required if you record with AWS Config and your host project belongs to an organization.