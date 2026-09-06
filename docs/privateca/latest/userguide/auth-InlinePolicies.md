

# Inline policies
<a name="auth-InlinePolicies"></a>

Inline policies are policies that you create and manage and embed directly into a user, group, or role. The following policy examples show how to assign permissions to perform AWS Private CA actions. For general information about inline policies, see [Working with Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#inline-policies) in the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/). You can use the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the IAM API to create and embed inline policies. 

**Important**  
We strongly recommend the use of multi-factor authentication (MFA) any time you access AWS Private CA.

**Topics**
+ [Listing private CAs](#policy-list-pcas)
+ [Retrieving a private CA certificate](#policy-retrieve-pca)
+ [Importing a private CA certificate](#policy-import-pca-cert)
+ [Deleting a private CA](#policy-delete-pca)
+ [Tag-on-create: Attaching tags to a CA at the time of creation](#tag-on-create)
+ [Tag-on-create: Restricted tagging](#tag-on-create-restricted1)
+ [Controlling access to Private CA using tags](#tag-on-create-restricted2)
+ [Read-only access to AWS Private CA](#policy-pca-read-only)
+ [Full access to AWS Private CA](#policy-pca-full-access)

## Listing private CAs
<a name="policy-list-pcas"></a>

 The following policy allows a user to list all of the private CAs in an account. 

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":"acm-pca:ListCertificateAuthorities",
         "Resource":"*"
      }
   ]
}
```

------

## Retrieving a private CA certificate
<a name="policy-retrieve-pca"></a>

 The following policy allows a user to retrieve a specific private CA certificate. 

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":{
      "Effect":"Allow",
      "Action":"acm-pca:GetCertificateAuthorityCertificate",
      "Resource":"arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{CA_ID}}/certificate/{{certificate_ID}}"
   }
}
```

------

## Importing a private CA certificate
<a name="policy-import-pca-cert"></a>

The following policy allows a user to import a private CA certificate. 

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":{
      "Effect":"Allow",
      "Action":"acm-pca:ImportCertificateAuthorityCertificate",
      "Resource":"arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{CA_ID}}/certificate/{{certificate_ID}}"
   }
}
```

------

## Deleting a private CA
<a name="policy-delete-pca"></a>

The following policy allows a user to delete a specific private CA.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":{
      "Effect":"Allow",
      "Action":"acm-pca:DeleteCertificateAuthority",
      "Resource":"arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{CA_ID}}/certificate/{{certificate_ID}}"   }
}
```

------

## Tag-on-create: Attaching tags to a CA at the time of creation
<a name="tag-on-create"></a>

The following policy allows a user to apply tags during CA creation.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
      {
         "Action": [
            "acm-pca:CreateCertificateAuthority",
            "acm-pca:TagCertificateAuthority"
         ],
         "Effect": "Allow",
         "Resource": "*"
      }
   ]  
}
```

------

## Tag-on-create: Restricted tagging
<a name="tag-on-create-restricted1"></a>

The following tag-on-create policy *prevents* use of the key-value pair Environment=Prod during CA creation. Tagging with other key-value pairs is allowed. 

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":"acm-pca:*",
         "Resource":"*"
      },
      {
         "Effect":"Deny",
         "Action":"acm-pca:TagCertificateAuthority",
         "Resource":"*",
         "Condition":{
            "StringEquals":{
               "aws:ResourceTag/Environment":[
                  "Prod"
               ]
            }
         }
      }
   ]
}
```

------

## Controlling access to Private CA using tags
<a name="tag-on-create-restricted2"></a>

The following policy allows access only to CAs with the key-value pair Environment=PreProd. It also requires that new CAs include this tag. 

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "acm-pca:*"
         ],
         "Resource":"*",
         "Condition":{
            "StringEquals":{
               "aws:ResourceTag/Environment":[
                  "PreProd"
               ]
            }
         }
      }
   ]
}
```

------

## Read-only access to AWS Private CA
<a name="policy-pca-read-only"></a>

 The following policy allows a user to describe and list private certificate authorities and to retrieve the private CA certificate and certificate chain. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":{
       "Effect":"Allow",
       "Action":[
          "acm-pca:DescribeCertificateAuthority",
          "acm-pca:DescribeCertificateAuthorityAuditReport",
          "acm-pca:ListCertificateAuthorities",
          "acm-pca:ListTags",
          "acm-pca:GetCertificateAuthorityCertificate",
          "acm-pca:GetCertificateAuthorityCsr",
          "acm-pca:GetCertificate"
       ],
       "Resource":"*"
    }
}
```

------

## Full access to AWS Private CA
<a name="policy-pca-full-access"></a>

 The following policy allows a user to perform any AWS Private CA action. 

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "acm-pca:*"
         ],
         "Resource":"*"
      }
   ]
}
```

------