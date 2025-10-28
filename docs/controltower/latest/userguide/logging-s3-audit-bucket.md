# Amazon S3 bucket policy in the audit account

In AWS Control Tower, AWS services have access to your resources only when the request originates
from your organization or organizational unit (OU). An `aws:SourceOrgID` condition
must be met for any write permissions.

You can use the `aws:SourceOrgID` condition key and set the value to your
**organization ID** in the condition element of your Amazon S3 bucket policy.
This condition ensures that CloudTrail only can write logs on behalf of accounts within your
organization to your S3 bucket; it prevents CloudTrail logs outside your organization from writing
to your AWS Control Tower S3 bucket.

This policy does not affect the functionality of your existing workloads. The policy is
shown in the example that follows.

```
S3AuditBucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref S3AuditBucket
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Sid: AllowSSLRequestsOnly
            Effect: Deny
            Principal: '*'
            Action: s3:*
            Resource:
             - !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}"
             - !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/*"
            Condition:
              Bool:
                aws:SecureTransport: false
          - Sid: AWSBucketPermissionsCheck
            Effect: Allow
            Principal:
              Service:
                - cloudtrail.amazonaws.com
                - config.amazonaws.com
            Action: s3:GetBucketAcl
            Resource:
              - !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}"
          - Sid: AWSConfigBucketExistenceCheck
            Effect: Allow
            Principal:
              Service:
                - cloudtrail.amazonaws.com
                - config.amazonaws.com
            Action: s3:ListBucket
            Resource:
              - !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}"
          - Sid: AWSBucketDeliveryForConfig
            Effect: Allow
            Principal:
              Service:
                - config.amazonaws.com
            Action: s3:PutObject
            Resource:
              - Fn::Join:
                  - ""
                  -
                    - !Sub "arn:${AWS::Partition}:s3:::"
                    - !Ref "S3AuditBucket"
                    - !Sub "/${AWSLogsS3KeyPrefix}/AWSLogs/*/*"
            `Condition:
 StringEquals:
 aws:SourceOrgID: !Ref OrganizationId`
          - Sid: AWSBucketDeliveryForOrganizationTrail
            Effect: Allow
            Principal:
              Service:
                - cloudtrail.amazonaws.com
            Action: s3:PutObject
            Resource: !If [IsAccountLevelBucketPermissionRequiredForCloudTrail,
                [!Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/${Namespace}/*", !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/${OrganizationId}/*"],
                !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/*/*"]
            `Condition:
 StringEquals:
 aws:SourceOrgID: !Ref OrganizationId`
```

For more information about this condition key, see the IAM documentation and the IAM
blog post entitled "_Use scalable controls for AWS services accessing your
resources_."
