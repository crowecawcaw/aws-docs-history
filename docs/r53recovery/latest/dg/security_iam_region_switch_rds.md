

# Amazon RDS execution block sample policy
<a name="security_iam_region_switch_rds"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon RDS read replica promotion or cross-Region replica creation. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:PromoteReadReplica",
        "rds:CreateDBInstanceReadReplica",
        "rds:ModifyDBInstance"
      ],
      "Resource": "*"
    }
  ]
}
```