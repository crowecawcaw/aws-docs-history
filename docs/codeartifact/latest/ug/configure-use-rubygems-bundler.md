# Configure and use RubyGems and Bundler with CodeArtifact

After you create a repository in CodeArtifact, you can use RubyGems (`gem`) and Bundler (`bundle`) to install and publish gems. This topic
describes how to configure the package managers to authenticate with and use a CodeArtifact repository.

## Configure RubyGems (`gem`) and Bundler (`bundle`) with CodeArtifact

To use RubyGems (`gem`) or Bundler (`bundle`) to publish gems to or consume gems from AWS CodeArtifact,
you'll first need to configure them with your CodeArtifact repository information, including credentials to access it. Follow
the steps in one of the following procedure to configure the `gem` and `bundle` CLI tools with your
CodeArtifact repository endpoint information and credentials.

### Configure RubyGems and Bundler using the console instructions

You can use configuration instructions in the console to connect your Ruby package managers to your CodeArtifact repository. The console
instructions provide custom commands that you can run to set up your package managers without needing to find and fill in your CodeArtifact information.

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. In the navigation pane, choose **Repositories**, and then
   choose the repository that you want to use for installing or pushing Ruby gems.
3. Choose **View connection instructions**.
4. Choose your operating system.
5. Choose the Ruby package manager client that you want to configure with your CodeArtifact repository.
6. Follow the generated instructions to configure the package manager client to install Ruby gems from or publish Ruby gems to the repository.

### Configure RubyGems and Bundler manually

If you cannot or do not want to use the configuration instructions from the console, you can use the following instructions to
connect to your Ruby package managers to your CodeArtifact repository manually.

1. In a command line, use the following command to fetch a CodeArtifact authorization token and store it in an environment variable.
   - Replace `my_domain` with your CodeArtifact domain name.
   - Replace `111122223333` with the AWS account ID of the owner of the domain. If you are accessing a repository in a domain that you own, you don't need to include
     `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").

macOS and Linux

```
export CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --query authorizationToken --output text`
```

Windows

    * Windows (using default command shell):



    ```
    for /f %i in ('aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --query authorizationToken --output text') do set CODEARTIFACT_AUTH_TOKEN=%i
    ```
    * Windows PowerShell:



    ```
    $env:CODEARTIFACT_AUTH_TOKEN = aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --query authorizationToken --output text
    ```

2. To publish Ruby gems to your repository, use the following command to fetch your CodeArtifact repository's endpoint and storing it in the
   `RUBYGEMS_HOST` environment variable. The `gem` CLI uses this environment variable to determine where gems are published.

###### Note

Alternatively, instead of using the `RUBYGEMS_HOST` environment variable, you can provide the repository endpoint
with the `--host` option when using the `gem push` command.

    * Replace `my_domain` with your CodeArtifact domain name.
    * Replace `111122223333` with the AWS account ID of the owner of the domain.
     If you are accessing a repository in a domain that you own, you don't need to include
     `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").
    * Replace `my_repo` with your CodeArtifact repository name.

macOS and Linux

```
export RUBYGEMS_HOST=`aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format ruby --query repositoryEndpoint --output text | sed 's:/*$::'`
```

Windows
The following commands retrieve the repository endpoint, trim the trailing `/`, then store them in an environment variable.

    * Windows (using default command shell):



    ```
    for /f %i in ('aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format ruby --query repositoryEndpoint --output text') do set RUBYGEMS_HOST=%i

    set RUBYGEMS_HOST=%RUBYGEMS_HOST:~0,-1%
    ```
    * Windows PowerShell:



    ```
    $env:RUBYGEMS_HOST = (aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format ruby --query repositoryEndpoint --output text).TrimEnd("/")
    ```

The following URL is an example repository endpoint:

```
https://`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/ruby/`my_repo`/
```

###### Note

To use a dualstack endpoint, use the `codeartifact.`region`.on.aws` endpoint. 3. To publish Ruby gems to your repository, you must authenticate to CodeArtifact with RubyGems by editing your `~/.gem/credentials`
file to include your auth token. Create a `~/.gem/` directory and a `~/.gem/credentials` file if the directory or file doesn't exist.

macOS and Linux

```
echo ":codeartifact_api_key: Bearer $CODEARTIFACT_AUTH_TOKEN" >> ~/.gem/credentials
```

Windows

    * Windows (using default command shell):



    ```
    echo :codeartifact_api_key: Bearer %CODEARTIFACT_AUTH_TOKEN% >> %USERPROFILE%/.gem/credentials
    ```
    * Windows PowerShell:



    ```
    echo ":codeartifact_api_key: Bearer $env:CODEARTIFACT_AUTH_TOKEN" | Add-Content ~/.gem/credentials
    ```

4. To use `gem` to install Ruby gems from your repository, you must add the repository endpoint information and auth token
   to your `.gemrc` file. You can add it to the global file (`~/.gemrc`) or your project `.gemrc` file.
   The CodeArtifact information you must add to the `.gemrc` is a combination of the repository endpoint and auth token. It is formatted as follows:

```
https://aws:${CODEARTIFACT_AUTH_TOKEN}@`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/ruby/`my_repo`/
```

    * For the authentication token, you can use the `CODEARTIFACT_AUTH_TOKEN` environment variable that was set in an earlier step.
    * To fetch the repository endpoint, you can read the value of the `RUBYGEMS_HOST` environment
     variable that was set earlier, or you can use the following `get-repository-endpoint` command, replacing the values as necessary:



    ```
    aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format ruby --query repositoryEndpoint --output text
    ```

After you have the endpoint, use a text editor to add `aws:${CODEARTIFACT_AUTH_TOKEN}@` in the appropriate position. Once you have
the repository endpoint and auth token string created, add it to the `:sources:` section of your `.gemrc` file with the `echo` command as follows:

###### Warning

CodeArtifact does not support adding repositories as sources using the `gem sources -add` command. You must add the source directly to the file.

macOS and Linux

```
echo ":sources:
    - https://aws:${CODEARTIFACT_AUTH_TOKEN}@`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/ruby/`my_repo`/" > ~/.gemrc
