

# Tutorial: Create an Amazon Quick Sight analysis
<a name="example-create-an-analysis"></a>

In the following short tutorial, you create an analysis, add a visual using AutoGraph, and add another visual by choosing a specific visual type. This procedure builds on the dataset that you create and prepare in [Tutorial: Create a prepared Amazon Quick Sight dataset](example-prepared-data-set.md).

## Create your analysis
<a name="example-create-the-analysis"></a>

Use the following procedure to create your analysis.

**To create your analysis**

1. On the Amazon Quick Sight homepage, choose **Analyses**.

1. Choose **Create analysis** and select the dataset to use.

## Create a visual by using AutoGraph
<a name="example-create-autograph-visual"></a>

Create a visual by using AutoGraph, which is selected by default.

On the analysis page, choose **Date** and **Return visitors** in the **Fields list** pane.

Amazon Quick Sight creates a line chart using this data.

## Create a scatter plot visual
<a name="example-create-scatter-plot-visual"></a>

Create a visual by choosing a visual type and dragging fields to the field wells.

**To create a scatter plot visual**

1. On the analysis page, choose **Insert** and then **Add visual** on the application bar. A new, blank visual is created, and AutoGraph is selected by default.

1. In the **Visual types** pane, choose the scatter plot icon.

1. Choose fields in the **Fields list** pane to add to the **Field wells** pane:
   + Choose **Desktop Uniques** to populate the **X axis** field well.
   + Choose **Mobile Uniques** to populate the **Y axis** field well. 
   + Choose **Date** to populate the **Group/Color** field well. 

   A scatter plot is created using these fields.

## Next steps
<a name="example-next-step-analysis"></a>

Modify the visuals in your analysis by using the procedure in [Tutorial: Modify Amazon Quick Sight visuals](example-modify-visuals.md).