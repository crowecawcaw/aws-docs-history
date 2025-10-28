# `Image` section

**(Optional)** Defines the image properties for the image build.

```
Image:
  Name: `string`
  RootVolume:
    Size: `integer`
    Encrypted: `boolean`
    KmsKeyId: `string`
  Tags:
    - Key: `string`
      Value: `string`
```

## `Image` properties

`Name` (**Optional**, `String`)

Specifies the name of the AMI. If not specified, the name used when calling the [pcluster build-image](pcluster.md "pcluster.md") command is used.

### `Tags`

#### `Tags` properties

(**Optional**) Specifies key-value pairs for the image.

```
Tags:
  - Key: `string`
    Value: `string`
```

`Key` (**Optional**, `String`)

Defines the name of the tag.

`Value` (**Optional**, `String`)

Defines the value of the tag.

### `RootVolume`

#### `RootVolume` properties

(**Optional**) Specifies properties of the root volume for the image.

```
RootVolume:
  Size: `integer`
  Encrypted: `boolean`
  KmsKeyId: `string`
```

`Size` (**Optional**,
`Integer`)

Specifies the size of the root volume for the image, in GiB. The default size is the size of the [ParentImage](Build-v3.md#yaml-build-image-Build-ParentImage "Build-v3.md#yaml-build-image-Build-ParentImage") plus 27 GiB.

`Encrypted` (**Optional**,
`Boolean`)

Specifies if the volume is encrypted. The default value is `false`.

`KmsKeyId` (**Optional**,
`String`)

Specifies the ARN of the AWS KMS key used to encrypt the volume. The format is
"`arn:`Partition`:kms:`Region`:`Account`:key/`KeyId``.
