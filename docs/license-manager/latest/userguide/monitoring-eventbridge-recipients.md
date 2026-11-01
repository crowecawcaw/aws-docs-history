

# License Manager event recipients and patterns
<a name="monitoring-eventbridge-recipients"></a>

Each AWS account that can view a license or grant receives events on its default event bus:

**License issuer**  
The account that creates the license and the grant. The issuer receives events for the licenses and grants that it creates and distributes to buyers.

**Buyer grantee**  
The account that receives a buyer grant (`BuyerGrant`). The grantee receives events for the license and grant that it receives.

**Delegate grantee**  
The account that receives a delegate grant (`DelegateGrant`). With a delegate grant, this account can view the licenses and grants that the issuer distributes to buyers. It can't change them. The account also receives the related events. For more information about grant types, see [CreateGrant](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateGrant.html) in the *AWS License Manager API Reference*.

**Note**  
Delegate grantees don't receive `License Token Change` or `License Consumption Change` events.

## Create an event pattern
<a name="monitoring-eventbridge-patterns"></a>

To receive all License Manager events, create an EventBridge rule with an event pattern. The following event pattern matches all License Manager events:

```
{
 "source": ["aws.license-manager"]
}
```

To match a specific event type, add the `detail-type` field. The following pattern matches only grant changes:

```
{
 "source": ["aws.license-manager"],
 "detail-type": ["Grant Change"]
}
```

For more information about rules and targets, see [Rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.