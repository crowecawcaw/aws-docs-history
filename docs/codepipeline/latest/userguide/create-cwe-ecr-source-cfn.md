# Create an EventBridge rule for an Amazon ECR source

(CloudFormation template)

To use CloudFormation to create a rule, use the template snippet as shown here.

###### To update your pipeline CloudFormation template and create EventBridge rule

1.  In the template, under `Resources`, use the
    `AWS::IAM::Role` CloudFormation resource to configure the IAM role
    that allows your event to start your pipeline. This entry creates a role
    that uses two policies:

        * The first policy allows the role to be assumed.
        * The second policy provides permissions to start the
         pipeline.

    **Why am I making this change?** You must
    create a role that can be assumed by EventBridge to start an execution in our
    pipeline.

YAML

```
  EventRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          -
            Effect: Allow
            Principal:
              Service:
                - events.amazonaws.com
            Action: sts:AssumeRole
      Path: /
      Policies:
        -
          PolicyName: eb-pipeline-execution
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              -
                Effect: Allow
                Action: codepipeline:StartPipelineExecution
                Resource: !Sub arn:aws:codepipeline:${AWS::Region}:${AWS::AccountId}:${AppPipeline}
```

JSON

```
{
    "EventRole": {
        "Type": "AWS::IAM::Role",
        "Properties": {
            "AssumeRolePolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": [
                                "events.amazonaws.com"
                            ]
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            },
            "Path": "/",
            "Policies": [
                {
                    "PolicyName": "eb-pipeline-execution",
                    "PolicyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": "codepipeline:StartPipelineExecution",
                                "Resource": {
                                    "Fn::Sub": "arn:aws:codepipeline:${AWS::Region}:${AWS::AccountId}:${AppPipeline}"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
}
...
```

2. In the template, under `Resources`, use the
   `AWS::Events::Rule` CloudFormation resource to add an EventBridge rule for
   the Amazon ECR source. This event pattern creates an event that monitors commits
   to your repository. When EventBridge detects a repository state change, the rule
   invokes `StartPipelineExecution` on your target pipeline.

**Why am I making this change?** You must
create an event with a rule that specifies how an image push must be made,
and a target that names the pipeline to be started by the event.

This snippet uses an image named `eb-test` with a tag of
`latest`.

YAML

```

EventRule:
  Type: 'AWS::Events::Rule'
  Properties:
    EventPattern:
      detail:
        action-type: [PUSH]
        image-tag: [latest]
        repository-name: [eb-test]
        result: [SUCCESS]
      detail-type: [ECR Image Action]
      source: [aws.ecr]
    Targets:
      - Arn: !Sub arn:aws:codepipeline:${AWS::Region}:${AWS::AccountId}:${AppPipeline}
        RoleArn: !GetAtt
          - EventRole
          - Arn
        Id: codepipeline-AppPipeline
```

JSON

```
{
    "EventRule": {
        "Type": "AWS::Events::Rule",
        "Properties": {
            "EventPattern": {
                "detail": {
                    "action-type": [
                        "PUSH"
                    ],
                    "image-tag": [
                        "latest"
                    ],
                    "repository-name": [
                        "eb-test"
                    ],
                    "result": [
                        "SUCCESS"
                    ]
                },
                "detail-type": [
                    "ECR Image Action"
                ],
                "source": [
                    "aws.ecr"
                ]
            },
            "Targets": [
                {
                    "Arn": {
                        "Fn::Sub": "arn:aws:codepipeline:${AWS::Region}:${AWS::AccountId}:${AppPipeline}"
                    },
                    "RoleArn": {
                        "Fn::GetAtt": [
                            "EventRole",
                            "Arn"
                        ]
                    },
                    "Id": "codepipeline-AppPipeline"
                }
            ]
        }
    }
},
```

###### Note

To view the full event pattern supported for Amazon ECR events, see [Amazon ECR Events and
EventBridge](../../../AmazonECR/latest/userguide/ecr-eventbridge.md "../../../AmazonECR/latest/userguide/ecr-eventbridge.md") or [Amazon Elastic Container Registry
Events](../../../eventbridge/latest/userguide/event-types.md#ecr-event-types "../../../eventbridge/latest/userguide/event-types.md#ecr-event-types"). 3. (Optional) To configure an input transformer with source overrides for a
specific image ID, use the following YAML snippet. The following example
configures an override where:

    * The `actionName`, `Source` in this example,
     is the dynamic value, defined at pipeline creation, not derived from
     the source event.
    * The `revisionType`, `IMAGE_DIGEST` in this
     example, is the dynamic value, defined at pipeline creation, not
     derived from the source event.
    * The `revisionValue`,
     <`revisionValue`> in this example,
     is derived from the source event variable.

```
---
Rule: my-rule
Targets:
- Id: MyTargetId
  Arn: ARN
  InputTransformer:
    InputPathsMap:
      revisionValue: "$.detail.image-digest"
    InputTemplate:
      sourceRevisions:
        actionName: `Source`
        revisionType: `IMAGE_DIGEST`
        revisionValue: '<`revisionValue`>'

```

4. Save the updated template to your local computer, and then open the CloudFormation
   console.
5. Choose your stack, and then choose **Create Change Set for Current
   Stack**.
6. Upload the template, and then view the changes listed in CloudFormation. These are
   the changes to be made to the stack. You should see your new resources in
   the list.
7. Choose **Execute**.
