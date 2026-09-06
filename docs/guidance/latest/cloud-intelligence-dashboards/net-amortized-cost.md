

# Net Amortized cost
<a name="net-amortized-cost"></a>

## Last Updated
<a name="last-updated"></a>

October 2024

## Author
<a name="author"></a>
+ Deepthi Nune, Sr. Technical Account Manager, AWS

## Introduction
<a name="introduction"></a>

By Default CUDOS dashboard shows Amortized and Unblended cost. For customers who would like to see cost after discounts, this guide provides steps to implement possibility to switch between Amortized and Net Amortized cost.

### Step 1 of 3. Modify Views/Queries in Athena
<a name="step-1-of-3-modify-viewsqueries-in-athena"></a>

You will need to modify several views in Athena to include net amortized cost. Views that you need to modify are:
+ summary\_view
+ hourly\_view
+ resource\_view

Navigate in the AWS Console to the **Athena** service

1. Select the **AwsDataCatalog** in the **DataSource** drop down

1. In the **Database** drop down select the database where your CUR table is located.

1. Under Views, scroll down until you locate the **summary\_view**.

1. Select the three dots to the right of the view and select **Show/edit query** from the context menu.

![Athena Query editor highlighting the summary view query and its context menu to select show edit query](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/cust_showedit_qry.png)


1. Find the line which ends with "amortized\_cost" and add the below snippet

   ```
       , SUM(CASE
   WHEN "line_item_line_item_type" = 'SavingsPlanRecurringFee' THEN (("savings_plan_total_commitment_to_date" - "savings_plan_used_commitment") * COALESCE((COALESCE("savings_plan_net_amortized_upfront_commitment_for_billing_period" , "savings_plan_amortized_upfront_commitment_for_billing_period") / NULLIF("savings_plan_amortized_upfront_commitment_for_billing_period" , 0)), 1))
   WHEN "line_item_line_item_type" = 'RIFee' THEN COALESCE("reservation_net_unused_amortized_upfront_fee_for_billing_period" + "reservation_net_unused_recurring_fee", "reservation_unused_amortized_upfront_fee_for_billing_period" + "reservation_unused_recurring_fee")
   WHEN "line_item_line_item_type" = 'SavingsPlanCoveredUsage' THEN COALESCE("savings_plan_net_savings_plan_effective_cost", "savings_plan_savings_plan_effective_cost")
   WHEN "line_item_line_item_type" = 'DiscountedUsage' THEN COALESCE("reservation_net_effective_cost", "reservation_effective_cost")
   WHEN "line_item_line_item_type" = 'Fee' AND COALESCE("reservation_reservation_a_r_n", '') = '' THEN COALESCE("line_item_net_unblended_cost", "line_item_unblended_cost")
   WHEN "line_item_line_item_type" IN ('Usage', 'Tax', 'Credit', 'Refund') THEN COALESCE("line_item_net_unblended_cost", "line_item_unblended_cost")
   ELSE 0 END) "net_amortized_cost"
   ```

1. click the **Run again** button and confirm that the query view updates successfully.  
![Inset show the run again button of the query window and the successful result](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/cust_runagain.png)

1. Under Views, locate **resource\_view**, Select the three dots to the right of the view and select **Show/edit query** from the context menu.

1. Find the line which ends with "unblended\_cost" , add the below snippet

   ```
   , "sum"("line_item_net_unblended_cost") "net_amortized_cost"
   , "sum"("reservation_net_effective_cost") "reservation_net_effective_cost"
   , "sum"("savings_plan_net_savings_plan_effective_cost") "savings_plan_net_effective_cost"
   ```

1. click the **Run again** button and confirm that the query view updates successfully.

1. Under Views, locate **hourly\_view**, Select the three dots to the right of the view and select **Show/edit query** from the context menu.

1. Find the line which ends with "unblended\_cost" , add the below snippet

   ```
   , "sum"("line_item_net_unblended_cost") "net_amortized_cost"
   , "sum"("reservation_net_effective_cost") "reservation_net_effective_cost"
   , "sum"("savings_plan_net_savings_plan_effective_cost") "savings_plan_net_effective_cost"
   ```

1. click the **Run again** button and confirm that the query view updates successfully.

### Step 2 of 3. Modify/Refresh DataSet in Amazon Quick Sight
<a name="step-2-of-3-modifyrefresh-dataset-in-amazon-quick-sight"></a>

Next the data set in Amazon Quick Sight needs to be refreshed in order to see the added fields and use them in your analysis and dashboard.

1. Navigate to Amazon Quick Sight in the console.  
![AWS Console search with results for Quick Sight](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/cust_navqs.png)

1. Select Datasets on the left side of the page.  
![Left navigation in Quick Sight with datasets option highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/cust_qs_ds.png)

1. Locate **summary\_view** in the list of datasets and click on the dataset.

1. Click on Edit Dataset under the **summary** tab in the top right of the page.  
![Quick Sight edit dataset button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/cust_editds.png)

1. Allow the dataset preview windows to load.

1. Click on **Save & Publish** button in the top right of the page. this will trigger a refresh of the dataset and import net\_amortized field  
![Save and Publish the dataset to trigger full refresh and import new columns](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_dataset_save_publish.png)

