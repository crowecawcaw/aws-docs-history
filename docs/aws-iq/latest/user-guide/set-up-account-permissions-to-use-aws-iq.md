End of support notice: On May 28, 2026, AWS
will end support for AWS IQ. After May 28, 2026, you will
no longer be able to access the AWS IQ console or AWS IQ resources.
For more information, see [AWS IQ end of support](../experts-user-guide/aws-iq-end-of-support.md "../experts-user-guide/aws-iq-end-of-support.md") in the _AWS IQ User Guide for Experts_.

# Setting up account permissions to use

AWS IQ

Through AWS IQ, you can post requests, engage with experts, grant experts temporary access
to your AWS account, and pay experts for projects. As a result, AWS IQ requires that you
sign in with an AWS Identity and Access Management (IAM) user that has both the **AWSIQFullAccess** and **IAMFullAccess** managed policies. If you're the administrator of
your account, you should already have those managed policies. If you are an IAM user that
doesn't have these managed policies, you will see an error when you attempt to sign in to the
AWS IQ console that states that you are not authorized to sign in and that you need to add
these managed policies to your IAM
identity.

![AWS IQ - Something went wrong (permissions error)](images/aws-iq-something-went-wrong-AWSIQFullAccess-permission-policy.png)
If necessary, you (or your AWS account administrator) can create an IAM user with the
required managed policies. You can also attach the required managed policies to an existing
IAM user.

## Create an IAM user with managed

policies

You or your AWS account administrator can create an IAM user with the **AWSIQFullAccess** and **IAMFullAccess** managed policies on your AWS account.

###### To create an IAM user with managed policies

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Users**.
3. Choose **Add users**.
4. Enter a **User name**, and then choose **AWS Management
   Console access**.

Accept all the defaults, or change them to a custom value if you prefer.

![AWS IQ - Set user details](images/aws-iq-customers-create-iam-user-details-administrator-access.png) 5. Choose **Next: Permissions**. 6. Choose **Attach existing policies directly**. 7. Choose both **AWSIQFullAccess** and
**IAMFullAccess**, and then choose **Next:
Tags**. 8. _(Optional)_ Add tags, and then choose **Next:
Review**. 9. Choose **Create user**. 10. Choose **Show** to show the password, and then copy the password to a
secure location. Or, choose **Send email** to send the login instructions
to yourself in an email message.

## Attach managed

policies to an existing IAM user

If you already have an IAM user, you can attach the **IAMFullAccess** and **AWSIQFullAccess** managed policies to the user by following this
procedure.

###### To attach managed policies to an existing IAM user

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Users**.
3. Choose the user name to see the summary page for the user.
4. Choose **Add permissions**.
5. Choose **Attach existing policies directly**.
6. Choose both **IAMFullAccess** and
   **AWSIQFullAccess** from the list of policy
   names.

If you don't see them on the first page, you can filter the policies or search for
them using the console. 7. Choose **Next: Review**. 8. Choose **Add permissions**.

For more information, see [Adding and Removing IAM Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User
Guide_.
