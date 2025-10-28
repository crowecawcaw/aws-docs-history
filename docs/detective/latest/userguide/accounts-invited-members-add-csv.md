# Inviting a list of member accounts to a

behavior graph

From the Detective console, you can provide a `.csv` file containing a
list of member accounts to invite to your behavior graph.

The first line in the file is the header row. Each account is then listed on a separate
line. Each member account entry contains the AWS account ID and the account's root user email
address.

Example:

```
Account ID,Email address
111122223333,srodriguez@example.com
444455556666,rroe@example.com
```

When Detective processes the file, it ignores accounts that were already invited, unless the
account status is **Verification failed**. That status indicates that the
email address provided for the account did not match the account's root user email address. In
that case, Detective deletes the original invitation and tries again to verify the email address
and send the invitation.

This option also provides a template that you can use to create the list of
accounts.

###### To invite member accounts from a .csv list (console)

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, choose **Account management**.
3. Choose **Actions**. Then choose **Invite
   accounts**.
4. Under **Add accounts**, choose **Add from
   .csv**.
5. To download a template file to work from, choose **Download .csv
   template**.
6. To select the file containing the list of accounts, choose **Choose .csv
   file**.
7. Under **Review member accounts**, verify the list of member
   accounts that Detective found in the file.
8. Under **Personalize invitation email**, add customized content to
   include in the invitation email.

For example, you can provide contact information, or remind the member account about
the required IAM policy. 9. **Member account IAM policy** contains the text of the required
IAM policy for member accounts. The email invitation includes this policy text. To
copy the policy text, choose **Copy**. 10. Choose **Invite**.

## Adding a list of member accounts across

Regions

Detective provides an open-source Python script in GitHub that allows you to do the
following:

- Add a specified list of member accounts to an administrator account's behavior
  graphs across a specified list of Regions.
- If the administrator account does not have a behavior graph in a Region, then the
  script also enables Detective and creates the behavior graph in that Region.
- Send invitation emails to the member accounts.
- Automatically accept the invitations for the member accounts.

For information on how to configure and use the GitHub scripts, see [Using Detective Python scripts to manage accounts](detective-github-scripts.md "detective-github-scripts.md").
