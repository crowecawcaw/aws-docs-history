

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Setting up an Amazon FinSpace environment
<a name="setting-up-for-amazon-finspace"></a>

**Important**  
Amazon FinSpace Dataset Browser will be discontinued on {{March 26, 2025}}. Starting {{November 29, 2023}}, FinSpace will no longer accept the creation of new Dataset Browser environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/) will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/) or contact [AWS Support](https://aws.amazon.com/contact-us/) to assist with your transition.

An Amazon FinSpace environment is created from an AWS account. In this section, you sign up for an AWS account, create an administrator access, and create a FinSpace environment.

** **Topics** **
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [(Optional) Attach managed policies for creating FinSpace environment](#optional-attach-managed-policies-for-creating-finspace-environment)
+ [Create an Amazon FinSpace environment](create-an-amazon-finspace-environment.md)
+ [Sample data bundles](sample-data-bundle.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## (Optional) Attach managed policies for creating FinSpace environment
<a name="optional-attach-managed-policies-for-creating-finspace-environment"></a>

To create a FinSpace environment, the user performing the actions must have IAM permissions for `AdministratorAccess` or must have the FinSpace managed policy attached to their role. This step is optional if the user has `AdministratorAccess` permissions. Create and attach FinSpace managed policies to the account you used to create the FinSpace environment. These policies grant permissions to create the FinSpace environment and superusers in an AWS account.

1. Create a managed policy on the JSON tab for FinSpace. For more information, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-json-editor).

1. Use the following managed policy:

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
                "finspace:*"
            ],
            "Resource": "*"
        }
    ]
}
```

------