# Managing access with S3 Access Grants

To adhere to the principle of least privilege, you define granular access to your Amazon S3
data based on applications, personas, groups, or organizational units. You can use various
approaches to achieve granular access to your data in Amazon S3, depending on the scale and
complexity of the access patterns.

The simplest approach for managing access to small-to-medium numbers of datasets in Amazon S3 by
AWS Identity and Access Management (IAM) principals is to define [IAM permission policies](user-policies.md "user-policies.md") and
[S3
bucket policies](bucket-policies.md "bucket-policies.md"). This strategy works, so long as the necessary policies fit
within the policy size limits of S3 bucket policies (20 KB) and IAM policies (5 KB), and
within the [number of
IAM principals allowed per account](../../../general/latest/gr/iam-service.md "../../../general/latest/gr/iam-service.md").

As your number of datasets and use cases scales, you might require more policy space. An
approach that offers significantly more space for policy statements is to use [S3
Access Points](access-points.md "access-points.md") as additional endpoints for S3 buckets, because each access point can have
its own policy. You can define quite granular access control patterns, because you can have
thousands of access points per AWS Region per account, with a policy up to 20 KB in size for each access point.
Although S3 Access Points increases the amount of policy space available, it requires a
mechanism for clients to discover the right access point for the right dataset.

A third approach is to implement an [IAM session
broker](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") pattern, in which you implement access-decision logic and dynamically
generate short-term IAM session credentials for each access session. While the IAM
session broker approach supports arbitrarily dynamic permissions patterns and scales
effectively, you must build the access-pattern logic.

Instead of using these approaches, you can use S3 Access Grants to manage access to your Amazon S3 data.
S3 Access Grants provides a simplified model for defining access permissions to data in Amazon S3 by
prefix, bucket, or object. In addition, you can use S3 Access Grants to grant access to both IAM
principals and directly to users or groups from your corporate directory.

You commonly define permissions to data in Amazon S3 by mapping users and groups to datasets.
You can use S3 Access Grants to define direct access mappings of S3 prefixes to users and roles within
Amazon S3 buckets and objects. With the simplified access scheme in S3 Access Grants, you can grant
read-only, write-only, or read-write access on a per-S3-prefix basis to both IAM
principals and directly to users or groups from a corporate directory. With these S3 Access Grants
capabilities, applications can request data from Amazon S3 on behalf of the application's current
authenticated user.

When you integrate S3 Access Grants with the [trusted identity
propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md") feature of AWS IAM Identity Center, your applications can make requests to
AWS services (including S3 Access Grants) directly on behalf of an authenticated corporate directory
user. Your applications no longer need to first map the user to an IAM principal.
Furthermore, because end-user identities are propagated all the way to Amazon S3, auditing which
user accessed which S3 object is simplified. You no longer need to reconstruct the
relationship between different users and IAM sessions. When you're using S3 Access Grants with IAM Identity Center
trusted identity propagation, each [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") data
event for Amazon S3 contains a direct reference to the end user on whose behalf the data was
accessed.

[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") is an AWS IAM Identity Center feature that administrators of connected AWS services can use to grant and audit access to service data. Access to this data is based on user attributes such as group associations. Setting up trusted identity propagation requires collaboration between the administrators of connected AWS services and the IAM Identity Center administrators. For more information, see [Prerequisites and considerations](../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md").

For more information about S3 Access Grants, see the following topics.

###### Topics

- [S3 Access Grants concepts](access-grants-concepts.md "access-grants-concepts.md")
- [S3 Access Grants and corporate directory identities](access-grants-directory-ids.md "access-grants-directory-ids.md")
- [Getting started with S3 Access Grants](access-grants-get-started.md "access-grants-get-started.md")
- [Working with S3 Access Grants instances](access-grants-instance.md "access-grants-instance.md")
- [Working with S3 Access Grants locations](access-grants-location.md "access-grants-location.md")
- [Working with grants in S3 Access Grants](access-grants-grant.md "access-grants-grant.md")
- [Getting S3 data using access grants](access-grants-data.md "access-grants-data.md")
- [S3 Access Grants cross-account access](access-grants-cross-accounts.md "access-grants-cross-accounts.md")
- [Managing tags for S3 Access Grants](access-grants-tagging.md "access-grants-tagging.md")
- [S3 Access Grants limitations](access-grants-limitations.md "access-grants-limitations.md")
- [S3 Access Grants integrations](access-grants-integrations.md "access-grants-integrations.md")
