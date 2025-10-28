# Create a Regression

or Classification Autopilot experiment for tabular data using the Studio Classic UI

###### Important

As of November 30, 2023, Autopilot's UI is migrating to [Amazon SageMaker Canvas](canvas.md "canvas.md") as part of the
updated [Amazon SageMaker Studio](studio-updated.md "studio-updated.md") experience. SageMaker Canvas provides analysts
and citizen data scientists no-code capabilities for tasks such as data preparation, feature engineering,
algorithm selection, training and tuning, inference, and more. Users can leverage built-in visualizations
and what-if analysis to explore their data and different scenarios, with automated predictions enabling
them to easily productionize their models. Canvas supports a variety of use cases,
including computer vision, demand forecasting, intelligent search, and generative AI.

Users of
[Amazon SageMaker Studio Classic](studio.md "studio.md"), the previous experience of [Studio](studio-updated.md "studio-updated.md"),
can continue using the Autopilot UI in Studio Classic. Users with coding experience can continue using all
[API references](autopilot-reference.md "autopilot-reference.md")
in any supported SDK for technical implementation.

If you have been using Autopilot in Studio Classic until now and want to migrate to SageMaker Canvas,
you might have to grant additional permissions to your user profile or IAM role so that you can create and use the SageMaker Canvas application.
For more information, see [(Optional) Migrate from
Autopilot in Studio Classic to SageMaker Canvas](studio-updated-migrate-ui.md#studio-updated-migrate-autopilot "studio-updated-migrate-ui.md#studio-updated-migrate-autopilot").

All UI-related instructions in this guide pertain to Autopilot's standalone features before
migrating to [Amazon SageMaker Canvas](canvas.md "canvas.md"). Users following these instructions should use [Studio Classic](studio.md "studio.md").

You can use the Amazon SageMaker Studio Classic UI to create Autopilot experiments for classification or
regression problems on tabular data. The UI helps you specify the name of your experiment,
provide locations for the input and output data, and specify which target data to predict.
Optionally, you can also specify the type of problem that you want to solve (regression,
classification, multiclass classification), choose your modeling strategy (_stacked ensembles_ or _hyperparameters
optimization_), select the list of algorithms used by the Autopilot job to train the
data, and more.

The UI has descriptions, toggle switches, dropdown menus, radio buttons, and more to help
you navigate creating your model candidates. After the experiment runs, you can compare trials
and delve into the details of the pre-processing steps, algorithms, and hyperparameter ranges of
each model. Optionally, you can download their [explainability](autopilot-explainability.md "autopilot-explainability.md") and [performance](autopilot-model-insights.md "autopilot-model-insights.md") reports. Use the provided [notebooks](autopilot-automate-model-development-notebook-output.md "autopilot-automate-model-development-notebook-output.md") to see the results of the automated data exploration or the candidate model
definitions.

Alternatively, you can use Autopilot AutoML API in [Create Regression or
Classification Jobs for Tabular Data Using the AutoML API](autopilot-automate-model-development-create-experiment.md "autopilot-automate-model-development-create-experiment.md").

###### To create an Autopilot experiment using Studio Classic UI

1. Sign in at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/"), choose **Studio** from the left
   navigation pane, select your Domain and user profile, then **Open
   Studio**.
2. In Studio, choose the Studio Classic icon in the top left navigation pane. This opens a
   Studio Classic app.
3. Run or open a Studio Classic application from the space of your choice, or **Create
   Studio Classic space.** . On the **Home** tab, choose the
   **AutoML** card. This opens a new **AutoML** tab.
4. Choose **Create an AutoML experiment**. This opens a new
   **Create experiment** tab.
5. In the **Experiment and data details** section, enter the following
   information:
   1. **Experiment name** – Must be unique to your account in the
      current AWS Region and contain a maximum of 63 alphanumeric characters. Can include
      hyphens (-) but not spaces.
   2. **Input data** – Provide the Amazon Simple Storage Service (Amazon S3)
      bucket location of your input data. This S3 bucket must be in your current AWS Region.
      The URL must be in an `s3://` format where Amazon SageMaker AI has write permissions.
      The file must be in CSV or Parquet format and contain at least 500 rows. Select
      **Browse** to scroll through available paths and
      **Preview** to see a sample of your input data.
   3. **Is your S3 input a manifest file?** – A manifest file
      includes metadata with your input data. The metadata specifies the location of your data
      in Amazon S3. It also specifies how the data is formatted and which attributes from the
      dataset to use when training your model. You can use a manifest file as an alternative
      to preprocessing when your labeled data is being streamed in `Pipe`
      mode.
   4. **Auto split data?** – Autopilot can split your data into an
      80-20% split for training and validation data. If you prefer a custom split, you can
      choose the **Specify split ratio**. To use a custom dataset for
      validation, choose **Provide a validation set**.
   5. **Output data location (S3 bucket)** – The name of the S3
      bucket location where you want to store the output data. The URL for this bucket must be
      in an Amazon S3 format where Amazon SageMaker AI has write permissions. The S3 bucket must be in the
      current AWS Region. Autopilot can also create this for you in the same location as your
      input data.

6. Choose **Next: Target and features**. The **Target and
   features** tab opens.
7. In the **Target and features** section:
   - Select a column to set as a target for model predictions.
   - Optionally, you can pass the name of a sample weights column in the **Sample
     weight** section to request your dataset rows to be weighted during training
     and evaluation. For more information on the available objective metrics, see [Autopilot weighted metrics](autopilot-metrics-validation.md#autopilot-weighted-metrics "autopilot-metrics-validation.md#autopilot-weighted-metrics").

   ###### Note

   Support for sample weights is available in [ensembling mode](autopilot-model-support-validation.md#autopilot-training-mode "autopilot-model-support-validation.md#autopilot-training-mode") only.
   - You can also select features for training and change their data type. The following
     data types are available: `Text`, `Numerical`,
     `Categorical`, `Datetime`, `Sequence`, and
     `Auto`. All features are selected by default.

8. Choose **Next: Training method**. The **Training
   method** tab opens.
9. In the **Training method** section, select your training
   option: **Ensembling**, **Hyperparameter optimization
   (HPO)**, or **Auto** to let Autopilot choose the training method
   automatically based on the dataset size. Each training mode runs a pre-defined set of
   algorithms on your dataset to train model candidates. By default, Autopilot pre-selects all the
   available algorithms for the given training mode. You can run an Autopilot training experiment
   with all the algorithms or choose your own subset.

For more information on the training modes and the available algorithms, see the
**Autopilot training modes** section in the [Training modes and algorithms](autopilot-model-support-validation.md "autopilot-model-support-validation.md") page. 10. Choose **Next: Deployment and advanced settings** to open the
**Deployment and advanced settings** tab. Settings include the
auto-display endpoint name, machine learning problem type, and additional choices for
running your experiment.

    1. **Deployment settings** – Autopilot can automatically create an
     endpoint and deploy your model for you.


    To auto-deploy to an automatically generated endpoint, or to provide an endpoint
     name for custom deployment, set the toggle to **Yes** under
     **Auto deploy?** If you are importing data from Amazon SageMaker Data Wrangler, you have
     additional options to auto-deploy the best model with or without the transforms from
     Data Wrangler.


    ###### Note

    If your Data Wrangler flow contains multi-row operations such as `groupby`,
     `join`, or `concatenate`, you can't auto-deploy with these
     transforms. For more information, see [Automatically Train Models on
     Your Data Flow](data-wrangler-autopilot.md "data-wrangler-autopilot.md").
    2. **Advanced settings (optional)** – Autopilot provides
     additional controls to manually set experimental parameters such as defining your
     problem type, time constraints on your Autopilot job and trials, security, and encryption
     settings.


    ###### Note

    Autopilot supports the setting of default values to simplify the configuration of
     Autopilot experiments using Studio Classic UI. Administrators can use Studio Classic [lifecycle
     configurations](studio-lcc.md "studio-lcc.md") (LCC) to set infrastructure, networking, and security values
     in configuration files and pre-populate the *advanced
     settings* of `AutoML` jobs.

    To learn about how administrators can automate the customization of an Autopilot
     experiment, see [Configure the default
     parameters of an Autopilot experiment (for administrators)](autopilot-set-default-parameters-create-experiment.md "autopilot-set-default-parameters-create-experiment.md").


    	1. **Machine learning problem type** – Autopilot can
    	 automatically infer the type of supervised learning problem from your dataset. If
    	 you prefer to choose it manually, you can use the **Select the machine
    	 learning problem type** dropdown menu. Note that it defaults to **Auto**. In some cases, SageMaker AI is unable to infer accurately.
    	 When that happens, you must provide the value for the job to succeed. In particular,
    	 you can choose from the following types:




    		* **Binary classification**– Binary
    		 classification assigns input data to one of two predefined and mutually
    		 exclusive classes, based on their attributes, such as medical diagnosis based on
    		 results of diagnostic tests that determine if someone has a disease.
    		* **Regression** – Regression establishes
    		 a relationship between the input variables (also known as independent variables
    		 or features) and the target variable (also known as the dependent variable).
    		 This relationship is captured through a mathematical function or model that maps
    		 the input variables to a continuous output. It is commonly used for tasks such
    		 as predicting house prices based on features like square footage and the number
    		 of bathrooms, stock market trends, or estimating sales figures.
    		* **Multiclass classification** –
    		 Multiclass classification assigns input data to one of several classes based on
    		 their attributes, like the prediction of the topic most relevant to a text
    		 document, such as politics, finance, or philosophy.
    	2. **Runtime** – You can define a maximum time limit. Upon
    	 reaching the time limit, trials and jobs that exceed the time constraint
    	 automatically stop.
    	3. **Access** – You can choose the role that Amazon SageMaker Studio Classic
    	 assumes to gain temporary access to AWS services (in particular, SageMaker AI and Amazon S3) on
    	 your behalf. If no role is explicitly defined, Studio Classic automatically uses the
    	 default SageMaker AI execution role attached to your user profile.
    	4. **Encryption** – To enhance the security of your data at
    	 rest and protect it against unauthorized access, you can specify encryption keys to
    	 encrypt data in your Amazon S3 buckets and in the Amazon Elastic Block Store (Amazon EBS) volume attached to
    	 your Studio Classic domain.
    	5. **Security** – You can choose the virtual private cloud
    	 (Amazon VPC) in which your SageMaker AI job runs. Ensure that the Amazon VPC has access to your input
    	 and output Amazon S3 buckets.
    	6. **Project** – Specify the name of the SageMaker AI project to
    	 associate with this Autopilot experiment and model outputs. When you specify a project,
    	 Autopilot tags the project to an experiment. This lets you know which model outputs are
    	 associated with this project.
    	7. **Tags** – Tags are an array of key-value pairs. Use
    	 tags to categorize your resources from AWS services, such as their purpose, owner,
    	 or environment.
    3. Choose **Next: Review and create** to get a summary of your Autopilot
     experiment before you create it.

11. Select **Create experiment**.The creation of the experiment starts an
    Autopilot job in SageMaker AI. Autopilot provides the status of the experiment, information on the data
    exploration process and model candidates in notebooks, a list of generated models and their
    reports, and the job profile used to create them.

For information on the notebooks generated by an Autopilot job, see [Autopilot notebooks
generated to manage AutoML tasks](autopilot-automate-model-development-notebook-output.md "autopilot-automate-model-development-notebook-output.md"). For information on
the details of each model candidate and their reports, see [View model details](autopilot-models-details.md "autopilot-models-details.md") and [View an Autopilot model performance
report](autopilot-model-insights.md "autopilot-model-insights.md").

###### Note

To avoid incurring unnecessary charges: If you deploy a model that is no longer needed,
delete the endpoints and resources that were created during that deployment. Information about
pricing instances by Region is available at [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").
