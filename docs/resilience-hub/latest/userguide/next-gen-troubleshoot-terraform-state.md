

# Terraform state file not accessible
<a name="next-gen-troubleshoot-terraform-state"></a>

**Symptom:** Resource discovery fails reading the Terraform state file.

**Solutions:**
+ Verify the Amazon S3 bucket and key path are correct.
+ Verify the invoker role has `s3:GetObject` permission on the state file.
+ Verify the state file is in a supported format.