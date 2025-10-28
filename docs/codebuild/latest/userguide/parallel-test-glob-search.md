# Use the `codebuild-glob-search` CLI command

AWS CodeBuild provides a built-in CLI tool called `codebuild-glob-search` that allows you to
search for files in your working directory based on one or more glob patterns. This tool can be particularly
useful when you want to run tests on specific files or directories within your project.

## Usage

The `codebuild-glob-search` CLI has the following usage syntax:

```
codebuild-glob-search `<glob_pattern1>` [`<glob_pattern2>` ...]
```

- `<glob_pattern1>`, `<glob_pattern2>`, etc.: One or more glob patterns to match against the files in your working directory.
- `*`: Matches any sequence of characters (excluding path separators).
- `**`: Matches any sequence of characters (including path separators).

###### Note

Ensure that the glob string has quotes. To check the results of pattern-matching, use the `echo` command.

```
version: 0.2

phases:
  build:
    commands:
      - echo $(codebuild-glob-search '**/__tests__/*.js')
      - codebuild-glob-search '**/__tests__/*.js' | xargs -n 1 echo
```

## Output

The CLI will output a newline-separated list of file paths that match the provided glob patterns. The file paths returned will be relative to the working directory.

If no files are found matching the provided patterns, the CLI will output a message indicating that no files were found.

Note that directories found due to any given pattern will be excluded from the search results.

## Example

If you want to search only for files inside the tests directory and its subdirectories with a `.js` extension,
you can use the following command with the `codebuild-glob-search` CLI:

```
codebuild-glob-search '**/__tests__/*.js'
```

This command will search for all files with a `.js` extension inside the `__tests__`directory and its
subdirectories, as denoted by the pattern.
