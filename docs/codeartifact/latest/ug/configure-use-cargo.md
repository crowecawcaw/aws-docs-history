# Configure and use Cargo with CodeArtifact

You can use Cargo to publish and download crates from CodeArtifact repositories or to fetch crates from
[crates.io](https://crates.io/ "https://crates.io/"), the Rust community's crate registry. This topic
describes how to configure Cargo to authenticate with and use a CodeArtifact repository.

## Configure Cargo with CodeArtifact

To use Cargo to install and publish crates from AWS CodeArtifact,
you'll first need to configure them with your CodeArtifact repository information. Follow
the steps in one of the following procedure to configure Cargo with your CodeArtifact repository endpoint information and credentials.

### Configure Cargo using the console instructions

You can use configuration instructions in the console to connect Cargo to your CodeArtifact repository. The console
instructions provide a Cargo configuration customized for your CodeArtifact repository. You can use this custom configuration
to set up Cargo without needing to find and fill in your CodeArtifact information.

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. In the navigation pane, choose **Repositories**, and then
   choose a repository to connect to Cargo.
3. Choose **View connection instructions**.
4. Choose your operating system.
5. Choose **Cargo**.
6. Follow the generated instructions to connect Cargo to your CodeArtifact repository.

### Configure Cargo manually

If you cannot or do not want to use the configuration instructions from the console, you can use the following instructions to
connect Cargo to your CodeArtifact repository manually.

macOS and Linux
In order to configure Cargo with CodeArtifact, you need to define your CodeArtifact repository as a registry in
the Cargo configuration and provide credentials.

- Replace `my_registry` with your registry name.
- Replace `my_domain` with your CodeArtifact domain name.
- Replace `111122223333` with the AWS account ID of the owner of the domain. If you are accessing a repository in a domain that you own, you don't need to include
  `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").
- Replace `my_repo` with your CodeArtifact repository name.

Copy the configuration to publish and download Cargo packages to your repository and save it in the `~/.cargo/config.toml`
file for a system-level configuration or `.cargo/config.toml` for a project-level configuration:

```
[registries.`my_registry`]
index = "sparse+https://`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/cargo/`my_repo`/"
credential-provider = "cargo:token-from-stdout aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --region `us-west-2` --query authorizationToken --output text"

[registry]
default = "`my_registry`"

[source.crates-io]
replace-with = "`my_registry`"
```

Windows: Download packages only
In order to configure Cargo with CodeArtifact, you need to define your CodeArtifact repository as a registry in
the Cargo configuration and provide credentials.

- Replace `my_registry` with your registry name.
- Replace `my_domain` with your CodeArtifact domain name.
- Replace `111122223333` with the AWS account ID of the owner of the domain. If you are accessing a repository in a domain that you own, you don't need to include
  `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").
- Replace `my_repo` with your CodeArtifact repository name.

Copy the configuration to only download Cargo packages from your repository and save it in the `%USERPROFILE%\.cargo\config.toml`
file for a system-level configuration or `.cargo\config.toml` for a project-level configuration:

```
[registries.`my_registry`]
index = "sparse+https://`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/cargo/`my_repo`/"
credential-provider = "cargo:token-from-stdout aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --region `us-west-2` --query authorizationToken --output text"

[registry]
default = "`my_registry`"

[source.crates-io]
replace-with = "`my_registry`"
```

Windows: Publish and download packages

1.  In order to configure Cargo with CodeArtifact, you need to define your CodeArtifact repository as a registry in
    the Cargo configuration and provide credentials.

        * Replace `my_registry` with your registry name.
        * Replace `my_domain` with your CodeArtifact domain name.
        * Replace `111122223333` with the AWS account ID of the owner of the domain. If you are accessing a repository in a domain that you own, you don't need to include
         `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").
        * Replace `my_repo` with your CodeArtifact repository name.

    Copy the configuration to publish and download Cargo packages to your repository and save it in the `%USERPROFILE%\.cargo\config.toml`
    file for a system-level configuration or `.cargo\config.toml` for a project-level configuration.

It is recommended that you use the credential provider
`cargo:token`, which uses the credentials stored in your `~/.cargo/credentials.toml` file. You may run into an
error during `cargo publish` if you use `cargo:token-from-stdout` because the Cargo client doesn't trim the
authorization token properly during `cargo publish`.

```
[registries.`my_registry`]
index = "sparse+https://`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/cargo/`my_repo`/"
credential-provider = "cargo:token"

[registry]
default = "`my_registry`"

[source.crates-io]
replace-with = "`my_registry`"
```

2. To publish Cargo packages to your repository with Windows, you must use the
   CodeArtifact `get-authorization-token` command and Cargo `login` command to
   fetch an authorization token and your credentials.
   - Replace `my_registry` with your registry name as defined in `[registries.`my_registry`]`.
   - Replace `my_domain` with your CodeArtifact domain name.
   - Replace `111122223333` with the AWS account ID of the owner of the domain. If you are accessing a repository in a domain that you own, you don't need to include
     `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").

```
aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --region `us-west-2` --query authorizationToken --output text | cargo login --registry `my_registry`
```

###### Note

The authorization token generated is valid for 12 hours. You will need to create a new one
if 12 hours have passed since a token was created.

The `[registries.`my_registry`]` section in the preceding example
defines a registry with `my_registry` and provides `index`
and `credential-provider` information.

- `index` specifies the URL of the index for your registry, which is the CodeArtifact repository endpoint
  that ends with a `/`. The `sparse+` prefix is required for registries that are not
  Git repositories.

###### Note

To use a dualstack endpoint, use the `codeartifact.`region`.on.aws` endpoint.

- `credential-provider` specifies the credential provider for the given registry. If `credential-provider` isn't set,
  the providers in `registry.global-credential-providers` will be used. By setting `credential-provider` to
  `cargo:token-from-stdout`, the Cargo client will fetch new authorization token automatically when
  publishing or downloading from your CodeArtifact repository, therefore you don't need to manually refresh the authorization token every 12 hours.

The `[registry]` section defines the default registry used.

- `default` specifies the name of the registry defined in `[registries.`my_registry`]`,
  to use by default when publishing or downloading from your CodeArtifact repository.

The `[source.crates-io]` section defines the default registry used when one isn't specified.

- `replace-with = "`my_registry`"` replaces the public registry, crates.io
  with your CodeArtifact repository defined in `[registries.`my_registry`]`. This configuration is
  recommended if you need to request packages from the external connection such as crates.io.

To get all of the benefits of CodeArtifact, such as the package origin control that prevents dependency confusion attacks,
it is recommended that you use source replacement. With the source replacement, CodeArtifact
proxies all requests to the external connection and copies the package from the external connection to your repository. Without the
source replacement, the Cargo client will directly retrieve the package based on the configuration in your `Cargo.toml`
file in your project. If a dependency is not marked with `registry=`my_registry``,
the Cargo client will retrieve it directly from crates.io without communicating with your CodeArtifact repository.

###### Note

If you start using source replacement and then update your configuration file to not use source replacement, you may
encounter errors. The opposite scenario may also lead to errors. Therefore, it is recommended that you avoid changing the
configuration for your project.

## Installing Cargo crates

Use the following procedures to install Cargo crates from a CodeArtifact repository or from [crates.io](https://crates.io/ "https://crates.io/").

### Install Cargo crates from CodeArtifact

You can use the Cargo (`cargo`) CLI to quickly install a specific version of a Cargo crate from your CodeArtifact repository.

###### To install Cargo crates from a CodeArtifact repository with `cargo`

1. If you haven't, follow the steps in [Configure and use Cargo with CodeArtifact](configure-use-cargo.md "configure-use-cargo.md") to
   configure the `cargo` CLI to use your CodeArtifact repository with proper credentials.
2. Use the following command to install Cargo crates from CodeArtifact:

```
cargo add my_cargo_package@`1.0.0`
```

For more information, see [cargo add](https://doc.rust-lang.org/cargo/commands/cargo-add.html "https://doc.rust-lang.org/cargo/commands/cargo-add.html")
in _The Cargo Book_.

## Publishing Cargo crates to CodeArtifact

Use the following procedure to publish Cargo crates to a CodeArtifact repository using the `cargo` CLI.

1. If you haven't, follow the steps in [Configure and use Cargo with CodeArtifact](configure-use-cargo.md "configure-use-cargo.md") to
   configure the `cargo` CLI to use your CodeArtifact repository with proper credentials.
2. Use the following command to publish Cargo crates to a CodeArtifact repository:

```
cargo publish
```

For more information, see [cargo publish](https://doc.rust-lang.org/cargo/commands/cargo-publish.html "https://doc.rust-lang.org/cargo/commands/cargo-publish.html")
in _The Cargo Book_.
