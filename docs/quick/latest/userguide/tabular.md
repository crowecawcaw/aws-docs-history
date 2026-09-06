

# Using tables as visuals
<a name="tabular"></a>

Use a table visual to see a customized table view of your data. To create a table visual, choose at least one field of any data type. You can add as many columns as you need, up to 200. You can also add calculated columns.

Table visuals don't display a legend. You can hide or display the title on a table. You can also hide or display totals, and choose to show totals at the top or the bottom of the table. For more information, see [Analytics formatting per type in Quick](analytics-format-options.md). 

**To create a table visual**

1. Open Amazon Quick and choose **Analyses** on the navigation pane at left.

1. Choose one of the following:
   + To create a new analysis, choose **New analysis** at upper right. For more information, see [Starting an analysis in Quick Sight](creating-an-analysis.md). 
   + To use an existing analysis, choose the analysis that you want to edit.

1. Choose **Insert** from the file menu and then **Add Visual**.

1. At lower left, choose the table icon from **Visual types**.

1. On the **Fields** list pane, choose the fields that you want to use. If you want to add a calculated field, choose **Insert** on the file menu and then **Add Calculated Field**.

   To create a nonaggregated view of the data, add fields only to the **Value** field well. Doing this shows data without any aggregations. 

   To create an aggregated view of the data, choose the fields that you want to aggregate by, and then add them to the **Group by** field well.

**To show or hide columns on a table**

1. On your visual, choose the field that you want to hide, then choose **Hide column**.

1. To display hidden columns, choose any column, then choose **Show all hidden columns**.

**To transpose columns to rows and rows to columns**
+ Choose the transpose icon ( ![Icon showing arrows pointing outward from center, indicating expand or resize functionality.](http://docs.aws.amazon.com/quick/latest/userguide/images/transpose-icon.png)) near the top right of the visual. It has two arrows at a 90 degree angle.

**To vertically align columns**

1. On your visual, choose the **Format visual** icon ( ![Icon showing a house with an upward arrow and a menu button.](http://docs.aws.amazon.com/quick/latest/userguide/images/format-visual-icon.png)) near the top right of the visual.

1. In the **Properties** pane, choose **Table options**, and choose your table's vertical alignment.

**To wrap the text for headers**

1. On your visual, choose the **Format visual** icon ( ![](http://docs.aws.amazon.com/quick/latest/userguide/images/format-visual-icon.png)) near the top right of the visual.

1. In the **Properties** pane, choose **Table options**, and select **Wrap header text**.

**To rearrange columns in a table chart**

1. Open the analysis with the visual that you want to sort. Visuals pane will be open by default.

1. Do one of the following:
   + Drag and drop one or more fields in **Field wells** to rearrange their order.
   + Select a field directly in the table and choose the left or right arrow on **Move column**.