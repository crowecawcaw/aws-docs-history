# FSx for Lustre file system status

You can view the status of an Amazon FSx file system by using the Amazon FSx console, the AWS CLI
command [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md"), or the API operation [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md").

| File system status | Description                                                                                                                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AVAILABLE          | The file system is in a healthy state, and is reachable and available for use.                                                                                                                     |
| CREATING           | Amazon FSx is creating a new file system.                                                                                                                                                          |
| DELETING           | Amazon FSx is deleting an existing file system.                                                                                                                                                    |
| UPDATING           | The file system is undergoing a customer-initiated update.                                                                                                                                         |
| MISCONFIGURED      | The file system is in a failed but recoverable state.                                                                                                                                              |
| FAILED             | This status can mean either of the following: <br>• The file system has failed and Amazon FSx can't recover it. <br>• When creating a new file system, Amazon FSx couldn't create the file system. |
