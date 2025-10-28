# Configuring a custom solution in Amazon Personalize

After you finish importing data, you are ready to create a solution. A _solution_ refers
to the combination of an Amazon Personalize recipe, customized training parameters, and one or more solution versions. A
_solution version_ refers to a trained machine learning model.

By default, all new solutions use
automatic training to create a new solution version every 7 days. Automatic training occurs only
if you imported bulk or real-time interaction data since the last training. This includes item interactions or,
for solutions that use the Next-Best-Action recipe, action interactions data.
Automatic training continues until you delete the solution. For more information, see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").

If you have an existing solution, you can use the Amazon Personalize console to clone the solution. When you clone a solution, you can
use the configuration of the existing solution as a starting point, such as the recipe and hyperparameters, and make any
changes. For more information, see [Cloning a solution (console)](cloning-solution.md "cloning-solution.md").

You can create and configure a solution by using the console, AWS Command Line Interface (AWS CLI), or AWS SDKs. After you create a
solution, you can view its configuration details on the solution's details page of the Amazon Personalize console, or with the [DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md") operation.

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

###### Topics

- [Creating a solution](create-solution.md "create-solution.md")
- [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md")
- [Configuring columns used when training](custom-config-columns.md "custom-config-columns.md")
- [Optimizing a solution for an additional
  objective](optimizing-solution-for-objective.md "optimizing-solution-for-objective.md")
- [Optimizing a solution with events configuration](optimizing-solution-events-config.md "optimizing-solution-events-config.md")
- [Hyperparameters and
  HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md")
- [Choosing the item interaction data used for training](event-values-types.md "event-values-types.md")
- [Cloning a solution (console)](cloning-solution.md "cloning-solution.md")
