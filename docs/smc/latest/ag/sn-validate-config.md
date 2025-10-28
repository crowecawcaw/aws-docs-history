# Validating AWS Config integration in

ServiceNow

To see AWS Config details, configure the service settings to record data for the
resource types of interest. For more information, see [Setting Up AWS Config with the
Console](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md").

###### To view configuration item details from AWS Config in the ServiceNow CMDB

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulfiller view (Standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. Choose **AWS Config**. Select and view the relationships for
   available AWS resources.
   This table illustrates the available AWS resources, ServiceNow CMDB
   label, and table name.

| AWS resources (AWS Config)              | ServiceNow CMDB/Scoped App Table Label | ServiceNow CMDB/Scoped App Table Name                 |
| --------------------------------------- | -------------------------------------- | ----------------------------------------------------- |
| Accounts                                | CMDB CI Cloud Service Accounts         | `cmdb_ci_cloud_service_account`                       |
| VPCs                                    | Cloud Networks                         | `cmdb_ci_network`                                     |
| Availability Zones                      | Availability Zone                      | `cmdb_ci_availability_zone`                           |
| EC2 Instances                           | Virtual Machine Instance               | `cmdb_ci_vm_instance`                                 |
| EBS Volumes                             | Storage Volume                         | `cmdb_ci_storage_volume`                              |
| Security Groups                         | Compute Security Group                 | `cmdb_ci_compute_security_group`                      |
| Auto Scaling Group                      | Auto Scaling Groups                    | `x_126749_aws_sc_cmdb_ci_autoscaling_group`           |
| Network Interfaces                      | Cloud Mgmt Network Interface           | `cmdb_ci_nic`                                         |
| RDS Instances                           | Cloud DataBase                         | `cmdb_ci_cloud_database`                              |
| Subnets                                 | Cloud Subnet                           | `cmdb_ci_cloud_subnet`                                |
| Load Balancers (V2)                     | Cloud Load Balancer                    | `cmdb_ci_cloud_load_balancer`                         |
| S3 Buckets                              | Cloud Object Storages                  | `cmdb_ci_cloud_object_storage`                        |
| CloudFormation Stacks                   | CloudFormation Stack                   | `x_126749_aws_sc_cmdb_ci_cloudformation_stack`        |
| CloudFormation Provisioned Products     | CloudFormation Provisioned Product     | `x_126749_aws_sc_cmdb_ci_config_pp`                   |
| Tags                                    | Key Value                              | `cmdb_key_value`                                      |
| Lambdas                                 | Cloud Function                         | `cmdb_ci_cloud_function`                              |
| Dynamo DB                               | DynamoDB Table                         | `cmdb_ci_dynamodb_table`                              |
| OS images                               | Images                                 | `cmdb_ci_os_template`                                 |
| AppRegistry Applications                | AppRegistry Application                | `x_126749_aws_sc_cmdb_ci_appregistry_application`     |
| AppRegistry Attribute Groups            | AppRegistry Attribute Group            | `x_126749_aws_sc_cmdb_ci_appregistry_attribute_group` |
| AppRegistry Resources                   | AppRegistryResource                    | `x_126749_aws_sc_cmdb_ci_appregistry_resource`        |
| RDS Cluster                             | Cloud Database Clusters                | `cmdb_ci_cloud_db_cluster`                            |
| API Gateway                             | Cloud Gateways                         | `cmdb_ci_cloud_gateway`                               |
| Amazon Workspaces                       | Virtual Desktop                        | `cmdb_ci_virtual_desktop`                             |
| Amazon Elastic Container Service (ECS)  | AWS Cloud ECS Cluster                  | `cmdb_ci_cloud_ecs_cluster`                           |
| Amazon Elastic Kubernetes Service (EKS) | Kubernetes Cluster                     | `cmdb_ci_kubernetes_cluster`                          |
| Amazon Elastic File System (EFS)        | File System                            | `cmdb_ci_file_service`                                |
