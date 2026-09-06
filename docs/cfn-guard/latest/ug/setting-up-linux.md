

# Installing Guard for Linux and macOS
<a name="setting-up-linux"></a>

You can install AWS CloudFormation Guard for Linux and macOS by using the pre-built release binary, Cargo, or through Homebrew.

## Install Guard from a pre-built release binary
<a name="install-pre-built-binaries"></a>

Use the following procedure to install Guard from a pre-built binary.

1. Open a terminal, and run the following command.

   ```
   curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/aws-cloudformation/cloudformation-guard/main/install-guard.sh | sh
   ```

1. Run the following command to set your `PATH` variable.

   ```
   export PATH=~/.guard/bin:$PATH
   ```

   *Results:* You have successfully installed Guard and set the `PATH` variable.

   1. (Optional) To confirm the installation of Guard, run the following command.

     ```
     cfn-guard --version
     ```

     The command returns the following output.

     ```
     cfn-guard 3.1.2
     ```

## Install Guard from Cargo
<a name="install-guard-from-cargo"></a>

Cargo is the Rust package manager. Complete the following steps to install Rust, which includes Cargo. Then, install Guard from Cargo.

1. Run the following command from a terminal, and follow the onscreen instructions to install Rust.

   ```
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```

   1. (Optional) For Ubuntu environments, run the following command.

     ```
     sudo apt-get update; sudo apt install build-essential
     ```

1. Configure your `PATH` environment variable, and run the following command.

   ```
   source $HOME/.cargo/env
   ```

1. With Cargo installed, run the following command to install Guard.

   ```
   cargo install cfn-guard
   ```

   *Results*: You have successfully installed Guard.

   1. (Optional) To confirm the installation of Guard, run the following command.

     ```
     cfn-guard --version
     ```

     The command returns the following output.

     ```
     cfn-guard 3.1.2
     ```

## Install Guard from Homebrew
<a name="install-guard-from-homebrew"></a>

Homebrew is a package manager for macOS and Linux. Complete the following steps to install Homebrew. Then, install Guard from Homebrew.

1. Run the following command from a terminal, and follow the onscreen instructions to install Homebrew.

   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

1. With Homebrew installed, run the following command to install Guard.

   ```
   brew install cloudformation-guard
   ```

   *Results*: You have successfully installed Guard.

   1. (Optional) To confirm the installation of Guard, run the following command.

     ```
     cfn-guard --version
     ```

     The command returns the following output.

     ```
     cfn-guard 3.1.2
     ```