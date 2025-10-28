# Best practices for flows in Amazon Connect

Use the list of recommended best practices in this topic when you are using and
creating flows.

- Use consistent attribute naming conventions across all AWS services. Use
  camel case for yourAttributeNames to avoid confusion when passing and
  referencing variables.
- Use standard naming conventions for attribute names. Don't use spaces or
  special characters that could impact downstream reporting processes such as
  AWS Glue crawlers.
- Create modular flows. Make the flows as small as possible, and then combine
  modular flows into an end-to-end contact experience. This helps to keep your
  flows manageable, and you won't require numerous regression testing
  cycles.
- When you set **User Defined** or
  **External** values in dynamic attribute fields, use only
  alphanumeric characters (A-Z, 0–9) and periods. No other characters are
  allowed.
- Ensure all error branches are routed to a block that effectively handles the
  error or terminates the contact.
- Use a **Set logging behavior** block to enable or disable
  logging for segments of the flow where sensitive information is collected and
  can't be stored in CloudWatch.
- Ensure that attributes used in the flow are set and referenced correctly. If
  there are periods prepended to the attribute names, you are likely using
  JSONPath ($.) format while also selecting a variable type from the pick list.
  For example, using:
  - **Save text as attribute** and value
    `$.External.variableName` works as expected.
  - `Set dynamically` and value `variableName` works
    as expected.
  - **Set dynamically** and
    `$.External.variableName` results in a prepended period.

- Before transferring a call to agent and putting that call in a queue, ensure
  that **Check hours of operation** and **Check
  staffing** blocks are used. They verify that the call is within
  working hours and that agents are staffed to service.
- Ensure that callbacks are offered before and after queue transfer by using
  **Check queue status** blocks. Include a condition for
  **Queue capacity** that is greater than X, where X is a
  number representing your expected queue capacity.
  - If queue capacity exceeds the expected capacity, use a **Get
    Customer Input** block to offer a callback. This retains
    the caller's position in the queue and calls them back when an agent is
    available.
  - In the **Set callback number** block, choose the
    number to be used to call the customer back in the CCP. Use
    **System** and **Customer Number**
    or a new number, collected by a **Store Customer
    Input** block, using **System** and
    **Stored customer input**.
  - Finally, add a **Transfer to queue** block. Configure
    it to **Transfer to callback queue** and configure the
    callback options to fit your specific use case.

- Use a **Loop prompts** block in your Customer queue flow to
  interrupt with a queued callback and external transfer option at regular
  intervals.
- Ensure that all countries referenced in external transfers or used for
  outbound dialing are added to the service quota for your
  account/instance.
- Ensure that all numbers referenced in external transfers are in E.164 format.
  Drop the national trunk prefix that you use when calling locally. This prefix
  would be the leading 0 for most of Europe, 1 for the US. The prefix is replaced
  by the country code. For example, the UK mobile number **07911
  123456** in E.164 format is **+44 7911 123456
  (tel:+447911123456)**.
- Ensure that there are no infinite loops in the flow logic. Also ensure that
  for each call, the flow connects the caller to an agent, bot, or transferred
  externally for further assistance.
