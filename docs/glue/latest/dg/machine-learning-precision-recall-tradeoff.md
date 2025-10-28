# Deciding between precision and recall

Each `FindMatches` transform contains a `precision-recall`
parameter. You use this parameter to specify one of the following:

- If you are more concerned about the transform falsely reporting that two records match
  when they actually don't match, then you should emphasize _precision_.
- If you are more concerned about the transform failing to detect records that really do
  match, then you should emphasize _recall_.
  You can make this trade-off on the AWS Glue console or by using the AWS Glue machine learning API
  operations.

###### When to favor precision

Favor precision if you are more concerned about the risk that `FindMatches`
results in a pair of records matching when they don't actually match.

To favor precision, choose a _higher_ precision-recall trade-off value.
With a higher value, the `FindMatches` transform requires more evidence to
decide that a pair of records should be matched. The transform is tuned to bias toward
saying that records do not match.

For example, suppose that you're using `FindMatches` to detect duplicate items
in a video catalog, and you provide a higher precision-recall value to the transform. If your
transform incorrectly detects that _Star Wars: A New Hope_ is the same as
_Star Wars: The Empire Strikes Back_, a customer who wants _A
New Hope_ might be shown _The Empire Strikes Back_. This would
be a poor customer experience.

However, if the transform fails to detect that _Star Wars: A New Hope_
and _Star Wars: Episode IV—A New Hope_ are the same item, the customer
might be confused at first but might eventually recognize them as the same. It would be a
mistake, but not as bad as the previous scenario.

###### When to favor recall

Favor recall if you are more concerned about the risk that the `FindMatches`
transform results might fail to detect a pair of records that actually do match.

To favor recall, choose a _lower_ precision-recall trade-off value. With
a lower value, the `FindMatches` transform requires less evidence to decide that
a pair of records should be matched. The transform is tuned to bias toward saying that
records do match.

For example, this might be a priority for a security organization. Suppose that you are
matching customers against a list of known defrauders, and it is important to determine
whether a customer is a defrauder. You are using `FindMatches` to match the
defrauder list against the customer list. Every time `FindMatches` detects a match
between the two lists, a human auditor is assigned to verify that the person is, in fact, a
defrauder. Your organization might prefer to choose recall over precision. In other words, you
would rather have the auditors manually review and reject some cases when the customer is not
a defrauder than fail to identify that a customer is, in fact, on the defrauder list.

###### How to favor both precision and recall

The best way to improve both precision and recall is to label more data. As you label
more data, the overall accuracy of the `FindMatches` transform improves, thus
improving both precision and recall. Nevertheless, even with the most accurate transform,
there is always a gray area where you need to experiment with favoring precision or recall,
or choose a value in the middle.
