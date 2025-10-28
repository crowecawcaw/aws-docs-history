# Preparing action metadata for training

An _action_ is an engagement or revenue generating activity that you might want to recommend to your
users. Actions might include installing your mobile app, completing a membership profile, joining your loyalty program, or
signing up for promotional emails. You import data about your actions into an Amazon Personalize _Actions dataset_.
Examples of data for an action include a unique ID for the action, the action's estimated value, or the action's expiration
timestamp.

If you use [Next-Best-Action](native-recipe-next-best-action.md "native-recipe-next-best-action.md"), you must import action metadata. With
this recipe, Amazon Personalize predicts the next best action from the actions you import into your Actions dataset. No other recipes or
use cases use action metadata. You can't create an Actions dataset in a domain dataset group.

When training, Amazon Personalize doesn't use non-categorical string action data, such as action titles or tags.
However, importing this data can still enhance recommendations. For more information, see [Non-categorical string data](#action-string-data "#action-string-data").

Your bulk action data must be in a CSV file. Each row in the file should represent a unique action. After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

The following sections provide more information on how to prepare your action metadata for Amazon Personalize. For
bulk data format guidelines for all types of data, see [bulk data format guidelines](preparing-training-data.md#general-formatting-guidelines "preparing-training-data.md#general-formatting-guidelines")

###### Topics

- [Action data requirements](#action-data-requirements "#action-data-requirements")
- [Action expiration timestamp data](#action-expiration-timestamp-data "#action-expiration-timestamp-data")
- [Repeat frequency data](#action-repeat-frequency "#action-repeat-frequency")
- [Value data](#action-value-data "#action-value-data")
- [Creation timestamp data](#action-creation-timestamp-data "#action-creation-timestamp-data")
- [Categorical metadata](#action-categorical-data "#action-categorical-data")
- [Non-categorical string data](#action-string-data "#action-string-data")
- [Actions metadata example](#actions-data-example "#actions-data-example")

## Action data requirements

The following are action data requirements for Amazon Personalize.

- You must have an ACTION_ID column that stores the unique identifier for each action. Every action must have an item ID. It
  must be a `string` with a max length of 256 characters.
- Your data must have at least one categorical string or numerical metadata column. Action metadata columns can include empty/null values.
  We recommend that these columns be at minimum 70 percent complete.
- During model training, Amazon Personalize considers a maximum of 1000 actions. If you import more than
  1000 actions, Amazon Personalize decides which actions to include in training, with priority given to new actions (actions
  you recently added with no interactions) and existing actions with recent interactions data.
- The maximum number of columns is 10.

## Action expiration timestamp data

An action expiration timestamp specifies the date at which an action is no longer valid.
You provide action expiration timestamp data in Unix epoch time format, in seconds.
If an action has expired, Amazon Personalize won't include it in recommendations.

Specify an action expiration timestamp for your actions if you want to limit their appearance
in recommendations to a certain time frame.
For example, you might have an application that is running a membership drive through a certain month.
You might set an expiration timestamp for the _enroll_ action for the end of that month.
Amazon Personalize automatically stops recommending this action when this date is reached.

If you set the expiration timestamp to a time in the past for a new action,
or if you update an actions timestamp to a time in the past, it can take up to 2 hours to
remove the action from recommendations.

## Repeat frequency data

Repeat frequency data specifies how many days Amazon Personalize should wait to recommend a particular action
after a user interacts with it, based on the user's history in your Action interactions dataset.
You specify an action's repeat frequency in days, with a maximum of 30.

For example, you might have an ecommerce application where each user creates an account and a profile. If you have a
`complete profile` action and you want to wait a week after a user interacts with it before recommending it
again, you would specify 7 days as the action's `REPEAT_FREQENCY`. After 7 days, Amazon Personalize starts considering the
action for recommendations.

If you don't provide a repeat frequency for an action, Amazon Personalize will not set any limits on the number
of times it appears in recommendations.

## Value data

Value data is the business value or importance of each action. An action's `value` can be 1 – 10,
where 10 is the most valuable action in your dataset.

For example, you might have two actions, one for enrolling in your basic subscription and one for enrolling in your
premium service. For the basic service, you might specify a value of `5` and for the premium, a value of
`10`.

Amazon Personalize uses value data as one input when determining the best action to recommend to your users. For example, if a user
is equally likely to take one action or another, Amazon Personalize ranks the action with the highest value higher in recommendations.

## Creation timestamp data

Amazon Personalize uses creation timestamp data (in Unix epoch time format, in seconds) to calculate
the age of an action and adjust recommendations accordingly.

If you don't have creation timestamp data, Amazon Personalize infers this information from any action interaction data. It uses the
timestamp of the action’s oldest interaction data as the action's creation timestamp. If an action has no interaction data,
its creation timestamp is set as the timestamp of the latest interaction in the training set, and Amazon Personalize considers it a new
action.

## Categorical metadata

Amazon Personalize uses categorical metadata about actions, such as seasonality or action exclusivity, when identifying
the underlying patterns that reveal the best actions for your users. You define your own range of values based on your use case.
Categorical metadata can be in any language.

You can import categorical data and use it to filter recommendations based on an action's attributes. For information
about filtering recommendations, see [Filtering recommendations and user segments](filter.md "filter.md").

Categorical values can have a maximum of 1000 characters. If you have an action with a categorical
value with more than 1000 characters, your dataset import job will fail.

## Non-categorical string data

Except for action IDs, Amazon Personalize doesn't use non-categorical string data when training, such as an action's name, keywords about the action, or tags.
However, Amazon Personalize can use it when filtering recommendations. You can create filters to include or remove actions from
recommendations based on non-categorical string data. For more
information about filters, see [Filtering recommendations and user segments](filter.md "filter.md"). Non-categorical values can have a maximum of
1000 characters.

## Actions metadata example

The first few lines of action metadata in a CSV file might look like the following.

```
ACTION_ID,VALUE,MEMBERSHIP_LEVEL,CREATION_TIMESTAMP,REPEAT_FREQUENCY
1,10,Deluxe|Premium,1510003267,7
2,5,Basic,1580003267,7
3,5,Preview,1590003267,3
4,10,Deluxe|Platinum,1560003267,4
...
...
```

The `ACTION_ID` column is required. The
`MEMBERSHIP_LEVEL` column is a categorical string field. The `VALUE`,
`CREATION_TIMESTAMP`, and `REPEAT_FREQUENCY` fields are reserved keywords with the required types.

After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").
This is what the schema JSON file would look like for
the above sample data.

```
{
  "type": "record",
  "name": "Actions",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
    {
      "name": "ACTION_ID",
      "type": "string"
    },
    {
      "name": "VALUE",
      "type": [
        "null",
        "long"
      ]
    },

    {
      "name": "MEMBERSHIP_LEVEL",
      "type": [
        "null",
        "string"
      ],
      "categorical": true
    },

    {
      "name": "CREATION_TIMESTAMP",
      "type": "long"
    },
    {
      "name": "REPEAT_FREQUENCY",
      "type": [
        "long",
        "null"
      ]
    }
  ],
  "version": "1.0"
}
```
