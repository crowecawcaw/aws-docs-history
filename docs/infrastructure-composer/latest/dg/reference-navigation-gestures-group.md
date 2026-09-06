

# Group cards together on Infrastructure Composer's visual canvas
<a name="reference-navigation-gestures-group"></a>

This topic contains details on grouping enhanced component cards and standard component cards. Grouping cards helps you categorize and organize your resources without needing to think about the code or markup you need write.

## Grouping enhanced component cards
<a name="w2aac17c21b7"></a>

There are two ways to group enhanced component cards together:
+ While pressing **Shift**, select cards to group. Then, choose **Group** from the resource actions menu.
+ select a card you want in a group. From the menu that appears, select **Group**. This will create a group that you can drag and drop other cards into.

![Selecting multiple Lambda functions and grouping them together.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_ref_07.gif)


## Grouping a standard component card into another
<a name="using-composer-cards-group-standard-component"></a>

The following example shows one way a standard component card can be grouped into another card from the **Resource properties** panel:

![The Resource properties panel for a standard component card.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_cards_17.png)


In the **Resource configuration** field on the **Resource properties** panel, the `Role` has been referenced in the Lambda function. This results in the **Role** card being grouped into the **Function** card on the canvas.