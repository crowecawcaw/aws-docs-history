# Requesting a maximum concurrent sessions

increase in Amazon WorkSpaces Secure Browser

The _maximum concurrent sessions_ quota is the highest amount of users
that can be connected at the same time to a portal. If the service quota limit for maximum
concurrent sessions is not set appropriately, users may find that a session is not available
when they sign in. In addition to increasing this service quota, customers must also ensure that
their VPC and subnets have sufficient IP space to support the maximum concurrent
sessions.

To request a maximum concurrent session increase

1. Open the [Service Quotas page](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas") in your desired region.
2. Choose **Number of Maximum Concurrent Sessions per Portal** for the
   instance type you want to increase.
3. Choose **Request an increase at account level**.
4. Under **Increase quota value**, enter in the total amount that you want
   the quota to be.

###### Note

For large or urgent increases, go to your [Service Quotas
history page](https://us-east-1.console.aws.amazon.com/servicequotas/home/requests "https://us-east-1.console.aws.amazon.com/servicequotas/home/requests"), select the link in the status column of your request, link to your
support case, and add a reply with details about your use case and/or the urgency. This
information helps the service team prioritize requests and ensure sufficient capacity is
allocated for your account.
