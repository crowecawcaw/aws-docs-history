# Check attributes

This topic defines the flow block for branching based on a comparison to the value of an
attribute.

## Description

The Check Attributes block branches the journey flow based on comparisons between attribute values. It evaluates contact, flow, or system attributes to determine which path the journey should take next.

You can use this block to apply conditional logic such as:

- Routing customers to different paths based on segment, preferred channel, or message outcome
- Checking Lambda-returned values such as eligibility results or risk scores
- Comparing delivery receipt attributes to decide follow-up actions
- Controlling loop progression based on counters or flags set in earlier steps

**Example use cases**

- Channel fallback: If an SMS delivery receipt returns a DeliveryStatus of failed, use the Check Attributes block to branch the journey and send an email instead.
- Personalization and targeting: Branch based on customer segment. For example, if customerSegment equals premium, send a high-value offer; otherwise, continue to a standard path.
- Dynamic scheduling: Evaluate an attribute such as DaysSinceLastEngagement. If greater than 30, send a re-engagement message; if less than 7, skip outreach.
- Lambda-driven logic: After a Lambda function returns an eligibilityStatus, continue only if the value equals true.
- Loop control: Use Check Attributes to evaluate loop counters. If loopCount is less than 3, continue retrying; otherwise, end the loop.

## How to configure this block

You can configure the **Check attributes** block by using the Amazon Connect admin website or by using the CheckAttributes action in Flow language.

### Common properties

| Property      | Description                                                             |
| ------------- | ----------------------------------------------------------------------- |
| Attribute key | Select the attribute to evaluate.                                       |
| Operator      | Choose the comparison condition (Equals, Contains, Greater than, etc.). |
| Value         | Specify the target value for comparison.                                |

Supported comparison conditions include: **Equals**, **Is less than**, **Is less or equal**, **Is greater than**, **Is greater or equal**, **Starts with**, **Ends with**, **Contains**, **Exists**, **Key exists**.

**Supported attribute namespaces**

The Check Attributes block can read attributes from the same namespaces supported by the Set Attributes block:

- Flow attributes
- Lambda invocation
- Loop
- Delivery receipts
- Outbound communication
