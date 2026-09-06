

# CloudFormation stack not found
<a name="next-gen-troubleshoot-cfn-not-found"></a>

**Symptom:** Resource discovery fails with "stack not found."

**Solutions:**
+ Verify the stack ARN is correct and the stack exists.
+ Verify the invoker role has `cloudformation:DescribeStackResources` permission.
+ For cross-account stacks, verify the cross-account role has access.