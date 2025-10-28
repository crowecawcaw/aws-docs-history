# Delete a VPC Lattice service

To delete a VPC Lattice service, you must first delete all associations that the service might
have with any service network. If you delete a service, all resources related to the
service, such as the resource policy, auth policy, listeners, listener rules, and access
log subscriptions, are also deleted.

###### To delete a service using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose **Service**.
3. On the **Services** page, select the service that
   you want to delete, and then choose **Actions**,
   **Delete service**.
4. When prompted for confirmation, choose **Delete**.

###### To delete a service using the AWS CLI

Use the [delete-service](../../../cli/latest/reference/vpc-lattice/delete-service.md "../../../cli/latest/reference/vpc-lattice/delete-service.md") command.
