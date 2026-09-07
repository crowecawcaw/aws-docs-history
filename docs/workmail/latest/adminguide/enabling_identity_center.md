

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Enabling IAM Identity Center in Amazon WorkMail
<a name="enabling_identity_center"></a>

When you enable IAM Identity Center, it acts as an authentication layer for the Amazon WorkMail users. IAM Identity Center users are managed separately from the Amazon WorkMail directory. It is recommended to use the same usernames across IAM Identity Center and Amazon WorkMail.

**Note**  
Make sure Amazon WorkMail and IAM Identity Center are setup in the same region.

**To enable IAM Identity Center, follow these steps.**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Region and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Identity Center**.

   The **IAM Identity Center Settings** page appears.

1. Choose **Enable**.

   The **Enable IAM Identity Center** window appears.

1. Choose **Enable**.

   The **Identity Center Settings** page appears with the **Identity Center Status** displayed.

1. To add IAM Identity Center users and groups to your Amazon WorkMail Organization, follow the link under **Identity Center status**. For information on how to add users and groups, see [Manage identities in IAM Identity Center.](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html).