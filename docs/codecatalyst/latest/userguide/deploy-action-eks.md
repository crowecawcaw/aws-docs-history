

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Deploying to Amazon EKS with a workflow
<a name="deploy-action-eks"></a>

**Tip**  
For a tutorial that shows you how to use the **Deploy to Kubernetes cluster ** action, see [Tutorial: Deploy an application to Amazon EKS](deploy-tut-eks.md).

This section describes how to deploy a containerized application into a Kubernetes cluster using a CodeCatalyst workflow. To accomplish this, you must add the **Deploy to Kubernetes cluster** action to your workflow. This action deploys your application to a Kubernetes cluster that you have set up in Amazon Elastic Kubernetes Service (EKS) using one or more Kubernetes manifest files. For a sample manifest, see [deployment.yaml](deploy-tut-eks.md#deploy-tut-eks-source-files-deployment-yml) in [Tutorial: Deploy an application to Amazon EKS](deploy-tut-eks.md).

For more information about Kubernetes, see the [Kubernetes Documentation](https://kubernetes.io/docs/home/).

For more information about Amazon EKS, see [What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) in the *Amazon EKS User Guide*.

**Topics**
+ [How the 'Deploy to Kubernetes cluster' action works](#deploy-action-eks-howitworks)
+ [Runtime image used by the 'Deploy to Amazon EKS' action](#deploy-action-eks-runtime)
+ [Tutorial: Deploy an application to Amazon EKS](deploy-tut-eks.md)
+ [Adding the 'Deploy to Kubernetes cluster' action](deploy-action-eks-adding.md)
+ ['Deploy to Kubernetes cluster' variables](deploy-action-eks-variables.md)
+ ['Deploy to Kubernetes cluster' action YAML](deploy-action-ref-eks.md)

## How the 'Deploy to Kubernetes cluster' action works
<a name="deploy-action-eks-howitworks"></a>

The **Deploy to Kubernetes cluster** works as follows:

1. At runtime, the action installs the Kubernetes `kubectl` utility to the CodeCatalyst compute machine where the action is running. The action configures `kubectl` to point to the Amazon EKS cluster you provided when you configured the action. The `kubectl` utility is necessary to run the `kubectl apply` command, next.

1. The action runs the `kubectl apply -f {{my-manifest.yaml}}` command, which carries out the instructions in {{my-manifest.yaml}} to deploy your application as a set of containers and pods into the configured cluster. For more information on this command, see the [kubectl apply](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) topic in the *Kubernetes Reference Documentation*.

## Runtime image used by the 'Deploy to Amazon EKS' action
<a name="deploy-action-eks-runtime"></a>

The **Deploy to Amazon EKS** action runs on a [November 2022 image](build-images.md#build.previous-image). For more information, see [Active images](build-images.md#build-curated-images).