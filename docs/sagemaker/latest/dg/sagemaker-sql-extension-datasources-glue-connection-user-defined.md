# Create

user-defined AWS Glue connections

###### Note

All AWS Glue connections created by users via the SQL extension UI are automatically tagged
with the following:

- `UserProfile: `user-profile-name``
- `AppType: "JL"`
  Those tags applied to the AWS Glue connections created via the SQL extension UI serve two
  purposes. The `"UserProfile": `user-profile-name``tag
 allows the identification of the specific user profile that created the AWS Glue connection,
 providing visibility into the user responsible for the connection. The`"AppType":
  "JL"` tag categorizes the provenance of the connection, associating it with the
  JupyterLab application. This allows these connections to be differentiated from those that
  may have been created through other means, such as the AWS CLI.

## Prerequisites

Before creating a AWS Glue connection using the SQL extension UI, ensure that you have
completed the following tasks:

- Have your administrator:
  - Enable the network communication between your Studio domain and the
    data sources to which you want to connect. To learn about the networking
    requirements, see [Configure network access between Studio and data sources (for administrators)](sagemaker-sql-extension-networking.md "sagemaker-sql-extension-networking.md").
  - Ensure that the necessary IAM permissions are set up for managing AWS Glue
    connections and access to Secrets Manager. To learn about the required permissions, see [Set up the IAM
    permissions to access the data sources (for administrators)](sagemaker-sql-extension-datasources-connection-permissions.md "sagemaker-sql-extension-datasources-connection-permissions.md").

  ###### Note

  Administrators can restrict user access to only the connections that were
  created by a user within the JupyterLab application. This can be done by
  configuring [tag-based access control](sagemaker-sql-extension-datasources-connection-permissions.md#user-defined-connections-permissions "sagemaker-sql-extension-datasources-connection-permissions.md#user-defined-connections-permissions") scoped down to the user profile.

- Check the connection properties and instructions to create a secret for your data
  source in [Create secrets for database
  access credentials in Secrets Manager](sagemaker-sql-extension-glue-connection-secrets.md "sagemaker-sql-extension-glue-connection-secrets.md").

## User workflow

The following steps provide the user workflow when creating user connections:

1. **Select the data source type**: Upon choosing the
   _Add new connection_ icon, a form opens, prompting
   the user to select the type of data source they want to connect to, such as Amazon Redshift, Athena,
   or Snowflake.
2. **Provide connection properties**: Based on the
   selected data source, the relevant connection properties are dynamically loaded. The
   form indicates which fields are mandatory or optional for the chosen data source. To
   learn about the available properties for your data source, see [Connection parameters](sagemaker-sql-extension-connection-properties.md "sagemaker-sql-extension-connection-properties.md").
3. **Select your AWS Secrets Manager ARN**: For Amazon Redshift and Snowflake
   data sources, the user is prompted to select the AWS Secrets Manager ARN that stores
   sensitive information such as the username and password. To learn about the creation of
   a secret for your data source, see [Create secrets for database
   access credentials in Secrets Manager](sagemaker-sql-extension-glue-connection-secrets.md "sagemaker-sql-extension-glue-connection-secrets.md").
4. **Save your connection details**: Upon clicking
   **Create**, the provided connection properties are saved as a AWS Glue
   connection.
5. **Test your connection**: If the connection is
   successful, the associated databases and tables become visible in the explorer. If the
   connection fails, an error message is displayed, prompting the user to review and
   correct the connection details.
6. **Familiarize with SQL extension features**: To
   learn about the capabilities of the extension, see the [SQL extension features and usage](sagemaker-sql-extension-features.md "sagemaker-sql-extension-features.md").
7. **(Optional) Update or delete user-created
   connections**: Provided that the user has been granted the necessary
   permissions, they can update or delete the connections they have created. To learn more
   about the required permissions, see [User-defined connections required
   IAM permissions](sagemaker-sql-extension-datasources-connection-permissions.md#user-defined-connections-permissions "sagemaker-sql-extension-datasources-connection-permissions.md#user-defined-connections-permissions").
