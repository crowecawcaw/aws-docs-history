

# Connecting to RISE using your single AWS account
<a name="rise-connection-accounts"></a>

You can establish connectivity between on-premises and RISE with SAP VPC using your AWS account. This method provides you with more control but also requires managing AWS services in your AWS account. You can use any one of the following options.
+  AWS Transit Gateway – Share AWS Transit Gateway resource in you AWS account with AWS account managed by SAP.
+  AWS VPN with AWS Transit Gateway – Create an IPsec VPN connection between your remote network and transit gateway over the internet. For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html) and [Transit gateway VPN attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html).
+ Direct Connect gateway – Create a Direct Connect gateway with a transit virtual interface. For more information, see [Transit gateway attachments to a Direct Connect gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-dcg-attachments.html).

  To strengthen the security, see [How do I establish an AWS VPN over an AWS Direct Connect connection?](https://repost.aws/knowledge-center/create-vpn-direct-connect) 

The following image shows this option within the same AWS Regions.

![Example connections in a single Region.](http://docs.aws.amazon.com/sap/latest/general/images/connectivity-own.jpg)


The following image shows this option across different AWS Regions.

![Example connections across Regions.](http://docs.aws.amazon.com/sap/latest/general/images/connectivity-own-regions.jpg)


When you choose AWS Site-to-Site VPN and/or AWS Direct Connect to establish connectivity between on-premises and RISE with SAP VPC using a Transit Gateway in the AWS account - managed by the Customer, either in the same AWS Region or a different AWS Region than the RISE with SAP VPC, the following applies.

 **Hourly cost:** 

As the AWS Site-to-Site VPN is residing in the AWS account – managed by Customer and is attached to the Transit Gateway that resides in the AWS account – managed by Customer, the cost for the VPN connection and the cost for the Transit Gateway attachment are billed to the AWS account – managed by Customer

As the Direct Connect and Direct Connect Gateway is residing in the AWS account – managed by Customer and is attached to the Transit Gateway that resides in the AWS account – managed by Customer the cost for the AWS Direct Connect ports hours and the cost for the Transit Gateway attachment are billed to the AWS account – managed by Customer.

For peering attachments, each Transit Gateway owner is billed hourly for the peering attachment with the other Transit Gateway.

 **Data processing charges:** 

Data processing charges apply for each gigabyte sent from a VPC, Direct Connect or VPN to/via the Transit Gateway.

Depending on the source and destination the data processing charges vary and will be billed to the AWS account – managed by Customer, or are already included in the RISE subscription (For a cost estimation example: see below)

For more information see:
+  [AWS Site-to-Site VPN Pricing](https://aws.amazon.com/vpn/pricing/) 
+  [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/) 
+  [Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/) 


|  | 
| --- |
|  **Pricing example – Transit Gateway in VPCs in the same region via VPN or Direct Connect**  Cost between AWS Regions vary. For more information, see [Amazon EC2 pricing Data Transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer). ![Transit Gateway in VPCs in the same region via VPN or Direct Connect.](http://docs.aws.amazon.com/sap/latest/general/images/connectivity-transit-same-regions-via-vpndxc-pricing.png)<br />1). 200GB of data sent from a VPC in the AWS account – managed by SAP via the Transit Gateway that resided in the AWS account – managed by Customer via a VPN or Direct Connect in the AWS account – managed by SAP towards On-Premises:<br />200GB \* USD 0.02 per GB = USD 4 (Transit Gateway data processing) \+ 100 GB \* USD 0.09 per GB = USD 9 (VPN data transfer out, with the first 100 GB are free, then USD 0.09 per GB) = USD 13 (Total data transfer out billed to AWS account – managed by SAP)<br />or<br />200GB \* USD 0.02 per GB = USD 4 (Transit Gateway data processing) \+ 200GB \* (USD 0.02–USD 0.19 per GB) = USD 4–USD 38 (Direct Connect data transfer out) = USD 8–USD 42 (Total data transfer out billed to AWS account – managed by SAP)<br />Data processing is charged to the VPC owner who sends the traffic to Transit Gateway. As the sending VPC is residing in the AWS account – managed by SAP and the cost for data transfer is included in the RISE Subscription, therefore the AWS account – managed by Customer will not incur Data Transfer cost in this example.<br />2). 200GB of data sent from On-Premises via a VPN or Direct Connect in the AWS account – managed by Customer via the Transit Gateway that resided in the AWS account – managed by Customer towards VPC in the AWS account – managed by SAP:<br />200GB \* USD 0.00 per GB = USD 0 (VPN data transfer in) \+ 200GB \* USD 0.02 per GB = USD 4 (Transit Gateway data processing) \+ USD 0 (VPN data transfer in) = USD 4 (Total data transfer in billed to AWS account – managed by Customer)<br />or<br />200GB \* USD 0.00 per GB = USD 0 (Direct Connect data transfer in) \+ 200GB \* USD 0.02 per GB = USD 4 (Transit Gateway data processing) = USD 4 (Total data transfer in billed to AWS account – managed by Customer)<br />Data transfer into AWS is free and this also applies to VPN and Direct Connect therefore the only data processing charge is the data processing of the Transit Gateway. As Transit Gateway resides in the AWS account – managed by Customer the cost for data transfer is billed to the AWS account – managed by Customer | 
|  **Pricing example – Transit Gateway in VPCs in the different regions via VPN or Direct Connect**  Cost between AWS Regions vary. For more information, see [Amazon EC2 pricing Data Transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer). ![Transit Gateway in VPCs in the different regions via VPN or Direct Connect.](http://docs.aws.amazon.com/sap/latest/general/images/connectivity-transit-different-regions-via-vpndxc-pricing.png)<br />1). 200GB of data sent from a VPC in the AWS account – managed by SAP via the Transit Gateway that resided in the AWS account – managed by SAP that is peered with an Transit Gateway in a different Region in the AWS account – managed by Customer via a VPN OR Direct Connect in the AWS account – managed by Customer towards On-Premises:<br />200GB \* USD 0.02 per GB = USD 4 (Transit Gateway data processing) \+ 200GB \* (USD 0.01–USD 0.138 per GB) = USD 2–USD 27.6 (Region out) \+ 100GB \* USD 0.09 per GB = USD 9 (VPN data transfer out, with the first 100 GB are free, then USD 0.09 per GB) = USD 15–USD 40.6 (Total data transfer out billed to AWS account – managed by SAP)<br />or<br />200GB \* USD 0.02 per GB = USD 4 (Transit Gateway data processing) \+ 200GB \* (USD 0.01–USD 0.138 per GB) = USD 2–USD 27.6 (Region out) \+ 200GB \* (USD 0.02–USD 0.19 per GB) = USD 4–USD 38 (Direct Connect data transfer out) = USD 10–USD 69.6 (Total data transfer out billed to AWS account – managed by SAP)<br />Data processing is charged to the VPC owner who sends the traffic to Transit Gateway. As the sending VPC is residing in the AWS account – managed by SAP and the cost for Data Transfer is included in the RISE subscription, therefore the AWS account – managed by Customer will not incur Data Transfer cost in this example.<br />2). 200GB of data sent from On-Premises via a VPN or Direct Connect in the AWS account – managed by Customer via the Transit Gateway that resided in the AWS account – managed by Customer via a peered Transit Gateway in a different region in the AWS account – managed by SAP towards a VPC in the AWS account – managed by SAP:<br />200GB \* USD 0.02 per GB = USD 4 (Transit Gateway data processing) \+ 200GB \* USD 0.00 per GB = USD 0 (VPN data transfer in) \+ 200GB \* (USD 0.01–USD 0.138 per GB) = USD 2–USD 27.6 (Region out) = USD 6–USD 31.6 (Total data transfer in billed to AWS account – managed by Customer)<br />or<br />200GB \* USD 0.02 per GB = USD 4 (Transit Gateway data processing) \+ 200GB \* USD 0.00 per GB = USD 0 (Direct Connect data transfer in) \+ 200GB \* (USD 0.01–USD 0.138 per GB) = USD 2–USD 27.6 (Region out) = USD 6–USD 31.6 (Total data transfer in billed to AWS account – managed by Customer)<br />Data transfer into AWS in is free and this also applies to VPN and Direct Connect therefore the data processing charge is the data processing of the Transit Gateway and the inter-region data transfer charges. As Transit Gateway resides in the AWS account – managed by Customer, the cost for data transfer is billed to the AWS account – managed by Customer. | 