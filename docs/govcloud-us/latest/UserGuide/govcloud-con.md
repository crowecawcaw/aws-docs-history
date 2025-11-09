# Amazon Connect in AWS GovCloud (US)

This service is currently available in AWS GovCloud (US-West) only.

Amazon Connect is an easy to use omnichannel cloud contact center that helps you provide superior customer service at a lower cost. It provides a seamless experience across voice and chat for your customers and agents. This includes one set of tools for skills-based routing, powerful real-time and historical analytics, and intuitive management tools – all with pay-as-you-go pricing, which means Amazon Connect simplifies contact center operations, improves agent efficiency, and lowers costs. You can set up a contact center in minutes that can scale to support millions of customers from the office or as a virtual contact center.

## How Amazon Connect differs for AWS GovCloud (US)

Amazon Connect in AWS GovCloud (US) differs from other commercial Regions in the following ways:

- Amazon Connect instances in AWS GovCloud (US) use the domain **\*.govcloud.connect.aws**
- It supports only the [latest Contact Control Panel](../../../connect/latest/adminguide/upgrade-to-latest-ccp.md "../../../connect/latest/adminguide/upgrade-to-latest-ccp.md") (CCP) for both voice and chat contacts for agents. The earlier CCP is not supported.
- It supports only the latest contact search experience, as described in [What’s new in contact search](../../../connect/latest/adminguide/contact-search.md#new-contact-search-experience "../../../connect/latest/adminguide/contact-search.md#new-contact-search-experience").
- Amazon Connect in AWS GovCloud (US) is in a separate partition from all commercial Regions. Therefore it does not support cross-partition integration with other AWS services – such as Amazon Lex, Amazon Lambda, Amazon Kinesis, Amazon S3, Amazon CloudWatch, amongst others – that are available in commercial Regions.
- The following Amazon Connect features are not supported.
  - Amazon Connect Customer Profiles
  - Amazon Q in Connect
  - Amazon Connect Voice ID
  - Amazon Connect Live Media Streaming
  - Amazon Connect Chat integration with Apple Business Chat
  - Amazon Connect Cases
  - Amazon Connect Outbound Campaigns
  - Granular access controls for real-time metrics
  - Amazon Connect Contact Lens GenAI features and the [ListRealTimeContactAnalysisSegments](../../../connect/latest/APIReference/API_connect-contact-lens_ListRealtimeContactAnalysisSegments.md "../../../connect/latest/APIReference/API_connect-contact-lens_ListRealtimeContactAnalysisSegments.md") API

## Documentation for Amazon Connect

[Amazon Connect documentation](../../../connect/latest/adminguide/what-is-amazon-connect.md "../../../connect/latest/adminguide/what-is-amazon-connect.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon Connect instance and resource configuration metadata is not permitted to contain export-controlled data. This metadata includes all configuration data (for example, name, alias, description, tags) that you enter when creating and maintaining your Amazon Connect instance and resources within an instance, such as users, queues, routing profiles, contact flows, or scheduled report names.
