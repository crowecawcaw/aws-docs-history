# Configuring user background sessions for EMR Serverless

###### Warning

When user background sessions is enabled for EMR Serverless, Amazon SageMaker Unified Studio will not terminate interactive sessions.
All interactive sessions will be only terminated once all queries are completed.

User background sessions for your EMR Serverless applications must be enabled manually.
To enable user background sessions, perform the following action using your EMR Serverless application.

```
aws emr-serverless update-application \
  --region `{aws-region-code}` \
  --application-id `{application-id}` \
  --identity-center-configuration userBackgroundSessionsEnabled=true
```

For more information, see [User background sessions](../../../emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop-user-background.md "../../../emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop-user-background.md")
in the EMR Serverless management guide.
