# Use AMS SSP to provision AWS Migration Hub in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Migration Hub capabilities directly in your AMS managed account. AWS Migration Hub provides a single location where you can track the progress of application migrations across multiple AWS
and partner solutions. Using Migration Hub allows you to choose the AWS and partner migration tools that best fit your needs,
while providing visibility into the status of migrations across your application portfolio. Migration Hub also provides key
metrics and progress for individual applications, regardless of which tools are being used to migrate them. This allows
you to quickly get progress updates across all of your migrations, easily identify and troubleshoot any issues, and
reduce the overall time and effort spent on your migration projects.
To learn more, see [AWS Migration Hub](https://aws.amazon.com/migration-hub/ "https://aws.amazon.com/migration-hub/").

## Migration Hub in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Migration Hub in my AMS account?**

Request access to Migration Hub by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct)
change type. This RFC provisions the following IAM role to your account:
`customer_migrationhub_author_role`. Once
provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions for Migration Hub?**

None.

**Q: What are the prerequisites to enable Migration Hub?**

There are no prerequisites to start using Migration Hub in your AMS account. However, permissions outside Migration Hub
might be required during
the management of the service, such as writing permissions to Amazon S3 to upload server information.
