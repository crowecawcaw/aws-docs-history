# Setting up open source OpenSearch permissions

If you use open source OpenSearch, you must be able to access your Amazon Personalize resources from your open search cluster. To
grant access, do the following:

- If you're setting up OpenSearch from scratch, you can use a [quick start bash script](https://github.com/opensearch-project/search-processor/blob/main/helpers/personalized_search_ranking_quickstart.sh "https://github.com/opensearch-project/search-processor/blob/main/helpers/personalized_search_ranking_quickstart.sh") to run an OpenSearch cluster in a
  Docker container. The script uses the default credentials in your AWS profile. You can specify an alternate profile
  when you run the script.

These credentials must be associated with a user or role that has permission to perform the GetPersonalizedRanking
action for your Amazon Personalize campaign. For an example of an IAM policy, see [IAM policy examples](#opensearch-role-policy-example "#opensearch-role-policy-example"). Alternatively, the credentials must have permission to assume a
role that has these permissions. You can provide the Amazon Resource Name (ARN) for this role when you create a
pipeline for the Amazon Personalize Search Ranking plugin.

- If you don't use the [quick start bash script](https://github.com/opensearch-project/search-processor/blob/main/helpers/personalized_search_ranking_quickstart.sh "https://github.com/opensearch-project/search-processor/blob/main/helpers/personalized_search_ranking_quickstart.sh"), you can manually add your credentials to your OpenSearch keystore. These
  credentials must correspond with a user or role that has permission to perform the GetPersonalizedRanking action for
  your Amazon Personalize campaign.

To manually add your AWS credentials to your OpenSearch keystore, run the following command where your
OpenSearch cluster is running (such as a Docker container). Then provide each credential. If you don't use a session
token, you can omit the final line in the command.

```
opensearch-keystore add \
personalized_search_ranking.aws.access_key \
personalized_search_ranking.aws.secret_key \
personalized_search_ranking.aws.session_token
```

- If you run your OpenSearch cluster on an Amazon EC2 instance, you can grant permissions with an IAM instance profile.
  The policy attached to the role must grant it permission to perform the GetPersonalizedRanking action for your Amazon Personalize
  campaign. It must also grant Amazon EC2 permissions to assume the role.

For information about Amazon EC2 instance profiles, see [Using instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md"). For
a policy example, see [IAM policy examples](#opensearch-role-policy-example "#opensearch-role-policy-example").

## IAM policy examples

The following policy example grants a user or role the minimum permissions to get a personalized ranking from your
Amazon Personalize campaign. For `Campaign ARN`, specify the Amazon Resource Name (ARN) of your Amazon Personalize campaign.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "personalize:GetPersonalizedRanking"
 ],
 "Resource": "arn:aws:personalize:us-east-1:111122223333:campaign/`YourResourceId`"
 }
 ]
}`

```

Additionally, if you run your OpenSearch cluster on an Amazon EC2 instance and grant permissions with an IAM instance
profile, the trust policy for the role must grant Amazon EC2 `AssumeRole` permissions as follows. For information
about Amazon EC2 instance profiles, see [Using instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ec2.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
