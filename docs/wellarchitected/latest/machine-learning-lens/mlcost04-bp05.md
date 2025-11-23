# MLCOST04-BP05 Use automated machine learning

Automate your model development process by using systems that
experiment with and select the best algorithms from high-performing
options. These automated systems test various solutions and
parameter settings to achieve optimal models, significantly speeding
up development while reducing the need for manual experimentation
and comparisons.

**Desired outcome:** You gain the
ability to develop high-quality machine learning models in a
fraction of the time traditionally required. By using automated
machine learning tools like Amazon SageMaker AI Autopilot, you can
focus on business problems rather than algorithm selection and
parameter tuning. Your team can produce optimized models with better
performance, reduce development costs, and accelerate time-to-market
for ML-powered solutions.

**Common anti-patterns:**

- Manually testing multiple algorithms and configurations one by
  one.
- Spending excessive time on hyperparameter tuning without
  systematic approach.
- Using the same algorithm for each problem without considering
  alternatives.
- Neglecting cross-validation during model selection.

**Benefits of establishing this best
practice:**

- Dramatically reduced time to develop production-ready models.
- Access to a broader range of algorithms and optimization
  techniques.
- Improved model performance through systematic evaluation.
- Lower costs through optimized resource utilization.
- Ability for domain experts to build models without deep ML
  expertise.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Automated machine learning (AutoML) systems democratize the
process of building machine learning models. By automating key
steps in model development—from data preparation to algorithm
selection and hyperparameter tuning—these systems enable even
those without extensive machine learning expertise to develop
high-quality models.

When using AutoML solutions like Amazon SageMaker AI Autopilot,
you provide your dataset and define your objective, and the system
handles the complex work of exploring potential algorithms,
optimizing parameters, and evaluating model performance. The
system applies cross-validation procedures automatically to check
that models can generalize well to new data. By ranking optimized
models by their performance, AutoML can identify the best solution
for your specific problem.

Beyond simply producing models, modern AutoML systems provide
visibility into the development process, allowing you to
understand what choices were made and why. This transparency
builds trust in the models and provides learning opportunities for
your team to understand what approaches work best for different
problem types.

### Implementation steps

1. **Evaluate your use case
   compatibility**. Determine if your ML problem is
   suitable for automated machine learning solutions. AutoML
   works particularly well for standard machine learning tasks
   like classification, regression, and some time series
   forecasting scenarios.
2. **Prepare your data for
   AutoML**. Clean your dataset, handle missing
   values, and convert categorical features appropriately.
   While AutoML handles feature engineering, providing
   high-quality data improves results. Use
   [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/ "https://aws.amazon.com/sagemaker/data-wrangler/") to simplify this preparation
   process.
3. **Set up Amazon SageMaker AI Autopilot
   with Canvas**. Open
   [Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md"), import your dataset into Amazon S3,
   and configure to access this data. Define your target
   variable and specify your problem type (classification or
   regression) if known.
4. **Launch the automated ML
   job**. Start Canvas training and let it analyze
   your data, select algorithms, and optimize models. Specify
   resources like maximum runtime and instance types to control
   costs. Canvas will automatically handle data preprocessing,
   feature engineering, algorithm selection, and hyperparameter
   optimization.
5. **Review candidate models**.
   Examine the generated models along with their performance
   metrics. Autopilot provides detailed reports on the data
   exploration, feature engineering decisions, and model
   optimization steps it performed.
6. **Deploy the best model**.
   Select the best-performing model from the Canvas
   recommendations and deploy it using Amazon SageMaker AI's
   deployment capabilities. You can deploy as a real-time
   endpoint or for batch inference depending on your needs.
7. **Monitor and evaluate
   performance**. Set up model monitoring to track
   your model's performance in production and detect concept
   drift. Use
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to automate this process.
8. **Customize and refine
   models**. If needed, extract and customize the
   models generated by Autopilot. The solution provides full
   visibility into the notebooks and artifacts it creates,
   allowing you to further refine specific aspects of the
   model.
9. **Enhance model development with
   foundation models**. Use
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") to incorporate foundation model capabilities
   into your AutoML workflow for tasks like text processing,
   content generation, and multimodal applications. Foundation
   models can complement traditional ML approaches handled by
   Autopilot.
10. **Use enhanced Canvas capabilities
    with Q integration**. Use
    [SageMaker AI
    Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md") with improved natural language support and Q
    integration for conversational data analysis, enabling
    business users to build models through natural language
    interactions.
11. **Implement intelligent preprocessing
    with generative AI**. Use generative AI tools to
    enhance data preprocessing, augment training datasets,
    generate synthetic data for edge cases, and improve feature
    engineering through intelligent text and image processing.

## Resources

**Related documents:**

- [Getting
  started with using Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas-getting-started.md "../../../sagemaker/latest/dg/canvas-getting-started.md")
- [SageMaker AI
  Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md")
- [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/ "https://aws.amazon.com/sagemaker/data-wrangler/")

**Related examples:**

- [SageMaker AI Autopilot](https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/automl/README.rst "https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/automl/README.rst")
- [Amazon SageMaker AI Autopilot Sample Notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/autopilot "https://github.com/aws/amazon-sagemaker-examples/tree/main/autopilot")
