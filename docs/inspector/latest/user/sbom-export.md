# Exporting SBOMs with Amazon Inspector

A software bill of materials (SBOM) is a nested inventory of all the open-source and third-party software components in your codebase.
Amazon Inspector provides SBOMs for individual resources in your environment.
You can use the Amazon Inspector console or Amazon Inspector API to generate SBOMs for your resources.
You can export SBOMs for all resources that Amazon Inspector supports and monitors.
Exported SBOMs provide information about your software supply.
You can review the status of your resources by [assessing the coverage of your AWS environment](assessing-coverage.md "assessing-coverage.md").
This section describes how to configure and export SBOMs.

Some software components and package managers use version ranges or dynamic references instead of fixed versions for dependencies.
This practice creates unresolved hashes, where Amazon Inspector identifies a hash or jar file but cannot map it to a specific name and version for vulnerability detection.
Amazon Inspector now includes these unresolved hashes in Software Bill of Materials (SBOM) exports.
While these packages cannot be scanned for vulnerabilities, their hash values are available within the exported components list.

###### Note

Currently, Amazon Inspector doesn't support exporting SBOMs for Windows Amazon EC2 instances.

## Amazon Inspector formats

Amazon Inspector supports exporting SBOMs in **CycloneDX 1.4** and **SPDX 2.3** compatible formats. Amazon Inspector exports SBOMs as `JSON` files to the Amazon S3 bucket you choose.

###### Note

SPDX format exports from Amazon Inspector are compatible with systems using **SPDX
2.3**, however they don't contain the Creative Commons Zero (CC0)
field. This is because including this field would allow users to redistribute or edit the material.

```

                    {
  "bomFormat": "CycloneDX",
  "specVersion": "1.4",
  "version": 1,
  "metadata": {
    "timestamp": "2023-06-02T01:17:46Z",
    "component": null,
    "properties": [
      {
        "name": "imageId",
        "value": "sha256:c8ee97f7052776ef223080741f61fcdf6a3a9107810ea9649f904aa4269fdac6"
      },
      {
        "name": "architecture",
        "value": "arm64"
      },
      {
        "name": "accountId",
        "value": "111122223333"
      },
      {
        "name": "resourceType",
        "value": "AWS_ECR_CONTAINER_IMAGE"
      }
    ]
  },
  "components": [
    {
      "type": "library",
      "name": "pip",
      "purl": "pkg:pypi/pip@22.0.4?path=usr/local/lib/python3.8/site-packages/pip-22.0.4.dist-info/METADATA",
      "bom-ref": "98dc550d1e9a0b24161daaa0d535c699"
    },
    {
      "type": "application",
      "name": "libss2",
      "purl": "pkg:dpkg/libss2@1.44.5-1+deb10u3?arch=ARM64&epoch=0&upstream=libss2-1.44.5-1+deb10u3.src.dpkg",
      "bom-ref": "2f4d199d4ef9e2ae639b4f8d04a813a2"
    },
    {
      "type": "application",
      "name": "liblz4-1",
      "purl": "pkg:dpkg/liblz4-1@1.8.3-1+deb10u1?arch=ARM64&epoch=0&upstream=liblz4-1-1.8.3-1+deb10u1.src.dpkg",
      "bom-ref": "9a6be8907ead891b070e60f5a7b7aa9a"
    },
    {
      "type": "application",
      "name": "mawk",
      "purl": "pkg:dpkg/mawk@1.3.3-17+b3?arch=ARM64&epoch=0&upstream=mawk-1.3.3-17+b3.src.dpkg",
      "bom-ref": "c2015852a729f97fde924e62a16f78a5"
    },
    {
      "type": "application",
      "name": "libgmp10",
      "purl": "pkg:dpkg/libgmp10@6.1.2+dfsg-4+deb10u1?arch=ARM64&epoch=2&upstream=libgmp10-6.1.2+dfsg-4+deb10u1.src.dpkg",
      "bom-ref": "52907290f5beef00dff8da77901b1085"
    },
    {
      "type": "application",
      "name": "ncurses-bin",
      "purl": "pkg:dpkg/ncurses-bin@6.1+20181013-2+deb10u3?arch=ARM64&epoch=0&upstream=ncurses-bin-6.1+20181013-2+deb10u3.src.dpkg",
      "bom-ref": "cd20cfb9ebeeadba3809764376f43bce"
    }
  ],
  "vulnerabilities": [
    {
      "id": "CVE-2022-40897",
      "affects": [
        {
          "ref": "a74a4862cc654a2520ec56da0c81cdb3"
        },
        {
          "ref": "0119eb286405d780dc437e7dbf2f9d9d"
        }
      ]
    }
  ]
}

```

