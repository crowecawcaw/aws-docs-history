# Add members to a project

In Amazon DataZone, projects enable a group of users to collaborate on various business use
cases that involve publishing, discovering, subscribing to, and consuming data assets in
the Amazon DataZone catalog. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

You must be a project owner or contributor to add members to a project. You can add
SSO groups, SSO users, or IAM principals (roles or users) as project members.

To add members to an exiting project, complete the following steps.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project.
3. Choose the project to which you want to add memebrs. If you don't readily see
   it in the list of projects, you can search for it by specifying the project name
   in the **Find project** field.
4. On the project's details page, select the **Members** tab and
   the choose **All members** node.
5. In the project Members tab, choose **Add members**.
6. In the **Add members to project** pop up window, specify the
   user(s) that you want to add and specify their role within the project (owner,
   contributor, consumer, steward, or viewer) and then choose **Add
   members**.

###### Important

You can only add those users as project members who are authorized to be members
of this project by the project membership authorization policy that is configured
for the domain unit in which this project lives. For more information, see [Assign
authorization policies to users and groups within an Amazon DataZone domain unit](assign-authorization-policies-to-users-in-domain-unit.md "assign-authorization-policies-to-users-in-domain-unit.md") .

###### Note

You can add an IAM principal as a project member if that principal already has a
Amazon DataZone user profile in the domain. Amazon DataZone automatically creates a user
profile for an IAM principal when it successfully interacts with the domain via the
portal, API, or CLI. You cannot create a user profile for an IAM principal. To add
IAM principals as project members in the case where the IAM principal does not have
an existing Amazon DataZone user profile in the domain, ask your administrator to add the
following two IAM permissions to your domain’s
**AmazonDataZoneDomainExecutionRole** in the IAM console:
`iam:GetUser` and `iam:GetRole`. Separately, to perform
actions in the domain, the IAM principal must have the corresponding IAM permissions
to such actions.
