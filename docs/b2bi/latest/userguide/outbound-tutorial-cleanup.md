

# Cleanup steps
<a name="outbound-tutorial-cleanup"></a>

Proper cleanup prevents ongoing charges for unused resources and maintains a clean AWS environment. This section ensures you remove all outbound tutorial resources while preserving any configurations you want to keep.

## Remove test files
<a name="outbound-remove-test-files"></a>

**To clean up test data**

1. Navigate to both Amazon S3 buckets in the Amazon S3 console.

1. Delete all test JSON files and generated EDI outputs.

1. Empty both buckets completely if you don't plan to use them.

## Delete AWS B2B Data Interchange resources
<a name="outbound-delete-b2bi-resources"></a>

**To remove outbound AWS B2B Data Interchange resources**

1. **Delete Partnership:**

   1. Go to **Partnerships** in the AWS B2B Data Interchange console.

   1. Select **SupplierXYZ-Outbound-Partnership**.

   1. Choose **Delete** and confirm.

1. **Delete Trading Capability:**

   1. Go to **Trading capabilities**.

   1. Select **Outbound-850-Generation**.

   1. Choose **Delete** and confirm.

1. **Delete Transformer:**

   1. Go to **Transformers**.

   1. Select **JSON-to-X12-850-Transformer**.

   1. Set status to **Inactive** first, then choose **Delete**.

1. **Delete Profile:**

   1. Go to **Profiles**.

   1. Select **AcmeCorpOutboundProfile**.

   1. Choose **Delete** and confirm.

## Remove Amazon S3 resources
<a name="outbound-remove-s3-resources"></a>

**To delete Amazon S3 buckets**

1. In the Amazon S3 console, select **my-b2bi-outbound-input-bucket-{{your-account-id}}**.

1. Choose **Delete** and confirm by typing the bucket name.

1. Repeat for **my-b2bi-outbound-output-bucket-{{your-account-id}}**.

## Clean up monitoring resources
<a name="outbound-cleanup-monitoring-resources"></a>
+ **CloudWatch Logs:** Log groups are automatically cleaned up when profiles are deleted. Manually delete any custom log groups you created.
+ **EventBridge Rules:** Delete any custom EventBridge rules you created for monitoring.

## Verification
<a name="outbound-cleanup-verification"></a>

After cleanup, verify:
+ No AWS B2B Data Interchange outbound resources remain in the console
+ Amazon S3 buckets are deleted (check billing to ensure no storage charges)
+ No unexpected CloudWatch or EventBridge charges appear

**Important**  
Always verify resource deletion to avoid unexpected charges. Some resources may have dependencies that prevent immediate deletion.