# Create row filters in Amazon DataZone

Amazon DataZone allows you to create row filters that you can use when approving
subscriptions to make sure that the subscriber can only access rows of data as defined
in the row filters. To create a row filter, follow the steps below:

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project to which the asset belongs.
3. Navigate to the **Data** tab for the project.
4. Choose **Published data** from the left navigation pane, then
   select the asset for which you want to create the row filter. You can add row
   filters if your data asset in Amazon DataZone is of type AWS Glue table, Amazon
   Redshift table, or Amazon Redshift view.
5. On the asset detail page, go to the **Asset filters** tab and
   then choose **Add asset filter**.
6. Configure the following fields:
   - **Name** - the name of the filter
   - **Description** – the description of the
     filters

7. Under filter type, choose **Row filter**.
8. Under row filter expression, provide one or more expressions for row
   filter.
   - Choose **column** from the column from the
     dropdown.
   - Choose **operator** from the operator
     dropdown.
   - Enter value in the **Value** field.

9. To add another condition to your filter expression, choose **Add
   condition**.
10. When using multiple conditions in the row filter expression, choose
    **And** or **Or** to link the
    conditions.
11. Choose **Create filter**.
    For information on how to apply row filters to a subscription, see [Approve or reject a subscription
    request in Amazon DataZone](approve-reject-subscription-request.md "approve-reject-subscription-request.md") .
