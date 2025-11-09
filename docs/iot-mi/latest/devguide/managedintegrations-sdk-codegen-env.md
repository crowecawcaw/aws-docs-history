# Environment setup

Learn how to configure your environment to use the `codegen.py` code generator.

###### Topics

- [Prerequisites](#managedintegrations-sdk-codegen-env-prereq "#managedintegrations-sdk-codegen-env-prereq")
- [Configure your environment](#managedintegrations-sdk-codegen-env-setup "#managedintegrations-sdk-codegen-env-setup")

## Prerequisites

Install the following items before you configure your environment:

- Git
- Python 3.10 or higher
- Poetry 1.2.0 or higher

## Configure your environment

Use the following procedure to configure your environment to use the codegen.py code generator.

1. Download the latest version of the [End device SDK](managedintegrations-sdk-devices.md "managedintegrations-sdk-devices.md") from the AWS Management Console.
2. Set up the Python environment. The **codegen** project is python-based and uses Poetry for dependency management.
   1. Install project dependencies using poetry in the `codegen` directory:

   ```
   poetry run poetry install --no-root
   ```

3. Set up your repository.
   1. Clone the **connectedhomeip**
      repository. It uses the `codegen.py` script located in the
      `connectedhomeip/scripts/` folder for code generation. For more
      information, see [connectedhomeip](https://github.com/project-chip/connectedhomeip "https://github.com/project-chip/connectedhomeip") on _GitHub._

   ```
   git clone -b v1.4.0.0 https://github.com/project-chip/connectedhomeip.git
   ```

   2. Clone it at the same level as your
      `IoT-managed-integrations-End-Device-SDK` root folder. Your folder
      structure should match the following:

   ```
     |-connectedhomeip
     |-IoT-managed-integrations-End-Device-SDK
   ```

###### Note

You don't need to recursively clone submodules.