```

{
	"name": "409870544328/EC2/i-022fba820db137c64/ami-074ea14c08effb2d8",
	"spdxVersion": "SPDX-2.3",
	"creationInfo": {
		"created": "2023-06-02T21:19:22Z",
		"creators": [
			"Organization: 409870544328",
			"Tool: Amazon Inspector SBOM Generator"
		]
	},
	"documentNamespace": "EC2://i-022fba820db137c64/AMAZON_LINUX_2/null/x86_64",
	"comment": "",
	"packages": [{
			"name": "elfutils-libelf",
			"versionInfo": "0.176-2.amzn2",
			"downloadLocation": "NOASSERTION",
			"sourceInfo": "/var/lib/rpm/Packages",
			"filesAnalyzed": false,
			"externalRefs": [{
				"referenceCategory": "PACKAGE-MANAGER",
				"referenceType": "purl",
				"referenceLocator": "pkg:rpm/elfutils-libelf@0.176-2.amzn2?arch=X86_64&epoch=0&upstream=elfutils-libelf-0.176-2.amzn2.src.rpm"
			}],
			"SPDXID": "SPDXRef-Package-rpm-elfutils-libelf-ddf56a513c0e76ab2ae3246d9a91c463"
		},
		{
			"name": "libcurl",
			"versionInfo": "7.79.1-1.amzn2.0.1",
			"downloadLocation": "NOASSERTION",
			"sourceInfo": "/var/lib/rpm/Packages",
			"filesAnalyzed": false,
			"externalRefs": [{
					"referenceCategory": "PACKAGE-MANAGER",
					"referenceType": "purl",
					"referenceLocator": "pkg:rpm/libcurl@7.79.1-1.amzn2.0.1?arch=X86_64&epoch=0&upstream=libcurl-7.79.1-1.amzn2.0.1.src.rpm"
				},
				{
					"referenceCategory": "SECURITY",
					"referenceType": "vulnerability",
					"referenceLocator": "CVE-2022-32205"
				}
			],
			"SPDXID": "SPDXRef-Package-rpm-libcurl-710fb33829bc5106559bcd380cddb7d5"
		},
		{
			"name": "hunspell-en-US",
			"versionInfo": "0.20121024-6.amzn2.0.1",
			"downloadLocation": "NOASSERTION",
			"sourceInfo": "/var/lib/rpm/Packages",
			"filesAnalyzed": false,
			"externalRefs": [{
				"referenceCategory": "PACKAGE-MANAGER",
				"referenceType": "purl",
				"referenceLocator": "pkg:rpm/hunspell-en-US@0.20121024-6.amzn2.0.1?arch=NOARCH&epoch=0&upstream=hunspell-en-US-0.20121024-6.amzn2.0.1.src.rpm"
			}],
			"SPDXID": "SPDXRef-Package-rpm-hunspell-en-US-de19ae0883973d6cea5e7e079d544fe5"
		},
		{
			"name": "grub2-tools-minimal",
			"versionInfo": "2.06-2.amzn2.0.6",
			"downloadLocation": "NOASSERTION",
			"sourceInfo": "/var/lib/rpm/Packages",
			"filesAnalyzed": false,
			"externalRefs": [{
					"referenceCategory": "PACKAGE-MANAGER",
					"referenceType": "purl",
					"referenceLocator": "pkg:rpm/grub2-tools-minimal@2.06-2.amzn2.0.6?arch=X86_64&epoch=1&upstream=grub2-tools-minimal-2.06-2.amzn2.0.6.src.rpm"
				},
				{
					"referenceCategory": "SECURITY",
					"referenceType": "vulnerability",
					"referenceLocator": "CVE-2021-3981"
				}
			],
			"SPDXID": "SPDXRef-Package-rpm-grub2-tools-minimal-c56b7ea76e5a28ab8f232ef6d7564636"
		},
		{
			"name": "unixODBC-devel",
			"versionInfo": "2.3.1-14.amzn2",
			"downloadLocation": "NOASSERTION",
			"sourceInfo": "/var/lib/rpm/Packages",
			"filesAnalyzed": false,
			"externalRefs": [{
				"referenceCategory": "PACKAGE-MANAGER",
				"referenceType": "purl",
				"referenceLocator": "pkg:rpm/unixODBC-devel@2.3.1-14.amzn2?arch=X86_64&epoch=0&upstream=unixODBC-devel-2.3.1-14.amzn2.src.rpm"
			}],
			"SPDXID": "SPDXRef-Package-rpm-unixODBC-devel-1bb35add92978df021a13fc9f81237d2"
		}
	],
	"relationships": [{
			"spdxElementId": "SPDXRef-DOCUMENT",
			"relatedSpdxElement": "SPDXRef-Package-rpm-elfutils-libelf-ddf56a513c0e76ab2ae3246d9a91c463",
			"relationshipType": "DESCRIBES"
		},
		{
			"spdxElementId": "SPDXRef-DOCUMENT",
			"relatedSpdxElement": "SPDXRef-Package-rpm-yajl-8476ce2db98b28cfab2b4484f84f1903",
			"relationshipType": "DESCRIBES"
		},
		{
			"spdxElementId": "SPDXRef-DOCUMENT",
			"relatedSpdxElement": "SPDXRef-Package-rpm-unixODBC-devel-1bb35add92978df021a13fc9f81237d2",
			"relationshipType": "DESCRIBES"
		}
	],
	"SPDXID": "SPDXRef-DOCUMENT"
}

```

