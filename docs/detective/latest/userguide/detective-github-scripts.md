# Using Detective Python scripts to manage accounts

Amazon Detective provides a set of open-source Python scripts in the GitHub repository [amazon-detective-multiaccount-scripts](https://github.com/aws-samples/amazon-detective-multiaccount-scripts "https://github.com/aws-samples/amazon-detective-multiaccount-scripts"). The scripts require Python 3.

You can use these to perform the following tasks:

- Enable Detective for an administrator account across Regions.

When you enable Detective, you can assign tag values to the behavior graph.

- Add member accounts to an administrator account's behavior graphs across Regions.
- Optionally send invitation emails to the member accounts. You can also configure the
  request to not send invitation emails.
- Remove member accounts from an administrator account's behavior graphs across
  Regions.
- Disable Detective for an administrator account across Regions. When an administrator account
  disables Detective, the administrator account's behavior graph in each Region is disabled.

## Overview of the

`enableDetective.py` script

The `enableDetective.py` script does the following:

1. Enables Detective in for an administrator account in each specified Region, if the
   administrator account does not already have Detective enabled in that Region.

When you use the script to enable Detective, you can assign tag values to the behavior
graph. 2. Optionally sends invitations from the administrator account to the specified member
accounts for each behavior graph.

The invitation email messages use the default message content and cannot be
customized.

You can also configure the request to not send invitation emails. 3. Automatically accepts the invitations for the member accounts.

Because the script automatically accepts the invitations, member accounts can ignore these
messages.

We recommend reaching out directly to the member accounts to notify them that the
invitations are accepted automatically.

## Overview of the

`disableDetective.py` script

The `disableDetective.py` script deletes the specified member accounts
from the administrator account's behavior graphs across the specified Regions.

It also provides an option to disable Detective for the administrator account across the
specified Regions.

## Required permissions for the scripts

The scripts require a preexisting AWS role in the administrator account and in all of the
member accounts that you add or remove.

###### Note

The role name must be the same in all of the accounts.

IAM policy [recommended best practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices "security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices") are to use least scoped roles. To execute the script’s workflow of [creating a graph](../APIReference/API_CreateGraph.md "../APIReference/API_CreateGraph.md"), [creating members](../APIReference/API_CreateMembers.md "../APIReference/API_CreateMembers.md"), and [adding members to the graph](../APIReference/API_AcceptInvitation.md "../APIReference/API_AcceptInvitation.md") the required permissions are:

- detective:CreateGraph
- detective:CreateMembers
- detective:DeleteGraph
- detective:DeleteMembers
- detective:ListGraphs
- detective:ListMembers
- detective:AcceptInvitation

**Role trust relationship**

The role trust relationship must allow your instance or local credentials to assume the
role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/`john_doe`"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

If you do not have a common role that includes the required permissions, you must create a
role with at least those permissions in each member account. You must also create the role in the
administrator account.

When you create the role, make sure that you do the following:

- Use the same role name in every account.
- Add the required permissions above (recommended) or select the [AmazonDetectiveFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-amazondetectivefullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-amazondetectivefullaccess") managed policy.
- Add role trust relationship block as discussed above.

To automate this process, you can use the `EnableDetective.yaml` CloudFormation
template. Because the template creates only global resources, it can be run in any Region.

## Setting up the run environment for the Python

scripts

You can run the scripts from either an EC2 instance or from a local machine.

### Launching and configuring an EC2 instance

One option for running the scripts is to run them from an EC2 instance.

###### To launch and configure an EC2 instance

1. Launch an EC2 instance in your administrator account. For details on how to launch an EC2
   instance, see [Getting Started with Amazon EC2 Linux Instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the _Amazon EC2 User Guide_.
2. Attach to the instance an IAM role that has permissions to allow the instance to call
   `AssumeRole` within the administrator account.

If you used the `EnableDetective.yaml` CloudFormation template, then an
instance role with a profile named `EnableDetective` was created.

Otherwise, for information on creating an instance role, see the blog post [Easily Replace or Attach an IAM Role to an Existing EC2 Instance by Using the EC2
Console](https://aws.amazon.com/blogs//security/easily-replace-or-attach-an-iam-role-to-an-existing-ec2-instance-by-using-the-ec2-console/ "https://aws.amazon.com/blogs//security/easily-replace-or-attach-an-iam-role-to-an-existing-ec2-instance-by-using-the-ec2-console/"). 3. Install the required software:

    * **APT:**
    `sudo apt-get -y install python3-pip python3 git`
    * **RPM:**
    `sudo yum -y install python3-pip python3 git`
    * **Boto (minimum version 1.15):**
    `sudo pip install boto3`

4. Clone the repository to the EC2 instance.

```
git clone https://github.com/aws-samples/amazon-detective-multiaccount-scripts.git
```

### Configuring a local machine to run the

scripts

You can also run the scripts from your local machine.

###### To configure a local machine to run the scripts

1. Make sure that you have set up on your local machine credentials for your administrator
   account that have permission to call `AssumeRole`.
2. Install the required software:
   - Python 3
   - Boto (minimum version 1.15)
   - GitHub scripts

| Platform | Setup instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows  | 1. Install Python 3 ([https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/ "https://www.python.org/downloads/windows/")).<br>2. Open a command prompt.<br>3. To install Boto, run: `pip install boto3`<br>4. Download the script source code from GitHub ([https://github.com/aws-samples/amazon-detective-multiaccount-scripts](https://github.com/aws-samples/amazon-detective-multiaccount-scripts "https://github.com/aws-samples/amazon-detective-multiaccount-scripts")). |
| Mac      | 1. Install Python 3 ([https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/macos/ "https://www.python.org/downloads/macos/")).<br>2. Open a command prompt.<br>3. To install Boto, run: `pip install boto3`<br>4. Download the script source code from GitHub ([https://github.com/aws-samples/amazon-detective-multiaccount-scripts](https://github.com/aws-samples/amazon-detective-multiaccount-scripts "https://github.com/aws-samples/amazon-detective-multiaccount-scripts")).     |
| Linux    | 1. To install Python 3, run one of the following:<br>• `sudo apt-get -y install install python3-pip python3 git`<br>• `sudo yum install git python`<br>2. To install Boto, run: `sudo pip install boto3`<br>3. Clone the script source code from [https://github.com/aws-samples/amazon-detective-multiaccount-scripts](https://github.com/aws-samples/amazon-detective-multiaccount-scripts "https://github.com/aws-samples/amazon-detective-multiaccount-scripts").                                           |

## Creating a `.csv` list of member

accounts to add or remove

To identify the member accounts to add to or remove from the behavior graphs, you provide a
`.csv` file that contains the list of accounts.

List each account on a separate line. Each member account entry contains the AWS account
ID and the account's root user email address.

See the following example:

```
111122223333,srodriguez@example.com
444455556666,rroe@example.com
```

## Running

`enableDetective.py`

You can run the `enableDetective.py` script from an EC2 instance or your
local machine.

###### To run `enableDetective.py`

1. Copy the `.csv` file to the
   `amazon-detective-multiaccount-scripts` directory on your EC2 instance or
   local machine.
2. Change to the `amazon-detective-multiaccount-scripts` directory.
3. Run the `enableDetective.py` script.

```
enableDetective.py --master_account `administratorAccountID` --assume_role `roleName` --input_file `inputFileName` --tags `tagValueList` --enabled_regions `regionList`  --disable_email
```

When you run the script, replace the following values:

`administratorAccountID`

The AWS account ID for the administrator account.

`roleName`

The name of the AWS role to assume in the administrator account and each member
account.

`inputFileName`

The name of the `.csv` file containing the list of member accounts to
add to the administrator account's behavior graphs.

`tagValueList`

(Optional) A comma-separated list of tag values to assign to a new behavior graph.

For each tag value, the format is
``key`=`value``. For
example:

```
--tags Department=Finance,Geo=Americas
```

`regionList`

(Optional) A comma-separated list of Regions in which to add the member accounts to the
administrator account's behavior graph. For example:

```
--enabled_regions us-east-1,us-east-2,us-west-2
```

The administrator account might not already have Detective enabled in a Region. In that case,
the script enables Detective and creates a new behavior graph for the administrator
account.

If you do not provide a list of Regions, then the script acts across all Regions that
Detective supports.

`--disable_email`

(Optional) If included, Detective does not send invitation emails to the member
accounts.

## Running

`disableDetective.py`

You can run the `disableDetective.py` script from an EC2 instance or your
local machine.

###### To run `disableDetective.py`

1. Copy the `.csv` file to the
   `amazon-detective-multiaccount-scripts` directory.
2. To use the `.csv` file to delete the listed member accounts from the
   administrator account's behavior graphs across a specified list of Regions, run the
   `disableDetective.py` script as follows:

```
disabledetective.py --master_account `administratorAccountID` --assume_role `roleName` --input_file `inputFileName` --disabled_regions `regionList`
```

3. To disable Detective for the administrator account across all Regions, run the
   `disableDetective.py` script with the `--delete-master`
   flag.

```
disabledetective.py --master_account `administratorAccountID` --assume_role `roleName` --input_file `inputFileName` --disabled_regions `regionList` --delete_master
```

When you run the script, replace the following values:

`administratorAccountID`

The AWS account ID for the administrator account.

`roleName`

The name of the AWS role to assume in the administrator account and each member
account.

`inputFileName`

The name of the `.csv` file containing the list of member accounts to
remove from the administrator account's behavior graphs.

You must provide a `.csv` file even if you are disabling Detective.

`regionList`

(Optional) A comma-separated list of Regions in which to do one of the following:

- Remove the member accounts from the administrator account's behavior graphs.
- If the `--delete-master` flag is included, disable Detective.

For example:

```
--disabled_regions us-east-1,us-east-2,us-west-2
```

If you do not provide a list of Regions, then the script acts across all Regions that
Detective supports.
