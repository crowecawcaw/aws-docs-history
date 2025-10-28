# Best practice 12.3 – Restrict and record resource allocation permissions using AWS Identity and Access Management (IAM)

To better control costs, create distinct IAM roles that authorize users to provision certain resources. This ensures that only permitted individuals can provision the resources they are allowed to, preventing unauthorized and unnecessary spending.

## Suggestion 12.3.1 – Create a cost governance framework that uses specialized IAM

roles, rather than individual users, to provision costly infrastructure

Restrict the authorization to launch costly resources to
specific IAM roles. For example, certain instances types
can only be provisioned by certain teams to reduce
unnecessary expenditure.

## Suggestion 12.3.2 – Track AWS CloudTrail logs to determine overall usage-per-user and role

Track the usage across users and roles to get a clear understanding of resource
usage. As part of your cost-allocation governance, automatically process the AWS CloudTrail logs so
that cost allocation is properly attributed to the relevant department.
