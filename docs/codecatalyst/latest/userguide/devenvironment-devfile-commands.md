Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Devfile commands

Currently, CodeCatalyst only supports `exec` commands in your devfile. For more
information, see [Adding commands](https://devfile.io/docs/2.0.0/adding-commands "https://devfile.io/docs/2.0.0/adding-commands")
in the Devfile.io documentation.

The following example shows you how to specify `exec` commands in your
devfile.

```
commands:
  - id: setupscript
    exec:
      component: test
      commandLine: "chmod +x script.sh"
      workingDir: /projects/devfiles
  - id: executescript
    exec:
      component: test
      commandLine: "./projects/devfiles/script.sh"
  - id: updateyum
    exec:
      component: test
      commandLine: "yum -y update --security"

```

After you're connected to your Dev Environment, you can execute defined commands through the
terminal.

```
/aws/mde/mde command `<command-id>`
/aws/mde/mde command executescript

```

For long running commands, you can use the streaming flag `-s` to output the
execution of the command in real time.

```
/aws/mde/mde -s command `<command-id>`
```

###### Note

`command-id` must be lower case.

## Exec parameters supported by CodeCatalyst

CodeCatalyst supports the following `exec` parameters on devfile version 2.0.0.

- `commandLine`

- `component`

- `id`

- `workingDir`
