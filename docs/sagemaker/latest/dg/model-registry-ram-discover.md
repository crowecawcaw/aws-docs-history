# Set up discoverability

The resource owner can set up model package group discoverability by creating
resource shares and attaching resource policies to the entities. For detailed
steps about how to create a general resource share in AWS RAM, see [Create a resource share](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") in the [AWS RAM](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") documentation.

Complete the following instructions to set up model package group
discoverability using the AWS RAM console or Model Registry Resource Policy APIs.

AWS CLI

1.  Create a resource share in the model owner account.
    1. The model owner attaches a resource policy to the
       model package group using the SageMaker AI Resource Policy
       API [put-model-package-group-policy](../../../cli/latest/reference/sagemaker/put-model-package-group-policy.md "../../../cli/latest/reference/sagemaker/put-model-package-group-policy.md"), as
       demonstrated in the following command.

    ```
    aws sagemaker put-model-package-group-policy
    --model-package-group-name `<model-package-group-name>`
    --resource-policy "{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Sid\":
    \"ExampleResourcePolicy\",\"Effect\":\"Allow\",\"Principal\":`<principal>`,
    \"Action\":[\"sagemaker:DescribeModelPackage\",
    \"sagemaker:ListModelPackages\",\"sagemaker:DescribeModelPackageGroup\"],
    \"Resource\":[\"`<model-package-group-arn>`,\"
    \"arn:aws:sagemaker:`<region>`:`<owner-account-id>`:model-package/
    `<model-package-group-name>`/*\"]}]}"
    ```

    ###### Note

    Different combinations of actions can be
    attached to the resource policy. For custom
    policies, the permission created should be
    promoted by the model package group owner, and
    only entities with promoted permissions attached
    are discoverable. Unpromotable resource shares
    cannot be made discoverable or managed through
    AWS RAM. 2. To check that AWS RAM created the resource share
    ARN, use the following command:

    ```
    aws ram get-resource-share-associations --association-type `resource` --resource-arn `<model-package-group-arn>`
    ```

    The response contains the
    `resource-share-arn` for
    the entity. 3. To check if the attached policy permission is a
    managed or custom policy, use the following
    command:

    ```
    aws ram list-resource-share-permissions --resource-share-arn `<resource-share-arn>`
    ```

    The `featureSet` field can take values
    `CREATED_FROM_POLICY` or
    `STANDARD`, which are defined as
    follows:

        * `STANDARD`: The permission
         already exists.
        * `CREATED_FROM_POLICY`: The
         permission needs to be promoted in order for the
         entity to be discoverable. For more information,
         see [Promote the permission and resource
         share](model-registry-ram-promote.md "model-registry-ram-promote.md").

2.  Accept the resource share invitation in the model consumer
    account.
    1. The model package group consumer accepts the
       invitation for resource share. To see all resource
       invitations, run the following command:

    ```
    aws ram get-resource-share-invitations
    ```

    Identify the requests that have status
    `PENDING` and include the account ID of
    the owner account. 2. Accept the resource share invitation from the
    model owner using the following command:

    ```
    aws ram accept-resource-share-invitation --resource-share-invitation-arn `<resource-share-invitation-arn>`
    ```

AWS RAM console

1. Log into the [AWS RAM
   console](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. Complete the following steps to create a resource share
   from the model package group owner account.
   1. Complete the following steps to specify resource
      share details.
      1. In the **Name** field, add
         a unique name for your resource.
      2. In the **Resources** card,
         choose the dropdown menu and select **SageMaker AI
         Model Package Groups**.
      3. Select the check box of the ARN of the model
         package group resource share.
      4. In the **Select resources**
         card, select the check box of your model package
         group resource share.
      5. In the **Tags** card, add
         key-value pairs for tags to add to your resource
         share.
      6. Choose **Next**.

   2. Complete the following steps to associate managed
      permissions to the resource share.
      1. If you use a managed permission, choose a
         managed permission in the **Managed
         permissions** dropdown menu.
      2. If you use a custom permission, choose
         **Customer Managed Permission**.
         In this case, the model package group is not
         immediately discoverable. You have to promote the
         permission and the resource policy after you
         create the resource share. For information about
         how to promote permissions and resource shares,
         see [Promote the permission and resource
         share](model-registry-ram-promote.md "model-registry-ram-promote.md"). For
         more information about how to attach custom
         permissions, see [Creating and using customer managed permissions
         in AWS RAM](../../../ram/latest/userguide/create-customer-managed-permissions.md "../../../ram/latest/userguide/create-customer-managed-permissions.md").
      3. Choose **Next**.

   3. Complete the following steps to grant access to
      principals.
      1. Choose **Allow sharing with
         anyone** to allow sharing with accounts
         outside of your organization, or choose
         **Allow sharing only within your
         organization**.
      2. In the **Select principal
         type** dropdown menu, add the principal
         types and ID for the principals you want to
         add.
      3. Add and select the chosen principals for the
         share.
      4. Choose **Next**.

   4. Review the displayed share configuration and then
      choose **Create resource
      share**.

3. Accept the resource share invitation from the consumer
   account. Once the model owner creates the resource share and
   principal associations, the specified resource consumer
   accounts receive an invitation to join the resource share.
   The resource consumer accounts can view and accept the
   invitations in the [Shared with me: Resource shares](https://console.aws.amazon.com/ram/home#SharedResourceShares: "https://console.aws.amazon.com/ram/home#SharedResourceShares:") page in the
   AWS RAM console. For more information about accepting and
   viewing resources in AWS RAM, see [Access AWS resources shared with you](../../../ram/latest/userguide/working-with-shared.md "../../../ram/latest/userguide/working-with-shared.md").
