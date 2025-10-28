# Enabling IAM database authentication in

Amazon Neptune

By default, IAM database authentication is disabled when you create an Amazon Neptune DB
cluster. You can enable IAM database authentication (or disable it again) using the
AWS Management Console.

To create a new Neptune DB cluster with IAM authentication by using the console,
follow the instructions for creating a Neptune DB cluster in [Launching a Neptune DB cluster using the AWS Management Console](manage-console-launch-console.md "manage-console-launch-console.md").

On the second page of the creation process, for **Enable IAM DB
Authentication**, choose **Yes**.

###### To enable or disable IAM authentication for an existing DB instance or cluster

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Clusters**.
3. Choose the Neptune DB cluster that you want to modify, and choose **Cluster
   actions**. Then choose **Modify cluster**.
4. In the **Database options** section, for **IAM DB
   Authentication**, choose either **Enable IAM DB
   authorization** or **No** (to disable). Then choose
   **Continue**.
5. To apply the changes immediately, choose **Apply
   immediately**.
6. Choose **Modify cluster**.
