# Running a transformation on the command line with Amazon Q Developer

Complete these steps to transform your code on the command line with the Amazon Q Developer command line
tool.

## Prerequisites

Before you begin a transformation on the command line, the following prerequisites must be
met:

- If you're upgrading your Java code version, your project meets the [prerequisites for upgrading Java versions
  with Amazon Q](code-transformation.md#java-upgrade-prerequisites "code-transformation.md#java-upgrade-prerequisites").
- If you're converting embedded SQL in a Java application, your application meets the
  [prerequisites for converting embedded SQL
  with Amazon Q](transform-sql.md#sql-transform-prereqs "transform-sql.md#sql-transform-prereqs").
- You have Python installed on your command line environment. This is how you will
  install the command line tool. The minimum supported Python version is 3.12.
- You are running the transformation on macOS or Linux.
- The size of your application is 2 GB or smaller.
- If you have specific dependencies you want Amazon Q to upgrade, you have
  configured a [dependency upgrade file](#step-3-dependency-upgrade-file "#step-3-dependency-upgrade-file").

## Step 1: Choose authentication method and add permissions

You can authenticate IAM Identity Center to run transformations on the command
line. Ensure you have the proper permissions.

###### Note

Customer managed keys aren't supported for transformations performed on the command
line.

### Add permissions

The IAM identity associated with the Amazon Q Developer subscription you are using
to authenticate must have permissions to perform transformations on the command
line. Before you proceed, ensure your IAM identity has the permissions defined
in [Allow users to run transformations on the command line](id-based-policy-examples-users.md#id-based-policy-examples-allow-cli-transformations "id-based-policy-examples-users.md#id-based-policy-examples-allow-cli-transformations").

### Authenticate with IAM Identity Center through a Amazon Q Developer subscription

To authenticate with IAM Identity Center, you must be [subscribed to
Amazon Q Developer Pro as a workforce user](subscribe-users.md "subscribe-users.md") by your administrator, and you must provide the Start URL to
authenticate through your subscription. You or your administrator can find the Start URL
in the Amazon Q Developer console. For more information see, [Finding the Start URL for use with Amazon Q Developer](manage-account-details.md "manage-account-details.md").

To add required permissions, see [Add permissions](#transform-CLI-add-permissions "#transform-CLI-add-permissions").

You provide the Start URL in [Step 4: Configure and authenticate](#step-4-configure-auth "#step-4-configure-auth").

## Step 2: Install the tool

1. [Download
   the Amazon Q command line tool for transformations](https://desktop-release.codewhisperer.us-east-1.amazonaws.com/amzn_qct_cli/amzn_qct_cli-1.2.2.zip "https://desktop-release.codewhisperer.us-east-1.amazonaws.com/amzn_qct_cli/amzn_qct_cli-1.2.2.zip") and unzip
   it.

To download a previous version of the command line tool, see [Version history](transform-CLI-versions.md "transform-CLI-versions.md"). 2. We recommend that you set up a virtual environment in Python to install
the tool. To create a virtual environment, open a terminal window in the
directory where you want to install the tool and run:

```
python -m venv qct-cli
```

3. To activate the virtual environment, run:

```
source qct-cli/bin/activate
```

4. To install the tool on your command line, run the following command with
   the path to where you unzipped the tool, based on your machine
   architecture:

Linux_aarch64

```
pip install <path/to/unzipped-tool>/Linux_aarch64/amzn_qct_cli-1.2.2-py3-none-any.whl
```

Linux_x86_64

```
pip install <path/to/unzipped-tool>/Linux_x86_64/amzn_qct_cli-1.2.2-py3-none-any.whl
```

###### Note

If you are using an older version of the command line tool for transformations,
replace `1.2.2` with the [version](transform-CLI-versions.md "transform-CLI-versions.md") you downloaded. 5. To verify that the tool was installed, run:

```
which qct
```

## Step 3: Create a dependency upgrade file (optional)

You can provide Amazon Q with a _dependency upgrade file_, a YAML
file that lists your project's dependencies and which versions to upgrade to during
a transformation. By providing a dependency upgrade file, you can specify third and
first party dependencies that Amazon Q might not otherwise know to upgrade.

First party dependencies refer to the libraries, plugins, and frameworks that your
organization maintains and are only available locally or on your organization’s
private network. Amazon Q is able to access your first party dependencies when it
performs builds in your local environment. For more information, see [Building code in your local environment](transform-CLI.md#local-builds "transform-CLI.md#local-builds"). Third party dependencies are publicly available
or open source dependencies that aren’t unique to your organization.

You can specify first party dependencies you want to upgrade in a YAML file, and Amazon Q
upgrades them during the JDK upgrade (for example, Java 8 to 17). You can initiate a
separate transformation (17 to 17 or 21 to 21) after the initial JDK upgrade to upgrade
third-party dependencies.

Once Amazon Q performs a minimum JDK upgrade, you can initiate a separate transformation
to upgrade all third party dependencies. Alternatively, you can specify third party
dependencies and their versions in a YAML file to only upgrade those dependencies during
the library upgrade transformation.

Amazon Q will prompt you to provide a dependency upgrade file during the
transformation. If you want to provide one, first make sure you've configured the
file properly. The following fields are required in the YAML file:

- name - The name of the dependency upgrade file.
- description (optional) - A description of the dependency upgrade file, and for which transformation.
- dependencyManagement - Contains the list of dependencies and plugins to upgrade.
- dependencies - Contains the name and version of the libraries to upgrade.
- plugins - Contains the names and versions of the plugins to upgrade.
- identifier - The name of the library, plugin, or other dependency.
- targetVersion - The version of the dependency to upgrade to.
- versionProperty (optional) - The version of the dependency you're
  defining, as set with the `properties` tag in your application's `pom.xml`
  file.
- originType - Whether the dependency is first or third party, specified by either FIRST_PARTY or THIRD_PARTY.

Following is an example of a dependency upgrade YAML file, and the required configuration for Amazon Q to parse:

```
name: dependency-upgrade

description: "Custom dependency version management for Java migration from JDK 8/11/17 to JDK 17/21"


dependencyManagement:

  dependencies:

    - identifier: "com.example:library1"

      targetVersion: "2.1.0"

      versionProperty: "library1.version"  # Optional

      originType: "FIRST_PARTY"

    - identifier: "com.example:library2"

      targetVersion: "3.0.0"

      originType: "THIRD_PARTY"

  plugins:

    - identifier: "com.example.plugin"

      targetVersion: "1.2.0"

      versionProperty: "plugin.version"  # Optional

      originType: "THIRD_PARTY"
```

## Step 4: Configure and authenticate

Before you can begin a transformation, you must authenticate with IAM Identity Center and
provide configuration details for your transformation.

1. To start the transformation configuration process, run the following command:

```
qct configure
```

2. You are prompted to enter a JDK path for each supported Java version.
   You only need to specify the path to the JDK of the source version of your
   Java application, not the target version.
3. Next, to authenticate with IAM Identity Center, you are prompted to enter the start URL
   for your Amazon Q Developer Pro subscription profile.

Then, enter the AWS Region where you were subscribed in the following
format: `us-east-1`. For a list of supported Regions, see [Supported Regions](regions.md "regions.md"). For a list of Region
codes, see [Regional endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in the _AWS General Reference guide_. 4. Your configuration preferences are saved to a configuration.ini file.

## Step 5: Run a transformation

Choose the type of transformation you're performing to see the
required configuration and commands.

###### Note

Do not turn off or close your local machine during the code transformation because
client-side build requires a stable network connection.

Java upgrade
**Modifying the transformation plan**

During Java version upgrades, Amazon Q generates a transformation plan
that you can review before the transformation begins. You have the
option to request the following changes to the plan:

- Which libraries Amazon Q upgrades, from the list included in the plan
  - Example prompts:
    - Only upgrade <dependency1>, <dependency2>, and <dependency5>
    - Don't upgrade <dependency1> or <dependency2>

- The target version to upgrade a library to
  - Example prompts:
    - Upgrade <dependency> to this version instead <version>

- Which steps Amazon Q should perform
  - Example prompts:
    - Only complete steps 1-7
    - Don't run steps 5-9

- Add additional dependencies to upgrade (only an option when upgrading to a newer JDK version)
  - Example prompts:
    - Also upgrade <dependency1> to <version2>

###### Upgrade Java code

1. Run the following command to start a transformation for a Java upgrade.
   Replace `<path-to-folder>` with the path to the folder with
   the code you're transforming and
   `<your-target-java-version>` with either
   `JAVA_17` or `JAVA_21`.

```
qct transform --source_folder `<path-to-folder>`
    --target_version `<your-target-java-version>`
```

Additional command options:

    * If you are specifying dependencies to upgrade, add the
     `--dependency_upgrade_file` option with the path to your
     dependency upgrade file.
    * If you don’t want to review or update the
     transformation plan, add the `--no-interactive` flag to
     your command. Amazon Q won’t ask you for feedback on the
     plan, and you won’t have the opportunity to request
     changes.

2. Your Maven version is verified before the transformation begins. If you have at least the minimum supported
   version, you will see the following output:

```
Running command: mvn --version at: path/to/current/directory
Your Maven version is supported for transformations.
```

If you don’t have a supported version of Maven, you must update it to continue. For
more information, see the [Prerequisites](#CLI-transformation-prerequisites "#CLI-transformation-prerequisites"). 3. If you didn’t add the `--no-interactive` flag, Amazon Q will
prompt you to provide feedback on the transformation plan. You
can explain the changes you want to make in English natural
language, and Amazon Q will update the plan if it can support
the changes you request. 4. Amazon Q begins the transformation. It will output status updates
throughout the transformation. When it’s complete, Amazon Q provides the
path where the transformation results, logs, and configuration files are
outputted.

Your upgraded code will be committed to the new branch Amazon Q created.
Amazon Q will commit the code in one or multiple commits, depending on the
selection you made when you ran `qct configure`. 5. If you're running another transformation after upgrading your
Java version, start the second transformation in the same branch where
you committed the changes from the first transformation.

SQL conversion
Before you begin, make you sure you've read [Converting embedded SQL in Java applications with Amazon Q Developer](transform-sql.md "transform-sql.md") to understand the prerequisites for this
type of transformation.

1. To convert embedded SQL, you must first create a YAML file that contains
   the path to the schema metadata file from your [AWS DMS
   Schema Conversion](../../../dms/latest/sbs/schema-conversion-oracle-postgresql.md "../../../dms/latest/sbs/schema-conversion-oracle-postgresql.md").

Following is the required format of the file:

```
schema_conv_metadata_path: `<path-to-metadata-zip-file>`
```

2. Run the following command to start a transformation for a SQL
   conversion. Replace `<path-to-folder>` with the path to the
   folder with the code you're transforming and
   `<path-to-sql-config-file>` with the path to the YAML
   file you created in step 1.

```
qct transform --source_folder `<path-to-folder>`
    --sql_conversion_config_file `<path-to-sql-config-file>`
```

3. If Amazon Q finds multiple schemas in your schema metadata file, it will
   stop the transformation and provide a list of the detected schemas. Choose
   which schema to use for the SQL conversion, and then add a new field
   `schema: `<schema-name>`` to
   the YAML file.
4. Amazon Q begins the transformation. It will output status updates
   throughout the transformation. When it’s complete, Amazon Q provides the
   path where the transformation results, logs, and configuration files are
   outputted.

Your upgraded code will be committed to the new branch Amazon Q
created.

## Pause or cancel a transformation

You can choose to pause or cancel your current transformation job. You can pause a transformation
job for up to 12 hours before you can resume again.

###### To pause or cancel a code transformation job

1. In your CLI terminal, press **Ctrl+C** on your keyboard.
2. Select whether you want to pause or cancel your tranformation.
   - Enter `1` if you want to puase the code transformation job. You
     can resume the job within 12 hours to continue the code transformation using the
     following QCT command:
     `qct transform --source_folder=≤/Path/Given/Originally/To/QCT>`.
   - Enter `2` if you want to cancel the code tranformation job.
