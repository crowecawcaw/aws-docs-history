# AMS Tools account hygiene

You'll want to clean up after you are done in the account have shared the AMI and no longer have a need for the replicated instances:

- Post instance WIGs ingestion:
  - Cutover instance: At a minimum, stop or terminate this instance, after the work has been completed, via the AWS console
  - Pre-Ingestion AMI backups: Remove once the instance has been ingested and the on-premise instance terminated
  - AMS-ingested instances: Turn off the stack or terminate once the AMI has been shared
  - AMS-ingested AMIs: Delete once sharing with the destination account is completed

- End of migration clean up: Document the resources deployed through Developer mode to ensure clean-up happens on regular basis, for example:
  - Security groups
  - Resources created via Cloud-formation
  - Network ACK
  - Subnet
  - VPC
  - Route Table
  - Roles
  - Users and accounts
