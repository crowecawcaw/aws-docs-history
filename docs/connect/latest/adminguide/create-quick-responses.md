

# Create quick responses for use with chat and email contacts in Connect Customer
<a name="create-quick-responses"></a>

Quick responses provide contact center agents with pre-written responses in English that they can use during chat and email contacts. Quick responses are especially useful for answering common customer inquiries. They help improve agent productivity, reduce handle times, and improve customer satisfaction scores. Quick responses are available in English only.

You can use the Connect Customer admin website or [agent assist actions](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_Operations.html) to create quick responses. You can add single quick responses or import many of them at the same time. You can also personalize responses with [user-defined attributes](add-attributes.md). In addition, you can assign shortcut keys to quick responses, and associate them with [routing profiles](https://docs.aws.amazon.com/connect/latest/adminguide/about-routing.html) so that agents can quickly access relevant content.

By default, CCP enables agents to search quick responses. Custom builders can use [Connect Customer Streams](https://github.com/aws/amazon-connect-streams) to programmatically implement quick response search in their implementations of CCP.

For information about how agents search for quick responses, see [Search for quick responses to customers in the Contact Control Panel (CCP)](search-qr-ccp.md).

**Tip**  
Even though quick responses use the agent assist APIs, quick responses don't lead to additional billing. You only pay for the chat message price or email price. For more information, see [Connect Customer Pricing](https://aws.amazon.com/connect/pricing/).

**Topics**
+ [Assign security profile permissions](quick-response-permissions.md)
+ [Set up a Connect Customer knowledge base](setup-knowledgebase.md)
+ [Add quick responses for use with chat and email contacts](quick-responses.md)
+ [Add attributes for personalizing quick responses](add-attributes.md)
+ [Edit quick responses](edit-quick-responses.md)
+ [Delete quick responses in Connect Customer](delete-qr.md)
+ [Import quick responses](add-data.md)
+ [View the import history for your quick responses](view-import-history.md)
+ [Enable quick responses in a custom CCP](enable-qr-search.md)