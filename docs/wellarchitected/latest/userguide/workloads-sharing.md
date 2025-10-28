# Share a workload in AWS Well-Architected Tool

You can share a workload that you own with other AWS accounts, users, an organization, and organization units (OUs) in the
same AWS Region.

###### Note

You can only share workloads within the same AWS Region.

When sharing a workload with another AWS account, if the recipient does not have
the `wellarchitected:UpdateShareInvitation` permission, they cannot
accept the share invitation. See [Providing users, groups, or roles access to AWS WA Tool](iam-auth-access.md "iam-auth-access.md") for permission
policy examples.

###### To share a workload with other AWS accounts and users

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/ "https://console.aws.amazon.com/wellarchitected/").
2. In the left navigation pane, choose **Workloads**.
3. Select a workload that you own in one of the following ways:
   - Choose the name of the workload.
   - Select the workload and choose **View
     details**.

4. Choose **Shares**. Then choose
   **Create** and **Create shares to users or accounts** to
   create a workload invitation.
5. Enter the 12-digit AWS account ID or the ARN of the user that you want to
   share the workload with.
6. Choose the permission that you want to grant.

**Read-Only**

Provides read-only access to the workload.

**Contributor**

Provides update access to answers and their notes, and read-only
access to the rest of the workload. 7. Choose **Create** to send a workload invitation to the
specified AWS account or user.
If the workload invitation is not accepted within seven days, the invitation is
automatically expired.

If a user and the user's AWS account both have workload invitations, the workload
invitation with the highest level permission is applied to the user.

###### Important

Before sharing a workload with an organization or organization units (OUs),
you must [enable AWS Organizations
access](sharing.md#getting-started-sharing-orgs "sharing.md#getting-started-sharing-orgs").

###### To share a workload with your organization or OUs

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/ "https://console.aws.amazon.com/wellarchitected/").
2. In the left navigation pane, choose **Workloads**.
3. Select a workload that you own in one of the following ways:
   - Choose the name of the workload.
   - Select the workload and choose **View
     details**.

4. Choose **Shares**. Then choose
   **Create** and **Create shares to Organizations**.
5. On the **Create workload share** page, choose whether to grant permissions
   to the entire organization, or to one or more OUs.
6. Choose the permission that you want to grant.

**Read-Only**

Provides read-only access to the workload.

**Contributor**

Provides update access to answers and their notes, and read-only
access to the rest of the workload. 7. Choose **Create** to share the workload.
To see who has shared access to a workload, choose **Shares** from
the [View workload details in AWS Well-Architected Tool](workload-details.md "workload-details.md") page.

To prevent an entity from sharing workloads, attach a policy that denies
`wellarchitected:CreateWorkloadShare` actions.

You can also share custom lenses that you own with other AWS accounts, users,
your organization, and OUs
in the same AWS Region. For details, refer to [Sharing a custom lens in AWS WA Tool](lenses-sharing.md "lenses-sharing.md").
