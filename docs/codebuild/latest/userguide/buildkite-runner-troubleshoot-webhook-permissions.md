# Troubleshoot the

webhook permission issues

**Issue:**

The Buildkite job fails to checkout the job's source repository due to permission
issues.

**Possible causes:**

- CodeBuild does not have sufficient permissions to checkout the job's source
  repository.
- The pipeline's repository settings are set to check out using SSH for CodeBuild
  managed credentials.

**Recommended solutions:**

- Verify that CodeBuild has sufficient permissions configured to check out the job's
  source repository. Additionally, verify that your CodeBuild project's service role
  has sufficient permissions to access the configured source permission
  option.
- Verify that your Buildkite pipeline is configured to use checkout using HTTPS
  if you are using CodeBuild managed source repository credentials.
