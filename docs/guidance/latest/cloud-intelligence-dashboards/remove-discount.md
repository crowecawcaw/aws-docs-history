# Removing Discounts

## Last Updated

August 2024

## Author

- Deepthi Nune, Sr. Technical Account Manager, AWS

## Introduction

In this customization playbook we will describe how you can remove all
Discounts information from Cloud Intelligence Dashboards (in this
example CUDOS). This can be helpful if you do not want to expose
Discount information to dashboard users, including Authors of customized
dashboards in Amazon QuickSight.

## Prerequisites

For this solution you must have the following:

- Ability to view and edit queries in Athena

### Step 1 of 2. Modify Queries in Athena

You will need to modify several queries in Athena to remove discounts.
Queries that you can modify to remove specific charge type are:

- summary_view
- resource_view

Navigate in the AWS Console to the **Athena** service

1. Select the **AwsDataCatalog** in the **DataSource** drop down.
2. In the **Database** drop down select the database where your CUR table is located.
3. Under Views, scroll down until you locate the **summary_view**.
4. Select the three dots to the right of the view and select **Show/edit query** from the context menu.

![Athena Query editor highlighting the summary view query and its context menu to select show edit query](images/cust_showedit_qry.png)

1. Modify the "Where" condition and include the two new "And" lines. In this example we also remove Refund, Credit and Tax along with Discounts

```
WHERE (("bill_billing_period_start_date" >= ("date_trunc"('month', current_timestamp) - INTERVAL  '7' MONTH)) AND (CAST("concat"("year", '-', "month", '-01') AS date) >= ("date_trunc"('month', current_date) - INTERVAL  '7' MONTH)))
AND line_item_line_item_type NOT LIKE '%Discount' -- New Line: remove all kind of discounts
AND line_item_line_item_type NOT IN ('Refund',  'Credit' , 'Tax')   -- New Line: (optional) If Refund, Tax, Credit etc., also need to be removed
```

2. When you’ve completed adding all of the fields, click the **RUN** button
   and confirm that the query view updates successfully.

![Inset show the run again button of the query window and the successful result](images/cust_runagain.png)

1. Repeat the steps above on the **resource_view** dataset.

### Step 2 of 2. Update DataSet in Amazon QuickSight

Next the data set in Amazon QuickSight needs to be refreshed in order to
view the changes immediately.

1. Navigate to Amazon QuickSight in the console.

![AWS Console search with results for QuickSight](images/cust_navqs.png) 2. Select Datasets on the left side of the page.

![Left navigation in QuickSight with datasets option highlighted](images/cust_qs_ds.png) 3. Locate **summary_view** in the list of datasets and click on the
dataset. 4. Click on the **Refresh** tab in the top left of the page. 5. Click on **Refresh Now** button in the top right of the page. 6. Repeat the steps to refresh **resource_view** dataset as well.

## Test

Now you can open CUDOS dashboard and check if the information about
Discounts is not present.
