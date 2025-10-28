# Store a value from a Lambda functions as a contact

attribute in Amazon Connect

Retrieve data from a system
that your organization uses internally, such as an ordering system or
other database with a Lambda function, and store the values as attributes that can then be
referenced in a flow.

The Lambda function returns a response from your internal system in the form of key-value
pairs of data. You can reference the values returned in the External namespace. For example,
`$.External.attributeName`. To use the attributes later in a flow, you can copy
the key-value pairs to user-defined attributes by using a **Set contact
attributes** block. You can then define logic to branch your contact based on
attribute values by using a **Check contact attributes** block. Any contact
attribute retrieved from a Lambda function is overwritten when you invoke any other Lambda
function. Make sure you store external attributes if you want to reference them later in a
flow.

###### Tip

For information about invoking a Lambda function from a flow, see [Grant Amazon Connect access to your AWS Lambda
functions](connect-lambda-functions.md "connect-lambda-functions.md") The topic
also shows how to consume a Lambda function response.

###### To store an external value from a Lambda function as a contact attribute

1. In Amazon Connect, choose **Routing**, **Contact
   flows**.
2. Select an existing flow, or create a new one.
3. Add an [AWS Lambda
   function](invoke-lambda-function-block.md "invoke-lambda-function-block.md") block, then choose the title of the
   block to open the settings for the block.
4. Add the **Function ARN** to your AWS Lambda function that retrieves
   customer data from your internal system.
5. After the [AWS Lambda
   function](invoke-lambda-function-block.md "invoke-lambda-function-block.md") block, add a **Set contact
   attributes** block and connect the **Success** branch of the
   [AWS Lambda
   function](invoke-lambda-function-block.md "invoke-lambda-function-block.md") block to it.
6. Edit the **Set contact attributes** block, and select **Use
   attribute**.
7. For **Destination key**, type a name to use as a reference to the
   attribute, such as customerName. This is the value you use in the
   **Attribute** field in other blocks to reference this attribute.
8. For **Type**, choose **External**.
9. For **Attribute**, enter the name of the attribute returned from the
   Lambda function. The name of the attribute returned from the function will vary depending
   on your internal system and the function you use.
   After this block executes during a flow, the value is saved as a user-defined attribute
   with the name specified by the **Destination key**, in this case
   _customerName_. It can be accessed in any block that uses dynamic
   attributes.

To branch your flow based on the value of an external attribute, such as an account
number, use a **Check contact attributes** block, and then add a condition to
compare the value of the attribute to. Next, branch the flow based on the condition.

######

1. In the **Check contact attributes** block, for **Attribute to
   check** do one of the following:
   - Select **External** for the **Type**, then enter
     the key name returned from the Lambda function in the **Attribute**
     field.

   ###### Important

   Any attribute returned from an AWS Lambda function is overwritten when you invoke
   any other Lambda function. To reference the attributes later in a flow, store them
   as user-defined attributes.
   - Select **User Defined** for the **Type**, and in
     the **Attribute** field, type the name that you specified as the
     **Destination key** in the **Set contact
     attributes** block.

2. Choose **Add another condition**.
3. Under **Conditions to check**, choose the operator for the condition,
   then enter a value to compare to the attribute value. The block creates a branch for each
   comparison you enter, letting you route the contact based on the conditions specified. If
   no condition is matched, the contact takes the **No Match** branch from
   the block.
