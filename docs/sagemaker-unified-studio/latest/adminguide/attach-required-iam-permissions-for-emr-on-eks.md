# Attach required IAM permissions for Amazon EMR on EKS in Amazon SageMaker Unified Studio

Amazon EMR on EKS requires additional IAM permissions when creating Amazon EMR on EKS virtual clusters in Amazon SageMaker Unified Studio.
You must attach the following inline IAM role policy to the IAM role designated as the provisioning role for Amazon SageMaker Unified Studio.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RequiredByEmrContainers",
            "Effect": "Allow",
            "Action": [
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:CreateSecurityGroup",
                "ec2:DeleteSecurityGroup",
                "ec2:DescribeNetworkInterfaces",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:RevokeSecurityGroupIngress",
                "eks:AssociateAccessPolicy",
                "eks:CreateAccessEntry",
                "eks:DisassociateAccessPolicy",
                "eks:DeleteAccessEntry",
                "eks:DescribeAccessEntry",
                "eks:ListAssociatedAccessPolicies"
            ],
            "Resource": "*"
        }
    ]
}
```

In order to identify the IAM role designated as the provisioning role:

1. Navigate to the [Amazon SageMaker Unified Studio management console](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. From the navigation bar, select **Domains**.
   For cross-account Amazon EKS clusters, select **Associated domains**.
3. Select the name of the domain you want to configure Amazon EMR on EKS for.
4. In the domain management view, navigate to **Blueprints**.
5. Search for and select the **EmrOnEks** blueprint.
6. In the blueprint provisioning view, select the IAM role designated as the **Provisioning role**.
