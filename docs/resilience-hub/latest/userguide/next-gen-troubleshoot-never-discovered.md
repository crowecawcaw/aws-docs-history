# Resource types never discovered

Next generation Resilience Hub never stores the following resource types during discovery. These resource types include auxiliary infrastructure, point-in-time backups, and
operational tooling with no bearing on resilience analysis.

| Resource type                                 |
| --------------------------------------------- |
| `AWS::EC2::EIP`                               |
| `AWS::EC2::Volume`                            |
| `AWS::EC2::Snapshot`                          |
| `AWS::FSx::Snapshot`                          |
| `AWS::Lightsail::DiskSnapshot`                |
| `AWS::RDS::DBSnapshot`                        |
| `AWS::RDS::DBClusterSnapshot`                 |
| `AWS::EC2::FlowLog`                           |
| `AWS::CloudWatch::Dashboard`                  |
| `AWS::Logs::LogGroup`                         |
| `AWS::Logs::MetricFilter`                     |
| `AWS::SSM::ResourceDataSync`                  |
| `AWS::RDS::DBParameterGroup`                  |
| `AWS::RDS::DBClusterParameterGroup`           |
| `AWS::ElastiCache::ParameterGroup`            |
| `AWS::RDS::DBSubnetGroup`                     |
| `AWS::ElastiCache::SubnetGroup`               |
| `AWS::EC2::SubnetNetworkAclAssociation`       |
| `AWS::EC2::VPCGatewayAttachment`              |
| `AWS::CloudFormation::Stack`                  |
| `AWS::CloudFormation::WaitConditionHandle`    |
| `AWS::CodeDeploy::DeploymentGroup`            |
| `AWS::KMS::Alias`                             |
| `AWS::SecretsManager::SecretTargetAttachment` |
| `AWS::CloudFormation::CustomResource`         |
