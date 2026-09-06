

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Config integration in ServiceNow
<a name="sn-validate-config"></a>

To see AWS Config details, configure the service settings to record data for the resource types of interest. For more information, see [Setting Up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html).

**To view configuration item details from AWS Config in the ServiceNow CMDB**

1.  Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulfiller view (Standard user interface view). 

1.  In the navigator, enter **AWS Service Management**. 

1.  Choose **AWS Config**. Select and view the relationships for available AWS resources. 

This table illustrates the available AWS resources, ServiceNow CMDB label, and table name.


| AWS resources (AWS Config) | ServiceNow CMDB/Scoped App Table Label | ServiceNow CMDB/Scoped App Table Name | 
| --- | --- | --- | 
| Accounts | CMDB CI Cloud Service Accounts | cmdb\_ci\_cloud\_service\_account | 
| VPCs | Cloud Networks  | cmdb\_ci\_network | 
| Availability Zones | Availability Zone | cmdb\_ci\_availability\_zone | 
| EC2 Instances | Virtual Machine Instance | cmdb\_ci\_vm\_instance | 
| EBS Volumes | Storage Volume | cmdb\_ci\_storage\_volume | 
| Security Groups | Compute Security Group | cmdb\_ci\_compute\_security\_group | 
| Auto Scaling Group | Auto Scaling Groups | x\_126749\_aws\_sc\_cmdb\_ci\_autoscaling\_group | 
| Network Interfaces | Cloud Mgmt Network Interface | cmdb\_ci\_nic | 
| RDS Instances | Cloud DataBase | cmdb\_ci\_cloud\_database | 
| Subnets | Cloud Subnet | cmdb\_ci\_cloud\_subnet | 
| Load Balancers (V2) | Cloud Load Balancer  | cmdb\_ci\_cloud\_load\_balancer | 
| S3 Buckets | Cloud Object Storages | cmdb\_ci\_cloud\_object\_storage | 
| CloudFormation Stacks | CloudFormation Stack | x\_126749\_aws\_sc\_cmdb\_ci\_cloudformation\_stack | 
| CloudFormation Provisioned Products | CloudFormation Provisioned Product | x\_126749\_aws\_sc\_cmdb\_ci\_config\_pp | 
| Tags | Key Value | cmdb\_key\_value | 
| Lambdas | Cloud Function | cmdb\_ci\_cloud\_function | 
| Dynamo DB | DynamoDB Table | cmdb\_ci\_dynamodb\_table | 
| OS images | Images | cmdb\_ci\_os\_template | 
| AppRegistry Applications | AppRegistry Application | x\_126749\_aws\_sc\_cmdb\_ci\_appregistry\_application | 
| AppRegistry Attribute Groups | AppRegistry Attribute Group | x\_126749\_aws\_sc\_cmdb\_ci\_appregistry\_attribute\_group  | 
| AppRegistry Resources | AppRegistryResource | x\_126749\_aws\_sc\_cmdb\_ci\_appregistry\_resource  | 
| RDS Cluster | Cloud Database Clusters |  cmdb\_ci\_cloud\_db\_cluster  | 
| API Gateway  | Cloud Gateways | cmdb\_ci\_cloud\_gateway  | 
| Amazon Workspaces | Virtual Desktop | cmdb\_ci\_virtual\_desktop  | 
| Amazon Elastic Container Service (ECS) | AWS Cloud ECS Cluster | cmdb\_ci\_cloud\_ecs\_cluster  | 
| Amazon Elastic Kubernetes Service (EKS) | Kubernetes Cluster | cmdb\_ci\_kubernetes\_cluster  | 
| Amazon Elastic File System (EFS) | File System | cmdb\_ci\_file\_service  | 