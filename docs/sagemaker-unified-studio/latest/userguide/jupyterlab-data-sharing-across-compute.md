# Data Sharing Across Compute

Environments

Amazon SageMaker Unified Studio provides magic commands to facilitate data sharing across different compute
environments. This section outlines three key commands: `%push`, `%pop`,
and `%send_to_remote`.

## %push

The `%push` command allows you to upload specified variables to your
project's shared S3 storage within Amazon SageMaker Unified Studio.

```

%push <var_name>
%push <var_name1>,<var_name2>
%push -v <var_name>
%push -v <var_name> --namespace <namespace_name>

```

**Key Features:**

- Supports multiple variable uploads when comma-separated
- -v specifies the variable name (alternative syntax)
- Optional --namespace argument (defaults to kernel ID)
- Uploaded variables are accessible to all project members

**Supported Connections:**

- Local Python connections
- AWS Glue connections
- AWS EMR connections

**Supported Language:** Python

## %pop

The %pop command enables you to download specified variables from shared project Amazon
S3 storage to your current compute environment.

```

%pop <var_name>
%pop <var_name1>,<var_name2>
%pop -v <var_name>
%pop -v <var_name> --namespace <namespace_name>

```

**Key Features:**

- Supports multiple variable downloads when comma-separated
- -v specifies the variable name (alternative syntax)
- Optional --namespace argument (defaults to kernel ID)

**Supported Connections:**

- Local Python connections
- AWS Glue connections
- AWS EMR connections

**Supported Language:** Python

## %send_to_remote

The %send_to_remote command allows you to send a variable from the local kernel to a
remote compute environment.

```

%send_to_remote --name <connection_name> --language <language> --local <local_variable_name> --remote <remote_variable_name>

```

**Key Features:**

- Supports both Python and Scala in remote environments
- Python remote supports dict, df, and str data types
- Scala remote supports df and str data types

  **Arguments:**

- -l or --language: Specifies the connection language
- -n or --name: Specifies the connection to be used
- --local: Defines the local variable name
- --remote or -r: Defines the remote variable name

**Supported Connections:** local Python connections

**Supported Language:**

- Python
- Scala

## Security

considerations

Remember that variables uploaded using `%push` are accessible to all project members
within your Amazon SageMaker Unified Studio project. Ensure that sensitive data is handled
appropriately and in compliance with your organization's data governance policies.
