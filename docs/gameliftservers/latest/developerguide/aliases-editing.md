# Edit an alias

You can edit an alias using the Amazon GameLift Servers console or with the AWS CLI command [update-alias](../../../cli/latest/reference/gamelift/update-alias.md "../../../cli/latest/reference/gamelift/update-alias.md").

This topic describes how to edit an Amazon GameLift Servers alias for use with game session placement. You can make the following edits:

**To edit an alias**

Use either the Amazon GameLift Servers console or the AWS Command Line Interface (AWS CLI) to edit an alias.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), use the navigation pane to open the
**Aliases** page.

1. Select the alias you want to edit and choose
   **Edit**. If you don't see the alias you want to edit,
   check your currently selected AWS Region.
2. On the **Edit alias** page, you can make the
   following edits:
   - Change the alias name.
   - Change the alias description.
   - Change the routing strategy from simple to terminal, or from
     terminal to simple.
   - For an alias with a simple routing strategy, change the fleet
     ID the alias is associated with.
   - For an alias with a terminal routing strategy, change the
     message text.

3. Choose **Save changes**. When updating the fleet ID
   for an alias with a simple routing strategy, it may take up to 2 minutes
   for the transition to complete. During this time, new game session
   placements might take place on the old fleet.

AWS CLI
Use the [`update-alias`](../../../cli/latest/reference/gamelift/update-alias.md "../../../cli/latest/reference/gamelift/update-alias.md") command to make changes to an alias resource.
You can update an alias resource in your current default AWS Region, or you can add
a `--region` tag to specify a different AWS Region.

You can change the following properties:

- Alias name.
- Alias description.
- Routing strategy type. Be sure to provide a fleet ID or a message string for the new routing strategy.
- Fleet ID for an existing simple routing strategy. The fleet ID must be in the same region as the alias.
- Message string for an existing terminal routing strategy.
