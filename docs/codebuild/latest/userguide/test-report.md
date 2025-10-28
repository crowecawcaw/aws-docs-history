# Test report statuses

The status of a test report can be one of the following:

- `GENERATING`: The run of the test cases is still in
  progress.
- `DELETING`: The test report is being deleted. When a test report is
  deleted, its test cases are also deleted. Raw test result data files exported to
  an S3 bucket are not deleted.
- `INCOMPLETE`: The test report was not completed. This status might
  be returned for one of the following reasons:
  - A problem with the configuration of the report group that specifies
    this report's test cases. For example, the path to the test cases under
    the report group in the buildspec file might be incorrect.
  - The IAM user that ran the build does not have permissions to run
    tests. For more information, see [Test report permissions](test-permissions.md "test-permissions.md").
  - The build was not completed because of an error that is not related to
    the tests.

- `SUCCEEDED`: All test cases were successful.
- `FAILED`: Some of the test cases were not successful.
  Each test case returns a status. The status for a test case can be one of the
  following:

- `SUCCEEDED`: The test case passed.
- `FAILED`: The test case failed.
- `ERROR`: The test case resulted in an unexpected error.
- `SKIPPED`: The test case did not run.
- `UNKNOWN`: The test case returned a status other than
  `SUCCEEDED`, `FAILED`, `ERROR`, or
  `SKIPPED`.
  A test report can have a maximum of 500 test case results. If more than 500 test cases
  are run, CodeBuild prioritizes tests with the status `FAILED` and truncates the
  test case results.
