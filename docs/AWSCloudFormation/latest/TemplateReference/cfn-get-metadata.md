This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# cfn-get-metadata

You can use the `cfn-get-metadata` helper script to fetch a metadata block
from CloudFormation and print it to standard output. You can also print a sub-tree of the
metadata block if you specify a key. However, only top-level keys are supported.

###### Topics

- [Syntax](#cfn-get-metadata-Syntax "#cfn-get-metadata-Syntax")
- [Options](#cfn-get-metadata-options "#cfn-get-metadata-options")

## Syntax

```
cfn-get-metadata --access-key `access.key` \
                 --secret-key `secret.key` \
                 --credential-file|f `credential.file` \
                 --key|k `key` \
                 --stack|-s `stack.name.or.id` \
                 --resource|-r `logical.resource.id` \
                 --role `IAM.role.name` \
                 --url|-u `service.url` \
                 --region `region`
```

###### Note

`cfn-get-metadata` doesn't require credentials, so you don't need to
use the `--access-key`, `--secret-key`, `--role`, or
`--credential-file` options. However, if no credentials are specified,
CloudFormation checks for stack membership and limits the scope of the call to the stack
that the instance belongs to. For more information, see [Permissions for helper
scripts](cfn-helper-scripts-reference.md#cfn-helper-scripts-reference-permissions "cfn-helper-scripts-reference.md#cfn-helper-scripts-reference-permissions").

## Options

| Name                               | Description                                                                                                                                                                                                          | Required    |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `-k, --key`                        | For a key-value pair, returns the name of the key for the value that you specified. _Type_: String _Example_: For `{ "Key1": "SampleKey1", "Key2": "SampleKey2" }`, `cfn-get-metadata -k Key2` returns `SampleKey2`. | No          |
| `-s, --stack`                      | Name of the Stack. _Type_: String _Default_: None _Example_: `-s { "Ref" : "AWS::StackName" },`                                                                                                                      | Yes         |
| `-r, --resource`                   | The logical resource ID of the resource that contains the metadata. _Type_: String _Example_: `-r WebServerHost`                                                                                                     | Yes         |
| `--role` (resource signaling only) | The name of an IAM role that's associated with the instance. _Type_: String Condition: The credential file parameter supersedes this parameter.                                                                      | No          |
| `--region`                         | The region to derive the CloudFormation URL from. _Type_: String _Default_: None _Example_: `--region ", { "Ref" : "AWS::Region" },`                                                                                 | No          |
| `--access-key`                     | AWS Access Key for an account with permission to call DescribeStackResource on CloudFormation. _Type_: String Condition: The credential file parameter supersedes this parameter.                                    | Conditional |
| `--secret-key`                     | AWS Secret Key that corresponds to the specified AWS Access Key. _Type_: String Condition: The credential file parameter supersedes this parameter.                                                                  | Conditional |
| `-f, --credential-file`            | A file that contains both a secret key and an access key. _Type_: String Condition: The credential file parameter supersedes the --access-key and --secret-key parameters.                                           | Conditional |
