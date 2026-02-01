# SQL Server setup

Perform these steps in your SQL Server environment to enable AWS Transform modernization.

## Database setup and configuration

### Step 1: Create database user with required permissions

Create a dedicated database user for AWS Transform with the necessary permissions. If you already have a DMS Schema Conversion user, you can reuse it.

Connect to your SQL Server instance and run the following commands:

```
-- Create the login in master database
USE master;
CREATE LOGIN [atx_user] WITH PASSWORD = 'YourStrongPassword123!';

-- Switch to your application database
USE [YourDatabaseName];
CREATE USER [atx_user] FOR LOGIN [atx_user];

-- Grant required permissions
GRANT VIEW DEFINITION TO [atx_user];
GRANT VIEW DATABASE STATE TO [atx_user];
ALTER ROLE [db_datareader] ADD MEMBER [atx_user];

-- Grant master database permissions
USE master;
GRANT VIEW SERVER STATE TO [atx_user];
GRANT VIEW ANY DEFINITION TO [atx_user];
```

###### Note

Repeat the database-specific commands (USE, CREATE USER, GRANT) for each database you want to modernize.

The db_datareader role is only necessary for data migration, not for schema conversion alone.

- The db_datareader role grants read access to all tables in the database
- This role is required ONLY when performing data migration.
- For schema conversion only (without data migration), the db_datareader role is NOT required
- The other permissions (VIEW DEFINITION, VIEW DATABASE STATE, etc.) are sufficient for schema conversion

### Step 2: Store credentials in AWS Secrets Manager

Store your database credentials securely in AWS Secrets Manager. Skip this step if you already have a secret created for DMS.

1. Navigate to AWS Secrets Manager in the console
2. Choose **Store a new secret**
3. Configure the secret:
   - **Secret type:** Credentials for other database
   - **Database**: Microsoft SQL Server
   - **Username**: atx_user (or your chosen username)
   - **Password**: The password you created
   - **Server name**: Your SQL Server endpoint
   - **Database name**: Your database name
   - **Port**: 1433 (or your custom port)

4. Choose **Next**
5. Enter secret name: atx-db-modernization-sqlserver
6. Add required tags (these tags are mandatory):
   - Key: Project, Value: atx-db-modernization
   - Key: Owner, Value: database-connector

7. Choose **Next** through remaining screens
8. Choose **Store**
9. Note the Secret ARN for use in the next step

###### Important

Database passwords must use printable ASCII characters only, excluding '/', '@', '"', and spaces. Secrets scheduled for deletion can cause transformation failures.

### Step 3: Create required DMS roles

AWS Transform requires specific IAM roles for DMS operations. Deploy these roles using the CloudFormation template below.

###### Note

If your AWS account already has existing DMS-related roles, modify this template to reuse those resources rather than creating duplicates.

Create a file named dms-roles.yaml with the following content:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: 'DMS Service Roles for AWS Transform SQL Server Modernization'

Resources:
  DMSCloudWatchLogsRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: dms-cloudwatch-logs-role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - dms.amazonaws.com
                - schema-conversion.dms.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole

  DMSS3AccessRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: dms-s3-access-role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - dms.amazonaws.com
                - schema-conversion.dms.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: S3TaggedAccess
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetBucketLocation
                  - s3:GetBucketVersioning
                  - s3:PutObject
                  - s3:PutBucketVersioning
                  - s3:GetObject
                  - s3:GetObjectVersion
                  - s3:ListBucket
                  - s3:DeleteObject
                Resource: arn:aws:s3:::atx-db-modernization-*
                Condition:
                  StringEquals:
                    aws:ResourceAccount: !Ref AWS::AccountId

  DMSSecretsManagerRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: dms-secrets-manager-role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - dms.amazonaws.com
                - schema-conversion.dms.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: SecretsManagerTaggedAccess
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - secretsmanager:GetSecretValue
                  - secretsmanager:DescribeSecret
                Resource: '*'
                Condition:
                  StringEquals:
                    secretsmanager:ResourceTag/Project: atx-db-modernization
                    secretsmanager:ResourceTag/Owner: database-connector

  DMSVPCRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: dms-vpc-role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - dms.amazonaws.com
                - schema-conversion.dms.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole

Outputs:
  DMSCloudWatchLogsRoleArn:
    Description: ARN of the DMS CloudWatch Logs Role
    Value: !GetAtt DMSCloudWatchLogsRole.Arn
  DMSS3AccessRoleArn:
    Description: ARN of the DMS S3 Access Role
    Value: !GetAtt DMSS3AccessRole.Arn
  DMSSecretsManagerRoleArn:
    Description: ARN of the DMS Secrets Manager Role
    Value: !GetAtt DMSSecretsManagerRole.Arn
  DMSVPCRoleArn:
    Description: ARN of the DMS VPC Role
    Value: !GetAtt DMSVPCRole.Arn
```

Deploy the CloudFormation stack using AWS CLI:

```
aws cloudformation create-stack \
  --stack-name dms-roles \
  --template-body file://dms-roles.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --region us-east-1
```

Or deploy using the AWS Console:

1. Navigate to CloudFormation in the AWS Console
2. Choose **Create stack**
3. Select **Upload a template file**
4. Upload the dms-roles.yaml file
5. Enter stack name: dms-roles
6. Acknowledge IAM capabilities
7. Choose **Create stack**

### Step 4: Configure network security

Ensure proper network connectivity between AWS Transform, your SQL Server database, and other AWS services.

#### Security group configuration (recommended approach)

**Recommended Approach:** Use security group-based access control rather than IP-based rules. This provides better security, easier management, and works seamlessly with AWS Transform's architecture.

**Why Security Group-Based Access Control?**

- DMS Schema Conversion creates Elastic Network Interfaces (ENIs) within your VPC
- Your databases do not need to be publicly accessible
- AWS Transform does not expose private IP addresses, making IP-based rules complex
- Security group references provide dynamic, automatic updates as resources scale

##### Configure your SQL Server security group

When you configure the DMS Schema Conversion Instance Profile in AWS Transform, you specify a Security Group for the DMS SC instance. Your database security group should allow inbound traffic from this DMS SC security group.

Step-by-step configuration:

1. Identify the DMS Schema Conversion Security Group:
   - This is specified when creating the Instance Profile in AWS Transform
   - Note the Security Group ID (e.g., sg-0123456789abcdef0)

2. Update your SQL Server Security Group inbound rules:
   - **Type**: Custom TCP
   - **Port**: 1433 (or your custom SQL Server port)
   - **Source**: The DMS Schema Conversion Security Group ID
   - **Description**: "Allow DMS Schema Conversion access"

3. For Aurora PostgreSQL target (after creation):
   - **Type**: PostgreSQL
   - **Port**: 5432 (or your custom PostgreSQL port)
   - **Source**: The DMS Schema Conversion Security Group ID
   - **Description**: "Allow DMS Schema Conversion access"

###### Important

**Important for Least Privileged Security Models:** If your organization uses a "least privileged" security model that blocks all traffic by default, you must explicitly allow inbound traffic from the DMS Schema Conversion Security Group to your database port. Do not open port 1433 to all sources or IP ranges.

#### Required AWS service connectivity

Ensure your VPC can communicate with:

- AWS Transform service endpoints
- AWS DMS endpoints
- Aurora PostgreSQL endpoints
- S3 endpoints for artifact storage
- AWS Secrets Manager endpoints
- AWS CodeConnections endpoints

**VPC Endpoints:** For private networks, configure VPC endpoints for required AWS services to avoid internet gateway dependencies.
