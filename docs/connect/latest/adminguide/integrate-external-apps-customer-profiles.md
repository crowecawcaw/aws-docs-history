# Integrate external

applications with Amazon Connect Customer Profiles

Amazon Connect provides a set of pre-built integrations powered by Amazon AppFlow and Amazon EventBridge. After
you enable Amazon Connect Customer Profiles, you can use these integrations to combine information from external
applications such as Salesforce or Zendesk, with contact history from Amazon Connect. This
creates a customer profile that has all the information agents need during customer
interactions in a single place.

You can also use Customer Profiles in Amazon AppFlow. Amazon AppFlow supports
`CustomerProfiles` as a destination. You can use Amazon AppFlow APIs to send data
into Customer Profiles using `CustomerProfiles` as the destination name.

Before you begin, make sure you are using a customer managed key. For more information about
configuring KMS keys, see [Create a KMS key to
be used by Customer Profiles to encrypt data (required)](enable-customer-profiles.md#enable-customer-profiles-awsmanagedkey "enable-customer-profiles.md#enable-customer-profiles-awsmanagedkey").

## Set up integrations

You can setup an integration using either featured applications in Amazon Connect or
external applications using Amazon AppFlow by choosing the method that best fits your
use-case below. For more detailed information on the integration of ServiceNow and
Slack, see the blog post [Combine data from multiple sources
using Amazon AppFlow and build a unified Amazon Connect Customer profile for contact center
agents](https://aws.amazon.com/blogs/contact-center/unified-customer-data/ "https://aws.amazon.com/blogs/contact-center/unified-customer-data/").

###### Contents

- [Set up integration
  for featured applications in Amazon Connect](integrate-customer-profiles-appflow.md "integrate-customer-profiles-appflow.md")
- [Set up
  integration for external applications using Amazon AppFlow](integrate-external-applications-appflow.md "integrate-external-applications-appflow.md")
- [Delete Customer Profiles or stop
  integrations](delete-customer-profile-connection.md "delete-customer-profile-connection.md")
