# Managing the Terraform Open Source product state file

Every Terraform Open Source provisioned product has a **single-state file**.
There is a 1:1 relationship between the provisioned product and its state file. The files are stored in
an Amazon S3 bucket named `sc-terraform-engine-state-${AWS::AccountId}-${AWS::Region}`.
The state file is saved under the `AccountID` or `ProvisionedProductID` object key.

State file access is limited to the `GetStateFile` AWS Lambda and Amazon EC2 launch templates.
AWS Service Catalog administrators do **not** have direct access to the state files in Amazon S3. Administrators
must access the files using Amazon EC2. By default, AWS Service Catalog administrators can see the list of state files,
but cannot read or write the file contents. Only the Terraform provisioning engine can read or write the file contents.
