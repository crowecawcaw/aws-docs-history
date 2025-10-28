# Obtaining Amazon SES SMTP credentials

You need Amazon SES SMTP credentials to access the SES SMTP interface.

The credentials that you use to send email through the SES SMTP interface are
unique to each AWS Region. If you use the SES SMTP interface to send email in more
than one Region, you must generate a set of SMTP credentials for each Region that you plan
to use.

Your SMTP password is different from your AWS secret access key. For more information
about credentials, see [Types of Amazon SES credentials](send-email-concepts-credentials.md "send-email-concepts-credentials.md").

###### Note

For a list of currently available SMTP endpoints, see [SMTP endpoints](../../../general/latest/gr/ses.md#ses_smtp_endpoints "../../../general/latest/gr/ses.md#ses_smtp_endpoints") in the
_AWS General Reference_.

## Obtaining SES SMTP credentials using

the SES console

###### Requirement

An IAM user can create SES SMTP credentials, but the user's policy must
give them permission to use IAM itself, because SES SMTP credentials are
created by using IAM. Your IAM policy must allow you to perform the following
IAM actions: `iam:ListUsers`, `iam:CreateUser`,
`iam:CreateAccessKey`, and `iam:PutUserPolicy`. If you try
to create SES SMTP credentials using the console and your IAM user doesn't
have these permissions, you see an error that states that your account is
_"not authorized to perform iam:ListUsers."_

###### Important

The IAM actions referenced above have the [Permission management](../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md#access_policies_access-level "../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md#access_policies_access-level") access level which is the highest IAM level
because it gives permission to grant or modify resource permissions in the service.
Therefore, to improve the security of your AWS account, it is highly recommended
that you restrict or regularly monitor these policies that include the Permissions
management access level classification.

###### To create your SMTP credentials

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Choose **SMTP settings** in the left navigation pane - this
   will open the **Simple Mail Transfer Protocol (SMTP) settings**
   page.
3. Choose **Create SMTP Credentials** in the upper-right corner

- the IAM console will open.

4. (Optional) If you need to view, edit, or delete SMTP users you’ve already
   created, choose **Manage my existing SMTP credentials** in the
   lower-right corner - the IAM console will open. Details for managing SMTP
   credentials is given following these procedures.
5. For **Create User for SMTP**, type a name for your SMTP user
   in the **User Name** field. Alternatively, you can use the
   default value that is provided in this field. When you finish, choose
   **Create user** in the bottom-right corner.
6. Select **Show** under _SMTP password_ -
   your SMTP credentials are shown on the screen.
7. Download these credentials by choosing **Download .csv file**
   or copy them and store them in a safe place, because you can't view or save your
   credentials after you close this dialog box.
8. Choose **Return to SES console**.

You can view a list of the SMTP credentials you've created using this procedure in the
IAM console under **Access management** and choosing
**Users** followed by using the search bar to find all users that
you've assigned SMTP credentials.

You can also use the IAM console to delete existing SMTP users. To learn more about
deleting users, see [Managing IAM
Users](../../../IAM/latest/UserGuide/id_users_manage.md "../../../IAM/latest/UserGuide/id_users_manage.md") in the _IAM Getting Started Guide_.

If you want to change your SMTP password, delete your existing SMTP user in the IAM
console. Then, to generate a new set of SMTP credentials, complete the previous
procedures.

## Obtaining SES SMTP credentials by

converting existing AWS credentials

If you have a user that you set up using the IAM interface, you can derive the
user's SES SMTP credentials from their AWS credentials.

###### Important

Don't use temporary AWS credentials to derive SMTP credentials. The SES
SMTP interface doesn't support SMTP credentials that have been generated from
temporary security credentials.

###### To enable the IAM user to send email using the SES SMTP

interface

1. Derive the user's SMTP credentials from their AWS credentials by using the
   algorithm provided in this section following these procedures.

Because you're starting from AWS credentials, the SMTP user name is the same
as the AWS access key ID, so you only need to generate the SMTP
password. 2. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). 3. Under **Access management**, choose
**Polices** followed by **Create
policy**. 4. In the **Policy editor**, select **JSON**
and remove any example code in the editor. 5. Paste to the following permissions policy into the editor:

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
"Effect": "Allow",
 "Action": "ses:SendRawEmail",
 "Resource": "*"
 }
 ]
}`

```

