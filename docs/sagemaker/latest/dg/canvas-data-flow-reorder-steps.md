# Reorder steps in your data flow

After adding steps to your data flow, you have the option to reorder steps instead of deleting
and re-adding them in the correct order. For example, you might decide to move a transform to impute
missing values before a step to format strings.

###### Note

You can’t change the order of certain step types, such as defining your data source, changing
data types, joining, concatenating, or splitting. Steps that can’t be reordered are grayed out in the
Canvas application UI.

To reorder your data flow steps, do the following:

1. While editing a data flow in Data Wrangler, choose the **Data** tab. A side panel
   called **Steps** lists your data flow steps in order.
2. Hover over a transform step and choose the **More options** icon (
   ![Vertical ellipsis icon representing a menu or more options.](images/studio/canvas/more-options-icon.png)
   ) next to that step.
3. From the context menu, choose **Reorder**.
4. Drag and drop your data flow steps into your desired order.
5. When you’ve finished, choose **Save**.
   Your data flow steps and graph should now reflect the changes you’ve made.
