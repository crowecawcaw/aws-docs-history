This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# Transform reference

Transforms are macros hosted by CloudFormation. Unlike custom macros, a transform doesn't
require any special permissions to use it because it is hosted by CloudFormation. Transforms can
be used in templates in any account within CloudFormation. Also, there is no charge incurred
when using transforms. CloudFormation treats a transform the same as any other macro in terms of
evaluation order and scope.

For more information about how macros work, see [Using CloudFormation macros to perform custom
processing on templates](../UserGuide/template-macros.md "../UserGuide/template-macros.md") in the _AWS CloudFormation User Guide_.

You can use the following transforms in your CloudFormation templates.

###### Topics

- [AWS::CodeDeployBlueGreen
  transform](transform-aws-codedeploybluegreen.md "transform-aws-codedeploybluegreen.md")
- [AWS::Include transform](transform-aws-include.md "transform-aws-include.md")
- [AWS::LanguageExtensions
  transform](transform-aws-languageextensions.md "transform-aws-languageextensions.md")
- [AWS::SecretsManager
  transform](transform-aws-secretsmanager.md "transform-aws-secretsmanager.md")
- [AWS::Serverless transform](transform-aws-serverless.md "transform-aws-serverless.md")
- [AWS::ServiceCatalog
  transform](transform-aws-servicecatalog.md "transform-aws-servicecatalog.md")
