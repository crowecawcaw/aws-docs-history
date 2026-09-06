

# Managing Worker details offline
<a name="ManagingWorkerDetailsOffline"></a>

If you have a large number of Workers, it's easier to manage them offline using another application, such as Microsoft Excel. This section shows how to download Worker information, edit it, and upload it.

**To download and modify Worker details**

1. On the Mechanical Turk Requester website at [https://requester.mturk.com/](https://requester.mturk.com/), choose the **Manage** tab and then choose **Workers**.

1. On the **Manage Workers** page, choose **Download CSV**. A **Generating Workers Results** page may temporarily appear while your CSV is generated. 

1. On the **Download Workers Results** page, a dialog box appears when your CSV is ready. choose the word **here** in the first sentence to download the Worker data file.

1. The Worker data downloads and opens in Microsoft Excel. The **CURRENT-{{QualName}}** column shows the Worker's current qualification score. If the cell is blank, you haven't assigned the qualification type to the Worker. The far-right column, **CURRENT BlockStatus**, shows the Worker's block status.

1. To update the values, do one or more of the following:
   + Indicate which qualification type to assign a Worker by putting a qualification score in the **UPDATE-{{QualName}}** column. For example, **UPDATE-Good Tagger**. Qualification scores must be 0 to 100, inclusive.
   + To revoke the qualification type, enter **Revoke** in the **UPDATE** column for your qualification type.
   + Block or unblock a worker by entering **Block** or **Unblock** in the **UPDATE-BlockStatus** column.

1. Save the `.csv` and choose **Workers**.

1. On the **Manage Workers** page, choose **Upload CSV**.

1. In the **Manage Workers Offline** window, choose **Choose File** to find the `.csv` file you saved, and then choose **Upload CSV**.

1. In the **Processing File** window, review the details about the changes you've made, and then choose **Yes** to confirm that you would like to save the changes for your **Workers**.

1. If your changes to not appear on the **Manage Workers** page, refresh the page to view your changes. 