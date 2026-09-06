

# AWS TNB deployment tasks
<a name="deployment-tasks"></a>

Understand the deployment tasks to effectively monitor deployments and take action faster.

The following table lists the AWS TNB deployment tasks:


| Task name for deployments started before March 7, 2024 | Task name for deployments started on and after March 7, 2024 | Task description | 
| --- | --- | --- | 
| AppInstallation | ClusterPluginInstall | Installs the Multus plugin on the Amazon EKS cluster. | 
| AppUpdate | *no change in name* | Updates the network functions that are already installed in a network instance. | 
| *-* | ClusterPluginUninstall | Uninstalls the plugins on the Amazon EKS cluster. | 
| ClusterStorageClassConfiguration | *no change in name* | Configures the storage class (CSI driver) on an Amazon EKS cluster. | 
| FunctionDeletion | *no change in name* | Deletes network functions from AWS TNB resources. | 
| FunctionInstantiation | FunctionInstall | Deploys network functions using HELM. | 
| FunctionUninstallation | FunctionUninstall | Uninstalls the network function from an Amazon EKS cluster. | 
| HookExecution | *no change in name* | Executes lifecycle hooks as defined in the NSD. | 
| InfrastructureCancellation | *no change in name* | Cancels a network service. | 
| InfrastructureInstantation | *no change in name* | Provisions AWS resources on behalf of the user. | 
| InfrastructureTermination | *no change in name* | Deprovisions AWS resources invoked through AWS TNB. | 
| *-* | InfrastructureUpdate | Updates the AWS resources provisioned on behalf of the user. | 
| InventoryDeregistration | *no change in name* | Deregisters AWS resources from AWS TNB. | 
| *-* | InventoryRegistration | Registers the AWS resources in AWS TNB. | 
| KubernetesClusterConfiguration | ClusterConfiguration | Configures the Kubernetes cluster and adds additional IAM roles to the Amazon EKS AuthMap as defined in the NSD. | 
| NetworkServiceFinalization | *no change in name* | Finalizes the network service and provides a success or failure status update. | 
| NetworkServiceInstantiation | *no change in name* | Initializes the network service. | 
| SelfManagedNodesConfiguration | *no change in name* | Bootstraps self-managed nodes with Amazon EKS and Kubernetes control plane. | 
| *-* | ValidateNetworkServiceUpdate | Runs the validations before updating a network instance. | 