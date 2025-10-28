# Use AMS SSP to provision Amazon AppStream 2.0 in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon AppStream 2.0 (AppStream 2.0) capabilities directly in your AMS managed account. AppStream 2.0 lets you move your desktop applications
to AWS, without rewriting them.
You can install your applications on AppStream 2.0, set launch configurations, and make your
applications available to users. AppStream 2.0 offers a wide selection of virtual machine options
so that you can select the instance type that best matches your application requirements,
and set the auto-scale parameters so that you can easily meet the needs of your end users.
AppStream 2.0 enables you to launch applications in your own network, which means your applications
can interact with your existing AWS resources.

Amazon AppStream 2.0 enables you to quickly and easily install, test, and update your applications
using the image builder. Any application that runs on Microsoft Windows Server 2012 R2,
Windows Server 2016, or Windows Server 2019 is supported, and you don’t need to make any
modifications. When your testing is complete, you can set application launch configurations,
default user settings, and publish your image for users to access.

To learn more, see
[AppStream 2.0](https://aws.amazon.com/appstream2/ "https://aws.amazon.com/appstream2/").

## AppStream 2.0 in AWS Managed Services FAQ

**Q: How do I request access to AppStream 2.0 in my AMS account?**

Request access to AppStream 2.0 by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_appstream_console_role`.

A `customer_appstream_stream_role` is also deployed to stream applications
that require users to be authenticated using their Active Directory login credentials.

Once provisioned in your account, you must onboard the roles in your federation solution.

**Q: What are the restrictions to using AppStream 2.0 in my AMS account?**

- The following functionality must be configured by the AMS Support team, and requires
  specific RFCs. Instruction on requesting additional functionality can be found in section 4.
  - Creating and Streaming from Interface VPC Endpoints.
  - Support for Amazon S3 endpoints for home folders and application setting persistence on a private network.
  - Creating and choosing the IAM role that will be available on all fleet streaming instances.
  - Joining AppStream 2.0 fleets and image builders Microsoft Active Directory domains.
  - Creating AppStream 2.0 Custom Usage Reports.
  - Custom branding is currently not supported.

**Q: What are the prerequisites or dependencies to using AppStream 2.0 in my AMS account?**

While submitting the RFC to onboard AppStream 2.0, include the Amazon S3 bucket name to be used for the AppStream 2.0 usage report. The bucket name is added to the
`customer-appstream-usagereports-policy` that is created when AppStream 2.0 is onboarded.

**Q: What AppStream 2.0 functionality requires separate RFCs?**

- In order to choose an interface VPC endpoint for AppStream 2.0, submit a Management | Other | Other |
  Update change type RFC to create a VPC endpoint in your account. For
  steps to create custom endpoints for AppStream 2.0, see
  [Creating and Streaming from Interface VPC Endpoints](../../../appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.md "../../../appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.md") in the AppStream 2.0 user guide.
- Support for Amazon S3 endpoints for home folders and application setting persistence on a private
  network can be configured by requesting Amazon S3 VPC endpoints with a
  Management | Other | Other | Create change type RFC. The RFC must
  include the target Amazon S3 bucket hosting the home folder contents, or
  application settings Amazon S3 buckets, respectively. This RFC will provide
  AppStream 2.0 the permissions it needs to access Amazon S3 VPC endpoints.
  For steps to create custom endpoints for streams, see
  [Using Amazon S3 VPC Endpoints for Home Folders and Application Settings Persistence](../../../appstream2/latest/developerguide/managing-network-vpce-iam-policy.md "../../../appstream2/latest/developerguide/managing-network-vpce-iam-policy.md") in the AppStream 2.0 user guide.
- In order to create and choose an IAM role that will be available on all fleet streaming
  instances, submit a Deployment | Advanced stack components | Identity and Access Management (IAM) | Create entity or policy (managed automation) change type (ct-3dpd8mdd9jn1r)
  RFC requesting the IAM role with the required policy. The IAM role
  name should always start with prefix : "customer_appstream".
- Amazon AppStream 2.0 fleets and image builders can be joined to domains in
  Microsoft Active Directory by submitting a Management | Other | Other | Update change type
  RFC for the Service Account creation in Active Directory (AD). Minimal permissions
  required to join Microsoft Active Directory are defined in the AppStream 2.0 documentation at
  [Granting Permissions to Create and Manage Active Directory Computer Objects](../../../appstream2/latest/developerguide/active-directory-admin.md#active-directory-permissions "../../../appstream2/latest/developerguide/active-directory-admin.md#active-directory-permissions").
- In order to create custom AppStream 2.0 Usage Reports, submit a Management | Other | Other | Create
  change type RFC requesting following:

      + "AppStreamUsageReports" CFN stack creation
      + "customer\_appstream\_usagereports\_role" be provisioned in the account
      + Also, provide the following details:




      	- Provide CRON expression to schedule Crawler run. By default it is 23:00 UTC everyday.
      	- Amazon S3 bucket ARN to be used for Athena query results. This bucket should have prefix: `aws-athena-query-results`
      	- Amazon S3 bucket ARN for AppStream 2.0 Usage Reports Logs.

  After the role is provisioned, onboard the role into your federation solution and login, then access AWS GlueAWS Glue and Athena for generating
  custom reports using the usage report role. For details about using AppStream 2.0 Usage Reports see
  [Create Custom Reports and Analyze AppStream 2.0 Usage Data](../../../appstream2/latest/developerguide/configure-custom-reports-analyze-usage-data.md "../../../appstream2/latest/developerguide/configure-custom-reports-analyze-usage-data.md"), in the AppStream 2.0 documentation.
