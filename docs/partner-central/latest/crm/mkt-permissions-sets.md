# AWS Marketplace permission sets

The CRM connector supports the following primary AWS Partner personas. Partners enable the personas by giving the Salesforce user the corresponding permission set included in
the application.

###### Topics

- [AWS Marketplace administrator](#aws-marketplace-administrator "#aws-marketplace-administrator")
- [AWS Marketplace user](#aws-marketplace-user "#aws-marketplace-user")
- [AWS Channel Partner user](#aws-channel-partner-user "#aws-channel-partner-user")

## AWS Marketplace administrator

Assign this persona to a systems or Business Administrator to perform the configuration and manage schedules.
This persona provides full access to the AWS Marketplace integration in the Salesforce connector.

This persona can do the following:

- Read, write, and view records for all objects related to the AWS Marketplace integration.
- View all AWS Marketplace sync log records.
- Create schedules related to AWS Marketplace entities.

###### Note

Certain settings in Salesforce require additional access, specifically
named credentials and custom settings that AWS Partners must provide to users.
However, if partners pair this permission set with a Salesforce systems
administrator profile, all permissions needed to fully configure the application
should work.

## AWS Marketplace user

Assign this persona to the user who creates and manages private offers and resale authorization.

The AWS Marketplace user can do the following:

- Synchronize AWS Marketplace products, offers, and resale authorizations.
- Modify expiry dates, and cancel and clone offers and resale authorizations.
- Access the AWS Marketplace dashboard.

## AWS Channel Partner user

The AWS Channel Partner user can do the following:

- View available shared resale authorizations created by the Independent Software Vendor (ISV) seller.
- View and create AWS Channel Partner private offers from shared resale authorizations.
