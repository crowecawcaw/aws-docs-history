# HealthOmics Resource permissions

AWS HealthOmics creates and accesses resources in other services on your behalf when you run a job
or create a store. In some cases, you need to configure permissions in other services to access
resources or to allow HealthOmics to access them.

For resource permissions related to Amazon ECR, see [Amazon ECR permissions](permissions-ecr.md "permissions-ecr.md").

## Lake Formation permissions

Before you use analytics features in HealthOmics, configure default database settings in
Lake Formation.

###### To configure resource permissions in Lake Formation

1. Open the [Data catalog
   settings](https://console.aws.amazon.com/lakeformation/home#default-permission-settings "https://console.aws.amazon.com/lakeformation/home#default-permission-settings") page in the Lake Formation console.
2. Uncheck the IAM access control requirements for databases and tables under
   **Default permissions for newly created databases and tables**.
3. Choose **Save**.

HealthOmics Analytics auto accepts data if your service policy has the correct RAM permissions, such as the following
example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "omics:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ram:AcceptResourceShareInvitation",
 "ram:GetResourceShareInvitations"
 ],
 "Resource": "*"
 }
 ]
}`

```