```

Windows

    * Windows (using default command shell):



    ```
    echo ":sources:
        - https://aws:%CODEARTIFACT_AUTH_TOKEN%@`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/ruby/`my_repo`/" > "%USERPROFILE%\.gemrc"
    ```
    * Windows PowerShell:



    ```
    echo ":sources:
        - https://aws:$env:CODEARTIFACT_AUTH_TOKEN@`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/ruby/`my_repo`/" | Add-Content ~/.gemrc
    ```

5. To use Bundler, you must configure Bundler with your repository endpoint URL and authentication token by
   running the following `bundle config` command:

macOS and Linux

```
bundle config $RUBYGEMS_HOST aws:$CODEARTIFACT_AUTH_TOKEN
```

Windows

    * Windows (using default command shell):



    ```
    bundle config %RUBYGEMS_HOST% aws:%CODEARTIFACT_AUTH_TOKEN%
    ```
    * Windows PowerShell:



    ```
    bundle config $Env:RUBYGEMS_HOST aws:$Env:CODEARTIFACT_AUTH_TOKEN
    ```

Now that you've configured RubyGems (`gem`) and Bundler (`bundle`) with your CodeArtifact repository, you can use
them to publish and consume Ruby gems to and from it.

## Installing Ruby gems from CodeArtifact

Use the following procedures to install Ruby gems from an CodeArtifact repository with the `gem` or `bundle` CLI tools.

### Install Ruby gems with `gem`

You can use the RubyGems (`gem`) CLI to quickly install a specific version of a Ruby gem from your CodeArtifact repository.

###### To install Ruby gems from a CodeArtifact repository with `gem`

1. If you haven't, follow the steps in [Configure RubyGems (gem) and Bundler (bundle) with CodeArtifact](#configure-ruby-gem "#configure-ruby-gem") to
   configure the `gem` CLI to use your CodeArtifact repository with proper credentials.

###### Note

The authorization token generated is valid for 12 hours. You will need to create a new one if 12 hours have passed since a token was created. 2. Use the following command to install Ruby gems from CodeArtifact:

```
gem install `my_ruby_gem` --version `1.0.0`
```

### Install Ruby gems with `bundle`

You can use the Bundler (`bundle`) CLI to install the Ruby gems that are configured in your `Gemfile`.

###### To install Ruby gems from a CodeArtifact repository with `bundle`

1. If you haven't, follow the steps in [Configure RubyGems (gem) and Bundler (bundle) with CodeArtifact](#configure-ruby-gem "#configure-ruby-gem") to
   configure the `bundle` CLI to use your CodeArtifact repository with proper credentials.

###### Note

The authorization token generated is valid for 12 hours. You will need to create a new one if 12 hours have passed since a token was created. 2. Add your CodeArtifact repository endpoint URL to your `Gemfile` as a `source`
to install configured Ruby gems from your CodeArtifact repository and its upstreams.

```
source "https://`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com/ruby/`my_repo`/"

gem 'my_ruby_gem'
```

3. Use the following command to install the Ruby gems as specified in your `Gemfile`:

```
bundle install
```

## Publishing Ruby gems to CodeArtifact

Use the following procedure to publish Ruby gems to a CodeArtifact repository using the `gem` CLI.

1. If you haven't, follow the steps in [Configure RubyGems (gem) and Bundler (bundle) with CodeArtifact](#configure-ruby-gem "#configure-ruby-gem") to
   configure the `gem` CLI to use your CodeArtifact repository with proper credentials.

###### Note

The authorization token generated is valid for 12 hours. You will need to create a new one if 12 hours have passed since a token was created. 2. Use the following command to publish Ruby gems to a CodeArtifact repository. Note that if you did not set the `RUBYGEMS_HOST` environment
variable, you must provide your CodeArtifact repository endpoint in the `--host` option.

```
gem push --key codeartifact_api_key `my_ruby_gem-0.0.1.gem`
```
