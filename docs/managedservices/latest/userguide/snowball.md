# Use AMS SSP to provision AWS Snowball Edge in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Snowball Edge capabilities directly in your AMS managed account. Snowball Edge is a petabyte-scale data transport solution that uses devices designed to be secure, to transfer large amounts
of data into and out of the AWS Cloud.
Snowball Edge addresses common challenges with large-scale data transfers including high network costs, long transfer times, and
security concerns.
You can use Snowball Edge to migrate analytics data, genomics data, video libraries, image repositories, backups, and to archive
part of data center shutdowns,
tape replacement or application migration projects. Transferring data with Snowball Edge is simple, fast, more secure, and can be as little as one-fifth the
cost of transferring data by way of high-speed Internet.

With Snowball Edge, you don’t need to write any code or purchase any hardware to transfer your data. Start by using the
AWS Management Console to
[Create an Import Job](../../../snowball/latest/ug/create-import-job.md "../../../snowball/latest/ug/create-import-job.md") for Snowball, and a
Snowball device will be automatically shipped to you. Once it arrives, attach the device to your local network, download and run the Snowball Client ("Client")
to establish a connection, and then use the Client to select the file directories that you want to transfer to the device. The Client then encrypts and transfers the files
to the device at high speed. Once the transfer is complete and the device is ready to be returned,
the E Ink shipping label automatically updates and you can track
the job status with Amazon Simple Notification Service (Amazon SNS), text messages, or directly in the Console.
To learn more, see [AWS Snowball Edge](https://aws.amazon.com/snowball/ "https://aws.amazon.com/snowball/").

## Snowball Edge in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS Snowball Edge in my AMS account?**

Implementation of Snowball Edge in AMS is a two-step process:

1. Submit a Management | Other | Other | Create (ct-1e1xtak34nx76) change type and request a
   service role for Snowball Edge for your AMS Account.
2. Request user access by submitting a
   Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct). This RFC provisions the following
   IAM roles to your account: `customer_snowball_console_role`, `customer_snowball_export_role`, and
   `customer_snowball_import_role`. After it's provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS Snowball Edge in my AMS account?**

Full functionality of the AWS Snowball Edge is available in your AMS account.

**Q: What are the prerequisites or dependencies to using AWS Snowball Edge in my AMS account?**

You must have the service role account as noted above.
