# Manually add the required IAM role to an existing

AWS account and enroll it

If you’ve already set up your AWS Control Tower landing zone, you can begin enrolling your
organization’s accounts into an OU that is registered with AWS Control Tower. If you haven't set
up your landing zone, follow the steps as described in the _AWS Control Tower User Guide_ at [Getting Started, Step 2](getting-started-with-control-tower.md#step-two "getting-started-with-control-tower.md#step-two"). After the landing zone is ready, complete the
following steps to bring existing accounts into governance by AWS Control Tower, manually.

**Be sure to review the [Prerequisites for enrollment](enrollment-prerequisites.md "enrollment-prerequisites.md") noted previously in this
chapter.**

Before enrolling an account with AWS Control Tower, you must give AWS Control Tower permission to manage
that account. To do so, you’ll add a role that has full access to the account, as shown
in the steps that follow. These steps must be performed for each account that you
enroll.

**For each account:**

**Step 1: Sign in with administrator access to the
management account of the organization that currently contains the account you wish
to enroll.**

For example, if you created this account from AWS Organizations and you use a cross-account
IAM role to sign in, then you may follow these steps:

1. Sign in to your organization’s management account.
2. Go to **AWS Organizations**.
3. Under **Accounts**, select the account you want to enroll and
   copy its account ID.
4. Open the account dropdown menu on the top navigation bar and choose
   **Switch Role**.
5. On the **Switch role** form, fill in the following
   fields:
   - Under **Account**, enter the account ID you
     copied.
   - Under **Role**, enter the name of the IAM role that
     enables cross-account access to this account. The name of this role was
     defined when the account was created. If you did not specify a role name
     when you created the account, enter the default role name,
     `OrganizationAccountAccessRole`.

6. Choose **Switch Role**.
7. You should now be signed into the AWS Management Console as the child account.
8. When you’re finished, stay in the child account for the next part of the
   procedure.
9. Make note of the management account ID, because you will need to enter it in
   the next step.
   **Step 2: Give AWS Control Tower permission to manage the
   account.**

10. Go to **IAM**.
11. Go to **Roles**.
12. Choose **Create role**.
13. When asked to select which service the role is for, choose **Custom
    trust policy**.
14. Copy the code example shown here and paste it into the Policy Document.
    Replace the string `Management Account ID`
    with the actual management account ID of your management account. Here is the
    policy to paste:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "sts:AssumeRole",
 "Condition": {}
 }
 ]
}`

```

6. When asked to attach policies, choose
   **AdministratorAccess**.
7. Choose **Next:Tags**.
8. You may see an optional screen titled **Add tags**. Skip this
   screen for now by choosing **Next:Review**
9. On the **Review** screen, in the **Role
   name** field, enter `AWSControlTowerExecution`.
10. Enter a brief description in the **Description** box, such as
    _Allows full account access for
    enrollment._
11. Choose **Create role**.
    **Step 3: Enroll the account by moving it into a registered OU,
    and verify enrollment.**

After you’ve set up the necessary permissions by creating the role, follow these steps
to enroll the account and verify enrollment.

1.  **Sign in again as Admin and go to
    AWS Control Tower.**
2.  ###### Enroll the account.
    - From the **Organization** page in AWS Control Tower, select
      your account, then choose **Enroll** from the
      **Actions** dropdown menu at the upper
      right.
    - Follow the steps for enrolling an individual account, as shown on the
      [Steps to enroll an account manually](quick-account-provisioning.md#enrollment-steps "quick-account-provisioning.md#enrollment-steps")
      page.

3.  ###### Verify enrollment.

        * From AWS Control Tower, choose **Organization** in the left
         navigation.
        * Look for the account you have recently enrolled. Its initial state
         will show a status of **Enrolling**.
        * When the state changes to **Enrolled**, the move was
         successful.

    To continue this process, sign into each account in your organization that you want to
    enroll in AWS Control Tower. Repeat the prerequisite steps and the enrollment steps for each
    account.
