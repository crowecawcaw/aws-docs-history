# Transforming code on the command line with Amazon Q Developer

You can transform your applications from the command line with the Amazon Q Developer command line
transformation tool. To transform your code, you provide the path to your source code and
any necessary configuration files, and Amazon Q generates new code in a series of steps.
Throughout the transformation, Amazon Q builds code on your local environment to verify
changes. For more information, see [Building code in your local environment](#local-builds "#local-builds"). Amazon Q creates a new branch in your repository where it commits the code changes. When
the transformation is complete, you can merge the branch into your original branch to
incorporate the changes into your codebase.

To get started, install the command line tool and authenticate, and then see the
commands to configure and start a transformation.

###### Topics

- [Building code in your local environment](#local-builds "#local-builds")
- [Commands](#commands "#commands")
- [Running a transformation on the command line with
  Amazon Q Developer](run-CLI-transformations.md "run-CLI-transformations.md")
- [Troubleshooting transformations on the command line](troubleshooting-CLI-transformations.md "troubleshooting-CLI-transformations.md")
- [Amazon Q Developer command line transformation tool version
  history](transform-CLI-versions.md "transform-CLI-versions.md")

## Building code in your local environment

During a transformation, Amazon Q performs verification builds in your local environment. Amazon Q
transforms your code on the server side in multiple steps. After each step, Amazon Q sends the code
to your local environment to build and test the changes it made. The code is then sent back to the
server side to continue the transformation.

The build in your local environment helps verify the transformed code by allowing Amazon Q to run
tests that require access to private resources. To minimize security risks associated with
building AI-generated code in your local environment, Amazon Q reviews and updates the code it
generates to address security concerns.

###### Note

Amazon Q performs transformations based on your project's requests, descriptions, and content.
To maintain security, avoid including external, unvetted artifacts in your project repository
and always validate transformed code for both functionality and security.

## Commands

For step-by-step instructions for running these commands, see [Running a transformation on the command line with
Amazon Q Developer](run-CLI-transformations.md "run-CLI-transformations.md").

To configure a transformation and authenticate to Amazon Q Developer Pro, run:

```
qct configure
```

To start a transformation for a Java upgrade, run the following command. For
`<your-source-java-version>`, you can enter
`JAVA_1.8`, `JAVA_8`, `JAVA_11`, `JAVA_17`, or
`JAVA_21`. For `<your-target-java-version>`, you can
enter either `JAVA_17` or `JAVA_21`. Both
`--source_version` and `--target_version` are optional. The `--trust`
flag enables a transformation to run while vetting code to maintain security.

```
qct transform --source_folder `<path-to-folder>`
    --source_version `<your-source-java-version>`
    --target_version `<your-target-java-version>`
    --trust
```

To start a transformation for a SQL conversion, run:

```
qct transform --source_folder `<path-to-folder>`
    --sql_conversion_config_file `<path-to-sql-config-file>`
```

To see what version of the command line tool for transformation you are using, run:

```
qct -v
```

To get help with transformations, run:

```
qct -h
```

To view your transformation job history, run:

```
qct history
```

For more information about viewing and managing your transformation job history, see [Viewing job history on the command line](transformation-job-history.md#cli-job-history "transformation-job-history.md#cli-job-history").
