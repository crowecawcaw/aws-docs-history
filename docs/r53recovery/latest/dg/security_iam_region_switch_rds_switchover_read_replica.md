

# Amazon RDS Switchover Read Replica execution block sample policy
<a name="security_iam_region_switch_rds_switchover_read_replica"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon RDS Oracle read replica switchover. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:SwitchoverReadReplica",
        "rds:DescribePendingMaintenanceActions",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{region}}:{{account-id}}:db:{{instance-name}}"
      ]
    }
  ]
}
```

If you configure an ungraceful behavior (`promoteReadReplica`), add the following action to the policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:SwitchoverReadReplica",
        "rds:DescribePendingMaintenanceActions",
        "rds:PromoteReadReplica",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{region}}:{{account-id}}:db:{{instance-name}}"
      ]
    }
  ]
}
```