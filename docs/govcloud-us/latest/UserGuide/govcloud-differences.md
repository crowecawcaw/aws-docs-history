# AWS GovCloud (US) Compared to Standard AWS

Regions

AWS GovCloud (US) are isolated AWS Regions designed to allow U.S. government agencies and
customers to move sensitive workloads into [the cloud](https://aws.amazon.com/what-is-cloud-computing/ "https://aws.amazon.com/what-is-cloud-computing/") by addressing their
specific regulatory and compliance requirements, including Federal Risk and Authorization Management Program (FedRAMP) High,
Department of Defense Security Requirements Guide (DoD SRG) Impact Level 5, and Criminal Justice Services (CJIS).
To assist customers in managing their obligations under U.S. export control regimes such as the International Traffic in Arms
Regulations (ITAR) and the Export Administration Regulations (EAR), AWS GovCloud (US) are logically and physically administered
exclusively by U.S. citizens

- AWS GovCloud (US) uses FIPS 140-3 approved cryptographic modules for
  all AWS service API endpoints, unless otherwise indicated in the [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md") section.
- AWS GovCloud (US) is appropriate for all types of Controlled Unclassified Information (CUI) and
  unclassified data. For more details, see [Maintaining U.S. International Traffic in Arms
  Regulations (ITAR) Compliance](govcloud-itar.md "govcloud-itar.md").
- The AWS GovCloud (US) Regions are physically isolated and have logical network
  isolation from all other AWS Regions.
- AWS restricts all physical and logical access for those staff supporting
  AWS GovCloud (US) to US Citizens.
  AWS allows only vetted U.S. citizens with distinct access controls separate from
  other AWS Regions to administer AWS GovCloud (US). Any customer data
  fields that are defined as outside of the ITAR boundary (such as S3 bucket
  names) are explicitly documented in the service-specific section as not
  permitted to contain export-controlled data.
- AWS GovCloud (US) authentication is completely isolated from
  Amazon.com.
  AWS GovCloud (US) Regions also have high-level differences compared to the standard AWS
  Regions. The standard AWS practice of using two AWS Regions in a partition remains. In this case, using both AWS AWS GovCloud (US) Regions for architecture is preferred. These differences are important when you evaluate and use
  AWS GovCloud (US). The following list outlines the differences:

Sign up

During the sign-up process, each customer is reviewed to determine if they are a
U.S. entity (such as a government body, contracting company, or educational
organization) where account credentials will be managed by a U.S. Person.

Endpoints

AWS GovCloud (US) uses endpoints that are specific to
AWS GovCloud (US) and are publicly available from the Internet but are accessible only to AWS GovCloud (US)
customers. For a list of these endpoints, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").

Credentials

You can access AWS GovCloud (US) only with AWS GovCloud (US)
credentials (AWS GovCloud (US) account access key and AWS GovCloud (US) IAM user
credentials). You cannot access AWS GovCloud (US) with standard AWS
credentials. Likewise, you cannot access standard AWS Regions using
AWS GovCloud (US) credentials.

AWS Management Console for the AWS GovCloud (US) Region

You sign in to the AWS GovCloud (US) console by using an IAM user name
and password. This requirement is different from the standard AWS Management Console,
where you can sign in using your account credentials (email address and
password). You cannot use your AWS GovCloud (US) account access keys to sign in
to the AWS GovCloud (US) console. For more information about creating an
IAM user, see [Getting Started with AWS GovCloud (US)](getting-set-up.md "getting-set-up.md").

Billing, account activity, and usage reports

An AWS GovCloud (US) account is always associated to a single standard AWS
account for billing and payment purposes. All AWS GovCloud (US) billing is
billed or invoiced to the associated standard AWS account. You can view the
AWS GovCloud (US) account activity and usage reports through the associated AWS
standard account only.

Services

Services in the AWS GovCloud (US) Regions might have different capabilities
compared to services in standard AWS Regions. For detailed information
about each service in the AWS GovCloud (US) Regions, see [Using AWS GovCloud (US) Regions](using-govcloud.md "using-govcloud.md").

For all AWS GovCloud (US) accounts created after December 15, 2014, AWS CloudTrail
will be automatically enabled with logging turned on. Amazon SNS notifications,
however, must be set up independently. If you prefer not to have CloudTrail
enabled, you can use the CloudTrail console in the AWS Management Console for
AWS GovCloud (US) to disable it or turn off logging.

Multi-factor authentication

AWS GovCloud (US) users can use the same FIDO security tokens or virtual authenticator apps as commercial users.
However, if instead opting for a TOTP hardware token for MFA, AWS GovCloud (US) users need to use a special device.
This is due to the separate authentication stack. For more information, see the list of AWS GovCloud (US)-supported MFA
devices on the [Multi-Factor
Authentication](https://aws.amazon.com/iam/details/mfa/ "https://aws.amazon.com/iam/details/mfa/") page.
