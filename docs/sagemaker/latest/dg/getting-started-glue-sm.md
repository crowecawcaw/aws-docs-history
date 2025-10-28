# Get Started with AWS Glue Interactive

Sessions

In this guide, you learn how to initiate an AWS Glue interactive session in SageMaker AI
Studio Classic, and manage your environment with Jupyter magics.

## Permissions for AWS Glue interactive sessions in

Studio or Studio Classic

This section lists the required policies to run AWS Glue interactive sessions in
Studio or Studio Classic and explains how to set them up. In particular, it details
how to:

- Attach the `AwsGlueSessionUserRestrictedServiceRole` managed
  policy to your SageMaker AI execution role.
- Create an inline custom policy on your SageMaker AI execution role.
- Modify the trust relationship of your SageMaker AI execution role.

###### To attach the `AwsGlueSessionUserRestrictedServiceRole` managed

policy to your execution role

1. Open the [IAM
   console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Select **Roles** in the left-side panel.
3. Find the Studio Classic execution role used by your user profile. For
   information about how to view a user profile, see [View user profiles in a domain](domain-user-profile-view.md "domain-user-profile-view.md").
4. Choose your role name to access the role summary page.
5. Under the **Permissions** tab, select **Attach
   policies** from the **Add Permissions**
   dropdown menu.
6. Select the checkbox next to the managed policy
   `AwsGlueSessionUserRestrictedServiceRole`.
7. Choose **Attach policies**.

The summary page shows your newly-added managed policies.

###### To create the inline custom policy on your execution role

1. Select **Create inline policy** in the **Add
   Permissions** dropdown menu.
2. Select the **JSON** tab.
3. Copy and paste in the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`uniqueStatementId`",

 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole",
 "sts:GetCallerIdentity"
 ],
 "Resource": "arn:aws:iam::*:`role/GlueServiceRole`*"
 }
 ]
}`

```

4. Choose **Review policy**.
5. Enter a **Name** and choose **Create
   policy**.

The summary page shows your newly-added custom policy.

###### To modify the trust relationship of your execution role

1. Select the **Trust relationships** tab.
2. Chose **Edit trust policy**.
3. Copy and paste in the following policy.

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "glue.amazonaws.com",
 "sagemaker.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
]
}`

```

4. Choose **Update policy**.

You can add additional roles and policies if you need to access other AWS
resources. For a description of the additional roles and policies you can include,
see [interactive sessions with IAM](../../../glue/latest/dg/glue-is-security.md "../../../glue/latest/dg/glue-is-security.md") in the AWS Glue documentation.

## Tag propagation

