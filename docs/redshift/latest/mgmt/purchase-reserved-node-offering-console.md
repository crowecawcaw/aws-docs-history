Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Purchasing a reserved

node

You can use the AWS Management Console or the AWS CLI to purchase reserved node offerings, and to
view current and past reservations.

AWS Management Console

###### To purchase a reserved node

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then
   choose **Reserved nodes** to display the list of
   reserved nodes.
3. Choose **Purchase reserved nodes** to display the
   page to choose the properties of the node that you want to
   purchase.
4. Enter the properties of the node, then choose **Purchase
   reserved nodes**.

After you purchase an offering, the **Reserved Node**
list displays your reservations and the details of each one, such as the
node type, number of nodes, and status of the reservation. For more
information about the reservation details, see [How reserved nodes work](purchase-reserved-node-instance.md#how-reserved-nodes-work "purchase-reserved-node-instance.md#how-reserved-nodes-work").

To upgrade a reserved node, use the AWS CLI.

You can't convert all node types to reserved nodes, and it's also possible
that an existing reserved node isn't available for renewal. This might be
because the node type is discontinued. Contact customer support to renew a
discontinued node type.

AWS CLI

###### To upgrade a reserved node

reservation with the AWS CLI

1. Obtain a list of ReservedNodeOfferingID's for offerings that meet
   your requirements for payment type, term, and charges. The following
   example illustrates this step.

```

aws redshift get-reserved-node-exchange-offerings --reserved-node-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
{
    "ReservedNodeOfferings": [
        {
            "Duration": 31536000,
            "ReservedNodeOfferingId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
            "UsagePrice": 0.0,
            "NodeType": "dc2.large",
            "RecurringCharges": [
                {
                    "RecurringChargeFrequency": "Hourly",
                    "RecurringChargeAmount": 0.2
                }
            ],
            "CurrencyCode": "USD",
            "OfferingType": "No Upfront",
            "ReservedNodeOfferingType": "Regular",
            "FixedPrice": 0.0
        }
    ]
}

```

2. Call `accept-reserved-node-exchange` and provide the ID
   for the DC1 reserved node that you want to exchange along with the
   ReservedNodeOfferingID you obtained in the previous step.

The following example illustrates this step.

```

aws redshift accept-reserved-node-exchange --reserved-node-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --target-reserved-node-offering-id yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyyy
{
    "ExchangedReservedNode": {
        "UsagePrice": 0.0,
        "OfferingType": "No Upfront",
        "State": "exchanging",
        "FixedPrice": 0.0,
        "CurrencyCode": "USD",
        "ReservedNodeId": "zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz",
        "NodeType": "dc2.large",
        "NodeCount": 1,
        "RecurringCharges": [
            {
                "RecurringChargeFrequency": "Hourly",
                "RecurringChargeAmount": 0.2
            }
        ],
        "ReservedNodeOfferingType": "Regular",
        "StartTime": "2018-06-27T18:02:58Z",
        "ReservedNodeOfferingId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyyy",
        "Duration": 31536000
    }
}

```

You can confirm that the exchange is complete by calling [describe-reserved-nodes](../../../cli/latest/reference/redshift/describe-reserved-nodes.md "../../../cli/latest/reference/redshift/describe-reserved-nodes.md") and checking the value for `Node
 type`.
