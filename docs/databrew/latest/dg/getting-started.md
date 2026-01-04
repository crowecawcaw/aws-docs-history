# Step 4: Review your DataBrew resources

Now that you worked with a sample project, review the DataBrew resources you created so
far.

###### To review your DataBrew resources

1. On the navigation pane, choose **Datasets**.

When you created the sample project, DataBrew created a dataset for you
(`chess-games`). The source data file is stored in Amazon S3, and is
in Microsoft Excel format (`chess-games.xlsx`). The file contains
metadata from over 20,000 games of chess. The `chess-games` dataset
provides the information that DataBrew needs to read the data in that file. 2. On the navigation pane, choose **Projects**.

You should see the project that you worked with in the previous steps
(`chess-project`). Every project requires a dataset, in this
case `chess-games`. Every project also requires a recipe, so that you
can add data transformation steps as you go along. When you created this sample
project, DataBrew created a new (empty) recipe for you, and attached it to the
project. 3. On the navigation pane, choose **Recipes**, and in the
**Recipe name** column, choose
**chess-project-recipe**. This shows you the recipe that DataBrew created for your
project, and that you've refined by adding transformation steps to it. 4. At left, view the recipe versions that have been published. Choose one of
these to view its **Recipe steps** tab, which shows the recipe
details and steps for that version. 5. View the **Data lineage** tab, which shows where the data
came from and how it's being used. For more details, choose any of the icons in
the diagram.
