# Testing configured ticketing integrations

For configured Jira and ServiceNow integrations you can test the connection to ensure that all the configuration in Security Hub and in your Jira or ServiceNow environment is complete.

The test ticket feature will create a ticket with a title of `TESTING Test CreateTicketV2 Finding`.
The test ticket is populated with sample data such as Account ID and region of the account where the test is performed, sample resource details, and sample AWS Finding JSON.

## Testing integrations using the console

Use the following steps to test your integration:

1. In the Security Hub navigation panel choose **Integrations**.
2. In the **Configured integrations** tab chose the integration that you want to test.
3. In the overview page for your integration choose **Create test ticket**.
4. If the test was successful a success message along with a link to the test ticket will be displayed.
   If the test was not successful an error for the test will be displayed.
   Based on the error message address the configuration issues in Security Hub or in your Jira or Service Now environment.

###### Note

The test ticket feature intended to help verify end to end functionality for the setup of a new connection or when you make changes to an existing connection.
This feature will create a new ticket in your Jira or Service Now environment every time it is used and is not intended to be used for regular verification of your connection.

## Testing with the AWS CLI

To test your integration using the AWS CLI, use the `create-ticket-v2` command with the `--mode DRYRUN` parameter:

```

aws securityhub create-ticket-v2 \
  --mode DRYRUN \
  --region <your-region> \
  --connector-id <your-connector-id> \
  --finding-metadata-uid "TEST_FINDING"

```

###### Example

The following example shows how to test an integration:

```

aws securityhub create-ticket-v2 \
  --mode DRYRUN \
  --region us-east-1 \
  --connector-id "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" \
  --finding-metadata-uid "TEST_FINDING"

```

###### Successful Response

A successful response returns the following:

```

{
    "TicketId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    "TicketSrcUrl": "https://your-instance.service-now.com/nav_to.do?uri=x_aws_se_0_finding.do?sys_id=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
}

```

The `TicketSrcUrl` in the response provides a direct link to view the test ticket in your Jira or ServiceNow environment.

If the test fails, an error message will be displayed indicating the configuration issue that needs to be addressed.

## Troubleshooting Jira cloud integration errors

When testing your integration to Jira Cloud from Security Hub the following error messages may be returned.
These error messages can provide insight on where the configuration issue with the connector could be and how to resolve.

| Jira Cloud integration error messages | Error                             | Error Message                                                                                                                                                                                                                                                             | Likely cause and resolution |
| ------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| ConflictException                     | Cannot find jira project          | **Likely cause:\*<br>• Project on the connector is incorrect, or credentials/permissions issue preventing us from accessing the project.<br>**Likely resolution:\*<br>• Add the correct project to the connector or re-authenticate to Jira with the correct credentials. |
| ConflictException                     | Security Hub issue type not found | **Likely cause:\*<br>• App installation issue or issue type is not associated with the project.<br>**Likely resolution:\*<br>• Perform the pre-requisite step to install the Jira app into your Jira environment and associate the app with the project.                  |
