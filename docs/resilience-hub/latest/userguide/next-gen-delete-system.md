# Delete a system

A system cannot be deleted while it has service associations. When you delete a system using the console, it automatically removes the service associations for you. When using the AWS CLI, you must remove all service associations first, then delete the system.

###### To delete a system (console)

1. Open the Next generation Resilience Hub console.
2. In the navigation pane, choose **Systems**.
3. Select the system you want to delete.
4. Choose **Actions**, then choose **Delete**.
5. In the confirmation dialog, select the deletion acknowledgement checkbox and choose
   **Delete**.

###### To delete a system (AWS CLI)

- Run the following command:

```

aws resiliencehubv2 delete-system \
  --system-arn "arn:aws:resiliencehub:`region`:`account-id`:system/`system-name`:`id`"

```
