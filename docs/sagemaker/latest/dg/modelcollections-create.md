# Create a Collection

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

You can create a Collection in the Amazon SageMaker Studio console. To create a
Collection, complete the following steps based on whether you use Studio or
Studio Classic.

Studio

1. Open the SageMaker Studio console by following the
   instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose
   **Models**.
3. Choose the **Registered models** tab, if not
   selected already.
4. Immediately below the **Registered models**
   tab label, choose **Collections**.
5. (Optional) To create a Collection inside another Collection,
   navigate to the hierarchy where you want to add your Collection.
   Otherwise, your Collection is created at the root level.
6. In the **Actions** dropdown menu in the top
   right, choose **Create new collection**.
7. Enter a name for your Collection in the
   **Name** field of the dialog box.

###### Note

If you plan to create multiple hierarchies in this
Collection, keep your Collection names short. The absolute
path, which is a string representing the location of your
Collections from the root level, must be 256 characters or
less. For additional details, see [Collection and Model Group
tagging](modelcollections-limitations.md#modelcollections-tagging "modelcollections-limitations.md#modelcollections-tagging"). 8. (Optional) To add Model Groups to your Collection, complete
the following steps:

    1. Choose **Select model
     groups**.
    2. Select the Model Groups that you want to add. You can
     select up to 10.

9. Choose **Create**.
10. Check to make sure your Collection was created in the current
    hierarchy. If you do not immediately see your new Collection,
    choose **Refresh**.

Studio Classic

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch
   Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the left navigation pane, choose the
   **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Choose **Models**, and then **Model
   registry**.
4. Choose the **Collections** tab.
5. (Optional) To create a Collection inside another Collection,
   navigate to the hierarchy where you want to add your Collection.
   Otherwise, your Collection is created at the root level.
6. In the **Actions** dropdown menu in the top
   right, choose **Create new collection**.
7. Enter a name for your Collection in the
   **Name** field of the dialog box.

###### Note

If you plan to create multiple hierarchies in this
Collection, keep your Collection names short. The absolute
path, which is a string representing the location of your
Collections from the root level, must be 256 characters or
less. For additional details, see [Collection and Model Group
tagging](modelcollections-limitations.md#modelcollections-tagging "modelcollections-limitations.md#modelcollections-tagging"). 8. (Optional) To add Model Groups to your Collection, complete
the following steps:

    1. Choose **Select model
     groups**.
    2. Select the Model Groups that you want to add. You can
     select up to 10.

9. Choose **Create**.
10. Check to make sure your Collection was created in the current
    hierarchy. If you do not immediately see your new Collection,
    choose **Refresh**.
