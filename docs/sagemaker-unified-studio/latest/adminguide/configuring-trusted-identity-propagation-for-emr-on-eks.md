

# Configuring trusted identity propagation for Amazon EMR on EKS
<a name="configuring-trusted-identity-propagation-for-emr-on-eks"></a>

 Amazon EMR on EKS requires additional IAM permissions to enable trusted identity propagation. You must attach the following inline IAM role policy to the IAM role created as the Amazon EMR on EKS system namespace role. 

**Note**  
 The Amazon EMR on EKS system namespace role for an Amazon SageMaker Unified Studio project is named `datazone_emr_containers_system_namespace_role_{{{project_id}}}`. 

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "TrustedIdentityPropagation",
            "Effect": "Allow",
            "Action": [
                "sso-oauth:CreateTokenWithIAM",
                "sso-oauth:IntrospectTokenWithIAM",
                "sso-oauth:RevokeTokenWithIAM"
            ],
            "Resource": "*"
        }
    ]
}
```