# How to allow or disallow input location types

AWS Elemental MediaConvert supports Amazon S3, HTTPS, and HTTP input location types for your input media
and files. You can allow or disallow access to one or more of these input location types by
using a MediaConvert policy.

By default, each Region in your AWS account does not have a policy and MediaConvert
allows all supported input location types. You only need to create an input policy if you
want to disallow access to one or more of these input location types.

To prevent jobs from running with a disallowed input location type, create a MediaConvert
_Input policy_.

Additionally, to prevent jobs from being submitted to the MediaConvert API if an Input
policy isn't in place, create an IAM policy using _condition
keys_. You can apply these IAM policies to IAM roles across your
organization.

The following sections describe how to create an Input policy and how to use IAM
condition keys to allow or disallow input location types.

###### Topics

- [How to allow or disallow input location types using an
  Input policy](#input-policies "#input-policies")
- [How to use IAM condition keys with
  Input policies](#input-policy-condition-keys "#input-policy-condition-keys")

## How to allow or disallow input location types using an

Input policy

To create or change a policy, submit a **put-policy** command using the
API, SDK, or Command Line Interface (CLI) and include the policy in JSON. Visit the
[MediaConvert API Reference](../apireference/policy.md "../apireference/policy.md") to learn more about supported policy commands
and expected response codes.

The following is an example of how to submit a policy using the CLI. This example allows
jobs with Amazon S3 and HTTPS inputs, and disallows jobs with HTTP inputs:

```
`aws mediaconvert put-policy --policy '{"S3Inputs":"ALLOWED", "HttpsInputs":"ALLOWED", "HttpInputs":"DISALLOWED"}'`
```

If you don’t specify an input location in the policy JSON, MediaConvert will treat the
input location as ALLOWED. Here is another example that allows jobs with Amazon S3 and HTTPS
inputs, and disallows jobs with HTTP inputs:

```
`aws mediaconvert put-policy --policy '{"HttpInputs":"DISALLOWED"}'`
```

Note that the put-policy command overwrites any existing policy in the Region.

**Retrieve the current policy**

To retrieve the current policy in JSON, submit a **get-policy**
command:

```
`aws mediaconvert get-policy`
```

**Delete the current policy**

To delete the current policy and allow all inputs (reverting to the default behavior),
submit a **delete-policy** command:

```
`aws mediaconvert delete-policy`
```

**What happens when you try to submit a job with a disallowed input
location?**

If you attempt to submit a job that specifies an input location that your policy
disallows, MediaConvert will instead return an **`HTTP 400
 (BadRequestException)`** error. The error message will be: **`You
 specified an input location that your policy disallows. Specify an allowed input
 location and resubmit your job.`** Since MediaConvert prevents these jobs from
being submitted, they will not appear in your job history.

If you submit a job that specifies an input location that is allowed, but the job requires
accessing another input location that is disallowed, your job will fail. For example, you
might encounter this if you specify an Apple HLS manifest on an allowed Amazon S3 location that
references other input segment files on a disallowed HTTP location. The job failure error
code will be **`3457`** and the message will be: **`You specified
 an input location that your policy disallows. Specify an allowed input location and
 resubmit your job.`**

## How to use IAM condition keys with

Input policies

When you include a _condition key_ in your IAM
policy that you use to submit create job requests, IAM checks if your account has
an Input policy that matches that condition. The condition you specify must match
your account's Input policy for the API request to be authorized. You can use any of
the following boolean condition keys:

- **HttpInputsAllowed**
- **HttpsInputsAllowed**
- **S3InputsAllowed**

When using condition keys, consider the following scenarios:

If the condition and Input policy match, for example if you set **HTTPInputsAllowed** to `*true*` and your account's Input policy allows HTTP inputs, then
your create job request will be submitted to the MediaConvert API.

If the condition and Input policy do not match, for example if you set **HTTPInputsAllowed** to `*false*` and your account's Input policy allows HTTP inputs,
then your create job request will not be submitted to the MediaConvert API. You will
receive following error message instead: **`"message": "User:
 arn:aws:iam::111122223333:user/User is not authorized to perform:
 mediaconvert:CreateJob on resource:
 arn:aws:mediaconvert:us-west-2:111122223333:queues/Default"`**

If the condition and Input policy match, for example if you set **HTTPInputsAllowed** to `*false*` and your account's Input policy _disallows_ HTTP inputs, then your create job request will be submitted to
the MediaConvert API. However, the API will then return an **`HTTP 400
 (BadRequestException)`** error. The error message will be: **`You
 specified an input location that your policy disallows. Specify an allowed input
 location and resubmit your job.`**

For more information about using IAM condition keys, see [IAM JSON
policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the
_IAM User Guide_.

The following JSON is an example IAM policy using MediaConvert condition keys that
checks if your account has an Input policy that disallows HTTP inputs:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`BlockHTTPInputsExample`",
 "Effect": "Allow",
 "Action": "mediaconvert:CreateJob",
 "Resource": "*",
 "Condition": {
 "BoolIfExists": {
 "mediaconvert:HttpInputsAllowed": false
 }
 }
 }
 ]
}`

```

For more information about condition key support within MediaConvert, see [How AWS Elemental MediaConvert works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