## Filters for SBOMs

When you export SBOMs you can include filters to create reports for specific subsets of resources. If you don’t supply a filter the SBOMs for all active, supported resources are exported. And if you are a delegated administrator this includes resources for all members too. The following filters are available:

- **AccountID** —
  This filter can be used to export SBOMs for any resources associated with specific
  Account ID.
- **EC2 instance tag** —
  This filter can be used to export SBOMs for EC2 instances with specific tags.
- **Function name** —
  This filter can be used to export SBOMs for specific Lambda functions.
- **Image tag** —
  This filter can be used to export SBOMs for container images with specific
  tags.
- **Lambda function tag** — This filter can be used to export SBOMs for Lambda functions with specific
  tags.
- **Resource type** —
  This filter can be used to filter resource type: EC2/ECR/Lambda.
- **Resource ID** — This filter can be used to export an SBOM for a specific resource.
- **Repository name** —This filter can be used to generate SBOMs for container images in specific
  repositories.

## Configure and export SBOMs

To export SBOMs, you must first configure an Amazon S3 bucket and a AWS KMS key that Amazon Inspector is allowed to use. You can use filters to export SBOMs for specific subsets of your resources. To export SBOMs for multiple accounts in an AWS Organization, follow these steps while signed in as the Amazon Inspector delegated administrator.

###### Prerequisites

- Supported resources that are being actively monitored by Amazon Inspector.
- An Amazon S3 bucket configured with a policy that allows Amazon Inspector to add object to. For information on configuring the policy see [Configure export permissions](findings-managing-exporting-reports.md#findings-managing-exporting-permissions "findings-managing-exporting-reports.md#findings-managing-exporting-permissions").
- An AWS KMS key configured with a policy that allows Amazon Inspector to use to encrypt your reports. For information on configuring the policy see [Configure an AWS KMS key for export](findings-managing-exporting-reports.md#findings-managing-exporting-KMS "findings-managing-exporting-reports.md#findings-managing-exporting-KMS").

###### Note

If you have previously configured an Amazon S3 bucket and an AWS KMS key for [findings export](findings-managing-exporting-reports.md "findings-managing-exporting-reports.md") you can use the same bucket and key for SBOM export.

Choose your preferred access method to export an SBOM.

Console1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home"). 2. Using the AWS Region selector in the upper-right corner of the page,
select the Region with the resources you want to export SBOM for. 3. In the navigation pane, choose **Export SBOMs**. 4. (Optional) In the **Export SBOMs** page, use the **Add filter** menu to select a subset of resources to create reports for. If no filter is provided Amazon Inspector will export reports for all active resources. If you are a delegated administrator this will include all active resources in your organization. 5. Under **Export setting** select the format you want for the SBOM. 6. Enter an **Amazon S3 URI** or choose **Browse Amazon S3** to select an Amazon S3 location to store the SBOM. 7. Enter a **AWS KMS key** configured for Amazon Inspector to use to encrypt your reports.

API\* To export SBOMs for your resources programmatically, use the [CreateSbomExport](../../v2/APIReference/API_CreateSbomExport.md "../../v2/APIReference/API_CreateSbomExport.md") operation of the Amazon Inspector API.

In your request, use the `reportFormat` parameter to specify the SBOM output format, choose `CYCLONEDX_1_4` or `SPDX_2_3`. The `s3Destination` parameter is required and you must specify an S3 bucket configured with a policy that allows Amazon Inspector to write to it. Optionally use `resourceFilterCriteria` parameters to limit the scope of the report to specific resources.

AWS CLI\* To export SBOMs for your resources using the AWS Command Line Interface run the following command:

`aws inspector2 create-sbom-export --report-format `FORMAT` --s3-destination bucketName=`amzn-s3-demo-bucket1`,keyPrefix=`PREFIX`,kmsKeyArn=`arn:aws:kms:Region:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

In your request, replace `FORMAT` with the format of your choice, `CYCLONEDX_1_4` or `SPDX_2_3`. Then replace the `user input placeholders` for the s3 destination with the name of the S3 bucket to export to, the prefix to use for the output in S3, and the ARN for the KMS key you are using to encrypt the reports.
