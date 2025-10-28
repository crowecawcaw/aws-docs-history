# Optimize your reputation for outbound

calling in Amazon Connect

In the contact center industry one of the most difficult tasks is understanding why
customers don't answer calls when you dial out. Is the customer deliberately not
answering, or are they busy on a work call or answering the door? For contact centers
it's impossible to know but there are things you can do about it.

This topic provides recommended steps you can take to improve your call answer rates
for outbound calling.

## Step 1: Know your

customer's preferred contact method

One of the biggest mistakes that contact centers make is not knowing whether the
customer wants to be contacted by telephone call. When the customer engaged with
you, did you check whether they want to be reached by phone, e-mail, or text?

Businesses with multi-channel engagement outperform 70% on average compared to
business without multi-channel engagement.

## Step 2: Brand your calls

By using call branding solutions, you can provide enhanced call displays that
include your business name, logos, reason for the call, and your service. Branding
your calls increases the call answer rate by 30%.

Amazon Connect partners with solutions providers like [First
Orion](https://firstorion.com/amazon-connect-branded-calling-now-available/ "https://firstorion.com/amazon-connect-branded-calling-now-available/") and Neustar to offer branded calling services.

## Step 3: Select caller IDs that mean something

to your customer

Not every contact center is the same. What works for some might not work for
others. But there are correlations in how successful outbound campaigns are based on
your caller ID. Following are a few suggestions to try creating meaningful caller
IDs:

- **Area localization**. Use a caller ID in the
  same area as the prospect.
- **City localization**. Use a caller ID in the
  same city as the prospect.
- **Recognizable golden toll free number** such
  as 0800 123 0000.
- **Mobile numbers**. Where countries permit
  this, it may be possible to use a virtual mobile number to dial out from a
  contact center. For a list of countries where Amazon Connect supports mobile numbers,
  see [Region requirements for ordering and porting
  phone numbers in Amazon Connect](phone-number-requirements.md "phone-number-requirements.md").

## Step 4: Make sure your campaign is calling

valid numbers

Maintaining accurate customer contact information is essential for successful
outbound calling operations. Amazon Connect's detailed disconnect reasons help
identify invalid phone numbers in your contact lists. If more than 0.5% of your
calls are failing due to invalid numbers, we recommend implementing regular contact
list maintenance through update campaigns or using services like Amazon Pinpoint for
phone number validation.

## Step 5: Make outbound calls at optimal times

Another strategy for outbound call campaigns is making sure that calls are placed
at the best times. It is critical to never harass your customers or
prospects—no one wants to be contacted multiple times by the same company.
Generally speaking, it is never a good idea to call before 10:00AM or after 5:00PM
as people are at their busiest or need their quiet time. Customers should be called
when it's a good for them, depending on their profile. This may mean that one
customer should be called around noon, while another is more accessible in the
afternoon.

In addition, there are regulations such as TCPA (in the US) and OFCOM (in the UK)
that provide guidance on when not to call end customers. We strongly recommend that
you abide by such regulations.

## Step 6: Manage and monitor the reputation of

your caller IDs

For US-based operations, registering your business numbers with services like Free
Caller Registry is essential for managing your caller ID reputation. Amazon
Connect's Contact Trace Record disconnect reasons help you identify when your
numbers are experiencing carrier-level blocking.

We recommend assigning dedicated resources to monitor your number reputation and
address blocking issues from carriers or third-party websites. Consider these
important factors:

1. Third-party blocking services like Hiya.com can implement automatic blocks
   based on user report thresholds
2. On specific devices, such as Samsung phones, blocking can make up to 20%
   of your prospects unreachable
3. Online complaints about specific caller IDs can significantly impact
   answer rates, as prospects often search numbers before answering

If your caller ID has been flagged, switching to a new phone number is typically
the fastest way to restore connectivity.

## Step 7: Use multiple numbers as a

callerID

Today, outbound contact centers typically embrace an intelligent, more efficient
manner of dialing.

For example, one method is to use multiple phone numbers when placing outbound
calls. Customers are more likely to answer a call if they feel that they are not
being called repeatedly by the same number. In fact, using the same phone number
repeatedly is a sure way to annoy customers and prospects who may feel they are
being contacted too often.

## Step 8: Engage with App Vendors

Apps that provide on-device call blocking are common across all major handsets.
Many apps use blocking services from other commercial entities, some allow users to
crowdsource spam numbers, and others partner with major carriers. Unblocking your
numbers across geographies and app providers is often challenging and sometimes
requires payment of fees. Some providers offer free business registration programs,
while others provide no opportunities for redress. You might need to research the
common apps in your region or those used by your customer base and work with these
services directly.

## Step 9: Add messaging to your outreach strategy to

let customers know who you are

It's inevitable that you'll end up with a list of unanswered calls that you
weren't able to connect. There are a variety of creative ways to use SMS with
prospects. Here are some ideas to increase answer rates with your prospects.

1. Send an SMS before calling, letting them know who you are and when you
   will be calling, optionally allowing them to reschedule to a more convenient
   time.
2. If the prospect doesn't answer, send an SMS to allow them to reschedule
   the call or request a call back.
3. Re-engage with prospects with promotional offers or discounts that
   resonates with your prospects.

## Step 10: Validate your outbound calling

strategy

Data-driven decisions and continuous improvement are key to delivering business
value through your outbound calling strategy. Treat each operational change as an
experiment, ensuring you can measure and compare its effectiveness.

We recommend creating custom reports that track both customer reachability and
specific business outcomes. You can combine Contact Trace Record data with your own
metrics using Amazon Connect's data lake or AWS services like QuickSight. Once you
establish a baseline, you can evaluate changes and optimize for success.