6. Select **Next** and enter `AmazonSesSendingAccess`
   in the **Policy name** field followed by **Create
   policy**.
7. Under **Access management**, choose **User
   groups** followed by **Create group**.
8. Enter `AWSSESSendingGroupDoNotRename` in the **User group
   name** field.
9. Add SMTP users to the group by selecting them from the **Add users to
   the group** table.
10. Attach the `AmazonSesSendingAccess` policy created previously by
    selecting it from the **Attach permissions policies** table
    followed by **Create user group**.

For more information about using SES with IAM, see [Identity and access management in Amazon SES](control-user-access.md "control-user-access.md").

###### Note

Although you can generate SES SMTP credentials for any IAM user, we
recommend that you create a separate IAM user when you generate your SMTP
credentials. For information about why it's good practice to create users for
specific purposes, go to [IAM Best
Practices](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md").

The following pseudocode shows the algorithm that converts an AWS secret access key
to an SES SMTP password.

```
// Modify this variable to include your AWS secret access key
key = "`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`";

// Modify this variable to refer to the AWS Region that you want to use to send email.
region = "`us-west-2`";

// The values of the following variables should always stay the same.
date = "11111111";
service = "ses";
terminal = "aws4_request";
message = "SendRawEmail";
version = 0x04;

kDate = HmacSha256(date, "AWS4" + key);
kRegion = HmacSha256(region, kDate);
kService = HmacSha256(service, kRegion);
kTerminal = HmacSha256(terminal, kService);
kMessage = HmacSha256(message, kTerminal);
signatureAndVersion = Concatenate(version, kMessage);
smtpPassword = Base64(signatureAndVersion);
```

Some programming languages include libraries that you can use to convert an IAM
secret access key into an SMTP password. This section includes a code example that you
can use to convert an AWS secret access key to an SES SMTP password using
Python.

###### Note

- The following example uses **f-strings** that
  were introduced in Python 3.6; if using an older version, they won't
  work.
- In the following example, the list of SMTP_REGIONS is simply an
  example—your actual list of regions could be shorter or longer
  depending on which regions you plan to send email in as you'll need SMTP
  credentials for each AWS Region.

Python

```
#!/usr/bin/env python3

import hmac
import hashlib
import base64
import argparse

SMTP_REGIONS = [
    "us-east-2",  # US East (Ohio)
    "us-east-1",  # US East (N. Virginia)
    "us-west-2",  # US West (Oregon)
    "ap-south-1",  # Asia Pacific (Mumbai)
    "ap-northeast-2",  # Asia Pacific (Seoul)
    "ap-southeast-1",  # Asia Pacific (Singapore)
    "ap-southeast-2",  # Asia Pacific (Sydney)
    "ap-northeast-1",  # Asia Pacific (Tokyo)
    "ca-central-1",  # Canada (Central)
    "eu-central-1",  # Europe (Frankfurt)
    "eu-west-1",  # Europe (Ireland)
    "eu-west-2",  # Europe (London)
    "eu-south-1",  # Europe (Milan)
    "eu-north-1",  # Europe (Stockholm)
    "sa-east-1",  # South America (Sao Paulo)
    "us-gov-west-1",  # AWS GovCloud (US)
    "us-gov-east-1",  # AWS GovCloud (US)
]

# These values are required to calculate the signature. Do not change them.
DATE = "11111111"
SERVICE = "ses"
MESSAGE = "SendRawEmail"
TERMINAL = "aws4_request"
VERSION = 0x04


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def calculate_key(secret_access_key, region):
    if region not in SMTP_REGIONS:
        raise ValueError(f"The {region} Region doesn't have an SMTP endpoint.")

    signature = sign(("AWS4" + secret_access_key).encode("utf-8"), DATE)
    signature = sign(signature, region)
    signature = sign(signature, SERVICE)
    signature = sign(signature, TERMINAL)
    signature = sign(signature, MESSAGE)
    signature_and_version = bytes([VERSION]) + signature
    smtp_password = base64.b64encode(signature_and_version)
    return smtp_password.decode("utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Convert a Secret Access Key to an SMTP password."
    )
    parser.add_argument("secret", help="The Secret Access Key to convert.")
    parser.add_argument(
        "region",
        help="The AWS Region where the SMTP password will be used.",
        choices=SMTP_REGIONS,
    )
    args = parser.parse_args()
    print(calculate_key(args.secret, args.region))


if __name__ == "__main__":
    main()

```

To obtain your SMTP password by using this script, save the preceding code
as `smtp_credentials_generate.py`. Then, at the command
line, run the following command:

```
python `path/to/`smtp_credentials_generate.py `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` `us-east-1`
```

In the preceding command, do the following:

- Replace `path/to/` with the path to the
  location where you saved
  `smtp_credentials_generate.py`.
- Replace `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` with the
  secret access key that you want to convert into an SMTP
  password.
- Replace `us-east-1` with the AWS Region
  in which you want to use the SMTP credentials.

When this script runs successfully, the only output is your SMTP
password.

## Migrating a SMTP user from an existing

inline policy to a group policy (security recommendation)

###### Important

If you created SES SMTP credentials before September 6, 2024, an inline
policy and a tag have been attached to your SMTP user. SES is moving away
from inline policies and encourages you to do the same as a security
recommendation.

Before migrating a SMTP user off of an existing inline policy to a group policy, you
must first create an IAM user group with the SES permissions policy to take the
place of the inline policy. If you've already created this IAM user group, or it was
automatically created for SMTP credentials you created from September 6, 2024 onward,
you can skip directly to _step 10_ in the following
procedures.

###### To migrate from an existing inline policy to a managed group

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Under **Access management**, choose
   **Polices** followed by **Create
   policy**.
3. In the **Policy editor**, select **JSON**
   and remove any example code in the editor.
4. Paste to the following permissions policy into the editor:

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
"Effect": "Allow",
 "Action": "ses:SendRawEmail",
 "Resource": "*"
 }
 ]
}`

```

