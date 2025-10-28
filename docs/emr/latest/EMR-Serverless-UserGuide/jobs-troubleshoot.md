# Troubleshooting errors in EMR Serverless

Use the following information to help diagnose and fix common issues that occur
when working with Amazon EMR Serverless.

###### Topics

- [Error: Job failed as account has reached the service limit on the
  maximum vCPU it can use concurrently.](#jobs-troubleshoot-allowed-capacity-vcpu "#jobs-troubleshoot-allowed-capacity-vcpu")
- [Error: Job failed as application has exceeded maximumCapacity settings.](#jobs-troubleshoot-maxcapacity "#jobs-troubleshoot-maxcapacity")
- [Error: Job failed due to Worker could not be allocated as the application
  has exceeded maximumCapacity.](#jobs-troubleshoot-worker-allocated "#jobs-troubleshoot-worker-allocated")
- [Error: S3 access is denied. Please check S3 access
  permissions of the job runtime role on the required S3 resources.](#jobs-troubleshoot-s3 "#jobs-troubleshoot-s3")
- [Error: ModuleNotFoundError: No module named
  <module>. Please refer to the user guide on how to use python libraries with
  EMR Serverless.](#jobs-troubleshoot-module "#jobs-troubleshoot-module")
- [Error: Could not assume execution role
  <role name> because it does not exist or is not set up with the required trust
  relationship.](#jobs-troubleshoot-runtime-role "#jobs-troubleshoot-runtime-role")

## Error: Job failed as account has reached the service limit on the

maximum vCPU it can use concurrently.

This error indicates that EMR Serverless couldn't submit the job as the account has exceeded the maximum capacity. Increase
the maximum capacity for the account. Check your service limits
at [EMR Serverless service quotas](https://console.aws.amazon.com/servicequotas/home/services/emr-serverless/quotas "https://console.aws.amazon.com/servicequotas/home/services/emr-serverless/quotas").

## Error: Job failed as application has exceeded maximumCapacity settings.

This error indicates that EMR Serverless couldn't submit the job as the application has exceeded the configured
maximum capacity. Increase the maximum capacity for the application.

## Error: Job failed due to Worker could not be allocated as the application

has exceeded maximumCapacity.

This error indicates that the job couldn't complete. Workers couldn't be allocated because the application has
exceeded maximumCapacity settings.

## Error: S3 access is denied. Please check S3 access

permissions of the job runtime role on the required S3 resources.

This error indicates that your job doesn't have access to your S3 resources. Verify that
the job runtime role has permission to access the S3 resources that the job needs to use. To
learn more about runtime roles, refer to [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md "security-iam-runtime-role.md").

## Error: ModuleNotFoundError: No module named

<module>. Please refer to the user guide on how to use python libraries with
EMR Serverless.

This error indicates that a Python module wasn't available for the Spark job. Check that
the dependent Python libraries are available to the job. For more information on how to
package Python libraries, refer to [Using Python libraries with
EMR Serverless](using-python-libraries.md "using-python-libraries.md").

## Error: Could not assume execution role

<role name> because it does not exist or is not set up with the required trust
relationship.

This error indicates that the job runtime role that you specified for the job doesn't
exist, or that the role doesn't have a trust relationship for EMR Serverless permissions.
To verify that the IAM role exists and validate that you have set up the role’s trust
policy properly, see the instructions in [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md "security-iam-runtime-role.md").
