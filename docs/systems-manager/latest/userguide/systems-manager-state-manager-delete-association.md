# Deleting

associations

Use the following procedure to delete an association by using the AWS Systems Manager
console.

###### To delete an association

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **State Manager**.
3. Select an association and then choose
   **Delete**.
   You can delete multiple associations in a single operation by running an
   automation from the AWS Systems Manager console. When you select multiple associations for
   deletion, State Manager launches the automation runbook start page with the
   association IDs entered as input parameter values.

###### To delete multiple associations in a single operation

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **State Manager**.
3. Select each association that you want to delete and then choose
   **Delete**.
4. (Optional) In the **Additional input parameters** area,
   select the Amazon Resource Name (ARN) for the _assume
   role_ that you want the automation to use while running. To
   create a new assume role, choose **Create**.
5. Choose **Submit**.
