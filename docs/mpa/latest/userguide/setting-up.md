

# Set up Multi-party approval
<a name="setting-up"></a>

When you sign in to your organization's management account, you can set up Multi-party approval by navigating to the Multi-party approval console and creating a Multi-party approval identity source.

An *identity source* is a Multi-party approval resource that models the connection between Multi-party approval and the AWS IAM Identity Center instance that manages the user authentication for approvers.

![AWS Organizations management account connecting IAM Identity Center and creating approval portal.](http://docs.aws.amazon.com/mpa/latest/userguide/images/setting-up.png)


*Figure 1: Diagram depicting a Multi-party approval administrator setting up Multi-party approval.*

## Create a Multi-party approval identity source
<a name="setting-up-steps"></a>

To create an identity source, complete the following steps.

 **Minimum permissions** 

To create a Multi-party approval identity source, you need permission to run the following actions:
+ `kms:Decrypt`
+ `mpa:CreateIdentitySource`
+ `sso:CreateApplication`
+ `sso:DeleteApplication`
+ `sso:DescribeApplication`
+ `sso:DescribeInstance`
+ `sso:ListInstances`
+ `sso:PutApplicationAccessScope`
+ `sso:PutApplicationAssignmentConfiguration`
+ `sso:PutApplicationAuthenticationMethod`
+ `sso:PutApplicationGrant`

If you are using the AWS Management Console, you also need permission to run the following actions:
+ `kms:Decrypt`
+ `organizations:DescribeOrganization`
+ `organizations:ListDelegatedAdministrators`
+ `sso:DescribeInstance`
+ `sso:DescribeRegisteredRegions`
+ `sso:GetSharedSsoConfiguration`
+ `sso:ListInstances`

------
#### [ AWS Management Console ]

**To create a Multi-party approval identity source**

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/).

1. On the left navigation, choose **Multi-party approval**.

1. On the **Multi-party approval** console, choose **Set up Multi-party approval**.

1. On the **Set up Multi-party approval** page, wait for the Multi-party approval to search for your IAM Identity Center instance. If you don't have an IAM Identity Center instance, you will be prompted to create one.

1. After Multi-party approval has found your IAM Identity Center instance, choose **Complete setup**.

------
#### [ AWS CLI & AWS SDKs ]

**To create a Multi-party approval identity source**  
You can use one of the following operations:
+ AWS CLI: [list-instances](https://docs.aws.amazon.com/cli/latest/reference/sso-admin/list-instances.html) and [create-identity-source](https://docs.aws.amazon.com/cli/latest/reference/mpa/create-identity-source.html)

  1. Run the following command to return a list of Amazon Resource Names (ARNs) for your IAM Identity Center instances:

     ```
     $ C:\> aws sso-admin list-instances
     ```

  1. Run the following command to create a Multi-party approval identity source with the available IAM Identity Center of your choice:

     ```
     $ C:\> aws mpa create-identity-source \
       --identity-source-parameters '{
         "IamIdentityCenter": {
           "InstanceArn": "arn:aws:sso:::instance/ssoins-{{111122223333}}",
           "Region": "{{region}}"
         }
       }'
     ```
     + **`InstanceArn`**: Amazon Resource Name (ARN) for the IAM Identity Center instance you want to connect with Multi-party approval.
     + **`Region`**: AWS Region where the IAM Identity Center instance is located. 
+ AWS SDKs: [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html) and [CreateIdentitySource](https://docs.aws.amazon.com/mpa/latest/APIReference/API_CreateIdentitySource.html)

------

**What to do next**  
After you set up Multi-party approval, you can create approval teams in the Multi-party approval console or using the AWS CLI & AWS SDKs. For more information, see [Create team](create-team.md).

## Considerations
<a name="setting-up-considerations"></a>

**AWS Organizations is required**

Multi-party approval is a capability of AWS Organizations. You access the Multi-party approval console through the Organizations console.

To set up Organizations, see [Getting started with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html) in the *Organizations User Guide*.

**Organization instance of IAM Identity Center is required**

Multi-party approval requires access to your identities in AWS IAM Identity Center. To enable an organization instance, see [Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html) in the *IAM Identity Center User Guide*.

For your organization instance, we strongly recommend using an [external identity provider](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html). This setup separates IAM Identity Center administrative privileges from identity management, which helps prevent the admin from being able to bypass Multi-party approval mechanisms by changing approver passwords and assuming their identities.

**Cross-Region setup for the IAM Identity Center instance**

When you enable Multi-party approval and your IAM Identity Center instance in different Regions, Multi-party approval makes calls across Regions to IAM Identity Center. This means that [user and group](https://docs.aws.amazon.com/singlesignon/latest/userguide/users-groups-provisioning.html) information moves across Regions.

If the Region where the IAM Identity Center instance is located experiences issues, approvers might temporarily be unable to access the Multi-party approval portal, and delivery of notifications about new approvals might be delayed.

**One identity source for Multi-party approval**

Creating an Multi-party approval identity source is a one-time operation, and you can only have one identity source for Multi-party approval.