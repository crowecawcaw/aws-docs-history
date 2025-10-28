# Step 2: Connect Amazon AppFlow to an application

You can securely move your data between supported source and destination applications with a
connection in Amazon AppFlow. Connections store the configuration details and credentials necessary to
run flows without the need to repeatedly enter information. After you have an established connection
with an application, you can use that connection in new or existing flows.

###### Topics

- [Prerequisites](#flow-tutorial-connection-prerequisites "#flow-tutorial-connection-prerequisites")
- [Create a connection](#flow-tutorial-make-connection "#flow-tutorial-make-connection")
- [Additional resources](#tutorial-connection-additional-resources "#tutorial-connection-additional-resources")

## Prerequisites

Before you begin, complete the [tutorial
prerequisites](flow-tutorial.md#flow-tutorial-prerequisites "flow-tutorial.md#flow-tutorial-prerequisites").

## Create a connection between Amazon AppFlow and a SaaS application

If you want to create and run a flow, you must establish a connection with the software as a
service (SaaS). You can create this connection while you create the flow, or you can create the
connection separately. Here, you create a connection in Amazon AppFlow before you create the flow.

###### To create a connection with Salesforce

1. Open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. Expand the navigation pane on the left-hand side of the console page and choose **Connections**.
3. For **Connectors**, select **Salesforce**.
4. Choose **Create connection**.
5. Leave the default selections and enter a **Connection name**. For example, enter `my-salesforce-connection`.
6. Choose **Continue**.
7. If you're not already logged into Salesforce, Amazon AppFlow prompts you to log in.
8. Choose **Allow** to give Amazon AppFlow access to your Salesforce account.

###### To create a connection with other applications

- Go to the [Supported applications](app-specific.md "app-specific.md") page and select the
  application that you want to connect with. Follow the instructions for your selected
  application.

You now have a connection in the Amazon AppFlow console to your SaaS account. If you use the same
third-party application in both flows, you only need one connection.

## Additional resources

For more information on connections, see the following resources:

- [Managing
  connections](connections.md "connections.md") in the _Amazon AppFlow User Guide_.
- [Salesforce](salesforce.md "salesforce.md") in the _Amazon AppFlow User Guide_.
