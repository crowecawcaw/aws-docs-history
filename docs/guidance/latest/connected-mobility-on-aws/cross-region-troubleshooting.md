

# Cross-region deployment troubleshooting
<a name="cross-region-troubleshooting"></a>

## Problem: Deployment fails with resource-name collision in a second region
<a name="problem-cross-region-resource-collision"></a>

A CDK deployment to a second AWS Region fails with an error such as `BucketAlreadyOwnedByYou`, `BucketAlreadyExists`, `CloudFront alias already in use`, or an IAM role-name conflict. This occurs because some AWS resource names occupy a global or account-wide namespace and collide with the same-stage deployment in the primary region.

### Diagnosis
<a name="diagnosis-5"></a>

The three resource types most likely to collide are:
+  **S3 buckets** — names are globally unique across all regions in the partition.
+  **CloudFront aliases (CNAMEs)** — a custom domain alias can only be associated with one distribution.
+  **IAM roles** — role names are unique within an AWS account regardless of region.

Identify the failing resource from the CloudFormation event:

```
STAGE=staging
REGION=ap-northeast-1
aws cloudformation describe-stack-events \
  --stack-name cms-$STAGE-ui \
  --region $REGION \
  --query "StackEvents[?ResourceStatus=='CREATE_FAILED'].[LogicalResourceId,ResourceStatusReason]" \
  --output table
```

### Resolution
<a name="resolution-23"></a>

 **S3 bucket name collision:** 

All CMS S3 bucket names are suffixed with both the AWS account ID and the region (for example, `cms-staging-storage-invoices-<account>-<region>`). If a bucket name collision occurs, verify that the stack code uses the `{stage}-{account}-{region}` suffix pattern and not a shorter `{stage}-{account}`-only form. Redeploy the affected stack after confirming the naming convention is in place.

 **CloudFront alias collision:** 

A custom domain alias (CNAME) can only be associated with one CloudFront distribution. When deploying to a second region, ensure the `cms.uiCustomDomain` CDK context key is either unset or set to a region-specific subdomain. A deployment without a custom domain (no `cms.uiCustomDomain` context key) uses the default CloudFront `*.cloudfront.net` domain and avoids this collision entirely.

If `cdk.context.json` was populated by a prior primary-region deployment, the persisted context values may override the second-region intent. Use CDK context isolation (see the deployment guide) or pass explicit context overrides on the command line:

```
cdk deploy cms-$STAGE-ui \
  --context cms.uiCustomDomain="" \
  --region $REGION
```

 **IAM role name collision:** 

IAM role names are account-wide. If you see an IAM role-name conflict, check whether the role name includes a region suffix. The guidance ships all globally-scoped resource names with an `{account}-{region}` suffix by default. If a custom role name was set via CDK context without a region component, add the region suffix.

Refer to the cross-region namespace discipline in the deployment guide for the full naming convention rules and the per-resource length budget across all AWS Regions.