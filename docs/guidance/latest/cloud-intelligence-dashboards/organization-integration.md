

# Organization (OU) integration
<a name="organization-integration"></a>

This content is DEPRECATED. Please use [Organizational Taxonomy Guide](add-org-taxonomy.md).

## Introduction
<a name="introduction"></a>

Attribution of cost and operational data to Business Units, Divisions, Projects, or Teams is an important phase. This can attribute ownership of assets and actions and follow up in scale.

If you use AWS Organizations, and your Organizational Units are aligned with your actual organizational structure, you probably would like to incorporate Organizational Units(OU) information into your Cloud Intelligence Dashboards, creating filters, views and visualizations of cost and usage based on your AWS Organizations structure. This customization will guide you through this process.

Using this guide you will be able to extend your various CID dashboards with AWS organization, such as:
+ OU Names (can be from multiple levels of OU structure)
+ OU and Account Tags - These tags that are applied on AWS Account or AWS Organization OU. Please note these are not the same Cost Allocation Tags that can work on resource level.
+ Hierarchical Tags - The tags that can be defined on OU level and propagate to account level (More specific tags override less specific).
+ Management Account names (or nicknames).

![Architecture](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/ou-integration-architecture.png)


You also can leverage the OU information for your Row Level Security.

## Prerequisites
<a name="prerequisites"></a>

For this solution you must have the following:
+ Deployed the [Data Collection Stack](data-collection.md) with the **AWS Organizations** module deployed.
+ Permissions to create and update Athena views.
+ Permissions to update Quick Sight Cloud Intelligence dashboard (CID) datasets

## Step by Step Guide
<a name="step-by-step-guide"></a>

This guide assumes you have enabled the [Data Collection Stack](data-collection.md) with the **AWS Organizations** module deployed. There are two methods of incorporating organization data into your CID dashboards. The first covers creating a dedicated view and add the data into Quick Sight. The other covers updating the `account_map` that is already used in most of CID datasets.

Method 2 is the recommended way to make this change.

Regardless of the path of customization, the last section provides how to customize the dashboards in 3 ways: filters, controls and views.

## Method 1 - Updating Quick Sight dataset schema
<a name="method-1-updating-quick-sight-dataset-schema"></a>

### Step 1. Create View in Athena
<a name="step-1-create-view-in-athena"></a>

You will need to create a new view `organization_map`.

#### Click here to expand step by step instructions
<a name="collapsible-section-id-organization-integration-1"></a>

1. Open the console and navigate to Athena.

1. Select the AwsDataCatalog data source and `cid_data` database (Please note that in older versions of [Data Collection Stack](data-collection.md) the name of data base was `optimization_data` and you will need to adapt SQL accordingly).

1. Confirm that you have the table, organization\_data and there is data in that table.

1. Create the following view:

```
CREATE OR REPLACE VIEW "organization_map" AS
SELECT "id" "account_id"
, "name" "account_name"
, "parent" "OU"
, "parentid" "OU_ID"
, "payer_id" "payer_org_account_id"
, "managementaccountid" "management_account_id"
FROM cid_data.organization_data
```

1. After creating the view, execute a query against the view and confirm you are getting the correct data:

```
SELECT *
FROM "organization_map" limit 10;
```

1. Move to the next step.

### Step 2. Modify Data Set in Amazon Quick Sight
<a name="step-2-modify-data-set-in-amazon-quick-sight"></a>

Next the data set in Amazon Quick Sight needs to be updated so that you can see the added fields to use them in your Dashboards and Analyses.

#### Click here to expand step by step instructions
<a name="collapsible-section-id-organization-integration-2"></a>

1. Navigate to Quick Sight in the console.

1. Select Datasets, and then select `summary_view` from the list of datasets.  
![Quick Sight dataset screen with the datasets navigation item and summary view dataset highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-01.png)

1. Click on EDIT DATASET.  
![Summary view summary page with edit dataset button highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-02.png)

1. Click on Add data.  
![Quick Sight edit dataset page with add data button highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-03.png)

