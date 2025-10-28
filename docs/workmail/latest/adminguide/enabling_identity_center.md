# Enabling IAM Identity Center in Amazon WorkMail

When you enable IAM Identity Center, it acts as an authentication layer for the Amazon WorkMail users. IAM Identity Center
users are managed separately from the Amazon WorkMail directory. It is recommended to use the same
usernames across IAM Identity Center and Amazon WorkMail.

###### Note

Make sure Amazon WorkMail and IAM Identity Center are setup in the same region.

###### To enable IAM Identity Center, follow these steps.

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the console
window, open the **Select a Region** list and
choose a Region. For more information, see [Region and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_Amazon Web Services General Reference_. 2. In the navigation pane, choose **Identity Center**.

The **IAM Identity Center Settings** page appears. 3. Choose **Enable**.

The **Enable IAM Identity Center** window appears. 4. Choose **Enable**.

The **Identity Center Settings** page appears with the
**Identity Center Status** displayed. 5. To add IAM Identity Center users and groups to your Amazon WorkMail Organization, follow the link under
**Identity Center status**. For information on how to add
users and groups, see [Manage identities in IAM Identity Center.](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md").
