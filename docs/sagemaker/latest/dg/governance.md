# Model governance to manage permissions and track model performance

Model governance is a framework that gives systematic visibility into machine learning
(ML) model development, validation, and usage. Amazon SageMaker AI provides purpose-built ML governance
tools for managing control access, activity tracking, and reporting across the ML
lifecycle.

Manage least-privilege permissions for ML practitioners using Amazon SageMaker Role Manager, create detailed
model documentation using Amazon SageMaker Model Cards, and gain visibility into your models with centralized
dashboards using Amazon SageMaker Model Dashboard.

## Amazon SageMaker Role Manager

With Amazon SageMaker Role Manager, administrators can define user permissions with least-privilege
permissions for common machine learning activities. Use Amazon SageMaker Role Manager to build and manage
persona-based IAM roles specific to your business needs.

For more information, see [Amazon SageMaker Role Manager](role-manager.md "role-manager.md").

## Amazon SageMaker Model Cards

Use Amazon SageMaker Model Cards to document, retrieve, and share essential model information from
conception to deployment. With model cards, model risk managers, data scientists, and ML
engineers can create an immutable record of intended model uses, risk ratings, training
details, evaluation results, and more.

For more information, see [Amazon SageMaker Model Cards](model-cards.md "model-cards.md").

## Amazon SageMaker Model Dashboard

Amazon SageMaker Model Dashboard is a pre-built, visual overview of all the models in your account. SageMaker Model Dashboard
integrates valuable information from Amazon SageMaker Model Monitor, Transform Jobs, Endpoints,
ML Lineage Tracking and Amazon CloudWatch so you can access high-level model information and
track model performance in one unified view.

For more information, see [Amazon SageMaker Model Dashboard](model-dashboard.md "model-dashboard.md").

## Amazon SageMaker Assets

Amazon SageMaker Assets is a new workflow that streamlines ML governance. It allows
users to easily publish, share, and subscribe to ML assets and data assets, such as
feature groups and Amazon Redshift tables.

Administrators use Amazon DataZone to set up the databases and the ML infrastructure
for users to share assets within Amazon SageMaker Studio. After set up, users can seamlessly
share assets with each other without additional administrator overhead. For more information about Amazon SageMaker Assets, see [Controlled access to assets with Amazon SageMaker Assets](sm-assets.md "sm-assets.md").
