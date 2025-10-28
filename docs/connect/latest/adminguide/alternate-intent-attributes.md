# Use alternate intent attributes in

Amazon Lex

Usually you configure flows to branch on the winning Lex intent. However, in some
situations, you might want to branch on an alternate intent. That is, what the customer
might have meant.

The following image shows the **Properties** page of the
**Check contact attributes** block. It is configured to check a Lex
attribute.

![The properties page of the Check contact attributes block.](images/check-contact-attributes-alternate-intents.png)

1. **Intent name** is the name of an alternate intent in Lex. It's
   case sensitive and must match what's in Lex exactly.
2. **Intent Attribute** is what Amazon Connect is going to check. In this
   example, it's going to check the **Intent Confidence Score**.
3. **Conditions to check**: If Lex is 70% certain the customer meant
   the alternate intent instead of the winning intent, branch.
