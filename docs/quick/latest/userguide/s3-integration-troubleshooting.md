

# Troubleshooting Amazon S3 integration issues
<a name="s3-integration-troubleshooting"></a>

If you encounter issues connecting to your Amazon S3 bucket, review the following common causes and solutions.

## Documents not appearing in ACL-enabled knowledge base
<a name="s3-troubleshooting-acl-documents-missing"></a>

**Issue:** Documents are not ingested into an ACL-enabled knowledge base.

**Solution:** For ACL-enabled knowledge bases, documents without an associated ACL entry are not ingested. Verify that every document has an ACL defined either through the global ACL file or in its metadata file. For more information, see [Document-level ACLs](s3-acl.md).

## Cross-account access not configured
<a name="s3-troubleshooting-cross-account"></a>

**Issue:** Your administrator hasn't granted access to use Amazon S3 buckets from other AWS accounts in Amazon Quick.

**Solution:** Ask your administrator to grant cross-account Amazon S3 access. For more information, see [Grant Amazon Quick access to Amazon S3 buckets](s3-admin-setup.md#s3-grant-bucket-access).

## Bucket not in approved list
<a name="s3-troubleshooting-bucket-not-approved"></a>

**Issue:** The bucket you're trying to access hasn't been authorized by your administrator.

**Solution:**
+ Confirm the bucket name is spelled correctly.
+ Verify with your administrator that the bucket is included in the approved list.
+ Request your administrator to add the bucket to the authorized buckets list if needed.

## Insufficient IAM permissions
<a name="s3-troubleshooting-iam-permissions"></a>

**Issue:** Your IAM role or user lacks the necessary permissions to access the Amazon S3 bucket.

**Solution:**
+ Verify your IAM policy includes the required Amazon S3 permissions:
  + `s3:GetObject`
  + `s3:ListBucket`
  + `s3:GetBucketLocation`
  + `s3:GetObjectVersion`
  + `s3:ListBucketVersions`
+ Check your own buckets for any explicit Deny statements that might be blocking access.

**Note**  
The ARN `arn:aws:iam::account-id:role/service-role/aws-quicksight-service-role-v0` is the default service role used when no custom role has been created. If a custom service role exists, contact your administrator to obtain the custom service role ARN and use it instead of the default.

## Cross-region restrictions
<a name="s3-troubleshooting-cross-region"></a>

**Issue:** The Amazon S3 bucket is located in a different AWS region than your Amazon Quick account or service.

**Solution:**
+ Verify the bucket region matches your Amazon Quick service region.
+ Check bucket region using AWS CLI: `aws s3api get-bucket-location --bucket bucket-name`
+ Use a bucket in the same region as your service.

## Additional troubleshooting steps
<a name="s3-troubleshooting-additional-steps"></a>
+ **Test bucket accessibility** using AWS CLI:

  ```
  aws s3 ls s3://bucket-name --profile your-profile
  ```
+ **Review CloudTrail logs** for AccessDenied errors to identify the specific permission issue.
+ **Check Amazon S3 Block Public Access settings** - while these typically don't affect authenticated access, verify they're not interfering with your specific use case.
+ **Verify bucket ownership** - ensure the bucket exists and you have the correct bucket name.