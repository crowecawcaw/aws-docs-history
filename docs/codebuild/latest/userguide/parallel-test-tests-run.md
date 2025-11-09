# Use the `codebuild-tests-run` CLI command

AWS CodeBuild provides CLI that will take test command and test file location as input. The CLI with these
input will split the tests into number of shards as specified in the `parallelism` field
based on test file names. The assignment of test files to shard is decided by the sharding strategy.

```
codebuild-tests-run \
    --files-search "codebuild-glob-search '**/__tests__/*.js'" \
    --test-command 'npx jest --runInBand --coverage' \
    --sharding-strategy 'equal-distribution'
```

The following table describes the fields for the `codebuild-tests-run` CLI command.

| Field name          | Type   | Required or optional | Definition                                                                                                                                                                                                                                                                                                                              |
| ------------------- | ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `test-command`      | String | Required             | This command is used for running the tests.                                                                                                                                                                                                                                                                                             |
| `files-search`      | String | Required             | This command gives a list of test files. You can use the AWS CodeBuild provided<br>[codebuild-glob-search](parallel-test-glob-search.md "parallel-test-glob-search.md") CLI command<br>or any other file search tool of your choice.<br>NoteEnsure that the `files-search` command outputs file names, each<br>separated by a new line. |
| `sharding-strategy` | Enum   | Optional             | Valid values: `equal-distribution` (default), `stability`<br>• `equal-distribution`: Shard test files evenly based on test file names.<br>• `stability`: Shard test files using consistent hashing of the file names.<br>For more information, see [About test splitting](parallel-test-splitting.md "parallel-test-splitting.md").     |

The `codebuild-tests-run` CLI works first to identify the list of test files using the command
provided in the `files-search` parameter. It then determines a subset of test files designated for the
current shard (environment) using the specified sharding strategy. Finally, this subset of test files is formatted
into a space-separated list and appended to the end of the command provided in the `test-command`
parameter before being executed.

For test frameworks that don't accept space-separated lists, the `codebuild-tests-run` CLI provides a
flexible alternative through the `CODEBUILD_CURRENT_SHARD_FILES` environment variable. This variable
contains a newline-separated list of test file paths designated for the current build shard. By leveraging this
environment variable, you can easily adapt to various test framework requirements, accommodating those that expect
input formats different from space-separated lists. Moreover, you can also format the test file names as per need of
test framework. The following is an example of the use of `CODEBUILD_CURRENT_SHARD_FILES` on Linux with the Django
framework. Here `CODEBUILD_CURRENT_SHARD_FILES` is used to get _dot notation_ file paths supported by Django:

```
codebuild-tests-run \
    —files-search "codebuild-glob-search '/tests/test_.py'" \
    —test-command 'python3 manage.py test $(echo "$CODEBUILD_CURRENT_SHARD_FILES" | sed -E "s/\//__/g; s/\.py$//; s/__/./g")' \
    —sharding-strategy 'equal-distribution'
```

###### Note

Note that the `CODEBUILD_CURRENT_SHARD_FILES` environment variable
can be used only inside the scope of the `codebuild-tests-run` CLI.

Also, if you are using `CODEBUILD_CURRENT_SHARD_FILES` inside test-command,
put `CODEBUILD_CURRENT_SHARD_FILES` inside double quotes as shown in above example.
