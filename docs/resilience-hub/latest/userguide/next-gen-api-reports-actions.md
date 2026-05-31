# Reports

| Action         | Method | Description                                                                                                         |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------------------- |
| `CreateReport` | POST   | Generate a PDF report (`FAILURE_MODE`,<br>`DEPENDENCY`, or `TESTING` type); writes to customer<br>Amazon S3 bucket. |
| `ListReports`  | GET    | List generated reports with status and Amazon S3 output location.                                                   |
