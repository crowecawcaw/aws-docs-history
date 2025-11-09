|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# rejectQualificationRequests

## Description

The `rejectQualificationRequests` command rejects Workers' Qualification requests.

## Arguments

The following table describes the arguments for the `rejectQualificationRequests` command.

| Name                                      | Description                                                                                                                                                                                                                                                                                                                                                                            | Required    |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `-force`                                  | Specifies \*not<br>• to prompt for manual confirmation before performing the<br>reject operation. Only advanced developers should use this argument.<br>Example: `-force`                                                                                                                                                                                                              | No          |
| `-help` or `-h`                           | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                              | No          |
| `-qualRequest [Qualification request ID]` | Specifies the Qualification request ID(s) to reject. You can specify multiple<br>Qualification request IDs in a comma-separated list. The list (or<br>single ID) must be enclosed in quotation marks.<br>Conditions: Required if the `rejectfile` argument is not specified.<br>Example: `-qualRequest "789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE"`                                     | Conditional |
| `-rejectfile [filename]`                  | Specifies a file that contains the list of Qualification requests to reject.<br>For information about this file, see \*The Qualification reject file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Conditions: Required if the `qualRequest` argument is not specified.<br>Example: `-rejectfile qualification_requests_toreject.txt` | Conditional |
| `-sandbox`                                | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence<br>even if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                                              | No          |

## Example

The following examples for Unix and Windows show how to use the
`rejectQualificationRequests` command. These examples reject
one Qualification request listed in the file `toreject.txt`.

### Unix

The following example demonstrates how to call this command from Unix.

```

./rejectQualificationRequests.sh -rejectfile toreject.txt

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

rejectQualificationRequests -rejectfile toreject.txt

```

## Output

These examples produce the following output.

```

You are about to reject 1 qualification request(s). Are you sure?
To confirm this operation, please press ENTER (or press Ctrl+C to abort):

If you would like to supply a comment to the worker(s), please type it below then press ENTER.
If not, just hit ENTER:

[789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE] Qualification request successfully rejected

```
