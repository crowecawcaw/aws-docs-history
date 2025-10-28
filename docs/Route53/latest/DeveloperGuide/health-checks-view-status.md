# Viewing health check status and the reason for health check failures

On the Route 53 console, you can view the status (healthy or unhealthy) of your health checks as reported by Route 53 health checkers.
For all health checks except calculated health checks, you can also view the reason for the last health check failure,
for example, health checkers were unable to establish a connection with the endpoint.

###### Note

We're updating the health checks console for Route 53. During the transition period, you can continue
to use the old console.

Choose the tab for the console you are using.

- [New console](#health-checks-view-status-new "#health-checks-view-status-new")
- [Old console](#health-checks-view-status-old "#health-checks-view-status-old")

New console

###### To view the status and last failure reason for a health check

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Health checks**.
3. For an overview of the status of all of your health checks—healthy or unhealthy—view the
   **Status** column. For more information, see
   [How Amazon Route 53 determines
   whether a health check is healthy](dns-failover-determining-health-of-endpoints.md "dns-failover-determining-health-of-endpoints.md").
4. For all health checks except calculated health checks, you can view the status of the Route 53 health checkers that
   are checking the health of a specified endpoint.
5. Choose the linked ID of the health check you want to view details for.
6. In the bottom pane, choose the **Health checkers** tab.

###### Note

New health checks must propagate to Route 53 health checkers before the health check status and last failure reason
appear in the **Status** column. Until propagation has finished, the message in that column
explains that no status is available. 7. The table
includes the following values:

**Health checker IP**
The IP address of the Route 53 health checker that performed the health check.

**Last checked**
The date and time of the health check or the date and time of the last failure.

**Status**
Either the current status of the health check or the reason for the last health check failure.

Old console

###### To view the status and last failure reason for a health check

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Health Checks**.
3. For an overview of the status of all of your health checks—healthy or unhealthy—view the
   **Status** column. For more information, see
   [How Amazon Route 53 determines
   whether a health check is healthy](dns-failover-determining-health-of-endpoints.md "dns-failover-determining-health-of-endpoints.md").
4. For all health checks except calculated health checks, you can view the status of the Route 53 health checkers that
   are checking the health of a specified endpoint. Select the health check.
5. In the bottom pane, choose the **Health Checkers** tab.

###### Note

New health checks must propagate to Route 53 health checkers before the health check status and last failure reason
appear in the **Status** column. Until propagation has finished, the message in that column
explains that no status is available. 6. Choose whether you want to view the current status of the health check, or view the date and time of the
last failure and the reason for the failure. The table on the **Status** tab
includes the following values:

**Health checker IP**
The IP address of the Route 53 health checker that performed the health check.

**Last checked**
The date and time of the health check or the date and time of the last failure, depending
on the option that you select at the top of the **Status** tab.

**Status**
Either the current status of the health check or the reason for the last health check failure, depending
on the option that you select at the top of the **Status** tab.
