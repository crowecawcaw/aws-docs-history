

# Custom blueprints as Tooling
<a name="tooling-custom-blueprints"></a>

In Amazon SageMaker Unified Studio, the managed Tooling blueprint provisions a fixed set of resources for every project. When your organization requires a different foundation, you can use a custom blueprint as a project's Tooling environment instead. Assign the `TOOLING` category when you create a custom blueprint, or update an existing custom blueprint to comply with the minimum Tooling requirements in [Template requirements](#tooling-template-requirements). Amazon SageMaker Unified Studio accepts custom blueprints categorized as `TOOLING` as the first environment deployed in a project profile.

For information that applies to all custom blueprints, including the reserved parameters that Amazon SageMaker Unified Studio populates and the trust policy that the provisioning role requires, see [Custom blueprints](custom-blueprint.md).

**Topics**
+ [Template requirements](#tooling-template-requirements)
+ [Minimum Tooling template](#tooling-minimum-template)
+ [Usage](#tooling-usage)

## Template requirements
<a name="tooling-template-requirements"></a>

When a blueprint is categorized as `TOOLING`, Amazon SageMaker Unified Studio validates your template by calling `cloudformation:GetTemplateSummary`. The summary of your template must adhere to the minimum Tooling requirements captured in this section, including required AWS CloudFormation parameters, required AWS CloudFormation resources, and required AWS CloudFormation exports.

### Parameters
<a name="tooling-template-parameters"></a>

Amazon SageMaker Unified Studio requires your template to declare the following three parameters so that it can supply their values at deployment time.

`datazoneEnvironmentDomainId`  
The domain ID.

`datazoneEnvironmentEnvironmentId`  
The environment ID.

`datazoneEnvironmentProjectId`  
The project ID.

### Resources
<a name="tooling-template-resources"></a>

`DefaultIAMConnection`  
The IAM connection that tools use to authenticate. Its name determines which project experience your users see. For more information about project permission sets, see [Tooling blueprints in Amazon SageMaker Unified Studio](tooling.md).

`DefaultS3Connection`  
The project's primary Amazon S3 connection.

`DefaultS3SharedConnection`  
The project's shared Amazon S3 connection, at the `/shared/` prefix of project storage.

### Exports
<a name="tooling-template-exports"></a>

`s3BucketArn`  
The ARN of the project's Amazon S3 bucket. A key prefix after the bucket name is allowed.

`s3BucketPath`  
The `s3://` URI that other environments in the project resolve their own paths against. A trailing forward slash is optional.

Suffix each export name with the project ID and the scope name, which keeps the name unique within an AWS account and AWS Region and matches the name that other blueprints import. Declare `datazoneScopeName` with a default of `dev`.

```
Outputs:
  S3BucketArn:
    Value: !Sub '${ProjectBucket.Arn}/'
    Export:
      Name: !Sub 's3BucketArn-${datazoneEnvironmentProjectId}-${datazoneScopeName}'
  S3BucketPath:
    Value: !Sub 's3://${ProjectBucket}/shared'
    Export:
      Name: !Sub 's3BucketPath-${datazoneEnvironmentProjectId}-${datazoneScopeName}'
```

**Important**  
The AWS CloudFormation export `userRoleArn` is not allowed. Amazon SageMaker Unified Studio resolves the project role itself, from the `RoleArn` you bind on the IAM connection, and rejects a template that exports the role again.

## Minimum Tooling template
<a name="tooling-minimum-template"></a>

Use one of the templates below to create a minimum Tooling template. Choose the template that matches your domain type, and add capabilities from [Tooling capabilities](tooling-capabilities.md).

**Note**  
The name of the default IAM connection sets the project's experience. The name must match the permission set that project members authenticate with: `default.iam` for IAM permissions, or `project.iam` for IAM Identity Center permissions. No other name is accepted. For more information about project permission sets, see [Tooling blueprints in Amazon SageMaker Unified Studio](tooling.md).

The `CreateEnvironmentBlueprint` API requires an Amazon S3 URL for the AWS CloudFormation template. The blueprint's provisioning role must have access to that Amazon S3 object. The `SageMakerStudioProjectProvisioningRolePolicy` managed policy grants `s3:GetObject` on buckets whose names begin with `amazon-sagemaker-cf-templates`. The console creates such a bucket when you upload a template there.

Register the template as a blueprint with `CreateEnvironmentBlueprint`, passing `TOOLING` as the `blueprintCategory`. Optionally, you can declare additional CloudFormation parameters mapped to user parameters when you create a blueprint.

```
aws datazone create-environment-blueprint \
  --domain-identifier {{domain-id}} \
  --name {{blueprint-name}} \
  --blueprint-category TOOLING \
  --provisioning-properties '{
    "cloudFormation": {
      "templateUrl": "https://amazon-sagemaker-cf-templates-{{region}}-{{suffix}}.s3.{{region}}.amazonaws.com/tooling-template.yaml"
    }
  }' \
  --user-parameters '[
    {
      "keyName": "{{key}}",
      "fieldType": "String",
      "defaultValue": "{{value}}",
      "isEditable": true,
      "isOptional": true
    }
  ]'
```

By default, the blueprint is disabled after it is created. To enable the blueprint in an AWS account and AWS Region, you must provide a provisioning role.

**Note**  
Amazon SageMaker Unified Studio deploys your template under the blueprint's provisioning role, so that role's trust policy must let Amazon SageMaker Unified Studio assume it with `sts:AssumeRole` and pass your user context with `sts:TagSession` for the `datazone.amazonaws.com` service principal. For the policy, see [Trust policy for the provisioning role](custom-blueprint.md#custom-blueprint-trust-policy).

```
aws datazone put-environment-blueprint-configuration \
  --domain-identifier {{domain-id}} \
  --environment-blueprint-identifier {{blueprint-id}} \
  --enabled-regions {{region}} \
  --provisioning-role-arn {{provisioning-role-arn}} \
  --regional-parameters '{
    "{{region}}": {
      "kmsKeyArn": "{{kms-key-arn}}"
    }
  }'
```

------
#### [ IAM-based domain ]

```
AWSTemplateFormatVersion: '2010-09-09'

Parameters:
  datazoneEnvironmentDomainId:                { Type: String }
  datazoneEnvironmentEnvironmentId:           { Type: String }
  datazoneEnvironmentProjectExecutionRoleArn: { Type: String }
  datazoneEnvironmentProjectId:               { Type: String }
  datazoneScopeName:                          { Type: String, Default: 'dev' }
  sagemakerUnifiedStudioKmsKeyArn:            { Type: String, Default: '' }

Conditions:
  kmsKeyArnExist: !Not [!Equals [!Ref sagemakerUnifiedStudioKmsKeyArn, '']]

Resources:
  ProjectBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    UpdateReplacePolicy: Retain
    Properties:
      BucketName: !Sub 'amazon-sagemaker-${AWS::AccountId}-${AWS::Region}-${datazoneEnvironmentProjectId}'
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm:   !If [kmsKeyArnExist, 'aws:kms', 'AES256']
              KMSMasterKeyID: !If [kmsKeyArnExist, !Ref sagemakerUnifiedStudioKmsKeyArn, !Ref 'AWS::NoValue']
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
      CorsConfiguration:
        CorsRules:
          - AllowedHeaders: ['*']
            AllowedMethods: [PUT, GET, POST, DELETE, HEAD]
            AllowedOrigins: ['*']
            ExposedHeaders: [x-amz-version-id, ETag, x-amz-checksum-crc32]

  ProjectBucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref ProjectBucket
      PolicyDocument:
        Version: '2012-10-17'		 	 	 
        Statement:
          - Sid: EnforceSSL
            Effect: Deny
            Principal: '*'
            Action: 's3:*'
            Resource: [!GetAtt ProjectBucket.Arn, !Sub '${ProjectBucket.Arn}/*']
            Condition: { Bool: { 'aws:SecureTransport': 'false' } }
          - Sid: ProjectUserRoleAccess
            Effect: Allow
            Principal: '*'
            Action:
              - s3:GetObject*
              - s3:GetBucket*
              - s3:PutObject*
              - s3:ListBucket*
              - s3:RestoreObject
              - s3:ReplicateObject
              - s3:DeleteObject
              - s3:DeleteObjectVersion
              - s3:ListMultipartUploadParts
              - s3:AbortMultipartUpload
              - s3:GetEncryptionConfiguration
            Resource: [!GetAtt ProjectBucket.Arn, !Sub '${ProjectBucket.Arn}/*']
            Condition: { ArnEquals: { 'aws:PrincipalArn': !Ref datazoneEnvironmentProjectExecutionRoleArn } }
          - Sid: DenyDeleteOfShared
            Effect: Deny
            Principal: '*'
            Action: s3:DeleteObject
            Resource:
              - !Sub '${ProjectBucket.Arn}/shared/'
              - !Sub '${ProjectBucket.Arn}/shared/*'
            Condition: { ArnEquals: { 'aws:PrincipalArn': !Ref datazoneEnvironmentProjectExecutionRoleArn } }

  DefaultIAMConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.iam
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation: { AwsAccountId: !Ref 'AWS::AccountId', AwsRegion: !Ref 'AWS::Region' }
      Props:
        IamProperties:
          GlueLineageSyncEnabled: true
          RoleArn: !Ref datazoneEnvironmentProjectExecutionRoleArn

  DefaultS3Connection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.s3
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref 'AWS::AccountId'
        AwsRegion: !Ref 'AWS::Region'
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        S3Properties: { S3Uri: !Sub 's3://${ProjectBucket}/', RegisterS3AccessGrantLocation: false }

  DefaultS3SharedConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.s3_shared
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref 'AWS::AccountId'
        AwsRegion: !Ref 'AWS::Region'
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        S3Properties: { S3Uri: !Sub 's3://${ProjectBucket}/shared/', RegisterS3AccessGrantLocation: false }

Outputs:
  S3BucketArn:
    Value: !Sub '${ProjectBucket.Arn}/'
    Export: { Name: !Sub 's3BucketArn-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  S3BucketPath:
    Value: !Sub 's3://${ProjectBucket}/shared'
    Export: { Name: !Sub 's3BucketPath-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
```

------
#### [ Identity Center-based domain ]

```
AWSTemplateFormatVersion: '2010-09-09'

Parameters:
  awsDefaultGlueCatalogKmsKeyArn:         { Type: String, Default: '' }
  datazoneEnvironmentDomainArn:           { Type: String }
  datazoneEnvironmentDomainId:            { Type: String }
  datazoneEnvironmentDomainKmsKeyArn:     { Type: String, Default: '' }
  datazoneEnvironmentEnvironmentId:       { Type: String }
  datazoneEnvironmentProjectId:           { Type: String }
  datazoneEnvironmentProvisioningRoleArn: { Type: String }
  datazoneScopeName:                      { Type: String, Default: 'dev' }
  sagemakerUnifiedStudioKmsKeyArn:        { Type: String, Default: '' }
  sagemakerUnifiedStudioNetworkVpcId:     { Type: String, Default: '' }

Conditions:
  defaultGlueCatalogKmsKeyArnExist: !Not [!Equals [!Ref awsDefaultGlueCatalogKmsKeyArn, '']]
  domainKmsKeyArnExist:             !Not [!Equals [!Ref datazoneEnvironmentDomainKmsKeyArn, '']]
  kmsKeyArnExist:                   !Not [!Equals [!Ref sagemakerUnifiedStudioKmsKeyArn, '']]

Resources:
  ProjectBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    UpdateReplacePolicy: Retain
    Properties:
      BucketName: !Sub 'sagemaker-${AWS::AccountId}-${AWS::Region}-${datazoneEnvironmentProjectId}'
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm:   !If [kmsKeyArnExist, 'aws:kms', 'AES256']
              KMSMasterKeyID: !If [kmsKeyArnExist, !Ref sagemakerUnifiedStudioKmsKeyArn, !Ref 'AWS::NoValue']
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
      CorsConfiguration:
        CorsRules:
          - AllowedHeaders: ['*']
            AllowedMethods: [PUT, GET, POST, DELETE, HEAD]
            AllowedOrigins: ['*']
            ExposedHeaders: [x-amz-version-id, ETag, x-amz-checksum-crc32]

  ToolingLogGroup:
    Type: AWS::Logs::LogGroup
    DeletionPolicy: Delete
    Properties:
      LogGroupName: !Sub 'datazone-${datazoneEnvironmentProjectId}-${datazoneScopeName}'
      RetentionInDays: 30

  ProjectUserRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub 'datazone_usr_role_${datazoneEnvironmentProjectId}_${datazoneEnvironmentEnvironmentId}'
      Description: User role for all environments and tools.
      Path: /
      ManagedPolicyArns:
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/SageMakerStudioProjectUserRolePolicy'
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/SageMakerStudioProjectRoleMachineLearningPolicy'
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/service-role/SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy'
      AssumeRolePolicyDocument:
        Version: '2012-10-17'		 	 	 
        Statement:
          - Effect: Allow
            Principal:
              Service: [datazone.amazonaws.com, auth.datazone.amazonaws.com]
            Action: [sts:AssumeRole, sts:TagSession, sts:SetContext, sts:SetSourceIdentity]
            Condition:
              StringEquals:
                aws:SourceAccount: !Select [4, !Split [':', !Ref datazoneEnvironmentDomainArn]]
          - Effect: Allow
            Principal:
              Service:
                - glue.amazonaws.com
                - lakeformation.amazonaws.com
                - sagemaker.amazonaws.com
                - emr-serverless.amazonaws.com
                - elasticmapreduce.amazonaws.com
                - airflow.amazonaws.com
                - airflow-env.amazonaws.com
                - lambda.amazonaws.com
                - scheduler.amazonaws.com
                - quicksight.amazonaws.com
                - access-grants.s3.amazonaws.com
                - athena.amazonaws.com
                - airflow-serverless.amazonaws.com
                - bedrock.amazonaws.com
            Action: [sts:AssumeRole, sts:TagSession, sts:SetContext, sts:SetSourceIdentity]
            Condition:
              StringEquals: { aws:SourceAccount: !Ref 'AWS::AccountId' }
          - Effect: Allow
            Principal:
              Service: [redshift-serverless.amazonaws.com, redshift.amazonaws.com]
            Action: sts:AssumeRole
            Condition:
              StringLike:
                sts:ExternalId: !Sub 'arn:${AWS::Partition}:redshift:*:${AWS::AccountId}:dbuser:*/*'
          - Effect: Allow
            Principal:
              Service: [redshift-serverless.amazonaws.com, redshift.amazonaws.com]
            Action: [sts:TagSession, sts:SetContext, sts:SetSourceIdentity]
          - Effect: Allow
            Principal:
              AWS: !Ref datazoneEnvironmentProvisioningRoleArn
            Action: [sts:AssumeRole, sts:TagSession, sts:SetContext, sts:SetSourceIdentity]
      Tags:
        - { Key: AmazonDataZoneScopeName,               Value: !Ref datazoneScopeName }
        - { Key: RedshiftDbUser,                        Value: !Sub 'user-project@${datazoneEnvironmentProjectId}' }
        - { Key: DomainBucketName,                      Value: !Ref ProjectBucket }
        - { Key: EnableAmazonBedrockPermissions,        Value: 'true' }
        - { Key: EnableGlueWorkloadsPermissions,        Value: 'true' }
        - { Key: EnableSageMakerMLWorkloadsPermissions, Value: 'true' }
        - { Key: KmsKeyId,                   Value: !If [kmsKeyArnExist,                   !Select [1, !Split ['/', !Ref sagemakerUnifiedStudioKmsKeyArn]],    ''] }
        - { Key: DomainKmsKeyId,             Value: !If [domainKmsKeyArnExist,             !Select [1, !Split ['/', !Ref datazoneEnvironmentDomainKmsKeyArn]], ''] }
        - { Key: DefaultGlueCatalogKmsKeyId, Value: !If [defaultGlueCatalogKmsKeyArnExist, !Select [1, !Split ['/', !Ref awsDefaultGlueCatalogKmsKeyArn]],     ''] }
        - { Key: LogGroupName,                          Value: !Ref ToolingLogGroup }
        - { Key: RoleName,  Value: !Sub 'datazone_usr_role_${datazoneEnvironmentProjectId}_${datazoneEnvironmentEnvironmentId}' }
        - { Key: vpcArn,    Value: !Sub 'arn:${AWS::Partition}:ec2:${AWS::Region}:${AWS::AccountId}:vpc/${sagemakerUnifiedStudioNetworkVpcId}' }
        - { Key: VpcId,     Value: !Ref sagemakerUnifiedStudioNetworkVpcId }

  ProjectBucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref ProjectBucket
      PolicyDocument:
        Version: '2012-10-17'		 	 	 
        Statement:
          - Sid: DenyInsecureConnections
            Effect: Deny
            Principal: '*'
            Action: 's3:*'
            Resource: [!GetAtt ProjectBucket.Arn, !Sub '${ProjectBucket.Arn}/*']
            Condition: { Bool: { 'aws:SecureTransport': 'false' } }
          - Sid: AllowToolingUserAccess
            Effect: Allow
            Principal: '*'
            Action: [s3:GetObject*, s3:GetBucket*, s3:PutObject*, s3:ListBucket*, s3:RestoreObject, s3:ReplicateObject,
                     s3:DeleteObject, s3:DeleteObjectVersion, s3:ListMultipartUploadParts, s3:AbortMultipartUpload,
                     s3:GetEncryptionConfiguration]
            Resource: [!GetAtt ProjectBucket.Arn, !Sub '${ProjectBucket.Arn}/*']
            Condition: { ArnEquals: { 'aws:PrincipalArn': !GetAtt ProjectUserRole.Arn } }

  DefaultIAMConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: project.iam
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation: { AwsAccountId: !Ref 'AWS::AccountId', AwsRegion: !Ref 'AWS::Region' }
      Props:
        IamProperties:
          GlueLineageSyncEnabled: true
          RoleArn: !GetAtt ProjectUserRole.Arn

  DefaultS3Connection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.s3
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref 'AWS::AccountId'
        AwsRegion: !Ref 'AWS::Region'
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        S3Properties: { S3Uri: !Sub 's3://${ProjectBucket}/', RegisterS3AccessGrantLocation: false }

  DefaultS3SharedConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.s3_shared
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref 'AWS::AccountId'
        AwsRegion: !Ref 'AWS::Region'
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        S3Properties: { S3Uri: !Sub 's3://${ProjectBucket}/shared/', RegisterS3AccessGrantLocation: false }

Outputs:
  S3BucketArn:
    Value: !Sub '${ProjectBucket.Arn}/'
    Export: { Name: !Sub 's3BucketArn-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  S3BucketPath:
    Value: !Sub 's3://${ProjectBucket}/shared'
    Export: { Name: !Sub 's3BucketPath-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
```

------

## Usage
<a name="tooling-usage"></a>

After your blueprint is created and enabled, you use it by composing it into a project profile and then creating a project from that profile.

### Project profile
<a name="tooling-usage-profile"></a>

A project profile names the blueprint that fills the Tooling slot and declares which parameters a project creator can set. Call `CreateProjectProfile`.

Give the Tooling environment a `deploymentMode` of `ON_CREATE` and a `deploymentOrder` of `0`, so that it deploys before anything else in the profile.

**Note**  
A profile can target an account pool instead of a named account. For how account pools work and how to create one, see [Account pools in Amazon SageMaker Unified Studio](account-pools.md).

```
aws datazone create-project-profile \
  --domain-identifier {{domain-id}} \
  --name {{profile-name}} \
  --status ENABLED \
  --environment-configurations '[
    {
      "name": "CustomTooling",
      "environmentBlueprintId": "{{blueprint-id}}",
      "deploymentMode": "ON_CREATE",
      "deploymentOrder": 0,
      "awsAccount": { "awsAccountId": "{{account-id}}" },
      "awsRegion": { "regionName": "{{region}}" },
      "configurationParameters": {
        "parameterOverrides": [
          { "name": "{{parameter-name}}", "value": "" }
        ]
      }
    }
  ]'
```

**Important**  
Pass `--status ENABLED`. A profile is created `DISABLED`, and a disabled profile can't be used to create a project.

### Project
<a name="tooling-usage-project"></a>

#### Create a project
<a name="tooling-usage-create-project"></a>

Call `CreateProject` and reference the profile. Supply user parameter values under `--user-parameters`. The `environmentConfigurationName` value must match the name in the profile exactly.

```
aws datazone create-project \
  --domain-identifier {{domain-id}} \
  --name {{project-name}} \
  --project-profile-id {{profile-id}} \
  --user-parameters '[
    {
      "environmentConfigurationName": "CustomTooling",
      "environmentParameters": [
        { "name": "{{parameter-name}}", "value": "{{value}}" }
      ]
    }
  ]'
```

In an IAM-based domain, also pass the role that becomes the project role. Your template receives this ARN through the reserved parameter `datazoneEnvironmentProjectExecutionRoleArn`. In an Identity Center-based domain, omit it, because your template creates the project role itself.

```
aws datazone create-project \
  --domain-identifier {{domain-id}} \
  --name {{project-name}} \
  --project-profile-id {{profile-id}} \
  --project-execution-role {{project-role-arn}}
```