# Types of data Amazon Personalize can use

The following topics introduce the different types of data that you can
import into Amazon Personalize.

###### Topics

- [Interactions data](#interactions-summary "#interactions-summary")
- [Item data](#items-summary "#items-summary")
- [User data](#users-summary "#users-summary")
- [Actions data](#actions-summary "#actions-summary")
- [Actions interactions data](#actions-interactions-summary "#actions-interactions-summary")

## Interactions data

An _interaction_ is an _event_ that you record and then import as training data. Amazon Personalize generates recommendations primarily based on the interactions data.
Interactions data can include the following:

- Event type and event value data
- Contextual metadata
- Impressions data

You
import interactions data into an _Item interactions dataset_. For more details about Item interactions datasets,
see [Item interaction data](interactions-datasets.md "interactions-datasets.md").

## Item data

The item metadata that Amazon Personalize can use includes the following:

- Numerical data about each item, such its price.
- Categorical metadata about each item, such as the item's genre or color.
- Creation timestamp data for each item.
- Unstructured text metadata, such as product descriptions or movie synopses.

You import metadata about your items into an _Items_ dataset. For more information about Items datasets,
see [Item metadata](items-datasets.md "items-datasets.md").

## User data

The user metadata Amazon Personalize can use includes the following:

- Numerical data about each user, such as their age.
- Categorical metadata about each user, such as their gender or loyalty membership status.

You import metadata about your users into a _Users_ dataset. For more information about Users datasets,
see [User metadata](users-datasets.md "users-datasets.md").

## Actions data

The action data Amazon Personalize can use includes the following:

- The business value or importance of each action.
- Categorical metadata for each action, such as seasonality or action exclusivity.
- Action expiration timestamp data that specifies when Amazon Personalize should stop recommending each action.
- Repeat frequency data that specifies long Amazon Personalize should wait before recommending each action after a user interacts with it.

You import data about your actions into a _Actions dataset_. You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group. For more information about Actions datasets,
see [Action metadata](actions-datasets.md "actions-datasets.md").

## Actions interactions data

The data Amazon Personalize can use from user interactions with actions includes the following:

- Event type data
- Categorical metadata

You import interactions data into an _Action interactions dataset_. You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group. For
more details about Action interactions datasets, see [Action interaction data](action-interactions-datasets.md "action-interactions-datasets.md").
