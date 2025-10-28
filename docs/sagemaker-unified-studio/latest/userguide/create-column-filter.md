# Create column filters in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables you to create column filters that you can use when approving
subscriptions to make sure that the subscriber can only access columns of data as
defined in the column filters. To create a column filter, follow the steps below:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane
   and select the project to which the asset belongs.
3. Under **Project catalog** in the left side navigation, choose **Assets**.
4. Make sure you are on the **Inventory** tab,
   then choose the name of the asset that you want to create a column filter for. You can add column
   filters if your data asset in Amazon SageMaker Unified Studio is of type AWS Glue table, Amazon Redshift table, or Amazon Redshift view.
   You are then brought to the asset details page.
5. On the asset detail page, go to the **Asset filters** tab and
   then choose **Add asset filter**.
6. Configure the following fields:
   - **Name** – the name of the filter
   - **Description** – the description of the
     filters

7. Under filter type, choose **Column**.
8. Select the columns you want to include in the filters using the check boxes
   for the columns in the data asset.
9. Choose **Create asset filter**.
