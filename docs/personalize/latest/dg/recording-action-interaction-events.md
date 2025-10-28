# Recording real-time action interaction events

An _action interaction_ event is an interaction between a user and an _action_.
For example, a user enrolling in a membership program or applying for a credit card.

If you use a PERSONALIZED_ACTIONS custom recipe, record real-time action interaction events as your customers interact with
action recommendations. This builds out your interactions data and keeps your data fresh. It also tells Amazon Personalize about the
current interests of your user, which can improve recommendation relevance. Only the PERSONALIZED_ACTIONS custom recipes use
action interactions data.

You record
action interaction events with the [PutActionInteractions](API_UBS_PutActionInteractions.md "API_UBS_PutActionInteractions.md") API operation. Amazon Personalize appends this
data to the [Action interactions dataset](action-interactions-datasets.md "action-interactions-datasets.md") in your dataset group.

An action interaction event must have an event type attribute, which can be one of the following:

- Taken – Record _Taken_ events when a user takes a recommended action.
- Not Taken – Record _Not Taken_ events when your user makes a deliberate choice to not take
  the action after viewing it. For example, if they choose _No_ when you show them the action.
  _Not Taken_ events can indicate that the customer isn't interested in the action.
- Viewed – Record _Viewed_ events when you show a user an action before they make a choice to take or not take an action. Amazon Personalize uses _View_ events to
  learn about your users' interests. For example, if a user views an action but doesn't take it, this user might not be interested in this action in the future.
  You can record real-time events using the AWS SDKs, or
  AWS Command Line Interface (AWS CLI). If you record two events with
  exactly the same timestamp and identical properties, Amazon Personalize keeps only one of the events.

###### Topics

- [Requirements for recording
  action interaction events](#recording-action-interaction-requirements "#recording-action-interaction-requirements")
- [Finding the ID of your action interaction event tracker](action-interaction-tracker-id.md "action-interaction-tracker-id.md")
- [Recording a single action interaction event](record-single-action-interaction.md "record-single-action-interaction.md")
- [Recording multiple action interaction events](recording-multiple-action-interactions.md "recording-multiple-action-interactions.md")

## Requirements for recording

action interaction events

To record real-time action interaction events, you need the following:

- A dataset group that includes an `Action interactions dataset`, which can be empty. For information on
  creating a dataset group and a dataset, see [Importing training data into Amazon Personalize datasets](import-data.md "import-data.md").
- The ID of your event tracker. You specify this ID in the PutActionInteractions operation. When you create an Action interactions dataset,
  Amazon Personalize automatically creates an action interaction event tracker for you. For more information, see [Finding the ID of your action interaction event tracker](action-interaction-tracker-id.md "action-interaction-tracker-id.md").
- A call to the [PutActionInteractions](API_UBS_PutActionInteractions.md "API_UBS_PutActionInteractions.md") operation.
