

# Lambda function dependencies not appearing

**Symptom:** Lambda function dependencies are not discovered.

**Cause:** The service doesn't include the function or its VPC, or the function hasn't run since you enabled dependency discovery.

**Solution:** Verify that Service topology includes the function. If the function is connected to a VPC, also include the VPC. Then wait for the function to run. For other causes, see [Coverage and known limitations](next-gen-discovery-limitations.md).