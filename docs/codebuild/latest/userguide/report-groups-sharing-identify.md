

# Identify a shared report group
<a name="report-groups-sharing-identify"></a>

Owners and consumers can use the AWS CLI to identify shared report groups. 

To identify and get information about a shared report group and its reports, use the following commands: 
+  To see the ARNs of report groups shared with you, run `[list-shared-report-groups](https://docs.aws.amazon.com/cli/latest/reference/codebuild/list-shared-report-groups.html)`: 

  ```
  aws codebuild list-shared-report-groups
  ```
+  To see the ARNs of the reports in a report group, run `[list-reports-for-report-group](https://docs.aws.amazon.com/cli/latest/reference/codebuild/list-reports-for-report-group.html)` using the report group ARN: 

  ```
  aws codebuild list-reports-for-report-group --report-group-arn {{report-group-arn}}
  ```
+  To see information about test cases in a report, run `[describe-test-cases](https://docs.aws.amazon.com/cli/latest/reference/codebuild/describe-test-cases.html)` using the report ARN: 

  ```
  aws codebuild describe-test-cases --report-arn {{report-arn}}
  ```

   The output looks like the following: 

  ```
  {
      "testCases": [
          {
              "status": "FAILED",
              "name": "Test case 1",
              "expired": 1575916770.0,
              "reportArn": "{{report-arn}}",
              "prefix": "Cucumber tests for agent",
              "message": "A test message",
              "durationInNanoSeconds": 1540540,
              "testRawDataPath": "path-to-output-report-files"
          },
          {
              "status": "SUCCEEDED",
              "name": "Test case 2",
              "expired": 1575916770.0,
              "reportArn": "{{report-arn}}",
              "prefix": "Cucumber tests for agent",
              "message": "A test message",
              "durationInNanoSeconds": 1540540,
              "testRawDataPath": "path-to-output-report-files"
          }
      ]
  }
  ```