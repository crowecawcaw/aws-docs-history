

# Create an approval team
<a name="create-team"></a>

When you sign in to your organization's management account, you can create approval teams by navigating to the Multi-party approval console.

![Workflow showing approval team creation in AWS Organizations and invitation acceptance in approval portal.](http://docs.aws.amazon.com/mpa/latest/userguide/images/create-team.png)


*Figure 1: Diagram depicting a Multi-party approval administrator creating an approval team.*

## Create an approval team
<a name="create-team-steps"></a>

To create a team, complete the following steps.

 **Minimum permissions** 

To create a team, you need permission to run the following action:
+ `mpa:CreateApprovalTeam`

If you are using the AWS Management Console, you also need permission to run the following actions:
+ `kms:Decrypt`
+ `organizations:DescribeOrganization`
+ `organizations:ListDelegatedAdministrators`
+ `sso:DescribeInstance`
+ `sso:GetSharedSsoConfiguration`
+ `sso:ListInstances`
+ `sso-directory:DescribeUsers`
+ `sso-directory:SearchUsers`

------
#### [ AWS Management Console ]

**To create a team**

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/).

1. On the left navigation, choose **Multi-party approval**.

1. On the **Multi-party approval** console, choose **Create team**.

1. On the **Create approval team** page, enter the following information:
   + **Name:** Name for the team.
   + **Description:** Description for the team.
   + **Approvers**: Choose **Assign approvers** to open a dialog box for selecting IAM Identity Center users to invite to the team. You must have at least three approvers per team.
   + **Minimum required approvals**: Minimum number of approvals needed for a protected operation to be executed. It is recommended to set an approval threshold below the total number of approvers. You must have an approval threshold of at least two.
   + **Tags**: (Optional) Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter teams.

1. After you have finished entering your information, choose **Create team**.

------
#### [ AWS CLI & AWS SDKs ]

**To create a team**  
You can use one of the following operations:
+ AWS CLI: [list-instances](https://docs.aws.amazon.com/cli/latest/reference/sso-admin/list-instances.html), [list-users](https://docs.aws.amazon.com/cli/latest/reference/identitystore/list-users.html), and [create-approval-team](https://docs.aws.amazon.com/cli/latest/reference/mpa/create-approval-team.html)

  1. Run the following command to return a list of Amazon Resource Names (ARNs) for your IAM Identity Center instances:

     ```
     $ C:\> aws sso-admin list-instances
     ```

     This returns the `IdentityStoreId` you need to get user IDs (Step 2).

  1. Run the following command to return a list of user IDs from the IAM Identity Center identity store of your choice:

     ```
     $ C:\> aws identitystore list-users --identity-store-id {{identitystoreId}}
     ```

     This returns the `UserId` you need for `PrimaryIdentityId` (Step 4).

  1. Run the following command to return the Amazon Resource Name (ARN) for your Multi-party approval identity source:

     ```
     $ C:\> aws mpa list-identity-sources
     ```

     This returns the `IdentitySourceArn` you need for `PrimaryIdentitySourceArn` (Step 4).

  1. Run the following command to create a team:

     ```
     $ C:\> aws mpa create-approval-team \
       --name "{{MyTeam}}" \
       --description "{{Description for my team}}" \
       --approval-strategy '{"MofN":{"MinApprovalsRequired":{{approval threshold}}}}' \
       --approvers '[{"PrimaryIdentityId":"{{544894e8-80c1-707f-60e3-3ba6510dfac1}}","PrimaryIdentitySourceArn":"arn:aws:mpa:{{region}}:{{123456789012}}:identity-sources/IamIdentityCenter"}]' \
       --policies '["arn:aws:mpa::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault"]' \
       --tags '{"{{Key1}}":"{{Value1}}","{{Key2}}":"{{Value2}}"}'
     ```
     + **`name`**: Name for the team.
     + **`description`**: Description for the team.
     + **`approval-strategy`**: Contains an `ApprovalStrategy` object. Currently, only `MofNApprovalStrategy` is supported. This object specifies the minimum number of approvals (M) required for a total number of approvers (N). The integer you specify is the approval threshold. It is recommended to set an approval threshold below the total number of approvers. You must have an approval threshold of at least two.
     + **`approvers`**: List of approvers. You must have at least three approvers per team. Each approver requires:
       + **`PrimaryIdentitySourceArn`**: Amazon Resource Name (ARN) for Multi-party approval identity source.
       + **`PrimaryIdentityId`**: User ID from the IAM Identity Center identity store for the approver you want to assign to the team.
     + **`policies`**: List of Amazon Resource Names (ARNs) for Multi-party approval resource policies that define permissions protecting the team. For a list of available policies, use `mpa list-policies`.
     + **`tags`**: (Optional) Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter teams.
+ AWS SDKs: [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html), [ListUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.html), and [CreateApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_CreateApprovalTeam.html)

------

**What to do next**  
After you have created a team, Multi-party approval sends email invitations to the approvers you assigned to the team. The team will become active if every invitation is accepted within 24 hours. If at least one approver declines the team invitation, the team will become inactive. For more information, see [Team health](team-health.md).