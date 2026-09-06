

# Amazon S3 bucket policy for logging
<a name="logging-s3-audit-bucket"></a>

In AWS Control Tower, AWS services have access to your resources only when the request originates from your organization or organizational unit (OU). An `aws:SourceOrgID` condition must be met for any write permissions.

You can use the `aws:SourceOrgID` condition key and set the value to your **organization ID** in the condition element of your Amazon S3 bucket policy. This condition ensures that only accounts within your organization can write logs to your Amazon S3 bucket. It prevents accounts outside your organization from writing logs to your AWS Control Tower Amazon S3 bucket.

For more information about this condition key, see [IAM global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html). For a blog post about scalable controls, see [Use scalable controls for AWS services accessing your resources](https://aws.amazon.com/blogs/security/use-scalable-controls-for-aws-services-accessing-your-resources/).

This policy does not affect the functionality of your existing workloads.

## Landing zone version 3.3 and earlier
<a name="logging-s3-bucket-policy-v33"></a>

In landing zone version 3.3 and earlier, AWS Control Tower deploys a single Amazon S3 bucket in the log archive account that stores both AWS CloudTrail and AWS Config logs. The bucket policy is shown in the following example.

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
            {{Condition:
              StringEquals:
                aws:SourceOrgID: !Ref OrganizationId}}
          - Sid: AWSBucketDeliveryForOrganizationTrail
            Effect: Allow
            Principal:
              Service:
                - cloudtrail.amazonaws.com
            Action: s3:PutObject
            Resource: !If [IsAccountLevelBucketPermissionRequiredForCloudTrail,
                [!Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/${Namespace}/*", !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/${OrganizationId}/*"],
                !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/*/*"]
            {{Condition:
              StringEquals:
                aws:SourceOrgID: !Ref OrganizationId}}
```

## Landing zone version 4.0 and later
<a name="logging-s3-bucket-policy-v40"></a>

In landing zone version 4.0 and later, AWS Config and AWS CloudTrail use separate dedicated Amazon S3 buckets instead of a shared bucket. The Amazon S3 bucket for AWS Config logs is in the AWS Config integration account (formerly the Audit account). The Amazon S3 bucket for AWS CloudTrail logs is in the AWS CloudTrail administrator account (formerly the Log Archive account). For more information, see [AWS Config Updates](config-updates-v4.md).

### AWS CloudTrail bucket policy (AWS CloudTrail administrator account)
<a name="logging-s3-bucket-policy-v40-ct"></a>

The following example shows the AWS CloudTrail bucket policy deployed in the AWS CloudTrail administrator account:

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
            Action: s3:GetBucketAcl
            Resource:
              - !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}"
          - Sid: AWSConfigBucketExistenceCheck
            Effect: Allow
            Principal:
              Service:
                - cloudtrail.amazonaws.com
            Action: s3:ListBucket
            Resource:
              - !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}"
          - Sid: AWSBucketDeliveryForOrganizationTrail
            Effect: Allow
            Principal:
              Service:
                - cloudtrail.amazonaws.com
            Action: s3:PutObject
            Resource: !If [IsAccountLevelBucketPermissionRequiredForCloudTrail,
                           [!Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/${Namespace}/*", !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/${OrganizationId}/*"],
                           !Sub "arn:${AWS::Partition}:s3:::${S3AuditBucket}/${AWSLogsS3KeyPrefix}/AWSLogs/*/*"]
            {{Condition:
              StringEquals:
                aws:SourceOrgID: !Ref OrganizationId}}
```

### AWS Config bucket policy (AWS Config integration account)
<a name="logging-s3-bucket-policy-v40-config"></a>

The following example shows the AWS Config bucket policy deployed in the AWS Config integration account:

```
ConfigS3BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref ConfigS3Bucket
      PolicyDocument:
        Version: 2012-10-17		 	 	 
        Statement:
          - Sid: AllowSSLRequestsOnly
            Effect: Deny
            Principal: '*'
            Action: s3:*
            Resource:
              - !Sub "arn:${AWS::Partition}:s3:::${ConfigS3Bucket}"
              - !Sub "arn:${AWS::Partition}:s3:::${ConfigS3Bucket}/*"
            Condition:
              Bool:
                aws:SecureTransport: false
          - Sid: AWSConfigBucketPermissionsCheck
            Effect: Allow
            Principal:
              Service:
                - config.amazonaws.com
            Action: s3:GetBucketAcl
            Resource:
              - !Sub "arn:${AWS::Partition}:s3:::${ConfigS3Bucket}"
          - Sid: AWSConfigBucketExistenceCheck
            Effect: Allow
            Principal:
              Service:
                - config.amazonaws.com
            Action: s3:ListBucket
            Resource:
              - !Sub "arn:${AWS::Partition}:s3:::${ConfigS3Bucket}"
          - Sid: AWSConfigBucketDelivery
            Effect: Allow
            Principal:
              Service:
                - config.amazonaws.com
            Action: s3:PutObject
            Resource:
              - !Sub "arn:${AWS::Partition}:s3:::${ConfigS3Bucket}/${ConfigS3KeyPrefix}/AWSLogs/*/*"
            {{Condition:
              StringEquals:
                aws:SourceOrgID: !Ref OrganizationId}}
```