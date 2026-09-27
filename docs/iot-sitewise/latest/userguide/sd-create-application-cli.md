

# Appendix: Create an application using the AWS CLI
<a name="sd-create-application-cli"></a>

When you create a Scenario Discovery application in the AWS IoT SiteWise console and choose **Complete Setup**, the console automatically creates two IAM service roles that the application needs. When you create an application with the AWS CLI or SDK instead, these tools don't create those roles for you. If you skip creating them, users of the application receive an AccessDenied error. This topic shows how to create the application and then create and scope the two required roles yourself so the CLI path matches the console path.

**Note**  
The IAM Identity Center (IdC) instance must be in the same AWS Region and account where you use Scenario Discovery.

The commands in this topic use the following placeholder values. Replace each placeholder with a value for your environment.
+ `<AccountId>`: 12-digit account ID for the owner of the application, for example, 123456789012
+ `<WorkspaceArn>`: full ARN of the workspace, for example, arn:aws:iotsitewise:us-east-1:123456789012:workspace/WorkspaceName
+ `<ApplicationArn>`: full ARN of the application, for example, arn:aws:iotsitewise:us-east-1:123456789012:workspace/WorkspaceName/application/ApplicationId
+ `<ApplicationId>`: application ID returned from the create-application or describe-application API calls, for example, 6b4c706d-9f48-4b33-892c-f3986e888f55
+ `<Region>`: the Region where the application exists, for example, us-east-1

## Step 1: Create the application
<a name="sd-cli-create-application"></a>

Create the application in an existing workspace. Note the ApplicationId in the response; you need it for the role names and ARNs.

```
aws iotsitewise create-application \
     --idc-instance-arn arn:aws:sso:::instance/ssoins-EXAMPLE \
     --workspace-name WorkspaceName \
     --name scenario_discovery \
     --description "app for scenario discovery" \
     --region <Region>
```

## Step 2: Configure the Application role
<a name="sd-cli-application-role"></a>

### Create the role
<a name="sd-cli-application-role-create"></a>

```
aws iam create-role \
     --role-name SD-Application-Role-<ApplicationId> \
     --path /service-role/ \
     --assume-role-policy-document '{
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AWSIoTSiteWiseScenarioDiscoveryApplication",
               "Effect": "Allow",
               "Principal": {
                   "Service": "applications.iotsitewise.amazonaws.com"
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:SetContext"
               ],
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "<AccountId>"
                   },
                   "ArnEquals": {
                       "aws:SourceArn": "<ApplicationArn>"
                   }
               }
           }
       ]
   }'
```

### Assign minimal permissions
<a name="sd-cli-application-role-permissions"></a>

```
aws iam put-role-policy \
     --role-name SD-Application-Role-<ApplicationId> \
     --policy-name SD-Application-IoTSiteWise-Permissions \
     --policy-document '{
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "iotsitewise:CreateDataset",
                   "iotsitewise:DescribeDataset",
                   "iotsitewise:UpdateDataset",
                   "iotsitewise:ListDatasets",
                   "iotsitewise:BatchAssociateDataSegmentsToDataset",
                   "iotsitewise:BatchDisassociateDataSegmentsFromDataset",
                   "iotsitewise:ListDatasetDataSegments",
                   "iotsitewise:DeleteDataset",
                   "iotsitewise:CreateDatasetExportJob",
                   "iotsitewise:DescribeDatasetExportJob",
                   "iotsitewise:ListDatasetExportJobs"
               ],
               "Resource": [
                   "<WorkspaceArn>",
                   "arn:aws:iotsitewise:<Region>:<AccountId>:dataset/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "iotsitewise:StartSearch",
                   "iotsitewise:GetSearchResults",
                   "iotsitewise:DescribeSearch",
                   "iotsitewise:ListSearches"
               ],
               "Resource": "<WorkspaceArn>"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "iotsitewise:GetCaptureData"
               ],
               "Resource": [
                   "arn:aws:iotsitewise:<Region>:<AccountId>:time-series/*",
                   "<WorkspaceArn>"
               ]
           }
       ]
   }'
```

## Step 3: Configure the Data Curation role
<a name="sd-cli-datacuration-role"></a>

### Create the role
<a name="sd-cli-datacuration-role-create"></a>

```
aws iam create-role \
     --role-name SD-DataCuration-Role-<ApplicationId> \
     --path /service-role/ \
     --assume-role-policy-document '{
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AWSIoTSiteWiseScenarioDiscoveryDataCuration",
               "Effect": "Allow",
               "Principal": {
                   "Service": "applications.iotsitewise.amazonaws.com"
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:SetContext"
               ],
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "<AccountId>"
                   },
                   "ArnEquals": {
                       "aws:SourceArn": "<ApplicationArn>"
                   }
               }
           }
       ]
   }'
```

### Assign minimal permissions
<a name="sd-cli-datacuration-role-permissions"></a>

```
aws iam put-role-policy \
     --role-name SD-DataCuration-Role-<ApplicationId> \
     --policy-name SD-DataCuration-IoTSiteWise-Permissions \
     --policy-document '{
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "iotsitewise:CreateDataset",
                   "iotsitewise:DescribeDataset",
                   "iotsitewise:BatchAssociateDataSegmentsToDataset"
               ],
               "Resource": [
                   "<WorkspaceArn>",
                   "arn:aws:iotsitewise:<Region>:<AccountId>:dataset/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "iotsitewise:StartSearch",
                   "iotsitewise:DescribeSearch",
                   "iotsitewise:GetSearchResults"
               ],
               "Resource": "<WorkspaceArn>"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "iotsitewise:GetCaptureData"
               ],
               "Resource": [
                   "arn:aws:iotsitewise:<Region>:<AccountId>:time-series/*",
                   "<WorkspaceArn>"
               ]
           }
       ]
   }'
```