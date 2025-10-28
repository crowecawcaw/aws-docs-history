Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding the 'Deploy to Kubernetes cluster' action

Use the following instructions to add the **Deploy to Kubernetes cluster**
action to your workflow.

**Before you begin**

Before you add the **Deploy to Kubernetes cluster** action to your workflow,
you must have the following prepared:

###### Tip

To set up these prerequisites quickly, follow the instructions in [Tutorial: Deploy an application to Amazon EKS](deploy-tut-eks.md "deploy-tut-eks.md").

- A Kubernetes cluster in Amazon EKS. For information about clusters, see [Amazon EKS clusters](../../../eks/latest/userguide/clusters.md "../../../eks/latest/userguide/clusters.md") in
  the **Amazon EKS User Guide**.
- At least one Dockerfile that describes how to assemble your application into a Docker
  image. For more information about Dockerfiles, see the [Dockerfile
  reference](https://docs.docker.com/engine/reference/builder/ "https://docs.docker.com/engine/reference/builder/").
- At least one Kubernetes manifest file, which is called a _configuration
  file_ or _configuration_ in the Kubernetes documentation. For
  more information, see [Managing resources](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/ "https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/") in the Kubernetes documentation.
- An IAM role that gives the **Deploy to Kubernetes cluster** action the
  ability to access and interact with your Amazon EKS cluster. For more information, see the
  [Role](deploy-action-ref-eks.md#deploy.action.eks.environment.connections.role "deploy-action-ref-eks.md#deploy.action.eks.environment.connections.role") topic in the ['Deploy to Kubernetes cluster' action YAML](deploy-action-ref-eks.md "deploy-action-ref-eks.md").

After creating this role, you must add it to:

    + Your Kubernetes ConfigMap file. To learn how to add a role to a ConfigMap file, see
     [Enabling
     IAM principal access to your cluster](../../../eks/latest/userguide/add-user-role.md "../../../eks/latest/userguide/add-user-role.md") in the
     **Amazon EKS User Guide**.
    + CodeCatalyst. To learn how to add an IAM role to CodeCatalyst, see [Adding IAM roles to account
     connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

- A CodeCatalyst space, project, and environment. The space and environment must both be
  connected to the AWS account into which you will be deploying your application. For more
  information, see [Creating a space](spaces-create.md "spaces-create.md"), [Creating an empty project in Amazon CodeCatalyst](projects-create.md#projects-create-empty "projects-create.md#projects-create-empty"), and [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md").
- A source repository supported by CodeCatalyst. The repository stores your application source
  files, Dockerfiles, and Kubernetes manifests. For more information, see [Store and collaborate on code with source repositories in CodeCatalyst](source.md "source.md").

Visual

###### To add the 'Deploy to Kubernetes cluster' action using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. At the top-left, choose **+ Actions** to open the action
   catalog.
8. From the drop-down list, choose **Amazon CodeCatalyst**.
9. Search for the **Deploy to Kubernetes cluster** action, and do one of
   the following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose **Deploy to Kubernetes cluster**. The action details
     dialog box appears. On this dialog box:
     - (Optional) Choose **Download** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. In the **Inputs** and **Configuration** tabs,
    complete the fields according to your needs. For a description of each field, see
    the ['Deploy to Kubernetes cluster' action YAML](deploy-action-ref-eks.md "deploy-action-ref-eks.md").
    This reference provides detailed information about each field (and corresponding
    YAML property value) as it appears in both the YAML and visual editors.
11. (Optional) Choose **Validate** to validate the workflow's YAML
    code before committing.
12. Choose **Commit**, enter a commit message, and choose
    **Commit** again.

YAML

###### To add the 'Deploy to Kubernetes cluster' action using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. At the top-left, choose **+ Actions** to open the action
   catalog.
8. From the drop-down list, choose **Amazon CodeCatalyst**.
9. Search for the **Deploy to Kubernetes cluster** action, and do one of
   the following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose **Deploy to Kubernetes cluster**. The action details
     dialog box appears. On this dialog box:
     - (Optional) Choose **Download** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. Modify the properties in the YAML code according to your needs. An explanation
    of each available property is provided in the ['Deploy to Kubernetes cluster' action YAML](deploy-action-ref-eks.md "deploy-action-ref-eks.md").
11. (Optional) Choose **Validate** to validate the workflow's YAML
    code before committing.
12. Choose **Commit**, enter a commit message, and choose
    **Commit** again.