5. Select **Next** and enter `AmazonSesSendingAccess`
   in the **Policy name** field followed by **Create
   policy**.
6. Under **Access management**, choose **User
   groups** followed by **Create group**.
7. Enter `AWSSESSendingGroupDoNotRename` in the **User group
   name** field.
8. Add SMTP users to the group by selecting them from the **Add users to
   the group** table.
9. Attach the `AmazonSesSendingAccess` policy created previously by
   selecting it from the **Attach permissions policies** table
   followed by **Create user group**.

Now that you've created the IAM user group with the SES permissions
policy, you can migrate a SMTP user from their current inline policy to this
group policy as explained in the remaining steps. 10. Under **Access management**, choose
**Users** followed by selecting the SMTP user you want to
migrate. 11. Select the **Groups** tab and choose **Add user to
groups**. 12. Select the `AWSSESSendingGroupDoNotRename` group followed by
**Add user to group(s)**. 13. Select the **Permissions** tab and confirm that there are two
rows listed with `AmazonSesSendingAccess` the in the **Policy
name** column, one with _Inline_ and one with
_Group `AWSSESSendingGroupDoNotRename`_ listed
in the **Attached via** column. 14. Select only the row that contains `AmazonSesSendingAccess` in the
**Policy name** column and _Inline_ in
the **Attached via** column followed by
**Remove** and confirm with **Remove
policy**.

Verify the row with _Group
`AWSSESSendingGroupDoNotRename`_ in the
**Attached via** column remains. 15. Select the **Tags** tab followed by **Manage
tags**. 16. Select **Remove** next to the row that contains
_InvokedBy_ in the **Key** column and
_SESConsole_ in the **Value** column
followed by **Save changes**.

###### Important

The `AmazonSesSendingAccess` policy (either as an inline or group
policy or both) must remain attached to the SMTP user to make sure their sending is
not impacted. Only remove the inline policy after the group policy is attached to
your user.
