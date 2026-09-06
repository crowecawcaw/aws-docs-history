

# Using Amazon SageMaker Feature Store in the console
<a name="feature-store-use-with-studio"></a>

**Important**  
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).  
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

You can use Amazon SageMaker Feature Store on the console to create, view, update, and monitor your feature groups. Monitoring in this guide includes viewing pipeline executions and lineage of your feature groups. This guide provides instructions on how to achieve these tasks from the console.

For Feature Store examples and resources using the Amazon SageMaker APIs and AWS SDK for Python (Boto3), see [Amazon SageMaker Feature Store resources](feature-store-resources.md).

**Topics**
+ [Create a feature group from the console](#feature-store-create-feature-group-studio)
+ [View feature group details from the console](#feature-store-view-feature-group-detail-studio)
+ [Update a feature group from the console](#feature-store-update-feature-group-studio)
+ [View pipeline executions from the console](#feature-store-view-feature-processor-pipeline-executions-studio)
+ [View lineage from the console](#feature-store-view-feature-processor-pipeline-lineage-studio)

## Create a feature group from the console
<a name="feature-store-create-feature-group-studio"></a>

The create feature group process has four steps:

1. Enter feature group information.

1. Enter feature definitions.

1. Enter required features.

1. Enter feature group tags.



Consider which of the following options fits your use case:
+ Create an online store, an offline store, or both. For more information about the differences between online and offline stores, see [Feature Store concepts](feature-store-concepts.md).
+ Use a default AWS Key Management Service key or your own KMS key. The default key is [AWS KMS key (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html). You can reduce AWS KMS request costs by configuring use of Amazon S3 Bucket Keys on the offline store Amazon S3 bucket. The Amazon S3 Bucket Key must be enabled before using the bucket for your feature groups. For more information about reducing the cost by using Amazon S3 Bucket Keys, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html).

  You can use the same key for both online and offline stores, or have a unique key for each. For more information about AWS KMS, see [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).
+ If you create an offline store:
  + Decide if you want to create an Amazon S3 bucket or use an existing one. When using an existing one, you must know the Amazon S3 bucket URL or Amazon S3 bucket name and dataset directory name, if applicable.
  + Choose which Amazon Resource Name (ARN) to use to specify the IAM role. For more information about how to find your role and attached policies, see [Adding policies to your IAM role](feature-store-adding-policies.md).
  + Decide whether to use the AWS Glue (default) or Apache Iceberg table format. In most use cases, you use the Apache Iceberg table format. For more information about table formats, see [Use Feature Store with SDK for Python (Boto3)](feature-store-create-feature-group.md).

You can use the console to view the lineage of a feature group. The instructions for using Feature Store on the console vary depending on whether you enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience.

### Create feature groups if Studio is your default experience (console)
<a name="feature-store-create-feature-group-studio-how-to-with-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** from the left navigation pane to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. Choose **Create feature group**.

1. Under **Feature group details**, enter a feature group name.

1. (Optional) Enter a description of the feature group.

1. Under **Feature group storage configuration**, choose a storage configuration from the dropdown list. For information about storage configurations, see [Feature Store storage configurations](feature-store-storage-configurations.md).

1. If you have chosen to enable the online storage:

   1. If you *only* enable the online storage, you can choose a **Storage type** from the dropdown list. For information about online store storage types, see [Online store](feature-store-storage-configurations-online-store.md).

   1. (Optional) Apply **Time to Live (TTL)** by toggling the switch to **On** and specifying the **Time to Live duration** value and unit. This will update the default TTL duration for all records added to the feature group *after the feature group is created*. For more information about TTL, see [Time to live (TTL) duration for records](feature-store-time-to-live.md).

1. If you have chosen to enable the offline storage:

   1. Under the **Amazon S3 bucket name**, enter a new bucket name, or enter an existing bucket URL, manually.

   1. From the **Table format** dropdown list, choose the table format. In most use cases, you should use the Apache Iceberg table format. For more information about table formats, see [Use Feature Store with SDK for Python (Boto3)](feature-store-create-feature-group.md).

   1. Under **IAM role ARN**, choose the IAM role ARN you want to attach to this feature group. For more information about how to find your role and attached policies, see [Adding policies to your IAM role](feature-store-adding-policies.md).

   1. If you have chosen to enable the offline storage **Table format** and AWS Glue (default) **Table format**, under **Data catalog**, you can choose one of the following two options:
      + **Use default values for your AWS Glue Data Catalog**.
      + Provide your existing Data Catalog name, table name, and database name to extend your existing AWS Glue Data Catalog. 

1. Under the **Online store encryption key** or **Offline store encryption key** dropdown list, choose one of the following options:
   + **Use AWS managed AWS KMS key (default)**
   + **Enter an AWS KMS key ARN** and enter your AWS KMS key ARN under **Offline store encryption key ARN**. For more information about AWS KMS, see [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

1. If applicable, you will have the option to choose your throughput mode, which impacts how you are charged. Under **Throughput mode**, choose a mode from the dropdown list and input the read and write capacities when available. For information about throughput modes, like when the mode can be applied and capacity units, see [Throughput modes](feature-store-throughput-mode.md).

1. After you specify all of the required information, the **Continue** button appears available. Choose **Continue**.

1. Under **Specify feature definitions**, you have two options for providing a schema for your features: a JSON editor, or a table editor.
   + JSON editor: In the **JSON** tab, enter or copy and paste your feature definitions in the JSON format.
   + Table editor: In the **Table** tab, enter the feature feature name and choose the corresponding data type for each feature in your feature group. Choose **\+ Add feature definitions** to include more features. Be aware that you cannot remove feature definitions from your feature groups. However, you can add and update feature definitions after the feature group is created.

   There must be at least two features in a feature group that represent the record identifier and event time:
   + The record **Feature type** can be a string, fractional, or an integral.
   + The event time **Feature type** must be a string or a fractional. However, if you chose the Iceberg table format, the event time must be a string.

1. After all of the features are included, choose **Continue**.

1. Under **Select required features**, you must specify the record identifier and event time features. Do this by choosing the feature name under **Record identifier feature name** and **Event time feature name** dropdown lists, respectively.

1. After you choose the record identifier and event time features, choose **Continue**.

1. (Optional) To add tags for the feature group, choose **Add new tag**. Then enter a tag key and the corresponding value under **Key** and **Value**, respectively.

1. Choose **Continue**.

1. Under **Review feature group**, review the feature group information. To edit any step, choose the **Edit** button that corresponds to that step. This brings you to the corresponding step for editing. To return to step 5, choose **Continue** until you return to step 5. 

1. After you finalize the setup for your feature group, choose **Create feature group**.

   If an issue occurs during setup, a pop-up alert message appears at the bottom of the page with tips for solving the issue. You can return to previous steps to fix the issues by choosing **Edit** for the step with conflicts.

   After the feature group has been successfully created, a green pop-up message appears at the bottom of the page. The new feature group also appears in your feature groups catalog.

### Create feature groups if Studio Classic is your default experience (console)
<a name="feature-store-create-feature-group-studio-how-to-with-studio-classic"></a>

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose the **Home** icon (![Black square icon representing a placeholder or empty image.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) on the left navigation pane.

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. Choose **Create feature group**.

1. Under **Feature group details**, enter a feature group name.

1. (Optional) Enter a description of the feature group.

1. Under **Feature group storage configuration**, choose a storage configuration from the dropdown list. For information about storage configurations, see [Feature Store storage configurations](feature-store-storage-configurations.md).

1. If you have chosen to enable the online storage:

   1. If you *only* enable the online storage, you may choose a **Storage type** from the dropdown list. For information about online store storage types, see [Online store](feature-store-storage-configurations-online-store.md).

   1. (Optional) Apply **Time to Live (TTL)** by toggling the switch to **On** and specifying the **Time to Live duration** value and unit. This will update the default TTL duration for all records added to the feature group *after the feature group is created*. For more information about TTL, see [Time to live (TTL) duration for records](feature-store-time-to-live.md).

1. If you have chosen to enable the offline storage:

   1. Under the **Amazon S3 bucket name**, enter a new bucket name or enter an existing bucket URL manually.

   1. From the **Table format** dropdown list, choose the table format. In most use cases, you should use the Apache Iceberg table format. For more information about table formats, see [Use Feature Store with SDK for Python (Boto3)](feature-store-create-feature-group.md).

   1. Under **IAM role ARN**, choose the IAM role ARN you want to attach to this feature group. For more information about how to find your role and attached policies, see [Adding policies to your IAM role](feature-store-adding-policies.md).

   1. If you have chosen to enable the offline storage **Table format** and AWS Glue (default) **Table format**, under **Data catalog**, you can choose one of the following two options:
      + **Use default values for your AWS Glue Data Catalog**.
      + Provide your existing Data Catalog name, table name, and database name to extend your existing AWS Glue Data Catalog. 

1. Under the **Online store encryption key** or **Offline store encryption key** dropdown list, choose one of the following options:
   + **Use AWS managed AWS KMS key (default)**
   + **Enter an AWS KMS key ARN** and enter your AWS KMS key ARN under **Offline store encryption key ARN**. For more information about AWS KMS, see [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

1. After you specify all of the required information, the **Continue** button appears available. Choose **Continue**.

1. Under **Specify feature definitions**, you have two options for providing a schema for your features: a JSON editor, or a table editor.
   + JSON editor: In the **JSON** tab, enter or copy and paste your feature definitions in the JSON format.
   + Table editor: In the **Table** tab, enter the feature feature name and choose the corresponding data type for each feature in your feature group. Choose **\+ Add feature definitions** to include more features. Be aware that you cannot remove feature definitions from your feature groups. However, you can add and update feature definitions after the feature group is created.

   There must be at least two features in a feature group that represent the record identifier and event time:
   + The record **Feature type** can be a string, fractional, or an integral.
   + The event time **Feature type** must be a string or a fractional. However, if you chose the Iceberg table format, the event time must be a string.

1. After all of the features are included, choose **Continue**.

1. Under **Select required features**, you must specify the record identifier and event time features. Do this by choosing the feature name under **Record identifier feature name** and **Event time feature name** dropdown lists, respectively.

1. After you choose the record identifier and event time features, choose **Continue**.

1. (Optional) To add tags for the feature group, choose **Add new tag**. Then enter a tag key and the corresponding value under **Key** and **Value**, respectively.

1. Choose **Continue**.

1. Under **Review feature group**, review the feature group information. To edit any step, choose the **Edit** button that corresponds to that step. This brings you to the corresponding step for editing. To return to step 5, choose **Continue** until you return to step 5. 

1. After you finalize the setup for your feature group, choose **Create feature group**.

   If an issue occurs during setup, a pop-up alert message appears at the bottom of the page with tips for solving the issue. You can return to previous steps to fix the issues by choosing **Edit** for the step with conflicts.

   After the feature group has been successfully created, a green pop-up message appears at the bottom of the page. The new feature group also appears in your feature groups catalog.

## View feature group details from the console
<a name="feature-store-view-feature-group-detail-studio"></a>

You can view details of your feature groups after a feature group has successfully been created in the Feature Store.

You can use the console or the Amazon SageMaker Feature Store API to view your feature group details. The instructions for using Feature Store through the console depends on if you have enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience.

### View feature group details if Studio is your default experience (console)
<a name="feature-store-view-feature-group-detail-studio-how-to-with-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** in the left navigation pane, to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Under the **Feature group catalog** tab, choose your feature group name from the list. This opens the feature group page.

1. On the **Features** tab, you can find a list of all of the features. Use the filter to refine your list. Choose a feature to view its details.

1. Under the **Details** tab and the **Information** subtab, you can review your feature group information. This includes **Latest execution**, **Offline storage settings**, **Online storage settings**, and more.

1. Under the **Details** tab and the **Tags** subtab, you can review your feature group tags. Choose **Add new tag** to add a new tag or **Remove** to remove a tag.

1. Under the **Pipeline Executions** tab, you can view the associated pipelines or pipeline executions for your feature group.

1. Under the **Lineage** tab, you can view the lineage of your feature group.

### View feature group details if Studio Classic is your default experience (console)
<a name="feature-store-view-feature-group-detail-studio-how-to-with-studio-classic"></a>

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose the **Home** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) in the left navigation pane.

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Under the **Feature group catalog** tab, choose your feature group name from the list. This opens the feature group page.

1. On the **Features** tab, you can find a list of all of the features. Use the filter to refine your list. Choose a feature to view its details.

1. Under the **Details** tab and the **Information** subtab, you can review your feature group information, including **Latest execution**, **Offline storage settings**, **Online storage settings**, and more.

1. Under the **Details** tab and the **Tags** subtab, you can review your feature group tags. Choose **Add new tag** to add a new tag or **Remove** to remove a tag.

1. Under the **Pipeline Executions** tab, you can view the associated pipelines or pipeline executions for your feature group.

1. Under the **Lineage** tab, you can view the lineage of your feature group.

## Update a feature group from the console
<a name="feature-store-update-feature-group-studio"></a>

You can update your feature groups after a feature group has successfully been created in the Feature Store.

You can use the console or the Amazon SageMaker Feature Store API to update a feature group. The instructions for using Feature Store through the console depends on if you have enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience.

### Update a feature group if Studio is your default experience (console)
<a name="feature-store-update-feature-group-studio-how-to-with-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** in the left navigation pane, to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Under the **Feature group catalog** tab, search for and choose your feature group name from the list. This opens the feature group page.

1. Choose **Update feature group**.

1. (Optional) If applicable, you can change your throughput mode, which impacts how you are charged. Under **Throughput mode**, choose a mode from the dropdown list and input the read and write capacities when available. For information about throughput modes, like when the mode can be applied and capacity units, see [Throughput modes](feature-store-throughput-mode.md).

1. (Optional) If your feature group uses the online store, you can update the default **Time to Live (TTL)**. If TTL hasn't been enabled for the feature group, toggle the switch button under **Time to Live (TTL)** to **On**. You can specify the TTL value and unit under **Time to Live duration**. This will update the default TTL duration for all records added to the feature group *after the feature group is updated*.

1. (Optional) You can add feature definitions to your feature group but be aware that you cannot remove feature definitions from your feature groups. To add a feature definition, choose **\+ Add feature definition** and then specify the new feature definition name under the **Name** column and select the feature type under the **Feature type** column.

1. Choose **Save changes**.

1. To confirm your changes, choose **Confirm**.

### Update a feature group if Studio Classic is your default experience (console)
<a name="feature-store-update-feature-group-studio-how-to-with-studio-classic"></a>

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose the **Home** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) in the left navigation pane.

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Under the **Feature group catalog** tab, search for and choose your feature group name from the list. This opens the feature group page.

1. Choose **Update feature group**.

1. (Optional) If your feature group uses the online store, you can update the default **Time to Live (TTL)**. If TTL hasn't been enabled for the feature group, toggle the switch button under **Time to Live (TTL)** to **On**. You can specify the TTL value and unit under **Time to Live duration**. This will update the default TTL duration for all records added to the feature group *after the feature group is updated*.

1. (Optional) You can add feature definitions to your feature group but be aware that you cannot remove feature definitions from your feature groups. To add a feature definition, choose **\+ Add feature definition** and then specify the new feature definition name under the **Name** column and select the feature type under the **Feature type** column.

1. Choose **Save changes**.

1. To confirm your changes, choose **Confirm**.

## View pipeline executions from the console
<a name="feature-store-view-feature-processor-pipeline-executions-studio"></a>

You can view the latest pipeline execution information for a feature or feature group under **Pipeline executions**. You can also get links to pipelines, executions, code, and other useful execution information.

You can use the console to view your pipeline executions. The instructions for using Feature Store through the console depends on if you have enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience.

### View pipeline executions if Studio is your default experience (console)
<a name="feature-store-view-feature-processor-pipeline-executions-studio-how-to-with-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** in the left navigation pane, to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Choose a feature group or feature to view their pipeline executions.

1. Choose the **Pipeline executions** tab.

1. Search for a pipeline from the **Select a pipeline** dropdown list.

1. You can view the links for the pipeline, execution, and code details. You can also view the execution owner, status, date, and duration.

### View pipeline executions if Studio Classic is your default experience (console)
<a name="feature-store-view-feature-processor-pipeline-executions-studio-how-to-with-studio-classic"></a>

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose the **Home** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) in the left navigation pane.

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Choose a feature group or feature to view their pipeline executions.

1. Choose the **Pipeline executions** tab.

1. Search for a pipeline from the **Select a pipeline** dropdown list.

1. You can view the links for the pipeline, execution, and code details. You can also view the execution owner, status, date, and duration.

## View lineage from the console
<a name="feature-store-view-feature-processor-pipeline-lineage-studio"></a>

You can view the lineage of a feature group. The lineage includes the information about the execution code of your feature processing workflow, what data sources were used, and how they are ingested to the feature group or feature.

You can use the console to view the lineage of a feature group. The instructions on using Feature Store through the console depends on if you have enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience.

### View lineage if Studio is your default experience (console)
<a name="feature-store-view-feature-processor-pipeline-lineage-studio-how-to-with-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** from the left navigation pane to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Choose a feature group or feature to view its lineage details.

1. Choose the **Lineage** tab.

1. Choose a feature group or pipeline node to expand the node. This contains more information about a feature group or pipeline.

1. You can zoom in, zoom out, or recenter the lineage graph by using the buttons on the bottom left of the screen.

1. You can move through the lineage map when you choose and drag the screen. To move your lineage maps using nodes as the focal point, you can press **Tab** or **Shift\+Tab** to switch between nodes.

1. If applicable, you can navigate the lineage upstream (left, earlier) or downstream (right, most recent). Do this by choosing a node and then choosing **Query upstream lineage** or **Query downstream lineage**.

### View lineage if Studio Classic is your default experience (console)
<a name="feature-store-view-feature-processor-pipeline-lineage-studio-how-to-with-studio-classic"></a>

1. Open Studio Classic by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose the **Home** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) in the left navigation pane.

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Choose a feature group or feature to view its lineage details.

1. Choose the **Lineage** tab.

1. Choose a feature group or pipeline node to expand the node. This contains more information about a feature group or pipeline.

1. You can zoom in, zoom out, or recenter the lineage graph by using the buttons on the bottom left of the screen.

1. You can move through the lineage map when you choose and drag the screen. To move your lineage maps using nodes as the focal point, you can press **Tab** or **Shift\+Tab** to switch between nodes.

1. If applicable, you can navigate the lineage upstream (left, earlier) or downstream (right, most recent). Do this by choosing a node and then choosing **Query upstream lineage** or **Query downstream lineage**.