1. Make the following selections:
   + Select DataSource from the first drop down.
   + Next select the same DataSource that issued for `summary_view`.
   + Leave the Catalog as AwsDataCatalog.
   + Select cid\_data as the database.  
![Add data dialog with all selections displayed](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-04.png)
   + Search for the view `organization_map`, check the box.

1. Click Select.

1. Select the join between **summary\_view** and **organization\_map**.

1. Ensure the join type is set to left.  
![Join configuration dialog showing the join clause details](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-05.png)

1. Set the join clause to be; *linked\_account\_id = account\_id*.

1. Click Apply.

1. Save and Publish the dataset.  
![Quick Sight dataset designer showing the summary view dataset with the save and publish button highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-06.png)

1. Now you can do the same for all other datasets (hourly\_view, resource\_view and others).

1. Once the dataset finishes loading successfully, you will then be able to incorporate payer account name in your dashboards, analysis to visuals, controls or filters.

## Method 2- Incorporating organization data into account\_map
<a name="method-2-incorporating-organization-data-into-account_map"></a>

### Step 1. Modify View in Athena
<a name="step-1-modify-view-in-athena"></a>

This method demonstrates how to modify the account map view query to include the data from the organization data directly. This requires you to replace the account map view.

**Note**  
When updating any view that is part of the cloud intelligence or data collection deployments you should create a copy of the original view so that you can rollback a change. This view could be overwritten by a future deployment or forced update of these views. You should have a backup copy of your customizations of view to be able to place them back if this happens.

#### Click here to expand step by step instructions
<a name="collapsible-section-id-organization-integration-3"></a>

1. Navigate to Athena and the cur database.

1. Locate the `account_map` and click on the vertical ellipses next to the view and select *Show/edit query* from the context menu.

1. First, make a copy of the view as backup, naming the new view something like *account\_map\_original*.

1. Select the entire view and replace it with this query:

   ```
   CREATE OR REPLACE VIEW "account_map" AS
   SELECT DISTINCT
       id account_id
     , name account_name
     , managementaccountid parent_account_id
     , email account_email_id
     , parent "ou"
   FROM
     "cid_data"."organization_data"
   ```

   Please explore `organization_data` table for more options that you can use in the view above.

1. Click *Run* to execute the query and create the view.

1. Next, switch to Quick Sight, locate the `summary_view` dataset and edit that dataset.

1. Confirm you see the *OU* field in your schema.

1. Save and publish that dataset to have the schema updated and data reloaded.

1. Repeat these previous steps in Quick Sight for each dataset that has `account_map`. Ex: `hourly_view` and `resource_view` 

1. Then follow the section on dashboard customization to complete the customizations.

## Managing complex organization
<a name="managing-complex-organization"></a>

Some organizations can have a complex multi-level structure. In these cases we recommend adding multiple OU levels or leveraging [AWS Organization Tags](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html). You can define a set of Tags. Ex: `MyEnterprise`, `MyBusinessLine` and `MyBusinessUnit`.

You can set these tags on any level of OU and then redefine on lower level if needed. This gives you the flexibility and control in defining org structure. Tags can be also redefined on the level of Account.

Here is an advanced example that leverage OU Tags as well as mapping for Management Account Names that you can adjust to needs of your Organization.

### Click here to explore more advanced example of account\_map
<a name="collapsible-section-id-organization-integration-4"></a>

1. Navigate to Athena and the cur database (default: `cid_cur`).

1. Locate the `account_map` and click on the vertical ellipses (`⋮`) next to the view and select *Show/edit query* from the context menu.

1. First, make a copy of the view as backup, naming the new view something like *account\_map\_original*.

1. Select the entire view and replace it with this query adjusted to your needs:

