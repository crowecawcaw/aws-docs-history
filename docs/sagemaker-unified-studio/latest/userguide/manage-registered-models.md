# Manage Registered Models

Your registered models can be accessed and managed in Amazon SageMaker Unified Studio.

1. Navigate to **AI/ML** > **Models** and
   select the **Registered Models** tab to view the
   models.
2. You can review the following information
   - Model group name - Logical grouping for related model
     versions
   - Model version - Specific version identifier
   - Model artifacts - Location of model files in Amazon S3
   - Description - Optional description of the model and its
     purpose

3. Select specific models to review key model information like
   - Framework - Machine learning framework used (e.g., PyTorch,
     TensorFlow)
   - Algorithm - Algorithm or approach used for training
   - Performance metrics - Accuracy, precision, recall, or other
     relevant metrics

## Model lifecycle management

The model registry provides version control and lifecycle management:

- Version tracking - Each model registration creates a new version with
  unique metadata
- Approval workflows - Models can have approval status (Approved,
  Pending, Rejected)
- Deployment status - Track which versions are deployed to
  endpoints
- Model comparison - Compare metrics and metadata across versions

To manage model versions:

1. Choose a model group name to view all versions.
2. Review version details including:
   - Version number - Sequential version identifier
   - Description - Version-specific notes and changes
   - Deployment Status - Current deployment state
   - Approval Status - Workflow approval state
   - Modified Date - Last update timestamp

3. Use the **Actions** dropdown to:
   - Deploy using Notebooks - Use a pre-created notebook to deploy
     the model to SageMaker AI Endpoint
   - Deploy using Jupyter Notebook - Use a pre-created JupyterLab
     notebook to deploy the model to SageMaker AI Endpoint
   - Approve/Reject - Update approval status
   - Delete - Delete the selected version
