# Troubleshooting Slurm CLI Filter Plugin

issues in AWS PCS

Use this troubleshooting information to resolve common CLI Filter Plugin issues.

**Job submission fails immediately with plugin loading error**

**Symptoms:** Users receive error messages about missing or
failed CLI Filter Plugin when submitting jobs.

**Possible causes:**

- CLI Filter Plugin script missing from one or more nodes
- Incorrect script filename (must be exactly `cli_filter.lua`)
- Script deployed to wrong directory path
- Script has incorrect file permissions

**Resolution:**

- Verify script exists at
  `/etc/aws/pcs/scheduler/slurm-<version>/cli_filter.lua` on all
  login and compute nodes
- Check script filename is exactly `cli_filter.lua`
- Ensure script has readable permissions (644 or similar)
- Test script deployment on a single login node before deploying to full cluster

**Cluster creation fails with CLI Filter Plugin validation error**

**Symptoms:** Cluster creation fails with error about invalid
`CliFilterPlugins` parameter.

**Possible causes:**

- Incorrect parameter value format in `slurmCustomSettings`
- Typo in parameter name or value

**Resolution:**

- Use exact parameter name: `CliFilterPlugins`
- Use exact parameter value: `cli_filter/lua`
- Verify JSON syntax in `slurmCustomSettings` array

**CLI Filter Plugin script executes but job validation doesn't work as expected**

**Symptoms:** Jobs submit successfully but custom validation
logic doesn't trigger or produces unexpected results.

**Possible causes:**

- Lua script syntax errors
- Incorrect field access patterns (using Job Submit Plugin syntax instead of CLI Filter
  Plugin)
- Logic errors in validation conditions

**Resolution:**

- Review Lua script for syntax errors
- Verify field access uses `options["field_name"]` format instead of
  `job_desc.field_name`
- Add logging statements to debug script execution flow
- Test script logic with simple validation cases first

**S3 script deployment fails**

**Symptoms:** Instances launch but CLI Filter Plugin script is not
downloaded from S3.

**Possible causes:**

- IAM instance profile lacks S3 read permissions
- S3 VPC endpoint not configured
- Incorrect S3 bucket or object path in user data

**Resolution:**

- Verify IAM instance profile has `s3:GetObject` permission for your
  bucket
- Configure S3 VPC Gateway endpoint for direct access
- Check S3 bucket name and object path in user data script
- Review instance user data logs for S3 download errors
