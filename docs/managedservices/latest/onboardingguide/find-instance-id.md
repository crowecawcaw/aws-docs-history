# Finding an instance ID or IP address

You need an instance IP address to log into the instance.

- To request access to an instance, to log in to an instance, or to create an AMI, you must have
  the instance ID. For an EC2 instance (either a standalone instance or a part of a
  stack), or a database instance, you can find the ID in a few different ways:
  - The AMS Console for an instance in an ASG stack: Look on the RFC detail page for the RFC that created the stack. In the Execution Output section,
    you will find the stack ID for the ASG stack and you can then go to the EC2 Console **Auto Scaling Groups** page and search for that
    stack ID and find instances for it. When you find the instance, select it and an area opens at the bottom of the page with details, including the IP address.
  - The AMS Console for a standalone EC2 or database (DB) instance: Look on the RFC detail page
    for the RFC that created the EC2 stack or DB instance. In the Execution Output
    section, you will find the Instance ID and IP address.
  - AWS EC2 Console:
    1. In the navigation pane, select **Instances**. The **Instances** page opens.
    2. Click the instance that you want the ID for. The instance details page opens and displays the ID and IP address.

  - AWS Database Console:
    1. On the Home page, select **DB Instances**. The **Instances** page opens.
    2. Filter for the DB instance that you want the ID for. The instance details page opens and displays the ID.

  - AMS CLI/API.

  ###### Note

  The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources**
  page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for
  authentication; for example, `aws amsskms `ams-cli-command` --profile SAML`. You may also need to add the `--region` option as all AMS
  commands run out of us-east-1; for example `aws amscm `ams-cli-command` --region=us-east-1`.

  ###### Note

  The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your
  authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1`
  when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.

  Run the following command to get stack execution output details:

  ```
  aws amsskms get-stack --stack-id `STACK_ID`
  ```

  The output looks similar to this with the InstanceId appearing near the bottom, under `Outputs` (values shown are examples):

  ```
  {
      "Stack": {
          "StackId": "stack-7fa52bd5eb8240123",
          "Status": {
              "Id": "CreateCompleted",
              "Name": "CreateCompleted"
          },
          "VpcId": "vpc-01234567890abcdef",
          "Description": "Amazon",
          "Parameters": [
              {
                  "Value": "sg-01234567890abcdef,sg-01234567890abcdef",
                  "Key": "SecurityGroups"
              },
              {
                  "Value": "subnet-01234567890abcdef",
                  "Key": "InstanceSubnetId"
              },
              {
                  "Value": "t2.large",
                  "Key": "InstanceType"
              },
              {
                  "Value": "ami-01234567890abcdef",
                  "Key": "InstanceAmiId"
              }
          ],
          "Tags": [],
          "Outputs": [
              {
                  "Value": "i-0b22a22eec53b9321",
                  "Key": "InstanceId"
              },
              {
                  "Value": "10.0.5.000",
                  "Key": "InstancePrivateIP"
              }
          ],
          "StackTemplateId": "stm-s6xvs000000000000",
          "CreatedTime": "1486584508416",
          "Name": "Amazon"
      }
  }
  ```
