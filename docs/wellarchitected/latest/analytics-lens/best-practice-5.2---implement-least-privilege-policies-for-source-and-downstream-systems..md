# Best practice 5.2 – Implement least privilege policies for source and downstream systems

The principle of least privilege works by giving only enough
access for systems to do the job. Set an expiry on temporary
permissions to ensure that re-authentication occurs
periodically. The system actions on the data should
determine the permission and granting permissions to other
systems should not be permitted.

## Suggestion 5.2.1 – Ensure that permissions are least for the action performed by user/system

Identify the minimum privileges that each user or system
requires, and only allow the permissions that they need.
For example, if a downstream system requests to read an
Amazon Redshift table from an analytics workload, only
give the read permission for the table using Amazon Redshift user privilege controls.

For more details, refer to the following information:

- AWS Security Blog:
  [Techniques
  for writing least privilege IAM policies](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/ "https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/")
- Amazon Redshift Database Developer Guide:
  [Managing
  database security](../../../redshift/latest/dg/r_Database_objects.md "../../../redshift/latest/dg/r_Database_objects.md")
- AWS Security Blog:
  [IAM
  Access Analyzer makes it easier to implement least
  privilege permissions by](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/ "https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/")
  [generating
  IAM policies based on access activity](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/ "https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/")

## Suggestion 5.2.2 – Implement the two-person rule to prevent accidental or malicious actions

Even if you have implemented the least privilege policies,
someone must have critical permissions for the business,
such as the ability to delete datasets from analytics
workloads.

The two-person rule is a safety mechanism that requires
the presence of two authorized personnel to perform tasks
that are considered important. It has its origins in
military protocol, but the IT security space has also
widely adopted the practice.

By implementing the two-person rule, you can have
additional prevention of accidental or malicious actions
of the people who have critical permissions.
