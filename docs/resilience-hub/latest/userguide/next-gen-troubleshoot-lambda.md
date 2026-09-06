

# Non-VPC Lambda not appearing
<a name="next-gen-troubleshoot-lambda"></a>

**Symptom:** Lambda function dependencies are not discovered.

**Cause:** Lambda functions not connected to a VPC do not make DNS queries through Route 53 resolvers.

**Solution:** Either connect the Lambda function to a VPC, or manually track its dependencies outside of Resilience Hub.