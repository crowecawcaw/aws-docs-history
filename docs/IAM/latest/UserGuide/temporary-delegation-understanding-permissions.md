# Understanding permissions

As part of the feature onboarding process, you will need to register policies with IAM that define the permissions you want to request in customers' AWS accounts. The registration process provides a more consistent experience for customers and helps avoid common pitfalls in policy authoring.

During registration, AWS evaluates your policies against a set of validations. These validations are intended to standardize policy formatting and structure, and provide basic protections against known anti-patterns. The validations also reduce the risk of privilege escalations, unintended cross-account access, and broad access to high-value resources in customer accounts.

## Permission Types

AWS will consider two categories of permissions: temporary and long-term.

### Temporary Permissions

Temporary permissions limit the permissions assigned to any temporary delegated access sessions. Temporary permissions are described in policy templates that are applied to the delegated session. The templates support parameters that you supply when you create a delegation request. These parameter values are then bound to the session. The temporary permissions work in the same way as the session policies available in AWS STS today: the policies limit the capability of the underlying user, but do not grant any additional access. For more information, see the AWS STS documentation on session policies.

### Long-Term Permissions

Long-term permissions limit the permissions of any roles that are created or managed via temporary access. Long-term permissions are implemented as IAM permissions boundaries. You may submit one or more permission boundaries to AWS as part of onboarding. Once approved, AWS will share a policy ARN with you that you can reference in your policies.

These boundary policies have two noteworthy features. First, they are immutable. If you want to update permissions, you can register a new permissions boundary. You can then attach the new permissions boundary to your customers' roles by sending a new delegation request. Second, the policies are not templated. Since the same boundary policy is globally shared, they cannot be altered on a per-customer basis.

###### Important

Permission boundaries have a maximum size limit of 6,144 characters.

###### Note

If you would like to update a permission boundary or policy template, contact IAM at aws-iam-partner-onboarding@amazon.com. Once the new permission boundary is registered, you can then send a delegation request to customers to update the IAM role and attach the newly registered permission boundary. See the Examples section for more details.

## Example Use Case: Data Processing Workload

Consider a product provider that runs a data processing workload in customer accounts. The provider needs to set up infrastructure during initial onboarding, but also requires ongoing access to operate the workload.

_Temporary permissions (for initial setup):_

- Create Amazon EC2 instances, VPC, and security groups
- Create an Amazon S3 bucket for processed data
- Create an IAM role for ongoing operations
- Attach a permission boundary to the IAM role

_Long-term permissions (IAM role with permission boundary for ongoing operations):_

- Start and stop Amazon EC2 instances to run processing jobs
- Read input data from Amazon S3 bucket
- Write processed results to Amazon S3 bucket

The temporary permissions are used once during onboarding to configure the infrastructure. The IAM role created during this process has a permission boundary that limits its maximum permissions to only the operations needed for ongoing workload management. This ensures that even if the role's policies are modified, it cannot exceed the permissions defined in the boundary.
