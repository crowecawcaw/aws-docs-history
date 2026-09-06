

# Send predictions to Quick
<a name="canvas-send-predictions"></a>

**Note**  
You can send batch predictions to Quick for numeric and categorical prediction and time series forecasting models. Single-label image prediction and multi-category text prediction models are excluded.

Once you generate batch predictions with custom tabular models in SageMaker Canvas, you can send those predictions as CSV files to Quick, which is a business intelligence (BI) service to build and publish predictive dashboards.

For example, if you built a 2 category prediction model to determine whether a customer will churn, you can create a visual, predictive dashboard in Quick to show the percentage of customers that are expected to churn. To learn more about Quick, see the [Quick User Guide](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

The following sections show you how to send your batch predictions to Quick for analysis.

## Before you begin
<a name="canvas-send-predictions-prereqs"></a>

Your user must have the necessary AWS Identity and Access Management (IAM) permissions to send your predictions to Quick. Your administrator can set up the IAM permissions for your user. For more information, see [Grant Your Users Permissions to Send Predictions to Quick](canvas-quicksight-permissions.md).

Your Quick account must contain the `default` namespace, which is set up when you first create your Quick account. Contact your administrator to help you get access to Quick. For more information, see [Setting up for Quick](https://docs.aws.amazon.com/quicksight/latest/user/setting-up.html) in the *Quick User Guide*.

Your Quick account must be created in the same Region as your Canvas application. If your Quick account’s home Region differs from your Canvas application’s Region, you must either [close](https://docs.aws.amazon.com/quicksight/latest/user/closing-account.html) and recreate your Quick account, or [set up a Canvas application](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html#canvas-prerequisites) in the same Region as your Quick account. You can check your Quick home Region by doing the following (assuming you already have an Quick account):

1. Open your [Quick console](https://quicksight.aws.amazon.com/).

1. When the page loads, your Quick home Region is appended to the URL in the following format: `https://{{<your-home-region>}}.quicksight.aws.amazon.com/`.

You must know the usernames of the Quick users to whom you want to send your predictions. You can send predictions to yourself or other users who have the right permissions. Any users to whom you send predictions must be in the `default` [namespace](https://docs.aws.amazon.com/quicksight/latest/user/namespaces.html) of your Quick account and have the `Author` or `Admin` role in Quick.

Additionally, Quick must have access to the SageMaker AI default Amazon S3 bucket for your domain, which is named with the following format: `sagemaker-{{{REGION}}}-{{{ACCOUNT_ID}}}`. The Region should be the same as your Quick account's home Region and your Canvas application’s Region. To learn how to give Quick access to the batch predictions stored in your Amazon S3 bucket, see the topic [I can’t connect to Amazon S3](https://docs.aws.amazon.com/quicksight/latest/user/troubleshoot-connect-S3.html) in the *Quick User Guide*.

## Supported data formats
<a name="canvas-send-predictions-formatting"></a>

Before sending your predictions, check that the data format of your batch predictions is compatible with Quick.
+ To learn more about the accepted data formats for timeseries data, see [Supported date formats](https://docs.aws.amazon.com/quicksight/latest/user/supported-date-formats.html) in the *Quick User Guide*.
+ To learn more about data values that might prevent you from sending to Quick, see [Unsupported values in data](https://docs.aws.amazon.com/quicksight/latest/user/unsupported-data-values.html) in the *Quick User Guide*.

Also note that Quick uses the character `"` as a text qualifier, so if your Canvas data contains any `"` characters, make sure that you close all matching quotes. Any mismatching quotes can cause issues with sending your dataset to Quick.

## Send your batch predictions to Quick
<a name="canvas-send-predictions-send"></a>

Use the following procedure to send your predictions to Quick:

1. Open the SageMaker Canvas application.

1. In the left navigation pane, choose **My models**.

1. On the **My models** page, choose your model.

1. Choose the **Predict** tab.

1. Under **Predictions**, select the dataset (or datasets) of batch predictions that you’d like to share. You can share up to 5 datasets of batch predictions at a time.

1. After you select your dataset, choose **Send to Quick**.
**Note**  
The **Send to Quick** button doesn’t activate unless you select one or more datasets.

   Alternatively, you can preview your predictions by choosing the **More options** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)) and then **View prediction results**. From the dataset preview, you can choose **Send to Quick**. The following screenshot shows you the **Send to Quick** button in a dataset preview.  
![Screenshot of a dataset preview with the Send to Quick button at the bottom.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/send-to-quicksight-preview.png)

1. In the **Send to Quick** dialog box, do the following:

   1. For **QuickSight users**, enter the name of the Quick users to whom you want to send your predictions. If you want to send them to yourself, enter your own username. You can only send predictions to users in the `default` namespace of the Quick account, and the user must have the `Author` or `Admin` role in Quick.

   1. Choose **Send**.

   The following screenshot shows the **Send to Quick** dialog box:  
![The Send to Quick dialog box.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/send-to-quicksight.png)

After you send your batch predictions, the **QuickSight** field for the datasets you sent shows as `Sent`. In the confirmation box that confirms your predictions were sent, you can choose **Open Quick** to open your Quick application. If you’re done using Canvas, you should [log out](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-log-out.html) of the Canvas application.

The Quick users that you’ve sent datasets to can open their Quick application and view the Canvas datasets that have been shared with them. Then, they can create predictive dashboards with the data. For more information, see [Getting started with Quick data analysis](https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html) in the *Quick User Guide*.

By default, all of the users to whom you send predictions have owner permissions for the dataset in Quick. Owners are able to create analyses, refresh, edit, delete, and re-share datasets. The changes that owners make to a dataset change the dataset for all users with access. To change the permissions, go to the dataset in Quick and manage its permissions. For more information, see [Viewing and editing the permissions users that a dataset is shared with](https://docs.aws.amazon.com/quicksight/latest/user/sharing-data-sets.html#view-users-data-set) in the *Quick User Guide*.