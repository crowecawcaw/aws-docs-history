# Use AMS SSP to provision AWS DataSync in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS DataSync capabilities directly in your AMS managed account. AWS DataSync moves large amounts of data online between on-premises storage and
Amazon S3, Amazon Elastic File System (Amazon Elastic File System) or Amazon FSx. Manual tasks related to data transfers
can slow down migrations and burden IT operations. DataSync eliminates or automatically handles many of
these tasks, including scripting copy jobs, scheduling and monitoring transfers, validating data, and
optimizing network utilization. The DataSync software agent connects to your Network File System (NFS)
and Server Message Block (SMB) storage, so you don’t have to modify your applications. DataSync can
transfer hundreds of terabytes and millions of files at speeds up to 10 times faster than open-source tools,
over the internet or AWS Direct Connect links. You can use DataSync to migrate active data sets or archives
to AWS, transfer data to the cloud for timely analysis and processing, or replicate data to AWS for business continuity.

To learn more, see [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/").

## DataSync in AWS Managed Services FAQ

**Q: How do I request access to DataSync in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_datasync_console_role`.

After provisioned in your account, you must onboard the roles in your federation solution.

The CloudWatch log group to use in order to stream task logs is "/aws/datasync".

**Q: What are the restrictions to using DataSync in my AMS account?**

Full functionality of AWS DataSync is available in your AMS account.

**Q: What are the prerequisites or dependencies to using DataSync in my AMS account?**

- Amazon S3 ARNs (Amazon Resource Names) are required for all S3 buckets associated with DataSync tasks that will be performed using the DataSync service role `customer_datasync_service_role`.
- VPC Endpoints and security groups for DataSync agents must be requested with
  an RFC with the Management | Other | Other | Create (ct-1e1xtak34nx76) change type prior to using VPC Endpoints.
- AWS DataSync agents run in AMS as an appliance. The AWS DataSync agent
  is patched and updated by the service; for details, see [AWS DataSync FAQ](https://aws.amazon.com/datasync/faqs/ "https://aws.amazon.com/datasync/faqs/").
- To launch an AWS DataSync agent,
  submit an RFC with the Management | Other | Other | Create
  (ct-1e1xtak34nx76) change type, requesting the agent be deployed.
  Provide the AWS DataSync Amazon EC2 AMI ID, instance type, subnet, security group;
  and either reference an existing Amazon EC2 keypair or request the creation of a
  new keypair.

###### Note

AMS provisions the AWS DataSync agent manually on behalf of customer, and doesn't
require the WIGS ingestion process on the AWS DataSync Amazon EC2 AMI.
