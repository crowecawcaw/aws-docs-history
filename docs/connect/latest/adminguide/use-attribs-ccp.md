

# Display contact information to the agent in the Contact Control Panel (CCP)
<a name="use-attribs-ccp"></a>

You can use contact attributes to capture information about the contact and then present it to the agent through the Contact Control Panel (CCP). For example, you might want to do this to customize the agent experience when using the CCP integrated with a customer relationship management (CRM) application. 

Also use them when integrating Connect Customer with a custom application using the Connect Customer Streams API or Connect Customer API. You can use all user-defined attributes, in addition to the customer number and the dialed number, in the CCP using the Connect Customer Streams JavaScript library. For more information, see [Connect Customer Streams API](https://github.com/aws/amazon-connect-streams) or Connect Customer API.

When you use the Connect Customer Streams API, you can access user-defined attributes by invoking contact.getAttributes(). You can access endpoints using contact.getConnections(), where a connection has a getEndpoint() invocation on it.

To access the attribute directly from a Lambda function, use $.External.AttributeName. If the attribute is stored to a user-defined attribute from a [Set contact attributes](set-contact-attributes.md) block, use $.Attributes.AttributeName.

For example, included with your Connect Customer instance, there is a flow named "Sample note for screenpop." In this flow, a [Set contact attributes](set-contact-attributes.md) block is used to create an attribute from a text string. The text, as an attribute, can be passed to the CCP to display a note to an agent.