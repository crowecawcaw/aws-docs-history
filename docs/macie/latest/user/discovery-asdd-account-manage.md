# Configuring automated sensitive data discovery

To gain broad visibility into where sensitive data might reside in your Amazon Simple Storage Service (Amazon S3) data
estate, enable and configure automated sensitive data discovery for your account or organization. Amazon Macie then evaluates
your S3 bucket inventory on a daily basis and uses sampling techniques to identify and select
representative S3 objects from your buckets. Macie retrieves and analyzes the selected objects,
inspecting them for sensitive data. If you're the Macie administrator for an organization, by default this
includes objects in S3 buckets that your member accounts own.

As the analysis progresses each day, Macie produces records of the sensitive data it finds
and the analysis that it performs. Macie also updates statistics, inventory data, and other
information that it provides about your Amazon S3 data. The resulting data provides insight into where
Macie found sensitive data in your Amazon S3 data estate, which can span all the S3 buckets for your
account or organization. For more information, see [How automated sensitive data discovery works](discovery-asdd-how-it-works.md "discovery-asdd-how-it-works.md").

If you have a standalone Macie account or you're the Macie administrator for an organization, you can
configure and manage automated sensitive data discovery for your account or organization. This includes enabling and
disabling automated discovery, and configuring settings that define the scope and nature of the analyses that
Macie performs. If you have a member account in an organization, contact your Macie administrator to learn
about the settings for your account and organization.

###### Topics

- [Prerequisites for configuring
  automated sensitive data discovery](discovery-asdd-account-configure-prereqs.md "discovery-asdd-account-configure-prereqs.md")
- [Enabling automated sensitive data discovery](discovery-asdd-account-enable.md "discovery-asdd-account-enable.md")
- [Configuring settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md")
- [Disabling automated sensitive data discovery](discovery-asdd-account-disable.md "discovery-asdd-account-disable.md")
