# Publishing and consuming generic packages

To publish a generic package version and its related assets, use the `publish-package-version` command.
You can list a generic package's assets using the `list-package-version-asset` command and download them
using `get-package-version-asset`. The following topic contains step-by-step instructions to publish generic packages or
download generic package assets using these commands.

## Publishing a generic package

A generic package consists of a package name, namespace, version, and one or more
assets (or files). This topic demonstrates how to publish a package named
`my-package`, with the namespace `my-ns`, version
`1.0.0`, and containing one asset named `asset.tar.gz`.

**Prerequisites:**

- Set up and configure the AWS Command Line Interface with CodeArtifact (see [Setting up with AWS CodeArtifact](get-set-up-for-codeartifact.md "get-set-up-for-codeartifact.md"))
- Have a CodeArtifact domain and repository (see [Getting started using the AWS CLI](getting-started-cli.md "getting-started-cli.md"))

###### To publish a generic package

1. Use the following command to generate the SHA256 hash for each file you want to upload to a
   package version, and place the value in an environment variable. This value is
   used as an integrity check to verify that the file contents have not changed after
   they were originally sent.

Linux

```
export `ASSET_SHA256`=$(sha256sum `asset.tar.gz` | awk '{print $1;}')
```

macOS

```
export `ASSET_SHA256`=$(shasum -a 256 `asset.tar.gz` | awk '{print $1;}')
```

Windows

```
for /f "tokens=*" %G IN ('certUtil -hashfile `asset.tar.gz` SHA256 ^| findstr /v "hash"') DO SET "`ASSET_SHA256`=%G"
```

2. Call `publish-package-version` to upload the asset and create a new package version.

###### Note

If your package contains more than one asset, you can call `publish-package-version` once for each asset to upload. Include the `--unfinished` argument for each call to `publish-package-version`, except for when uploading the final asset. Omitting `--unfinished` will set the package version's status to `Published`, and prevent additional assets from being uploaded to it.

Alternatively, include `--unfinished` for every call to `publish-package-version`, then set the package version's status to `Published` using the `update-package-versions-status` command.

Linux/macOS

```
aws codeartifact publish-package-version --domain `my_domain` --repository `my_repo` \
      --format `generic` --namespace `my-ns` --package `my-package` --package-version `1.0.0` \
      --asset-content `asset.tar.gz` --asset-name `asset.tar.gz` \
      --asset-sha256 `$ASSET_SHA256`
```

Windows

```
aws codeartifact publish-package-version --domain `my_domain` --repository `my_repo` ^
      --format `generic` --namespace `my-ns` --package `my-package` --package-version `1.0.0` ^
      --asset-content `asset.tar.gz` --asset-name `asset.tar.gz` ^
      --asset-sha256 `%ASSET_SHA256%`
```

The following shows the output.

```
{
    "format": "generic",
    "namespace": "my-ns",
    "package": "my-package",
    "version": "1.0.0",
    "versionRevision": "REVISION-SAMPLE-1-C7F4S5E9B772FC",
    "status": "Published",
    "asset": {
        "name": "asset.tar.gz",
        "size": 11,
        "hashes": {
            "MD5": "41bba98d5b9219c43089eEXAMPLE-MD5",
            "SHA-1": "69b215c25dd4cda1d997a786ec6EXAMPLE-SHA-1",
            "SHA-256": "43f24850b7b7b7d79c5fa652418518fbdf427e602b1edabe6EXAMPLE-SHA-256",
            "SHA-512": "3947382ac2c180ee3f2aba4f8788241527c8db9dfe9f4b039abe9fc560aaf5a1fced7bd1e80a0dca9ce320d95f0864e0dec3ac4f2f7b2b2cbEXAMPLE-SHA-512"
        }
    }
}
```

## Listing generic package assets

To list the assets contained in a generic package, use the
`list-package-version-assets` command. For more information, see [List package version assets](list-assets.md "list-assets.md").

The following example lists the assets of version `1.0.0` of package
`my-package`.

###### To list package version assets

- Call `list-package-version-assets` to list the assets contained in a
  generic package.

Linux/macOS

```
aws codeartifact list-package-version-assets --domain `my_domain` \
  --repository `my_repo` --format `generic` --namespace `my-ns` \
  --package `my-package` --package-version `1.0.0`

```

Windows

```
aws codeartifact list-package-version-assets --domain `my_domain` ^
  --repository `my_repo` --format `generic` --namespace `my-ns` ^
  --package `my-package` --package-version `1.0.0`

```

The following shows the output.

```
{
    "assets": [
        {
            "name": "asset.tar.gz",
            "size": 11,
            "hashes": {
                "MD5": "41bba98d5b9219c43089eEXAMPLE-MD5",
                "SHA-1": "69b215c25dd4cda1d997a786ec6EXAMPLE-SHA-1",
                "SHA-256": "43f24850b7b7b7d79c5fa652418518fbdf427e602b1edabe6EXAMPLE-SHA-256",
                "SHA-512": "3947382ac2c180ee3f2aba4f8788241527c8db9dfe9f4b039abe9fc560aaf5a1fced7bd1e80a0dca9ce320d95f0864e0dec3ac4f2f7b2b2cbEXAMPLE-SHA-512"
            }
        }
    ],
    "package": "my-package",
    "format": "generic",
    "namespace": "my-ns",
    "version": "1.0.0",
    "versionRevision": "REVISION-SAMPLE-1-C7F4S5E9B772FC"
}
```

## Downloading generic package

assets

To download the assets from a generic package, use the
`get-package-version-asset` command. For more information, see [Download package version assets](download-assets.md "download-assets.md").

The following example downloads the asset `asset.tar.gz` from version
`1.0.0` of the package `my-package` to the current working
directory into a file also named `asset.tar.gz`.

###### To download package version assets

- Call `get-package-version-asset` to download assets from a generic
  package.

Linux/macOS

```
aws codeartifact get-package-version-asset --domain `my_domain` \
  --repository `my_repo` --format `generic` --namespace `my-ns` --package `my-package` \
  --package-version `1.0.0` --asset `asset.tar.gz` \
  `asset.tar.gz`
```

Windows

```
aws codeartifact get-package-version-asset --domain `my_domain` ^
  --repository `my_repo` --format `generic` --namespace `my-ns` --package `my-package` ^
  --package-version `1.0.0` --asset `asset.tar.gz` ^
  `asset.tar.gz`
```

The following shows the output.

```
{
    "assetName": "asset.tar.gz",
    "packageVersion": "1.0.0",
    "packageVersionRevision": "REVISION-SAMPLE-1-C7F4S5E9B772FC"
}
```
