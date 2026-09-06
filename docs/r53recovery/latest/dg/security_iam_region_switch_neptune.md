

# Amazon Neptune Global Cluster execution block sample policy
<a name="security_iam_region_switch_neptune"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon Neptune global clusters. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "neptune:DescribeGlobalClusters",
        "neptune:DescribeDBClusters",
        "neptune:FailoverGlobalCluster",
        "neptune:SwitchoverGlobalCluster"
      ],
      "Resource": "*"
    }
  ]
}
```