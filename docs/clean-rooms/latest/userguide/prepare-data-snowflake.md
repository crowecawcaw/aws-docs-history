# Preparing data tables in Snowflake

You can query data tables that have been stored in Snowflake data warehouse.

Preparing your data tables in Snowflake involves the following steps:

###### Topics

- [Step 1: Complete the
  prerequisites](#prepare-data-snowflake-prereq "#prepare-data-snowflake-prereq")
- [Step 2: (Optional) Prepare your
  data for cryptographic computing](#prepare-data-snowflake-encrypt "#prepare-data-snowflake-encrypt")
- [Step 3: Create an AWS Secrets Manager
  secret](#prepare-data-snowflake-secrets "#prepare-data-snowflake-secrets")
- [Step 4: Next steps](#prepare-data-snowflake-next "#prepare-data-snowflake-next")

## Step 1: Complete the

prerequisites

To prepare your data tables for use with AWS Clean Rooms, you must complete the
following prerequisites:

- You have an AWS account with the proper permissions granted to read your
  data tables. For more information, see [Create a service role to read data
  from Snowflake](setting-up-roles.md#create-service-role-third-party "setting-up-roles.md#create-service-role-third-party").
- Your data tables are saved as one of the [supported data formats for AWS Clean Rooms](data-formats.md "data-formats.md").
- Your data tables use the [supported data types
  for AWS Clean Rooms](data-formats.md#data-types "data-formats.md#data-types").
- Your data table is stored in a Snowflake warehouse. For more information,
  see the [Snowflake documentation](https://docs.snowflake.com/en/guides-overview-db "https://docs.snowflake.com/en/guides-overview-db ").
- You have set up a new Snowflake user with read-only privileges to the
  Snowflake table you are going to associate with your collaboration.

## Step 2: (Optional) Prepare your

data for cryptographic computing

(Optional) If you're using cryptographic computing and your data table contains
sensitive information that you want to encrypt, you must encrypt the data table
using the C3R encryption client.

To prepare your data for cryptographic computing, follow the procedures in [Preparing encrypted data tables with Cryptographic Computing for Clean Rooms](prepare-encrypted-data.md "prepare-encrypted-data.md").

## Step 3: Create an AWS Secrets Manager

secret

To connect to Snowflake from AWS Clean Rooms, you will need to create and store your
Snowflake credentials in a AWS Secrets Manager secret, then associate that secret with a
Snowflake table in AWS Clean Rooms.

###### Note

We recommend that you create a new user that is exclusively for AWS Clean Rooms. That
user should only have a role with Read permissions for the data that you want
AWS Clean Rooms to access.

###### To create an AWS Secrets Manager secret

1. In Snowflake, generate a user `snowflakeUser` and set up
   key-pair authentication.

###### Note

In November 2025, Snowflake will transition to supporting only
key-pair authentication. This change will affect the current AWS Clean Rooms
integration with Snowflake, which uses username and password
authentication. After this date, Snowflake connections in AWS Clean Rooms will
require key-pair authentication using a Snowflake Privacy Enhanced Mail
(PEM) private key. 2. Determine which Snowflake warehouse this user will interact with,
`snowflakeWarehouse`. Either set it as the
`DEFAULT_WAREHOUSE` for `snowflakeUser` in
Snowflake or remember it for the next step. 3. In [AWS Secrets Manager](https://us-east-1.console.aws.amazon.com/secretsmanager/listsecrets?region=us-east-1 "https://us-east-1.console.aws.amazon.com/secretsmanager/listsecrets?region=us-east-1"), create a secret using your Snowflake credentials. To
create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_. After creating the secret, keep the
Secret name, `secretName` for the next step.

    * When selecting **Key/value pairs**, create a pair
     for `snowflakeUser` with the key `sfUser`.
    * When selecting **Key/value pairs**, create a pair
     for your Snowflake PEM private key with the key
     `pem_private_key`.
    * When selecting **Key/value pairs**, create a pair
     for `snowflakeWarehouse` with the key
     `sfWarehouse`.


    This isn't needed if a default is set in Snowflake.
    * When selecting **Key/value pairs**, create a pair
     for `snowflakeRole` with the key `sfRole`.

## Step 4: Next steps

Now that you have prepared your data tables in Snowflake, you are ready to:

- [Create a configured
  table](create-configured-table.md "create-configured-table.md")
- [Create an ML
  model](working-with-machine-learning-tdp.md "working-with-machine-learning-tdp.md")

The tables can be queried after:

- The collaboration creator has set up a collaboration in AWS Clean Rooms. For
  more information, see [Creating a collaboration](create-collaboration.md "create-collaboration.md").
- The collaboration creator has sent the collaboration ID to you as a
  participant in the collaboration.