```
CREATE OR REPLACE VIEW "account_map" AS
SELECT DISTINCT
    id account_id
  , name account_name
  , email account_email_id
  , ManagementAccountId parent_account_id
  , "parent" "OU" -- The Name of the lowest level OU of the Account

  -- A simple mapping of Management Account Ids to user-friendly names
  , CASE ManagementAccountId
     WHEN '111111111111' THEN 'My Management Org'
     WHEN '222222222222' THEN 'My Test Org'
     ELSE ManagementAccountId
  END parent_account_name

  -- Full path separated with '>'
  , HierarchyPath as ou_hierarchy

  -- Levels of OU hierarchy
  , TRY(hierarchy[1].name) ou_l1
  , TRY(hierarchy[2].name) ou_l2
  , TRY(hierarchy[3].name) ou_l3
  , TRY(hierarchy[4].name) ou_l4
  , TRY(hierarchy[5].name) ou_l5

  -- Hierarchical Tags
  , TRY(FILTER(HierarchyTags, (x) -> (x.key = 'MyEnterprise'))[1].value) as ou_tag_enterprise
  , TRY(FILTER(HierarchyTags, (x) -> (x.key = 'MyBusinessLine'))[1].value) as ou_tag_business_line
  , TRY(FILTER(HierarchyTags, (x) -> (x.key = 'MyBusinessUnit'))[1].value) as ou_tag_business_unit
FROM
  "cid_data"."organization_data"
```

1. Click `Run` to execute the query and create the view.

1. Next, switch to Quick Sight, locate the `summary_view` dataset and edit that dataset.

1. Save and publish that dataset to have the schema updated and data reloaded.

1. Repeat these previous steps in Quick Sight for each dataset that has `account_map`. Ex: `hourly_view` and `resource_view` 

1. Then follow the section on dashboard customization to complete the customizations.

## Dashboard Customization
<a name="dashboard-customization"></a>

**Note**  
By design your customized dashboards will not be overwritten by new releases of CUDOS dashboards. Best practice is to clearly name your customized dashboards a clear and unique name separate from the dashboards we deploy.

### Step 1. Modify Quick Sight Analysis - CUDOS Dashboard
<a name="step-1-modify-quick-sight-analysis-cudos-dashboard"></a>

After the dataset has been updated you can now add those fields to different visualizations. Here we will demonstrate how you can update the CUDOS dashboard to use the organization information in a visualization. We’ll save the dashboard as an analysis to make an update to "Invoiced Spend by Payer Account" visual on the "Executive: Billing Summary" sheet to instead reflect the same information by organization.

#### Click here to expand step by step instructions
<a name="collapsible-section-id-organization-integration-5"></a>

1. Open up Quick Sight.

1. Navigate Dashboards and select the CUDOS dashboard.

1. Save the dashboard as a new analysis named "cudos-out-customization".  
![Quick Sight save as dialog](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-07.png)

1. In that analysis, select the "Invoiced Spend by Payer Account" visual on the "Executive: Billing Summary" sheet.

1. Locate the "ou" field that was added in the field list for the *summary\_view* dataset.  
![Quick Sight analysis showing the field list](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-08.png)

1. Select that field.

1. Drag and drop that field in Visual details under the GROUP/COLOR FOR BARS section. Make sure the field is at the top of the fields listed there.  
![Group by fields list with ou field at the top and all other fields indented below it](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-09.png)

1. You will see the visual "Invoiced Spend by Payer Account" update to reflect the invoiced spend by organization instead of payer.  
![Invoiced spend visualization showing the group by data with ou](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-10.png)

1. Lets update the title of this visual. Double-click on the title of the visual.

1. Select the "${BillingSummaryGroupBy}" parameter and delete it. Replace it with *organization*.  
![Title edit dialog showing the completed title change](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-11.png)

1. Click Save.

1. You will now see the visual updated to reflect the title and data grouped by organization.  
![Invoice spend by organization bar chart visualization](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-12.png)

1. Continue with customizations of other visuals with organization as you need.

1. Publish the dashboard when you are done\!

### Step 2. (Optional) Add to CUDOS controls
<a name="step-2-optional-add-to-cudos-controls"></a>

The CUDOS dashboard comes with several controls across the sheet by default. You can add more controls to allow you to filter all the visuals on a sheet at once. Here we’ll show you how to add organization as a control.

#### Click here to expand step by step instructions
<a name="collapsible-section-id-organization-integration-6"></a>

1. Open up Quick Sight.

