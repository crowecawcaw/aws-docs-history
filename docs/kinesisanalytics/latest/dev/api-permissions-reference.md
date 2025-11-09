After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# API Permissions: Actions,

Permissions, and Resources Reference

When you are setting up [Access Control](authentication-and-access-control.md#access-control "authentication-and-access-control.md#access-control") and writing a permissions policy that you can attach to an IAM identity
(identity-based policies), you can use the following table
as a reference. The
table lists
each
API operation, the corresponding actions for which you can grant
permissions to perform the action, and the AWS resource for which you can grant the
permissions. You specify the actions in the policy's `Action` field, and you
specify the resource value in the policy's `Resource` field.

You can use AWS-wide condition keys in your policies to express
conditions. For a complete list of AWS-wide keys, see [Available
Keys](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

###### Note

To specify an action, use the `kinesisanalytics` prefix followed by the API
operation name (for example, `kinesisanalytics:AddApplicationInput`).

Use the scroll bars to see the rest of the table.

| API and Required Permissions for Actions                                                                                          | API Operations                                          | Required Permissions (API Actions)                                              | Resources |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------- | --------- |
| [AddApplicationInput](API_AddApplicationInput.md "API_AddApplicationInput.md")                                                    | `kinesisanalytics:AddApplicationInput`                  | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [AddApplicationOutput](API_AddApplicationOutput.md "API_AddApplicationOutput.md")                                                 | `kinesisanalytics:AddApplicationOutput`                 | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [AddApplicationReferenceDataSource](API_AddApplicationReferenceDataSource.md "API_AddApplicationReferenceDataSource.md")          | `kinesisanalytics:AddApplicationReferenceDataSource`    | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [CreateApplication](API_CreateApplication.md "API_CreateApplication.md")                                                          | `kinesisanalytics:CreateApplication`                    | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [DeleteApplication](API_DeleteApplication.md "API_DeleteApplication.md")                                                          | `kinesisanalytics:DeleteApplication`                    | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [DeleteApplicationOutput](API_DeleteApplicationOutput.md "API_DeleteApplicationOutput.md")                                        | `kinesisanalytics:DeleteApplicationOutput`              | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [DeleteApplicationReferenceDataSource](API_DeleteApplicationReferenceDataSource.md "API_DeleteApplicationReferenceDataSource.md") | `kinesisanalytics:DeleteApplicationReferenceDataSource` | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [DescribeApplication](API_DescribeApplication.md "API_DescribeApplication.md")                                                    | `kinesisanalytics:DescribeApplication`                  | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [DiscoverInputSchema](API_DiscoverInputSchema.md "API_DiscoverInputSchema.md")                                                    | `kinesisanalytics:DiscoverInputSchema`                  | \*                                                                              |
| [ListApplications](API_ListApplications.md "API_ListApplications.md")                                                             | `kinesisanalytics:ListApplications`                     | \*                                                                              |
| [StartApplication](API_StartApplication.md "API_StartApplication.md")                                                             | `kinesisanalytics:StartApplication`                     | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [StopApplication](API_StopApplication.md "API_StopApplication.md")                                                                | `kinesisanalytics:StopApplication`                      | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| [UpdateApplication](API_UpdateApplication.md "API_UpdateApplication.md")                                                          | `kinesisanalytics:UpdateApplication`                    | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |
| Access or sample data in the console                                                                                              | `kinesisanalytics:GetApplicationState`                  | `arn:aws:kinesisanalytics: `region`:`accountId`:application/`application-name`` |

## GetApplicationState

The console uses an internal method called `GetApplicationState` to sample or access application data. Your
service application
needs to have permissions for the internal `kinesisanalytics:GetApplicationState` API to sample or access application data through the AWS Management Console.
