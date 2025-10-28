# Renaming a Neptune DB Instance

You can rename an Amazon Neptune DB instance by using the AWS Management Console. Renaming a DB instance
can have far-reaching effects. The following is a list of things you should know before you
rename a DB instance.

- When you rename a DB instance, the endpoint for the DB instance changes because the URL
  includes the name you assigned to the DB instance. You should always redirect traffic from
  the old URL to the new one.
- When you rename a DB instance, the old DNS name that was used by the DB instance is
  immediately deleted, but it can remain cached for a few minutes. The new DNS name for the
  renamed DB instance becomes effective after about 10 minutes. The renamed DB instance is not
  available until the new name becomes effective.
- You can't use an existing DB instance name when you are renaming an instance.
- All read replicas that are associated with a DB instance remain associated with that instance
  after it is renamed. For example, suppose that you have a DB instance that serves your
  production database, and the instance has several associated read replicas. If you rename
  the DB instance and then replace it in the production environment with a DB snapshot, the DB
  instance that you renamed still has the read replicas associated with it.
- Metrics and events that are associated with the name of a DB instance are maintained if you
  reuse a DB instance name. For example, if you promote a read replica and rename it to be the
  name of the previous primary instance, the events and metrics that were associated with the
  primary instance are then associated with the renamed instance.
- DB instance tags remain with the DB instance, regardless of renaming.
- DB snapshots are retained for a renamed DB instance.

###### To rename a DB instance using the Neptune console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Databases**.
3. Choose the radio button next to the DB instance that you want to rename.
4. In the **Instance actions** menu, choose **Modify**.
5. Enter a new name in the **DB instance identifier** text box. Select
   **Apply immediately**, and then choose **Continue**.
6. Choose **Modify DB instance** to complete the change.
