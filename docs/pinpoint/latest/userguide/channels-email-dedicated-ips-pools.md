**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Creating dedicated IP pools

If you purchased several dedicated IP addresses to use with Amazon Pinpoint, you can create groups
of those addresses. These groups are called _dedicated IP
pools_. A common scenario is to create one pool of dedicated IP addresses for
sending marketing communications, and another for sending transactional emails. Your sender
reputation for transactional emails is then isolated from that of your marketing emails. In
this scenario, if a marketing campaign generates a large number of complaints, the delivery
of your transactional emails isn't impacted.

Dedicated IP pools are available for use in both Amazon Pinpoint and Amazon Simple Email Service (Amazon SES). When you
create a dedicated IP pool, you have to choose a configuration set to associate it with.
Currently, you can only manage configuration sets and IP pools using Amazon SES. For more
information about setting up configuration sets, see [Creating
configuration sets](../../../ses/latest/dg/creating-configuration-sets.md "../../../ses/latest/dg/creating-configuration-sets.md") in the _Amazon Simple Email Service Developer Guide_. For more
information about setting up dedicated IP pools, see Creating dedicated IP pools in the
_Amazon Simple Email Service Developer Guide_.

In order to use configuration sets (and therefore, dedicated IP pools) with Amazon Pinpoint, you
must configure the configuration set as the default configuration set for the email
identities that you use with Amazon Pinpoint. For more information, see [Applying a
configuration set to an email identity](channels-email-manage-configuration-sets.md#channels-email-manage-configuration-sets-applying "channels-email-manage-configuration-sets.md#channels-email-manage-configuration-sets-applying").
