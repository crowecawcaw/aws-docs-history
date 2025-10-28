# Creating a software package and package version

You can use the following steps to create a package and an initial version thing through the AWS Management Console.

###### To create a software package

1. Sign into your AWS account and navigate to the
   [AWS IoT console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
2. On the navigation pane, choose **Software packages**.
3. On the **AWS IoT software package** page,
   choose **Create package**.
   The **Enable dependencies for package management**
   dialog box appears.
4. Under **Fleet indexing**, select
   **Add device software packages and version**.
   This is required for Software Package Catalog and provides fleet indexing and metrics about your fleet.
5. [Optional] If you want AWS IoT jobs to update the reserved named shadow when jobs successfully complete, select **Auto update shadows from jobs**.
   If you do not want AWS IoT jobs to make this update, leave this check-box unselected.
6. [Optional] To grant AWS IoT jobs the rights to update the reserved named shadow,
   under **Select role**, choose **Create role**.
   If you don't want AWS IoT jobs to make this update, this role is not required.
7. Create or select a role.
   1. If you **don’t have a role** for this purpose: When the **Create role** dialog box appears, enter a **Role name**, and
      then choose **Create**.
   2. If you **do have a role** for this purpose: For **Select role**,
      choose your role and then make sure the **Attach policy to IAM role** check box is selected.

8. Choose **Confirm**. The **Create new package** page appears.
9. Under **Package detail**, enter a **Package name**.
10. Under **Package description**, enter information to help you identify and manage this package.
11. [Optional] You can use tags to help you categorize and manage this package. To add tags, expand **Tags**, choose **Add tag**, and enter a key-value pair. You can enter up to 50 tags. For more information, see [Tagging your AWS IoT resources](tagging-iot.md "tagging-iot.md").

###### To add a package version while creating a new package

1. Under **Initial version**, enter a **Version name**.

We recommend using the [SemVer format](https://semver.org/ "https://semver.org/") (for example, `1.0.0.0`)
to uniquely identify your package version. You are also able to use a different formatting strategy
that better suits your use case. For more information, see
[Package version lifecycle](preparing-to-use-software-package-catalog.md#package-version-lifecycle "preparing-to-use-software-package-catalog.md#package-version-lifecycle"). 2. Under **Version description**, enter information that will help you identify and manage this package version .

###### Note

The **Default version** check box is deactivated
because package versions are created in a `draft` state.
You can name the default version after you create the package version and when you
change the state to `published`. For more information, see
[Package version lifecycle](preparing-to-use-software-package-catalog.md#package-version-lifecycle "preparing-to-use-software-package-catalog.md#package-version-lifecycle"). 3. [Optional] To help you manage this version or to communicate information to your devices, enter one or more name-value pairs for **Version attributes**.
Choose **Add attribute** for each name-value pair you enter.
For more information, see [Version attributes](preparing-to-use-software-package-catalog.md#version-attributes "preparing-to-use-software-package-catalog.md#version-attributes"). 4. [Optional] You can use tags to help you categorize and manage this package. To add tags, expand
**Tags**, choose **Add** tag, and enter a key-value pair.
You can enter up to 50 tags. For more information, see
[Tagging your AWS IoT resources](tagging-iot.md "tagging-iot.md"). 5. Choose **Next**.

###### Associate the Software Bill of Materials to a Package Version

(Optional)

1. On **Step 3: Version SBOMs (Optional)** in the
   **SBOM configurations** window, choose the default SBOM
   file format and validation mode used to validate your software bill of
   materials before it is associated to your package version.
2. In the **Add SBOM file** window, enter the Amazon
   Resource Name (ARN) representing your versioned Amazon S3 bucket and the
   preferred SBOM file format if the default type doesn't work.

###### Note

You can either add a single SBOM file or a single zip file containing
multiple SBOMs if you have more than one software bill of material for
your package version. 3. In the **Added SBOM file** window, you can view the SBOM
file you added for your package version. 4. Choose **Create package and version**. The package
version page appears and you can see the validation status of your SBOM file
in the **Added SBOM file** window. The initial status will
be `In progress` as the SBOM file undergoes validation.

###### Note

The SBOM file validation statuses are `Invalid file`,
`Not started`, `In progress`, `Validated
 (SPDX)`, `Validated (CycloneDX)`, and the
validation failure reasons.
