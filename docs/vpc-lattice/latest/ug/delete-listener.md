# Delete a listener for your VPC Lattice service

You can delete a listener at any time. When you delete a listener, all its rules are
automatically deleted.

###### To delete a listener using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Services**.
3. Select the name of the service to open its details page.
4. On the **Routing** tab, choose **Delete
   listener**.
5. When prompted for confirmation, enter `confirm` and then
   choose **Delete**.

###### To delete a listener using the AWS CLI

Use the [delete-listener](../../../cli/latest/reference/vpc-lattice/delete-listener.md "../../../cli/latest/reference/vpc-lattice/delete-listener.md") command.
