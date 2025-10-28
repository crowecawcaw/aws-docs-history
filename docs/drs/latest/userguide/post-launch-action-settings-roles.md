# Install the required IAM roles if needed

To operate post-launch actions and allow to run SSM documents on launched instances, certain IAM roles must be installed. Usually these roles are installed into an AWS account when AWS DRS is initialized in the account for the first time in any region.

If you have already initialized Elastic Disaster Recovery in your account before September 13, 2023,
it's possible that the required IAM roles were not installed in your account.

To verify the IAM roles are installed or install them if not installed (a one time
operation, go to **Settings → Default post-launch
actions** and check **Post-launch actions
settings**. If you see the message **Install the
required IAM roles to allow using post-launch actions** select
**Install post-launched IAM roles**. If the roles
were installed successfully, the message to install the roles is not present in
**Post-launch actions settings**.
