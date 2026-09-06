# Connecting via JDBC

## Connecting to Your Database with JDBC

This guide walks you through connecting your database to Amazon Connect Decisions using **Java Database Connectivity** (JDBC). You'll set up secure encryption for your database credentials and establish a connection that Amazon Connect Decisions can use to access your data.

## What is JDBC Connection and When Should You Use It?

JDBC connection allows Amazon Connect Decisions to connect to your existing database to read data, rather than requiring you to export and upload CSV files or set up your own Extraction, Transformation, Load (ETL) pipelines to S3. This approach is ideal when:

- Your data is already stored in an AWS Glue-compatible relational database. Refer to [this guide](../../../glue/latest/dg/aws-glue-programming-etl-connect-jdbc-home.md "../../../glue/latest/dg/aws-glue-programming-etl-connect-jdbc-home.md") for compatible databases and versions.
- You want real-time or near-real-time data access without manual file exports
- Your data volume is large and frequently updated
- You prefer to keep your data in its current location rather than duplicating it
- If you're working with smaller datasets or prefer file-based uploads, the standard CSV upload process may be simpler for your needs. Refer to [Data Onboarding User Guide](data-onboarding.md "data-onboarding.md") for more details on this process.

## Prerequisites

Before you begin, ensure you have:

- An AWS account with permissions to create KMS keys and Secrets Manager resources
- Your AWS account ID and the region where Amazon Connect Decisions will operate
- Database connection details: hostname, port, database name, and credentials
- Administrative access to your database to verify connectivity
- Your database configured to accept connections from AWS services

## Create a Customer-Managed KMS Key

Before connecting your database to Amazon Connect Decisions, you'll need to set up encryption for your database credentials. AWS Key Management Service (KMS) provides this security layer, ensuring your connection details remain protected.

### Create Your KMS Key

1. **Navigate to AWS KMS Console**

   - Open the AWS Management Console in your browser
   - In the search bar at the top, type "KMS" and select "Key Management Service" from the results
   - This opens the KMS dashboard where you'll manage encryption keys

2. **Initiate key creation**

   - On the KMS dashboard, locate and click the **Create key** button in the upper right
   - This starts the key creation wizard that will guide you through the setup process

3. **Configure key type and usage**

   - On the "Configure key" page, select **Symmetric** as the key type (this is the default and recommended option)
   - Keep "Encrypt and decrypt" selected under key usage

4. **Set key identification details**

   - In the "Alias" field, enter a descriptive name for your key, such as `aws-supply-chain-database-key`
   - In the "Description" field, add context like "Encryption key for Amazon Connect Decisions database credentials"
   - Optionally, add tags to help organize and track your AWS resources (e.g., Key: "Project", Value: "Amazon Connect Decisions")

5. **Define key administrative permissions**

   - Select the IAM users or roles who should be able to manage this key (create, delete, modify policies)
   - At minimum, include your own Admin role to ensure you can modify the key later if needed
   - These administrators can manage the key but won't automatically have permission to use it for encryption/decryption
   - On the "Key Deletion" section, Allow key administrators to delete this key. (this is the default and recommended option)

6. **Define key usage permissions**

   - On this page, you'll see options to select IAM users and roles that can use the key
   - Skip selecting specific users here, you'll configure service permissions in the next step

7. **Configure the key policy for Amazon Connect Decisions services**

   - You'll see a policy editor with default JSON
   - In the KMS key policy editor, append the following statement to your existing "Statement" array
   - This policy grants your account full control and allows Amazon Connect Decisions's services (Secrets Manager and Glue) to decrypt your database credentials

```
{
      "Sid": "Allow GDIS service to decrypt",
      "Effect": "Allow",
      "Principal": {
        "Service": "scn.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*"
    }
```

8. **Review and finalize**

   - Review all your configuration settings on the summary page
   - Verify that your alias, description, and policy are correct
   - Click **Finish** to create the key
   - Once created, you'll be returned to the KMS dashboard where your new key will appear in the list

### What to Expect

Key creation is immediate. Once created, you'll see your new key listed in the KMS console with a status of "Enabled." The key is now ready to encrypt your database credentials in Secrets Manager.

## Configure AWS Secrets Manager

Now that you have a KMS key, you'll create a secret in AWS Secrets Manager to securely store your database credentials, then configure a resource policy that allows Amazon Connect Decisions to access this secret.

### Create Your Secret

1. **Navigate to AWS Secrets Manager**

   - In the AWS Management Console search bar, type "Secrets Manager"
   - Select "Secrets Manager" from the results to open the service dashboard

