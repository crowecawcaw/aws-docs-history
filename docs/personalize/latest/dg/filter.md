# Filtering recommendations and user segments

When getting recommendations with a domain recommender or custom campaign, you can filter results based on custom
criteria. For example, you might not want to recommend products that a user has already
purchased or recommend only items for a particular age group.

Similarly, with USER_SEGMENTATION recipes, you might not want to include certain
types of users in user segments. By filtering your results, you can control the items that will
be recommended to users or the users that will be included in user segments.

You can create, edit, delete, and apply filters using the Amazon Personalize console, the AWS Command Line Interface
(AWS CLI), and the AWS SDKs.

- For real-time recommendations, you apply a filter and specify any filter parameter values when you call the
  GetRecommendations, GetActionRecommendations, or GetPersonalizedRanking operations. You can also apply
  a filter when you get
  recommendations from a campaign or a recommender in the console.

When you get real-time item recommendations with personalized or related items recipes or use cases, you can specify a promotion in your request. A
_promotion_ uses a filter to define additional business rules that apply to a configurable subset of
recommended items. For more information, see [Promoting items in real-time recommendations](promoting-items.md "promoting-items.md").

- For batch workflows, you include any filter parameter values in your input JSON. Then you specify the filter's Amazon
  Resource Name (ARN) when you create a batch inference job or batch segment job. For more information, see [Filtering batch recommendations and user segments (custom resources)](filter-batch.md "filter-batch.md").
  **Filter updates for new records**

For data that you import with the PutEvents or PutActionInteractions operations, Amazon Personalize updates any filters in the dataset
group with the new data within seconds of import. For example, if your filter removes purchased items from recommendations,
and you record a purchase event for a user with the PutEvents operation, this item would be removed from future
recommendations for this user within seconds of recording the event.

For all other data imported in bulk or individually,
Amazon Personalize updates any filters in the dataset group with the new data
within 20 minutes from the last import.

###### Topics

- [Filter expressions](filter-expressions.md "filter-expressions.md")
- [Filtering real-time recommendations](filter-real-time.md "filter-real-time.md")
- [Filtering batch recommendations and user segments (custom resources)](filter-batch.md "filter-batch.md")
