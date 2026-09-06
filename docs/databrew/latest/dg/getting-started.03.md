

# Step 3: Add more transformations
<a name="getting-started.03"></a>

In this step, you add more transformations to your recipe and publish another version of it. To refine our example, we use the information that not all chess games result in a clear winner; some games are played to a draw. 

**To add more recipe transformations and republish**

1. From the transformation toolbar, choose **Filter**, **By Condition**, **Is not** to remove the games that were played to a draw.

1. Set these options as follows:
   + **Source column** - `victory_status`
   + **Filter condition** – Is not `draw`

   To add this transform to your recipe, choose **Apply**.

1. Change the data in `victory_status` so that it's more meaningful. To do this, from the transformation toolbar choose **Clean**, **Replace**, **Replace value or pattern**.

1. Set these options as follows:
   + **Source column** - `victory_status`
   + **Specify values to replace** – Value or pattern
   + **Value to be replaced** - `mate`
   + **Replace with value** - `checkmate`

   To add this transform to your recipe, choose **Apply**.

1. Repeat the previous step, but change `resign` to `other player resigned`.

1. Repeat the previous step, but change `outoftime` to `time ran out`.

1. Choose **Publish** to save your work, at right on the recipe pane. 