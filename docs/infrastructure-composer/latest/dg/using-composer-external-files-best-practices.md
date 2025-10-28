# Best

practices for Infrastructure Composer external reference files

## Use

Infrastructure Composer with a local IDE

When you use Infrastructure Composer with a local IDE in **local
sync** mode, you can use your local IDE to view and modify
external files. Content from supported external files that are
referenced on your template will automatically update in the Infrastructure Composer
canvas. To learn more, see [Connect the Infrastructure Composer console with your local IDE](other-services-ide.md "other-services-ide.md").

## Keep external files within your project’s parent directory

You can create subdirectories within your project’s parent directory
to organize your external files. Infrastructure Composer can’t access external files that
are stored in a directory outside of your project’s parent
directory.

## Deploy your application using the AWS SAM CLI

When deploying your application to the AWS Cloud, local external
files need to first be uploaded to an accessible location, such as
Amazon Simple Storage Service (Amazon S3). You can use the AWS SAM CLI to automatically facilitate
this process. To learn more, see [Upload local files at deployment](../../../serverless-application-model/latest/developerguide/deploy-upload-local-files.md "../../../serverless-application-model/latest/developerguide/deploy-upload-local-files.md") in the
_AWS Serverless Application Model Developer Guide_.
