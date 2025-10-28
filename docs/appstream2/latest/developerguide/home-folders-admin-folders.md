# Home Folder Formats

The hierarchy of a user folder depends on how a user launches a streaming
session, as described in the following sections.

## AWS SDKs and

AWS CLI

For sessions launched using `CreateStreamingURL` or
`create-streaming-url` the user folder structure is as
follows:

```
`bucket-name`/user/custom/`user-id-SHA-256-hash`/
```

Where `bucket-name` is in the format
shown in [Amazon S3 Bucket Storage](home-folders-s3.md "home-folders-s3.md")
and `user-id-SHA-256-hash` is the
user-specific folder name created using a lowercase SHA-256 hash hexadecimal
string generated from the `UserId` value passed to the
CreateStreamingURL API operation or `create-streaming-url`
command. For more information, see [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") in
the _Amazon AppStream 2.0 API Reference_ and
[create-streaming-url](../../../cli/latest/reference/appstream/create-streaming-url.md "../../../cli/latest/reference/appstream/create-streaming-url.md") in the
_AWS CLI Command Reference_.

The following example folder structure applies to session access using the
API or AWS CLI with a `UserId` testuser@mydomain.com, account id
123456789012 in the US West (Oregon) Region (us-west-2):

```
appstream2-36fb080bb8-us-west-2-123456789012/user/custom/a0bcb1da11f480d9b5b3e90f91243143eac04cfccfbdc777e740fab628a1cd13/
```

You can identify the folder for a user by generating the lowercase SHA-256
hash value of the `UserId` using websites or open source coding
libraries available online.

## SAML 2.0

For sessions created using SAML federation, the user folder structure is
as follows:

```
`bucket-name`/user/federated/`user-id-SHA-256-hash`/
```

In this case, `user-id-SHA-256-hash`
is the folder name created using a lowercase SHA-256 hash hexadecimal string
generated from the `NameID` SAML attribute value passed in the
SAML federation request. To differentiate users who have the same name but
belong to two different domains, send the SAML request with
`NameID` in the format `domainname\username`. For
more information, see [Amazon AppStream 2.0 Integration with SAML 2.0](external-identity-providers.md "external-identity-providers.md").

The following example folder structure applies to session access using
SAML federation with `NameID` SAMPLEDOMAIN\testuser, account ID
123456789012 in the US West (Oregon) Region:

```
appstream2-36fb080bb8-us-west-2-123456789012/user/federated/8dd9a642f511609454d344d53cb861a71190e44fed2B8aF9fde0C507012a9901
```

When part or all of the NameID string is capitalized (as the domain name
`SAMPLEDOMAIN` is in the example), AppStream 2.0
generates the hash value based on the capitalization used in the string.
Using this example, the hash value for SAMPLEDOMAIN\testuser is
8DD9A642F511609454D344D53CB861A71190E44FED2B8AF9FDE0C507012A9901. In the
folder for that user, this value is displayed in lowercase, as follows:
8dd9a642f511609454d344d53cb861a71190e44fed2B8aF9fde0C507012a9901.

You can identify the folder for a user by generating the SHA-256 hash
value of the `NameID` using websites or open source coding
libraries available online.
