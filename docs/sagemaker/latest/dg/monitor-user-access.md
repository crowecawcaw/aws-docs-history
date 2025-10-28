# Monitoring user resource access from SageMaker AI

Studio Classic with sourceIdentity

With Amazon SageMaker Studio Classic, you can monitor user resource access. To view resource access activity,
you can configure AWS CloudTrail to monitor and record user activities by following
the steps in [Log Amazon SageMaker API Calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

However, the AWS CloudTrail logs for resource access only list the Studio Classic
execution IAM role as the identifier. This level of logging is enough to audit user activity
when each user profile has a distinct execution role. However, when a single execution IAM
role is shared between several user profiles, you can't get information about the specific user
that accessed the AWS resources. 

You can get information about which specific user performed an action in an
AWS CloudTrail log when using a shared execution role, using
the `sourceIdentity` configuration to propagate the Studio Classic user profile name. For
more information about source identity, see [Monitor and control
actions taken with assumed roles](../../../IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.md "../../../IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.md"). To turn `sourceIdentity` on or off for your
CloudTrail logs, see [Turn on sourceIdentity in CloudTrail logs for SageMaker AI
Studio Classic](monitor-user-access-how-to.md "monitor-user-access-how-to.md").

## Considerations when using

sourceIdentity

When you make AWS API calls from Studio Classic notebooks, SageMaker Canvas, or Amazon SageMaker Data Wrangler, the
`sourceIdentity` is only recorded in CloudTrail if those calls are made using the
Studio Classic [execution role](sagemaker-roles.md "sagemaker-roles.md") session or any [chained
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-role-chaining "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-role-chaining") from that session.

When these API calls invoke other services to perform additional operations,
`sourceIdentity` logging depends on the specific implementation of the invoked
services.

- Amazon SageMaker Training and Processing: When you create a job using the training feature or the processing feature,
  the job creation API calls ingest the `sourceIdentity` that exists in the session. As a result, any AWS
  API calls made from these jobs record the `sourceIdentity` in the CloudTrail logs.
- Amazon SageMaker Pipelines: When you create jobs using automated CI/CD pipelines,
  `sourceIdentity` propagates downstream and can be viewed in the CloudTrail
  logs.
- Amazon EMR: When connecting to Amazon EMR from Studio Classic using [runtime roles](studio-notebooks-emr-cluster-rbac.md "studio-notebooks-emr-cluster-rbac.md"), administrators must
  explicitly [set the
  PropagateSourceIdentity field](../../../emr/latest/ManagementGuide/emr-steps-runtime-roles.md "../../../emr/latest/ManagementGuide/emr-steps-runtime-roles.md"). This ensures that Amazon EMR applies the
  `sourceIdentity` from the calling credentials to a job or query session. The
  `sourceIdentity` is then recorded in CloudTrail logs.

###### Note

The following exceptions apply when using `sourceIdentity`.

- SageMaker Studio Classic shared spaces do not support `sourceIdentity`
  passthrough. AWS API calls made from SageMaker AI shared spaces do not record
  `sourceIdentity` in CloudTrail logs.
- If AWS API calls are made from sessions that are created by users or other
  services and the sessions are not based on the Studio Classic execution role session, then
  the `sourceIdentity` is not recorded in CloudTrail logs.
