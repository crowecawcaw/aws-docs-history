# Security Best Practices for SageMaker geospatial capabilities

Amazon SageMaker geospatial capabilities provide a number of security features to consider as you develop and implement your
own security policies. The following best practices are general guidelines and don't represent a complete
security solution. Because these best practices might not be appropriate or sufficient for your environment,
treat them as helpful considerations rather than prescriptions.

###### Apply principle of least privilege

Amazon SageMaker geospatial capabilities provide granular access policy for applications using IAM roles. We recommend that the roles
be granted only the minimum set of privileges required by the job. We also recommend auditing the
jobs for permissions on a regular basis and upon any change to your application.

###### Role-based access control (RBAC) permissions

Administrators should strictly control Role-based access control (RBAC) permissions
for Amazon SageMaker geospatial capabilities.

###### Use temporary credentials whenever possible

Where possible, use temporary credentials instead of long-term credentials, such as access keys.
For scenarios in which you need IAM users with programmatic access and long-term credentials,
we recommend that you rotate access keys. Regularly rotating long-term credentials helps
you familiarize yourself with the process. This is useful in case you are ever in a situation
where you must rotate credentials, such as when an employee leaves your company.
We recommend that you use IAM access last used information to rotate and remove access keys safely.
For more information, see [Rotating access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey") and
[Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").

###### Use AWS CloudTrail to view and log API calls

AWS CloudTrail tracks anyone making API calls in your AWS account.
API calls are logged whenever anyone uses the Amazon SageMaker geospatial capabilities API, the Amazon SageMaker geospatial capabilities console or
Amazon SageMaker geospatial capabilities AWS CLI commands. Enable logging and specify an Amazon S3 bucket to store the logs.

Your trust, privacy, and the security of your content are our highest priorities.
We implement responsible and sophisticated technical and physical controls designed
to prevent unauthorized access to, or disclosure of, your content and ensure that our
use complies with our commitments to you. For more information, see [AWS Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").
