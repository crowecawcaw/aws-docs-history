# Installing Guard for Windows

You can install AWS CloudFormation Guard for Windows through Cargo or through Chocolatey.

## Prerequisites

To build Guard from the command line interface, you must install the Build Tools for
Visual Studio 2019.

1. Download Microsoft Visual C++ build tools from the [Build
   Tools for Visual Studio 2019](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019 "https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019") website.
2. Run the installer, and select the defaults.

## Install Guard from Cargo

Cargo is the Rust package manager. Complete the following steps to install Rust, which includes
Cargo. Then, install Guard from Cargo.

1. [Download Rust](https://forge.rust-lang.org/infra/other-installation-methods.html#other-ways-to-install-rustup "https://forge.rust-lang.org/infra/other-installation-methods.html#other-ways-to-install-rustup") and then run **rustup-init.exe**.
2. From the command prompt, choose **1**, which is the default
   option.

The command returns the following output.

```
Rust is installed now. Great!

    To get started you may need to restart your current shell.
    This would reload its PATH environment variable to include
    Cargo's bin directory (%USERPROFILE%\.cargo\bin).

    Press the Enter key to continue.
```

3. To finish the installation, press the **Enter** key.
4. With Cargo installed, run the following command to install Guard.

```
cargo install cfn-guard
```

_Results_: You have successfully installed
Guard.

    1. (Optional) To confirm the installation of Guard, run the following command.



    ```
    cfn-guard --version
    ```

    The command returns the following output.



    ```
    cfn-guard 3.1.2
    ```

## Install Guard from Chocolatey

Chocolatey is a package manager for Windows. Complete the following steps to install Chocolatey.
Then, install Guard from Chocolatey.

1. Follow this guide to [install Chocolatey](https://chocolatey.org/install "https://chocolatey.org/install")
2. With Chocolatey installed, run the following command to install Guard.

```
choco install cloudformation-guard
```

_Results_: You have successfully installed
Guard.

    1. (Optional) To confirm the installation of Guard, run the following command.



    ```
    cfn-guard --version
    ```

    The command returns the following output.



    ```
    cfn-guard 3.1.2
    ```
