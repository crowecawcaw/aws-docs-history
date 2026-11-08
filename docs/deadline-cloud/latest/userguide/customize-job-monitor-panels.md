

# Customize the panels in the job monitor
<a name="customize-job-monitor-panels"></a>

The **Job monitor** page is built from panels. The **Jobs**, **Steps**, and **Tasks** panels are shown by default. Other panels are available to add when you need them, and you can move and resize any panel so that the information you use most is where you want it.

The monitor saves your arrangement in your browser and restores it the next time you open the job monitor.

To try adding and moving panels with sample data, open the [demo job monitor](https://_demo.us-east-1.deadlinecloud.amazonaws.com/us-west-2/farms/farm-94d29d9475dd814529b87a52f20ff9cb/queues/queue-8df336a45cbed661f57da93efa5b14db?jobId=job-fd8b065107a2688ea8519a63f944f5f0&stepId=step-7ef06ab55a605912f88e1c7345f78c30&taskId=task-7ef06ab55a605912f88e1c7345f78c30-0&demo=moonrise).

The following panels are available to add:
+ **Logs** shows the Amazon CloudWatch logs for the selected task, so that you can read them without leaving the job monitor. For more information, see [View session and worker logs in Deadline Cloud](view-logs.md).
+ **Task outputs** shows the output files of the selected task and previews them, including 3D meshes and point clouds. For more information, see [Preview task outputs in the job monitor](preview-task-outputs.md).

**To add a panel**

1. Follow the steps in [View and manage job details in Deadline Cloud](view-a-job.md) to view a list of jobs.

1. Choose **Add panel**, the outlined tile that follows the last panel on the page. You can also choose **Add panel** from the actions menu at the top of the page.  
![The job monitor showing the Jobs, Steps, and Tasks panels, with an outlined Add panel tile at the end of the page.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-add-panel-tile.png)

1. In **Add a panel**, choose the panel that you want. The panel is added after the last panel on the page.  
![The Add a panel dialog box listing the Logs panel and the Task outputs panel, each with a thumbnail and a description of what the panel shows.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-add-panel-modal.png)

The **Add panel** tile appears only when panels remain to add. After the page shows every available panel, the tile no longer appears.

**To remove a panel**

1. In the header of the panel that you want to remove, choose the **Panel settings** icon.

1. Choose **Remove panel**.  
![The header of the Logs panel with the Panel settings menu open, showing the Remove panel item.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-remove-panel.png)

To move a panel, use its drag handle. To resize a panel, use its resize handle. With either handle, select the handle, press Space or Enter, use the arrow keys to move or resize the panel, and then press Space or Enter to confirm the change or Esc to discard it. You can also select and hold either handle to move or resize the panel.

To return the page to the panels and arrangement that it started with, choose **Reset to default layout** from the actions menu at the top of the page. Resetting discards your customizations, including any panel that you added that isn't shown by default.