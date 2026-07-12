This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Consent pop-up for AWS Wickr

You can configure consent pop-up for your network to display terms, policies, or
organizational requirements to users when they log in to Wickr. Users must acknowledge
the pop-up before they can access the application. The pop-up is displayed again when
users log out and log back in, or when the pop-up content is updated.

To enable the consent pop-up, complete the following procedure.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to navigate
   to that network.
3. In the navigation pane, choose **Network policies**.
4. On the **Network policies** page, in the **Consent
   popup** section, choose **Edit**.
5. On the **Edit consent popup** page, in the **Consent
   popup** section, toggle on **Enabled**.
6. Complete the following fields:

   - **Header** – Enter the title displayed at the
     top of the consent pop-up. Use the header to provide a summary of the
     information or action being presented to the users.
   - **Body content** – Enter the main message
     displayed in the consent pop-up. Use the body content to communicate
     terms, policies, organizational requirements, or other information that
     users must review before accessing the application.
   - **Close button label (Optional)** – Enter the
     text displayed on the button that users select to acknowledge and
     dismiss the consent pop-up. For example, you can use
     **Acknowledge**, **Accept**, or
     **Continue**.

7. To preview your consent pop-up, choose **Preview** in the
   top-right corner. After the preview, choose **Close preview**.
8. Choose **Save changes**.
