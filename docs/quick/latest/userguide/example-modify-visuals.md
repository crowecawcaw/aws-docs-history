

# Tutorial: Modify Amazon Quick Sight visuals
<a name="example-modify-visuals"></a>

Use the following procedures to modify the visuals that you created using the procedures in [Tutorial: Create an Amazon Quick Sight analysis](example-create-an-analysis.md). 

## Modify the line chart visual
<a name="example-line-visual"></a>

Modify your line chart visual by making it show an additional measure by date, and also by changing the chart color.

**To modify your line chart visual**

1. In your analysis, select the line chart visual.

1. Add another measure to the visual.

   Select the **New visitors SEO** field in the **Fields list** pane. This measure is added to the **Value** field well, and the line chart updates with a line to represent it. The visual title also updates.

1. Change the color of the line used to represent the **Return visitors** measure.

   Choose the line on the chart that represents **Return visitors**. To do this, choose the end of the line, not the middle of the line. 

   Choose **Color Return visitors**, and then choose the red icon from the color selector.

1. Choose the **Date** field in the **X axis** field well, choose **Aggregate**, and then choose **Month**.

## Modify the scatter plot visual
<a name="example-scatter-plot-visual"></a>

Modify your scatter plot visual by changing the data granularity.

**To modify your scatter chart visual**

1. In the analysis, select the scatter plot visual.

1. Choose the **Group/Color** field well, choose **Aggregate**, and then choose **Month**.

   The scatter plot updates to show the measures by month, rather than by the default of by year.

## Modify both visuals by changing visual layout and adding a filter
<a name="example-both-visuals"></a>

Modify both visuals by changing visual size and location, and by adding a filter and applying it to both of them.

### Change the visual layout
<a name="example-both-visuals-layout"></a>

Modify both visuals by changing visual size and location.

**To modify both visuals**

1. In your analysis, select the line chart visual.

1. Choose the resize handle in the lower right corner of the visual and drag up and to the left, until the visual is half its former size both horizontally and vertically.

1. Repeat this procedure on the scatter plot visual.

1. Choose the move handle on the scatter plot visual, and drag it up to the right of the line chart visual so that they are side by side.

### Modify both visuals by adding a filter
<a name="example-both-visuals-filter"></a>

Modify both visuals by adding a filter and applying it to both of them.

**To add a filter to both visuals**

1. In the analysis, choose the scatter plot visual.

1. Choose **Insert** then **Add Filter** on the application bar.

1. Choose the **Date** field to filter on.

1. Select the new filter to expand it.

1. In the **Edit filter** pane, for **Condition**, choose the **After** comparison type.

1. Enter a start date value of 1/1/2014.

   Choose **Date**, choose **2014** for the year, **January** for the month, and then choose **1** on the calendar.

1. In the **Edit filter** pane, choose **Apply** to apply the filter to the visual.

   The filter is applied to the scatter plot visual. This is indicated with a filter icon on the visual drop-down menu.

1. Apply the filter to the line chart visual.

   In the **Filter** pane, choose the **Date** filter again and choose **Single visual**, and then choose **All visuals of this dataset**. 

   The filter is applied to the line chart visual as well.

## Next steps
<a name="example-next-step-visuals"></a>

Create a dashboard from your analysis by using the procedure in [Tutorial: Create an Amazon Quick Sight dashboard](example-create-a-dashboard.md).