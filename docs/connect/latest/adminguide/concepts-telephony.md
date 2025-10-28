# The voice channel in Amazon Connect

###### Important

Trying to contact Amazon for support? See [Amazon Customer
Service](https://www.amazon.com/gp/help/customer/display.html "https://www.amazon.com/gp/help/customer/display.html") (Amazon orders and deliveries) or [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") (Amazon Web Services).

Amazon Connect provides a variety of choices to enable your company to make and receive
telephone calls. One of the great advantages of Amazon Connect is AWS manages the telephony
infrastructure for you: carrier connections, redundancy, and routing. And, it's designed
to scale.

This topic explains the options that Amazon Connect provides for telephony, which helps you
build a solution to meet your business requirements.

###### Contents

- [Telephony architecture](#concepts-telephony-architecture "#concepts-telephony-architecture")
- [Use cases for different configurations](#concepts-use-cases "#concepts-use-cases")

## Telephony architecture

Amazon Connect provides capabilities to host both toll-free and direct dial numbers (DID)
in all AWS Regions supported by Amazon Connect. You can use both types of numbers in a
single instance. A complete list of supported countries/regions and costs is located
on the [Amazon Connect pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/")
page.

AWS manages the connectivity to our network of carriers providing diverse
connections to multiple carriers in each region supported by Amazon Connect. When Amazon Connect is
deployed in a Region, we take advantage of the built-in redundancy of the AWS
Availability Zone design to provide multiple carrier interfaces into multiple data
centers. You can see how AWS manages the design of a Region [here](https://infrastructure.aws/ "https://infrastructure.aws/").

In addition to the Amazon Connect service being spread across multiple Availability Zones,
AWS also has multiple telephony providers. These providers have multiple links
into the data centers in those Availability Zones. This ensures that if a single or
even multiple links fail from a carrier, there are alternate routes available to
ensure the service remains available.

To learn more about Amazon Connect architecture, see [Architectural guidance for Amazon Connect](architecture-guidance.md "architecture-guidance.md").

- **AWS manages toll-free numbers as a Responsible
  Organization**

These numbers are phone numbers with distinct prefix codes that can be
dialed with no charge to the person placing the call. Such numbers allow
callers to reach businesses and/or individuals out of the area without being
charged a long-distance fee for the call.

In the United States, the [Federal Communications Commission](https://www.fcc.gov/consumers/guides/what-toll-free-number-and-how-does-it-work "https://www.fcc.gov/consumers/guides/what-toll-free-number-and-how-does-it-work") provides rules for obtaining
and using toll-free numbers. In other countries, similar governing bodies
ensure that such numbers are managed and distributed in accordance with
local laws.

When you claim or port a US toll-free number into Amazon Connect, we register that
number with [SOMOS](https://www.somos.com/ "https://www.somos.com/"). After the
number is registered, we are able to select multiple carriers to provide
BOTH route and carrier redundancy. This provides the highest level of
availability, ensuring the number will remain available even in the event of
a complete carrier outage. This level of service does come at an additional
cost, as these numbers are a higher price than direct dial, but the service
reliability and customer experience make this the most attractive
option.

- **Locally formatted numbers**

Direct inward dialing (DID), also called direct dial-in (DDI) in Europe,
is a telecommunication service offered by telephone companies to
subscribers. DID numbers provide a locally formatted telephone number that
can match the dialing pattern of a local subscriber. For example, in
Seattle, Washington, USA, the local dialing pattern is +1(206)-NXX-XXXX. The
provider of the DID number would provide numbers with the +1(206) pattern to
match local dialing.

In the United States, DID numbers are regulated by State Public Utilities
commissions. DID numbers are managed by a single carrier. While they are
portable, they can't be load balanced/managed across multiple carriers. This
makes them less reliable than toll-free numbers.

DID numbers offer you the ability to present a local calling line
identification when placing outbound calls, and a local presence to inbound
callers. This can be very useful to increase the likelihood outbound and
queued callback calls get answered by your customers. It can also show a
customer that you are local to their area, and provide a cheaper inbound
route than a long-distance call if you don't publish a toll-free
number.

Because DID numbers are threaded to single carrier, Amazon Connect doesn't offer
carrier redundancy for DID numbers. We do offer link redundancy across
multiple Availability Zones, so in the event of a link failure that carrier
still has facilities available in another location to deliver calls. DID
numbers also have a capacity limitation on how many calls a single number
can accommodate, and this number does vary by Region. It is important to
work with your AWS account team to ensure you are properly enabled with
the right type of DID numbers if you plan on using DID numbers as your
primary inbound channel, and have an expectation of over 100 concurrent
calls per number.

DID numbers are less expensive than toll-free numbers, but don't have the
redundancy and broad geographical coverage of them. The ability to localize
numbers may be an attractive option for your business.

## Use cases for different configurations

### Starting fresh with Amazon Connect

In this case, simply select new numbers using the claim a number process. For
instructions, see [Get a local toll-free or DID Amazon Connect phone
number](get-connect-number.md "get-connect-number.md").

### Migrating to Amazon Connect from another

provider/platform

If you're migrating to Amazon Connect from other platform, we recommend starting with a
proof of concept, and migrating to Amazon Connect over time.

- A best practice is to forward your existing numbers to a new number
  (or numbers) claimed in Amazon Connect until you are fully converted.
- After fully converting, use the [porting process](port-phone-number.md "port-phone-number.md") to bring your numbers into Amazon Connect.
- This gives you a fallback in case you have migration issues.

### Maintaining two separate

platforms

In some cases, you may have more than one Contact Center platform requiring
telephony. Here's an overview of how to configure this:

- Choose which platform is the initial call-handling service, and
  forward to the other platform.
- If Amazon Connect is the primary call handling platform, you can port or claim
  numbers. You will design your flows to transfer calls to the other
  platform on a telephone number you will provide in the flow.
- If the external platform is the primary call handler, you will need to
  configure that platform to forward calls to a number you claim in Amazon Connect.
  Choose either a toll-free number, which will give you better redundancy
  and capacity at an increased cost, or a bank of DID numbers to terminate
  the call into Amazon Connect.
- For the use case, we recommend that you engage AWS Solution
  Architecture support to ensure your contact center is well-architected
  to achieve the best possible outcomes.
