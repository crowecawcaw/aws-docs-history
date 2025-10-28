We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Suggested Recipes

When you create a new datasource in Amazon ML and statistics are
computed for that datasource, Amazon ML will also create a
suggested recipe that can be used to create a new ML model from
the datasource. The suggested datasource is based on the data and
target attribute present in the data, and provides a useful
starting point for creating and fine-tuning your ML models.

To use the suggested recipe on the Amazon ML console, choose
**Datasource** or
**Datasource and ML model** from
the **Create new** drop down list.
For ML model settings, you will have a choice of Default or Custom
Training and Evaluation settings in the **ML
Model Setting**s step of the
**Create ML Model** wizard. If you
pick the Default option, Amazon ML will automatically use the
suggested recipe. If you pick the Custom option, the recipe editor
in the next step will display the suggested recipe, and you will
be able to verify or modify it as needed.

###### Note

Amazon ML allows you to create a datasource and then immediately
use it to create an ML model, before statistics computation is
completed. In this case, you will not be able to see the
suggested recipe in the Custom option, but you will still be
able to proceed past that step and have Amazon ML use the
default recipe for model training.

To use the suggested recipe with the Amazon ML API, you can pass
an empty string in both Recipe and RecipeUri API parameters. It is
not possible to retrieve the suggested recipe using the Amazon ML
API.
