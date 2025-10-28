# Create a package group

You can create a package group using the CodeArtifact console, the AWS Command Line Interface (AWS CLI), or AWS CloudFormation. For more information about
managing CodeArtifact package groups with CloudFormation, see [Creating CodeArtifact resources with AWS CloudFormation](cloudformation-codeartifact.md "cloudformation-codeartifact.md").

## Create a package group (console)

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. In the navigation pane, choose **Domains**, and then choose the domain
   in which you want to create a package group.
3. Choose **Package groups**, and choose **Create package group**.
4. In **Package group definition**, enter the package group definition for your package group. The
   package group definition determines which packages are associated with the group. You can enter the package group
   definition manually with text, or you can use the visual mode to make selections and the package group definition will be created automatically.
5. To use the visual mode to create the package group definition:
   1. Choose **Visual** to switch to the visual mode..
   2. In **Package format**, choose the format of the packages to be associated with this group.
   3. In **Namespace (Scope)**, choose the namespace criteria to match on.
      - **Equals**: Match the specified namespace exactly. If chosen, enter the namespace to match on.
      - **Blank**: Match packages with no namespace.
      - **Starts with word**: Match namespaces that begin with a specified word. If chosen, enter the
        prefix word to match on. For more information about words
        and word boundaries, see [Words, word boundaries, and prefix matching](package-group-definition-syntax-matching-behavior.md#package-group-word-boundary-prefix "package-group-definition-syntax-matching-behavior.md#package-group-word-boundary-prefix").
      - **All**: Match packages in all namespaces.

   4. If **Equals**, **Blank**, or **Starts with word** is selected, in
      **Package name**, choose the package name criteria to match on.
      - **Exactly equals**: Match the specified package name exactly. If chosen, enter the package name to match on.
      - **Starts with prefix**: Match packages that start with the specified prefix.
      - **Starts with word**: Match packages that begin with a specified word. If chosen, enter the
        prefix word to match on. For more information about words
        and word boundaries, see [Words, word boundaries, and prefix matching](package-group-definition-syntax-matching-behavior.md#package-group-word-boundary-prefix "package-group-definition-syntax-matching-behavior.md#package-group-word-boundary-prefix").
      - **All**: Match all packages.

   5. Choose **Next** to review the definition.

6. To enter the package group definition with text:
   1. Choose **Text** to switch to the text mode.
   2. In **Package group definition**, enter the package group definition. For more information about package group definition syntax, see
      [Package group definition syntax and matching behavior](package-group-definition-syntax-matching-behavior.md "package-group-definition-syntax-matching-behavior.md").
   3. Choose **Next** to review the definition.

7. In **Review definition**, review the packages that will be included in the new package
   group based on the definition provided previously. After reviewing, choose **Next**.
8. In **Package group information**, optionally add a description and contact email for the package group.
   Choose **Next**.
9. In **Package origin controls**, configure the origin controls to be applied to the packages in the group.
   For more information about package group origin controls, see [Package group origin controls](package-group-origin-controls.md "package-group-origin-controls.md").
10. Choose **Create package group**.

## Create a package group (AWS CLI)

Use the `create-package-group` command to create a package group in your domain. For the `--package-group` option, enter the
package group definition that determines which packages are associated with the group. For more information about package group definition syntax, see
[Package group definition syntax and matching behavior](package-group-definition-syntax-matching-behavior.md "package-group-definition-syntax-matching-behavior.md").

If you haven't, configure the AWS CLI by following the steps in [Setting up with AWS CodeArtifact](get-set-up-for-codeartifact.md "get-set-up-for-codeartifact.md").

```
aws codeartifact create-package-group \
         --domain `my_domain` \
         --package-group `'/nuget/*'` \
         --domain-owner `111122223333` \
         --contact-info `contact@email.com` \
         --description `"a new package group"` \
         --tags key=`key1`,value=`value1`
```
