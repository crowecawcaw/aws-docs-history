# A/B testing with CloudWatch Evidently

After you create a recommender or deploy a custom solution version with a campaign, you can perform A/B tests with
Amazon Personalize recommendations and Amazon CloudWatch Evidently. The following video describes the process of using CloudWatch Evidently to perform A/B
testing with Amazon Personalize recommendations. For step-by-step instructions, see [Performing an A/B test with CloudWatch Evidently](#ab-testing-evidently-steps "#ab-testing-evidently-steps").

###### Topics

- [Performing an A/B test with CloudWatch Evidently](#ab-testing-evidently-steps "#ab-testing-evidently-steps")
- [Sample implementations](#ab-testing-evidently-learn-more "#ab-testing-evidently-learn-more")

## Performing an A/B test with CloudWatch Evidently

To perform an A/B test with Amazon Personalize and Amazon CloudWatch Evidently, create a CloudWatch Evidently project, define a feature and its
variations, update your application to support your experiment, and create and run the experiment. As the experiment runs,
you can view results in CloudWatch Evidently.

###### To perform an A/B test with Amazon Personalize and CloudWatch Evidently

1. Create a CloudWatch Evidently project. A project is a logical grouping of CloudWatch resources. Within the project, you create
   features that have variations that you want to test or launch. For step-by-step instructions, see [Create a new
   project](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-newproject.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-newproject.md") in the _Amazon CloudWatch User Guide_.
2. Add a feature to your project and define its variations. For this experiment, your feature should represent the
   recommendation scenario that you want to test, such as the click-through rate.

When you add a feature, specify identifiers to map the different variations of your scenario to Amazon Personalize
recommenders or custom campaigns. For each variation, specify the **Variation type**,
such as String, give the variation a name, and give it a value.

When your experiment runs, your application uses the value of variation to determine what Amazon Personalize resource to use
for recommendations. For example, if you're testing two VIDEO_ON_DEMAND recommenders, one created for the
_Top picks for you_ use case and one created for the _Trending now_ use case,
you might set the following JSON as the **Value** for each variation.

```
{"type":"top-picks-recommendations","arn":"arn:aws:personalize:us-west-2:<acct-id>:recommender/top-picks-recommender"}
```

```
{"type":"trending-recommendations","arn":"arn:aws:personalize:us-west-2:<acct-id>:recommender/trending-now-recommender"}
```

You can specify any identifier, as long as your application can use it to identify the relevant resource. For
example, you might specify only the name of the recommender or campaign, and construct the Amazon Resource Name (ARN)
of the resource in your application.

For step-by-step instructions to add a feature, see [Add a feature to a project](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-newfeature.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-newfeature.md") in
the _Amazon CloudWatch User Guide_. 3. Update your application to support your experiment:

    * **Feature evaluation** – Use the CloudWatch Evidently
     `EvaluateFeature` API operation to assign variations to each user session. The
     `EvaluateFeature` response includes the variation value that you specified in the previous step. In
     this case, it's a JSON object with the type of recommender and it's the ARN of the recommender. Update your
     recommendation request code to get recommendations from this resource.


     For information about evaluating a feature, see [Using EvaluateFeature](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-code-application.md#CloudWatch-Evidently-code-EvaluateFeature "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-code-application.md#CloudWatch-Evidently-code-EvaluateFeature") in the *Amazon CloudWatch User Guide*.
    * **Record outcomes** – Add code to your application to track results from
     users' interactions with recommendations.


    To track metrics for your experiments in CloudWatch Evidently, use the CloudWatch Evidently `PutProjectEvents`
     API operation to record outcomes for each user. For example, if a user in an experiment clicks a recommended item,
     you would send details for this event to CloudWatch Evidently.


     For information about sending events to CloudWatch Evidently, see [Using PutProjectEvents](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-code-application.md#CloudWatch-Evidently-code-PutProjectEvents "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-code-application.md#CloudWatch-Evidently-code-PutProjectEvents") in the *Amazon CloudWatch User Guide*.


     To improve Amazon Personalize recommendation relevance, you can record outcome events with the Amazon Personalize
     `PutEvents` API operation. If your domain use case or custom recipe supports real-time updates to
     recommendations, Amazon Personalize can learn from your user’s most recent activity and update recommendations as they use
     your application. If it doesn't support updates, Amazon Personalize uses this data during the next full retraining of your
     model and then it impacts recommendations.


     For information about streaming events to Amazon Personalize, see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md").

4.  Create and start an experiment. When you create an experiment, specify the following:

        * **Feature** – Choose the feature to be tested in the experiment.
        * **Audience** – Configure how many of your users will participate, and
         configure how to split traffic between feature variations.
        * **Metrics** – Specify the metrics that determine the success of the
         experiment. For example, the number of clicks.

    After you finish creating the experiment, specify its duration and start the experiment. For step-by-step
    instructions to create and start experiments in CloudWatch Evidently, see [Create an experiment](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-newexperiment.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-newexperiment.md") in the
    _Amazon CloudWatch User Guide_.

5.  As you run your experiment, you can view results in the CloudWatch Evidently experiment dashboard. For information about
    viewing experiment results, see [View experiment results in
    the dashboard](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-experiment-dashboard.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-experiment-dashboard.md") in the _Amazon CloudWatch User Guide_.

## Sample implementations

The following sample implementations show how to implement A/B testing with CloudWatch Evidently.

- For a complete example of real-time APIs that include source code for implementing A/B tests, see [Real-Time Personalization APIs](https://github.com/aws-samples/personalization-apis "https://github.com/aws-samples/personalization-apis") in the AWS
  samples GitHub repository.
- For a tutorial that describes how to use A/B testing with CloudWatch Evidently and a sample react application, see
  [Tutorial: A/B testing with the Evidently sample application](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-sample-application.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-sample-application.md") in the _Amazon CloudWatch User Guide_.
