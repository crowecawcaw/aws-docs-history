# Delete an Direct Connect endpoint LAG

If you no longer need LAGs, you can delete them. You cannot delete a LAG if it has virtual
interfaces associated with it. You must first delete the virtual interfaces, or
associate them with a different LAG or connection. Deleting a LAG does not delete the
connections in the LAG; you must delete the connections yourself. For more information,
see [Delete a connection](deleteconnection.md "deleteconnection.md").

You can delete a LAG using either the Direct Connect console or using the command line or API.

###### To delete a LAG

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **LAGs**.
3. Select the LAGs, and then choose **Delete**.
4. In the confirmation dialog box, choose **Delete**.

###### To delete a LAG using the command line or API

- [delete-lag](../../../cli/latest/reference/directconnect/delete-lag.md "../../../cli/latest/reference/directconnect/delete-lag.md")
  (AWS CLI)
- [DeleteLag](../APIReference/API_DeleteLag.md "../APIReference/API_DeleteLag.md") (Direct Connect
  API)
