# Use parameters to specify module values

In CloudFormation, you can use template parameters to customize your stacks by providing input
values during stack creation or update. These parameters allow you to change certain aspects
of the stack based on your needs. For more information about defining template parameters, see
[CloudFormation template Parameters
syntax](parameters-section-structure.md "parameters-section-structure.md").

Similarly, modules can also have parameters. These module parameters allow you to input
custom values to the module from the template (or another module) that's using it. The module
can then use these custom values to set property values for the resources it contains.

You can also define template parameters that set module properties, so that you can input
values that get passed to the module at the time of the stack operation.

If a module contains a nested module that has its own module parameters, you can
either:

- Specify the values for the nested module's parameters directly in the parent
  module.
- Define corresponding module parameters in the parent module that enable the nested
  module's parameters to be set by the template (or module) in which the parent module is
  contained.

## Using template parameters to specify module

parameter values

The following example shows how to define template parameters that pass values to a
module.

This template containing `My::S3::SampleBucket::MODULE` defines a template
parameter, `BucketName`, that enables the user to specify an S3 bucket name
during the stack operation.

```
# Template containing My::S3::SampleBucket::MODULE
Parameters:
  BucketName:
    Description: Name for your sample bucket
    Type: String
Resources:
  MyBucket:
    Type: 'My::S3::SampleBucket::MODULE'
    Properties:
      BucketName: !Ref BucketName
```

## Specifying properties on resources in a

child module from the parent module

The following example illustrates how to specify parameter values in a module that's
nested within another module.

This first module, `My::S3::SampleBucketPrivate::MODULE`, will be the child
module. It defines two parameters: `BucketName` and `AccessControl`.
The values specified for these parameters are used to specify the `BucketName`
and `AccessControl` properties of the `AWS::S3::Bucket` resource the
module contains. Below is the template fragment for
`My::S3::SampleBucketPrivate::MODULE`.

```
# My::S3::SampleBucketPrivate::MODULE
AWSTemplateFormatVersion: 2010-09-09
Description: A sample S3 Bucket with Versioning and DeletionPolicy.
Parameters:
  BucketName:
    Description: Name for the bucket
    Type: String
  AccessControl:
    Description: AccessControl for the bucket
    Type: String
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Ref BucketName
      AccessControl: !Ref AccessControl
      DeletionPolicy: Retain
      VersioningConfiguration:
        Status: Enabled
```

Next, the previous module is nested within a parent module,
`My::S3::SampleBucket::MODULE`. The parent module,
`My::S3::SampleBucket::MODULE`, sets the child module parameters in the
following ways:

- It sets the `AccessControl` parameter of
  `My::S3::SampleBucketPrivate::MODULE` to `Private`.
- For `BucketName`, it defines a module parameter, which will enable the
  bucket name to be specified in the template (or module) that contains
  `My::S3::SampleBucket::MODULE`.

```
# My::S3::SampleBucket::MODULE
AWSTemplateFormatVersion: 2010-09-09
Description: A sample S3 Bucket. With Private AccessControl.
Parameters:
  BucketName:
    Description: Name for your sample bucket
    Type: String
Resources:
  MyBucket:
    Type: 'My::S3::SampleBucketPrivate::MODULE'
    Properties:
      BucketName: !Ref BucketName
      AccessControl: Private
```

## Specifying constraints for module

parameters

Module parameters don't support constraint enforcement. To perform constraint checking
on a module parameter, create a template parameter with the desired constraints. Then,
reference that template parameter in your module parameter. For more information about
defining template parameters, see [CloudFormation template Parameters
syntax](parameters-section-structure.md "parameters-section-structure.md").
