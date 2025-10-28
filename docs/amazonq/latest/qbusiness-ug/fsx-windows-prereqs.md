# Prerequisites for connecting Amazon Q Business to Amazon FSx (Windows)

Before you begin, make sure that you have completed the following
prerequisites.

**In Amazon FSx (Windows), make sure you have:**

- An Amazon FSx (Windows) account with read and mounting permissions.
- Noted your Amazon FSx authentication credentials for an Active Directory user
  account. This includes your Active Directory username and your Domain Name System (DNS)
  domain name. For example, `user@corp.example.com`.
- Copied your Amazon FSx file system ID.
- Used an Amazon VPC (AWS VPC) where your Amazon FSx
  resides.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Amazon FSx (Windows) authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

You must also make sure you have configured your Amazon VPC instance with a NAT Gateway. For
instructions on how to do this, see Step 1 of [Connecting
to a database in a VPC.](../../../kendra/latest/dg/vpc-example.md#vpc-example-1 "../../../kendra/latest/dg/vpc-example.md#vpc-example-1")
