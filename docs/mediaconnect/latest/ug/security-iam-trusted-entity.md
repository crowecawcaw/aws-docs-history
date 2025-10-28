# Setting up AWS Elemental MediaConnect as a trusted

service

You can use AWS Identity and Access Management (IAM) to control which AWS resources can be accessed by which users and applications. This includes setting up
permissions to allow AWS Elemental MediaConnect to communicate with other services on behalf of your account. To set up AWS Elemental MediaConnect as a trusted
entity, you must perform the following steps:

**[Step 1.](#security-iam-trusted-entity-create-policy "#security-iam-trusted-entity-create-policy")** – Create an IAM policy that governs which actions
you want to allow.

**[Step
2](#security-iam-trusted-entity-create-role "#security-iam-trusted-entity-create-role")** – Create an IAM role with a
trusted
relationship, and attach the policy that you created in the previous
step.

## Step 1: Create an IAM

policy to allow specific actions

In this step, you create an IAM policy that governs which actions you want to
allow.

###### To create the IAM policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**, and then choose the
   **JSON** tab.
4. Enter a policy that uses the JSON format. For examples, see the
   following:
   - [Policy
     example for connecting to your VPC](security_iam_resource-based-policy-examples.md#iam-policy-examples-for-mediaconnect-vpc "security_iam_resource-based-policy-examples.md#iam-policy-examples-for-mediaconnect-vpc")
   - [Policy examples for
     secrets in AWS Secrets Manager](iam-policy-examples-asm-secrets.md "iam-policy-examples-asm-secrets.md")

5. Choose **Review policy**.
6. For **Name**, enter a name for your policy.
7. Choose **Create policy**.

## Step 2: Create an IAM

role with a trusted relationship

In [step 1](#security-iam-trusted-entity-create-policy "#security-iam-trusted-entity-create-policy"), you
created an IAM policy that governs which actions you want to allow. In this step,
you
create
an IAM role and assign the policy to that role. Then you define AWS Elemental MediaConnect
as a trusted entity that can assume the role.

###### To create a role with a trusted relationship

1. In the navigation pane of the IAM console, choose **Roles**.
2. On the **Role** page, choose **Create role**.
3. On the **Create role** page, for **Select type of trusted entity**, choose **AWS
   service** (the default).
4. For **Choose the service that will use this role**, choose **EC2**.

You choose EC2 because MediaConnect is not currently included in this list. Choosing EC2 lets you create a role. In a later step, you
change this role to include MediaConnect instead of EC2. 5. Choose **Next: Permissions**. 6. For **Attach permissions policies**, enter the name of the policy that you created in [step 1](#security-iam-trusted-entity-create-policy "#security-iam-trusted-entity-create-policy"). 7. Select the check box next to the name of the policy, and then choose **Next: Tags**. 8. (Optional) Add metadata to the user by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM Entities](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 9. Choose **Next: Review**. 10. For **Role name**, enter a name. The name `MediaConnectAccessRole` is reserved, so you can't use it.
Instead, use a name that includes `MediaConnect` and describes this role's purpose. 11. For **Role description**, replace the default text with a description that will help you remember the purpose of this
role. 12. Choose **Create role**. 13. In the confirmation message that appears across the top of your page,
choose the name of the role that you just created by selecting
**View role**. 14. Choose **Trust relationships** tab, and then choose
**Edit trust policy**. 15. in the **Edit trust policy** window, make the following
changes to the JSON:

    * For **Service**, change
     `ec2.amazonaws.com` to
     `mediaconnect.amazonaws.com`
    * For added security, define specific conditions for the trust
     policy. This will limit MediaConnect to only using resources in your
     account. You do this by using a global condition such as the
     **Account ID**, the **flow
     ARN**, or both. See the following example of the
     conditional trust policy. For more information about the security
     benefits of the global conditions, see [Cross-service
     confused deputy prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").


    ###### Note

    The following example uses both the **Account
     ID** and **flow ARN** conditions.
     Your policy will look different if you do not use both
     conditions. If you don't know the full ARN of the flow or if you
     are specifying multiple flows, use the
     `aws:SourceArn` global context condition key with
     wildcard characters (`*`) for the unknown portions of
     the ARN. For example,
     `arn:aws:mediaconnect:*:`111122223333`:*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "mediaconnect.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:mediaconnect:`us-west-2`:`111122223333`:flow:`*`:`flow-name`"
 }
 }
 }
 ]
}`

```

16. Choose **Update policy**.
17. On the **Summary** page,
    make a note of the value for
    **Role ARN**. It looks like this:
    `arn:aws:iam::111122223333:role/MediaConnectASM`.
