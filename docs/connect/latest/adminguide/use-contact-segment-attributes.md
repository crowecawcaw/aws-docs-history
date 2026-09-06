

# Use contact segment attributes
<a name="use-contact-segment-attributes"></a>

For scenarios where information for a contact varies between transfers or conferences, such as business unit names that might change as a contact moves between departments, you need to use *contact segment attributes*. 

Contact segment attributes keep the values that remain specific to individual contact segments. (For a discussion about the difference between contact attributes and contact segment attributes, see [Contacts, contact chains, and contact attributes](contacts-contact-chains-attributes.md).)

To implement contact segment attributes, you first create predefined attributes, and then use the [Set contact attributes](set-contact-attributes.md) block to attach them to the contact as contact segment attributes. There are two ways you can do this:
+ Use the Connect Customer admin website, as described in this topic.
+ Use the [CreatePredefinedAttribute](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatePredefinedAttribute.html) to create the predefined attributes programmatically, and use the [UpdateContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContact.html) API to attach a predefined attribute as a contact segment attribute.

**Topics**
+ [Step 1: Create a predefined attribute](#create-predefined-attribute)
+ [Step 2: Attach a predefined attribute to the contact segment](#attach-predefined-attribute)

## Step 1: Create a predefined attribute
<a name="create-predefined-attribute"></a>

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an **Admin** account, or an account assigned to a security profile that has **Routing** - **Predefined attributes** - **Create** permission. 

1. In Connect Customer, on the left navigation menu, choose **Routing**, **Predefined attributes**. 

1. On the **Attribute management** page, choose **Add attribute**, as shown in the following image.  
![The Attribute management page, the Add attribute option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/attribute-management-1.png)

1. On the **Add predefined attributes** page, add the name in the **Predefined attribute** box and the value in the **Value** box. The following example image shows a predefined attribute named **Business Unit**, and three values: Sales, Marketing, and Accounts.  
![The Add predefined attribute page, a predefined attribute named Business Unit, and three sample values.](http://docs.aws.amazon.com/connect/latest/adminguide/images/attribute-management-2.png)

1. Choose **Add value** to add more values to the predefined attribute.

1. To use this attribute and its values to filter contact search results, select **Use as Contact search filter**.

1. To enforce value validations when attaching the attribute and value to a contact segment, select **Enforce valid values**.

1. To use this attribute and its values for filtering contact related metrics, select **Use in analytics for granular insights**.

   1. This feature is only available for instances that have unlimited AI capabilities enabled.

## Step 2: Attach a predefined attribute to the contact segment
<a name="attach-predefined-attribute"></a>

The following image shows the properties panel of the [Set contact attributes](set-contact-attributes.md) block. 

![The Set contact attributes block properties.](http://docs.aws.amazon.com/connect/latest/adminguide/images/attribute-management-3.png)


When **Namespace ** = **Segment attributes**, the **Key** dropdown menu lists the predefined attributes. 

Under the **Set manually** option, you can set a **Value** based on established values for the selected predefined attribute.

For information about filtering contacts by contact segment attributes, see [Search by custom contact attributes or contact segment attributes](search-custom-attributes.md).

For information on how to use predefined attributes for analytics reporting, see [Use predefined attributes in dashboards](use-predefined-attributes-dashboards.md).