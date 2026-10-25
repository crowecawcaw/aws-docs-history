

# Get started
<a name="getting-started"></a>

Before you begin, you should familiarize yourself with the basic concepts in AWS Ground Station. For more information, see [How AWS Ground Station works](how-it-works.md).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Add AWS Ground Station permissions to your AWS account
<a name="add-permissions-to-account"></a>

 To use AWS Ground Station without requiring an administrative user, you need to create a new policy and attach it to your AWS account.

1.  Sign in to the AWS Management Console and open the [IAM console](https://console.aws.amazon.com/iam). 

1.  Create a new policy. Use the following steps: 

   1.  In the navigation pane, choose **Policies** and then choose **Create Policy**. 

   1.  In the **JSON** tab, edit the JSON with one of the following values. Use the JSON that works best for your application. 
      +  For Ground Station administrative privileges, set **Action** to **groundstation:\*** as follows: 

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
                "groundstation:*"
              ],
              "Resource": [
                "*"
              ]
            }
          ]
        }
        ```

------
      +  For Read-only privileges, set **Action** to **groundstation:Get\***, **groundstation:List\***, and **groundstation:Describe\*** as follows: 

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
                "groundstation:Get*",
                "groundstation:List*",
                "groundstation:Describe*"
              ],
              "Resource": [
                "*"
              ]
            }
          ]
        }
        ```

------
      +  For additional security through multifactor authentication, set **Action** to **groundstation:\***, and **Condition/Bool** to **aws:MultiFactorAuthPresent:true** as follows: 

------
#### [ JSON ]

****  

        ```
        {
            "Version":"2012-10-17",		 	 	 
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "groundstation:*",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "aws:MultiFactorAuthPresent": true
                        }
                    }
                }
            ]
        }
        ```

------

1.  In the IAM console, attach the policy you created to the desired user. 

 For more information about IAM users and attaching policies, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html). 