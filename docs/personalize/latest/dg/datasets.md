

# Types of data Amazon Personalize can use
<a name="datasets"></a>

 The following topics introduce the different types of data that you can import into Amazon Personalize. 

**Topics**
+ [Interactions data](#interactions-summary)
+ [Item data](#items-summary)
+ [User data](#users-summary)
+ [Actions data](#actions-summary)
+ [Actions interactions data](#actions-interactions-summary)

## Interactions data
<a name="interactions-summary"></a>

 An *interaction* is an *event* that you record and then import as training data. Amazon Personalize generates recommendations primarily based on the interactions data. Interactions data can include the following:
+ Event type and event value data
+ Contextual metadata
+ Impressions data

You import interactions data into an *Item interactions dataset*. For more details about Item interactions datasets, see [Item interaction data](interactions-datasets.md).

## Item data
<a name="items-summary"></a>

The item metadata that Amazon Personalize can use includes the following:
+ Numerical data about each item, such its price.
+ Categorical metadata about each item, such as the item's genre or color.
+ Creation timestamp data for each item.
+  Unstructured text metadata, such as product descriptions or movie synopses. 

 You import metadata about your items into an *Items* dataset. For more information about Items datasets, see [Item metadata](items-datasets.md). 

## User data
<a name="users-summary"></a>

The user metadata Amazon Personalize can use includes the following: 
+ Numerical data about each user, such as their age.
+ Categorical metadata about each user, such as their gender or loyalty membership status.

 You import metadata about your users into a *Users* dataset. For more information about Users datasets, see [User metadata](users-datasets.md). 

## Actions data
<a name="actions-summary"></a>

The action data Amazon Personalize can use includes the following: 
+ The business value or importance of each action.
+ Categorical metadata for each action, such as seasonality or action exclusivity.
+ Action expiration timestamp data that specifies when Amazon Personalize should stop recommending each action.
+ Repeat frequency data that specifies long Amazon Personalize should wait before recommending each action after a user interacts with it.

 You import data about your actions into a *Actions dataset*. You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group. For more information about Actions datasets, see [Action metadata](actions-datasets.md). 

## Actions interactions data
<a name="actions-interactions-summary"></a>

The data Amazon Personalize can use from user interactions with actions includes the following: 
+ Event type data
+ Categorical metadata

You import interactions data into an *Action interactions dataset*. You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group. For more details about Action interactions datasets, see [Action interaction data](action-interactions-datasets.md).