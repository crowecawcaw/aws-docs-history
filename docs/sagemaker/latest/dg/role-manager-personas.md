# Persona reference

Amazon SageMaker Role Manager provides suggested permissions for a number of ML personas. These include
user execution roles for common ML practitioner responsibilities as well as service
execution roles for common AWS service interactions needed to work with SageMaker AI.

Each persona has suggested permissions in the form of selected ML activities. For
information on predefined ML activities and their permissions, see [ML activity reference](role-manager-ml-activities.md "role-manager-ml-activities.md").

## Data scientist

persona

Use this persona to configure permissions to perform general machine learning
development and experimentation in a SageMaker AI environment. This persona includes the
following preselected ML activities:

- Run Studio Classic Applications
- Manage ML Jobs
- Manage Models
- Manage AWS Glue Tables
- Canvas AI Services
- Canvas MLOps
- Canvas Kendra Access
- Use MLflow
- Access required to AWS Services for MLflow
- Run Studio EMR Serverless Applications

## MLOps persona

Choose this persona to configure permissions for operational activities. This
persona includes the following preselected ML activities:

- Run Studio Classic Applications
- Manage Models
- Manage Pipelines
- Search and visualize experiments
- Amazon S3 Full Access

## SageMaker AI compute persona

###### Note

We recommend that you first use the role manager to create a SageMaker AI Compute Role
so that SageMaker AI compute resources can perform tasks such as training and inference.
Use the SageMaker AI Compute Role persona to create this role with the role manager.
After creating a SageMaker AI Compute Role, take note of its ARN for future use.

This persona includes the following preselected ML activity:

- Access Required AWS Services
