# Use MLFlow to create and track

experiments

To get started, you should have an existing MLFlow server created in SageMaker AI
Studio. Make sure that you have the ARN to get started.

1. From your project's main page, choose **MLflow** from the
   left navigation menu.
2. Select the **MLflow** tab to view MLflow tracking
   servers.
3. Connect to an existing MLFlow Tracking Server. Note that you can’t create
   a new MLFlow Server in Amazon SageMaker Unified Studio. You have to create this using SageMaker AI
   APIs or in SageMaker AI Studio.
   1. Choose **Connect Tracking Server**
   2. Enter a Tracking Server Name
   3. Provide a Connection name for identification
   4. Enter the MLflow Tracking Server ARN for your project
   5. Choose **Connect to server**

4. Once connected, choose **Open MLflow** to launch the
   MLflow UI.
5. In the MLflow interface, view your experiments:
   - Experiments tab shows all tracked experiments
   - Models tab displays registered model versions
   - Prompts tab contains prompt templates and versions

6. You can perform additional actions such as
   - Stop ML Server
   - User server to train model – this will launch a sample notebook
     which will provide instructions on how to use MLFlow to train a
     linear regression model
   - Edit the connection with new ARNs
   - Delete the connection
