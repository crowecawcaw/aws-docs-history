

# Tagging for ARC Region switch;
<a name="tagging.region-switch"></a>

Tags are words or phrases (meta data) that you use to identify and organize your AWS resources. You can add multiple tags to each resource, and each tag includes a key and a value that you define. For example, the key might be environment and the value might be production. You can search and filter your resources based on the tags you add.

You can tag the following resource in Region switch in ARC:
+ Plans

Tagging in ARC is available only through the API, for example, by using the AWS CLI. 

The following are examples of tagging in Region switch by using the AWS CLI.

`aws arc-region-switch --region us-east-1 create-plan --plan-name example-plan --tags Region=IAD,Stage=Prod`

For more information, see [TagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_TagResource.html) in the *Region Switch API Reference Guide* for Amazon Application Recovery Controller (ARC).