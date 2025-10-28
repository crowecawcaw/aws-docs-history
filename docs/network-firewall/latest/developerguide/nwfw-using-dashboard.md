# Working with the firewall monitoring dashboard

The firewall monitoring dashboard provides multiple options for viewing key metrics about your firewall.
Review the guidance in this section to understand the dashboard's capabilities.

Dashboard performance and data availability depend on two main factors:

- The processing speed of CloudWatch and Athena in your respective AWS regions.
- Your logging configuration choices (such as log types enabled and logging destinations) affect both the available visualizations and the dashboard's performance.
  To analyze your network traffic using the dashboard:

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. In the **Firewalls** page, choose the name of the firewall that you want
   to edit. This takes you to the firewall's details page.
4. In the firewall's details page, choose the **Monitoring** tab.
5. Optionally, adjust the scope of data shown in the dashboards:
   - Enter a valid IP address to specify which source or destination IPs you want to analyze
   - Select a protocol to specify the kind of traffic you want to analyze
   - Use the scope selector to specify whether metrics reflect logged activity from the top 10, 50, or 100 domains
   - Use the time range selector to specify the period you want to analyze

###### Note

Changes to the time range will affect query costs. The scope selector (10/50/100 results) does not affect the cost of queries.

## Best practices

Review the following following best practices to optimize your use of the firewall monitoring dashboard:

- Configure both flow and alert logs for your firewall to gain access to all available visualizations.
- Use the time range selector or custom time range option to compare recent data against historical trends.
- Avoid incurring extra charges by limiting the amount of times you update page data.
  When the dashboard updates page data, Network Firewall queries your configured logging destinations to pull the latest metrics.
  Each query incurs an additional charge.

The dashboard will query your logging destinations when:

    + You make scope adjustments with the time range selectors.
    + You start a new browser session and navigate to **Monitoring** from Firewall Details.

Note that refreshing your browser window or navigating away from and back to the dashboard will clear any displayed data, requiring new queries to restore the view.

###### Note

Network Firewall queries logging destinations separately to fetch log data. If your firewall sends logs to both CloudWatch and Amazon S3, any update to
the dashboard page data will result in separate queries.
