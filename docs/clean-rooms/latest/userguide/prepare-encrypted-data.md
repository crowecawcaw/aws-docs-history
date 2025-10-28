# Preparing encrypted data tables with Cryptographic Computing for Clean Rooms

Cryptographic Computing for Clean Rooms (C3R) is a capability in AWS Clean Rooms. You can use C3R to
limit cryptographically what can be learned by any party and AWS in an AWS Clean Rooms
collaboration.

You can encrypt the data table using the C3R encryption client, a client-side encryption tool,
before uploading the data table to
your data source:
Amazon Simple Storage Service
(Amazon S3), Amazon Athena, or
Snowflake.

For more information, see [Cryptographic Computing for Clean Rooms](crypto-computing.md "crypto-computing.md").

Preparing encrypted data tables with C3R involves the following steps:

###### Steps

- [Step 1: Complete the prerequisites](prerequisites.md "prerequisites.md")
- [Step 2: Download the C3R encryption client](download-client.md "download-client.md")
- [Step 3: (Optional) View available commands in the
  C3R encryption client](view-commands.md "view-commands.md")
- [Step 4: Generate an encryption schema for a
  tabular file](gen-encryption-schema-csv.md "gen-encryption-schema-csv.md")
- [Step 5: Create a shared secret key](create-SSK.md "create-SSK.md")
- [Step 6: Store the shared secret key in an environment
  variable](store-key.md "store-key.md")
- [Step 7: Encrypt data](encrypt-data.md "encrypt-data.md")
- [Step 8: Verify data encryption](verify-encryption.md "verify-encryption.md")
- [(Optional) Create a schema (advanced users)](create-schema.md "create-schema.md")
