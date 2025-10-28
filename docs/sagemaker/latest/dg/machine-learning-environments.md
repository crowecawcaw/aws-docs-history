# Machine learning environments offered by Amazon SageMaker AI

###### Important

Amazon SageMaker Studio and Amazon SageMaker Studio Classic are two of the machine learning environments that you can use to interact with SageMaker AI.

If your domain was created after November 30, 2023, Studio is your default experience.

If your domain was created before November 30, 2023, Amazon SageMaker Studio Classic is your default experience. To use Studio if Amazon SageMaker Studio Classic is your default experience, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md").

When you migrate from Amazon SageMaker Studio Classic to Amazon SageMaker Studio, there is no loss in feature availability. Studio Classic also exists as an IDE within Amazon SageMaker Studio to help you run your legacy machine learning workflows.

SageMaker AI supports the following machine learning environments:

- _Amazon SageMaker Studio_ (Recommended): The latest web-based experience for running ML workflows with a suite of IDEs.
  Studio supports the following applications:
  - Amazon SageMaker Studio Classic
  - Code Editor, based on Code-OSS, Visual Studio Code - Open Source
  - JupyterLab
  - Amazon SageMaker Canvas
  - RStudio

- _Amazon SageMaker Studio Classic_: Lets you build, train,
  debug, deploy, and monitor your machine learning models.
- _Amazon SageMaker Notebook Instances_: Lets you prepare and process data, and train and deploy
  machine learning models from a compute instance running the Jupyter Notebook application.
- _Amazon SageMaker Studio Lab_: Studio Lab is a free service that gives you access to
  AWS compute resources, in an environment based on open-source JupyterLab, without
  requiring an AWS account.
- _Amazon SageMaker Canvas_: Gives you the ability to use machine
  learning to generate predictions without needing to code.
- _Amazon SageMaker geospatial_: Gives you the ability to
  build, train, and deploy geospatial models.
- _RStudio on Amazon SageMaker AI_: RStudio is an IDE for
  [R](https://aws.amazon.com/blogs/opensource/getting-started-with-r-on-amazon-web-services/ "https://aws.amazon.com/blogs/opensource/getting-started-with-r-on-amazon-web-services/"),
  with a console, syntax-highlighting editor that supports direct
  code execution, and tools for plotting, history, debugging and workspace
  management.
- _SageMaker HyperPod_: SageMaker HyperPod lets you provision resilient
  clusters for running machine learning (ML) workloads and developing state-of-the-art
  models such as large language models (LLMs), diffusion models, and foundation models
  (FMs).
  To use these machine learning environments, you or your organization's
  administrator must create an Amazon SageMaker AI domain. The exceptions are Studio Lab, SageMaker Notebook Instances, and SageMaker HyperPod.

Instead of manually provisioning resources and managing permissions for yourself and your users, you can create a Amazon DataZone domain.
The process of creating a Amazon DataZone domain creates a corresponding Amazon SageMaker AI domain with AWS Glue or Amazon Redshift databases for your ETL workflows. Setting up a domain through Amazon DataZone reduces the amount of time it takes to set up SageMaker AI
environments for your users.
For more information about setting up a Amazon SageMaker AI domain within Amazon DataZone, see [Set up SageMaker Assets (administrator guide)](sm-assets-set-up.md "sm-assets-set-up.md").

Users within the Amazon DataZone domain have permissions to all Amazon SageMaker AI actions, but their permissions are scoped down to resources within the Amazon DataZone domain.

Creating a Amazon DataZone domain streamlines creating a domain that allows your users to share data and models with each other.
For information about how they can share data and models, see [Controlled access to assets with Amazon SageMaker Assets](sm-assets.md "sm-assets.md").

###### Topics

- [Amazon SageMaker Studio](studio-updated.md "studio-updated.md")
- [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md")
- [Amazon SageMaker notebook instances](nbi.md "nbi.md")
- [Amazon SageMaker Studio Lab](studio-lab.md "studio-lab.md")
- [Amazon SageMaker Canvas](canvas.md "canvas.md")
- [Amazon SageMaker geospatial capabilities](geospatial.md "geospatial.md")
- [RStudio on Amazon SageMaker AI](rstudio.md "rstudio.md")
- [Code Editor in Amazon SageMaker Studio](code-editor.md "code-editor.md")
- [Amazon SageMaker HyperPod](sagemaker-hyperpod.md "sagemaker-hyperpod.md")
- [Generative AI in SageMaker notebook environments](jupyterai.md "jupyterai.md")
- [Amazon Q Developer](studio-updated-amazon-q.md "studio-updated-amazon-q.md")
- [Amazon SageMaker Partner AI Apps overview](partner-apps.md "partner-apps.md")
