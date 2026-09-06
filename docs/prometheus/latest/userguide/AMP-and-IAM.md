

# IAM permissions and policies
<a name="AMP-and-IAM"></a>

Access to Amazon Managed Service for Prometheus actions and data requires credentials. Those credentials must have permissions to perform the actions and to access the AWS resources, such as retrieving Amazon Managed Service for Prometheus data about your cloud resources. The following sections provide details about how you can use AWS Identity and Access Management (IAM) and Amazon Managed Service for Prometheus to help secure your resources, by controlling who can access them. For more information, see [Policies and permissions in IAM.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

## Amazon Managed Service for Prometheus permissions
<a name="AMP-permissions"></a>

To see the list of possible Amazon Managed Service for Prometheus actions. resource types, and condition keys, see [Actions, resources, and condition keys for Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedserviceforprometheus.html).

## Sample IAM policies
<a name="AMP-IAM-policies"></a>

This section provides examples of other self-managed policies that you can create.

The following IAM policy grants full access to Amazon Managed Service for Prometheus and also enables a user to discover Amazon EKS clusters and see the details about them.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aps:*",
                "eks:DescribeCluster",
                "eks:ListClusters"
            ],
            "Resource": "*"
        }
    ]
}
```

------