1. Navigate Dashboards and select the CUDOS dashboard.

1. Save the dashboard as a new analysis named "cudos-out-customization".

![Quick Sight save as dialog](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-07.png)


1. Click on *Insert* from the analysis menu and select *Add Parameter*.  
![Quick Sight insert menu dropdown showing add parameter](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-13.png)

1. Enter *organization* for the name, leave other settings to their default.  
![Create new parameter dialog](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-14.png)

1. Click Create.

1. Click on *Control*.  
![Parameter created dialog with control selection highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-15.png)

1. Make the following selections for the control configuration:
   + Name: **Organization** 
   + Style: **Dropdown** 
   + Values: **Link to dataset field** 
   + Dataset: **summary\_view** 
   + Field: **ou** 

1. Click *Add*.

1. You will see the *Organization* control added to the controls of the sheet.  
![Display of the controls on the sheet](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-16.png)

1. We need one more step for the control to work on the page.

1. Select a visual from the sheet and click on the `filters` icon from the analysis menu.

1. Click the \_ ADD\_ button under the **Filters** heading, search for the *ou* field to add it to the filters.  
![Add filters drop down with ou highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-17.png)

1. Click on the *ou* filter to edit it and make the following selections:
   + Filter type: **Custom filter** 
   + Filter condition: **equals** 
   + Use Parameters: **checked** 
   + Parameter: **organization** 

1. Click *APPLY*.  
![Edit filter dialog with ou and other selections made](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-18.png)

1. When you make a selection with the *Organization* control, all the visuals on the sheet should be updated to be filtered by that organization unit.

1. To add this control to other sheets in the analysis, follow these steps:

   1. Select the sheet you want to add the control.

   1. Click the parameters icon from the toolbar.

   1. Search for `organization` in the parameters search.

   1. Select the vertical ellipses (`⋮`) next to the parameter.

   1. Select `Add control` from the context menu.

   1. Set the values like previously:

   1. Name: **Organization** 

   1. Style: **Dropdown** 

   1. Values: **Link to dataset field** 

   1. Dataset: **summary\_view** 

   1. Field: **ou** 

   1. Click *Add*.

   1. Select a visual from the sheet and click on the *filters* icon from the analysis menu.

   1. Click the ` ADD` button under the **Filters** heading, search for the *ou* field to add it to the filters.

   1. Click on the `ou` filter to edit it and make the following selections:

      1. Filter type: **Custom filter** 

      1. Filter condition: **equals** 

      1. Use Parameters: **checked** 

      1. Parameter: **organization** 

   1. Click `APPLY`.

   1. Repeat these steps for each sheet you want to see this control.

1. You’ve now customized the dashboard to add a control that filters all applicable visuals on a sheet. You can now publish your dashboard.

### Step 3. (Optional) Modify OPTICS Explorer sheet
<a name="step-3-optional-modify-optics-explorer-sheet"></a>

The CUDOS dashboard has a sheet titled **OPTICS Explorer** which places controls on the sheet with a number of common visualizations to allow you to freely explore your CUR data or investigate different aspects of your data quickly. You can add *Organization* or any other control you would like, such as *tags* to add more flexibility to filter data on this sheet.

After adding the control, it will appear as a dropdown at the top of the sheet. Follow these steps to move the control to the sheet.

#### Click here to expand step by step instructions
<a name="collapsible-section-id-organization-integration-7"></a>

1. Follow the steps in the optional step for adding controls

1. Expand the control menu at the top of the sheet.

1. Select the `Organization` control.

1. Select the 3 vertical ellipses for the control.

1. Select `Move to sheet`.  
![Context dialog showing move to sheet option](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-19.png)

1. This will place the control at the very bottom of the sheet.

1. Select the control and drag the control up with the other controls.

1. You can edit the size the control and other controls to fit them in with the other controls.  
![OPTICS explorer sheet showing controls adjusted to include the organization control](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/out-integration/ou-integration-20.png)

## Summary
<a name="summary"></a>

We’ve shown you how you can customize your datasets, views and dashboards to include AWS Organization data.