# Matching your use case to Amazon Personalize resources

Amazon Personalize recommendations can address the following use cases:

- Generating personalized recommendations for a user
- Recommending similar or related items
- Recommending trending or popular items
- Recommending the next best actions for a user (only with custom resources)
- Re-ordering by relevance (only with custom resources)
- Generating user segments (only with custom resources)
  Amazon Personalize features domain based resources and custom resources configured for these use cases. You start by creating a
  Domain dataset group or a Custom dataset group:

- With a _Domain dataset group_, you create resources that are pre-configured and optimized
  for the VIDEO_ON_DEMAND or ECOMMERCE domains.

If you have a streaming video or e-commerce application, we recommend that you start with a Domain dataset group. You
can still add custom resources, such as solutions and solution versions trained for custom use cases. And you can still
use custom resources to get batch recommendations. You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group.

- With a _Custom dataset group_, you choose a recipe that matches your use case. You then train
  and deploy only configurable solutions and solution versions (trained Amazon Personalize recommendation models). When ready,
  you can deploy the solution version in a campaign for real-time recommendations. Or you can get
  batch recommendations without a campaign.

If you don't have a
streaming video or e-commerce application, we recommend that you create a Custom dataset group. Otherwise, start with
a Domain dataset group and adding custom resources as necessary.
The following sections provide detailed information about the use cases and custom recipes available in Amazon Personalize. When you
match your use case to an Amazon Personalize resource, note its data requirements. After you choose a use case or recipe, this information
can help as you prepare your data in [Preparing training data for Amazon Personalize](preparing-training-data.md "preparing-training-data.md").

###### Topics

- [Use case and recipe features](use-case-recipe-features.md "use-case-recipe-features.md")
- [Choosing a use case](domain-use-cases.md "domain-use-cases.md")
- [Choosing a
  recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md")
