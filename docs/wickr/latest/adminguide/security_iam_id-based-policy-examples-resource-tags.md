

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Control access to Wickr networks based on tags

The following policy allows a principal to get a network and list its tags only when the network has the tag `Environment=production`.

```
{
   "Version": "2012-10-17", 		 	 	 
   "Statement": [
      {
         "Sid": "AccessProductionWickrNetworks",
         "Effect": "Allow",
         "Action": [
            "wickr:GetNetwork",
            "wickr:ListTagsForResource"
         ],
         "Resource": "arn:aws:wickr:*:*:network/*",
         "Condition": {
            "StringEquals": {
               "aws:ResourceTag/Environment": "production"
            }
         }
      }
   ]
}
```