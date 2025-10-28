# Package the AWS SAM application

You should now have four files in your `SAM-Tutorial` directory:

- `beforeAllowTraffic.js`
- `afterAllowTraffic.js`
- `myDateTimeFunction.js`
- `template.yml`
  You are now ready to use the AWS SAM **sam package** command to
  create and package artifacts for your Lambda functions and CodeDeploy application. The artifacts
  are uploaded to an S3 bucket. The output of the command is a new file called
  `package.yml`. This file is used by the AWS SAM **sam
  deploy** command in the next step.

###### Note

For more information on the **sam package** command, see [AWS SAM CLI command reference](../../../serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.md "../../../serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.md") in the _AWS Serverless Application Model Developer Guide_.

In the `SAM-Tutorial` directory, run the following.

```
sam package \
  --template-file template.yml \
  --output-template-file package.yml \
  --s3-bucket `amzn-s3-demo-bucket`
```

For the `s3-bucket` parameter, specify the Amazon S3 bucket you created as a
prerequisite for this tutorial. The `output-template-file` specifies the
name of the new file that is used by the AWS SAM **sam deploy**
command.
