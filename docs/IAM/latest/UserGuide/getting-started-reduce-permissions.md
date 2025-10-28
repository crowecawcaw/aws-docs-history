# Prepare for least-privilege

permissions

Using _least-privilege permissions_ is an IAM best practice
recommendation. The concept of least-privilege permissions is to grant users the permissions
required to perform a task and no additional permissions. As you get set up, consider how you
are going to support least-privilege permissions. The root user, the administrative user, and the
emergency access IAM user have powerful permissions that aren't required for everyday tasks.
While you are learning about AWS and testing out different services we recommend that you
create at least one additional user in IAM Identity Center with lesser permissions that you can use in
different scenarios. You can use IAM policies to define the actions that can be taken on
specific resources under specific conditions and then connect to those resources with your
lesser privileged account.

If you are using IAM Identity Center, consider using IAM Identity Center permissions sets to get started. To learn more,
see [Create a permission
set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _IAM Identity Center User Guide_.

If you aren't using IAM Identity Center, use IAM roles to define the permissions for different IAM
entities. To learn more, see [IAM role creation](id_roles_create.md "id_roles_create.md").

Both IAM roles and IAM Identity Center permissions sets can use AWS managed policies based on job
functions. For details on the permissions granted by these policies, see [AWS managed policies for job functions](access_policies_job-functions.md "access_policies_job-functions.md").

###### Important

Keep in mind that AWS managed policies might not grant least-privilege permissions for
your specific use cases because they're available for use by all AWS customers. After
getting set up, we recommend that you use IAM Access Analyzer to generate least-privilege policies
based on your access activity that's logged in AWS CloudTrail. For more information about policy
generation, see [IAM Access Analyzer policy
generation](access-analyzer-policy-generation.md "access-analyzer-policy-generation.md").

When you are getting started, we recommend that you use AWS managed policies to grant
permissions. After a predefined sample period of activity (such as 90 days) has passed, you can
review the services that people and workloads have accessed. Then you can create a new customer
managed policy with reduced permissions to replace the AWS managed policy. The new policy
should include only the services that were accessed during the sample period. Update your
permissions to remove the AWS managed policy and attach the new customer managed policy you
created.
