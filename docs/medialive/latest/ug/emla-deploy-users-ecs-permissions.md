# Create special FAS policies

After you have assigned permissions to MediaLive Anywhere users, you must create two extra
policies:

- A Create Cluster policy that you must attach to the roles of users who can create
  a cluster. This policy lets MediaLive send a request to Amazon Elastic Container Service to create an Amazon ECS
  cluster.
- A Node Registration policy that you must attach to the roles of users who can
  create nodes. This policy lets MediaLive send a request to Amazon Elastic Container Service to create an Amazon ECS
  service.
  Both these policies allow MediaLive to make the requests using IAM forward access
  sessions (FAS).

## Create the create cluster policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**. Then
   choose **Create policy**. On the page that appears, choose the
   **JSON** view (instead of the **Visual** view).
3. Erase the sample, copy the text that appears at the end of this procedure, and
   paste it into the **Policy editor**.
4. Choose **Next**. Give the policy a name. We recommend the name
   `MediaLiveAnywhereCreateCluster`.
5. Choose **Create policy**.

## Create the node registration

policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**. Then
   choose **Create policy**. On the page that appears, choose the
   **JSON** view (instead of the **Visual** view).
3. Erase the sample, copy the text that appears at the end of this procedure, and
   paste it into the **Policy editor**.
4. Choose **Next**. Give the policy a name. We recommend the name
   `MediaLiveAnywhereRegisterScript`.
5. Choose **Create policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SSMCreateActivation",
 "Effect": "Allow",
 "Action": [
 "ssm:AddTagsToResource",
 "ssm:CreateActivation"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/created_by": "MediaLiveAnywhere"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "ssm.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```
