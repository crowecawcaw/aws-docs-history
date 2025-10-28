# Setting up your Ruby development environment for Elastic Beanstalk

This chapter provides instructions to set up a Ruby development environment to test your application locally prior to deploying it to
AWS Elastic Beanstalk. It also references websites that provide installation instructions for useful tools.

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in
listings preceded by a
prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ `this is a command`
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10 "https://docs.microsoft.com/en-us/windows/wsl/install-win10") to get a Windows-integrated version of
Ubuntu and Bash.

###### Sections

- [Installing Ruby](#ruby-development-environment-ruby "#ruby-development-environment-ruby")
- [Installing the AWS SDK for Ruby](#ruby-development-environment-sdk "#ruby-development-environment-sdk")
- [Installing an IDE or text editor](#ruby-development-environment-ide "#ruby-development-environment-ide")

## Installing Ruby

Install GCC if you don't have a C compiler. On Ubuntu, use `apt`.

```
~$ `sudo apt install gcc`
```

On Amazon Linux, use `yum`.

```
~$ `sudo yum install gcc`
```

Install RVM to manage Ruby language installations on your machine. Use the commands at [rvm.io](https://rvm.io/ "https://rvm.io/") to get the project
keys and run the installation script.

```
~$ `gpg2 --recv-keys `key1` `key2``
~$ `curl -sSL https://get.rvm.io | bash -s stable`
```

This script installs RVM in a folder named `.rvm` in your user directory, and modifies your shell profile to load a setup script
whenever you open a new terminal. Load the script manually to get started.

```
~$ `source ~/.rvm/scripts/rvm`
```

Use `rvm get head` to get the latest version.

```
~$ `rvm get head`
```

View the available versions of Ruby.

```
~$ `rvm list known`
```

Check [Ruby](../platforms/platforms-supported.md#platforms-supported.ruby "../platforms/platforms-supported.md#platforms-supported.ruby") in the _AWS Elastic Beanstalk Platforms_
document to find the latest version of Ruby available on an Elastic Beanstalk platform. Install that version.

```
~$ `rvm install `3.2``
```

Test your Ruby installation.

```
~$ `ruby --version`
```

## Installing the AWS SDK for Ruby

If you need to manage AWS resources from within your application, install the AWS SDK for Ruby. For example, with the SDK for Ruby, you can use Amazon DynamoDB
(DynamoDB) to store user and session information without creating a relational database.

Install the SDK for Ruby and its dependencies with the `gem` command.

```
$ `gem install aws-sdk`
```

Visit the [AWS SDK for Ruby homepage](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/") for more information and installation instructions.

## Installing an IDE or text editor

Integrated development environments (IDEs) provide a wide range of features that facilitate application development. If you haven't used an IDE for
Ruby development, try Aptana and RubyMine and see which works best for you.

- [Install Aptana](https://github.com/aptana/studio3 "https://github.com/aptana/studio3")
- [RubyMine](https://www.jetbrains.com/ruby/ "https://www.jetbrains.com/ruby/")

###### Note

An IDE might add files to your project folder that you might not want to commit to source control. To prevent committing these files to source
control, use `.gitignore` or your source control tool's equivalent.

If you just want to begin coding and don't need all of the features of an IDE, consider [installing Sublime
Text](http://www.sublimetext.com/ "http://www.sublimetext.com/").
