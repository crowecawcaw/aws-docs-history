# Step 1: Complete the prerequisites

To prepare your data tables for use with C3R, you must complete the following
prerequisites:

- You can access the Cryptographic Computing for Clean Rooms repository on GitHub:

[https://github.com/aws/c3r](https://github.com/aws/c3r "https://github.com/aws/c3r")

- You have set up AWS credentials to use the C3R encryption client. These credentials are
  used by C3R encryption client for read-only API calls to AWS Clean Rooms to retrieve collaboration
  metadata. For more information, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the _AWS Command Line Interface User Guide for
  Version 2_.
- You have Java Runtime Environment (JRE) 11 or later
  installed on your machine.
  - The recommended Java Runtime Environment, Amazon Corretto 11 or higher,
    can be downloaded from [https://aws.amazon.com/corretto](https://aws.amazon.com/corretto "https://aws.amazon.com/corretto").
  - The Java Development Kit (JDK) includes a
    corresponding JRE of the same version. However, the additional
    capabilities of the JDK are not needed for running the Cryptographic Computing for Clean Rooms
    (C3R) encryption client.

- Your tabular data files (.csv) or Parquet files
  (.parquet) are saved locally.
- You or another member in the collaboration has the ability to create a shared secret
  key. For more information, see [Step 5: Create a shared secret key](create-SSK.md "create-SSK.md").
- The collaboration creator has created a collaboration in AWS Clean Rooms with
  **Cryptographic computing** enabled for the collaboration. For more
  information, see [Creating a collaboration](create-collaboration.md "create-collaboration.md").
- The collaboration creator has sent the collaboration ID to you as a participant in the
  collaboration. The collaboration Amazon Resource Name (ARN) is included in the invitation
  that is sent, which contains the collaboration ID.
