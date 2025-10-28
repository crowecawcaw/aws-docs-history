# Sample flow in Amazon Connect for A/B contact distribution

testing

###### Note

This topic explains a sample flow that is included with Amazon Connect. For information
about locating the sample flows in your instance, see [Sample flows in Amazon Connect](contact-flow-samples.md "contact-flow-samples.md").

Type: Flow (inbound)

This flow shows how to perform an A/B call distribution based on a percentage. Here's
how it works:

1. The **Play prompt** block uses Amazon Polly, the text-to-speech
   service, to say "Amazon Connect will now simulate rolling dice by using the Distribute
   randomly block. Now rolling."
2. The contact reaches the **Distribute by percentage** block,
   which routes the customer randomly based on a percentage.

**Distribute by percentage** simulates a dice roll, resulting
in a values between 2 to 12 with different percentages. For example, there is 3
percent chance for the "2" option, 6 percent chance for the "3" option, and so
on. 3. After the contact gets routed, the **Play prompt** tells the
customer which number the dice rolled. 4. At the end of the sample, the **Transfer to flow** block
transfers the customer back to the [Sample inbound flow](sample-inbound-flow.md "sample-inbound-flow.md").
