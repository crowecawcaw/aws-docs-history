# Create

row filters in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio allows you to create row filters that you can use when approving
subscriptions to make sure that the subscriber can only access rows of data as defined
in the row filters. To create a row filter, follow the steps below:

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
   - **Name** - the name of the filter
   - **Description** – the description of the
     filters

7. Under filter type, choose **Row filter**.
8. Under row filter expression, provide one or more expressions for row
   filter.
   - Choose a column from the **Column**
     dropdown.
   - Choose an operator from the **Operator**
     dropdown.
   - Enter a value in the **Value** field.

9. To add another condition to your filter expression, choose **Add
   condition**.
10. When using multiple conditions in the row filter expression, choose
    **And** or **Or** to link the
    conditions.
11. Select an option to indicate whether or not the filter contains sensitive values that you want to hide from approved subscribers.
12. Choose **Create asset filter**.
