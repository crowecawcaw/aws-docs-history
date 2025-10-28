# Pricing for AWS Global Accelerator

With AWS Global Accelerator, you are charged a _fixed hourly fee_ for each accelerator that is provisioned in your account
(whether it's enabled or disabled), and an _incremental charge_, in addition to standard data transfer rates,
for every hour of traffic in the dominant direction that flows through the accelerator. The incremental rate depends on the AWS Region
that serves the request (the source) and the AWS edge location where the responses are directed (the destination). Customers
typically create one accelerator for each application, but customers with complex applications might require more accelerators.

In addition, you will incur standard public IPv4 address charges for IPv4 addresses used with your accelerators.

For details about pricing, information about pricing by source and destination Regions, and a pricing example,
see [AWS Global Accelerator pricing](https://aws.amazon.com/global-accelerator/pricing "https://aws.amazon.com/global-accelerator/pricing").
