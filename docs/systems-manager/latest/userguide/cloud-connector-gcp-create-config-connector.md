

# Step 1: Create an AWS Config connector (optional)
<a name="cloud-connector-gcp-create-config-connector"></a>

Complete this step only if you want AWS Config to record the connector's GCP resources. If you don't, skip to [Step 2](cloud-connector-gcp-create-ssm-connector.md). The AWS Config connector uses workload identity federation to let AWS Config record GCP resource state. Create it before you create the Systems Manager Cloud Connector. AWS Config allows one Config connector per host project. If your host project already has one, skip this step and use that connector's ARN in Step 2. When you use the AWS Management Console, it detects and reuses an existing Config connector for the host project.

**Note**  
The AWS Config connector automatically creates a service-linked role for federation. You do not need to create a separate IAM role for this step.

**To create an AWS Config connector for GCP**

1. Create the AWS Config connector. Replace {{WORKLOAD\_IDENTITY\_POOL\_PROVIDER}} with the full resource name (`projects/{{HOST_PROJECT_NUMBER}}/locations/global/workloadIdentityPools{{/POOL_ID/}}providers/{{PROVIDER_ID}}`), {{CONFIG\_SERVICE\_ACCOUNT\_EMAIL}} with the AWS Config service account email (`aws-config-{{ACCOUNT_ID}}@{{HOST_PROJECT_ID}}.iam.gserviceaccount.com`), and {{ORGANIZATION\_ID}} with the numeric organization ID.

   ```
   aws configservice put-connector \
       --connector-configuration '{
           "gcp": {
               "workloadIdentityPoolProvider": "{{WORKLOAD_IDENTITY_POOL_PROVIDER}}",
               "serviceAccountEmail": "{{CONFIG_SERVICE_ACCOUNT_EMAIL}}",
               "gcpOrganizationId": "{{ORGANIZATION_ID}}"
           }
       }'
   ```

   Include `gcpOrganizationId` only if the host project belongs to a GCP organization. The value must match that organization. Otherwise, omit it. To check whether the host project belongs to an organization, run the following command:

   ```
   gcloud projects get-ancestors {{HOST_PROJECT_ID}}
   ```

   Note the `Arn` from the response – you need it in a later step.

1. Confirm the connector was created:

   ```
   aws configservice list-connectors
   ```
**Note**  
AWS Config allows one Config connector per host project. If one already exists, `put-connector` returns a `ConflictException`. In that case, use the existing connector's ARN from `list-connectors`.