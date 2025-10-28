# Connect a CodeArtifact repository to a public repository

You can add a external connection between a CodeArtifact repository and an external, public repository
such as [https://npmjs.com](https://npmjs.com "https://npmjs.com") or the [Maven Central
repository](https://repo.maven.apache.org/maven2/ "https://repo.maven.apache.org/maven2/"). Then, when
you request a package from the CodeArtifact repository that's not already present in the
repository, the package can be fetched from the external connection. This makes it possible
to consume open-source dependencies used by your application.

In CodeArtifact, the intended way to use external connections is to have one repository per domain with an external connection to a given public repository.
For example, if you want to connect to npmjs.com, configure one repository in your domain with an external connection to
npmjs.com and configure all the other repositories with an upstream to it. This way, all the repositories can make use of the packages that have already
been fetched from npmjs.com, rather than fetching and storing them again.

###### Topics

- [Connect to an external repository (console)](#adding-an-external-connection-console "#adding-an-external-connection-console")
- [Connect to an external repository (CLI)](#adding-an-external-connection "#adding-an-external-connection")
- [Supported external connection
  repositories](#supported-public-repositories "#supported-public-repositories")
- [Remove an external connection (CLI)](#removing-an-external-connection "#removing-an-external-connection")

## Connect to an external repository (console)

When you use the console to add a connection to an external repository, the following will occur:

1. A `-store` repository for the external repository will be created in your CodeArtifact domain if one does not exist already.
   These `-store` repositories behave as intermediate repositories between your repository and the external repository and allow you to connect to
   more than one external repository.
2. The appropriate `-store` repository is added as an upstream to your repository.

The following list contains each `-store` repository in CodeArtifact and the respective external repository they connect to.

1. `cargo-store` is connected to crates.io.
2. `clojars-store` is connected to Clojars Repository.
3. `commonsware-store` is connected to CommonsWare Android Repository.
4. `google-android-store` is connected to Google Android.
5. `gradle-plugins-store` is connected to Gradle plugins.
6. `maven-central-store` is connected to Maven Central Repository.
7. `npm-store` is connected to npmjs.com.
8. `nuget-store` is connected to nuget.org.
9. `pypi-store` is connected to the Python Packaging Authority.
10. `rubygems-store` is connected to RubyGems.org.

###### To connect to an external repository (console)

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. In the navigation pane, choose **Domains**, and then choose the
   domain name that contains your repository.
3. Choose the name of your repository.
4. Choose **Edit**.
5. In **Upstream repositories**, choose **Associate upstream repository** and add the appropriate `-store` repository
   that is connected as an upstream.
6. Choose **Update repository**.

After the `-store` repository is added as an upstream repository, package managers connected to your CodeArtifact repository can fetch
packages from the respective external repository.

## Connect to an external repository (CLI)

You can use the AWS CLI to connect your CodeArtifact repository to an external repository by adding an external connection directly to the repository. This will
allow users connected to the CodeArtifact repository, or any of its downstream repositories, to fetch packages from the configured external repository. Each CodeArtifact repository can only have one external connection.

It is recommended to have one repository per domain with an external connection to a given public repository. To
connect other repositories to the public repository, add the repository with the external connection as an upstream to them.
If you or someone else in your domain has already configured external connections in the console, your domain likely already has a `-store` repository with an external connection to the
public repository you want to connect to. For
more information about `-store` repositories and connecting with the console, see [Connect to an external repository (console)](#adding-an-external-connection-console "#adding-an-external-connection-console").

###### To add an external connection to a CodeArtifact repository (CLI)

- Use `associate-external-connection` to add an external connection. The following example connects a repository to the npm public registry, npmjs.com.
  For a list of supported external repositories, see [Supported external connection
  repositories](#supported-public-repositories "#supported-public-repositories").

```
aws codeartifact associate-external-connection --external-connection `public:npmjs` \
    --domain `my_domain` --domain-owner `111122223333` --repository `my_repo`
```

Example output:

```
{
    "repository": {
        "name": `my_repo`
        "administratorAccount": "`123456789012`",
        "domainName": "`my_domain`",
        "domainOwner": "`111122223333`",
        "arn": "arn:aws:codeartifact:`us-west-2`:`111122223333`:repository/`my_domain`/`my_repo`",
        "description": "`A description of my_repo`",
        "upstreams": [],
        "externalConnections": [
            {
                "externalConnectionName": "`public:npmjs`",
                "packageFormat": "npm",
                "status": "AVAILABLE"
            }
        ]
    }
}
```

After adding an external connection, see
[Requesting packages from external connections](external-connection-requesting-packages.md "external-connection-requesting-packages.md")
for information about requesting packages from an external repository with an external connection.

## Supported external connection

repositories

CodeArtifact supports an external connection to the following public repositories. To use
the CodeArtifact CLI to specify an external connection, use the value in the **Name** column for the `--external-connection`
parameter when you run the `associate-external-connection` command.

| Repository type | Description                    | Name                         |
| --------------- | ------------------------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maven           | Clojars repository             | `public:maven-clojars`       |
| Maven           | CommonsWare Android repository | `public:maven-commonsware`   |
| Maven           | Google Android repository      | `public:maven-googleandroid` |
| Maven           | Gradle plugins repository      | `public:maven-gradleplugins` |
| Maven           | Maven Central                  | `public:maven-central`       |
| npm             | npm public registry            | `public:npmjs`               |
| NuGet           | NuGet Gallery                  | `public:nuget-org`           |
| Python          | Python Package Index           | `public:pypi`                |
| Ruby            | RubyGems.org                   | `public:ruby-gems-org`       |
| Rust            | Crates.io                      | `public:crates-io`           | ## Remove an external connection (CLI) To remove an external connection that was added by using the `associate-external-connection` command in the AWS CLI, use `disassociate-external-connection`. `` aws codeartifact disassociate-external-connection --external-connection `public:npmjs` \ --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` `` Example output: ``{ "repository": { "name": `my_repo` "administratorAccount": "`123456789012`", "domainName": "`my_domain`", "domainOwner": "`111122223333`", "arn": "arn:aws:codeartifact:`us-west-2`:`111122223333`:repository/`my_domain`/`my_repo`", "description": "`A description of my_repo`", "upstreams": [], "externalConnections": [] } }`` |
