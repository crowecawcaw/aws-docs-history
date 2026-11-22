

# Example: WorkSpaces Applications fleet machine role cross-service confused deputy prevention

**Example `aws:SourceAccount` Conditional:**    
****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "appstream.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{your AWS account ID}}"
                }
            }
        }
    ]
}
```

**Example `aws:SourceArn` Conditional:**  
If you want to use one IAM role for multiple fleets, we recommend using the `aws:SourceArn` global context condition key with wildcards (\*) to match multiple WorkSpaces Applications fleet resources.  
****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "appstream.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnLike": {
                "aws:SourceArn": "arn:aws:appstream:{{us-east-1}}:{{111122223333}}:fleet/{{your-fleet-name}}"
                }
            }
        }
    ]
}
```