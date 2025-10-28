# Programming Model for Amazon SageMaker AI

Making API calls directly from code is cumbersome, and requires you to write code to
authenticate your requests. Amazon SageMaker AI provides the following alternatives:

- **Use the SageMaker AI console**–With the console,
  you don't write any code. You use the console UI to start model training or
  deploy a model. The console works well for simple jobs, where you use a built-in
  training algorithm and you don't need to preprocess training data.
- **Modify the example Jupyter
  notebooks**–SageMaker AI provides several Jupyter notebooks that train
  and deploy models using specific algorithms and datasets. Start with a notebook
  that has a suitable algorithm and modify it to accommodate your data source and
  specific needs.
- **Write model training and inference code from
  scratch**–SageMaker AI provides multiple AWS SDK languages (listed
  in the overview) and the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"), a high-level Python library that
  you can use in your code to start model training jobs and deploy the resulting
  models.

   

      + **The SageMaker Python SDK**–This
       Python library simplifies model training and deployment. In addition to
       authenticating your requests, the library abstracts platform specifics
       by providing simple methods and default parameters. For example:


       




      	- To deploy your model, you call only the `deploy()`
      	 method. The method creates a SageMaker AI model artifact, an endpoint
      	 configuration, then deploys the model on an endpoint.
      	- If you use a custom framework script for model training, you
      	 call the `fit()` method. The method creates a .gzip
      	 file of your script, uploads it to an Amazon S3 location, and then
      	 runs it for model training, and other tasks. For more
      	 information, see [Machine Learning Frameworks and Languages](frameworks.md "frameworks.md").
      	- To set defaults for SageMaker API calls made by the SageMaker AI Python
      	 SDK, you use a default configuration dictionary. For more
      	 information, see [Configuring and using defaults with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/overview.html#configuring-and-using-defaults-with-the-sagemaker-python-sdk "https://sagemaker.readthedocs.io/en/stable/overview.html#configuring-and-using-defaults-with-the-sagemaker-python-sdk").
      + **The AWS SDKs** – The SDKs
       provide methods that correspond to the SageMaker API (see [`Operations`](../APIReference/API_Operations.md "../APIReference/API_Operations.md")). Use the SDKs to programmatically
       start a model training job and host the model in SageMaker AI. SDK clients
       handle authentication for you, so you don't need to write authentication
       code. They are available in multiple languages and platforms. For more
       information, see the preceding list in the overview.

  In [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md"), you train and deploy a model using
  an algorithm provided by SageMaker AI. That exercise shows how to use both of these
  libraries. For more information, see [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md").

- **Integrate SageMaker AI into your Apache Spark
  workflow**–SageMaker AI provides a library for calling its APIs from
  Apache Spark. With it, you can use SageMaker AI-based estimators in an Apache Spark
  pipeline. For more information, see [Apache Spark with Amazon SageMaker AI](apache-spark.md "apache-spark.md").
