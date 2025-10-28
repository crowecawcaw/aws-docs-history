# Defining sensitive data exceptions with allow lists

With allow lists in Amazon Macie, you can define specific text and text patterns that you want
Macie to ignore when it inspects Amazon Simple Storage Service (Amazon S3) objects for sensitive data. These are typically
sensitive data exceptions for your particular scenarios or environment. If data matches text or a
text pattern in an allow list, Macie doesn’t report the data. This is the case even if the data
matches the criteria of a [managed data identifier](managed-data-identifiers.md "managed-data-identifiers.md")
or a [custom data identifier](custom-data-identifiers.md "custom-data-identifiers.md"). By using allow lists,
you can refine your analysis of Amazon S3 data and reduce noise.

You can create and use two types of allow lists in Macie:

- **Predefined text** – For this type of list, you specify certain
  character sequences to ignore. For example, you might specify the names of public
  representatives for your organization, specific phone numbers, or specific sample data that your
  organization uses for testing. If you use this type of list, Macie ignores text that exactly
  matches an entry in the list.

This type of allow list is helpful if you want to specify words, phrases, and other kinds
of character sequences that aren’t sensitive, aren’t likely to change, and don’t necessarily
adhere to a common pattern.

- **Regular expression** – For this type of list, you specify a
  regular expression (_regex_) that defines a text pattern to
  ignore. For example, you might specify the pattern for your organization's public phone numbers,
  email addresses for your organization’s domain, or patterned sample data that your organization
  uses for testing. If you use this type of list, Macie ignores text that completely matches the
  pattern defined by the list.

This type of allow list is helpful if you want to specify text that isn’t sensitive but
varies or is likely to change while also adhering to a common pattern.
After you create an allow list, you can [create and
configure sensitive data discovery jobs](discovery-jobs-create.md "discovery-jobs-create.md") to use it, or [add it to your settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md"). Macie then
uses the list when it analyzes data. If Macie finds text that matches an entry or pattern in an
allow list, Macie doesn’t report that occurrence of text in sensitive data findings, statistics,
and other types of results.

You can manage and use allow lists in all the AWS Regions where Macie is currently
available except the Asia Pacific (Osaka) Region.

###### Topics

- [Configuration options for allow
  lists](allow-lists-options.md "allow-lists-options.md")
- [Creating an allow list](allow-lists-create.md "allow-lists-create.md")
- [Checking the status of an allow
  list](allow-lists-status-check.md "allow-lists-status-check.md")
- [Changing an allow list](allow-lists-change.md "allow-lists-change.md")
- [Deleting an allow list](allow-lists-delete.md "allow-lists-delete.md")
