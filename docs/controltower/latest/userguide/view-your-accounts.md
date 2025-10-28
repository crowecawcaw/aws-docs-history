# View your accounts

The **Organization** page lists all OUs and accounts in your
organization, regardless of OU or enrollment status in AWS Control Tower. You can view and enroll
member accounts into AWS Control Tower—individually or by OU groups—if each account
meets the prerequisites for enrollment.

###### To view a specific account

- Navigate to the **Organization** page.
- You can choose **Accounts only** from the dropdown menu at
  the upper right.
- Then, select the name of your account from the table.
- Alternatively, you can select the name of the parent OU from the table, and
  view a list of all accounts within that OU on the **Details**
  page for that OU.
  On the **Organization** page and the **Account
  details** page, you can see the account's **State**, which
  is one of these:

- **Not enrolled** – The account is a member of the
  parent OU, but it is not fully managed by AWS Control Tower. If the parent OU is
  registered, the account is governed by the preventive controls configured for
  its registered parent OU, but the OU’s detective controls do not apply to this
  account. If the parent OU is unregistered, no controls apply to this account.
- **Enrolling** – The account is being brought into
  governance by AWS Control Tower. We are aligning the account with the control
  configuration for the parent OU. This process may require several minutes per
  account resource.
- **Enrolled** – The account is governed by the controls
  configured for its parent OU. It is fully managed by AWS Control Tower.
- **Enrollment failed** – The account could not be
  enrolled in AWS Control Tower. For more information, see [Common causes for failure of
  enrollment](quick-account-provisioning.md#common-causes-for-enrollment-failure "quick-account-provisioning.md#common-causes-for-enrollment-failure").
- **Update available** – The account has an update
  available. Accounts in this state are still **Enrolled**, but
  the account must be updated to reflect recent changes made to your environment.
  To update a single account, navigate to the account detail page and select
  **Update account**.

If you have multiple accounts with this state under a single OU, you can
choose to **Re-register** the OU and update those accounts
together.
