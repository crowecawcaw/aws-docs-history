# Edit row or column filters in Amazon SageMaker Unified Studio

To edit a row or a column filter, follow the steps below:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane
   and select the project to which the asset belongs.
3. Under **Project catalog** in the left side navigation, choose **Assets**.
4. Make sure you are on the **Inventory** tab,
   then choose the name of the asset that contains the filter that you want to edit.
5. On the asset detail page, go to **Asset filters** tab and
   then choose the name of the filter that you want to edit.
6. You can edit the following fields:
   - **Name** – the name of the filter
   - **Description** – the description of the
     filters

7. If you're editing a row filter, you can update the row filter
   expression.
8. If you're editing a column filter, you can add or remove the columns selected
   in the filter.
9. After you have made the changes, choose **Edit asset
   filter**.

###### Note

If you edit a filter that is being used in active subscriptions, Amazon SageMaker Unified Studio will
automatically update the permissions granted to the subscriber projects. This means
that the subscribers will only be able to access the rows or columns as defined in
the updated filter, ensuring that your data access policies are consistently
enforced.
