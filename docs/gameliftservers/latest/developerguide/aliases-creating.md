# Create an Amazon GameLift Servers alias

This topic describes how to create an Amazon GameLift Servers alias for use with game session placement.

**To create an alias**

Use either the Amazon GameLift Servers console or the AWS Command Line Interface (AWS CLI) to create an alias.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), use the navigation pane to open the
**Aliases** page.

1. Choose **Create alias**.
2. Enter an alias **Name**. We recommend including
   meaningful characteristics in the alias name to help when viewing a list of
   aliases.
3. Enter an alias **Description** as needed.
4. Choose a **Routing strategy** for the alias.
   1. If you choose a **Simple** routing strategy, select a fleet ID from the list
      to associate with this alias. The list includes all fleets in
      eith currently selected AWS Region. You must create an alias
      in the same Region as the fleet.
   2. If you choose a **Terminal** routing strategy,
      enter a string value that you want Amazon GameLift Servers to return to a game client
      in response to a game session request. A request with a terminal alias
      throws an exception with the message embedded.

5. (Optional) Add **Tags** to the alias
   resource. Each tag consists of a key and an optional value,
   both of which you define. Assign tags to AWS resources
   that you want to categorize in useful ways, such as by
   purpose, owner, or environment. Choose **Add new
   tag** for each tag that you want to add.
6. When you're ready to deploy the new fleet, choose **Create**.

AWS CLI
Use the [`create-alias`](../../../cli/latest/reference/gamelift/create-alias.md "../../../cli/latest/reference/gamelift/create-alias.md") command to create an alias. .Amazon GameLift Servers
creates the alias resource in your current default AWS Region (or you can add
a --region tag to specify a different AWS Region).

At minimum, include an alias name and routing strategy. For a simple routing
strategy, specify the ID of a fleet in the same Region as the alias. For a
terminal routing strategy, provide a message string.
