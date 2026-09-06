

# Disassociate a web ACL from an Amplify application
<a name="disassociate-web-acl"></a>

You can't delete a web ACL that is associated with an Amplify app. You must first disassociate the web ACL from the app in the Amplify console. Then you can delete it in the AWS WAF console.

**To disassociate a web ACL from an Amplify app**

1. Sign in to the AWS Management Console and open the Amplify console at [https://console.aws.amazon.com/amplify/](https://console.aws.amazon.com/amplify/).

1. On the **All apps** page, choose the name of the app to disassociate a web ACL from.

1. In the navigation pane, choose **Hosting**, and then choose **Firewall**.

1. On the **Firewall** page, choose **Actions**, then choose **Disassociate firewall**.

1. In the confirmation modal, enter **disassociate**, then choose **Disassociate firewall**.

1. On the **Firewall** page, the **Disassociating** status is displayed to indicate that the AWS WAF settings are being propagated.

   When the process is complete, you can delete the web ACL in the AWS WAF console.