Tags are commonly used to track and allocate costs, control access to your
session, isolate your resources, and more. To learn about adding metadata to your
AWS resources using tagging, or for details on common use cases, see [Additional information](#more-information "#more-information").

You can enable the automatic propagation of AWS tags to new AWS Glue interactive
sessions created from within the Studio or Studio Classic UI. When an AWS Glue
interactive session is created from Studio or Studio Classic, any [user-defined tags](../../../awsaccountbilling/latest/aboutv2/custom-tags.md "../../../awsaccountbilling/latest/aboutv2/custom-tags.md") attached to the user profile or shared space are
carried over to the new AWS Glue interactive session. Additionally,Studio and
Studio Classic automatically add two AWS-generated internal tags
((`sagemaker:user-profile-arn` and `sagemaker:domain-arn`)
or (`sagemaker:shared-space-arn` and `sagemaker:domain-arn`))
to new AWS Glue interactive sessions created from their UI. You can use these tags to
aggregate costs across individual domains, user profiles, or spaces.

### Enable tag propagation

To enable the automatic propagation of tags to new AWS Glue interactive sessions,
set the following permissions for your SageMaker AI execution role and the IAM role
associated with your AWS Glue session:

###### Note

By default, the role associated with the AWS Glue interactive session is the
same as the SageMaker AI execution role. You can specify a different execution role
for the AWS Glue interactive session by using the `%iam_role` magic
command. For information on the available Jupyter magic commands to configure
AWS Glue interactive sessions, see [Configure your AWS Glue interactive session in
Studio or Studio Classic](#glue-sm-magics "#glue-sm-magics").

- _On your SageMaker AI execution role_: Create
  a new inline policy, and paste the following JSON file. The policy
  grants the execution role permission to describe
  (`DescribeUserProfile`, `DescribeSpace`,
  `DescribeDomain`) and list the tags
  (`ListTag`) set on the user profiles, shared spaces, and SageMaker AI
  domain.

```
{
    "Effect": "Allow",
    "Action": [
        "sagemaker:ListTags"
    ],
    "Resource": [
        "arn:aws:sagemaker:*:*:user-profile/*",
        "arn:aws:sagemaker:*:*:space/*"
    ]
},
{
    "Effect": "Allow",
    "Action": [
        "sagemaker:DescribeUserProfile"
    ],
    "Resource": [
        "arn:aws:sagemaker:*:*:user-profile/*"
    ]
},
{
    "Effect": "Allow",
    "Action": [
        "sagemaker:DescribeSpace"
    ],
    "Resource": [
        "arn:aws:sagemaker:*:*:space/*"
    ]
}
{
    "Effect": "Allow",
    "Action": [
        "sagemaker:DescribeDomain"
    ],
    "Resource": [
        "arn:aws:sagemaker:*:*:domain/*"
    ]
}
```

- _On the IAM role of your AWS Glue
  session_: Create a new inline policy, and paste the
  following JSON file. The policy grants your role permission to attach
  tags (`TagResource`) to your session, or retrieve its list of
  tags (`GetTags`).

```
{
    "Effect": "Allow",
    "Action": [
        "glue:TagResource",
        "glue:GetTags"
    ],
    "Resource": [
        "arn:aws:glue:*:*:session/*"
    ]
}
```

###### Note

- Failures occurring while applying those permissions do not prevent
  the creation of AWS Glue interactive sessions. You can find details
  about the reason of the failure in Studio or Studio Classic [CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") logs.
- You must restart the kernel of your AWS Glue interactive session to
  propagate the update of a tag’s value.

It is important to note the following points:

- Once a tag is attached to a session, it cannot be removed by
  propagation.

You can remove tags from an AWS Glue interactive session directly through
the AWS CLI, the AWS Glue API, or the [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/"). For example, using
the AWS CLI, you can remove a tag by providing the session's ARN and the
tag keys you want to remove as follows:

```
aws glue untag-resource \
--resource-arn `arn:aws:glue:region:account-id:session:session-name` \
--tags-to-remove `tag-key1`,`tag-key2`
```

- Studio and Studio Classic add two AWS-generated internal tags
  ((`sagemaker:user-profile-arn` and
  `sagemaker:domain-arn`) or
  (`sagemaker:shared-space-arn` and
  `sagemaker:domain-arn`)) to new AWS Glue interactive
  sessions created from their UI. Those tags count against the limit of 50
  tags set on all AWS resources. Both
  `sagemaker:user-profile-arn` and
  `sagemaker:shared-space-arn` contain the domain ID to
  which they belong.
- Tags keys starting with `aws:`, `AWS:`, or any
  combination of upper and lowercase letters as a prefix for keys are not
  propagated and are reserved for AWS use.

### Additional information

For more information on tagging, refer to the following resources.

- To learn about adding metadata to your AWS resources with tagging,
  see [Tagging AWS
  resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").
- For information on tracking costs using tags, see [Cost analysis](../../../whitepapers/latest/sagemaker-studio-admin-best-practices/cost-attribution.md "../../../whitepapers/latest/sagemaker-studio-admin-best-practices/cost-attribution.md") in Studio administration best
  practices.
- For information on controlling access to AWS Glue based on tag keys, see
  [ABAC with AWS Glue](glue/latest/dg/security_iam_service-with-iam.md#security_iam_service-with-iam-tags "glue/latest/dg/security_iam_service-with-iam.md#security_iam_service-with-iam-tags").

## Launch your AWS Glue interactive session on

Studio or Studio Classic

After you create the roles, policies, and SageMaker AI domain, you can launch your
AWS Glue interactive session in Studio or Studio Classic.

1. Sign in to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. From the left navigation pane, choose
   **Studio**.
3. From the Studio landing page, select the domain and user profile for
   launching Studio.
4. Choose **Open Studio** and start a JupyterLab or
   Studio Classic application.
5. In the Jupyter view, choose **File**, then
   **New**, then **Notebook**.
6. For Studio Classic users: In the **Image** dropdown menu,
   select **SparkAnalytics 1.0** or **SparkAnalytics
   2.0**. In the **kernel** dropdown menu, select
   **Glue Spark** or **Glue Python [PySpark and
   Ray]**. Choose **Select**.

For Studio users, select a **Glue Spark** or
**Glue Python [PySpark and Ray]** kernel 7. (optional) Use Jupyter magics to customize your environment. For more
information about Jupyter magics, see [Configure your AWS Glue interactive session in
Studio or Studio Classic](#glue-sm-magics "#glue-sm-magics"). 8. Start writing your Spark data processing scripts. The following [notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/use-cases/pyspark_etl_and_training/pyspark-etl-training.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/use-cases/pyspark_etl_and_training/pyspark-etl-training.ipynb") showcases an end-to-end workflow for ETL on a large
dataset using an AWS Glue interactive session, exploratory data analysis, data
preprocessing, and finally training a model on the processed data with SageMaker AI.

## Configure your AWS Glue interactive session in

Studio or Studio Classic

###### Note

All magic configurations are carried over to subsequent sessions for the
lifetime of the AWS Glue kernel.

You can use Jupyter magics in your AWS Glue interactive session to modify your session
and configuration parameters. Magics are short commands prefixed with `%`
at the start of Jupyter cells that provide a quick and easy way to help you control
your environment. In your AWS Glue interactive session, the following magics are set
for you by default:

| Magic           | Default value                                         |
| --------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `%glue_version` | 3.0                                                   |
| `%iam_role`     | `execution role attached to your SageMaker AI domain` |
| `%region`       | your region                                           | You can use magics to further customize your environment. For example, if you want to change the number of workers allocated to your job from the default five to 10, you can specify `%number_of_workers 10`. If you want to configure your session to stop after 10 minutes of idle time instead of the default 2880, you can specify `%idle_timeout 10`. All of the Jupyter magics currently available in AWS Glue are also available in Studio or Studio Classic. For the complete list of AWS Glue magics available, see [Configuring AWS Glue interactive sessions for Jupyter and AWS Glue Studio notebooks](../../../glue/latest/dg/interactive-sessions-magics.md "../../../glue/latest/dg/interactive-sessions-magics.md"). |
