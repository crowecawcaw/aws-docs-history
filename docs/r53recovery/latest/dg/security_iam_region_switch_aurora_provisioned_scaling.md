

# Aurora provisioned scaling execution block sample policy
<a name="security_iam_region_switch_aurora_provisioned_scaling"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Aurora provisioned cluster scaling. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:DescribeDBClusters",
        "rds:DescribeGlobalClusters",
        "rds:CreateDBInstance",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{us-east-1}}:{{111122223333}}:db:{{instance-name}}",
        "arn:aws:rds:{{us-east-1}}:{{111122223333}}:cluster:{{cluster-name}}",
        "arn:aws:rds::{{111122223333}}:global-cluster:{{global-cluster-name}}"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeOrderableDBInstanceOptions",
        "ec2:DescribeInstanceTypes"
      ],
      "Resource": "*"
    }
  ]
}
```