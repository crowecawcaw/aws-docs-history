# Deciding Between accuracy and cost

Each `FindMatches` transform contains an `accuracy-cost` parameter.
You can use this parameter to specify one of the following:

- If you are more concerned with the transform accurately reporting that two records
  match, then you should emphasize _accuracy_.
- If you are more concerned about the cost or speed of running the transform, then you should
  emphasize _lower cost_.
  You can make this trade-off on the AWS Glue console or by using the AWS Glue machine learning
  API operations.

###### When to favor accuracy

Favor accuracy if you are more concerned about the risk that the `find
 matches` results won't contain matches. To favor accuracy, choose a
_higher_ accuracy-cost trade-off value. With a higher value, the
`FindMatches` transform requires more time to do a more thorough search for
correctly matching records. Note that this parameter doesn't make it less likely to falsely
call a nonmatching record pair a match. The transform is tuned to bias towards spending more
time finding matches.

###### When to favor cost

Favor cost if you are more concerned about the cost of running the `find
 matches` transform and less about how many matches are found. To favor cost, choose
a _lower_ accuracy-cost trade-off value. With a lower value, the
`FindMatches` transform requires fewer resources to run. The transform is
tuned to bias towards finding fewer matches. If the results are acceptable when favoring
lower cost, use this setting.

###### How to favor both accuracy and lower cost

It takes more machine time to examine more pairs of records to determine whether they
might be matches. If you want to reduce cost without reducing quality, here are some steps
you can take:

- Eliminate records in your data source that you aren't concerned about matching.
- Eliminate columns from your data source that you are sure aren't useful for making a
  match/no-match decision. A good way of deciding this is to eliminate columns that you
  don't think affect your own decision about whether a set of records is “the same.”
