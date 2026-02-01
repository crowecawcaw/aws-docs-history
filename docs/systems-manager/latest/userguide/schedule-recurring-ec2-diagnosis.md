• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Scheduling a recurring scan for

unmanaged EC2 instances

You can run an on-demand scan for Amazon EC2 instances in your account or organization
that Systems Manager isn't able to manage due to various configuration issues. You can also
schedule this scan to occur automatically on a regular schedule.

###### To schedule a recurring scan for unmanaged EC2 instances

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Diagnose and
   remediate**.
3. Choose the **Unmanaged EC2 instances issue** tab.
4. In the **Diagnose unmanaged EC2 instances** section, turn
   on **Schedule recurring diagnosis**.
5. For **Diagnostic frequency**, select whether to run the
   diagnosis once a day or once a week.
6. (Optional) For **Start time**, enter a time, in 24-hour
   format, for the diagnosis to begin. For example, for 8:15 PM, enter
   `20:15`.

The time you enter is for your current local time zone.

If you don't specify a time, the diagnostic scan runs immediately. Systems Manager
also schedules the scan to run in the future at the current time. If you
specify a time, Systems Manager waits to run the diagnostic scan at the specified
time. 7. Choose **Execute**. The diagnosis runs immediately, but
will also run on the schedule you have specified.
