# Connect Customer in AWS GovCloud (US)

Amazon Connect Customer is an easy to use omnichannel cloud contact center that helps you provide superior customer service at a lower cost. It provides a seamless experience across voice and chat for your customers and agents. This includes one set of tools for skills-based routing, powerful real-time and historical analytics, and intuitive management tools – all with pay-as-you-go pricing, which means Amazon Connect Customer simplifies contact center operations, improves agent efficiency, and lowers costs. You can set up a contact center in minutes that can scale to support millions of customers from the office or as a virtual contact center.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)

## How Connect Customer differs

The following differences apply to Connect Customer:

- Amazon Connect Customer instances in AWS GovCloud (US) use the domain **\*.govcloud.connect.aws**
- It supports only the [latest Contact Control Panel](../../../connect/latest/adminguide/upgrade-to-latest-ccp.md "../../../connect/latest/adminguide/upgrade-to-latest-ccp.md") (CCP) for both voice and chat contacts for agents. The earlier CCP is not available.
- It supports only the latest contact search experience, as described in [What’s new in contact search](../../../connect/latest/adminguide/contact-search.md#new-contact-search-experience "../../../connect/latest/adminguide/contact-search.md#new-contact-search-experience").
- Amazon Connect Customer in AWS GovCloud (US) is in a separate partition from all commercial Regions. Therefore it does not support cross-partition integration with other AWS services – such as Amazon Lex, Amazon Lambda, Amazon Kinesis, Amazon S3, Amazon CloudWatch, amongst others – that are available in commercial Regions.
- The following Amazon Connect Customer features are not available.

  - Agentic CX designer
  - AI agents
  - Email channel
  - Cases
  - Outbound campaigns
  - Chat integration with Apple Business Chat
  - Customer profiles
  - Conversational analytics AI features
  - Live media streaming

## Documentation

- [Connect Customer documentation](../../../connect/latest/adminguide/what-is-amazon-connect.md "../../../connect/latest/adminguide/what-is-amazon-connect.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon Connect Customer instance and resource configuration metadata is not permitted to contain export-controlled data. This metadata includes all configuration data (for example, name, alias, description, tags) that you enter when creating and maintaining your Amazon Connect Customer instance and resources within an instance, such as users, queues, routing profiles, contact flows, or scheduled report names.
