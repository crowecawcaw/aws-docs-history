# Troubleshooting

This section covers common issues you might encounter when working with CloudWatch pipelines and
their solutions.

**Pipeline creation failures**

- **Issue:** Pipeline creation fails with
  permission errors

**Solution:** Verify that your IAM role has the
required PassRole permissions for any roles specified in the pipeline
configuration

- **Issue:** Configuration validation errors

**Solution:** Use the ValidateTelemetryPipeline
API to check your configuration syntax before creating the pipeline

- **Issue:** Log source not available to select

**Possible reason:** There is already a log source with the same data source name and type. Duplicate combinations are greyed out since you can only create one of each.
**Data processing issues**

- **Issue:** No data flowing through
  pipeline

**Solution:** Check that your data source is
properly configured and generating data, and verify that CloudWatch Logs
resource policies are correctly set

- **Issue:** Processor errors in pipeline

**Solution:** Review processor configuration and
ensure input data format matches processor expectations
