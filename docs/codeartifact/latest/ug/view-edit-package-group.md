# View or edit a package group

You can view a list of all package groups, view details of a specific package group, or edit a package group's
details or configuration using the CodeArtifact console or the AWS Command Line Interface (AWS CLI).

## View or edit a package group (console)

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. In the navigation pane, choose **Domains**, and then choose the domain that contains
   the package group you want to view or edit.
3. Choose **Package groups**, and choose the package group you want to view or edit.
4. In **Details**, view information about the package group including its parent group, description,
   ARN, contact email, and package origin controls.
5. In **Subgroups**, view a list of package groups that have this group as a parent group. The
   package groups in this list can inherit settings from this package group. For more information, see
   [Package group hierarchy and pattern specificity](package-group-definition-syntax-matching-behavior.md#package-group-hierarchy-pattern-specificity "package-group-definition-syntax-matching-behavior.md#package-group-hierarchy-pattern-specificity").
6. In **Packages**, view the packages that belong to this package group based on the package group
   definition. In the **Strength** column, you can see the strength of the package association. For more
   information, see [Package group hierarchy and pattern specificity](package-group-definition-syntax-matching-behavior.md#package-group-hierarchy-pattern-specificity "package-group-definition-syntax-matching-behavior.md#package-group-hierarchy-pattern-specificity").
7. To edit package group information, choose **Edit package group**.
   1. In **Information**, update the package group's description or contact information. You cannot edit
      a package group's definition.
   2. In **Package group origin controls**, update the package group's origin control settings, which determine how associated packages
      can enter repositories in the domain. For more information, see [Package group origin controls](package-group-origin-controls.md "package-group-origin-controls.md").

## View or edit a package group (AWS CLI)

Use the following commands to view or edit package groups with the AWS CLI. If you haven't, configure the AWS CLI by following the steps in [Setting up with AWS CodeArtifact](get-set-up-for-codeartifact.md "get-set-up-for-codeartifact.md").

To view all package groups in a domain, use the `list-package-groups` command.

```
aws codeartifact list-package-groups \
         --domain `my_domain` \
         --domain-owner `111122223333`
```

To view details about a package group, use the `describe-package-group` command. For more information about package group definitions, see
[Package group definition syntax and examples](package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples "package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples").

```
aws codeartifact describe-package-group \
         --domain `my_domain` \
         --domain-owner `111122223333` \
         --package-group `'/nuget/*'`
```

To view the child package groups of a package group, use the `list-sub-package-groups` command.

```
aws codeartifact list-sub-package-groups \
         --domain `my_domain` \
         --domain-owner `111122223333` \
         --package-group `'/nuget/*'` \
```

To view the package group that is associated to a package, use the `get-associated-package-group` command. You must use
the normalized package name and namespace for the NuGet, Python, and Swift package formats. For more information about how
the package names and namespaces are normalized, see the [NuGet](nuget-name-normalization.md "nuget-name-normalization.md"),
[Python](python-name-normalization.md "python-name-normalization.md"), and [Swift](swift-name-normalization.md "swift-name-normalization.md") name normalization documentation.

```
aws codeartifact get-associated-package-group \
         --domain `my_domain` \
         --domain-owner `111122223333` \
         --format `npm` \
         --package `packageName` \
         --namespace `scope`
```

To edit a package group, use the `update-package-group` command. This command is used to
update a package group's contact information or description. For information about package group origin control settings, and adding or editing them, see
[Package group origin controls](package-group-origin-controls.md "package-group-origin-controls.md"). For more information about package group definitions, see
[Package group definition syntax and examples](package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples "package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples")

```
aws codeartifact update-package-group \
         --domain `my_domain` \
         --package-group `'/nuget/*'` \
         --domain-owner `111122223333` \
         --contact-info `contact@email.com` \
         --description `"updated package group description"`
```
