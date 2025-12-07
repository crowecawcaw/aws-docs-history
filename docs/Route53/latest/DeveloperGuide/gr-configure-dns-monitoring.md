# Configure DNS monitoring and logging with

Route 53 Global Resolver

Configure DNS monitoring in Route 53 Global Resolver to capture detailed information about DNS queries,
responses, and security actions. This section covers the steps to set up logging destinations
and configure monitoring tools.

## Setting the observability Region

Before configuring DNS logging, you must set an observability Region where logs and
metrics will be stored. This region determines where your monitoring data is processed and
stored.

1. Open the Route 53 Global Resolver console at [https://console.aws.amazon.com/route53globalresolver/](https://console.aws.amazon.com/route53globalresolver/ "https://console.aws.amazon.com/route53globalresolver/").
2. In the navigation pane, choose **Settings**.
3. In the **Observability region** section, choose
   **Set region**.
4. Select the AWS Region where you want to store monitoring data, then choose
   **Set region**.

After setting the observability region, you can configure log delivery destinations in
that region.
