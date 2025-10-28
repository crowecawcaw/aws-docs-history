# Configuring flywheels using the console

You can use the Amazon Comprehend console to create, update, and delete flywheels.

When you create a flywheel, Amazon Comprehend creates a data lake to hold all the data that the flywheel needs, such as the
training data and test data for each version of the model.

When you delete a flywheel, Amazon Comprehend doesn't delete the data lake or the model associated with the flywheel.

Review the information in section [Flywheel creation](flywheels-about.md#flywheels-about-create "flywheels-about.md#flywheels-about-create") before you create a new flywheel.

###### Topics

- [Create a flywheel](#flywheels-config-console-create "#flywheels-config-console-create")
- [Update a flywheel](#flywheels-update-console "#flywheels-update-console")
- [Delete a flywheel](#flywheels-delete-console "#flywheels-delete-console")

## Create a flywheel

When you create a flywheel, the required configuration fields depend on whether the flywheel is for an
existing custom model or a new model.

###### To create a flywheel

1.  Sign in to the AWS Management Console and open the [Amazon Comprehend console](https://console.aws.amazon.com/comprehend/ "https://console.aws.amazon.com/comprehend/").
2.  From the left menu, choose **Flywheels**.
3.  From the **Flywheels** table, choose **Create new flywheel**.
4.  Under **Flywheel name**, enter a name for the flywheel.
5.  (Optional) To create a flywheel for an existing model, configure the fields under
    **Active model version**.
    1. From the **Model** drop-down list, select a model
    2. From the **Version** drop-down list, select the model version.

6.  (Optional) To create a new classifier model for the flywheel,
    under **Custom model type**, choose a **Custom classification** and configure
    the parameters in following steps.
    1. Under **Language**, select the language for the model.
    2. Under **Classifier mode**, choose single-label mode or multi-label mode.
    3. Under **Custom labels**, enter one or more custom labels to use for training the model.
       Each label must match one of the classes in your input training data.

7.  (Optional) To create a new entity recognition model for the flywheel,
    under **Custom model type**, choose a **Custom entity recognition** and configure
    the parameters in following steps.
    1. Under **Language**, select the language for the model.
    2. Under **Custom entity type**, enter up to 25 custom entities to use for training the model.
       Each label must match one of the entity types in your input training data.

    To create more than one label, perform the following steps multiple times.

        1. Enter a custom label. The label must be all uppercase. Use an underscore as a separator between words in the label.
        2. Choose **Add type**.To remove one of the labels that you've added, choose **X** to the right of the label name.

8.  Configure your choices for volume encryption, model encryption, and data lake encryption.
    For each of these, choose whether to use an AWS owned KMS key or a key that you have permission to use.

        * If you are using an AWS owned KMS key, there are no additional parameters.
        * If you are using another existing key, for **KMS key
         ARN** enter the ARN for the key ID.
        * If you want to create a new key, choose **Create an AWS KMS key**.

    For more information on creating and using KMS keys and the associated encryption, see [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

        1. Configure the **Volume encryption** key. Amazon Comprehend uses this key to encrypt the data in
         the storage volume while your job is being processed. choose whether to use an AWS owned KMS key or a
         key that you have permission to use.
        2. Configure the **Model encryption** key. Amazon Comprehend uses this key to encrypt
         the model data for this model version.

9.  Configure the **Data lake location**. For more information, see
    [Data lake management](flywheels-datalake.md#flywheels-datalake-mgmt "flywheels-datalake.md#flywheels-datalake-mgmt").
10. (Optional) Configure **Data lake encryption** key.
    Amazon Comprehend uses this key to encrypt all files in the data lake.
11. (Optional) Configure **VPC settings**. Enter the VPC ID under **VPC** or choose
    the ID from the drop-down list.
    1. Choose the subnet under **Subnets(s)**. After you select the first subnet,
       you can choose additional ones.
    2. Under **Security Group(s)**, choose the security group to use if you
       specified one. After you select the first security group, you can choose additional
       ones.

12. Configure the **Service access** permissions.
    1. If you select **Use an existing IAM role**,
       select the role name in the drop-down list.
    2. If you select **Create an IAM role**, Amazon Comprehend creates a new role.
       The console displays the permissions that Amazon Comprehend configures for the role.
       Under **Role name**, enter a descriptive name for the role.

13. (Optional) Configure **Tags** settings. To add a tag, enter a key-value pair under
    **Tags**. Choose **Add tag**. To remove this pair before creating the
    flywheel, choose **Remove tag**. For more information, see [Tagging your resources](tagging.md "tagging.md").
14. Choose **Create**.

## Update a flywheel

You can configure the flywheel name, data lake location, model type, and model configuration only when you
create the flywheel.

When you update a flywheel, you can specify a different model if the model type and configuration options are
the same as the current model. You can configure a new active model version. You can also update encryption
details, service access permissions, and VPC settings.

###### To update a flywheel

1. Sign in to the AWS Management Console and open the [Amazon Comprehend console](https://console.aws.amazon.com/comprehend/ "https://console.aws.amazon.com/comprehend/").
2. From the left menu, choose **Flywheels**.
3. From the **Flywheels** table, choose the flywheel to update.
4. Under **Active model version**, choose a model from the **Model** drop-down list and
   choose a model version.

The form populates the model type and model configuration. 5. (Optional) Configure **Volume encryption** and **Model encryption** settings. 6. (Optional) Configure **Data lake encryption** settings. 7. Configure the **Service access** permissions. 8. (Optional) Configure **VPC settings**. 9. (Optional) Configure **Tags** settings. 10. Choose **Save**.

## Delete a flywheel

###### To delete a flywheel

1. Sign in to the AWS Management Console and open the [Amazon Comprehend console](https://console.aws.amazon.com/comprehend/ "https://console.aws.amazon.com/comprehend/").
2. From the left menu, choose **Flywheels**.
3. From the **Flywheels** table, choose the flywheel to delete.
4. Choose **Delete**.
