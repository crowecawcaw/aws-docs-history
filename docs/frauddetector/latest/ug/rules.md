Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Rules

A rule is a condition that tells Amazon Fraud Detector how to interpret variable values during a fraud prediction. A rule is part of a detector logic and it consists of the following elements:

- **Variable or List** – Variable represents a data element in your event dataset that you want to use in a fraud prediction.
  A list is a set of input data elements for a variable in your event dataset. Variables used in a rule must be predefined in the evaluated event type and lists used in a rule must be associated with a variable type. For more information, see [Variables](variables.md "variables.md") and [Lists](lists.md "lists.md").
- **Expression** – An expression in a rule captures your business logic. If you are using variable in your rule, a simple rule expression is constructed using a
  variable, a comparison operator such as >, <, <=, >=. == , and a value. If you are using a list, rule expression is constructed as list entry, `in`, and the list name. For more information, see [Rule language reference](rule-language-reference.md "rule-language-reference.md").
  You can combine multiple expressions together using `and` and `or`. All expressions must evaluate to a Boolean value (true or false) and be less than 4,000 characters in length.
  If-else type conditions are not supported.
- **Outcome** – An outcome is a response returned by Amazon Fraud Detector when a rule is matched. The outcome indicates the result of a fraud prediction.
  You can create outcomes for each possible fraud prediction and add them to a rule. For more information, see [Outcomes](outcomes.md "outcomes.md").
  A detector must have at least one associated rule. A rule can have up to 3 lists, and a detector can have up to 30 lists. You create rule as part of the detector creation process. You can also create and associate new rules with an existing detector.
