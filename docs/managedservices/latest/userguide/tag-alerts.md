# Tag-based alert notifications in AMS

Use tags to send alert notifications for your resources to different email addresses. It's a best practice to use tag-based alert notifications because notifications sent to a single email address
might cause confusion when multiple developer teams use the same account.

###### Important

Tag-based alert notifications only work for notifications related to Amazon EC2, Amazon EBS, Elastic Load Balancing, Network Load Balancer, Application Load Balancer, Amazon RDS, Amazon Redshift, and OpenSearch.

Don't add personally identifiable information (PII) in your tags.

**Send alerts to a specific email address**

Tag resources that have alerts that must be sent to a specific email address with the `key = OwnerTeamEmail`, `value = `EMAIL_ADDRESS``.

**Send alerts to multiple email addresses**

To use multiple email addresses, specify a comma-separated list of values. For example, `key = `OwnerTeamEmail``, `value = `EMAIL_ADDRESS_1`, `EMAIL_ADDRESS_2`, `EMAIL_ADDRESS_3`, ...`.
The total number of characters for the value field cannot exceed 260.

**Use a custom tag key**

To use a custom tag key, provide the custom tag key name to your CSDM in
an email providing consent to activate automated notification for the tag-based communication.
It's a best practice to use the same tagging strategy for contact tags across all your instances and resources.

The email address must be specified in full, with the "at sign" (@) to separate the local part from the domain.
Examples of invalid email addresses: `Team.AppATabc.xyz` or `john.doe`.
For general guidance on your tagging strategy, see
[Using tags](ex-using-tags.md "ex-using-tags.md").
To tag an existing resource, submit an RFC with the Deployment | Advanced stack components | Tag | Create (auto) (ct-3cx7we852p3af) change type.

###### Note

The key value `OwnerTeamEmail` does not have to be in camel case. However, tags are case sensitive and it's best practice
to use the recommended format.
