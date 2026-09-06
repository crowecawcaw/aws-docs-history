

# Prerequisites for using Aurora PostgreSQL Limitless Database
<a name="limitless-prereqs"></a>

To use Aurora PostgreSQL Limitless Database, you must first perform the following tasks.

**Topics**
+ [Enabling DB shard group operations](#limitless-enable-iam)

## Enabling DB shard group operations
<a name="limitless-enable-iam"></a>

Before you can create a DB shard group, you must enable DB shard group operations.
+ Add the following section to the IAM policy of the IAM role of the user that accesses Aurora PostgreSQL Limitless Database:

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "AllowDBShardGroup",
              "Effect": "Allow",
              "Action": [
                  "rds:CreateDBShardGroup",
                  "rds:DescribeDBShardGroups",
                  "rds:DeleteDBShardGroup",
                  "rds:ModifyDBShardGroup",
                  "rds:RebootDBShardGroup"
              ],
              "Resource": [
                  "arn:aws:rds:*:*:shard-group:*",
                  "arn:aws:rds:*:*:cluster:*"
              ]
          }
      ]
  }
  ```

------