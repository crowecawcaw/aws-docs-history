

# Amazon Inspector SBOM Generator
<a name="sbom-generator"></a>

 A Software Bill of Materials (SBOM) is [a formally structured list of components, libraries, and modules](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html) required to build a piece of software. The Amazon Inspector SBOM Generator (Sbomgen) is a tool that produces an SBOM for archives, container images, directories, local systems, and compiled Go and Rust binaries. Sbomgen scans for files that contain information about installed packages. When Sbomgen finds a relevant file, it extracts package names, versions, and other metadata. Sbomgen then transforms package metadata into a CycloneDX SBOM. You can use Sbomgen to generate the CycloneDX SBOM as a file or in STDOUT and send SBOMs to Amazon Inspector for vulnerability detection. You can also use Sbomgen as part of [the CI/CD integration](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html), which scans container images automatically as part of your deployment pipeline. 

 Amazon Inspector uses Sbomgen for several managed scanning features. When Amazon Inspector performs [Amazon ECR container image scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html), [AWS Lambda function scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html), and [Agentless scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html#agentless) of Amazon Elastic Compute Cloud instances through Amazon EBS volume analysis, it invokes Sbomgen behind the scenes to generate the software inventory used for vulnerability assessment. The standalone Sbomgen tool described on this page provides the same underlying technology, enabling you to integrate SBOM generation directly into your workflows. 

## Supported packages types
<a name="sbomgen-supported"></a>

 Sbomgen collects inventory for the following package types: 
+  Alpine APK 
+  Debian/Ubuntu DPKG 
+  Red Hat RPM 
+  C\# 
+  Go 
+  Java 
+  Node.js 
+  PHP 
+  Python 
+  Ruby 
+  Rust 

## Supported container image configuration checks
<a name="sbomgen-supported-configuration"></a>

 Sbomgen can scan standalone Dockerfiles and build history from exisiting images for security issues. For more information, see [Amazon Inspector Dockerfile checks](https://docs.aws.amazon.com/inspector/latest/user/dockerfile-checks.html). 

## Installing Sbomgen
<a name="install-sbomgen"></a>

 Sbomgen is only available for Linux operating systems. 

 You must have Docker installed if you want Sbomgen to analyze locally cached images. Docker isn't required to analyze images exported as `.tar` files or images hosted in remote container registries. 

 Amazon Inspector recommends that you run Sbomgen from a system with at least the following hardware specs: 
+ 4x core CPU
+ 8 GB RAM

**To install Sbomgen**

1.  Download the latest Sbomgen zip file from the correct URL for your architecture: 

    Linux AMD64: [https://amazon-inspector-sbomgen.s3.amazonaws.com/latest/linux/amd64/inspector-sbomgen.zip](https://amazon-inspector-sbomgen.s3.amazonaws.com/latest/linux/amd64/inspector-sbomgen.zip) 

    Linux ARM64: [https://amazon-inspector-sbomgen.s3.amazonaws.com/latest/linux/arm64/inspector-sbomgen.zip](https://amazon-inspector-sbomgen.s3.amazonaws.com/latest/linux/arm64/inspector-sbomgen.zip) 

    Alternatively, you can download [previous versions of the Amazon Inspector SBOM Generator zip file](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-versions.html). 

1.  Unzip the download using the following command: 

    `unzip inspector-sbomgen.zip` 

1.  Check for the following files in the extracted directory: 
   +  `inspector-sbomgen` – This is the tool you will execute to generate SBOMs. 
   +  `README.txt` – This is the documentation for using Sbomgen. 
   +  `LICENSE.txt` – This file contains the software license for Sbomgen. 
   +  `licenses` – This folder contains license info for third party packages used by Sbomgen. 
   +  `checksums.txt` – This file provides hashes of the Sbomgen tool. 
   +  `sbom.json` – This is a CycloneDX SBOM for the Sbomgen tool. 
   +  `WhatsNew.txt` – This file contains a summarized change log, so you can view major changes and improvements between Sbomgen versions quickly. 

1.  (Optional) Verify the authenticity and integrity of the tool using the following command: 

    `sha256sum < inspector-sbomgen` 

   1.  Compare the results with the contents of the `checksums.txt` file. 

1.  Grant executable permissions to the tool using the following command: 

    `chmod +x inspector-sbomgen` 

1.  Verify that Sbomgen is successfully installed using the following command: 

    `./inspector-sbomgen --version` 

    You should see the output similar to the following: 

    `Version: 1.X.X ` 

## Using Sbomgen
<a name="using-sbomgen"></a>

 This section describes different ways you can use Sbomgen. You can learn more about how to use Sbomgen through built-in examples. To view these examples, run the `list-examples` command: 

```
./inspector-sbomgen list-examples
```

### Generate an SBOM for a container image and output the result
<a name="w2aac39c13b7"></a>

 You can use Sbomgen to generate SBOMs for container images and output the result to a file. This capability can be enabled using the `container` subcommand. 

**Example command**  
 In the following snippet, you can replace {{`image:tag`}} with the ID of your image and {{`output_path.json`}} with the path to the output you want to save. 

```
# generate SBOM for container image
./inspector-sbomgen container {{--image image:tag}} -o {{output_path.json}}
```

**Note**  
 Scan time and performance depends on the image size and how small the number of layers are. Smaller images not only improve Sbomgen performance, but also reduce the potential attack surface. Smaller images also improve image build, download, and upload times. 

 When using Sbomgen with [`ScanSbom`](https://docs.aws.amazon.com/inspector/v2/APIReference/API_scan_ScanSbom.html), the Amazon Inspector Scan API won't process SBOMs that contain more than 5,000 packages. In this scenario, the Amazon Inspector Scan API returns an HTTP 400 response. 

 If an image includes bulk media files or directories, consider excluding them from Sbomgen using the `--skip-files` argument. 

**Example: Common error cases**  
 Container image scanning can fail due to the following errors: 
+  `InvalidImageFormat` – Occurs when scanning malformed container images with corrupt TAR headers, manifest files, or config files . 
+  `ImageValidationFailure` – Occurs when checksum or content-length validation fails for container image components, such as mismatched Content-Length headers, incorrect manifest digests, or failed SHA256 checksum verification. 
+  `ErrUnsupportedMediaType` – Occurs when image components include unsupported media types. For information about supported media types, see [Supported operating systems and media types](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html#ecr-supported-media). 

 Amazon Inspector does not support the `application/vnd.docker.distribution.manifest.list.v2+json` media type. However, Amazon Inspector does support manifest lists. When scanning images that use manifest lists, you can explicitly specify which platform to use with the `--platform` argument. If the `--platform` argument is not specified, the Amazon Inspector SBOM Generator automatically selects the manifest based on the platform where its running. 

### Generate an SBOM from directories and archives
<a name="w2aac39c13b9"></a>

 You can use Sbomgen to generate SBOMs from directories and archives. This capability can be enabled using the `directory` or `archive` subcommands. Amazon Inspector recommends using this feature when you want to generate an SBOM from a project folder, such as a downloaded git repository. 

**Example command 1**  
 The following snippet shows a subcommand that generates an SBOM from a directory file. 

```
# generate SBOM from directory
./inspector-sbomgen directory --path /path/to/dir -o /tmp/sbom.json
```

**Example command 2**  
 The following snippet shows a subcommand that generates an SBOM from an archive file. The only supported archive formats are `.zip`, `.tar`, and `.tar.gz`. 

```
# generate SBOM from archive file (tar, tar.gz, and zip formats only)
./inspector-sbomgen archive --path testData.zip -o /tmp/sbom.json
```

### Generate an SBOM from Go or Rust compiled binaries
<a name="w2aac39c13c11"></a>

 You can use Sbomgen to generate SBOMs from compiled Go and Rust binaries. You can enable this cabapility through the `binary` subcommand: 

```
./inspector-sbomgen binary --path /path/to/your/binary
```

### Generate an SBOM from mounted volumes
<a name="w2aac39c13c13"></a>

 You can use Amazon Inspector SBOM Generator to generate SBOMs from mounted volumes. This capability can be enabled using the `volume` subcommand. We recommend using this feature when you want to analyze storage volumes, such as Amazon EBS volumes that have been mounted to your system. Unlike the directory subcommand, mounted volume scanning detects OS packages and OS information. 

 You can scan an Amazon EBS volume by attaching it to an Amazon EC2 instance where Amazon Inspector SBOM Generator is installed and mounting it on that instance. For Amazon EBS volumes that are currently in use by other Amazon EC2 instances, you can create an Amazon EBS snapshot of the volume and then create a new Amazon EBS volume from that snapshot for scanning purposes. For more information about Amazon EBS, see [What is Amazon EBS?](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) in the *Amazon Elastic Block Store User Guide*. 

**Example command**  
 The following snippet shows a subcommand that generates an SBOM from a mounted volume. The `--path` argument should specify the root directory where the volume is mounted. 

```
# generate SBOM from mounted volume
./inspector-sbomgen volume --path /mount/point/of/volume/root
```

**Example command**  
 The following snippet shows a subcommand that generates an SBOM from a mounted volume while excluding specific file paths with the `--exclude-suffix` argument. The `--exclude-suffix` argument is particularly useful when a volume contains bulk files (such as log files or media files). Files and directories whose paths end with the specified suffixes will be excluded from scanning, which can reduce scan time and memory usage. 

```
# generate SBOM from mounted volume with exclusions
./inspector-sbomgen volume --path /mount/point/of/volume/root \
--exclude-suffix .log \
--exclude-suffix cache
```

 All file paths in the target volume are normalized to their original paths. For example, when scanning a volume mounted at `/mnt/volume` that contains a file at `/mnt/volume/var/lib/rpm/rpmdb.sqlite`, the path will be normalized to `/var/lib/rpm/rpmdb.sqlite` in the generated SBOM. 

### Send an SBOM to Amazon Inspector for vulnerability identification
<a name="w2aac39c13c15"></a>

 In addition to generating an SBOM, you can send an SBOM for scanning with a single command from the Amazon Inspector Scan API. Amazon Inspector evaluates the contents of the SBOM for vulnerabilites before returning findings to Sbomgen. Depending on your input, the findings can be displayed or written to a file. 

**Note**  
 You must have an active AWS account with read permissions to `InspectorScan-ScanSbom` to use this capability. 

 To enable this capability, you pass the `--scan-sbom` argument to the Sbomgen CLI. You can also pass the `--scan-sbom` argument to any of the following Sbomgen subcommands: `archive`, `binary`, `container`, `directory`, `localhost`. 

**Note**  
 The Amazon Inspector Scan API doesn't process SBOMs with more than 5,000 packages. In this scenario, the Amazon Inspector Scan API returns an HTTP 400 response. 

 You can authenticate to Amazon Inspector through an AWS profile or an IAM role with the following AWS CLI arguments: 

```
--aws-profile {{profile}}
--aws-region {{region}}
--aws-iam-role-arn {{role_arn}}
```

 You can also authenticate to Amazon Inspector by providing the following environment variables to Sbomgen. 

```
AWS_ACCESS_KEY_ID=$access_key \
AWS_SECRET_ACCESS_KEY=$secret_key \
AWS_DEFAULT_REGION=$region \
./inspector-sbomgen {{arguments}}
```

 To specify the response format, use the `--scan-sbom-output-format cyclonedx` argument or `--scan-sbom-output-format inspector` argument. 

**Example command 1**  
 This command creates an SBOM for the latest Alpine Linux release, scans the SBOM, and writes the vulnerability results to a JSON file. 

```
./inspector-sbomgen container --image alpine:latest \
                          --scan-sbom \
                          --aws-profile {{your_profile}} \
                          --aws-region {{your_region}} \
                          --scan-sbom-output-format cyclonedx \
                          --outfile /tmp/inspector_scan.json
```

**Example command 2**  
 This command authenticates to Amazon Inspector using AWS credentials as environment variables. 

```
AWS_ACCESS_KEY_ID=$your_access_key \
AWS_SECRET_ACCESS_KEY=$your_secret_key \
AWS_DEFAULT_REGION=$your_region \
./inspector-sbomgen container --image alpine:latest \
                          -o /tmp/sbom.json \
                          --scan-sbom \
                          --scan-sbom-output-format inspector
```

**Example command 3**  
 This command authenticates to Amazon Inspector using the ARN for an IAM role. 

```
./inspector-sbomgen container --image alpine:latest \
                          --scan-sbom \
                          --aws-profile your_profile \
                          --aws-region your_region \
                          --outfile /tmp/inspector_scan.json
                          --aws-iam-role-arn arn:aws:iam::123456789012:role/{{your_role}}
```

### Use additional scanners to enhance detection capabilities
<a name="w2aac39c13c17"></a>

 The Amazon Inspector SBOM Generator applies predefined scanners based on the command being used. 

**Default scanner groups**  
 Each Amazon Inspector SBOM Generator subcommand applies the following default scanner groups automatically. 
+  For the `directory` subcommand: binary, programming-language-packages, dockerfile scanner groups 
+  For the `localhost` subcommand: os, programming-language-packages, extra-ecosystems scanner groups 
+  For the `container` subcommand: os, programming-language-packages, extra-ecosystems, dockerfile, binary scanner groups 

**Special scanners**  
 To include scanners beyond the default scanner groups, use the `--additional-scanners` option followed by the name of the scanner to be added. The following is an example command showing how to do this. 

```
# Add WordPress installation scanner to directory scan
./inspector-sbomgen directory --path /path/to/directory/ --additional-scanners wordpress-installation -o output.json
```

 The following is an example command showing how to add multiple scanners with a comma-separated list. 

```
./inspector-sbomgen container --image image:tag --additional-scanners scanner1,scanner2 -o output.json
```

### Optimize container scans by adjusting maximum file size to scan
<a name="w2aac39c13c19"></a>

 When you analyze and process a container image, Sbomgen scans files that are 200 MB or less by default. Files larger than 200 MB rarely contain package metadata. You can encounter misses when you inventory a Go or Rust binary that exceeds 200MB. To adjust the size limit, use the `--max-file-size` argument. This allows you to increase the limit to include large files and decrease the limit to reduce resource usage by excluding large files. 

**Example**  
 The following example shows how to use the `--max-file-size` argument to increase the file size. 

```
# Increase the file size limit to scan files up to 300 MB
./inspector-sbomgen container --image alpine:latest \
--outfile /tmp/sbom.json \
--max-file-size 300000000
```

 Adjusting this setting helps control disk usage, memory consumption, and overall scan duration. 

### Detect scratch images with filesystem heuristics
<a name="w2aac39c13c21"></a>

 When Sbomgen can't identify a container image's operating system, you can use the `--enable-scratch-heuristics` argument to inspect the filesystem for signals that indicate a scratch image. If at least two signals are present, Sbomgen labels the operating-system component `scratch` instead of `unknown`. An identified operating system is never relabeled. 

**Note**  
 This argument is experimental, applies to container scans only, and is disabled by default. 

 Sbomgen evaluates the following signals and records each one it detects as an `amazon:inspector:sbom_generator:scratch:heuristic:*` property on the operating-system component: 
+  `missing_lib_dir` – The `/lib` directory is absent. 
+  `missing_bin_dir` – The `/bin` directory is absent. 
+  `missing_var_dir` – The `/var` directory is absent. 
+  `missing_shell` – No interactive shell is present (none of `sh`, `bash`, `ash`, `dash`, `zsh`, or `busybox` found under `/bin` or `/usr/bin`). 

**Example**  
 The following example shows how to use the `--enable-scratch-heuristics` argument. 

```
# enable scratch image detection heuristics
./inspector-sbomgen container --image image:tag \
--outfile /tmp/sbom.json \
--enable-scratch-heuristics
```

**Note**  
 This behavior is heuristic and may produce false positives. It only changes the operating-system component. 

### Disable progress indicator
<a name="w2aac39c13c23"></a>

 Sbomgen displays a spinning progress indicator that can result in excessive slash characters in CI/CD environments. 

```
INFO[2024-02-01 14:58:46]coreV1.go:53: analyzing artifact
|
\
/
|
\
/
INFO[2024-02-01 14:58:46]coreV1.go:62: executing post-processors
```

 You can disable the progress indicator using the `--disable-progress-bar` arguement: 

```
./inspector-sbomgen container --image alpine:latest \
--outfile /tmp/sbom.json \
--disable-progress-bar
```

## Authenticating to private registries with Sbomgen
<a name="authenticating-private-registry"></a>

 By providing your private registry authentication credentials, you can generate SBOMs from containers that are hosted in private registries. You can provide these credentials through the following methods: 

### Authenticate using cached credentials (recommended)
<a name="w2aac39c15b5"></a>

 For this method, you authenticate to your container registry. For example, if using Docker, you can authenticate to your container registry using the Docker loging command: `docker login`. 

1.  Authenticate to your container registry. For example, if using Docker, you can authenticate to your registry using the Docker `login` command: 

1.  After you authenticate to your container registry, use Sbomgen on a container image that's in the registry. To use the following example, replace {{`image:tag`}} with the name of the image to scan: 

```
./inspector-sbomgen container --image {{image:tag}}
```

### Authenticate using the interactive method
<a name="w2aac39c15b7"></a>

 For this method, provide your username as a parameter, and Sbomgen will prompt you for secure password entry when needed. 

 To use the following example, replace {{`image:tag`}} with the name of the image that you want to scan and {{`your_username`}} with a username that has access to the image: 

```
./inspector-sbomgen container --image {{image:tag}} --username {{your_username}}
```

### Authenticate using the non-interactive method
<a name="w2aac39c15b9"></a>

 For this method, store your password or registry token in a `.txt` file. 

**Note**  
 The current user should only be able to read this file. The file should also contain your password or token on a single line. 

 To use the following example, replace {{`your_username`}} with your username, {{`password.txt`}} with the `.txt` file that includes your password or token on a single line, and {{`image:tag`}} with the name of the image to scan: 

```
INSPECTOR_SBOMGEN_USERNAME={{your_username}} \
INSPECTOR_SBOMGEN_PASSWORD=`cat {{password.txt}}` \
./inspector-sbomgen container --image {{image:tag}}
```

## Example outputs from Sbomgen
<a name="sbom-examples"></a>

The following is an example of an SBOM for a container image inventoried using Sbomgen.

### Container image SBOM
<a name="container-sbom-example"></a>

```
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "serialNumber": "urn:uuid:828875ef-8c32-4777-b688-0af96f3cf619",
  "version": 1,
  "metadata": {
    "timestamp": "2023-11-17T21:36:38Z",
    "tools": [
      {
        "vendor": "Amazon Web Services, Inc. (AWS)",
        "name": "Amazon Inspector SBOM Generator",
        "version": "1.0.0",
        "hashes": [
          {
            "alg": "SHA-256",
            "content": "10ab669cfc99774786301a745165b5957c92ed9562d19972fbf344d4393b5eb1"
          }
        ]
      }
    ],
    "component": {
      "bom-ref": "comp-1",
      "type": "container",
      "name": "fedora:latest",
      "properties": [
        {
          "name": "amazon:inspector:sbom_generator:image_id",
          "value": "sha256:c81c8ae4dda7dedc0711daefe4076d33a88a69a28c398688090c1141eff17e50"
        },
        {
          "name": "amazon:inspector:sbom_generator:layer_diff_id",
          "value": "sha256:eddd0d48c295dc168d0710f70364581bd84b1dda6bb386c4a4de0b61de2f2119"
        }
      ]
    }
  },
  "components": [
    {
      "bom-ref": "comp-2",
      "type": "library",
      "name": "dnf",
      "version": "4.18.0",
      "purl": "pkg:pypi/dnf@4.18.0",
      "properties": [
        {
          "name": "amazon:inspector:sbom_generator:source_file_scanner",
          "value": "python-pkg"
        },
        {
          "name": "amazon:inspector:sbom_generator:source_package_collector",
          "value": "python-pkg"
        },
        {
          "name": "amazon:inspector:sbom_generator:source_path",
          "value": "/usr/lib/python3.12/site-packages/dnf-4.18.0.dist-info/METADATA"
        },
        {
          "name": "amazon:inspector:sbom_generator:is_duplicate_package",
          "value": "true"
        },
        {
          "name": "amazon:inspector:sbom_generator:duplicate_purl",
          "value": "pkg:rpm/fedora/python3-dnf@4.18.0-2.fc39?arch=noarch&distro=39&epoch=0"
        }
      ]
    },
    {
      "bom-ref": "comp-3",
      "type": "library",
      "name": "libcomps",
      "version": "0.1.20",
      "purl": "pkg:pypi/libcomps@0.1.20",
      "properties": [
        {
          "name": "amazon:inspector:sbom_generator:source_file_scanner",
          "value": "python-pkg"
        },
        {
          "name": "amazon:inspector:sbom_generator:source_package_collector",
          "value": "python-pkg"
        },
        {
          "name": "amazon:inspector:sbom_generator:source_path",
          "value": "/usr/lib64/python3.12/site-packages/libcomps-0.1.20-py3.12.egg-info/PKG-INFO"
        },
        {
          "name": "amazon:inspector:sbom_generator:is_duplicate_package",
          "value": "true"
        },
        {
          "name": "amazon:inspector:sbom_generator:duplicate_purl",
          "value": "pkg:rpm/fedora/python3-libcomps@0.1.20-1.fc39?arch=x86_64&distro=39&epoch=0"
        }
      ]
    }
  ]
}
```