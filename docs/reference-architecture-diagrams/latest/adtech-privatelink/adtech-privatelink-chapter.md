# Guidance for AdTech PrivateLink Network on AWS

Publication date: **May 13, 2022 ([Diagram history](#adtech-diagram-history "#adtech-diagram-history"))**

This architecture enables supply-side platforms (SSPs) and demand-side platforms (DSPs) to deploy programmatic bidding applications in the same AWS Region. It uses [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") to route real-time bidding (RTB) traffic in a highly scalable, secure, and cost-optimized design.

## AdTech PrivateLink Network architecture

![Architecture diagram showing AWS PrivateLink connecting SSP and DSP VPCs for real-time bidding traffic.](images/adtech-privatelink.png)

The following steps describe the data flow in this architecture:

1. A reader accesses a webpage with an ad impression, and the browser sends an ad request to the publisher ad server.
2. The publisher ad server processes the request and sends it to the SSP endpoint URL. [Elastic Load Balancing](../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md "../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md") on the SSP Amazon VPC forwards the request to auction instances. The auction server selects DSPs to participate by sending bid requests to each DSP endpoint URL.
3. The SSP Amazon VPC performs a DNS lookup with the VPC DNS resolver or the [Amazon Route 53 private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zones-private.md "../../../Route53/latest/DeveloperGuide/hosted-zones-private.md"). The request routes through the interface endpoint or out to the internet.
4. If AWS PrivateLink connects the DSP, the bid request routes to the endpoint elastic network interface (ENI) in the SSP private subnet. The request then forwards to the endpoint service on the DSP side.
5. The endpoint service routes the bid request to the associated Network Load Balancer. The load balancer distributes the request to the bidder fleet. The bidder instance processes the request and sends a bid response back to the auction instance over the AWS backbone network.
6. For DSPs to use a private hostname for their endpoint URL, the DSP verifies the domain by creating a TXT record on their DNS. This architecture assumes the DSP uses [Amazon Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md") for DNS.
7. Both SSP and DSP configure [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") dashboards to gain visibility into active connections and bytes processed per endpoint connection.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date         |
| ------------------- | ----------------------------------------------- | ------------ |
| Initial publication | Reference architecture diagram first published. | May 13, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
