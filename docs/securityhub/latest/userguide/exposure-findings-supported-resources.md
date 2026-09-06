

# Supported resource types for exposure findings in Security Hub
<a name="exposure-findings-supported-resources"></a>

 AWS Security Hub generates exposure findings for the following types of AWS resources: 
+ `AWS::DynamoDB::Table`
+ `AWS::EC2::Instance`
+ `AWS::ECS::Service`
+ `AWS::EKS::Cluster`
+ `AWS::IAM::User`
+ `AWS::Lambda::Function`
+ `AWS::RDS::DBInstance`
+ `AWS::S3::Bucket`
+ `AWS::SageMaker::NotebookInstance`

If you have an Azure connector, Security Hub also generates exposure findings for the following types of Azure resources:
+ `microsoft.app/containerapps`
+ `microsoft.compute/virtualmachines`
+ `microsoft.containerservice/managedclusters`
+ `microsoft.documentdb/databaseaccounts`
+ `microsoft.graph/user`
+ `microsoft.sql/servers/databases`
+ `microsoft.storage/storageaccounts/blobservices/containers`
+ `microsoft.web/sites`

Security Hub generates one exposure finding per primary resource. If a resource does not have any exposure traits or has insufficient traits, Security Hub does not generate an exposure finding for that resource. 