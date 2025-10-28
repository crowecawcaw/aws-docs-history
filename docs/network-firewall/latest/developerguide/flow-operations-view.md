# Viewing flow operations in Network Firewall

You can view the history of operations in your firewall and monitor the progress of ongoing operations.
Network Firewall only stores capture and flush operations performed within the last 12 hours.

###### To view operation history

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. Choose the name of the firewall that you want to view.
4. Navigate to the **Firewall operation history** section.
5. Review the status of operations:

**In progress**
Operations that have not yet completed.

**Completed**
Operations that successfully completed.

**Failed**
Operations that could not be completed.

**Completed with errors**
Operations that experienced a timeout issue or an issue that prevented
completion across all hosts. These operations may have flows missing from the results. 6. Choose any completed operation to view the summary of results.
