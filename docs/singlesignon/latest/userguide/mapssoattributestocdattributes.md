# Mapping user attributes between IAM Identity Center and

Microsoft AD directory

You can use the following procedure to specify how your user attributes in IAM Identity Center should
map to corresponding attributes in your Microsoft AD directory.

###### To map attributes in IAM Identity Center to attributes in your directory

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Settings**.
3. On the **Settings** page, choose the **Attributes for
   access control** tab, and then choose **Manage
   Attributes**.
4. On the **Manage attribute for access control** page, find the
   attribute in IAM Identity Center that you want to map and then type a value in the text box. For
   example, you might want to map the IAM Identity Center user attribute
   **`email`** to the Microsoft AD directory attribute
   **`${mail}`**.
5. Choose **Save changes**.
