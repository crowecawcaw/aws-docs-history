# Use AMS SSP to provision Amazon Simple Workflow Service in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Simple Workflow Service (Amazon SWF) capabilities directly in your AMS managed account. Amazon Simple Workflow Service helps developers build, run, and scale background jobs that have parallel or
sequential steps. You can think of Amazon SWF as a fully-managed state tracker and task
coordinator in the Cloud. If your application's steps take more than 500 milliseconds to complete,
you need to track the state of processing, or you need to recover or retry if a task fails,
Amazon SWF can help you.
To learn more, see [Amazon Simple Workflow Service](https://aws.amazon.com/swf/ "https://aws.amazon.com/swf/").

## Amazon SWF in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon SWF in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service |
Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account:
`customer_swf_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon SWF in my AMS account?**

The Lambda `InvokeFunction` permissions have been included in
this service however, the AMS `customer_deny_policy` that is
added to all AMS customer roles explicitly denies access to AMS Lambda
functions and AMS-owned resources. In order to tag or untag resources
within Amazon SWF, submit a Management | Other | Other Change Type.

**Q: What are the prerequisites or dependencies to using Amazon SWF in my AMS account?**

Amazon SWF is dependent on the AWS Lambda service, therefore, permissions to
invoke Lambda have been provided as a part of this role and no additional
permissions are required to invoke Lambda from Amazon SWF. Otherwise, there are no
prerequisites to using Amazon SWF.