2. **Start creating a new secret**

   - Click the **Store a new secret** button
   - On the "Choose secret type" page, select **Other type of secret** (this gives you flexibility to structure your credentials)

3. **Enter your database credentials**

   - In the key-value pairs section, add your database connection details as **strings**:

```
Key: username, Value: your database username
    Key: password, Value: your database password
    Key: host, Value: your database hostname (e.g., database.example.com)
    Key: port, Value: your database port (e.g., 3306 for MySQL)
    Key: database, Value: your database name
```

4. **Select your encryption key**

   - Under "Encryption key," select **Choose an AWS KMS key**
   - From the dropdown, select the KMS key you created in Step 1 (e.g., `aws-supply-chain-database-key`)
   - This ensures your credentials are encrypted with your customer-managed key

5. **Name your secret**

   - Enter a descriptive name for your secret, such as `aws-supply-chain-production-database`
   - Optionally, add a description like "Database credentials for Amazon Connect Decisions production environment"
   - Add tags if desired for organization (e.g., Key: "Environment", Value: "Production")

6. **Add Resource Permissions**

   - Click "Edit Permissions". In the policy editor, paste the following policy. This policy allows Amazon Connect Decisions's services to read your secret

```
{
      "Version" : "2012-10-17",
      "Statement" : [ {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "scn.amazonaws.com"
        },
        "Action" : [ "secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret" ],
        "Resource" : "<COPY-THE-SECRET-ARN-HERE-AFTER-CREATING>"
      } ]
    }
```

7. **Save the policy**

   - Click **Save** to apply the resource policy
   - The policy is now active and allows Amazon Connect Decisions to retrieve your database credentials

8. **Configure rotation (optional)**

   - For this setup, you can skip automatic rotation by selecting **Disable automatic rotation**
   - You can enable rotation later if your security policies require it

9. **Review and create**

   - Review all your secret details
   - Click **Store** to create the secret
   - You'll be returned to the Secrets Manager dashboard

10. **Save your Secret ARN**

    - Find your newly created secret in the secrets list
    - Click on the secret name to open its details page
    - At the top, you'll see the Secret ARN
    - Copy and save this ARN
    - The ARN format looks like: `arn:aws:secretsmanager:us-east-1:123456789012:secret:aws-supply-chain-production-database-AbCdEf`

11. **Edit Resource Permissions**

    - Click "Edit permissions"
    - Paste the copied Secret ARN and replace `<COPY-THE-SECRET-ARN-HERE-AFTER-CREATING>` with your copied ARN
    - Click **Save** to attach the policy

### What to Expect

Your secret is now securely stored and encrypted with your KMS key. Amazon Connect Decisions's services have permission to retrieve the credentials when establishing a database connection, but the credentials remain encrypted at rest and in transit.

## Connect Your Database to Amazon Connect Decisions

With your KMS key and secret configured, you're ready to establish the JDBC connection in Amazon Connect Decisions.

### Configure Your JDBC Connection

1. **Navigate to Amazon Connect Decisions > Data Management**

   - Log into your Amazon Connect Decisions instance
   - From the main navigation, select "Data Management"
   - Within the tab navigation, navigate to "Connections"
   - Select "New Connection" to create a new Connection

2. **Enter your connection details**

   - **Connection name (required):** Enter a unique identifier for this connection (e.g., "production-database")
   - **Description (optional):** Add details about the purpose and usage of this connection to help your team understand what data it accesses
   - **JDBC URL (required):** Enter your full JDBC connection string in the format: `jdbc:<database-type>://<hostname>:<port>/<database>` (e.g., `jdbc:postgresql://db.example.com:5432/mydb`)
   - **Schema name (optional):** Specify the database schema if needed (e.g., "public", "dbo", "myschema"). Leave blank to use your database's default schema
   - **Secret ARN (required):** Paste the Secret ARN you saved from Step 2. This allows Amazon Connect Decisions to securely retrieve your database credentials from Secrets Manager.
   - **Enforce SSL connection:** Keep this checkbox selected (recommended) to require SSL/TLS encryption for your database connection
   - **VPC endpoint service name (required):** Enter your VPC endpoint service name for private connectivity via AWS PrivateLink (format: `com.amazonaws.vpce.<region>.vpce-svc-xxxxxxxxx`)

