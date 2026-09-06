

# Use alternate intent attributes in Amazon Lex
<a name="alternate-intent-attributes"></a>

Usually you configure flows to branch on the winning Lex intent. However, in some situations, you might want to branch on an alternate intent. That is, what the customer might have meant. 

The following image shows the **Properties** page of the **Check contact attributes** block. It is configured to check a Lex attribute. 

![The properties page of the Check contact attributes block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/check-contact-attributes-alternate-intents.png)


1. **Intent name** is the name of an alternate intent in Lex. It's case sensitive and must match what's in Lex exactly.

1. **Intent Attribute** is what Connect Customer is going to check. In this example, it's going to check the **Intent Confidence Score**.

1. **Conditions to check**: If Lex is 70% certain the customer meant the alternate intent instead of the winning intent, branch.