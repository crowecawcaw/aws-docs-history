# AWS CloudFormation artifacts

CodePipeline performs tasks on artifacts as CodePipeline runs a pipeline. For AWS CloudFormation, artifacts can include
 a stack template file, a template configuration file, or both. CodePipeline uses these artifacts to
 work with AWS CloudFormation stacks and change sets.

If you use Amazon Simple Storage Service (Amazon S3) as a source repository, you must zip the template and template
 configuration files into a single file before you upload them to an S3 bucket. For other
 repositories, such as GitHub and AWS CodeCommit, upload artifacts without zipping them. For more
 information, see [Create a pipeline, stages, and actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html "https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html") in the *AWS CodePipeline User Guide*.

You can add as many files as you need to your repository. For example, you might want to
 include two different configurations for the same template: one for a test configuration and
 another for a production configuration.

This topic describes each artifact type.

###### Topics

* [Stack template file](#w71aac21c15c13 "#w71aac21c15c13")
* [Template configuration file](#w71aac21c15c15 "#w71aac21c15c15")
* [See also](#w71aac21c15c17 "#w71aac21c15c17")

## Stack template file


A stack template file defines the resources that AWS CloudFormation provisions and configures. These
 files are the same template files that you use when you create or update stacks using AWS CloudFormation.
 You can use YAML or JSON-formatted templates. For more information about templates, see [CloudFormation template sections](template-anatomy.md "template-anatomy.md").


## Template configuration file


A template configuration file is a JSON-formatted text file that can specify template
 parameter values, a [stack policy](protect-stack-resources.md "protect-stack-resources.md"), and tags. Use
 these configuration files to specify parameter values or a stack policy for a stack. All of
 the parameter values that you specify must be declared in the associated template.


If you include sensitive information—such as passwords—in this file,
 restrict access to it. For example, if you upload your artifact to an S3 bucket, use [S3 bucket policies or user policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-management.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-management.html") to
 restrict access.


To create a configuration file, use the following format :



```
{
  "Parameters" : {
    "`NameOfTemplateParameter`" : "`ValueOfParameter`",
    ...
  },
  "Tags" : {
    "`TagKey`" : "`TagValue`",
    ...
  }, 
  "StackPolicy" : {
    "Statement" : [
      `StackPolicyStatement`
    ]
  }
}
```

The following example specifies `TestEC2Key` for the `KeyName`
 parameter, adds a `Department` tag whose value is `Marketing`, and adds
 a stack policy that allows all update actions except for an update that deletes a
 resource.



```
{
  "Parameters" : {
    "KeyName" : "TestEC2Key"
  },
  "Tags" : {
    "Department" : "Marketing"
  },
  "StackPolicy" : {
    "Statement" : [
      {
        "Effect" : "Allow",
        "NotAction" : "Update:Delete",
        "Principal": "*",
        "Resource" : "*"
      }
    ]
  }
}
```

## See also


The following related resources can help you as you work with these parameters.



* For more information about the CloudFormation action parameters in CodePipeline, see the [AWS CloudFormation deploy
 action configuration reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CloudFormation.html "https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CloudFormation.html") in the
 *AWS CodePipeline User Guide*.
* For example template values by action provider, such as for the `Owner`
 field or the `configuration` fields, see the [Action structure
 reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html "https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html") in the *AWS CodePipeline User Guide*.
* To download example pipeline stack templates in YAML or JSON format, see [Tutorial: Create a
 pipeline with AWS CloudFormation](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-cloudformation.html "https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-cloudformation.html") in the *AWS CodePipeline User Guide*.
