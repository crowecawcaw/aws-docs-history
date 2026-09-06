

# User-Personalization recipe
<a name="native-recipe-new-item-USER_PERSONALIZATION"></a>

**Important**  
We recommend using the [User-Personalization-v2](native-recipe-user-personalization-v2.md) recipe. It can consider up to 5 million items with faster training, and generate more relevant recommendations with lower latency.

The User-Personalization (aws-user-personalization) recipe is optimized for all personalized recommendation scenarios. It predicts the items that a user will most likely interact with. You might use User-Personalization to generate personalized movie recommendations for a streaming app or personalized product recommendations for a retail app.

With User-Personalization, Amazon Personalize generates recommendations primarily based on user item interaction data in an Item interactions dataset. It can also use any item and user metadata in your Items and Users datasets. For more information about the data it uses, see [Required and optional datasets](#user-personalization-datasets). 

**Topics**
+ [Recipe features](#user-personalization-features)
+ [Required and optional datasets](#user-personalization-datasets)
+ [Properties and hyperparameters](#bandit-hyperparameters)
+ [Training with the User-Personalization recipe (console)](#training-user-personalization-recipe-console)
+ [Training with the User-Personalization recipe (Python SDK)](#training-user-personalization-recipe)
+ [Getting recommendations and recording impressions (SDK for Python (Boto3))](#user-personalization-get-recommendations-recording-impressions)
+ [Sample Jupyter notebook](#bandits-sample-notebooks)

## Recipe features
<a name="user-personalization-features"></a>

User-Personalization uses the following Amazon Personalize recipe features when generating item recommendations: 
+ Real-time personalization – With real-time personalization, Amazon Personalize updates and adapts item recommendations according to a user's evolving interest. For more information, see [Real-time personalization](use-case-recipe-features.md#about-real-time-personalization).
+ Exploration – With exploration, recommendations include new items or items with less interactions data. This improves item discovery and engagement when you have a fast-changing catalog, or when new items, such as news articles or promotions, are more relevant to users when fresh. For more information about exploration, see [Exploration](use-case-recipe-features.md#about-exploration).
+ Automatic updates – With automatic updates, Amazon Personalize automatically updates the latest model (solution version) every two hours to consider new items for recommendations. For more information, see [Automatic updates](use-case-recipe-features.md#automatic-updates).

## Required and optional datasets
<a name="user-personalization-datasets"></a>

To use the User-Personalization, you must create an [Item interactions dataset](interactions-datasets.md) and import at minimum 1000 item interactions. Amazon Personalize generates recommendations primarily based on item interaction data.

With User-Personalization, Amazon Personalize can use Item interactions data that includes the following:
+ Event type and event value data – Amazon Personalize uses event type data, such as click or watch event types, to identify user intent and interest through any patterns in their behavior. Also, you can use event type and event value data to filter records before training. For more information, see [Event type and event value data](interactions-datasets.md#event-type-and-event-value-data). 
+ Contextual metadata – Contextual metadata is interactions data you collect on the user's environment at the time of an event, such as their location or device type. For more information, see [Contextual metadata](interactions-datasets.md#interactions-contextual-metadata). 
+ Impressions data – Impressions are lists of items that were visible to a user when they interacted with (clicked, watched, purchased, and so on) a particular item. For more information, see [Impressions data](interactions-datasets.md#interactions-impressions-data).

 The following datasets are optional and can improve recommendations: 
+ Users dataset – Amazon Personalize can use data in your Users dataset to better understand your users and their interests. You can also use data in a Users dataset to filter recommendations. For information about the user data you can import, see [User metadata](users-datasets.md).
+ Items dataset – Amazon Personalize can use data in your Items dataset to identify connections and patterns in their behavior. This helps Amazon Personalize understand your users and their interests. You can also use data in a Items dataset to filter recommendations. For information about the item data you can import, see [Item metadata](items-datasets.md). 

## Properties and hyperparameters
<a name="bandit-hyperparameters"></a>

The User-Personalization recipe has the following properties:
+  **Name** – `aws-user-personalization`
+  **Recipe Amazon Resource Name (ARN)** – `arn:aws:personalize:::recipe/aws-user-personalization`
+  **Algorithm ARN** – `arn:aws:personalize:::algorithm/aws-user-personalization`

For more information, see [Choosing a recipe](working-with-predefined-recipes.md).

The following table describes the hyperparameters for the User-Personalization recipe. A *hyperparameter* is an algorithm parameter that you can adjust to improve model performance. Algorithm hyperparameters control how the model performs. Featurization hyperparameters control how to filter the data to use in training. The process of choosing the best value for a hyperparameter is called hyperparameter optimization (HPO). For more information, see [Hyperparameters and HPO](customizing-solution-config-hpo.md). 

The table provides the following information for each hyperparameter:
+ **Range**: [lower bound, upper bound]
+ **Value type**: Integer, Continuous (float), Categorical (Boolean, list, string)
+ **HPO tunable**: Can the parameter participate in HPO?


<table>
<thead>
  <tr><th>Name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>Algorithm hyperparameters</b></td></tr>
  <tr><td><code>hidden_dimension</code></td><td>The number of hidden variables used in the model. <i>Hidden variables</i> recreate users' purchase history and item statistics to generate ranking scores. Specify a greater number of hidden dimensions when your Item interactions dataset includes more complicated patterns. Using more hidden dimensions requires a larger dataset and more time to process. To decide on the best value, use HPO. To use HPO, set <code>performHPO</code> to <code>true</code> when you call <a href="API_CreateSolution.md">CreateSolution</a> and <a href="API_CreateSolutionVersion.md">CreateSolutionVersion</a> operations.<br />Default value: 149<br />Range: [32, 256]<br />Value type: Integer<br />HPO tunable: Yes</td></tr>
  <tr><td><code>bptt</code></td><td>Determines whether to use the back-propagation through time technique. <i>Back-propagation through time</i> is a technique that updates weights in recurrent neural network-based algorithms. Use <code>bptt</code> for long-term credits to connect delayed rewards to early events. For example, a delayed reward can be a purchase made after several clicks. An early event can be an initial click. Even within the same event types, such as a click, it’s a good idea to consider long-term effects and maximize the total rewards. To consider long-term effects, use larger <code>bptt</code> values. Using a larger <code>bptt</code> value requires larger datasets and more time to process.<br />Default value: 32<br />Range: [2, 32]<br />Value type: Integer<br />HPO tunable: Yes</td></tr>
  <tr><td><code>recency_mask</code></td><td>Determines whether the model should consider the latest popularity trends in the Item interactions dataset. Latest popularity trends might include sudden changes in the underlying patterns of interaction events. To train a model that places more weight on recent events, set <code>recency_mask</code> to <code>true</code>. To train a model that equally weighs all past interactions, set <code>recency_mask</code> to <code>false</code>. To get good recommendations using an equal weight, you might need a larger training dataset.<br />Default value: <code>True</code><br />Range: <code>True</code> or <code>False</code><br />Value type: Boolean<br />HPO tunable: Yes</td></tr>
  <tr><td colspan="2"><b>Featurization hyperparameters</b></td></tr>
  <tr><td><code>min_user_history_length_percentile</code></td><td>The minimum percentile of user history lengths to include in model training. <i>History length</i> is the total amount of data about a user. Use <code>min_user_history_length_percentile</code> to exclude a percentage of users with short history lengths. Users with a short history often show patterns based on item popularity instead of the user's personal needs or wants. Removing them can train models with more focus on underlying patterns in your data. Choose an appropriate value after you review user history lengths, using a histogram or similar tool. We recommend setting a value that retains the majority of users, but removes the edge cases.<br /> For example, setting <code>min_user_history_length_percentile to 0.05</code> and <code>max_user_history_length_percentile to 0.95</code> includes all users except those with history lengths at the bottom or top 5%.<br />Default value: 0.0<br />Range: [0.0, 1.0]<br />Value type: Float<br />HPO tunable: No</td></tr>
  <tr><td><code>max_user_history_length_percentile</code></td><td>The maximum percentile of user history lengths to include in model training. <i>History length</i> is the total amount of data about a user. Use <code>max_user_history_length_percentile</code> to exclude a percentage of users with long history lengths because data for these users tend to contain noise. For example, a robot might have a long list of automated interactions. Removing these users limits noise in training. Choose an appropriate value after you review user history lengths using a histogram or similar tool. We recommend setting a value that retains the majority of users but removes the edge cases.<br />For example, setting <code>min_user_history_length_percentile to 0.05</code> and <code>max_user_history_length_percentile to 0.95</code> includes all users except those with history lengths at the bottom or top 5%.<br />Default value: 0.99<br />Range: [0.0, 1.0]<br />Value type: Float<br />HPO tunable: No</td></tr>
  <tr><td colspan="2"><b>Item exploration campaign configuration hyperparameters</b></td></tr>
  <tr><td><code>exploration_weight</code></td><td>Determines how frequently recommendations include items with less item interaction data or relevance. The closer the value is to 1.0, the more exploration. At zero, no exploration occurs and recommendations are based on current data (relevance). For more information see <a href="API_CampaignConfig.md">CampaignConfig</a>.<br />Default value: 0.3<br />Range: [0.0, 1.0]<br />Value type: Float<br />HPO tunable: No</td></tr>
  <tr><td><code>exploration_item_age_cut_off</code></td><td>Specify the maximum item age in days since the latest interaction across all items in the Item interactions dataset. This defines the scope of item exploration based on item age. Amazon Personalize determines an item's age based on its creation timestamp or, if creation timestamp data is missing, item interaction data. For more information how Amazon Personalize determines an item's age, see <a href="items-datasets.md#creation-timestamp-data">Creation timestamp data</a>. <br />To increase the items Amazon Personalize considers during exploration, enter a greater value. The minimum is 1 day and the default is 30 days. Recommendations might include items that are older than the item age cut off you specify. This is because these items are relevant to the user and exploration didn't identify them.<br />Default value: 30.0<br />Range: Positive floats<br />Value type: Float<br />HPO tunable: No</td></tr>
</tbody>
</table>


## Training with the User-Personalization recipe (console)
<a name="training-user-personalization-recipe-console"></a>

To use the User-Personalization recipe to generate recommendations in the console, first train a new solution version using the recipe. Then deploy a campaign using the solution version and use the campaign to get recommendations. 

**Training a new solution version with the User-Personalization recipe (console)**

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home) and sign into your account.

1. Create a Custom dataset group with a new schema and upload your dataset with impressions data. Optionally include [CREATION\_TIMESTAMP]() and [Unstructured text metadata](items-datasets.md#text-data) data in your Items dataset so Amazon Personalize can more accurately calculate the age of an item and identify cold items.

   For more information on importing data, see [Importing training data into Amazon Personalize datasets](import-data.md).

1. On the **Dataset groups** page, choose the new dataset group that contains the dataset or datasets with impressions data.

1. In the navigation pane, choose **Solutions and recipes** and choose **Create solution**.

1. On the **Create solution** page, for the **Solution name**, enter the name of your new solution.

1. For **Solution type**, choose **Item recommendation** to get item recommendations for your users. 

1. For **Recipe**, choose **aws-user-personalization**. The **Solution configuration** section appears providing several configuration options. 

1. In **Event configuration**, if your Item interactions dataset has EVENT\_TYPE or both EVENT\_TYPE and EVENT\_VALUE columns, optionally use the **Event type** and **Event value threshold** fields to choose the item interactions data that Amazon Personalize uses when training the model. For more information, see [Choosing the item interaction data used for training](event-values-types.md). 

    If you have multiple event types and use the User-Personalization-v2 recipe or Personalized-Ranking-v2 recipe, you can also specify different weights for different types. For example, you can configure a solution to give more weight to purchase events than click events. For more information, see [Optimizing a solution with events configuration](optimizing-solution-events-config.md). 

1. Optionally configure hyperparameters for your solution. For a list of User-Personalization recipe properties and hyperparameters, see [Properties and hyperparameters](#bandit-hyperparameters). 

1. Choose **Create and train solution** to start training. The **Dashboard** page displays.

   You can navigate to the solution details page to track training progress in the **Solution versions** section. When training is complete, the status is **Active**.

**Creating a campaign and getting recommendations (console)**

 When your solution version status is **Active** you are ready to create your campaign and get recommendations as follows: 

1. On either the solution details page or the **Campaigns** page, choose **Create new campaign**.

1.  On the **Create new campaign** page, for **Campaign details**, provide the following information: 
   + **Campaign name:** Enter the name of the campaign. The text you enter here appears on the Campaign dashboard and details page.
   + **Solution:** Choose the solution that you just created.
   + **Solution version ID:** Choose the ID of the solution version that you just created.
   + **Minimum provisioned transactions per second:** Set the minimum provisioned transactions per second that Amazon Personalize supports. For more information, see the [CreateCampaign](API_CreateCampaign.md) operation.

1. For **Campaign configuration**, provide the following information:
   + **Exploration weight:** Configure how much to explore, where recommendations include items with less item interaction data or relevance more frequently the more exploration you specify. The closer the value is to 1, the more exploration. At zero, no exploration occurs and recommendations are based on current data (relevance).
   + **Exploration item age cut off**: Enter the maximum item age, in days since the latest interaction, to define the scope of item exploration. To increase the number of items Amazon Personalize considers during exploration, enter a greater value. 

      For example, if you enter 10, only items with item interaction data from the 10 days since the latest interaction in the dataset are considered during exploration. 
**Note**  
Recommendations might include items without item interaction data from outside this time frame. This is because these items are relevant to the user's interests, and exploration wasn't required to identify them.

1. Choose **Create campaign**.

1. On the campaign details page, when the campaign status is **Active**, you can use the campaign to get recommendations and record impressions. For more information, see [Step 5: Get recommendations](getting-started-console.md#getting-started-console-get-recommendations) in "Getting Started." 

    Amazon Personalize automatically updates your latest solution version every two hours to include new data. Your campaign automatically uses the updated solution version. For more information, see [Automatic updates](use-case-recipe-features.md#automatic-updates). 

   To manually update the campaign, you first create and train a new solution version using the console or the [CreateSolutionVersion](API_CreateSolutionVersion.md) operation, with `trainingMode` set to `update`. You then manually update the campaign on the **Campaign** page of the console or by using the [UpdateCampaign](API_UpdateCampaign.md) operation. 
**Note**  
 Amazon Personalize doesn't automatically update solution versions you created before November 17, 2020. 

## Training with the User-Personalization recipe (Python SDK)
<a name="training-user-personalization-recipe"></a>

When you have created a dataset group and uploaded your dataset(s) with impressions data, you can train a solution with the User-Personalization recipe. Optionally include [CREATION\_TIMESTAMP]() and [Unstructured text metadata](items-datasets.md#text-data) data in your Items dataset so Amazon Personalize can more accurately calculate the age of an item and identify cold items. For more information on creating dataset groups and uploading training data see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md).

**To train a solution with the User-Personalization recipe using the AWS SDK**

1. Create a new solution using the `create_solution` method.

   Replace `solution name` with your solution name and `dataset group arn` with the Amazon Resource Name (ARN) of your dataset group.

   ```
   import boto3
   
   personalize = boto3.client('personalize')
   
   print('Creating solution')
   create_solution_response = personalize.create_solution(name = '{{solution name}}', 
                               recipeArn = 'arn:aws:personalize:::recipe/aws-user-personalization', 
                               datasetGroupArn = '{{dataset group arn}}',
                               )
   solution_arn = create_solution_response['solutionArn']
   print('solution_arn: ', solution_arn)
   ```

   For a list of aws-user-personalization recipe properties and hyperparameters, see [Properties and hyperparameters](#bandit-hyperparameters).

1. Create a new *solution version* with the updated training data and set `trainingMode` to `FULL` using the following code snippet. Replace the `solution arn` with the ARN of your solution.

   ```
   import boto3
           
   personalize = boto3.client('personalize')
           
   create_solution_version_response = personalize.create_solution_version(solutionArn = '{{solution arn}}', 
                                                                  trainingMode='FULL')
   
   new_solution_version_arn = create_solution_version_response['solutionVersionArn']
   print('solution_version_arn:', new_solution_version_arn)
   ```

1. When Amazon Personalize is finished creating your solution version, create your campaign with the following parameters:
   + Provide a new `campaign name` and the `solution version arn` generated in step 2.
   + Modify the `explorationWeight` item exploration configuration hyperparameter to configure how much to explore. Items with less item interaction data or relevance are recommended more frequently the closer the value is to 1.0. The default value is 0.3.
   + Modify the `explorationItemAgeCutOff` item exploration configuration hyperparameter parameter to provide the maximum duration, in days relative to the latest interaction, for which items should be explored. The larger the value, the more items are considered during exploration.

   Use the following Python snippet to create a new campaign with an emphasis on exploration with exploration cut-off at 30 days. Creating a campaign usually takes a few minutes but can take over an hour.

   ```
   import boto3
           
   personalize = boto3.client('personalize')
   
   create_campaign_response = personalize.create_campaign(
       name = '{{campaign name}}',
       solutionVersionArn = '{{solution version arn}}',
       minProvisionedTPS = 1,
       campaignConfig = {"itemExplorationConfig": {"explorationWeight": "{{0.3}}", "explorationItemAgeCutOff": "{{30}}"}}
   )
   
   campaign_arn = create_campaign_response['campaignArn']
   print('campaign_arn:', campaign_arn)
   ```

    With User-Personalization, Amazon Personalize automatically updates your solution version every two hours to include new data. Your campaign automatically uses the updated solution version. For more information, see [Automatic updates](use-case-recipe-features.md#automatic-updates). 

   To manually update the campaign, you first create and train a new solution version using the console or the [CreateSolutionVersion](API_CreateSolutionVersion.md) operation, with `trainingMode` set to `update`. You then manually update the campaign on the **Campaign** page of the console or by using the [UpdateCampaign](API_UpdateCampaign.md) operation.
**Note**  
 Amazon Personalize doesn't automatically update solution versions you created before November 17, 2020. 

## Getting recommendations and recording impressions (SDK for Python (Boto3))
<a name="user-personalization-get-recommendations-recording-impressions"></a>

When your campaign is created, you can use it to get recommendations for a user and record impressions. For information on getting batch recommendations using the AWS SDKs see [Creating a batch inference job (AWS SDKs)](creating-batch-inference-job.md#batch-sdk).



**To get recommendations and record impressions**

1. Call the `get_recommendations` method. Change the `campaign arn` to the ARN of your new campaign and `user id` to the userId of the user.

   ```
   import boto3
               
   rec_response = personalize_runtime.get_recommendations(campaignArn = '{{campaign arn}}', userId = '{{user id}}')
   print(rec_response['recommendationId'])
   ```

1. Create a new event tracker for sending PutEvents requests. Replace `event tracker name` with the name of your event tracker and `dataset group arn` with the ARN of your dataset group.

   ```
   import boto3
           
   personalize = boto3.client('personalize')
   
   event_tracker_response = personalize.create_event_tracker( 
       name = '{{event tracker name}}',
       datasetGroupArn = '{{dataset group arn}}'
   )
   event_tracker_arn = event_tracker_response['eventTrackerArn']
   event_tracking_id = event_tracker_response['trackingId']
   print('eventTrackerArn:{},\n eventTrackingId:{}'.format(event_tracker_arn, event_tracking_id))
   ```

1.  Use the `recommendationId` from step 1 and the `event tracking id` from step 2 to create a new `PutEvents` request. This request logs the new impression data from the user’s session. Change the `user id` to the ID of the user. 

   ```
   import boto3
               
   personalize_events.put_events(
        trackingId = '{{event tracking id}}',
        userId= '{{user id}}',
        sessionId = '1',
        eventList = [{
        'sentAt': datetime.now().timestamp(),
        'eventType' : 'click',
        'itemId' : rec_response['itemList'][0]['itemId'],        
        'recommendationId': rec_response['{{recommendationId}}'],
        'impression': [item['itemId'] for item in rec_response['itemList']],
        }]
   )
   ```

## Sample Jupyter notebook
<a name="bandits-sample-notebooks"></a>

For a sample Jupyter notebook that shows how to use the User-Personalization recipe, see [User Personalization with Exploration](https://github.com/aws-samples/amazon-personalize-samples/blob/master/next_steps/core_use_cases/user_personalization/user-personalization-with-exploration.ipynb).