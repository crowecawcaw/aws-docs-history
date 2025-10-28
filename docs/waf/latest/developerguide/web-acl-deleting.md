**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Deleting a protection pack (web ACL)

This section provides procedures for deleting protection packs (web ACLs) through
the AWS console.

To delete a protection pack (web ACL), you first disassociate all AWS resources from the protection pack (web ACL).
Perform the following procedure.

Using the new console

1. Sign in to the new AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2-pro](https://console.aws.amazon.com/wafv2-pro "https://console.aws.amazon.com/wafv2-pro").
2. In the navigation pane, choose **Resources &
   protection packs (web ACLs)**.
3. In the protection pack (web ACL) card, choose the
   **Edit** link next to
   **Resources** to open the **Manage
   resources** panel.
4. In the **Manage resources** section for the rule
   group, choose the resource you want to disassociate, and then choose
   **Disassociate**.

###### Note

You must disassociate one resource at a time. Do not choose
multiple resources. 5. In the confirmation page, type "disassociate", and then choose
**Disassociate**. Repeat to disassociate each
resource in the protection pack (web ACL). 6. Choose the protection pack (web ACL) that you want to delete. The console
makes the main protection pack (web ACL) card editable, and also opens a
side panel with details you can edit. 7. In the details panel, choose the trash can icon. 8. In the confirmation page, type "delete" and then choose
**Delete**.

Using the standard console

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **web ACLs**.
3. Select the name of the web ACL that you want to delete. The console takes you to the web
   ACL's description, where you can edit it.

###### Note

If you don't see the web ACL that you want to delete,
make sure the Region selection inside the web ACLs section is correct.
Any web ACLs that protect Amazon CloudFront distributions are in **Global (CloudFront)**. 4. On the **Associated AWS resources** tab, for each
associated resource, select the radio button next to the resource
name and then choose **Disassociate**. This
disassociates the protection pack (web ACL) from your AWS resources. 5. In the navigation pane, choose **web ACLs**. 6. Select the radio button next to the web ACL that you are deleting, and
then choose **Delete**.
