# Editing records

The following procedure explains how to edit records using the Amazon Route 53 console. For information about how to
edit records using the Route 53 API, see
[ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md") in the _Amazon Route 53 API Reference_.

###### Note

Your changes to records take time to propagate to the Route 53 DNS servers.
Currently, the only way to verify that changes have propagated is to use the
[GetChange](../APIReference/API_GetChange.md "../APIReference/API_GetChange.md") API action. Changes generally propagate to all
Route 53 name servers within 60 seconds.

###### To edit records using the Route 53 console

1. If you're not editing alias records, skip to step 2.

If you're editing alias records that route traffic to an ELB Classic Load Balancer, Application Load Balancer, or Network Load Balancer, and if you
created your Route 53 hosted zone and your load balancer using different accounts, perform the procedure
[Getting the DNS name for an ELB load balancer](resource-record-sets-creating.md#resource-record-sets-elb-dns-name-procedure "resource-record-sets-creating.md#resource-record-sets-elb-dns-name-procedure")
to get the DNS name for the load balancer.

If you're editing alias records for any other AWS resource, skip to step 2. 2. Sign in to the AWS Management Console and open the Route 53 console at
[https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/"). 3. In the navigation pane, choose **Hosted zones**. 4. On the **Hosted Zones** page, choose the row for the hosted zone that contains the records that you want to edit. 5. Select the row for the record that you want to edit, and then enter your changes in the **Edit record** pane. 6. Enter the applicable values. For more information, see
[Values that you specify when you create or edit Amazon Route 53 records](resource-record-sets-values.md "resource-record-sets-values.md"). 7. Choose **Save changes**. 8. If you're editing multiple records, repeat steps 5 through 7.
