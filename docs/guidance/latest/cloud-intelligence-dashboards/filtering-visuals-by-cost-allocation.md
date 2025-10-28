# Filtering Visuals by Cost Allocation Tags

## DEPRECATED

This content is DEPRECATED. Please use [Organizational Taxonomy Guide](add-org-taxonomy.md "add-org-taxonomy.md").

## Last Updated

August 2023

## Introduction

Now that you’ve added your cost allocation tags, follow this video
tutorial to learn how to add a control or filter across your entire
dashboard so you can see everything grouped by tags.

## Prerequisites

For this solution you must have the following:

- Ability to save and publish dashboards in Amazon QuickSight

## Step 1 create a parameter and control

1. Select the dashboard you would like to customize and save it as an analysis.
2. In the analysis, select parameters from the left navigation.
3. Click the plus icon next to the Parameters header to create a new parameter.
4. Enter a name for the parameter and click the multiple values radio selection.

###### Note

The parameter name is not a viewable or friendly name for the
parameter that will be displayed on the analysis or dashboard.

1. Click create.
2. Next select control to connect your parameter.
3. Enter in a display name, and ensure "Dropdown multiselect" is the style.
4. Click the "Link to a dataset field" radio selection.
5. Select the dataset from the down selection, then select a field from that dataset.
6. Finally click the add button.
7. The control will be added to your analysis.

## Step 2 bind that control to a filter

Now that we’ve created the parameter and control we need to associate it
with a filter in order to have an effect in our analysis visualizations.

1. Click on Filter from the left navigation.
2. Click the plus icon next to the Filters heading.
3. Search for the field that you created the parameter against.
4. Click on that field to add it as a parameter.
5. Click on that filter to edit.
6. Change the filter type to "custom filter"
7. Click the check box to use parameters.
8. A dialog to change the scope of the filter will pop up. Click yes to change the scope to all visuals that use the dataset.
9. Select the parameter you created from the drop down list of parameters and select apply.
10. You will now see that changing the selection of the control changes the associated visuals on that sheet.

###### Note

To apply this to all sheets in you analysis, repeat these steps on each sheet of your analysis.

## Step 3 Publish your analysis

Now that you have customized your analysis, you can publish that
analysis as a dashboard to share with other users to allow them to
leveraged additional fields for filtering.

## Additional information

- [Amazon
  QuickSight parameter documentation](../../../quicksight/latest/user/parameters-in-quicksight.md "../../../quicksight/latest/user/parameters-in-quicksight.md")
- [Using
  dataset parameters in Amazon QuickSight](../../../quicksight/latest/user/dataset-parameters.md "../../../quicksight/latest/user/dataset-parameters.md")
