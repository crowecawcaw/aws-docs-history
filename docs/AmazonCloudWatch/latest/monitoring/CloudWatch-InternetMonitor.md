# Pricing for Internet Monitor

With Internet Monitor, there are no upfront costs or long-term commitments. Pricing for Internet Monitor has two components: a per
monitored resource fee and a per city-network fee. A _city-network_ is the location where clients access your
application resources from and the network (ASN, such as an internet service provider or ISP) that clients access
the resources through. Note that you are also charged standard CloudWatch prices for logs and any additional
metrics, dashboards, alarms, or insights that you create.

You choose a percentage of traffic to monitor when you create a monitor. To help control your bill, you can also set a
limit for the maximum number of city-networks to monitor. You can update the percentage of traffic to monitor or the maximum
city-networks limit at any time by editing your monitor. The first 100 city-networks (across all monitors per account) are
included. After that, you only pay for the actual additional number of city-networks that you monitor, up to the maximum number.

You pay only the actual additional number of city-networks that you monitor, up to the maximum number, with no charge for the first
100 city-networks (across all monitors per account). A flat amount equivalent to the cost of 100 city-networks is
deducted from your monthly bill.

For example, a large global company could choose to monitor 100% of its internet-facing traffic, and set a city-networks
maximum of 50,000, for one monitor with one resource. Assuming the traffic reached 50,000 city-networks, that portion of its bill
would be around 2,700 USD/month. For another company, in fewer geographic areas, with one monitor with one resource and
200 city-networks, this portion of the bill would be around 13 USD/month. For more information, see
[Choose a city-networks maximum limit](IMCityNetworksMaximum.md "IMCityNetworksMaximum.md").

You can try out different options with the pricing calculator. To explore pricing options, on
the [Pricing calculator for CloudWatch page](https://calculator.aws/#/addService/CloudWatch "https://calculator.aws/#/addService/CloudWatch"),
scroll down to Internet Monitor.

For more information about Internet Monitor and CloudWatch pricing, see the [Amazon CloudWatch pricing](https://aws.amazon.com//cloudwatch/pricing/ "https://aws.amazon.com//cloudwatch/pricing/") page.
