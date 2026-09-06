

# Filtering Visuals by Cost Allocation Tags
<a name="filtering-visuals-by-cost-allocation"></a>

## DEPRECATED
<a name="deprecated"></a>

This content is DEPRECATED. Please use [Organizational Taxonomy Guide](add-org-taxonomy.md).

## Last Updated
<a name="last-updated"></a>

August 2023

## Introduction
<a name="introduction"></a>

Now that you’ve added your cost allocation tags, follow this video tutorial to learn how to add a control or filter across your entire dashboard so you can see everything grouped by tags.

[![AWS Videos](http://img.youtube.com/vi/7lTH-XzPfHc?rel=0/0.jpg)](http://www.youtube.com/watch?v=7lTH-XzPfHc?rel=0)


## Prerequisites
<a name="prerequisites"></a>

For this solution you must have the following:
+ Ability to save and publish dashboards in Amazon Quick Sight

## Step 1 create a parameter and control
<a name="step-1-create-a-parameter-and-control"></a>

1. Select the dashboard you would like to customize and save it as an analysis.

1. In the analysis, select parameters from the left navigation.

1. Click the plus icon next to the Parameters header to create a new parameter.

1. Enter a name for the parameter and click the multiple values radio selection.

**Note**  
The parameter name is not a viewable or friendly name for the parameter that will be displayed on the analysis or dashboard.

1. Click create.

1. Next select control to connect your parameter.

1. Enter in a display name, and ensure "Dropdown multiselect" is the style.

1. Click the "Link to a dataset field" radio selection.

1. Select the dataset from the down selection, then select a field from that dataset.

1. Finally click the add button.

1. The control will be added to your analysis.

## Step 2 bind that control to a filter
<a name="step-2-bind-that-control-to-a-filter"></a>

Now that we’ve created the parameter and control we need to associate it with a filter in order to have an effect in our analysis visualizations.

1. Click on Filter from the left navigation.

1. Click the plus icon next to the Filters heading.

1. Search for the field that you created the parameter against.

1. Click on that field to add it as a parameter.

1. Click on that filter to edit.

1. Change the filter type to "custom filter" 

1. Click the check box to use parameters.

1. A dialog to change the scope of the filter will pop up. Click yes to change the scope to all visuals that use the dataset.

1. Select the parameter you created from the drop down list of parameters and select apply.

1. You will now see that changing the selection of the control changes the associated visuals on that sheet.

**Note**  
To apply this to all sheets in your analysis, repeat these steps on each sheet of your analysis.

## Step 3 Publish your analysis
<a name="step-3-publish-your-analysis"></a>

Now that you have customized your analysis, you can publish that analysis as a dashboard to share with other users to allow them to leverage additional fields for filtering.

## Additional information
<a name="additional-information"></a>
+  [Amazon Quick Sight parameter documentation](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) 
+  [Using dataset parameters in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/dataset-parameters.html) 