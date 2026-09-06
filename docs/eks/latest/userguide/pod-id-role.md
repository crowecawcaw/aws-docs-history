

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create IAM role with trust policy required by EKS Pod Identity
<a name="pod-id-role"></a>

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
            "Effect": "Allow",
            "Principal": {
                "Service": "pods.eks.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
            ]
        }
    ]
}
```

 ** `sts:AssumeRole` **   
EKS Pod Identity uses `AssumeRole` to assume the IAM role before passing the temporary credentials to your pods.

 ** `sts:TagSession` **   
EKS Pod Identity uses `TagSession` to include *session tags* in the requests to AWS STS.

 **Setting Conditions**   
You can use these tags in the *condition keys* in the trust policy to restrict which service accounts, namespaces, and clusters can use this role. For the list of request tags that Pod Identity adds, see [Enable or disable session tags](pod-id-abac.md#pod-id-abac-tags).  
For example, you can restrict which pods can assume a Pod Identity IAM Role to a specific `ServiceAccount` and `Namespace` with the following Trust Policy with the added `Condition`:

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
            "Effect": "Allow",
            "Principal": {
                "Service": "pods.eks.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/kubernetes-namespace": [
                        "Namespace"
                    ],
                    "aws:RequestTag/kubernetes-service-account": [
                        "ServiceAccount"
                    ]
                }
            }
        }
    ]
}
```

For a list of Amazon EKS condition keys, see [Conditions defined by Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastickubernetesservice.html#amazonelastickubernetesservice-policy-keys) in the *Service Authorization Reference*. To learn which actions and resources you can use a condition key with, see [Actions defined by Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastickubernetesservice.html#amazonelastickubernetesservice-actions-as-permissions).