3. **Connect to your database**

   - Click "Connect" to test and establish the connection. Amazon Connect Decisions will verify that it can successfully connect to your database using the provided credentials. This step can take up to 2 minutes, so please do not leave this screen during connection.
   - If the connection succeeds, you'll be automatically navigated to table selection
   - If the connection fails:

     - Review your connection details to ensure all fields are accurate:

       - Verify your Secret ARN is correct
       - Confirm your database credentials are accurate
       - Check that your JDBC URL format is correct
       - Ensure your database is configured to accept connections from AWS services
       - Verify your KMS key and Secrets Manager policies are correctly configured

     - You can also use the chat experience to help troubleshoot connection issues by asking questions like "Why is my database connection failing?" or "Help me debug my JDBC connection"

4. **Select tables to ingest**

   - Once connected, you'll see the Select Tables screen showing all available tables from your database
   - Select the checkbox next to each table you want to ingest

5. **Configure table refresh schedule**

   - For each selected table, click the three-dot menu in the Action column and select "Schedule refresh"
   - In the Configure load details dialog, set:

     - **Cadence:** How often to refresh (Hourly, Daily, Weekly, or Custom)
     - **Start hour:** The time for refresh to begin (displayed in UTC with your timezone offset)
     - **Refresh type:** Choose Complete refresh (replace all data) or Incremental update (add new data to existing; requires selecting a Record timestamp column)
     - Repeat for each table as needed

   - Click Start mapping when all tables are configured

6. **Continue with data mapping**

   - From this point forward, the experience is identical to our Data Onboarding flow
   - Follow the Data Mapping section of the [Data Onboarding User Guide](data-onboarding.md "data-onboarding.md") to complete your setup

### What to Expect

Once your connection is established and tables are selected, Amazon Connect Decisions can read data from your database. The connection remains active and secure, with credentials encrypted and managed through AWS Secrets Manager. You won't need to manually update credentials in Amazon Connect Decisions, any changes you make in Secrets Manager will automatically be reflected.

## Best Practices

### Security and Access Management

- **Store credentials securely**: Always use AWS Secrets Manager to store database credentials, never hardcode credentials in connection strings or configuration files
- **Enable SSL/TLS encryption**: Keep the "Enforce SSL connection" option enabled to ensure data is encrypted in transit
- **Review KMS and Secrets Manager policies regularly**: Ensure only authorized services and accounts have access to your encryption keys and secrets
- **Use least-privilege access**: Grant only the minimum necessary permissions to database users that Amazon Connect Decisions will use for connections

### Connection Configuration

- **Use descriptive connection names**: Choose clear, meaningful names that indicate the environment and purpose (e.g., "production-inventory-db" rather than "db1")
- **Document your connections**: Use the Description field to note what data the connection accesses, who owns it, and any special considerations
- **Test connections before proceeding**: Always verify your connection works before selecting tables and configuring refresh schedules
- **Validate JDBC URL format**: Double-check your JDBC URL syntax matches your database type to avoid connection errors

### Data Refresh Strategy

- **Choose appropriate refresh cadence**: Select refresh frequency based on how often your source data changes and your business needs
- **Schedule refreshes during low-activity periods**: Configure refresh times when your database has lower load to minimize performance impact
- **Use incremental updates when possible**: For large datasets with frequent changes, incremental updates are more efficient than complete refreshes
- **Select meaningful timestamp columns**: When using incremental updates, choose columns that accurately reflect when records were created or modified

### Working with the chat for troubleshooting

- **Be specific in your requests**: Provide clear context when asking for help troubleshooting connection or mapping issues
- **Ask for explanations**: If you don't understand the recommendations or generated SQL queries, ask for clarification
- **Test all SQL changes before accepting**: Use the preview feature to verify transformations work as expected with your actual data
- **Leverage the chat for troubleshooting**: When connections fail or refreshes encounter errors, ask diagnostic questions like "Why is my connection failing?" or "Help me understand this refresh error"

### Ongoing Maintenance

- **Monitor refresh execution regularly**: Check the Destinations and Sources tabs in Data Management to ensure refreshes are completing successfully
- **Address errors promptly**: When Amazon Connect Decisions alerts you to refresh failures, investigate and resolve issues quickly to avoid data gaps
- **Update credentials securely**: When database passwords change, update them in AWS Secrets Manager, Amazon Connect Decisions will automatically use the new credentials
- **Document custom configurations**: Keep notes about any special refresh schedules, transformation logic, or connection requirements for your team's reference
- **Review table selections periodically**: As your data needs evolve, revisit which tables you're ingesting and whether refresh schedules still align with business requirements
