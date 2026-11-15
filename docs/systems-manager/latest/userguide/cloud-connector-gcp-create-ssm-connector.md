

# Step 2: Create a Systems Manager Cloud Connector
<a name="cloud-connector-gcp-create-ssm-connector"></a>

After the AWS Config connector is set up, create the Systems Manager Cloud Connector. The Systems Manager Cloud Connector stores your GCP workload identity federation settings and project or organization targets, and links them to the AWS Config connector if you created one.

**To create a Systems Manager Cloud Connector**

1. Run the following command. Replace the placeholder values with your Workload Identity Pool provider, connector service account email, target project IDs, the Systems Manager GCP federation role ARN, and the AWS Config connector ARN from Step 1.
**Create the federation role before you run this command**  
Before you run this command, the Systems Manager GCP federation role that `--role-arn` identifies must already exist. Its trust policy must also allow the Systems Manager service principal (`ssm.amazonaws.com`) to assume it. The AWS CLI and API do not create this role for you. If either requirement is not met, the command fails. The error message is `ValidationException: Nonexistent role or missing ssm service principal in trust policy`. Create the role first with the trust and permissions policies in [GCP federation role](cloud-connector-gcp-federation-role.md). Use the same role ARN that you used as the OIDC provider attribute-condition subject in [GCP prerequisites](cloud-connector-gcp-prereqs-gcp.md).

   ```
   aws ssm create-cloud-connector \
       --display-name "{{MyGcpConnector}}" \
       --configuration '{
           "GcpConfiguration": {
               "WorkloadIdentityPoolProvider": "projects/{{HOST_PROJECT_NUMBER}}/locations/global/workloadIdentityPools{{/POOL_ID/}}providers/{{PROVIDER_ID}}",
               "ServiceAccountEmail": "{{SERVICE_ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com",
               "Targets": {
                   "Projects": [
                       {"ProjectId": "{{PROJECT_ID}}"}
                   ]
               }
           }
       }' \
       --role-arn "arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/SSM-GCPRole-{{CONNECTOR_NAME}}" \
       --config-connector-arn {{CONFIG_CONNECTOR_ARN}}
   ```

   If you don't record with AWS Config, leave out `--config-connector-arn`.

   To target multiple projects, add more entries to `Projects` (up to 75). To target an entire GCP organization, replace the `Targets` value with `"OrganizationId": "{{ORGANIZATION_ID}}"`. If you record with AWS Config, the AWS Config connector from Step 1 must have the same `gcpOrganizationId`.

   The response returns the `CloudConnectorId`. Note this value for future operations.

1. Verify the Cloud Connector was created successfully:

   ```
   aws ssm get-cloud-connector \
       --cloud-connector-id {{CLOUD_CONNECTOR_ID}}
   ```