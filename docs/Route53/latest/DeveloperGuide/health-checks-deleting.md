# Deleting health checks

To disable health checks, perform the following procedure.

###### Note

If you're using AWS Cloud Map and you configured AWS Cloud Map to create a Route 53 health
check when you register an instance, you can't use the Route 53 console to delete
the health check. The health check is deleted automatically when you deregister
the instance. There can be a delay of several hours before the health check no
longer appears in the Route 53 console.

###### Note

We're updating the health checks console for Route 53. During the transition period, you can continue
to use the old console.

Choose the tab for the console you are using.

- [New console](#health-checks-deleting-new "#health-checks-deleting-new")
- [Old console](#health-checks-deleting-old "#health-checks-deleting-old")

New console

###### To delete a health check

1. If you're deleting health checks that are associated with records, perform
   the recommended tasks in [Updating or deleting health
   checks when DNS failover is configured](health-checks-updating-deleting-tasks.md "health-checks-updating-deleting-tasks.md").
2. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
3. In the navigation pane, choose **Health checks**.
4. Select the linked ID of the health check that you want to delete.
5. Choose **Delete**.
6. Enter `confirm` in the text box and then choose **Delete**.

Old console

###### To delete a health check

(console)

1. If you're deleting health checks that are associated with records, perform
   the recommended tasks in [Updating or deleting health
   checks when DNS failover is configured](health-checks-updating-deleting-tasks.md "health-checks-updating-deleting-tasks.md").
2. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
3. In the navigation pane, choose **Health Checks**.
4. In the right pane, select the health check that you want to delete.
5. Choose **Delete Health Check**.
6. Choose **Yes, Delete** to confirm.
