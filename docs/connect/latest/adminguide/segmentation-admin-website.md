# Set up customer segments in

Amazon Connect Customer Profiles

A _customer segment_ is a group of customer profiles that share
certain attributes. For example, a customer segment might contain all of your customers
who live in a particular city, or all customers who are frequent callers and whose
average spend is more than 500 dollars. With Amazon Connect Outbound campaigns, you can
send campaigns to a customer segment.

Customer segments are dynamically evaluated based on attributes that you define, and
can change over time when the value of the attributes change. For example, if you add
new profiles to Customer Profiles domain, or if you modify or delete existing profiles, the number of
profiles in that customer segment may increase or decrease. For more information about
creating a customer segment, see [Build customer segments in
Amazon Connect](customer-segments-building-segments.md "customer-segments-building-segments.md").

As a prerequisite to building segments in Amazon Connect, your administrator must
setup your domain in the AWS Management Console and configure integrations to bring
profile, order, asset, and/or case data into Customer Profiles. For more information, see [Enable Customer Profiles for your Amazon Connect instance](enable-customer-profiles.md "enable-customer-profiles.md").
Enabling data integrations will let continue to generate your dynamic segments based on
new data coming to your domain

Customer segments only contain customer profiles in your Amazon Connect Customer Profiles domain. Customer Profiles can be
ingested from S3 or external applications, or created through Agent App, Contact Flows,
or API. For more information about customer profiles, see [What is a customer profile in
Amazon Connect?](customer-profiles-what-data.md "customer-profiles-what-data.md").

###### Contents

- [Build customer
  segments](customer-segments-building-segments.md "customer-segments-building-segments.md")
- [Manage
  segments](customer-segments-managing-segments.md "customer-segments-managing-segments.md")
- [Create segments from
  imported files](customer-segments-imported-files.md "customer-segments-imported-files.md")
- [Export segments to
  a CSV file](customer-segments-exporting-segments.md "customer-segments-exporting-segments.md")
- [Use the segment AI assistant](customer-segments-ai-assistant.md "customer-segments-ai-assistant.md")
- [Troubleshooting](customer-segments-troubleshooting.md "customer-segments-troubleshooting.md")
