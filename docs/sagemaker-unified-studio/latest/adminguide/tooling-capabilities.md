

# Tooling capabilities
<a name="tooling-capabilities"></a>

A service-managed Tooling environment already provisions a broad set of capabilities. With a custom Tooling blueprint you decide which of them your template provisions, subject only to the minimum in [Template requirements](tooling-custom-blueprints.md#tooling-template-requirements).

Each module is a partial AWS CloudFormation fragment, not a template on its own. Combine one, several, or all of them into a template from [Minimum Tooling template](tooling-custom-blueprints.md#tooling-minimum-template). For the IAM roles that Tooling requires and the AWS managed policies that grant their permissions, see [Tooling blueprints in Amazon SageMaker Unified Studio](tooling.md).

**Topics**
+ [Amazon Athena](#tooling-capability-athena)
+ [Amazon Athena (Spark)](#tooling-capability-athena-spark)
+ [Data catalog](#tooling-capability-data-catalog)
+ [Amazon EventBridge Scheduler](#tooling-capability-scheduler)
+ [AWS Glue (Spark)](#tooling-capability-glue-spark)
+ [AWS Lake Formation](#tooling-capability-lake-formation)
+ [Amazon Managed Workflows for Apache Airflow](#tooling-capability-workflows)
+ [Amazon SageMaker AI](#tooling-capability-sagemaker-ai)
+ [Trusted identity propagation](#tooling-capability-tip)

## Amazon Athena
<a name="tooling-capability-athena"></a>

Provisions an Amazon Athena workgroup and a connection to it, so project members can run SQL against the project's data. The workgroup writes its results under the project's Amazon S3 storage, encrypted with the project's AWS KMS key when the domain has one.

------
#### [ IAM-based domain ]

```
Resources:
  AthenaWorkGroup:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name: !Sub 'sagemaker-studio-workgroup-${datazoneEnvironmentProjectId}'
      Description: SageMaker Unified Studio project Workgroup
      RecursiveDeleteOption: true
      Tags:
        - { Key: AmazonDataZoneScopeName, Value: !Ref datazoneScopeName }
      WorkGroupConfiguration:
        EnforceWorkGroupConfiguration: true
        CustomerContentEncryptionConfiguration:
          Fn::If:
            - kmsKeyArnExist
            - KmsKey: !Ref sagemakerUnifiedStudioKmsKeyArn
            - !Ref 'AWS::NoValue'
        ResultConfiguration:
          EncryptionConfiguration:
            Fn::If:
              - kmsKeyArnExist
              - EncryptionOption: SSE_KMS
                KmsKey: !Ref sagemakerUnifiedStudioKmsKeyArn
              - EncryptionOption: SSE_S3
          OutputLocation: !Sub 's3://${ProjectBucket}/sys/athena/'

  AthenaConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.sql
      Description: Default connection to Amazon Athena SQL for interactive queries on your data.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        AthenaProperties:
          WorkgroupName: !Ref AthenaWorkGroup

Outputs:
  AthenaWorkGroupName:
    Value: !Ref AthenaWorkGroup
    Export:
      Name: !Sub 'athenaWorkGroupName-${datazoneEnvironmentEnvironmentId}'
  AthenaOutputUri:
    Value: !Sub 's3://${ProjectBucket}/sys/athena/'
    Export:
      Name: !Sub 'athenaOutputUri-${datazoneEnvironmentEnvironmentId}'
```

------
#### [ Identity Center-based domain ]

```
Resources:
  AthenaWorkGroup:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name: !Sub 'workgroup-${datazoneEnvironmentProjectId}-${datazoneEnvironmentEnvironmentId}'
      Description: DataZone Workgroup
      RecursiveDeleteOption: true
      Tags:
        - { Key: AmazonDataZoneScopeName, Value: !Ref datazoneScopeName }
      WorkGroupConfiguration:
        EnforceWorkGroupConfiguration: true
        CustomerContentEncryptionConfiguration:
          Fn::If:
            - kmsKeyArnExist
            - KmsKey: !Ref sagemakerUnifiedStudioKmsKeyArn
            - !Ref 'AWS::NoValue'
        ResultConfiguration:
          EncryptionConfiguration:
            Fn::If:
              - kmsKeyArnExist
              - EncryptionOption: SSE_KMS
                KmsKey: !Ref sagemakerUnifiedStudioKmsKeyArn
              - EncryptionOption: SSE_S3
          OutputLocation: !Sub 's3://${ProjectBucket}/dev/sys/athena/'

  AthenaConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: project.athena
      Description: Default connection to Amazon Athena SQL for interactive queries on your data.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        AthenaProperties:
          WorkgroupName: !Ref AthenaWorkGroup

Outputs:
  AthenaWorkGroupName:
    Value: !Ref AthenaWorkGroup
    Export:
      Name: !Sub 'athenaWorkGroupName-${datazoneEnvironmentEnvironmentId}'
  AthenaOutputUri:
    Value: !Sub 's3://${ProjectBucket}/dev/sys/athena/'
    Export:
      Name: !Sub 'athenaOutputUri-${datazoneEnvironmentEnvironmentId}'
```

------

## Amazon Athena (Spark)
<a name="tooling-capability-athena-spark"></a>

Provisions an Amazon Athena Spark workgroup and a connection to it, which gives members Spark without a VPC or a cluster. The workgroup runs calculations as the project user role and writes its logs under the project's Amazon S3 storage.

------
#### [ IAM-based domain ]

```
Resources:
  AthenaSparkWorkGroup:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name: !Sub 'sagemaker-studio-spark-workgroup-${datazoneEnvironmentProjectId}'
      Description: SageMaker Unified Studio project Athena Spark Workgroup
      WorkGroupConfiguration:
        EnforceWorkGroupConfiguration: false
        PublishCloudWatchMetricsEnabled: true
        EngineVersion:
          SelectedEngineVersion: Apache Spark version 3.5
        ExecutionRole: !Ref datazoneEnvironmentProjectExecutionRoleArn
        MonitoringConfiguration:
          ManagedLoggingConfiguration:
            Enabled: true
            KmsKey: !If [kmsKeyArnExist, !Ref sagemakerUnifiedStudioKmsKeyArn, !Ref 'AWS::NoValue']
          S3LoggingConfiguration:
            Enabled: true
            KmsKey: !If [kmsKeyArnExist, !Ref sagemakerUnifiedStudioKmsKeyArn, !Ref 'AWS::NoValue']
            LogLocation: !Sub 's3://${ProjectBucket}/sys/athena-spark/'

  ServerlessSparkConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: serverless.spark
      Description: Default connection to Amazon Athena for Apache Spark, designed for interactive data analysis.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        AthenaProperties:
          WorkgroupName: !Ref AthenaSparkWorkGroup

Outputs:
  AthenaSparkWorkGroupName:
    Value: !Ref AthenaSparkWorkGroup
    Export:
      Name: !Sub 'athenaSparkWorkGroupName-${datazoneEnvironmentEnvironmentId}'
```

------
#### [ Identity Center-based domain ]

```
Resources:
  AthenaSparkWorkGroup:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name: !Sub 'sagemaker-studio-spark-workgroup-${datazoneEnvironmentProjectId}'
      Description: SageMaker Unified Studio project Athena Spark Workgroup
      WorkGroupConfiguration:
        EnforceWorkGroupConfiguration: true
        PublishCloudWatchMetricsEnabled: true
        EngineVersion:
          SelectedEngineVersion: Apache Spark version 3.5
        ExecutionRole: !GetAtt ProjectUserRole.Arn
        MonitoringConfiguration:
          ManagedLoggingConfiguration:
            Enabled: true
            KmsKey: !If [kmsKeyArnExist, !Ref sagemakerUnifiedStudioKmsKeyArn, !Ref 'AWS::NoValue']
          S3LoggingConfiguration:
            Enabled: true
            KmsKey: !If [kmsKeyArnExist, !Ref sagemakerUnifiedStudioKmsKeyArn, !Ref 'AWS::NoValue']
            LogLocation: !Sub 's3://${ProjectBucket}/dev/sys/athena-spark-logs/'

  ServerlessSparkConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: serverless.spark
      Description: Default connection to Amazon Athena for Apache Spark, designed for interactive data analysis.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        AthenaProperties:
          WorkgroupName: !Ref AthenaSparkWorkGroup

Outputs:
  AthenaSparkWorkGroupName:
    Value: !Ref AthenaSparkWorkGroup
    Export:
      Name: !Sub 'athenaSparkWorkGroupName-${datazoneEnvironmentEnvironmentId}'
```

------

## Data catalog
<a name="tooling-capability-data-catalog"></a>

Declares the connection that gives project members the catalogs available in AWS Glue, which is what populates the catalog browser in the project. The connection carries no configuration of its own: it resolves the account's catalogs through the project user role, so a project gets exactly the catalogs that role can reach.

------
#### [ IAM-based domain ]

```
Resources:
  DefaultCatalogConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.catalog
      Description: This is the default connection to all catalogs available in your AWS Glue.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        LakehouseProperties: {}
```

------
#### [ Identity Center-based domain ]

```
Resources:
  DefaultCatalogConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: project.default_lakehouse
      Description: This is the default connection to interact with project Lakehouse.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        LakehouseProperties:
          GlueLineageSyncEnabled: true
```

------

## Amazon EventBridge Scheduler
<a name="tooling-capability-scheduler"></a>

Declares the schedule group that holds a project's schedules. Project members who schedule a notebook or a query create schedules inside this group, and a project without one cannot schedule work.

```
Resources:
  EventBridgeScheduleGroup:
    Type: AWS::Scheduler::ScheduleGroup
    Properties:
      Name: !Sub 'SageMakerUnifiedStudio-${datazoneEnvironmentProjectId}-${datazoneScopeName}'
      Tags:
        - { Key: AmazonDataZoneScopeName, Value: !Ref datazoneScopeName }

Outputs:
  ScheduleGroupName:
    Value: !Ref EventBridgeScheduleGroup
    Export:
      Name: !Sub 'ScheduleGroupName-${datazoneEnvironmentProjectId}-${datazoneScopeName}'
```

## AWS Glue (Spark)
<a name="tooling-capability-glue-spark"></a>

Declares the Spark connections that run AWS Glue ETL sessions. An IAM-based domain uses a single compatibility connection. An Identity Center-based domain uses two, differing only in AWS Lake Formation permission mode. Each connection takes the project's Glue network connection when the domain has one, and omits it otherwise.

------
#### [ IAM-based domain ]

```
Parameters:
  sagemakerUnifiedStudioNetworkGlueConnectionNames:
    Type: String
    Default: ''

Conditions:
  NetworkGlueConnectionsExist: !Not [!Equals [!Ref sagemakerUnifiedStudioNetworkGlueConnectionNames, '']]

Resources:
  SparkGlueCompatibilityConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.spark
      Description: Default connection to Spark compute from AWS Glue for visual ETL, interactive analysis and batch jobs.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        SparkGlueProperties:
          GlueConnectionName: !If
            - NetworkGlueConnectionsExist
            - !Select [0, !Split [',', !Ref sagemakerUnifiedStudioNetworkGlueConnectionNames]]
            - !Ref 'AWS::NoValue'
          GlueVersion: '5.0'
          IdleTimeout: 60
          NumberOfWorkers: 10
          WorkerType: G.1X
      Configurations:
        - Classification: GlueDefaultArgument
          Properties:
            '--enable-lakeformation-fine-grained-access': 'false'
```

------
#### [ Identity Center-based domain ]

```
Parameters:
  sagemakerUnifiedStudioNetworkSecurityGroupId:
    Type: String
  sagemakerUnifiedStudioNetworkSubnets:
    Type: String

Resources:
  ProjectGlueNetworkConnection:
    Type: AWS::Glue::Connection
    Properties:
      CatalogId: !Ref AWS::AccountId
      ConnectionInput:
        ConnectionType: NETWORK
        Description: Connection between Glue and VPC
        Name: !Sub 'datazone-glue-network-connection-${datazoneEnvironmentProjectId}-${datazoneScopeName}'
        PhysicalConnectionRequirements:
          SecurityGroupIdList:
            - !Ref sagemakerUnifiedStudioNetworkSecurityGroupId
          SubnetId: !Select [0, !Split [',', !Ref sagemakerUnifiedStudioNetworkSubnets]]

  SparkGlueCompatibilityConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: project.spark.compatibility
      Description: Glue-ETL compute with Permission Mode set to compatibility. (Auto-created by project).
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        SparkGlueProperties:
          GlueConnectionName: !Ref ProjectGlueNetworkConnection
          GlueVersion: '5.0'
          IdleTimeout: 60
          NumberOfWorkers: 10
          WorkerType: G.1X
      Configurations:
        - Classification: GlueDefaultArgument
          Properties:
            '--enable-lakeformation-fine-grained-access': 'false'

  SparkGlueFineGrainedConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: project.spark.fineGrained
      Description: Glue-ETL compute with Permission Mode set to fine-grained. (Auto-created by project).
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        SparkGlueProperties:
          GlueConnectionName: !Ref ProjectGlueNetworkConnection
          GlueVersion: '5.0'
          IdleTimeout: 60
          NumberOfWorkers: 10
          WorkerType: G.1X
      Configurations:
        - Classification: GlueDefaultArgument
          Properties:
            '--enable-lakeformation-fine-grained-access': 'true'
```

------

## AWS Lake Formation
<a name="tooling-capability-lake-formation"></a>

Grants the project user role the AWS Lake Formation permissions it needs to work with the project's data. With an Identity Center-based domain, your project's Amazon S3 location is also registered with AWS Lake Formation, so AWS Lake Formation governs data written there. With an IAM-based domain, you rely on account-level full table access instead; no location is registered and no data location permission is granted.

With an IAM-based domain, you don't add this capability to your template. The project role is the role that you pass at project creation, and the grant belongs to that role rather than to a project. As a result, you make the grant once per role with the AWS CLI instead of once per project in a template.

**Important**  
Amazon SageMaker Unified Studio performs two account-level AWS Lake Formation actions for a service-managed environment that a template can't express. You are responsible for both, once per account, before you deploy a custom blueprint that includes this capability:  
Register the blueprint's provisioning role as an AWS Lake Formation data lake administrator. Creating an AWS Lake Formation permission fails without it.
In an IAM-based domain, enable full table access for the account. This is an account-level setting, and it stays in effect after you delete the project.

------
#### [ IAM-based domain ]

Don't put this grant in your template. The project role in an IAM-based domain is the role that you pass at project creation, and an AWS Lake Formation permission is held by a principal, not by a project. A template that grants it fails on the second project that passes the same role, with `Resource of type 'AWS::LakeFormation::PrincipalPermissions' ... already exists.`

Grant it yourself instead, once per project role.

```
aws lakeformation grant-permissions \
  --catalog-id {{account-id}} \
  --principal DataLakePrincipalIdentifier={{project-role-arn}} \
  --resource '{
    "Database": { "CatalogId": "{{account-id}}", "Name": "default" }
  }' \
  --permissions DESCRIBE
```

An IAM-based domain registers no Amazon S3 location and grants no data location permission, so this AWS Lake Formation DESCRIBE grant is the whole of the capability for this domain type.

------
#### [ Identity Center-based domain ]

```
Resources:
  ProjectS3LakeFormationResource:
    Type: AWS::LakeFormation::Resource
    Properties:
      ResourceArn: !Sub '${ProjectBucket.Arn}/${datazoneScopeName}'
      RoleArn: !GetAtt ProjectUserRole.Arn
      UseServiceLinkedRole: false

  DefaultDatabaseDescribePermission:
    Type: AWS::LakeFormation::PrincipalPermissions
    Properties:
      Catalog: !Ref AWS::AccountId
      Principal:
        DataLakePrincipalIdentifier: !GetAtt ProjectUserRole.Arn
      Resource:
        Database:
          CatalogId: !Ref AWS::AccountId
          Name: default
      Permissions:
        - DESCRIBE
      PermissionsWithGrantOption: []

  ProjectS3DataLocationPermission:
    Type: AWS::LakeFormation::PrincipalPermissions
    DependsOn: ProjectS3LakeFormationResource
    Properties:
      Catalog: !Ref AWS::AccountId
      Principal:
        DataLakePrincipalIdentifier: !GetAtt ProjectUserRole.Arn
      Resource:
        DataLocation:
          CatalogId: !Ref AWS::AccountId
          ResourceArn: !Sub '${ProjectBucket.Arn}/${datazoneScopeName}'
      Permissions:
        - DATA_LOCATION_ACCESS
      PermissionsWithGrantOption: []
```

------

## Amazon Managed Workflows for Apache Airflow
<a name="tooling-capability-workflows"></a>

Declares the connection that runs a project's workflows on serverless Amazon Managed Workflows for Apache Airflow compute. Project members author and run workflows through this connection, and a project without it cannot run them. The connection carries no configuration of its own.

------
#### [ IAM-based domain ]

```
Resources:
  WorkflowsServerlessConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.workflow_serverless
      Description: Default connection to Amazon Managed Workflows for Apache Airflow (MWAA) serverless compute.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        WorkflowsServerlessProperties: {}
```

------
#### [ Identity Center-based domain ]

```
Resources:
  WorkflowsServerlessConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: default.workflow_serverless
      Description: Default connection to Amazon Managed Workflows for Apache Airflow (MWAA) serverless compute.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      Props:
        WorkflowsServerlessProperties: {}
```

------

## Amazon SageMaker AI
<a name="tooling-capability-sagemaker-ai"></a>

Provisions an Amazon SageMaker AI domain, which backs the JupyterLab and Code Editor spaces that members open from the project. The domain runs spaces as the project user role. When the Amazon SageMaker Unified Studio domain is configured with a VPC, the Amazon SageMaker AI domain confines space traffic to it; otherwise spaces reach the internet through an Amazon SageMaker AI managed VPC.

------
#### [ IAM-based domain ]

```
Parameters:
  datazoneEnvironmentDomainArn:
    Type: String
  sagemakerUnifiedStudioNetworkVpcId:
    Type: String
    Default: ''
  sagemakerUnifiedStudioNetworkSubnets:
    Type: String
    Default: ''
  sagemakerUnifiedStudioNetworkSecurityGroupId:
    Type: String
    Default: ''

Conditions:
  VpcIdExists: !Not [!Equals [!Ref sagemakerUnifiedStudioNetworkVpcId, '']]

Resources:
  SageMakerSpacesDefaultDomain:
    Type: AWS::SageMaker::Domain
    Properties:
      DomainName: !Sub 'SageMakerUnifiedStudio-${datazoneEnvironmentProjectId}-${datazoneEnvironmentEnvironmentId}-${datazoneScopeName}'
      AuthMode: IAM
      AppNetworkAccessType: !If [VpcIdExists, VpcOnly, PublicInternetOnly]
      VpcId: !If [VpcIdExists, !Ref sagemakerUnifiedStudioNetworkVpcId, !Ref 'AWS::NoValue']
      SubnetIds: !If [VpcIdExists, !Split [',', !Ref sagemakerUnifiedStudioNetworkSubnets], !Ref 'AWS::NoValue']
      KmsKeyId: !If [kmsKeyArnExist, !Ref sagemakerUnifiedStudioKmsKeyArn, !Ref 'AWS::NoValue']
      DomainSettings:
        DockerSettings:
          EnableDockerAccess: ENABLED
        ExecutionRoleIdentityConfig: USER_PROFILE_NAME
      DefaultSpaceSettings:
        ExecutionRole: !Ref datazoneEnvironmentProjectExecutionRoleArn
        JupyterLabAppSettings:
          AppLifecycleManagement:
            IdleSettings:
              IdleTimeoutInMinutes: 60
              LifecycleManagement: ENABLED
              MaxIdleTimeoutInMinutes: 525600
              MinIdleTimeoutInMinutes: 60
      DefaultUserSettings:
        ExecutionRole: !Ref datazoneEnvironmentProjectExecutionRoleArn
        SecurityGroups: !If [VpcIdExists, !Split [',', !Ref sagemakerUnifiedStudioNetworkSecurityGroupId], !Ref 'AWS::NoValue']
        JupyterLabAppSettings:
          AppLifecycleManagement:
            IdleSettings:
              IdleTimeoutInMinutes: 60
              LifecycleManagement: ENABLED
              MaxIdleTimeoutInMinutes: 525600
              MinIdleTimeoutInMinutes: 60
        CodeEditorAppSettings:
          AppLifecycleManagement:
            IdleSettings:
              IdleTimeoutInMinutes: 60
              LifecycleManagement: ENABLED
              MaxIdleTimeoutInMinutes: 525600
              MinIdleTimeoutInMinutes: 60
        SpaceStorageSettings:
          DefaultEbsStorageSettings:
            DefaultEbsVolumeSizeInGb: 16
            MaximumEbsVolumeSizeInGb: 100
        CustomFileSystemConfigs:
          - S3FileSystemConfig:
              S3Uri: !Sub 's3://${ProjectBucket}/shared/'
              MountPath: shared
      Tags:
        - { Key: AmazonDataZoneDomainAccount, Value: !Select [4, !Split [':', !Ref datazoneEnvironmentDomainArn]] }
        - { Key: AmazonDataZoneDomainRegion,  Value: !Select [3, !Split [':', !Ref datazoneEnvironmentDomainArn]] }
        - { Key: AmazonDataZoneDomain,        Value: !Ref datazoneEnvironmentDomainId }
        - { Key: AmazonDataZoneProject,       Value: !Ref datazoneEnvironmentProjectId }
        - { Key: AmazonDataZoneEnvironment,   Value: !Ref datazoneEnvironmentEnvironmentId }
        - { Key: AmazonDataZoneStage,         Value: prod }
        - { Key: AmazonDataZoneScopeName,     Value: !Ref datazoneScopeName }
        - { Key: ProjectS3Path,               Value: !Sub 's3://${ProjectBucket}/shared/' }

Outputs:
  SageMakerSpacesDomain:
    Value: !GetAtt SageMakerSpacesDefaultDomain.DomainId
    Export:
      Name: !Sub 'SageMakerSpacesDomain-${datazoneEnvironmentEnvironmentId}-${datazoneScopeName}'
  SageMakerDomainId:
    Value: !GetAtt SageMakerSpacesDefaultDomain.DomainId
    Export:
      Name: !Sub 'sageMakerDomainId-${datazoneEnvironmentEnvironmentId}-${datazoneScopeName}'
```

------
#### [ Identity Center-based domain ]

**Note**  
Replace {{minute}} and {{hour}} on the data source schedule with a daily time of your choosing. A service-managed environment picks this time per data source so that scans don't all run at once. Avoid giving every project the same value. Copying the listing without substituting them leaves an invalid cron expression. The stack then fails validation before any resource is created.

```
Parameters:
  datazoneEnvironmentDomainArn:
    Type: String
  sagemakerUnifiedStudioNetworkVpcId:
    Type: String
    Default: ''
  sagemakerUnifiedStudioNetworkSubnets:
    Type: String
    Default: ''
  sagemakerUnifiedStudioNetworkSecurityGroupId:
    Type: String
    Default: ''

Conditions:
  VpcIdExists: !Not [!Equals [!Ref sagemakerUnifiedStudioNetworkVpcId, '']]

Resources:
  SageMakerSpacesDefaultDomain:
    Type: AWS::SageMaker::Domain
    Properties:
      DomainName: !Sub 'SageMakerUnifiedStudio-${datazoneEnvironmentProjectId}-${datazoneEnvironmentEnvironmentId}-${datazoneScopeName}'
      AuthMode: IAM
      AppNetworkAccessType: !If [VpcIdExists, VpcOnly, PublicInternetOnly]
      VpcId: !If [VpcIdExists, !Ref sagemakerUnifiedStudioNetworkVpcId, !Ref 'AWS::NoValue']
      SubnetIds: !If [VpcIdExists, !Split [',', !Ref sagemakerUnifiedStudioNetworkSubnets], !Ref 'AWS::NoValue']
      KmsKeyId: !If [kmsKeyArnExist, !Ref sagemakerUnifiedStudioKmsKeyArn, !Ref 'AWS::NoValue']
      DomainSettings:
        DockerSettings:
          EnableDockerAccess: ENABLED
        ExecutionRoleIdentityConfig: USER_PROFILE_NAME
      DefaultSpaceSettings:
        ExecutionRole: !GetAtt ProjectUserRole.Arn
        JupyterLabAppSettings:
          AppLifecycleManagement:
            IdleSettings:
              IdleTimeoutInMinutes: 60
              LifecycleManagement: ENABLED
              MaxIdleTimeoutInMinutes: 525600
              MinIdleTimeoutInMinutes: 60
      DefaultUserSettings:
        ExecutionRole: !GetAtt ProjectUserRole.Arn
        SecurityGroups: !If [VpcIdExists, !Split [',', !Ref sagemakerUnifiedStudioNetworkSecurityGroupId], !Ref 'AWS::NoValue']
        JupyterLabAppSettings:
          AppLifecycleManagement:
            IdleSettings:
              IdleTimeoutInMinutes: 60
              LifecycleManagement: ENABLED
              MaxIdleTimeoutInMinutes: 525600
              MinIdleTimeoutInMinutes: 60
        CodeEditorAppSettings:
          AppLifecycleManagement:
            IdleSettings:
              IdleTimeoutInMinutes: 60
              LifecycleManagement: ENABLED
              MaxIdleTimeoutInMinutes: 525600
              MinIdleTimeoutInMinutes: 60
        SpaceStorageSettings:
          DefaultEbsStorageSettings:
            DefaultEbsVolumeSizeInGb: 16
            MaximumEbsVolumeSizeInGb: 100
        CustomFileSystemConfigs:
          - S3FileSystemConfig:
              S3Uri: !Sub 's3://${ProjectBucket}/shared'
              MountPath: shared
      Tags:
        - { Key: AmazonDataZoneDomainAccount, Value: !Select [4, !Split [':', !Ref datazoneEnvironmentDomainArn]] }
        - { Key: AmazonDataZoneDomainRegion,  Value: !Select [3, !Split [':', !Ref datazoneEnvironmentDomainArn]] }
        - { Key: AmazonDataZoneDomain,        Value: !Ref datazoneEnvironmentDomainId }
        - { Key: AmazonDataZoneProject,       Value: !Ref datazoneEnvironmentProjectId }
        - { Key: AmazonDataZoneEnvironment,   Value: !Ref datazoneEnvironmentEnvironmentId }
        - { Key: AmazonDataZoneStage,         Value: prod }
        - { Key: AmazonDataZoneScopeName,     Value: !Ref datazoneScopeName }
        - { Key: ProjectS3Path,               Value: !Sub 's3://${ProjectBucket}/${datazoneScopeName}' }

  SageMakerSubscriptionTarget:
    Type: AWS::DataZone::SubscriptionTarget
    Properties:
      Name: 'Tooling-default-target'
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      Type: BaseSubscriptionTargetType
      Provider: Amazon SageMaker
      ApplicableAssetTypes:
        - SageMakerFeatureGroupAssetType
        - SageMakerModelPackageGroupAssetType
      AuthorizedPrincipals:
        - !GetAtt ProjectUserRole.Arn
      SubscriptionTargetConfig: []

  SageMakerDataSource:
    Type: AWS::DataZone::DataSource
    Properties:
      Name: 'Tooling-default-sagemaker-modelpackagegroup-datasource'
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      ConnectionIdentifier: !GetAtt DefaultIAMConnection.ConnectionId
      Type: SAGEMAKER
      EnableSetting: ENABLED
      PublishOnImport: false
      Schedule:
        Schedule: 'cron({{minute}} {{hour}} * * ? *)'
      Recommendation:
        EnableBusinessNameGeneration: false
      Configuration:
        SageMakerRunConfiguration:
          TrackingAssets:
            SageMakerModelPackageGroupAssetType: []

Outputs:
  SageMakerSpacesDomain:
    Value: !GetAtt SageMakerSpacesDefaultDomain.DomainId
    Export:
      Name: !Sub 'SageMakerSpacesDomain-${datazoneEnvironmentEnvironmentId}-${datazoneScopeName}'
  SageMakerDomainId:
    Value: !GetAtt SageMakerSpacesDefaultDomain.DomainId
    Export:
      Name: !Sub 'sageMakerDomainId-${datazoneEnvironmentEnvironmentId}-${datazoneScopeName}'
```

------

## Trusted identity propagation
<a name="tooling-capability-tip"></a>

Declares the connections that support trusted identity propagation, and whether the project enables user background sessions. For more information, see [Trusted identity propagation](trusted-identity-propagation.md).

------
#### [ IAM-based domain ]

Trusted identity propagation requires an IAM Identity Center instance attached to your Amazon SageMaker Unified Studio domain.

------
#### [ Identity Center-based domain ]

```
Parameters:
  enableTrustedIdentityPropagation:
    Type: String
    Default: 'false'
    AllowedValues: ['true', 'false']
  enableUserBackgroundSessions:
    Type: String
    Default: 'false'
    AllowedValues: ['true', 'false']

Resources:
  AthenaConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: project.athena
      Description: Default connection to Amazon Athena SQL for interactive queries on your data.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      EnableTrustedIdentityPropagation: !Ref enableTrustedIdentityPropagation
      Props:
        AthenaProperties:
          WorkgroupName: !Ref AthenaWorkGroup

  DefaultCatalogConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: project.default_lakehouse
      Description: This is the default connection to interact with project Lakehouse.
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      EnableTrustedIdentityPropagation: !Ref enableTrustedIdentityPropagation
      Props:
        LakehouseProperties:

  SparkGlueCompatibilityConnection:
    Type: AWS::DataZone::Connection
    Properties:
      Name: project.spark.compatibility
      Description: Glue-ETL compute with Permission Mode set to compatibility. (Auto-created by project).
      DomainIdentifier: !Ref datazoneEnvironmentDomainId
      EnvironmentIdentifier: !Ref datazoneEnvironmentEnvironmentId
      ProjectIdentifier: !Ref datazoneEnvironmentProjectId
      AwsLocation:
        AwsAccountId: !Ref AWS::AccountId
        AwsRegion: !Ref AWS::Region
        IamConnectionId: !GetAtt DefaultIAMConnection.ConnectionId
      EnableTrustedIdentityPropagation: !Ref enableTrustedIdentityPropagation
      Props:
        SparkGlueProperties:
          GlueConnectionName: !Ref ProjectGlueNetworkConnection
          GlueVersion: '5.0'
          IdleTimeout: 60
          NumberOfWorkers: 10
          WorkerType: G.1X

Outputs:
  EnableTrustedIdentityPropagationPermissions:
    Value: !Ref enableTrustedIdentityPropagation
    Export:
      Name: !Sub 'enableTrustedIdentityPropagationPermissions-${datazoneEnvironmentProjectId}-${datazoneScopeName}'
  EnableUserBackgroundSessions:
    Value: !Ref enableUserBackgroundSessions
    Export:
      Name: !Sub 'enableUserBackgroundSessions-${datazoneEnvironmentProjectId}-${datazoneScopeName}'
```

------