1. Repeat the steps to refresh **resource\_view** and **hourly\_view** dataset as well.

### Step 3 of 3. Create/Modify CUDOS Dashboard Analysis
<a name="step-3-of-3-createmodify-cudos-dashboard-analysis"></a>

After the dataset has been updated you can now add the net\_amortized cost to different visualizations. Here we will demonstrate how you can update the CUDOS dashboard to use the net\_amortized cost along with amortized\_cost

**Note**  
If you deploy an update to the CUDOS/CID dashboards with the `--recursive` option it will overwrite your Athena query view changes and published dashboard changes

1. First, we’ll need to [save the dashboard as an analysis](create-analysis.md) so we can make changes.

1. Open the CUDOS dashboard and select the save icon, selecting "save as" in the drop-down selection to save the dashboard as an analysis. ![Save Dashboard as an analysis](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_save_analysis.png) 

1. Open the saved analysis.

### Step 3a. Create a parameter and control
<a name="step-3a-create-a-parameter-and-control"></a>

We will create a new parameter and control/filter so we can switch between unblended cost and net\_amortized cost for all the visuals

1. Click on Insert → Add Parameter from the top left menu bar

![Top Menu Bar to insert paramater](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_top_menu_insert.png)


1. Enter a name: CostType for the parameter and enter the static default value : net amortized cost

1. Click create

![Create new parameter](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_createparameter.png)


1. In the parameter added window, select Control to create a new control and connect to the parameter.  
![options for added parameter](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_parameteradded.png)

1. Enter in a display name : Cost Type, and ensure "Dropdown" is the style.

1. Define specific values as displayed below  
![Add control for the parameter](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_AddControl.png)

1. Finally click the add button.

1. The control will be added to the sheet in your analysis.  
![CostType Control](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_control_options.png)

**Note**  
The control has to be re-added to each sheet in the analysis

### Step 3b. Bind this control to calculated fields in datasets
<a name="step-3b-bind-this-control-to-calculated-fields-in-datasets"></a>

Now that we’ve created the parameter and control we need to associate it with a few calculated fields in order to have an effect in our analysis visualizations.

1. Click on Dataset from the left navigation and select the dataset **hourly\_view**   
![Select Hourly view dataset](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_hourlyview_dataset.png)

1. Find the calculated column **amortized cost** and edit the calculated field as shown below and click on save

   ```
   ifelse(
   ({charge_type} = 'SavingsPlanCoveredUsage' and ${CostType} = 'amortized cost'), {savings_plan_effective_cost},
   ({charge_type} = 'SavingsPlanCoveredUsage' and ${CostType} = 'net amortized cost' ), {savings_plan_net_effective_cost},
   ({charge_type} = 'DiscountedUsage' and ${CostType} = 'amortized cost'), {reservation_effective_cost},
   ({charge_type} = 'DiscountedUsage' and ${CostType} = 'net amortized cost'), {reservation_net_effective_cost},
   ({charge_type} = 'Usage' and ${CostType} = 'amortized cost'), {unblended_cost},
   ({charge_type} = 'Usage' and ${CostType} = 'net amortized cost'), {net_amortized_cost},
   0
   )
   ```

    ![Edit calculated filed in hourly view](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_hourly_view_amortized_cost.png) 

1. Now select the dataset **resource\_view** and find the calculated field **amortized cost**. Make changes as shown below and save

   ```
   ifelse(
   ({charge_type} = 'SavingsPlanCoveredUsage' and ${CostType} = 'amortized cost'), {savings_plan_effective_cost},
   ({charge_type} = 'SavingsPlanCoveredUsage' and ${CostType} = 'net amortized cost' ), {savings_plan_net_effective_cost},
   ({charge_type} = 'DiscountedUsage' and ${CostType} = 'amortized cost'), {reservation_effective_cost},
   ({charge_type} = 'DiscountedUsage' and ${CostType} = 'net amortized cost'), {reservation_net_effective_cost},
   ({charge_type} = 'Usage' and ${CostType} = 'amortized cost'), {unblended_cost},
   ({charge_type} = 'Usage' and ${CostType} = 'net amortized cost'), {net_amortized_cost},
   0
   )
   ```

    ![Edit calculated filed in hourly view](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_hourly_view_amortized_cost.png) 

1. Find the calculated field **Workspace Total Resource Cost**, edit as shown below and click on Save

   ```
   sumOver(sum(Cost), [{Workspace ID}])
   ```

    ![Edit calculated filed in hourly view](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_resource_view_workspace_total_resource_cost.png) 

1. Find the calculated field **Workspace Average Cost**, edit as shown below and click on Save

   ```
   sum(Cost)/distinct_count({Workspace ID})
   ```

    ![Edit calculated filed in hourly view](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_resource_view_workspace_average_cost.png) 

1. Now Select the dataset **summary\_view** and find the calculated filed **Cost\_Amortized** . edit the calculated field as shown below and click on save

   ```
   ifelse(
   ${CostType}= 'amortized cost',{amortized_cost},
   ${CostType}= 'net amortized cost', {net_amortized_cost},
   NULL)
   ```

    ![Edit calculated filed in hourly view](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/net_Summary_view_cost_amortized.png) 

1. Publish the modified analysis as a new dashboard which now has option to switch between both unblended and net\_amortized cost.