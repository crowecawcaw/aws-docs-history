# Updating provisioned product properties

You can change the owner of a provisioned product at any time. You need to know the user's
ARN or the role you want to set as the new owner.

###### Note

This feature is only available if your administrator has given you access to update the properties of provisioned products.

###### To change the owner of a provisioned product

1. Select the provisioned product to update, choose the **Actions** tab, and then select **Change owner**.
   You can also find the **Change owner** option on the detail
   page of the provisioned product.
2. Enter the ARN of the user or role you want to set as the new owner. An ARN begins with
   `arn:` and includes other information, separated by colons or slashes. For
   example: `arn:aws:iam::123456789012:user/NewOwner`.
3. Choose **Change owner**. You see a success message when the
   owner has been updated.
