

# Check block
<a name="testing-simulation-check-block"></a>

The Check block validates that specific values or conditions in your contact flow match your expectations. It's your quality assurance tool within the test, making sure that data, attributes, and system states are exactly what they should be at any given point.

You can add a Check block. In the interaction group menu (⋮), choose **Add check block**. When you add a Check block, you're essentially asking: "Is this value what I expect it to be?" The test will pass or fail based on whether the actual value meets your defined criteria.

![Check block configuration panel showing assertion options for validating contact flow attributes.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-check-block-intro.png)


## How assertions work
<a name="testing-simulation-check-assertions"></a>

An assertion compares an actual value from your contact flow against an expected value using a comparison operator. If the comparison is true, the assertion passes; if false, the test fails and provides details about what was expected versus what was found.

Configuration options:

### Attribute to check
<a name="testing-simulation-check-attribute"></a>

Specify which attribute or value you want to validate using the predefined list of supported Namespaces and Keys. This tells the system where to find the value you want to check.

Examples:
+ Namespace = System, Key = Queue name – Checks the name of the current queue
+ Namespace = System, Key = Customer address or number – Validates the source phone number or address
+ Namespace = User defined, Key = Customer type – Examines a custom contact attribute

### Condition type
<a name="testing-simulation-check-condition-type"></a>

Choose how you want to compare the actual value against your expected value:
+ **Equals** – The value must exactly match your expected value
+ **Starts With** – The text value must begin with your specified text
+ **Ends With** – The text value must end with your specified text
+ **Contains** – The text value must include your specified text anywhere within it
+ **Number Greater Than** – The numeric value must be larger than your expected number
+ **Number Greater or Equal To** – The numeric value must be larger than or equal to your expected number
+ **Number Less Than** – The numeric value must be smaller than your expected number
+ **Number Less or Equal To** – The numeric value must be smaller than or equal to your expected number

### Condition value
<a name="testing-simulation-check-condition-value"></a>

Enter the value you expect to find. This is what the actual value will be compared against using your chosen operator.

## Practical examples
<a name="testing-simulation-check-examples"></a>

Example: Validating Queue Placement
+ Namespace: System
+ Key: Queue name
+ Operator: Equals
+ Expected Value: "Basic Queue"

This checks that the contact was placed in the correct queue.

![Check block configuration showing queue name validation with Equals operator and Basic Queue expected value.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-check-block-example.png)


## What happens when checks fail?
<a name="testing-simulation-check-failures"></a>

When an assertion fails, the test execution stops and provides detailed information about the failure, including:
+ Which attribute was being checked
+ What value was expected
+ What value was found
+ The comparison operator that was used

This information helps you quickly identify and fix issues in your contact flow.

![Check block failure details showing expected versus actual values and the comparison operator used.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-check-block-failures.png)
