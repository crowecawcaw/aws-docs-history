# Custom notification for Config rules

There can be occurrences of critical non-compliant Config Rules that require raising escalated awareness directly with the
your InfoSec and Leadership teams. For such scenarios, AMS recommends that you configure a non-compliance event-driven custom notification.

For example:

```
ConfigRuleName: required-tags
      Description: >-
        A Config rule that checks whether EC2 instances have the mandated tags.
      Scope:
        ComplianceResourceTypes:
          - 'AWS::EC2::Instance'
      InputParameters:
        tag1Key: COST_CENTER
        tag2Key: APP_ID
      Source:
        Owner: AWS
        SourceIdentifier: REQUIRED_TAGS
  NotificationEventRule:
    Type: 'AWS::Events::Rule'
    Properties:
      Name: CWEventForrequired-tags
      Description: >-
        SNS Notification for Non-Compliant Events of Config Rule:
        required-tags
      State: ENABLED
      EventPattern:
        detail-type:
          - Config Rules Compliance Change
        source:
          - aws.config
        detail:
          newEvaluationResult:
            complianceType:
              - NON_COMPLIANT
          configRuleARN:
            - 'Fn::GetAtt':
                - RequiredEC2Tags
                - Arn
      Targets:
        - Id: RemediationNotification
          Arn:
            Ref: SnsTopic
          InputTransformer:
            InputTemplate: >-
              "EC2 Instance <Instance_ID> is non-compliant. Please add required tags: COST_CENTER, APP_ID, Name, and Backup."
            InputPathsMap:
              instance_id: $.detail.resourceId
  SnsTopic:
    Type: 'AWS::SNS::Topic'
    Properties:
      Subscription:
        - Endpoint: Cloud_Ops_Leaders@customer.com
          Protocol: email
      TopicName: noncompliant-instance-notification
  SnsTopicPolicy:
    Type: 'AWS::SNS::TopicPolicy'
    Properties:
      PolicyDocument:
        Statement:
          - Sid: __default_statement_ID
            Effect: Allow
            Principal:
              AWS: '*'
            Action:
              - 'SNS:GetTopicAttributes'
              - 'SNS:SetTopicAttributes'
              - 'SNS:AddPermission'
              - 'SNS:RemovePermission'
              - 'SNS:DeleteTopic'
              - 'SNS:Subscribe'
              - 'SNS:ListSubscriptionsByTopic'
              - 'SNS:Publish'
              - 'SNS:Receive'
            Resource:
              Ref: SnsTopic
            Condition:
              StringEquals:
                'AWS:SourceOwner':
                  Ref: 'AWS::AccountId'
          - Sid: TrustCWEToPublishEventsToMyTopic
            Effect: Allow
            Principal:
              Service: events.amazonaws.com
            Action: 'sns:Publish'
            Resource:
              Ref: SnsTopic
      Topics:
        - Ref: SnsTopic
```
