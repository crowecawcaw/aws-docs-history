

# Prerequisites for sharing

**Owner account**
+ Your account must own the TD. You can't share a TD that was shared with you.
+ You can't share AWS managed transformations.
+ The TD must be published. Drafts can't be shared.
+ Share in the Region where the TD is published. The share commands use the Region from `AWS_REGION` or your AWS profile. For more information, see [Configuring AWS Region](custom-get-started.md#custom-region-configuration).
+ To share with your organization or an OU, or to share with accounts in your organization without invitations, sharing with AWS Organizations must be turned on in AWS RAM. A principal in the organization's management account turns it on once, on the AWS RAM console **Settings** page or with `aws ram enable-sharing-with-aws-organization`. The organization must have all features enabled. Turning on trusted access for AWS RAM in the AWS Organizations console doesn't turn on sharing in AWS RAM. For more information, see [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.
+ Your IAM principal needs AWS RAM permissions to create and manage shares. For more information, see [Identity-based policy examples for sharing](custom-sharing-policy-examples.md).
+ To use the share commands, you need version 3.23.0 or later of the AWS Transform CLI. To update, run `atx update`.

**Consumer account**
+ Run the TD in the same Region as the share.
+ Your IAM principal needs AWS RAM permissions to view and accept invitations, and `transform-custom:ExecuteTransformation` on the shared TD's ARN. The ARN includes the owner's account ID, so a policy that allows only `arn:aws:transform-custom:*:{{your-account-id}}:package/*` doesn't cover shared TDs. For more information, see [Identity-based policy examples for sharing](custom-sharing-policy-examples.md).