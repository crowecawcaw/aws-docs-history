# What is a package URL?

[A package URL or PURL](https://github.com/package-url/purl-spec "https://github.com/package-url/purl-spec") is a standardized format used to identify software packages, components, and libraries across different package management systems.
The format makes it easier to track, analyze, and manage dependencies in software projects, particularly when generating a Software Bill of Materials (SBOMs).

## PURL structure

The PURL structure is similar to a URL and is composed of multiple components:

- `pkg` – The literal prefix
- `type`– The package type
- `namespace` – The grouping
- `name` – The package name
- `version` – The package version
- `qualifiers` – Extra key-value pairs
- `subpath` – The filepath in the package

###### Example PURL

The following is an example of how a PURL might look.

```
pkg:<type>/<namespace>/<name>@<version>?<qualifiers>#<subpath>
```

### The generic PURL

A generic PURL is used to represent software packages and components that don't fit into established package ecosystems, such as npm, pypi, or maven.
It identifies software components and captures metadata that might not align with specific package management systems.
A generic PURL is useful for a variety of software projects, from compiled binaries to platforms, such as Apache and WordPress.
Its allows it to be applied across a wide range of use cases, including compiled binaries, web platforms, and custom software distributions.

###### Key use cases

- Supports compiled binaries and is useful for Go and Rust
- Supports web platforms, such as Apache and WordPress, where a package might not be associated with traditional package managers.
- Supports custom legacy software by allowing organizations to reference internally developed software or systems lacking formal packages.

###### Example format

The following is an example of the generic PURL format.

```
pkg:generic/<namespace>/<name>@<version>?<qualifiers>
```

#### Additional examples of the generic PURL format

The following are additional examples of the generic PURL format.

###### Compiled Go binary

The following represents the `inspector-sbomgen binary` compiled with a Go.

```
pkg:generic/inspector-sbomgen?go_toolchain=1.22.5
```

###### Compiled Rust binary

The following represents the `myrustapp` binary compiled with Rust.

```
pkg:generic/myrustapp?rust_toolchain=1.71.0
```

###### Apache project

The following refers to an http project under the Apache namespace.

```
pkg:generic/apache/httpd@1.0.0
```

###### WordPress software

The following refers to a core WordPress software.

```
pkg:generic/wordpress/core/wordpress@6.0.0
```

###### WordPress theme

The following refers to a custom WordPress theme.

```
pkg:generic/wordpress/theme/mytheme@1.0.0
```

###### WordPress plugin

The following refers to a custom WordPress plugin.

```
pkg:generic/wordpress/plugin/myplugin@1.0.0
```
