# Upload local artifacts to an S3 bucket with the

AWS CLI

You can use the AWS CLI to upload local artifacts that are referenced by a CloudFormation template
to an Amazon S3 bucket. Local artifacts are files that you reference in your template. Instead of
manually uploading files to an S3 bucket and then adding their locations to your template, you
can specify local artifacts in your template and use the [package](../../../cli/latest/reference/cloudformation/package.md "../../../cli/latest/reference/cloudformation/package.md") command to
upload them quickly.

A local artifact is a path to a file or folder that the **package** command
uploads to Amazon S3. For example, an artifact can be a local path to your AWS Lambda function's
source code or an Amazon API Gateway REST API's OpenAPI file.

When using the **package** command:

- If you specify a file, the command directly uploads it to the S3 bucket.
- If you specify a folder, the command creates a `.zip` file for the
  folder, and then uploads the `.zip` file.
- If you don't specify a path, the command creates a `.zip` file for
  the working directory and uploads it.
  You can specify an absolute or relative path, where the relative path is relative to your
  template's location.

After uploading the artifacts, the command returns a copy of your template, replacing
references to local artifacts with the S3 location where the command uploaded the artifacts. You
can then use the returned template to create or update a stack.

###### Note

You can use local artifacts only for resource properties that the
**package** command supports. For more information about this command and a
list of the supported resource properties, see the [package](../../../cli/latest/reference/cloudformation/package.md "../../../cli/latest/reference/cloudformation/package.md") documentation
in the [AWS CLI Command Reference](../../../cli/latest/reference/cloudformation/index.md "../../../cli/latest/reference/cloudformation/index.md").

## Prerequisites

Before you begin, you must have an existing Amazon S3 bucket.

## Package and deploy a

template with local artifacts

The following template specifies the local artifact for a Lambda function's source code.
The source code is stored in the `/home/user/code/lambdafunction` folder.

**Original template**

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::Serverless-2016-10-31",
  "Resources": {
    "MyFunction": {
      "Type": "AWS::Serverless::Function",
      "Properties": {
        "Handler": "index.handler",
        "Runtime": "nodejs18.x",
        "CodeUri": "/home/user/code/lambdafunction"
      }
    }
  }
}
```

The following [package](../../../cli/latest/reference/cloudformation/package.md "../../../cli/latest/reference/cloudformation/package.md") command creates and uploads a `.zip` file
of the function's source code folder to the root of the specified bucket.

```
aws cloudformation package \
  --s3-bucket `amzn-s3-demo-bucket` \
  --template `/path_to_template/template.json` \
  --output-template-file `packaged-template.json` \
  --output json
```

The command generates a new template at the path specified by
`--output-template-file`. It replaces the artifact reference with the Amazon S3
location, as shown below. The `.zip` file is named using the MD5 checksum
of the folder contents, rather than using the folder name itself.

**Resulting template**

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::Serverless-2016-10-31",
  "Resources": {
    "MyFunction": {
      "Type": "AWS::Serverless::Function",
      "Properties": {
        "Handler": "index.handler",
        "Runtime": "nodejs18.x",
        "CodeUri": "s3://`amzn-s3-demo-bucket`/`md5 checksum`"
      }
    }
  }
}
```

After you package your template’s artifacts, deploy the processed template using the
[deploy](../../../cli/latest/reference/cloudformation/deploy.md "../../../cli/latest/reference/cloudformation/deploy.md")
command.

```
aws cloudformation deploy \
  --template-file `packaged-template.json` \
  --stack-name `stack-name`
```

When deploying templates larger than 51,200 bytes, use the **deploy**
command with the `--s3-bucket` option to upload your template to S3, as in the
following
example.

```
aws cloudformation deploy \
  --template-file `packaged-template.json` \
  --stack-name `stack-name` \
  --s3-bucket `amzn-s3-demo-bucket`
```

###### Note

For another example of using the **package** command to upload local
artifacts, see [Split a template into reusable pieces using nested
stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md").
