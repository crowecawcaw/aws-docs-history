We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Creating an ML Model

After you've created a datasource, you are ready to create an ML model. If you use the Amazon Machine Learning
console to create a model, you can choose to use the default settings or you
customize your model by applying custom options.

Custom options include:

- Evaluation settings: You can choose to have Amazon ML reserve a portion of the input data
  to evaluate the predictive quality of the ML model. For information about evaluations, see
  [Evaluating ML Models](evaluating_models.md "evaluating_models.md").
- A recipe: A recipe tells Amazon ML which attributes and attribute
  transformations are available for model training. For information about
  Amazon ML recipes, see [Feature Transformations with Data Recipes](feature-transformations-with-data-recipes.md "feature-transformations-with-data-recipes.md").
- Training parameters: Parameters control certain properties of the training process and
  of the resulting ML model. For more information about training parameters, see [Training Parameters](training-parameters.md "training-parameters.md").
  To select or specify values for these settings, choose the **Custom** option
  when you use the Create ML Model wizard. If you want Amazon ML to apply the
  default settings, choose **Default**.

When you create an ML model, Amazon ML selects the type of learning algorithm it
will use based on the attribute type of your target attribute. (The target attribute is the
attribute that contains the "correct" answers.) If your target attribute is Binary, Amazon ML creates
a binary classification model, which uses the logistic regression algorithm. If your target attribute
is Categorical, Amazon ML creates a multiclass model, which uses a multinomial logistic regression
algorithm. If your target attribute is Numeric, Amazon ML creates a regression model, which uses a linear
regression algorithm.

###### Topics

- [Prerequisites](#model-prereqs "#model-prereqs")
- [Creating an ML Model with Default
  Options](#creating-ml-model-using-default-settings "#creating-ml-model-using-default-settings")
- [Creating an ML Model with Custom
  Options](#creating-ml-model-using-custom-settings "#creating-ml-model-using-custom-settings")

## Prerequisites

Before using the Amazon ML console to create an ML model, you need to create two datasources,
one for training the model and one for evaluating the model. If you haven't created two
datasources, see [Step 2: Create a Training Datasource](step-2-create-a-datasource.md "step-2-create-a-datasource.md") in the tutorial.

## Creating an ML Model with Default

Options

Choose the **Default** options, if you want Amazon ML to:

- Split the input data to use the first 70 percent for training and use the remaining
  30 percent for evaluation
- Suggest a recipe based on statistics collected on the training datasource, which is
  70 percent of the input datasource
- Choose default training parameters

###### To choose default options

1. In the Amazon ML console, choose **Amazon Machine Learning**, and then choose
   **ML models**.
2. On the **ML models** summary page, choose **Create a new ML
   model**.
3. On the **Input data** page, make sure that **I already
   created a datasource pointing to my S3 data** is selected.
4. In the table, choose your datasource, and then choose
   **Continue**.
5. On the **ML model settings** page, for **ML model
   name**, type a name for your ML model.
6. For **Training and evaluation settings**, make sure that
   **Default** is selected.
7. For **Name this evaluation**, type a name for the evaluation, and then
   choose **Review**. Amazon ML bypasses the rest of the wizard and takes you to
   the **Review** page.
8. Review your data, delete any tags copied from the datasource that you don't
   want applied to your model and evaluations, and then choose **Finish**.

## Creating an ML Model with Custom

Options

Customizing your ML model allows you to:

- Provide your own recipe. For information about how to provide your own recipe, see
  [Recipe Format
  Reference](recipe-format-reference.md "recipe-format-reference.md").
- Choose training parameters. For more information about training parameters, see [Training Parameters](training-parameters.md "training-parameters.md").
- Choose a training/evaluation splitting ratio other than the default 70/30 ratio or
  provide another datasource that you have already prepared for evaluation. For information
  about splitting strategies, see [Splitting Your Data](splitting-types.md "splitting-types.md").

You can also choose the default values for any of these settings.

If you've already created a model using the default options and want to improve your
model's predictive performance, use the **Custom** option to create a new model
with some customized settings. For example, you might add more feature transformations to the
recipe or increase the number of passes in the training parameter.

###### To create a model with custom options

1. In the Amazon ML console, choose **Amazon Machine Learning**, and then choose
   **ML models**.
2. On the **ML models** summary page, choose **Create a new ML
   model**.
3. If you have already created a datasource, on the **Input data** page,
   choose **I already created a datasource pointing to my S3 data**. In the
   table, choose your datasource, and then choose **Continue**.

If you need to create a datasource, choose **My data is in S3, and I need to
create a datasource**, choose **Continue**. You are redirected
to the **Create a Datasource** wizard. Specify whether your data is in
**S3** or **Redshift**, then choose **Verify**.
Complete the procedure for creating a datasource.

After you have created a datasource, you are redirected to the next step in the
**Create ML Model** wizard. 4. On the **ML model settings** page, for **ML model
name**, type a name for your ML model. 5. In **Select training and evaluation settings**, choose
**Custom**, and then choose **Continue**. 6. On the **Recipe** page, you can [customize a recipe](recipe-format-reference.md "recipe-format-reference.md"). If you don't want to
customize a recipe, Amazon ML suggests one for you. Choose
**Continue**. 7. On the **Advanced settings** page, specify the **Maximum ML
model Size**, the **Maximum number of data passes**, the
**Shuffle type for training data**, the **Regularization
type**, and the **Regularization amount**. If you don't
specify these, Amazon ML uses the default training parameters.

For more information about these parameters and their defaults, see [Training Parameters](training-parameters.md "training-parameters.md").

Choose **Continue**. 8. On the **Evaluation** page, specify whether you want to evaluate the
ML model immediately. If you don't want to evaluate the ML model now, choose
**Review**.

If you want to evaluate the ML model now:

    1. For **Name this evaluation**, type a name for the
     evaluation.
    2. For **Select evaluation data**, choose whether you want Amazon ML to
     reserve a portion of the input data for evaluation and, if you do, how you want to
     split the datasource, or choose to provide a different datasource for evaluation.
    3. Choose **Review**.

9. On the **Review** page, edit your selections, delete any tags copied
   from the datasource that you don't want applied to your model and evaluations, and then choose
   **Finish**.

After you have created the model, see [Step 4: Review the ML Model's Predictive
Performance and Set a Score Threshold](step-4-review-model-and-set-cutoff.md "step-4-review-model-and-set-cutoff.md").
