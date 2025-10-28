# AWS TNB deployment tasks

Understand the deployment tasks to effectively monitor deployments and take action
faster.

The following table lists the AWS TNB deployment tasks:

| Task name for deployments started before March 7, 2024 | Task name for deployments started on and after March 7, 2024 | Task description                                                                                                 |
| ------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| AppInstallation                                        | ClusterPluginInstall                                         | Installs the Multus plugin on the Amazon EKS cluster.                                                            |
| AppUpdate                                              | _no change in name_                                          | Updates the network functions that are already installed in a network instance.                                  |
| _-_                                                    | ClusterPluginUninstall                                       | Uninstalls the plugins on the Amazon EKS cluster.                                                                |
| ClusterStorageClassConfiguration                       | _no change in name_                                          | Configures the storage class (CSI driver) on an Amazon EKS cluster.                                              |
| FunctionDeletion                                       | _no change in name_                                          | Deletes network functions from AWS TNB resources.                                                                |
| FunctionInstantiation                                  | FunctionInstall                                              | Deploys network functions using HELM.                                                                            |
| FunctionUninstallation                                 | FunctionUninstall                                            | Uninstalls the network function from an Amazon EKS cluster.                                                      |
| HookExecution                                          | _no change in name_                                          | Executes lifecycle hooks as defined in the NSD.                                                                  |
| InfrastructureCancellation                             | _no change in name_                                          | Cancels a network service.                                                                                       |
| InfrastructureInstantation                             | _no change in name_                                          | Provisions AWS resources on behalf of the user.                                                                  |
| InfrastructureTermination                              | _no change in name_                                          | Deprovisions AWS resources invoked through AWS TNB.                                                              |
| _-_                                                    | InfrastructureUpdate                                         | Updates the AWS resources provisioned on behalf of the user.                                                     |
| InventoryDeregistration                                | _no change in name_                                          | Deregisters AWS resources from AWS TNB.                                                                          |
| _-_                                                    | InventoryRegistration                                        | Registers the AWS resources in AWS TNB.                                                                          |
| KubernetesClusterConfiguration                         | ClusterConfiguration                                         | Configures the Kubernetes cluster and adds additional IAM roles to the Amazon EKS AuthMap as defined in the NSD. |
| NetworkServiceFinalization                             | _no change in name_                                          | Finalizes the network service and provides a success or failure status update.                                   |
| NetworkServiceInstantiation                            | _no change in name_                                          | Initializes the network service.                                                                                 |
| SelfManagedNodesConfiguration                          | _no change in name_                                          | Bootstraps self-managed nodes with Amazon EKS and Kubernetes control plane.                                      |
| _-_                                                    | ValidateNetworkServiceUpdate                                 | Runs the validations before updating a network instance.                                                         |
