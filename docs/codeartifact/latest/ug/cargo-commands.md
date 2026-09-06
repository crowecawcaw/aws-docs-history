

# Cargo command support
<a name="cargo-commands"></a>

The following sections summarize the Cargo commands that are supported by CodeArtifact repositories, in addition to specific commands that are not supported.

**Contents**
+ [Supported commands that require accessing the registry](#supported-commands-access-the-registry)
+ [Unsupported commands](#unsupported-commands)

## Supported commands that require accessing the registry
<a name="supported-commands-access-the-registry"></a>

This section lists Cargo commands where the Cargo client requires access to the registry it's been configured with. These commands have been verified to function correctly when invoked against a CodeArtifact repository.



| Command | Description | 
| --- | --- | 
|  [build](https://doc.rust-lang.org/cargo/commands/cargo-build.html)  | Builds local packages and their dependencies. | 
|  [check](https://doc.rust-lang.org/cargo/commands/cargo-check.html)  | Checks local packages and their dependencies for errors. | 
|  [fetch](https://doc.rust-lang.org/cargo/commands/cargo-fetch.html)  | Fetches the dependencies of a package. | 
|  [publish](https://doc.rust-lang.org/cargo/commands/cargo-publish.html)  | Publishes a package to the registry. | 

## Unsupported commands
<a name="unsupported-commands"></a>

These Cargo commands are not supported by CodeArtifact repositories.



| Command | Description | 
| --- | --- | 
|  [owner](https://doc.rust-lang.org/cargo/commands/cargo-owner.html)  | Manages the owners of the crate on the registry. | 
|  [search](https://doc.rust-lang.org/cargo/commands/cargo-search.html)  | Searches for packages in the registry. | 