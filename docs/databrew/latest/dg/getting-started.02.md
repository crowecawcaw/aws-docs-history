# Step 2: Summarize the data

In this step, you build a DataBrew recipe—a set of transformations that can be
applied to this dataset and others like it. When the recipe is complete, you publish it
so that it's available for use.

In the game of chess, players can be rated based on how well they perform against
other players. (For more information, see [https://en.wikipedia.org/wiki/Chess_rating_system](https://en.wikipedia.org/wiki/Chess_rating_system "https://en.wikipedia.org/wiki/Chess_rating_system")). For this tutorial, you
focus on only the games where both players were Class A, meaning that their ratings were
1800 or more.

###### To summarize the data

1.  On the transformation toolbar, choose **Filter**,
    **By Condition**, **Greater than or equal
    to**.
2.  Set these options as follows:

        * **Source column** - `white_rating`
        * **Filter condition** – Greater than or equal
         to 1800

    To see how the transform works, choose **Preview changes**.
    Then choose **Apply**.

3.  Repeat the previous step, but this time set **Source column**
    to `black_rating`. After you apply your changes, the sample data
    contains only those games where the players on each side (black and white) were
    Class A or above.
4.  Summarize the data to determine how many games were won by each side. To do
    this, on the transformation toolbar, choose **Group**.
5.  For the **Group** properties, do the following:
    1. In the first row, choose `winner` for **Column
       name**. Leave **Aggregate** set to
       **Group by**.
    2. In the second row, choose `victory_status` for the
       **Column name**. Leave
       **Aggregate** set to **Group
       by**.
    3. Choose **Add another column**.
    4. In the third row, choose `winner` for **Column
       name**. Set **Aggregate** to
       **Count**.
    5. For **Group type**, choose **Group as new
       table**. The preview pane shows you what the result will
       look like.
    6. Choose **Finish**.

6.  Choose **Publish** to save your work, at right on the recipe
    pane.
7.  For **Version Description**, enter **First version of
    my recipe**. Then choose **Publish**.
