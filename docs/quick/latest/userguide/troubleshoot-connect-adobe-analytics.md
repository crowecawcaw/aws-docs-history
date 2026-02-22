# I can't create or refresh a

dataset from an existing Adobe Analytics data source

As of May 1, 2022, Quick Sight no longer supports legacy OAuth and version 1.3
and SOAP API operations in Adobe Analytics. If you experience failures while trying
to create or refresh a dataset from an existing Adobe Analytics data source, you
might have a stale access token.

###### To troubleshoot failures while creating or refreshing a dataset from an

existing Adobe Analytics data source

1. Open Quick Sight and choose **Data** at left.
2. Choose **New** then **Dataset**.
3. On the **Create a dataset** page, choose the Adobe
   Analytics data source that you want to update from the list of existing data
   sources.
4. Choose **Edit data source**.
5. On the **Edit Adobe Analytics data source** page that
   opens, choose **Update data source** to reauthorize the
   Adobe Analytics connection.
6. Try recreating or refreshing the dataset again. The dataset creation or
   refresh should succeed.
