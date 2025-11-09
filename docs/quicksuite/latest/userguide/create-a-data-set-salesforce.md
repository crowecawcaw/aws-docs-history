# Creating a dataset from

Salesforce

Use the following procedure to create a dataset by connecting to Salesforce and
selecting a report or object to provide data.

###### To create a dataset using Salesforce from a report or object

1. Check [Data source quotas](data-source-limits.md "data-source-limits.md")
   to make sure that your target report or object doesn't exceed data source
   quotas.
2. On the Quick Suite start page, choose **Data**.
3. On the **Data** page, choose **Create** then
   **New dataset**.
4. Choose the **Salesforce** icon.
5. Enter a name for the data source and then choose **Create data
   source**.
6. On the Salesforce login page, enter your Salesforce credentials.
7. For **Data elements: contain your data**, choose
   **Select** and then choose either
   **REPORT** or **OBJECT**.

###### Note

Joined reports aren't supported as Quick Sight data sources. 8. Choose one of the following options:

    * To prepare the data before creating an analysis, choose
     **Edit/Preview data** to open data preparation.
     For
     more information about data preparation, see [Preparing dataset examples](preparing-data-sets.md "preparing-data-sets.md").
    * Otherwise, choose a report or object and then choose
     **Select**.

9. Choose one of the following options:
   - To create a dataset and an analysis using the data as-is, choose
     **Visualize**.

   ###### Note

   If you don't have enough [SPICE](spice.md "spice.md") capacity, choose
   **Edit/Preview data**. In data preparation, you
   can remove fields from the dataset to decrease its size or apply a
   filter that reduces the number of rows returned. For more
   information about data preparation, see [Preparing dataset examples](preparing-data-sets.md "preparing-data-sets.md").
   - To prepare the data before creating an analysis, choose
     **Edit/Preview data** to open data preparation for
     the selected report or object. For more information about data
     preparation, see [Preparing dataset examples](preparing-data-sets.md "preparing-data-sets.md").

###### Note

The Salesforce connector is not supported in embedded console deployments where
users authenticate through namespace isolation. The OAuth authentication flow
requires direct Amazon Quick Sight console access to complete the sign-in process.
