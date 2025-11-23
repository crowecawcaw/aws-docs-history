# Deploy the AWS SAM application

Use the AWS SAM **sam deploy** command with the
`package.yml` file to create your Lambda functions and CodeDeploy application
and deployment group using CloudFormation.

###### Note

For more information on the **sam deploy** command, see [AWS SAM CLI command reference](../../../serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.md "../../../serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.md") in the _AWS Serverless Application Model Developer Guide_.

In the `SAM-Tutorial` directory, run the following command.

```
sam deploy \
  --template-file package.yml \
  --stack-name my-date-time-app \
  --capabilities CAPABILITY_IAM
```

The `--capabilities CAPABILITY_IAM` parameter is required to authorize CloudFormation
to create IAM roles.
