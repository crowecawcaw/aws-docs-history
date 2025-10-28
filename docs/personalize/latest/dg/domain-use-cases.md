# Choosing a use case

When you create a recommender in a Domain dataset group, you specify a
use case. Amazon Personalize trains the models backing the recommender with the best configurations for the use case. Each domain has different use cases. For example,
if you specify _VIDEO_ON_DEMAND_ for your Domain dataset group, only VIDEO_ON_DEMAND use cases are available. Each use case
has different requirements for getting recommendations. Some use cases require specific event types. You are free to include additional event types.

For all use cases, your interactions data must have the following:

- At minimum 1000 item interactions records from users interacting with items in your catalog.
  These interactions can be from bulk imports, or streamed events, or both.
- At minimum 25 unique user IDs with at least two item interactions for each.
  For quality recommendations, we recommend that you have at minimum 50,000 item interactions from at least 1,000 users with two or more item interactions each.

###### Topics

- [VIDEO_ON_DEMAND use
  cases](VIDEO_ON_DEMAND-use-cases.md "VIDEO_ON_DEMAND-use-cases.md")
- [ECOMMERCE use cases](ECOMMERCE-use-cases.md "ECOMMERCE-use-cases.md")
