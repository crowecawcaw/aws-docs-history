# Custom resources for training and deploying Amazon Personalize models

If you are using a custom recipe, after you [import data](import-data.md "import-data.md") you are ready to create the custom resources for training and deploying Amazon Personalize models.
You use these resources to get recommendations. When you create custom resources, you do the following:

1. **Create and configure a solution:** Customize solution parameters and recipe-specific
   hyperparameters so the model meets your specific business needs. By default, new solution versions use automatic training
   to create solution versions at a configurable frequency. The default frequency is every 7 days.
   For more information about configuring a solution, see [Configuring a solution](customizing-solution-config.md "customizing-solution-config.md"). For more information about custom recipes in Amazon Personalize, see [Choosing a
   recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").
2. **Create a solution version (for solutions that don't use automatic training):** For
   solutions that use automatic training, solution version creation starts automatically after your solution is active. For
   solutions that use manual training, you manually create a solution version. The solution version generates Amazon Personalize
   recommendations or user segments. For more information about manually creating a solution version, see [Manually creating a solution version](creating-a-solution-version.md "creating-a-solution-version.md"). To stop solution version creation,
   navigate to the solution version details page and choose **Stop**. For more information, see [Stopping the creation of a solution version](stop-solution-version.md "stop-solution-version.md").
3. **Evaluate the solution version** – Use the metrics Amazon Personalize generates from the new
   solution version to evaluate the performance of the model. See [Evaluating an Amazon Personalize solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md").
4. **Deploy the solution version with a campaign (only for real-time recommendations):**
   Create a campaign to deploy your solution version. You use the campaign when you request real-time recommendations. If you
   are getting batch recommendations, you don't need to create a campaign. For more information, see [Deploying an Amazon Personalize solution version with a campaign](campaigns.md "campaigns.md"). If you want to change an existing campaign's settings, such as enabling
   metadata in recommendations, you must update your campaign. For more information, see [Updating an Amazon Personalize campaign's configuration](update-campaigns.md "update-campaigns.md").

###### Topics

- [Configuring a custom solution in Amazon Personalize](customizing-solution-config.md "customizing-solution-config.md")
- [Updating a solution to change its automatic training configuration](updating-solution.md "updating-solution.md")
- [Manually creating a solution version](creating-a-solution-version.md "creating-a-solution-version.md")
- [Stopping the creation of a solution version](stop-solution-version.md "stop-solution-version.md")
- [Evaluating an Amazon Personalize solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md")
- [Deploying an Amazon Personalize solution version with a campaign](campaigns.md "campaigns.md")
- [Updating an Amazon Personalize campaign's configuration](update-campaigns.md "update-campaigns.md")
