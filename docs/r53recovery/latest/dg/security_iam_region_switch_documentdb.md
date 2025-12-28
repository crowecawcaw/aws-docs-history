# Amazon DocumentDB Global Cluster execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon DocumentDB global clusters.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeGlobalClusters",
        "rds:DescribeDBClusters",
        "rds:FailoverGlobalCluster",
        "rds:SwitchoverGlobalCluster"
      ],
      "Resource": "*"
    }
  ]
}
```
