# Viewing jobs in the Amazon EMR console

Job run data is avilable to view, so you can monitor each job as it passes through the states. To view
jobs in the Amazon EMR console, perform the following steps.

1. In the Amazon EMR console lefthand menu, under Amazon EMR on EKS, choose **Virtual
   clusters**.
2. From the list of virtual clusters, select the virtual cluster for which you want to
   view jobs.
3. On the **Job runs** table, select **View logs** to
   view the details of a job run.

###### Note

Support for the one-click experience is enabled by default. It can be turned off by
setting `persistentAppUI` to `DISABLED` in
`monitoringConfiguration` during job submission. For more information, see
[View Persistent Application User Interfaces](../ManagementGuide/app-history-spark-UI.md "../ManagementGuide/app-history-spark-UI.md").
