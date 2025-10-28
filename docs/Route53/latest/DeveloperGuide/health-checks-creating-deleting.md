# Creating, updating, and deleting

health checks

###### Important

If you're updating or deleting health checks that are associated with records,
review the tasks in [Updating or deleting health
checks when DNS failover is configured](health-checks-updating-deleting-tasks.md "health-checks-updating-deleting-tasks.md") before you
proceed.

This section covers the following topics related to managing Route 53 health checks:

1.  **Creating and updating health checks:**
    - Learn how to create and update health checks using the Route 53 console.
    - Understand the values you need to specify when creating or updating health checks, such as endpoint monitoring, protocol, IP address, domain name, and advanced configuration options.

2.  **Values displayed when creating a health check:**
    - Discover the values that the Route 53 console displays based on your input when creating a health check, such as the full URL or IP address and port.

3.  **Updating health checks for CloudWatch alarm changes:**
    - Find out how to update a health check when you change the settings of the associated CloudWatch alarm.

4.  **Deleting health checks:**
    - Follow the procedure to delete health checks by using the Route 53 console.

5.  **Updating or deleting health checks when DNS failover is configured:**
    - Learn the recommended tasks to perform when updating or deleting health checks associated with DNS records to ensure proper routing and failover configuration.

6.  **Configuring router and firewall rules:**

        * Understand how to configure your router and firewall rules to allow inbound traffic from Route 53 health checkers, ensuring successful health checks.

    By following the information provided in this section, you can effectively create, update,
    and delete Route 53 health checks, manage their configuration, and ensure proper integration with DNS failover and routing policies.

###### Topics

- [Creating and updating health checks](health-checks-creating.md "health-checks-creating.md")
- [Values that you specify when you
  create or update health checks](health-checks-creating-values.md "health-checks-creating-values.md")
- [Values that Amazon Route 53
  displays when you create a health check](health-checks-creating-values-displayed.md "health-checks-creating-values-displayed.md")
- [Updating health
  checks when you change CloudWatch alarm settings (health checks that monitor a CloudWatch
  alarm only)](health-checks-updating-cloudwatch-alarm-settings.md "health-checks-updating-cloudwatch-alarm-settings.md")
- [Disabling or enabling health checks](health-checks-disable.md "health-checks-disable.md")
- [Inverting health checks](health-checks-invert.md "health-checks-invert.md")
- [Deleting health checks](health-checks-deleting.md "health-checks-deleting.md")
- [Updating or deleting health
  checks when DNS failover is configured](health-checks-updating-deleting-tasks.md "health-checks-updating-deleting-tasks.md")
- [Configuring router and firewall
  rules for Amazon Route 53 health checks](dns-failover-router-firewall-rules.md "dns-failover-router-firewall-rules.md")
