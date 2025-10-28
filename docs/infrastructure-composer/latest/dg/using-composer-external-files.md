# Reference external files in Infrastructure Composer

You can use external files with your AWS Serverless Application Model (AWS SAM) templates to
reuse repeated code and organize your projects. For example, you may have
multiple Amazon API Gateway REST API resources that are described by an
OpenAPI specification. Instead of replicating the
OpenAPI specification code in your template, you can create
one external file and reference it for each of your resources.

AWS Infrastructure Composer supports the following external file use cases:

- API Gateway REST API resources defined by external
  OpenAPI specification files.
- AWS Step Functions state machine resources defined by external state machine
  definition files.
  To learn more about configuring external files for supported resources,
  see the following:

- `DefinitionBody` for
  `AWS::Serverless::Api`.
- `DefinitionUri` for
  `AWS::Serverless::StateMachine`.

###### Note

To reference external files with Infrastructure Composer from the Infrastructure Composer console, you must use Infrastructure Composer in **local sync** mode. For more information, see [Locally sync and save your
project in the Infrastructure Composer console](using-composer-project-local-sync.md "using-composer-project-local-sync.md").

###### Topics

- [Best
  practices for Infrastructure Composer external reference files](using-composer-external-files-best-practices.md "using-composer-external-files-best-practices.md")
- [Create an external
  file reference in Infrastructure Composer](using-composer-external-files-new.md "using-composer-external-files-new.md")
- [Load a project with an external file reference in Infrastructure Composer](using-composer-external-files-load.md "using-composer-external-files-load.md")
- [Create an application that references an external file in
  Infrastructure Composer](using-composer-external-files-examples-example3.md "using-composer-external-files-examples-example3.md")
- [Reference an OpenAPI specification external
  file with Infrastructure Composer](using-composer-external-files-examples-example1.md "using-composer-external-files-examples-example1.md")
