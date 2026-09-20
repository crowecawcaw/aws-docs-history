

# Service roles for AWS HealthOmics
<a name="permissions-service"></a>

A service role is an AWS Identity and Access Management (IAM) role that grants permissions for an AWS service to access resources in your account. You provide a service role to AWS HealthOmics when you start an import job or start a run.

The HealthOmics console can create the required role for you. If you use the HealthOmics API to manage resources, create the service role using the IAM console. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html).

Service roles must have the following trust policy.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "omics.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

The trust policy allows the HealthOmics service to assume the role.

**Topics**
+ [Example IAM service policies](#permissions-service-samplepolicies)
+ [Use session policies to scope down permissions](#permissions-service-sessionpolicy)
+ [Example CloudFormation template](#permissions-service-sampletemplates)

## Example IAM service policies
<a name="permissions-service-samplepolicies"></a>

In these examples, resource names and account IDs are placeholders for you to replace with actual values.

The following example shows the policy for a service role that you can use for starting a run. The policy grants permissions to access the Amazon S3 output location, the workflow log group, and the Amazon ECR container for the run. 

**Note**  
If you're using call caching for the run, add the run cache Amazon S3 location as a resource in the s3 permissions. 

**Example Service role policy for starting a run**    
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement": [
      {
          "Effect": "Allow",
          "Action": [
              "s3:GetObject",
              "s3:PutObject"
          ],
          "Resource": [
              "arn:aws:s3:::{{amzn-s3-demo-bucket1}}/*"
          ]
      },
      {
          "Effect": "Allow",
          "Action": [
              "s3:ListBucket"
          ],
          "Resource": [
              "arn:aws:s3:::{{amzn-s3-demo-bucket1}}"
          ]
      },
      {
          "Effect": "Allow",
          "Action": [
              "logs:DescribeLogStreams",
              "logs:CreateLogStream",
              "logs:PutLogEvents"
          ],
          "Resource": [
              "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/omics/WorkflowLog:log-stream:*"
          ]
      },
      {
          "Effect": "Allow",
          "Action": [
              "logs:CreateLogGroup"
          ],
          "Resource": [
              "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/omics/WorkflowLog:*"
          ]
      },
      {
          "Effect": "Allow",
          "Action": [
              "ecr:BatchGetImage",
              "ecr:GetDownloadUrlForLayer",
              "ecr:BatchCheckLayerAvailability"
          ],
          "Resource": [
              "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/*"
          ]
      }
    ]
}
```

The following example shows the policy for a service role that you can use for a store import job. The policy grants permissions to access the Amazon S3 input location .

**Example Service role for Reference store job**    
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ]
        },

        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
            ]
        }

    ]
}
```

The following example shows the policy for a service role that publishes run metrics to CloudWatch. For more information, see [Run metrics for Private Workflows](monitoring-run-metrics.md).

**Example Service role policy for run metrics**  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*"
    }
  ]
}
```

## Use session policies to scope down permissions
<a name="permissions-service-sessionpolicy"></a>

You can use session policies to further restrict the permissions granted by a service role for individual workflow runs. Session policies are inline IAM policies that you provide when starting a run. The effective permissions for the run are the intersection of the service role's permissions and the session policy.

Session policies are useful when you want to:
+ Grant temporary access to specific Amazon S3 buckets or objects for a single run
+ Restrict access to sensitive resources on a per-run basis
+ Apply additional security controls without modifying the service role

**Important**  
Session policies can only restrict permissions; they cannot grant permissions beyond what the service role already allows. The session policy must include permissions for Amazon CloudWatch Logs (`logs:CreateLogStream` and `logs:PutLogEvents`) because HealthOmics uses the run's credentials to create and write to log groups.

Session policies have a maximum length of 2,048 characters and must be valid JSON documents. For more information about session policies, see [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the *IAM User Guide*.

**Example Session policy for a workflow run**  
The following example shows a session policy that restricts a run to access only a specific Amazon S3 prefix for output and requires CloudWatch Logs permissions:  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/workflow-outputs/run-123/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:log-group:/aws/omics/WorkflowLog:*"
    }
  ]
}
```

You can specify a session policy when starting a run using the HealthOmics API. The `StartRun` API includes a `sessionPolicy` parameter where you provide the inline policy as a JSON string. For batch runs, you can specify a session policy in the `DefaultRunSetting` that applies to all runs in the batch.

## Example CloudFormation template
<a name="permissions-service-sampletemplates"></a>

The following sample CloudFormation template creates a service role that gives HealthOmics permission to access Amazon S3 buckets that have names prefixed with `omics-`, and to upload workflow logs.

**Example Reference store, Amazon S3 and CloudWatch Logs permissions**  

```
Parameters:
  bucketName:
    Description: Bucket name
    Type: String
    
Resources:
  serviceRole:
    Type: AWS::IAM::Role
    Properties:
      Policies:
        - PolicyName: read-reference
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Effect: Allow
              Action:
                - omics:*
              Resource: !Sub arn:${AWS::Partition}:omics:${AWS::Region}:${AWS::AccountId}:referenceStore/*
        - PolicyName: read-s3
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Effect: Allow
              Action: 
                - s3:ListBucket
              Resource: !Sub arn:${AWS::Partition}:s3:::${bucketName}
            - Effect: Allow
              Action:
                - s3:GetObject
                - s3:PutObject
              Resource: !Sub arn:${AWS::Partition}:s3:::${bucketName}/*
        - PolicyName: upload-logs
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Effect: Allow
              Action: 
                - logs:DescribeLogStreams
                - logs:CreateLogStream
                - logs:PutLogEvents
              Resource: !Sub arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:loggroup:/aws/omics/WorkflowLog:log-stream:*
            - Effect: Allow
              Action: 
                - logs:CreateLogGroup
              Resource: !Sub arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:loggroup:/aws/omics/WorkflowLog:*
      AssumeRolePolicyDocument: |
        {
          "Version": "2012-10-17",		 	 	 
          "Statement": [
            {
              "Action": [
                "sts:AssumeRole"
              ],
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "omics.amazonaws.com"
                ]
              }
            }
          ]
        }
```