Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Lists

A list is a set of input data for a variable in your event dataset. You use the input data in a rule that’s associated with your
detector. A rule is a condition that tells Amazon Fraud Detector how to interpret input data during a fraud prediction. For example, you can create a list of
IP addresses and then create a rule to deny access if a specific IP address is in the list. Rules that use lists are expressed in the
`$ip_address_value` in `@list_name` format.

With Amazon Fraud Detector, you can manage a list by adding or removing data without needing to update an associated rule. A rule associated with your list
automatically incorporates newly added or removed data.

A list can contain up to 100,000 unique entries and each entry can be up to 320 characters long. Every list you use in a rule is, by default, associated
with Amazon Fraud Detector’s [Variable types](variables.md#variable-types "variables.md#variable-types") FREE_FORM_TEXT. You can assign a variable type to your list at any time.
You can use up to 3 lists in a rule.

You can create a list, add entries to the list, delete a list, or delete one or more entries in the list, or assign a variable type to your list in the Amazon Fraud Detector console, using the API, using the AWS CLI,
or using the AWS SDK.
