

# Flow block in Connect Customer: Store customer input
<a name="store-customer-input"></a>

This topic defines the flow block to store input as a contact attribute and then encrypting it.

## Description
<a name="store-customer-input-description"></a>

This block is similar to **Get customer input**, but this one stores the input as a contact attribute (in the [Stored customer input](connect-attrib-list.md#attribs-system-table) system attribute) and you can encrypt it. This way, you can encrypt sensitive input such as credit card numbers. This block:
+ Plays a prompt to get a response from the customer. For example, "Please enter your credit card number" or "Please enter the phone number we should use to call you back." 
+ Plays an interruptible audio prompt or play text-to-speech for a customer to respond to. 
+ Stores numerical input as in the [Stored customer input](connect-attrib-list.md#attribs-system-table) system attribute.
+ You can specify a custom terminating keypress.
+ When a call includes no customer input, the contact takes the **Success branch**. The [Stored customer input](connect-attrib-list.md#attribs-system-table) system attribute holds a value of `Timeout`.

**Check for a timeout**  
To route contacts that time out, add a [Check contact attributes](check-contact-attributes.md) block after the **Store customer input** block. For the attribute to check, choose the **System** namespace and the **Stored customer input** attribute. Then add a condition that checks whether the value equals `Timeout`.  
The **Stored customer input** attribute holds only the result of the most recent **Store customer input** block. Timeouts in other flow blocks do not change its value.

## Supported channels
<a name="store-customer-input-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes | 
| Chat | No - Error branch | 
| Task | No - Error branch | 
| Email | No - Error branch | 

## Flow types
<a name="store-customer-input-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ Inbound flow
+ Customer Queue flow
+ Outbound whisper flow
+ Transfer to Agent flow
+ Transfer to Queue flow

## Properties
<a name="store-customer-input-properties"></a>

The following image shows the **Properties** page of the **Store customer input** block. It shows the **Prompt** section configured to play the **Audio prompt**. 

 For information about choosing a prompt from the Connect Customer library or an S3 bucket, see the [Play prompt](play.md) block. 

![The properties page of the Store customer input block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/store-customer-input-properties1.png)


The following image shows the **Customer input** section of the page. It is configured to allow up to 20 digits. 

![The Customer input section of the properties page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/store-customer-input-properties1b.png)


Note the following properties:
+ **Maximum Digits**: Define the maximum number of digits that a customer can enter.
+ **Phone number**: This option is useful for queued callback scenarios.
  + **Local format**: If all of your customers all calling from the same country that your instance is in, choose that country from the dropdown list. Connect Customer then auto-populates the country code for customers so that they don't have to enter it.
  + **International format**: If you have customers calling from different countries, choose **International format**. Connect Customer then requires customers to enter their country code.

The following image shows the **Input settings** section of the page. It is set to timeout after 15 seconds of no input and 3 seconds for any subsequent inputs.

![The Input settings section of the properties page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/store-customer-input-properties2b.png)


Note the following properties:
+ **Timeout before first entry**: Specify how long to wait for a customer to start entering their reply by voice or DTMF. For example, you might enter 20 seconds, to give the customer time to get their credit card.
+ **Timeout in between each entry**: Specify how long to wait for the next input digit from the customer, by voice or DTMF. For example, you set this field to 10 seconds. When collecting the customer's credit card number, after the customer enters the first digit of their card number, Connect Customer waits up to 10 seconds for them to press the next digit. If they take longer than 10 seconds between any two digits, Connect Customer considers the input complete or timed out. By default, Connect Customer waits 5 seconds for each digit. 
  + Minimum value: 1 second
  + Maximum value: 20 seconds
+ **Encrypt entry**: Encrypt the customer's entry, such as their credit card information. 
+ **Specify terminating keypress**: Define a custom terminating keypress that is used when your contacts complete their DTMF inputs. The terminating keypress can be up to five digits long, with \#, \* and 0-9 characters, instead of just \#. 
**Note**  
To use a star (\*) as part of the terminating keypress, you must also choose **Disable cancel key**.
+ **Disable cancel key**: By default, when a customer enters \* as input, it deletes all of the DTMF input that came before it. However, if you choose **Disable cancel key**, Connect Customer treats the **\*** as any other key.

  If you send the DMTF input to an [AWS Lambda function](invoke-lambda-function-block.md) block, the **Disable cancel key** property affects the input, as follows: 
  + When **Disable cancel key** is selected, all the characters entered—including any \*—are sent to the **AWS Lambda function** block. 
  + When **Disable cancel key** is not selected, only the \* is sent to the **AWS Lambda function** block. 

  For example, let's say you chose **Disable cancel key**, and a customer entered *1\#2\#3\*4\#\#\#*, where *\#\#* is the terminating keypress. The **AWS Lambda function** block then receives the entire *1\#2\#3\*4\#* as input. You could program the Lambda function to ignore the character before the \* character. So, the customer input would be interpreted as *1\#2\#4\#*.

## Problems with DTMF input?
<a name="store-customer-input-use-multiple-input-blocks"></a>

Let's say you have the following scenario with two contacts flows, each one capturing DTMF input from customers: 

1. One flow uses the **Get customer input** block to request DTMF input from customers.

1. After the DTMF input is entered, it uses the **Transfer to flow** block to move the contact to the next contact flow.

1. In the next flow, there's a **Store customer input** block to get more DTMF input from the customer.

There's setup time between the first and second flows. This means if the customer enters DTMF input very quickly for the second flow, some of the DTMF digits might be dropped.

For example, the customer needs to press 5, then wait for a prompt from the second flow, then type 123. In this case, 123 is captured without problem. However, if they don't wait for the prompt and enter 5123 very quickly, the **Store customer input** block may capture only 23 or 3.

To guarantee the **Store customer input** block in second contact flow captures all of the digits, the customer needs to wait for the prompt to be played, and then enter their type DTMF input.

## Touchtone buffering
<a name="store-customer-input-touchtone-buffering"></a>

When touchtone buffering is enabled through the [Set Touchtone Buffer Behavior](set-touchtone-buffer-behavior.md) block, the **Store customer input** block integrates with the buffer:
+ Buffered digits are automatically used as input. If the buffer already contains enough digits to meet the configured maximum, the prompt is skipped entirely and the flow proceeds immediately.
+ If the buffer contains fewer digits than the configured maximum, the block waits for the customer to enter the remaining digits using the inter-digit timeout. For example, if the maximum is 6 digits and the buffer contains 4, the block collects 2 more from the customer before proceeding.
+ Custom terminating keypresses are respected. If the terminating keypress appears in the buffer, input collection ends at that point.

For more information, see [Set Touchtone Buffer Behavior](set-touchtone-buffer-behavior.md).

## Configured block
<a name="store-customer-input-configured"></a>

The following image shows an example of what this block looks like when it is configured. It has the following branches: **Success**, **Error**, and **Invalid number**. 

![A configured Store customer input block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/store-customer-input-configured.png)


1. **Invalid number**: What to do if the customer enters an invalid number.

## Sample flows
<a name="store-customer-input-samples"></a>

Connect Customer includes a set of sample flows. For instructions that explain how to access the sample flows in the flow designer, see [Sample flows in Connect Customer](contact-flow-samples.md). Following are topics that describe the sample flows which include this block.
+ [Sample secure customer data entry input in a call with a contact center agent](sample-secure-input-with-agent.md)
+ [Sample secure customer data entry input in a call with no contact center agent](sample-secure-input-with-noagent.md) 
+ [Sample queue configurations flow in Connect Customer](sample-queue-configurations.md) 
+ [Sample queued callback flow in Connect Customer](sample-queued-callback.md) 