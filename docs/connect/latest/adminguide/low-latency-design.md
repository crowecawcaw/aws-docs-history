# Design your Amazon Connect contact center for low latency to

help ensure call quality

###### Note

As of July 2023 we have simplified requirements to claim phone numbers
that are located in countries outside of the AWS Region where your Amazon Connect instance is located.
The process has been simplified to remove the need for the opt-in approval.
Instead we provide best practice design guidance.
This makes it easier for you to use an Amazon Connect instance that is created in the US-East Region, for example, and then request numbers in Japan.
Or, if your instance is created in Asia Pacific (Singapore), you don't need to contact AWS Support to claim phone numbers based in Europe or US Regions.

We continue to extend the support of Amazon Connect so you can claim
phone numbers in the countries you need, wherever you need them.

If you are configuring your Amazon Connect instance to support phone numbers outside of your
country's home AWS Region, we recommend the following best practices.

1. Anchor either your phone numbers or agents in the same AWS Region where they are
   geographically located. For example, if your agents are located in a US Region, your
   Amazon Connect instance should be created in an AWS Region in the US, too. Or, if your
   phone numbers are in an EU country, your Amazon Connect instance should be created in an EU
   AWS Region, too.
   1. If both your phone numbers **and** agents are
      located in an AWS Region that is different from the one where your Amazon Connect
      instance is created, call latency is extended above 500ms for network latency (WebRTC RTT).
      This latency may result in call quality issues.

2. Calculate your latency before setting up your Amazon Connect contact center in production.
   Perform the following steps on a test environment:
   1. Use the [Amazon Connect Endpoint Test
      Utility](check-connectivity-tool.md "check-connectivity-tool.md") to check latency.
   2. Calculate the latency for routing telephony from the country to the AWS
      Region using internet-based, external tools, such as [WonderNetwork](https://wondernetwork.com/ "https://wondernetwork.com/").
   3. For calls with the best call quality, we recommend configurations with
      less than 500ms of latency end-to-end.
   4. You may determine that call quality is acceptable at up to 900ms of
      latency for both network and telephony latency. (900ms is a sum
      of 500ms network latency and 400ms carrier latency.) However, if you note
      a call-quality issue that can be due to latency, and other potential causes
      are ruled out (for example, neither packet loss nor jitter are detected), we
      recommend configuring your Amazon Connect instance or telephony for a lower latency.
      For example, create your Amazon Connect instance in the same Region as your telephony
      or agents.

   ###### Important

   When call latency is greater than 900ms for both network
   and telephony latency, it leads to a significant delay between agents
   and customers.

3. Check that latency matches your design.

After you claim a number you can immediately call it to hear what the experience
will be like for your customers. Amazon Connect uses the [default flows](contact-flow-default.md "contact-flow-default.md") to power your initial experience.

To test a customized flow, [assign a phone
number](associate-claimed-ported-phone-number-to-flow.md "associate-claimed-ported-phone-number-to-flow.md") to it and then call that number.
