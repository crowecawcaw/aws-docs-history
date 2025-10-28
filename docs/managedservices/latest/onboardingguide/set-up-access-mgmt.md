# Set up access management

Using a network managed by AWS Managed Services (AMS) means giving AMS access to manage your cloud infrastructure. You'll need to
configure a means of securely connecting between your private network and AMS. This starts with some decisions:

- _AMS API/CLI and Console access_: You will want to install the AMS CLI (instructions are
  provided in this
  document). You use the AMS change management API to make change requests to AMS and the AMS SKMS API to learn about your
  AMS-managed resources. Using Active Directory Federation Services (AD FS), you can access the AMS Console.
- _User access_: Connectivity needs to be established between AD on the AMS side (via Directory
  Services)
  and the directory you use to manage users.
- _Instance access_: Instance-level access is accomplished via a one-way trust configuration. Directory
  Services trusts credentials in your CORP AD, allowing stacks within the AMS side to allow login with CORP credentials.

###### Note

Your Active Directory (AD) that AMS sets up the trust to, must be the directory that has the accounts of users authorized by
you to gain access to your AWS resources.
