# Edit row or column filters in Amazon DataZone

To edit a row or a column filter, follow the steps below:

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Navigate to the **Data** tab for the project.
3. Choose **Published data** or **Inventory
   data** from the left navigation pane, then select the asset where
   you want to edit a row or a column filter.
4. On the asset detail page, go to **Asset filters** tab and
   then open the filter you want to edit.
5. You can edit the following field:
   - **Description** – the description of the
     filters

6. If you're editing a row filter, you can update the row filter
   expression.
7. If you're editing a column filter, you can add or remove the columns selected
   in the filter.
8. Once you have made the changes, choose **Edit asset
   filter**.

###### Note

If you edit a filter that is being used in active subscriptions, Amazon DataZone will
automatically update the permissions granted to the subscriber projects. This means
that the subscribers will only be able to access the rows or columns as defined in
the updated filter, ensuring that your data access policies are consistently
enforced.
