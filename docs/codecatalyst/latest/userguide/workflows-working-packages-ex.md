Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Examples: Package repositories in

workflows

The following examples show how to reference packages in the workflow definition
file.

###### Topics

- [Example: Defining packages
  with NpmConfiguration](#workflows-working-packages-ex-basic "#workflows-working-packages-ex-basic")
- [Example:
  Overriding the default registry](#workflows-working-packages-ex-overriding-registry "#workflows-working-packages-ex-overriding-registry")
- [Example:
  Overriding scopes in your package registry](#workflows-working-packages-ex-overriding-scopes "#workflows-working-packages-ex-overriding-scopes")
- [Example: Manually
  configuring pip to authenticate with CodeCatalyst](#workflows-working-packages-pypi-token "#workflows-working-packages-pypi-token")

## Example: Defining packages

with `NpmConfiguration`

The following example shows how to define a package with
`NpmConfiguration` in your workflow definition file.

```
Actions:
  Build:
  Identifier: aws/build-beta@v1
  Configuration:
    Packages:
        NpmConfiguration:
          PackageRegistries:
            - PackagesRepository: main-repo
            - PackagesRepository: scoped-repo
              Scopes:
                - "@scope1"

```

This example configures the npm client as such:

```
default: main-repo
@scope1: scoped-repo
```

In this example, there are two repositories defined. The default registry is set
as `main-repo` as it is defined without a scope. Scope
`@scope1` is configured in `PackageRegistries` for
`scoped-repo`.

## Example:

Overriding the default registry

The following example shows you how to override the default registry.

```
NpmConfiguration:
  PackageRegistries:
    - PackagesRepository: my-repo-1
    - PackagesRepository: my-repo-2
    - PackagesRepository: my-repo-3
```

This example configures the npm client as such:

```
default: my-repo-3
```

If you specify multiple default repositories, the last repository will take
priority. In this example, the last repository listed is `my-repo-3`,
meaning that npm will connect to `my-repo-3`. This overrides the
repositories `my-repo-1` and `my-repo-2`.

## Example:

Overriding scopes in your package registry

The following example shows you how to override a scope in your package
registry.

```
NpmConfiguration:
  PackageRegistries:
    - PackagesRepository: my-default-repo
    - PackagesRepository: my-repo-1
      Scopes:
        - "@scope1"
        - "@scope2"
    - PackagesRepository: my-repo-2
      Scopes:
        - "@scope2"
```

This example configures the npm client as such:

```
default: my-default-repo
@scope1: my-repo-1
@scope2: my-repo-2
```

If you include overriding scopes, the last repository will take priority. In this
example, the last time that scope `@scope2` is configured in
`PackageRegistries` is for `my-repo-2`. This overrides the
scope `@scope2` configured for `my-repo-1`.

## Example: Manually

configuring `pip` to authenticate with CodeCatalyst

The following example shows you how to reference CodeCatalyst authorization environment
variables in a build action.

```
Actions:
  Build:
    Identifier: aws/build@v1.0.0
    Configuration:
      Steps:
        - Run: pip config set global.index-url https://$CATALYST_MACHINE_RESOURCE_NAME:$CATALYST_PACKAGES_AUTHORIZATION_TOKEN@codecatalyst.aws/pypi/my-space/my-project/my-repo/simple/
    Packages:
      ExportAuthorizationToken: true
```
