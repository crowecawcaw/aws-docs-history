# Next-Best-Action recipe

The Next-Best-Action (aws-next-best-action) recipe generates real-time recommendations for the next best actions for
your users. The next best action for a user is the action that they will most likely take. For example, enrolling in your
loyalty program, downloading your app, or applying for a credit card.

With Next-Best-Action, you can provide personalized action recommendations for your users as they use your
application. Suggesting the right action for a user can result in more users taking your actions. Depending on the actions
you want to recommend, you can increase customer loyalty, generate more revenue, and improve the user experience of your
application. For a use case example that describes how personalized action recommendations can benefit an ecommerce
application, see [Use case example](#nba-use-case-example "#nba-use-case-example").

Amazon Personalize predicts the next best action from the actions you import into your Actions dataset. It identifies the actions
that a user will most likely take based on their interactions with actions and items. If your action data includes the
value of the action, Amazon Personalize accounts for the action's value. If a user is equally likely to take two different actions,
Amazon Personalize ranks the action with the greater value higher.

When you get real-time action recommendations for a user, Amazon Personalize returns a list of actions that the user will most
likely take within a configurable period of time (the `action optimization period`). For example, the actions
they will most likely take in the next 14 days. The list is sorted in descending order by propensity score. This score
represents the likelihood that the user will take the action.

Until you import action interaction data, Amazon Personalize recommends actions in your without
personalization, and propensity scores are 0.0.
An action will have a score after the action has the following:

- At least 50 action interactions with the TAKEN event type.
- At least 50 action interactions with the NOT_TAKEN or VIEWED event type.
  These action interactions must be present at the latest solution version training, and must occur within a span of 6 weeks from the
  latest interaction timestamp in the Action interactions dataset.

For more information about the data the Next-Best-Action recipe uses, see
[Required and optional datasets](#nba-datasets "#nba-datasets").

When you create a solution with the Next-Best-Action recipe, you can configure the window of time Amazon Personalize uses when predicting
actions by using the `action optimization period` featurization hyperparameter. For more information, see [Properties and hyperparameters](#nba-hyperparameters "#nba-hyperparameters").

###### Topics

- [Use case example](#nba-use-case-example "#nba-use-case-example")
- [Recipe features](#nba-recipe-features "#nba-recipe-features")
- [Required and optional datasets](#nba-datasets "#nba-datasets")
- [Properties and hyperparameters](#nba-hyperparameters "#nba-hyperparameters")

## Use case example

Suggesting the right action for a user can result in more users taking your actions. Depending on the actions you
want to recommend, you can potentially increase customer loyalty, generate more revenue, and improve the user
experience of your application.

For example, you might have an ecommerce application that suggests the following different actions:

- Subscribe to loyalty program
- Download mobile app
- Purchase in _Jewelry_ category
- Purchase in _Beauty and grooming_ category

You might have a user who frequently shops at your site and has repeatedly taken the _Jewelry_
and _Beauty and grooming_ purchase actions. For this user, Amazon Personalize action recommendations and their
scores might include the following:

- Subscribe to loyalty program

Propensity score – 1.00

- Purchase in _Jewelry_ category

Propensity score – 0.86

- Purchase in _Beauty and grooming_ category

Propensity score – 0.85

With these action recommendations, you know to prompt the user to enroll in your loyalty program. This action has
the highest propensity score and it is the action the user will most likely take. This is because the user frequently shops at your
store and is likely to engage with the benefits from your loyalty program.

## Recipe features

The Next-Best-Action recipe uses the following Amazon Personalize recipe features when generating action recommendations:

- Real-time personalization: Amazon Personalize uses real-time personalization to update and adapt action recommendations
  according to a user's evolving interest. For more information, see [Real-time personalization](use-case-recipe-features.md#about-real-time-personalization "use-case-recipe-features.md#about-real-time-personalization").
- Exploration: With exploration, recommendations include new actions or actions with less interactions data.
  For more information about exploration, see [Exploration](use-case-recipe-features.md#about-exploration "use-case-recipe-features.md#about-exploration").
- Automatic updates: With automatic updates, Amazon Personalize automatically updates the latest model (solution version)
  every two hours to include new actions in recommendations through exploration. For more information, see [Automatic updates](use-case-recipe-features.md#automatic-updates "use-case-recipe-features.md#automatic-updates").

## Required and optional datasets

To use the Next-Best-Action recipe, you must create the following datasets:

- Actions: You import data about your actions, such as their value, into an Amazon Personalize Actions dataset.

In your actions data, you can provide an EXPIRATION_TIMESTAMP for each action. If an action has expired,
Amazon Personalize won't include it in recommendations. You can also provide a REPEAT_FREQUENCY for each action. This
indicates how long Amazon Personalize should wait before recommending an action again after a user interacts with it. For
information about the data an Actions dataset can store, see [Action metadata](actions-datasets.md "actions-datasets.md").

- Item interactions: Your Item interactions dataset must have at minimum 1000 item interactions.
  Amazon Personalize uses item interactions to understand your users' current state and their interests. For information
  about the item interactions data, see [Item interaction data](interactions-datasets.md "interactions-datasets.md").

The following datasets are optional:

- Action interactions dataset: An _action interaction_ is an interaction involving a user and an
  action in your Actions dataset. You can import Taken, Not taken, and Viewed action interactions. Although this
  data is optional, we recommend that you import action interaction data for quality recommendations. If you
  don't have action interaction data, you can create an empty Action interactions dataset and record your customers'
  interactions with actions by using the [PutActionInteractions](API_UBS_PutActionInteractions.md "API_UBS_PutActionInteractions.md") API operation.

Until you import action interaction data, Amazon Personalize recommends actions in your without
personalization, and propensity scores are 0.0.
An action will have a score after the action has the following:

    + At least 50 action interactions with the TAKEN event type.
    + At least 50 action interactions with the NOT\_TAKEN or VIEWED event type.

These action interactions must be present at the latest solution version training, and must occur within a span of 6 weeks from the
latest interaction timestamp in the Action interactions dataset.

For information about the action interactions data you can import, see [Action interaction data](action-interactions-datasets.md "action-interactions-datasets.md"). For information
about recording action interaction events, see [Recording real-time action interaction events](recording-action-interaction-events.md "recording-action-interaction-events.md").

###### Note

With Next-Best-Action, Amazon Personalize doesn't use impressions data or contextual metadata in an
Action interactions dataset.

- Users: Amazon Personalize uses any data in your Users dataset to better understand your users and their interests. You
  can also use data in a Users dataset to filter action recommendations. For information about the user data you
  can import, see [User metadata](users-datasets.md "users-datasets.md").
- Items: Amazon Personalize uses any data in your Items dataset along with your Item interactions dataset to identify
  connections and patterns in their behavior. This helps Amazon Personalize understand your users and their interests. For
  information about the item data you can import, see [Item metadata](items-datasets.md "items-datasets.md").

## Properties and hyperparameters

The Next-Best-Action recipe doesn't support hyperparameter optimization. The Next-Best-Action recipe has the
following properties:

- Name – `aws-next-best-action`
- Recipe Amazon Resource Name (ARN) –
  `arn:aws:personalize:::recipe/aws-next-best-action`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-next-best-action`

The following table describes the featurization hyperparameters for the aws-next-best-action recipe. A _hyperparameter_ is an algorithm parameter that you can adjust to improve model
performance. Featurization hyperparameters control how to filter the data to use in training.

The table also provides the following information for each hyperparameter:

- Range: [lower bound, upper bound]
- Value type: Integer, Continuous (float), Categorical (Boolean, list,
  string)
- HPO tunable: Whether the parameter can participate in HPO

| Name                                 | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Featurization<br>hyperparameters** |
| `action_optimization_period`         | The window of time Amazon Personalize uses when predicting the next best actions for a user. For example,<br>the actions the user will most likely take in the next 14 days.<br>If you don’t have much action interaction data, specify a larger value. If you aren’t sure what<br>value to specify, use the default.<br>Default value: 14<br>Range: [7, 28]<br>Value type: Integer<br>HPO tunable: No |
