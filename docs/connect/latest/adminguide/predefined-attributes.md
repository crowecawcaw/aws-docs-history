

# Create predefined attributes for routing contacts to agents
<a name="predefined-attributes"></a>

A predefined attributed is made up of a name-value pair. For example, a name such as `language` and values such as `English`, `French`, `Japanese`. You can use predefined attributes to route contacts to an agent or pools of agents within a queue. 

**Tip**  
You define the level of an agent's proficiency in their user profile, not when you create a predefined attribute. A proficiency level is an indicator, ranging from 1 to 5, of the level of expertise of an agent for a given attribute value. Level 1 is the lowest proficiency, while 5 is the highest.

You can create and manage predefined attributes manually by using the Connect Customer admin website; the steps are described in this topic. Or programmatically by using the [Predefined attribute management APIs](#predefined-attributes-apis).

**Topics**
+ [Important things to know](#important-things-predefined-attributes)
+ [System predefined attributes](#sytem-predefined-attributes)
+ [Create a predefined attribute](#predefined-attributes-create-web-admin)
+ [Update the name of an attribute or value](#update-predefined-attributes)
+ [Predefined attribute management APIs](#predefined-attributes-apis)

## Important things to know
<a name="important-things-predefined-attributes"></a>
+ The information in a predefined attribute is not encrypted. We strongly recommend you follow the [Best practices for PII compliance in Connect Customer](compliance-validation-best-practices-PII.md).
+ You can create up to 500 values per attribute.
+ A predefined attribute **name** can be up to 100 characters long.
+ A predefined attribute **value** can be up to 100 characters long.
+ The pattern for predefined attribute name and value is `^(?!(aws:|connect:))[\p{L}\p{Z}\p{N}_.:/=+-@']+$`. For example, it can contain any letter, numeric value, whitespace, or `_.:/=+-@'` special characters, but can't start with `aws:` or `connect:`.
+ The preceding pattern restriction applies to **customer-created** predefined attributes only. System predefined attributes (such as `connect:WorkloadType`, `connect:Language`, and `connect:Subtype`) use the `connect:` prefix and are managed by Connect Customer. You can add custom values to system attributes where permitted, but you cannot rename or delete the attribute itself.
+ You cannot create duplicate predefined attribute names or values. In addition, case sensitivity means you cannot use duplicate names. For example, a new predefined attribute with the name `language` cannot be created if a predefined attribute with name `Language` exists in your Connect Customer instance.
+ An attribute can only be deleted if it not associated with any agent.

  Before deleting an attribute, ensure none of the contacts are waiting for an agent with that attribute or the contact will not find a match.
+ For the quota for predefined attributes allowed in a Connect Customer instance, see [Connect Customer quotas](amazon-connect-service-limits.md#connect-quotas).

## System predefined attributes
<a name="sytem-predefined-attributes"></a>

System attributes, identified as `connect:`, are predefined attributes set by Connect Customer. You cannot change or delete the `connect:` name and values.

The following system attributes are available: 
+ `connect:Language`. You can add 500 custom values for `connect:Language`.
+ `connect:Subtype`. You cannot change `connect:Subtype` but it can be used in routing criteria for routing.
+ `connect:WorkloadType`. Represents the complexity or urgency of a contact's work. You can add up to 500 custom values for `connect:WorkloadType`. These values are used to configure workload-type concurrency in routing profiles, allowing you to set different agent capacity limits for different types of work within the same channel (Task or Email). For more information, see [Channels and concurrency for routing contacts in Connect Customer](channels-and-concurrency.md).

## Create a predefined attribute
<a name="predefined-attributes-create-web-admin"></a>

1. Log in to the Connect Customer admin website with an **Admin** account, or an account assigned to a security profile that has **Routing** - **Predefined attributes** - **Create** permission. 

1. In Connect Customer, on the left navigation menu, choose **Routing**, **Predefined attributes**. 

1. On the **Attribute management** page choose **Add attribute**, as shown in the following image.  
![The Attribute management page, the Add attribute button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/add-attribute.png)

1. On the **Add predefined attribute** page, in the **Details** section, complete the following fields as needed:

   1. **Name**: Enter a name for the segment attribute.

   1. **Use as a Contact search filter**: Choose if you want to enable contact search on this segment attribute.

   1. **Use in analytics for granular insights**: Choose if you want to enable Analytics on this segment attribute.

      Amazon Connect unlimited AI should be enabled for the instance to view this option.

      Note: Do not store personally identifiable information (PII) as values in attributes are used for analytics purposes.

   1. **Enforce valid values**: Choose to allow only predefined values when using this attribute as a contact segment attribute.

1. Choose **Add value** to add values to the attribute. For example, you might enter Sales, Marketing, and Accounts for Business units.   
![Save to save the attribute and values.](http://docs.aws.amazon.com/connect/latest/adminguide/images/predefined-attribute-add.png)

1. Choose **Save** to save the predefined attribute and values.

## Update the name of an attribute or value
<a name="update-predefined-attributes"></a>

1. Stop using the attribute on future contacts to drain all of the contacts on an active contact type.

1. Update all of the attributes.

## Predefined attribute management APIs
<a name="predefined-attributes-apis"></a>
+ [CreatePredefinedAttribute](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatePredefinedAttribute.html)
+ [UpdatePredefinedAttribute](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePredefinedAttribute.html)
+ [DeletePredefinedAttribute](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeletePredefinedAttribute.html)
+ [DescribePredefinedAttribute](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePredefinedAttribute.html)
+ [ListPredefinedAttributes](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPredefinedAttributes.html)