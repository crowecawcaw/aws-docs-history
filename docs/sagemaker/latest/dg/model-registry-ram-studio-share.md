# Share model group in

Studio

You can share your model groups with other AWS principals (AWS accounts or
AWS Organizations) using the Studio UI. This streamlined sharing process enables
cross-team collaboration, promotes best practices, and facilitates model reuse
across your teams. The following will provide instructions on how to share model
groups in Studio.

This feature is not available in Amazon SageMaker Studio Classic.

- If Studio is your default experience, the UI is similar to the
  images found in [Amazon SageMaker Studio UI overview](studio-updated-ui.md "studio-updated-ui.md").
- If Studio Classic is your default experience, the UI is similar to the
  images found in [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").
  To share model groups you will first need to make sure that you have the
  following permission added to the execution role you a sharing the resources
  from.

1. [Get your execution
   role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role").
2. [Update role permissions](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") with the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ram:ListPermissions",
 "ram:GetPermission",
 "ram:GetResourceShareAssociations",
 "ram:ListResourceSharePermissions",
 "ram:DeleteResourceShare",
 "ram:GetResourceShareInvitations",
 "ram:AcceptResourceShareInvitation"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following provides instructions on how to share a model group with other
AWS principals.

###### To share a model group with other AWS principals

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Choose **Models** from the left navigation
   pane.
3. Choose the **Registered models** tab, if not selected
   already.
4. Immediately below the **Registered models** tab
   label, choose **Model Groups**, if not selected
   already.
5. Select a registered model.
6. At the top right corner, choose **Share**. This will
   open the **Share model group** section.

If you see an error message at the bottom of the screen, you will need
add the appropriate permissions to your execution role. See the above
permissions for more information. 7. Under **Resource shares**, choose a resource share to
update or create a new resource share. 8. Under **Managed permission**, choose a managed
permission to control the level of access for your model.

The viewable options include permissions that have already been
created for you or your custom made permissions in AWS RAM. See [Creating and using customer managed permissions](../../../ram/latest/userguide/create-customer-managed-permissions.md "../../../ram/latest/userguide/create-customer-managed-permissions.md") in the
_AWS Resource Access Manager_ User Guide. 9. Under **AWS principals**, input the AWS Organizations ARN or
AWS account IDs you wish to share to and then choose
**Add**. You can add multiple AWS principals this
way. 10. When the minimum requirements are satisfied, the
**Share** button becomes accessible. Once you have
verified your settings, choose **Share**.

A successful share will result in a green banner message at the bottom
of the screen.
