# Manage Applications Associated to an Elastic Fleet in Amazon AppStream 2.0

You can associate and disassociate applications from an Elastic fleet at any time.
Changes to the applications associated to an Elastic fleet are visible to users
currently streaming from the fleet, but may not take effect. For example, if you
disassociate an application from a fleet, it will be removed from the application
catalog, but the virtual hard disk will remain mounted to existing streaming
sessions.

###### To manage applications associated to an Elastic fleet

1. Open the [AppStream 2.0
   console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md").
2. In the left navigation pane, choose **Fleets**, then either
   select the name of the fleet, or select the fleet radio button, then choose
   **View details**.
3. To associate a new application to the fleet, choose
   **Associate** in **Assigned
   applications**, select the application to be associated, and choose
   **Associate**.
4. To disassociate an existing application from the fleet, select the application
   to disassociate, choose **Disassociate**, and confirm that you
   want to disassociate the selected application by choosing
   **Disassociate**.
