# Example policies: Using condition keys

Following are examples of how you can use condition keys in Amazon Aurora IAM permissions policies.

## Example 1: Grant permission to create a DB instance that uses a

specific DB engine and isn't MultiAZ

The following policy uses an RDS condition key and allows a user to
create only DB instances that use the MySQL database engine and don't use
MultiAZ. The `Condition` element indicates the requirement that the
database engine is MySQL.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowMySQLCreate",
 "Effect": "Allow",
 "Action": "rds:CreateDBInstance",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "rds:DatabaseEngine": "mysql"
 },
 "Bool": {
 "rds:MultiAz": false
 }
 }
 }
 ]
}`

```

## Example 2: Explicitly deny permission to create DB instances for certain DB instance classes and create DB instances

that use Provisioned IOPS

The following policy explicitly denies permission to create DB instances that use the DB
instance classes `r3.8xlarge` and `m4.10xlarge`, which are the largest and most expensive
DB instance classes. This policy also prevents users from creating DB instances that use
Provisioned IOPS, which incurs an additional cost.

Explicitly denying permission supersedes any other permissions granted.
This ensures that identities to not accidentally get permission that you
never want to grant.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyLargeCreate",
 "Effect": "Deny",
 "Action": "rds:CreateDBInstance",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "rds:DatabaseClass": [
 "db.r3.8xlarge",
 "db.m4.10xlarge"
 ]
 }
 }
 },
 {
 "Sid": "DenyPIOPSCreate",
 "Effect": "Deny",
 "Action": "rds:CreateDBInstance",
 "Resource": "*",
 "Condition": {
 "NumericNotEquals": {
 "rds:Piops": "0"
 }
 }
 }
 ]
}`

```

## Example 3: Limit the set of tag keys and values that can be used to tag a resource

The following policy uses an RDS condition key and allows the addition of a tag with the key `stage` to be added
to a resource with the values `test`, `qa`, and `production`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowTagEdits",
 "Effect": "Allow",
 "Action": [
 "rds:AddTagsToResource",
 "rds:RemoveTagsFromResource"
 ],
 "Resource": "arn:aws:rds:us-east-1:123456789012:db:db-123456",
 "Condition": {
 "StringEquals": {
 "rds:req-tag/stage": [
 "test",
 "qa",
 "production"
 ]
 }
 }
 }
 ]
}`

```
