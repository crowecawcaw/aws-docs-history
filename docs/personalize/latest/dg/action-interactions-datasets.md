# Preparing action interaction data for training

If you use the [Next-Best-Action](native-recipe-next-best-action.md "native-recipe-next-best-action.md") custom recipe, Amazon Personalize uses action interactions data
to identify user interest and predict the actions they will most likely take. An _action interaction_ is an
interaction involving a user and an action in your [Actions dataset](actions-datasets.md "actions-datasets.md"). For example, if
you have an _enroll_ action in your Actions dataset, and a user takes this action, you would record the
user's ID, the action's ID, the timestamp, and for event type, record `TAKEN`.

You import action interactions into an Amazon Personalize _Action interactions dataset_. You can import action
interaction events in bulk with a dataset import job, or you can stream them in real time with the [PutActionInteractions](API_UBS_PutActionInteractions.md "API_UBS_PutActionInteractions.md") API operation.
You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group.

Your bulk action interactions data must be in a CSV file. Each row in the file should represent a unique interaction between a user
and an action. After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

The following sections provide more information on how to prepare your action interaction data for Amazon Personalize. For
bulk data format guidelines for all types of data, see [bulk data format guidelines](preparing-training-data.md#general-formatting-guidelines "preparing-training-data.md#general-formatting-guidelines").

###### Topics

- [Action interaction data requirements](#action-interaction-requirements "#action-interaction-requirements")
- [Event type data](#action-interaction-event-type-data "#action-interaction-event-type-data")
- [Action interactions data example](#action-interactions-data-schema-example "#action-interactions-data-schema-example")

## Action interaction data requirements

There is no minimum requirement for action interactions data. We recommend that you import it for quality action
recommendations. If you don't have action interaction data, you can create an empty Action interactions dataset and record your
customers' interactions with actions by using the [PutActionInteractions](API_UBS_PutActionInteractions.md "API_UBS_PutActionInteractions.md") API operation.

Your action interactions data must have at minimum the
following columns. You are free to add additional custom columns depending on your use case and your data.

- USER_ID – The unique identifier of the user who interacted with the item. Every event must have an USER_ID.
  It must be a `string` with a max length of 256 characters.
- ACTION_ID – The unique identifier of the item that the user interacted with. Every event must have an item
  ID. It must be a `string` with a max length of 256 characters.
- TIMESTAMP – The time the event occurred (in Unix epoch time format in seconds). Every action interaction
  must have an TIMESTAMP. For more information, see [Timestamp data](interactions-datasets.md#timestamp-data "interactions-datasets.md#timestamp-data").
- EVENT_TYPE – Whether the action was Taken, Not taken, or Viewed. Every action interaction must have an event
  type. For more information, see [Event type data](#action-interaction-event-type-data "#action-interaction-event-type-data").

Until you import action interaction data, Amazon Personalize recommends actions in your without
personalization, and propensity scores are 0.0.
An action will have a score after the action has the following:

- At least 50 action interactions with the TAKEN event type.
- At least 50 action interactions with the NOT_TAKEN or VIEWED event type.

These action interactions must be present at the latest solution version training, and must occur within a span of 6 weeks from the
latest interaction timestamp in the Action interactions dataset.

## Event type data

Amazon Personalize can use patterns in event type data to identify the actions your users will most likely take. For example, if a
customer frequently ignores an email subscription action (indicated with the NOT_TAKEN event type), Amazon Personalize might adjust
recommendations to feature fewer of this type of action.

You can use only the following event types for action interaction events. Amazon Personalize uses these events to learn about your
user and calculate what actions to recommend next.

- Taken – Record _Taken_ events when a user takes a recommended action.
- Not Taken – Record _Not Taken_ events when your user makes a deliberate choice to not take
  the action after viewing it. For example, if they choose _No_ when you show them the action.
  _Not Taken_ events can indicate the customer isn’t interested in the action.
- Viewed – Record _Viewed_ events when you show a user an action before they make a choice
  to take or not take an action. Amazon Personalize uses _View_ events to learn about your users' interests. For
  example, if a user views an action but doesn't take it, this user might not be interested in this action in the future.

## Action interactions data example

The first few lines of a CSV file with action interaction data and all required columns might look like the
following.

```
USER_ID,ACTION_ID,EVENT_TYPE,TIMESTAMP
35,73,Viewed,1586731606
54,35,Not taken,1586731609
9,33,Viewed,1586735158
23,10,Taken,1586735697
27,11,Taken,1586735763
...
...
```

After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").
This is what the schema JSON file would look like for the above sample data.

```
{

  "type": "record",
  "name": "ActionInteractions",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
      {
          "name": "USER_ID",
          "type": "string"
      },
      {
          "name": "ACTION_ID",
          "type": "string"
      },
      {
          "name": "EVENT_TYPE",
          "type": "string"
      },
      {
          "name": "TIMESTAMP",
          "type": "long"
      }
  ],
  "version": "1.0"
}
```
