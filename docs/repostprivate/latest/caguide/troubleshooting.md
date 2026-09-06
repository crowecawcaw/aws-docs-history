

End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html). 

# Troubleshooting re:Post Private
<a name="troubleshooting"></a>

The following information can help you troubleshoot issues with AWS re:Post Private.

**Topics**
+ [Can't set up my private re:Post in a specific AWS Region](#region-setup-issue)
+ [Can't set up private re:Post in my account](#account-setup-issue)
+ [Can't manage users or groups in a private re:Post](#manage-console-issue)

## Can't set up my private re:Post in a specific AWS Region
<a name="region-setup-issue"></a>

re:Post Private is available only in US East (N. Virginia), US West (Oregon), Europe (Frankfurt), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), and Europe (Ireland) Regions. Make sure that you're creating your private re:Post in one of these Regions.

## Can't set up private re:Post in my account
<a name="account-setup-issue"></a>

Make sure that you enabled AWS IAM Identity Center for your account and set up IAM Identity Center in the same Region where you want to create the private re:Post. For more information, see [Prerequisites](what-is.md#prerequisites).

## Can't manage users or groups in a private re:Post
<a name="manage-console-issue"></a>

Be sure that you have the required permissions to edit a private re:Post and manage users and groups within the private re:Post. For more information, see [AWS re:Post Private identity-based policy examples](security-iam-policy-examples.md).