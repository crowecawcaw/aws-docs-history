This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `AWS::CloudFormation::Authentication`

Use the `AWS::CloudFormation::Authentication` metadata type to specify
authentication credentials for files or sources that you specify with the [AWS::CloudFormation::Init](aws-resource-init.md "aws-resource-init.md") metadata type.

To include authentication information for a file or source that you specify with
`AWS::CloudFormation::Init`, use the `uris` property if the source is
a URI or the `buckets` property if the source is an Amazon S3 bucket. For more
information about files, see [Files](aws-resource-init.md#aws-resource-init-files "aws-resource-init.md#aws-resource-init-files"). For more information about sources, see [Sources](aws-resource-init.md#aws-resource-init-sources "aws-resource-init.md#aws-resource-init-sources").

You can also specify authentication information for files directly in the
`AWS::CloudFormation::Init` metadata type. The files key of the resource
contains a property named `authentication`. You can use the
`authentication` property to associate authentication information defined in the
`AWS::CloudFormation::Authentication` metadata type directly with a file.

For files, AWS CloudFormation looks for authentication information in the following order:

1. The `authentication` property of the
   `AWS::CloudFormation::Init`
   `files` key.
2. The `uris` or `buckets` property of the
   `AWS::CloudFormation::Authentication` metadata.
   For sources, CloudFormation looks for authentication information in the `uris` or
   `buckets` property of the `AWS::CloudFormation::Authentication`
   metadata.

###### Topics

- [Syntax](#aws-resource-cloudformation-authentication-syntax "#aws-resource-cloudformation-authentication-syntax")
- [Properties](#w2294aac19c23c15c19 "#w2294aac19c23c15c19")
- [Examples](#aws-resource-authentication-examples "#aws-resource-authentication-examples")

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

Be aware of the following considerations when using the
`AWS::CloudFormation::Authentication` metadata type:

- Unlike most CloudFormation resources, the
  `AWS::CloudFormation::Authentication` metadata type doesn't contain a
  block called _Properties_, but instead contains a list of
  user-named blocks, each containing its own authentication properties.

Not all properties pertain to each authentication type. For more information, see
the [type](#cfn-cloudformation-authentication-type "#cfn-cloudformation-authentication-type")
property.

- Unlike most CloudFormation resources, `AWS::CloudFormation::Authentication`
  property names use lower camel case.

### JSON

```
{
  "AWS::CloudFormation::Authentication" {
    "`String`" : {
      "accessKeyId" : `String`,
      "buckets" : [ `String, ...` ],
      "password" : `String`,
      "secretKey" : `String`,
      "type" : `String`,
      "uris" : [ `String, ...` ],
      "username" : `String`,
      "roleName" : `String`
    }
  }
}
```

### YAML

```
AWS::CloudFormation::Authentication
`String`:
  accessKeyId: `String`
  buckets:
    - `String`
  password: `String`
  secretKey: `String`
  type: `String`
  uris:
    - `String`
  username: `String`
  roleName: `String`
```

## Properties

`accessKeyId`

Specifies the access key ID for S3 authentication.

_Required_: Conditional. Can be specified only if the `type` property
is set to `S3`.

_Type_: String

`buckets`

A comma-delimited list of Amazon S3 buckets to be associated with the S3
authentication credentials.

_Required_: Conditional. Can be specified only if the `type` property
is set to `S3`.

_Type_: List of String values

`password`

Specifies the password for basic authentication.

_Required_: Conditional. Can be specified only if the type property is set to
`basic`.

_Type_: String

`secretKey`

Specifies the secret key for S3 authentication.

_Required_: Conditional. Can be specified only if the `type` property
is set to `S3`.

_Type_: String

`type`

Specifies whether the authentication scheme uses a user name and password
(basic) or an access key ID and secret key (S3).

If you specify `basic`, specify the `username`,
`password`, and `uris` properties.

If you specify `S3`, specify the `accessKeyId`,
`secretKey`, and `buckets` (optional) properties.

_Required_: Yes

_Valid values_: `basic` | `S3`

`uris`

A comma-delimited list of URIs to be associated with the basic authentication
credentials. The authorization applies to the specified URIs and any more specific
URI. For example, if you specify `http://www.example.com`, the
authorization will also apply to `http://www.example.com/test`.

_Required_: Conditional. Can be specified only if the `type` property
is set to `basic`.

_Type_: List of String values

`username`

Specifies the user name for basic authentication.

_Required_: Conditional. Can be specified only if the type property is set to
`basic`.

_Type_: String

`roleName`

Describes the role for role-based authentication.

###### Important

This role must be contained within the instance profile that's attached to
the EC2 instance. An instance profile can only contain one IAM role.

_Required_: Conditional. Can be specified only if the `type` property
is set to `S3`.

_Type_: String.

## Examples

###### Topics

- [EC2 web server authentication](#aws-resource-cloudformation-authentication-example1 "#aws-resource-cloudformation-authentication-example1")
- [Specifying both basic and S3 authentication](#aws-resource-cloudformation-authentication-example2 "#aws-resource-cloudformation-authentication-example2")
- [IAM roles](#aws-resource-cloudformation-authentication-example3 "#aws-resource-cloudformation-authentication-example3")

### EC2 web server authentication

This template snippet shows how to get a file from a private S3 bucket within an EC2
instance. The credentials used for authentication are defined in the
`AWS::CloudFormation::Authentication` metadata, and referenced by the
`AWS::CloudFormation::Init` metadata in the _files_
section.

#### JSON

```
"WebServer": {
   "Type": "AWS::EC2::Instance",
   "DependsOn" : "BucketPolicy",
   "Metadata" : {
      "AWS::CloudFormation::Init" : {
         "config" : {
            "packages" : { "yum" : { "httpd" : [] } },
            "files" : {
               "/var/www/html/index.html" : {
                  "source" : {
                     "Fn::Join" : [
                        "", [ "http://s3.amazonaws.com/", { "Ref" : "BucketName" }, "/index.html" ]
                     ]
                  },
                  "mode"   : "000400",
                  "owner"  : "apache",
                  "group"  : "apache",
                  "authentication" : "S3AccessCreds"
               }
            },
            "services" : {
               "sysvinit" : {
                  "httpd" : { "enabled" : "true", "ensureRunning" : "true" }
               }
            }
         }
      },
      "AWS::CloudFormation::Authentication" : {
         "S3AccessCreds" : {
            "type" : "S3",
            "accessKeyId" : { "Ref" : "AccessKeyID" },
            "secretKey" : { "Ref" : "SecretAccessKey" }
         }
      }
   },
   "Properties": {
   `EC2 Resource Properties ...`
   }
}
```

#### YAML

```
WebServer:
  Type: AWS::EC2::Instance
  DependsOn: BucketPolicy
  Metadata:
    AWS::CloudFormation::Init:
      config:
        packages:
          yum:
            httpd: []
        files:
          /var/www/html/index.html:
            source: !Join
              - ''
              - - 'http://s3.amazonaws.com/'
                - !Ref BucketName
                - '/index.html'
            mode: '000400'
            owner: apache
            group: apache
            authentication: S3AccessCreds
        services:
          sysvinit:
            httpd:
              enabled: 'true'
              ensureRunning: 'true'
    AWS::CloudFormation::Authentication:
      S3AccessCreds:
        type: S3
        accessKeyId: !Ref AccessKeyID
        secretKey: !Ref SecretAccessKey
  Properties:
  `EC2 Resource Properties ...`
```

### Specifying both basic and S3 authentication

The following example template snippet includes both _basic_ and
_S3_ authentication types.

#### JSON

```
"AWS::CloudFormation::Authentication" : {
   "testBasic" : {
      "type" : "basic",
      "username" : { "Ref" : "UserName" },
      "password" : { "Ref" : "Password" },
      "uris" : [ "example.com/test" ]
   },
   "testS3" : {
      "type" : "S3",
      "accessKeyId" : { "Ref" : "AccessKeyID" },
      "secretKey" : { "Ref" : "SecretAccessKey" },
      "buckets" : [{ "Fn::Sub": "${BucketName}" }]
   }
}
```

#### YAML

```
AWS::CloudFormation::Authentication:
  testBasic:
    type: basic
    username: !Ref UserName
    password: !Ref Password
    uris:
      - 'example.com/test'
  testS3:
    type: S3
    accessKeyId: !Ref AccessKeyID
    secretKey: !Ref SecretAccessKey
    buckets:
      - !Sub ${BucketName}
```

### IAM roles

The following example shows how to use IAM roles:

- `myRole` is an [AWS::IAM::Role](aws-resource-iam-role.md "aws-resource-iam-role.md") resource.
- The Amazon EC2 instance that runs `cfn-init` is associated with
  `myRole` through an instance profile.
- The example specifies the authentication by using the `buckets`
  property, like in Amazon S3 authentication. You can also specify authentication by
  name.

#### JSON

```
"AWS::CloudFormation::Authentication": {
    "rolebased" : {
        "type": "S3",
        "buckets": [{ "Fn::Sub": "${BucketName}" }],
        "roleName": { "Ref": "myRole" }
    }
}
```

#### YAML

```
AWS::CloudFormation::Authentication:
  rolebased:
    type: S3
    buckets:
      - !Sub ${BucketName}
    roleName: !Ref myRole
```
