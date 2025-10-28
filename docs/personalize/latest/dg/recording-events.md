# Recording real-time events to influence recommendations

An _event_ is an interaction between a user and your catalog. It
can be an interaction with an _item_, such as a user
purchasing an item or watching a video, or it can be taking an _action_, such as applying for a credit card
or enrolling in a membership program.

Amazon Personalize can make recommendations based on real-time event data only, historical event data only, or a mixture of both.
Record real-time events as your customers interact with
recommendations. This builds out your interactions data and keeps
your data fresh. And it tells Amazon Personalize about the current interests of your user, which can improve
recommendation relevance.

If your domain use case or custom recipe supports [real-time
personalization](use-case-recipe-features.md#about-real-time-personalization "use-case-recipe-features.md#about-real-time-personalization"), Amazon Personalize uses events in real time to update and adapt recommendations according to a user's evolving
interest.

How you record real-time events depends on the type of interactions data you are importing:

- For _item interactions_, you record real-time events with the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") API operation. Amazon Personalize appends this data to the [item interaction](interactions-datasets.md "interactions-datasets.md") data in your dataset group. For more information, see [Recording real-time item interaction events](recording-item-interaction-events.md "recording-item-interaction-events.md").
- For _action interactions_, you record real-time events with the [PutActionInteractions](API_UBS_PutActionInteractions.md "API_UBS_PutActionInteractions.md") API operation. Amazon Personalize appends
  this data to the [Action interactions dataset](action-interactions-datasets.md "action-interactions-datasets.md") in your dataset group.
  Only the PERSONALIZED_ACTIONS recipes use action interactions data. For more information, see [Recording real-time action interaction events](recording-action-interaction-events.md "recording-action-interaction-events.md").

###### Topics

- [How real-time
  events influence recommendations](#recorded-events-influence-recommendations "#recorded-events-influence-recommendations")
- [Recording real-time item interaction events](recording-item-interaction-events.md "recording-item-interaction-events.md")
- [Recording real-time action interaction events](recording-action-interaction-events.md "recording-action-interaction-events.md")
- [Recording events for
  anonymous users](#recording-anonymous-user-events "#recording-anonymous-user-events")
- [Third-party event tracking services](#record-events-third-parties "#record-events-third-parties")
- [Sample
  implementations](#recording-events-sample-architecture "#recording-events-sample-architecture")

## How real-time

events influence recommendations

If your recipe supports real-time personalization, after you create a recommender or custom campaign,
Amazon Personalize uses new recorded event
data for existing items or actions within seconds of import. The following use cases and recipes support real-time personalization:

- [Recommended for you (ECOMMERCE use case)](ECOMMERCE-use-cases.md#recommended-for-you-use-case "ECOMMERCE-use-cases.md#recommended-for-you-use-case")
- [Top picks for you (VIDEO_ON_DEMAND use case)](VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case "VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case")
- [User-Personalization-v2 recipe](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md")
- [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
- [Personalized-Ranking-v2 recipe](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md")
- [Personalized-Ranking recipe](native-recipe-search.md "native-recipe-search.md")
- [Next-Best-Action recipe](native-recipe-next-best-action.md "native-recipe-next-best-action.md")

If you use the Trending-Now recipe, Amazon Personalize automatically considers items from new events data over configurable intervals. You don't have
to create a new solution version. For more information,
see [Trending-Now
recipe](native-recipe-trending-now.md "native-recipe-trending-now.md").

If the item, action, or user in the event is new, how the Amazon Personalize uses the data depends on your use case or recipe.
For more information, see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

## Recording events for

anonymous users

###### Important

If you don't record at minimum one event with a `sessionId` and `userId` for a user, Amazon Personalize won't use
the activity tracked to only the `sessionId` when training. And after training completes, recommendations will
no longer be based on activity tracked to the `sessionId`. This will create a continuous event history for userIds before and after they log in.

You can record item interaction or action interaction events for users before they create an account.
Record events for anonymous users to build a continuous event history
with events from before and after they log in. This provides Amazon Personalize more
interactions data about the user, which can help generate more relevant
recommendations.

To record events for anonymous users (users who haven't logged in), for each event specify only a `sessionId`.
Your application generates a unique `sessionId` when a user first visits your website or uses your application.
You must use the same `sessionId` in all events throughout the session.
Amazon Personalize uses the
`sessionId` to associate events with the user before they log in.

Amazon Personalize doesn't use events from anonymous users when training until you associate them with a `userId`. For
more information, see [Building a continuous event history for anonymous users](#recording-events-building-continuous-event-history "#recording-events-building-continuous-event-history").

To provide [real-time personalization](use-case-recipe-features.md#about-real-time-personalization "use-case-recipe-features.md#about-real-time-personalization") for anonymous users,
specify the sessionId as the userId in your [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") or GetActionRecommendations request.

- For a code samples that show how to record item interaction events with the PutEvents operation and a sessionId and
  userId, see [Recording a single item interaction event](putevents-example.md "putevents-example.md").
- For a code samples that show how to record action interaction events with the PutActionInteractions operation and a
  sessionId and userId, see [Recording a single action interaction event](record-single-action-interaction.md "record-single-action-interaction.md").

### Building a continuous event history for anonymous users

To build an event history for an anonymous user
and have Amazon Personalize use their events when training, record at minimum one
event with both a `sessionId` and a `userId`. Then you can record any number of events for the
`userId`. After you start providing a `userId`, the `sessionId` can change. During the
next full retraining, Amazon Personalize associates the `userId` with the
anonymous user history tracked to the original `sessionId`.

After retraining completes, recommendations will be based on activity
tracked to both the `sessionId` from the anonymous events and any events
tracked to their `userId`.

###### Note

If your user doesn't create an account and you want Amazon Personalize to use the data when training, you can use the
`sessionId` as the `userId` in events. However, if the user eventually creates an account, you
won't be able to associate the events from their anonymous browsing with their new `userId`.

## Third-party event tracking services

The following Customer Data Platforms (CDPs) can help you collect event data from
your application and send it to Amazon Personalize.

- **Amplitude** – You can use Amplitude to track
  user actions to help you understand your users' behavior.
  For information on using Amplitude and Amazon Personalize, see the following
  AWS Partner Network (APN) blog post: [Measuring the Effectiveness of Personalization with Amplitude and Amazon Personalize](https://aws.amazon.com/blogs/apn/measuring-the-effectiveness-of-personalization-with-amplitude-and-amazon-personalize/ "https://aws.amazon.com/blogs/apn/measuring-the-effectiveness-of-personalization-with-amplitude-and-amazon-personalize/").
- **Segment** – You can use Segment to send your data to Amazon Personalize. For more information on integrating Segment with Amazon Personalize, see [Amazon Personalize Destination](https://segment.com/docs/connections/destinations/catalog/amazon-personalize/ "https://segment.com/docs/connections/destinations/catalog/amazon-personalize/").

## Sample

implementations

For a sample Jupyter notebook that shows how to use Amazon Personalize to react to
real-time behavior of users using an event tracker and the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md")
operation, see [2.View_Campaign_And_Interactions.ipynb](https://github.com/aws-samples/amazon-personalize-samples/blob/master/getting_started/notebooks/2.View_Campaign_And_Interactions.ipynb "https://github.com/aws-samples/amazon-personalize-samples/blob/master/getting_started/notebooks/2.View_Campaign_And_Interactions.ipynb") in the **getting_started** folder of the [amazon-personalize-samples](https://github.com/aws-samples/amazon-personalize-samples "https://github.com/aws-samples/amazon-personalize-samples") GitHub repository.

For an example that shows how to stream events from users interacting with recommendations, see [streaming_events](https://github.com/aws-samples/amazon-personalize-samples/tree/master/next_steps/operations/streaming_events "https://github.com/aws-samples/amazon-personalize-samples/tree/master/next_steps/operations/streaming_events") in the Amazon Personalize samples GitHub repository.

For a complete example that contains the source code and supporting
files to deploy real-time APIs that sit between your Amazon Personalize resources and
client applications, see [Real-Time
Personalization APIs](https://github.com/aws-samples/personalization-apis "https://github.com/aws-samples/personalization-apis") in the AWS samples GitHub repository.
This project includes how to implement the following:

- User context and user event collection
- Response caching
- Decorating recommendations based on item metadata
- A/B testing
- API authentication
