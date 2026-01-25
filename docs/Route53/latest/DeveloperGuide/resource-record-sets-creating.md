# Creating records by using the Amazon Route 53 console

The following procedure explains how to create records using the Amazon Route 53 console. For information about how to
create records using the Route 53 API, see
[ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md") in the _Amazon Route 53 API Reference_.

###### Note

To create records for complex routing configurations, you can also use the Traffic Flow visual editor and
save the configuration as a traffic policy. You can then associate the traffic policy with one or more domain names
(such as example.com) or subdomain names (such as www.example.com), in the same hosted zone or in multiple hosted zones.
In addition, you can roll back the updates if the new configuration isn't performing as you expected it to. For more information,
see [Using Traffic Flow to route DNS traffic](traffic-flow.md "traffic-flow.md").

###### To create a record using the Route 53 console

1. If you're not creating an alias record, go to step 2.

Also go to step 2 if you're creating an alias record that routes DNS traffic to an AWS resource other than an Elastic Load Balancing
load balancer or another Route 53 record.

If you're creating an alias record that routes traffic to an Elastic Load Balancing load balancer, and if you created your hosted zone and your
load balancer using different accounts, perform the procedure
[Getting the DNS name for an Elastic Load Balancing load balancer](#resource-record-sets-elb-dns-name-procedure "#resource-record-sets-elb-dns-name-procedure")
to get the DNS name for the load balancer. 2. Sign in to the AWS Management Console and open the Route 53 console at
[https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/"). 3. In the navigation pane, choose **Hosted zones**. 4. If you already have a hosted zone for your domain, skip to step 5. If you don't, perform the applicable procedure to
create a hosted zone:

    * To route internet traffic to your resources, such as Amazon S3 buckets or Amazon EC2 instances, see
     [Creating a public hosted zone](CreatingHostedZone.md "CreatingHostedZone.md").
    * To route traffic in your VPC, see
     [Creating a private hosted zone](hosted-zone-private-creating.md "hosted-zone-private-creating.md").

5. On the **Hosted zones** page, choose the name of the hosted zone that you
   want to create records in.
6. Choose **Create record**.
7. Choose and define the applicable routing policy and values. For more information, see the
   topic for the kind of record that you want to create:
   - [Values that are common for all routing
     policies](resource-record-sets-values-shared.md "resource-record-sets-values-shared.md")
   - [Values that are common for
     alias records for all routing policies](resource-record-sets-values-alias-common.md "resource-record-sets-values-alias-common.md")
   - [Values specific for simple
     records](resource-record-sets-values-basic.md "resource-record-sets-values-basic.md")
   - [Values specific for simple alias
     records](resource-record-sets-values-alias.md "resource-record-sets-values-alias.md")
   - [Values specific for failover
     records](resource-record-sets-values-failover.md "resource-record-sets-values-failover.md")
   - [Values specific for failover
     alias records](resource-record-sets-values-failover-alias.md "resource-record-sets-values-failover-alias.md")
   - [Values specific for geolocation
     records](resource-record-sets-values-geo.md "resource-record-sets-values-geo.md")
   - [Values specific for geolocation
     alias records](resource-record-sets-values-geo-alias.md "resource-record-sets-values-geo-alias.md")
   - [Values specific for geoproximity
     records](resource-record-sets-values-geoprox.md "resource-record-sets-values-geoprox.md")
   - [Values specific for geoproximity
     alias records](resource-record-sets-values-geoprox-alias.md "resource-record-sets-values-geoprox-alias.md")
   - [Values specific for latency
     records](resource-record-sets-values-latency.md "resource-record-sets-values-latency.md")
   - [Values specific for latency
     alias records](resource-record-sets-values-latency-alias.md "resource-record-sets-values-latency-alias.md")
   - [Values specific for IP-based records](resource-record-sets-values-ipbased.md "resource-record-sets-values-ipbased.md")
   - [Values specific for IP-based alias records](resource-record-sets-values-ipbased-alias.md "resource-record-sets-values-ipbased-alias.md")
   - [Values specific for multivalue
     answer records](resource-record-sets-values-multivalue.md "resource-record-sets-values-multivalue.md")
   - [Values specific for weighted
     records](resource-record-sets-values-weighted.md "resource-record-sets-values-weighted.md")
   - [Values specific for weighted
     alias records](resource-record-sets-values-weighted-alias.md "resource-record-sets-values-weighted-alias.md")

8. Choose **Create records**.

###### Note

Your new records take time to propagate to the Route 53 DNS servers.
Currently, the only way to verify that changes have propagated is to use the
[GetChange](../APIReference/API_GetChange.md "../APIReference/API_GetChange.md") API action. Changes generally propagate to all
Route 53 name servers within 60 seconds. 9. If you're creating multiple records, repeat steps 7 through 8.

###### Getting the DNS name for an Elastic Load Balancing load balancer

1. Sign in to the AWS Management Console using the AWS account that was used to create the Classic, Application, or Network Load Balancer that you
   want to create an alias record for.
2. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
3. In the navigation pane, choose **Load Balancers**.
4. In the list of load balancers, select the load balancer for which you want to create an
   alias record.
5. On the **Description** tab, get the value of **DNS name**.
6. If you want to create alias records for other Elastic Load Balancing load balancers, repeat steps 4 and 5.
7. Sign out of the AWS Management Console.
8. Sign in to the AWS Management Console again using the AWS account that you used to create the Route 53 hosted zone.
9. Return to step 3 of the procedure Creating records by using the Amazon Route 53 console.
