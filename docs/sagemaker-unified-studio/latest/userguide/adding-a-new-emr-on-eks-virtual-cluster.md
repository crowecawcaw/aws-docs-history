# Adding a new Amazon EMR on EKS virtual cluster in Amazon SageMaker Unified Studio

As a data worker, you can make use of Amazon EMR on EKS by adding new Amazon EMR on EKS virtual clusters
as compute instances to a Amazon SageMaker Unified Studio project. However, in order to create new Amazon EMR on EKS virtual clusters,
your admin must enable and configure blueprints.

After your admin has enabled and configured blueprints:

1. From inside the project management view, select **Compute** from the navigation bar.
2. In the Compute panel, select the **Data processing** tab.
3. To create a new Amazon EMR on EKS virtual cluster, select the **Add compute**
   dropdown menu and then choose **New compute**.
4. In the **Add compute** modal, you can select the type of compute you would like to add to your project.
   Select **Create new compute resources**.
5. Select **Amazon EMR on EKS virtual cluster**.
6. The **Add compute** dialog box allows you to select your admin created Amazon EKS cluster configuration,
   specify the name of the Amazon EMR on EKS virtual cluster, provide a description,
   and choose a release of Amazon EMR (such as EMR 7.11.0-latest) that you want to install on your managed endpoint.
7. After configuring these settings, select **Add compute**.
   After some time, your Amazon EMR on EKS virtual cluster will be added to your project.
