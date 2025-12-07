# Supported resource types for

exposure findings in Security Hub

AWS Security Hub generates exposure findings for the following types of AWS resources:

- `AWS::DynamoDB::Table`
- `AWS::EC2::Instance`
- `AWS::ECS::Service`
- `AWS::EKS::Cluster`
- `AWS::IAM::User`
- `AWS::Lambda::Function`
- `AWS::RDS::DBInstance`
- `AWS::S3::Bucket`
  Security Hub generates one exposure finding per primary resource. If a resource doesn't have any
  exposure traits or has insufficient traits, Security Hub doesn't generate an exposure
  finding for that resource.
