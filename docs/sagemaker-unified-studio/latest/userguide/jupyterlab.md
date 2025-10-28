# Using the JupyterLab IDE in Amazon SageMaker Unified Studio

The JupyterLab page of Amazon SageMaker Unified Studio provides a JupyterLab interactive development environment
(IDE) for you to use as you perform data integration, analytics, or machine learning in your
projects. Amazon SageMaker Unified Studio notebooks are powered by JupyterLab spaces.

By default, the JupyterLab application comes with the Amazon SageMaker Distribution image.
The distribution image includes popular packages such as the following:

- PyTorch
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn
  Amazon SageMaker Unified Studio includes a sample notebook that you can use to get started. You can also choose to
  create new notebooks for your business use cases.

Amazon SageMaker Unified Studio notebooks include the following key features:

- Manage configurations to scale the instance vertically if the job being submitted
  demands it.
- Access metadata to find out information such as the path to the Amazon S3 bucket where data
  is being stored.
- Perform Git operations for version control.
- Use Amazon Q chat functionality to ask questions and generate code using prompts.
- Perform code completion using Amazon Q Developer.

###### Note

The JupyterLab IDE has an idle shutdown feature that shuts down the IDE after it has been
idle for 60 minutes. This means that if both the IDE kernel and terminal have been unused for
an hour, the IDE stops running. In order to start using the IDE again after idle shutdown, you
would need to navigate to the JupyterLab page again and click on the Start button to restart
the kernel in the JupyterLab IDE.
