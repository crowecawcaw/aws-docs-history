

# Configure dynamic fields in a view
<a name="no-code-ui-builder-properties-dynamic-fields"></a>

Some data changes from contact to contact, so you can't hardcode it. For example, a screen pop might show the customer's name and profile ID.

To dynamically populate a component field:

1. Open the **Properties** tab for the component.

1. Choose the dynamic icon (the lightning bolt) that appears next to the field you want to be dynamic.

The most common fields that require dynamic values are:
+ The **Value** field for display fields.
+ The **DefaultValue** field in form inputs.

You can set any field in the **Properties** tab to dynamic, whether it's visible to users or hidden.

For example, look at the **AttributeBar** component in the following image.

![An Attributes bar component, with the Value set to dynamic.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-attributebar-example.png)

+ The **Label** of Attribute 1 is static: **Customer Name**.
+ The **Value** of the attribute is set to dynamic (the lightning bolt icon is selected).

With these settings, the value comes from the data passed into the [Show view](show-view-block.md) block at runtime.

When you set a field to dynamic, a dynamic reference replaces its static value, and a **Sample Data** section appears below the field. You use this section to define [sample data](no-code-ui-builder-sample-data.md).

The dynamic reference reflects the data structure expected by the [Show view](show-view-block.md) block when setting up runtime data. For example, consider the **Value** of Attribute 1 in the [AttributeBar](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/ui-component-attributebar--with-attributes) component, shown in the following image.

![The Value of Attribute 1 in the AttributeBar component when it is dynamic.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-dynamicicon.png)

+ When set to dynamic, the field becomes `$.AttributeBar_1.Attributes[0].Value`, where `AttributeBar_1` is the Id of the component.
+ This indicates that in the [Show view](show-view-block.md) block, the `AttributeBar_1` field should receive an object. 
+ The object contains an `Attributes` array where the first item (`[0]`) is expected to be an object with a `Value` field.

You can edit dynamic references for clarity or reusability. Dynamic references can be shared across multiple fields and components within the view. For example, in the following image of the [AttributeBar](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/ui-component-attributebar--with-attributes) component, you change its dynamic reference to `$.myAttributeValue`. The [Show view](show-view-block.md) block now has a `myAttributeValue` field that expects a string input.

![The Properties of the AttributeBar component, a Value that is dynamic.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-dynamic-example2.png)


**Important**  
The type of the dynamic reference must match the expected type of the field. For example, you can't use a string-based dynamic reference in a Boolean field. The following image shows an example error message when the dynamic reference doesn't match.  

![The Customize panel, an error message because the dynamic reference doesn't match the expected type in the field.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties-dynamic-fields-example-4.png)


You can also set every property of an attribute to dynamic. In the following image, everything about this attribute, including the label, is determined at runtime based on the values passed into the [Show view](show-view-block.md) block. For example, **Customer Name** is now sample data that you can use to preview what users see. Users don't see the sample value itself.

![The Customize panel, Customer Name as sample data.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties-dynamic-fields-example-5.png)


For certain components, such as [AttributeBar](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/ui-component-attributebar--with-attributes), you can also set all properties of the component as dynamic. For example, with the AttributeBar, you can choose the dynamic icon (the lightning bolt) to make all of the attributes dynamic. The attributes are determined by whatever is passed to the [Show view](show-view-block.md) block at runtime. 

![All properties of the AttributeBar are set to dynamic.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties-dynamic-6.png)
