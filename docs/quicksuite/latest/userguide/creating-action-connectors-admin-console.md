# Creating AWS service action

connectors using the admin console

Action connectors enable you to integrate AWS services with your automation workflows.
You can create these connectors through the Amazon Quick Suite admin console, which provides a
user-friendly interface for configuring and managing connector permissions.

This procedure describes how to create first-party (AWS) action connectors that can be used in Amazon Quick Automate workflows to perform actions on AWS resources.

## Prerequisites

Before you create action connectors, ensure that you have the following:

- Administrative access to your Amazon Quick Suite account
- An IAM role with the necessary permissions for the connector you want to create
- Access to the Amazon Quick Suite admin console

###### Note

For information about creating customer IAM roles with AWS service permissions, see the Amazon Quick Automate documentation for creating AWS action connectors.

## Accessing the admin console

To create action connectors, you need to access the Amazon Quick Suite admin console.

1. Sign in to the AWS using your administrative credentials.
2. Navigate to the Amazon Quick Suite service.
3. In the Amazon Quick Suite console, choose `Admin` to access the admin console.
4. In the left navigation pane, choose `Permissions`.
5. Choose `AWS action connectors` to view the action connectors page.

## Creating a new action connector

After accessing the action connectors page, you can create a new connector.

1. On the action connectors page, choose `New action` in the upper right corner.
2. Select the first-party connector type that you want to create from the available options.
3. Fill in the connector details:
   1. Provide a descriptive name for your connector.
   2. In the connection details section, enter the `Role ARN` for the IAM role that grants the connector permissions to perform actions on resources.
   3. Configure any additional settings specific to the connector type you selected.

4. Configure sharing permissions for the connector:
   1. Choose `Share` to add users or groups who can access the connector.
   2. Select the appropriate permission level:
      - **Owner** - Grants full permissions to share, edit, and delete the connector. Recommended if you are granting the connector to your own user account.
      - **User** - Grants permission to use the connector in automation workflows.

   3. Choose `Add` to apply the sharing settings.

5. Review your configuration and choose `Create` to create the connector.
6. Verify that the new connector appears in the list of actions on the admin console page.

## Using the new connector in Amazon Quick Suite

After creating the action connector, you can use it in Amazon Quick Suite automation workflows.

1. In a new browser tab, sign in to Amazon Quick Suite as a regular user using the same account that you used for the admin console.
2. In the left navigation pane, choose `Add Connections`, then choose `Actions`.
3. Verify that you can see the newly created action connector in the list.

###### Note

If you have Owner permissions, you can also view, edit, share, and delete the connector from this interface. 4. To use the connector in an automation:

    1. Add the connector to an Automation Group.
    2. Create an automation that uses the connector's capabilities.
    3. Verify that the connector can be attached to the Automation Group and used in the workflow.

## Next steps

After creating your action connector, you can:

- Create automation workflows that use the connector to perform actions on AWS resources
- Share the connector with additional users or groups as needed
- Monitor the connector's usage and performance through the admin console
- Update the connector's configuration or permissions as requirements change
