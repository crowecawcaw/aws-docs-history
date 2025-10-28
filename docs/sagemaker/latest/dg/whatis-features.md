# Amazon SageMaker AI Features

Amazon SageMaker AI includes the following features.

###### Topics

- [New features for re:Invent 2024](#whatis-features-alpha-new "#whatis-features-alpha-new")
- [Machine learning environments](#whatis-features-alpha-mle "#whatis-features-alpha-mle")
- [Major features](#whatis-features-alpha-major "#whatis-features-alpha-major")

## New features for re:Invent 2024

SageMaker AI includes the following new features for re:Invent 2024.

**[HyperPod recipes](sagemaker-hyperpod-recipes.md "sagemaker-hyperpod-recipes.md")**

You can run recipes within Amazon SageMaker HyperPod or as SageMaker training jobs. You use the
HyperPod training adapter as the framework to help you run end-to-end training
workflows. The training adapter is built on the NVIDIA NeMo framework and Neuronx
Distributed Training package.

**[HyperPod in Studio](sagemaker-hyperpod-studio.md "sagemaker-hyperpod-studio.md")**

In Amazon SageMaker Studio, you can launch machine learning workloads on HyperPod
clusters and view HyperPod cluster information. The increased visibility into
cluster details and hardware metrics can help your team identify the right candidate for
your pre-training or fine-tuning workloads.

**[HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md")**

Amazon SageMaker HyperPod task governance is a robust management system designed to
streamline resource allocation and ensure efficient utilization of compute resources
across teams and projects for your Amazon EKS clusters. HyperPod task governance
also provides Amazon EKS cluster Observability, offering real-time visibility into cluster
capacity, compute availability and usage, team allocation and utilization, and task run
and wait time information.

**[Amazon SageMaker Partner AI Apps](partner-apps.md "partner-apps.md")**

With Amazon SageMaker Partner AI Apps, users get access to generative artificial intelligence (AI) and
machine learning (ML) development applications built, published, and distributed by
industry-leading application providers. Partner AI Apps are certified to run on SageMaker AI. With
Partner AI Apps, users can accelerate and improve how they build solutions based on foundation
models (FM) and classic ML models without compromising the security of their sensitive
data, which stays completely within their trusted security configuration and is never
shared with a third party.

**[Q Developer is
available in Canvas](canvas-q.md "canvas-q.md")**

You can chat with Amazon Q Developer in Amazon SageMaker Canvas using natural language for generative AI
assistance with solving your machine learning problems. You can converse with
Q Developer to discuss the steps of a machine learning workflow and leverage Canvas
functionality such as data transforms, model building, and deployment.

**[SageMaker training
plans](reserve-capacity-with-training-plans.md "reserve-capacity-with-training-plans.md")**

Amazon SageMaker training plans are a compute reservation capability designed for
large-scale AI model training workloads running on SageMaker training jobs and
HyperPod clusters. They provide predictable access to high-demand
GPU-accelerated computing resources within specified timelines. You can specify a
desired timeline, duration, and maximum compute resources, and SageMaker training plans
automatically manages infrastructure setup, workload execution, and fault recovery. This
allows for efficiently planning and executing mission-critical AI projects with a
predictable cost model.

## Machine learning environments

SageMaker AI includes the following machine learning environments.

**[SageMaker Canvas](canvas.md "canvas.md")**

An auto ML service that gives people with no coding experience the ability to build
models and make predictions with them.

**[Code
Editor](code-editor.md "code-editor.md")**

Code Editor extends Studio so that you can write, test, debug and run your
analytics and machine learning code in an environment based on Visual Studio Code - Open
Source ("Code-OSS").

**[SageMaker geospatial capabilities](geospatial.md "geospatial.md")**

Build, train, and deploy ML models using geospatial data.

**[SageMaker
HyperPod](sagemaker-hyperpod.md "sagemaker-hyperpod.md")**

Amazon SageMaker HyperPod is a capability of SageMaker AI that provides an always-on machine learning
environment on resilient clusters that you can run any machine learning workloads for
developing large machine learning models such as large language models (LLMs) and
diffusion models.

**[JupyterLab in Studio](studio-updated-jl.md "studio-updated-jl.md")**

JupyterLab in Studio improves latency and reliability for Studio
Notebooks

**[Studio](studio-updated.md "studio-updated.md")**

Studio is the latest web-based experience for running ML workflows. Studio
offers a suite of IDEs, including Code Editor, a new Jupyterlab application, RStudio,
and Studio Classic.

**[Amazon SageMaker Studio Classic](studio.md "studio.md")**

An integrated machine learning environment where you can build, train, deploy, and
analyze your models all in the same application.

**[SageMaker Studio Lab](studio-lab.md "studio-lab.md")**

A free service that gives customers access to AWS compute resources in an
environment based on open-source JupyterLab.

**[RStudio on Amazon SageMaker AI](rstudio.md "rstudio.md")**

An integrated development environment for R, with a console, syntax-highlighting
editor that supports direct code execution, and tools for plotting, history, debugging
and workspace management.

## Major features

SageMaker AI includes the following major features in alphabetical order excluding any SageMaker AI
prefix.

**[Amazon Augmented
AI](a2i-use-augmented-ai-a2i-human-review-loops.md "a2i-use-augmented-ai-a2i-human-review-loops.md")**

Build the workflows required for human review of ML predictions. Amazon A2I brings
human review to all developers, removing the undifferentiated heavy lifting associated
with building human review systems or managing large numbers of human reviewers.

**[AutoML step](build-and-manage-steps.md "build-and-manage-steps.md")**

Create an AutoML job to automatically train a model in Pipelines.

**[SageMaker Autopilot](autopilot-automate-model-development.md "autopilot-automate-model-development.md")**

Users without machine learning knowledge can quickly build classification and
regression models.

**[Batch Transform](batch-transform.md "batch-transform.md")**

Preprocess datasets, run inference when you don't need a persistent endpoint, and
associate input records with inferences to assist the interpretation of results.

**[SageMaker Clarify](clarify-configure-processing-jobs.md#clarify-fairness-and-explainability "clarify-configure-processing-jobs.md#clarify-fairness-and-explainability")**

Improve your machine learning models by detecting potential bias and help explain
the predictions that models make.

**[Collaboration with shared spaces](domain-space.md "domain-space.md")**

A shared space consists of a shared JupyterServer application and a shared
directory. All user profiles in a Amazon SageMaker AI domain have access to all shared spaces in the
domain.

**[SageMaker Data Wrangler](data-wrangler.md "data-wrangler.md")**

Import, analyze, prepare, and featurize data in SageMaker Studio. You can integrate Data
Wrangler into your machine learning workflows to simplify and streamline data
pre-processing and feature engineering using little to no coding. You can also add your
own Python scripts and transformations to customize your data prep workflow.

**[Data Wrangler data
preparation widget](data-wrangler-interactively-prepare-data-notebook.md "data-wrangler-interactively-prepare-data-notebook.md")**

Interact with your data, get visualizations, explore actionable insights, and fix
data quality issues.

**[SageMaker Debugger](train-debugger.md "train-debugger.md")**

Inspect training parameters and data throughout the training process. Automatically
detect and alert users to commonly occurring errors such as parameter values getting too
large or small.

**[SageMaker Edge Manager](edge.md "edge.md")**

Optimize custom models for edge devices, create and manage fleets and run models
with an efficient runtime.

**[SageMaker Experiments](experiments.md "experiments.md")**

Experiment management and tracking. You can use the tracked data to reconstruct an
experiment, incrementally build on experiments conducted by peers, and trace model
lineage for compliance and audit verifications.

**[SageMaker Feature Store](feature-store.md "feature-store.md")**

A centralized store for features and associated metadata so features can be easily
discovered and reused. You can create two types of stores, an Online or Offline store.
The Online Store can be used for low latency, real-time inference use cases and the
Offline Store can be used for training and batch inference.

**[SageMaker Ground Truth](sms.md "sms.md")**

High-quality training datasets by using workers along with machine learning to
create labeled datasets.

**[SageMaker Ground Truth Plus](gtp.md "gtp.md")**

A turnkey data labeling feature to create high-quality training datasets without
having to build labeling applications and manage the labeling workforce on your
own.

**[SageMaker Inference Recommender](inference-recommender.md "inference-recommender.md")**

Get recommendations on inference instance types and configurations (e.g. instance
count, container parameters and model optimizations) to use your ML models and
workloads.

**[Inference shadow tests](shadow-tests.md "shadow-tests.md")**

Evaluate any changes to your model-serving infrastructure by comparing its
performance against the currently deployed infrastructure.

**[SageMaker JumpStart](studio-jumpstart.md "studio-jumpstart.md")**

Learn about SageMaker AI features and capabilities through curated 1-click solutions,
example notebooks, and pretrained models that you can deploy. You can also fine-tune the
models and deploy them.

**[SageMaker ML Lineage Tracking](lineage-tracking.md "lineage-tracking.md")**

Track the lineage of machine learning workflows.

**[SageMaker Model Building Pipelines](pipelines.md "pipelines.md")**

Create and manage machine learning pipelines integrated directly with SageMaker AI
jobs.

**[SageMaker Model Cards](model-cards.md "model-cards.md")**

Document information about your ML models in a single place for streamlined
governance and reporting throughout the ML lifecycle.

**[SageMaker Model Dashboard](model-dashboard.md "model-dashboard.md")**

A pre-built, visual overview of all the models in your account. Model Dashboard
integrates information from SageMaker Model Monitor, transform jobs, endpoints, lineage
tracking, and CloudWatch so you can access high-level model information and track model
performance in one unified view.

**[SageMaker Model Monitor](model-monitor.md "model-monitor.md")**

Monitor and analyze models in production (endpoints) to detect data drift and
deviations in model quality.

**[SageMaker Model Registry](model-registry.md "model-registry.md")**

Versioning, artifact and lineage tracking, approval workflow, and cross account
support for deployment of your machine learning models.

**[SageMaker Neo](neo.md "neo.md")**

Train machine learning models once, then run anywhere in the cloud and at the
edge.

**[Notebook-based Workflows](notebook-auto-run.md "notebook-auto-run.md")**

Run your SageMaker Studio notebook as a non-interactive, scheduled job.

**[Preprocessing](processing-job.md "processing-job.md")**

Analyze and preprocess data, tackle feature engineering, and evaluate models.

**[SageMaker Projects](sagemaker-projects.md "sagemaker-projects.md")**

Create end-to-end ML solutions with CI/CD by using SageMaker Projects.

**[Reinforcement Learning](reinforcement-learning.md "reinforcement-learning.md")**

Maximize the long-term reward that an agent receives as a result of its
actions.

**[SageMaker Role Manager](role-manager.md "role-manager.md")**

Administrators can define least-privilege permissions for common ML activities using
custom and preconfigured persona-based IAM roles.

**[SageMaker Serverless Endpoints](serverless-endpoints.md "serverless-endpoints.md")**

A serverless endpoint option for hosting your ML model. Automatically scales in
capacity to serve your endpoint traffic. Removes the need to select instance types or
manage scaling policies on an endpoint.

**[Studio Classic Git extension](studio-git-attach.md "studio-git-attach.md")**

A Git extension to enter the URL of a Git repository, clone it into your
environment, push changes, and view commit history.

**[SageMaker Studio Notebooks](notebooks.md "notebooks.md")**

The next generation of SageMaker notebooks that include AWS IAM Identity Center (IAM Identity Center) integration,
fast start-up times, and single-click sharing.

**[SageMaker Studio Notebooks and
Amazon EMR](studio-notebooks-emr-cluster.md "studio-notebooks-emr-cluster.md")**

Easily discover, connect to, create, terminate and manage Amazon EMR clusters in
single account and cross account configurations directly from SageMaker Studio.

**[SageMaker Training Compiler](training-compiler.md "training-compiler.md")**

Train deep learning models faster on scalable GPU instances managed by SageMaker AI.
