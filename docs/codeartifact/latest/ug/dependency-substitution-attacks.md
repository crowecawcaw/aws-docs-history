# Dependency substitution attacks

Package managers simplify the process of packaging and sharing reusable code. These
packages may be private packages developed by an organization for use in their applications,
or they may be public, typically open-source packages that are developed outside an organization and
distributed by public package repositories. When requesting packages, developers rely on their package manager
to fetch new versions of their dependencies. Dependency substitution attacks, also known as dependency
confusion attacks, exploit the fact that a package manager typically has no way to distinguish legitimate
versions of a package from malicious versions.

Dependency substitution attacks belong to a subset of hacks known as software supply chain attacks.
A software supply chain attack is an attack that takes advantage of vulnerabilities anywhere in the
software supply chain.

A dependency substitution attack can target anyone who uses both internally developed
packages and packages fetched from public repositories. The attackers identify internal
package names and then strategically place malicious code with the same name in public
package repositories. Typically, the malicious code is published in a package with a high version number.
Package managers fetch the malicious code from these public feeds
because they believe that the malicious packages are the latest versions of the package.
This causes a "confusion" or "substitution" between the desired package and the malicious
package, leading to the code being compromised.

To prevent dependency substitution attacks, AWS CodeArtifact provides package origin controls. Package origin controls are settings that control how packages can be added to your repositories.
The controls can be used to ensure package versions cannot be both published directly to your repository and ingested from public sources, protecting you from dependency substitution attacks. Origin
controls can be set on individual packages and multiple packages by setting origin controls on package groups.
For more information about package origin controls and how to change them, see [Editing package origin controls](package-origin-controls.md "package-origin-controls.md") and
[Package group origin controls](package-group-origin-controls.md "package-group-origin-controls.md").
