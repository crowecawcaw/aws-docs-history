

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites for connecting Amazon Q Business to Amazon FSx (Windows)
<a name="fsx-windows-prereqs"></a>

Before you begin, make sure that you have completed the following prerequisites.

**In Amazon FSx (Windows), make sure you have:**
+ An Amazon FSx (Windows) account with read and mounting permissions.
+ Noted your Amazon FSx authentication credentials for an Active Directory user account. This includes your Active Directory username and your Domain Name System (DNS) domain name. For example, {{user@corp.example.com}}.
+ Copied your Amazon FSx file system ID.
+ Used an Amazon VPC (AWS VPC) where your Amazon FSx resides.

**In your AWS account, make sure you have:**
+ Created a Amazon Q Business application.
+ Created a [Amazon Q Business retriever and added an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html).
+ Created an [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html#iam-roles-ds) for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
+ Stored your Amazon FSx (Windows) authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret.
**Note**  
If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [ Data source connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).

You must also make sure you have configured your Amazon VPC instance with a NAT Gateway. For instructions on how to do this, see Step 1 of [Connecting to a database in a VPC.](https://docs.aws.amazon.com/kendra/latest/dg/vpc-example.html#vpc-example-1)