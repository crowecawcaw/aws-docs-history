# Cleanup steps

Proper cleanup prevents ongoing charges for unused resources and maintains a clean
AWS environment. This section ensures you remove all outbound tutorial resources while
preserving any configurations you want to keep.

## Remove test files

###### To clean up test data

1. Navigate to both Amazon S3 buckets in the Amazon S3 console.
2. Delete all test JSON files and generated EDI outputs.
3. Empty both buckets completely if you don't plan to use them.

## Delete AWS B2B Data Interchange resources

###### To remove outbound AWS B2B Data Interchange resources

1. **Delete Partnership:**
   1. Go to **Partnerships** in the AWS B2B Data Interchange
      console.
   2. Select
      **SupplierXYZ-Outbound-Partnership**.
   3. Choose **Delete** and confirm.

2. **Delete Trading Capability:**
   1. Go to **Trading capabilities**.
   2. Select **Outbound-850-Generation**.
   3. Choose **Delete** and confirm.

3. **Delete Transformer:**
   1. Go to **Transformers**.
   2. Select **JSON-to-X12-850-Transformer**.
   3. Set status to **Inactive** first, then choose
      **Delete**.

4. **Delete Profile:**
   1. Go to **Profiles**.
   2. Select **AcmeCorpOutboundProfile**.
   3. Choose **Delete** and confirm.

## Remove Amazon S3 resources

###### To delete Amazon S3 buckets

1. In the Amazon S3 console, select
   `my-b2bi-outbound-input-bucket-`your-account-id``.
2. Choose **Delete** and confirm by typing the bucket
   name.
3. Repeat for
   `my-b2bi-outbound-output-bucket-`your-account-id``.

## Clean up monitoring

resources

- **CloudWatch Logs:** Log groups are automatically
  cleaned up when profiles are deleted. Manually delete any custom log groups
  you created.
- **EventBridge Rules:** Delete any custom EventBridge rules
  you created for monitoring.

## Verification

After cleanup, verify:

- No AWS B2B Data Interchange outbound resources remain in the console
- Amazon S3 buckets are deleted (check billing to ensure no storage
  charges)
- No unexpected CloudWatch or EventBridge charges appear

###### Important

Always verify resource deletion to avoid unexpected charges. Some resources
may have dependencies that prevent immediate deletion.
