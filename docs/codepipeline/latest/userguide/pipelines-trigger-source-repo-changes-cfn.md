# Create an EventBridge rule for

a CodeCommit source (CloudFormation template)

To use CloudFormation to create a rule, update your template as shown here.

###### To update your pipeline CloudFormation template and create EventBridge

rule

1.  In the template, under `Resources`, use the `AWS::IAM::Role` CloudFormation
    resource to configure the IAM role that allows your event to start your pipeline. This entry
    creates a role that uses two policies:

        * The first policy allows the role to be assumed.
        * The second policy provides permissions to start the pipeline.

    **Why am I making this change?** Adding the
    `AWS::IAM::Role` resource enables CloudFormation to create permissions for EventBridge. This
    resource is added to your CloudFormation stack.

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
                Resource: !Join [ '', [ 'arn:aws:codepipeline:', !Ref 'AWS::Region', ':', !Ref 'AWS::AccountId', ':', !Ref AppPipeline ] ]
```

JSON

```
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
                "Fn::Join": [
                  "",
                  [
                    "arn:aws:codepipeline:",
                    {
                      "Ref": "AWS::Region"
                    },
                    ":",
                    {
                      "Ref": "AWS::AccountId"
                    },
                    ":",
                    {
                      "Ref": "AppPipeline"
                    }
                  ]

...
```

2. In the template, under `Resources`, use the `AWS::Events::Rule`
   CloudFormation resource to add an EventBridge rule. This event pattern creates an event that monitors push
   changes to your repository. When EventBridge detects a repository state change, the rule invokes
   `StartPipelineExecution` on your target pipeline.

**Why am I making this change?** Adding the
`AWS::Events::Rule` resource enables CloudFormation to create the event. This resource is
added to your CloudFormation stack.

YAML

```
  EventRule:
    Type: AWS::Events::Rule
    Properties:
      EventPattern:
        source:
          - aws.codecommit
        detail-type:
          - 'CodeCommit Repository State Change'
        resources:
          - !Join [ '', [ 'arn:aws:codecommit:', !Ref 'AWS::Region', ':', !Ref 'AWS::AccountId', ':', !Ref RepositoryName ] ]
        detail:
          event:
            - referenceCreated
            - referenceUpdated
          referenceType:
            - branch
          referenceName:
            - main
      Targets:
        -
          Arn:
            !Join [ '', [ 'arn:aws:codepipeline:', !Ref 'AWS::Region', ':', !Ref 'AWS::AccountId', ':', !Ref AppPipeline ] ]
          RoleArn: !GetAtt EventRole.Arn
          Id: codepipeline-AppPipeline
```

JSON

```

"EventRule": {
  "Type": "AWS::Events::Rule",
  "Properties": {
    "EventPattern": {
      "source": [
        "aws.codecommit"
      ],
      "detail-type": [
        "CodeCommit Repository State Change"
      ],
      "resources": [
        {
          "Fn::Join": [
            "",
            [
              "arn:aws:codecommit:",
              {
                "Ref": "AWS::Region"
              },
              ":",
              {
                "Ref": "AWS::AccountId"
              },
              ":",
              {
                "Ref": "RepositoryName"
              }
            ]
          ]
        }
      ],
      "detail": {
        "event": [
          "referenceCreated",
          "referenceUpdated"
        ],
        "referenceType": [
          "branch"
        ],
        "referenceName": [
          "main"
        ]
      }
    },
    "Targets": [
      {
        "Arn": {
          "Fn::Join": [
            "",
            [
              "arn:aws:codepipeline:",
              {
                "Ref": "AWS::Region"
              },
              ":",
              {
                "Ref": "AWS::AccountId"
              },
              ":",
              {
                "Ref": "AppPipeline"
              }
            ]
          ]
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
},
```

3. (Optional) To configure an input transformer with source overrides for a specific image
   ID, use the following YAML snippet. The following example configures an override where:
   - The `actionName`, `Source` in this example, is the dynamic
     value, defined at pipeline creation, not derived from the source event.
   - The `revisionType`, `COMMIT_ID` in this example, is the dynamic
     value, defined at pipeline creation, not derived from the source event.
   - The `revisionValue`, <`revisionValue`> in this
     example, is derived from the source event variable.
   - The output variables for `BranchName` and `Value` are
     specified.

```

Rule: my-rule
Targets:
- Id: MyTargetId
  Arn: pipeline-ARN
  InputTransformer:
    sourceRevisions:
      actionName: `Source`
      revisionType: `COMMIT_ID`
      revisionValue: <`revisionValue`>
    variables:
    - name: `BranchName`
      value: `value`
```

4. Save the updated template to your local computer, and then open the CloudFormation console.
5. Choose your stack, and then choose **Create Change Set for Current
   Stack**.
6. Upload the template, and then view the changes listed in CloudFormation. These are the changes to
   be made to the stack. You should see your new resources in the list.
7. Choose **Execute**.

###### To edit your pipeline's PollForSourceChanges

parameter

###### Important

In many cases, the `PollForSourceChanges` parameter defaults to true when
you create a pipeline. When you add event-based change detection, you must add the
parameter to your output and set it to false to disable polling. Otherwise, your
pipeline starts twice for a single source change. For details, see [Valid settings for the
PollForSourceChanges parameter](PollForSourceChanges-defaults.md "PollForSourceChanges-defaults.md").

- In the template, change `PollForSourceChanges` to `false`. If
  you did not include `PollForSourceChanges` in your pipeline definition, add
  it and set it to `false`.

**Why am I making this change?** Changing this parameter
to `false` turns off periodic checks so you can use event-based change
detection only.

YAML

```
          Name: Source
          Actions:
            -
              Name: SourceAction
              ActionTypeId:
                Category: Source
                Owner: AWS
                Version: 1
                Provider: CodeCommit
              OutputArtifacts:
                - Name: SourceOutput
              Configuration:
                BranchName: !Ref BranchName
                RepositoryName: !Ref RepositoryName
                `PollForSourceChanges: *false*`
              RunOrder: 1
```

JSON

```
{
  "Name": "Source",
  "Actions": [
    {
      "Name": "SourceAction",
      "ActionTypeId": {
        "Category": "Source",
        "Owner": "AWS",
        "Version": 1,
        "Provider": "CodeCommit"
      },
      "OutputArtifacts": [
        {
          "Name": "SourceOutput"
        }
      ],
      "Configuration": {
        "BranchName": {
          "Ref": "BranchName"
        },
        "RepositoryName": {
          "Ref": "RepositoryName"
        },
        "PollForSourceChanges": `*false*`
      },
      "RunOrder": 1
    }
  ]
},

```
