# Installing Guard for Linux and macOS

You can install AWS CloudFormation Guard for Linux and macOS by using the pre-built release binary,
Cargo, or through Homebrew.

## Install Guard from a pre-built release

binary

Use the following procedure to install Guard from a pre-built binary.

1. Open a terminal, and run the following command.

```
curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/aws-cloudformation/cloudformation-guard/main/install-guard.sh | sh
```

2. Run the following command to set your `PATH` variable.

```
export PATH=~/.guard/bin:$PATH
```

_Results:_ You have successfully installed Guard and set the
`PATH` variable.

    1. (Optional) To confirm the installation of Guard, run the following command.



    ```
    cfn-guard --version
    ```

    The command returns the following output.



    ```
    cfn-guard 3.1.2
    ```

## Install Guard from Cargo

Cargo is the Rust package manager. Complete the following steps to install Rust, which
includes Cargo. Then, install Guard from Cargo.

1. Run the following command from a terminal, and follow the onscreen instructions to install
   Rust.

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

    1. (Optional) For Ubuntu environments, run the following command.



    ```
    sudo apt-get update; sudo apt install build-essential
    ```

2. Configure your `PATH` environment variable, and run the following
   command.

```
source $HOME/.cargo/env
```

3. With Cargo installed, run the following command to install Guard.

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

## Install Guard from Homebrew

Homebrew is a package manager for macOS and Linux. Complete the following steps to install Homebrew.
Then, install Guard from Homebrew.

1. Run the following command from a terminal, and follow the onscreen instructions to install
   Homebrew.

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. With Homebrew installed, run the following command to install Guard.

```
brew install cloudformation-guard
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
