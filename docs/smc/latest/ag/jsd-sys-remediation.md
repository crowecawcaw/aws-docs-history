# AWS Systems Manager Automation Suggested

Remediation

The **AWS Systems Manager Automation Suggested Remediation** field should be set to the JSON string that represents a list
of objects (maps) that correspond to the automation documents as
remediations, each with the following keys:

- _documentName_: the name of the Systems Manager
  automation document
- _description_: a description of the remediation
  to display in Jira; this may be different to the document
  description in AWS and might explain why it is a good remediation
  for the issue where this is being set
- _accountName_: the name or alias of the AWS
  account configured in Jira that should be used to access this
  resource
- _region_: the Region where AWS Config should be
  accessed to get information on this resource
  For example, the following value would suggest the
  `AWS-DisableS3BucketPublicReadWrite` automation document,
  with a description to show in Jira, to apply in
  `eu-central-1`, using the account and end-user credentials
  that is specified in Jira for the AWS account identified in Jira as
  `MyAccount1`:

```

                               [ { "documentName": "AWS-DisableS3BucketPublicReadWrite",
        "description": "This will make the bucket private, resolving the issue.",
        "accountName": "MyAccount1",
        "region": "eu-central-1" } ]


```

###### Scripting Field Creation

As an example, the following bash script using curl links the
above-noted resource to an issue and attaches a suggested remediation.
The values used below assume Jira is at _localhost:2990/jira_ with login _admin:admin_, the issue is _PRJ-1_, and the field IDs are 10011 (AWS Config linked
resources) and 10010 (suggested remediation). These should be changed
to reflect your environment.

1. Set the following to correspond to your environment and
   issue:

JIRA_BASE_URL=http://localhost:2990/jira

JIRA_USER_PASS=admin:admin

ISSUE_KEY=PRJ-1 2. Set the field ID and edit the JSON record for an AWS Config resource
to link.

```

                          CUSTOM_FIELD_ID=customfield_10011
cat > value.json  EOF
    [ { "resourceId": "my-bucket",
        "resourceType": "AWS::S3::Bucket",
        "accountName": "MyAccount1",
        "region": "eu-central-1" } ]
EOF


```

3. Define a helper function to escape the JSON.

```

                        json_escape () {
    printf '%s' "$1" | python -c \
      'import json,sys; print(json.dumps(sys.stdin.read()))'
}


```

4. Make the REST call to set the AWS Config Linked Resource field.

```

                        curl -v -D- -X PUT  -H "Content-Type: application/json" \
  --data '{ "update": { "'${CUSTOM_FIELD_ID}'": [ {"set": '"$(
     json_escape "$(cat value.json)")"' } ] } }' \
  -u admin:admin ${JIRA_BASE_URL}/rest/api/2/issue/${ISSUE_KEY}


```

5. Set the field ID and edit the JSON record for a suggested
   remediation to attach.

```

                        CUSTOM_FIELD_ID=customfield_10010
cat > value.json  EOF
    [ { "documentName": "AWS-DisableS3BucketPublicReadWrite",
        "description": "This will make the bucket private, resolving the issue.",
        "accountName": "MyAccount1",
        "region": "eu-central-1" } ]
EOF


```

6. Make the REST call to set the **AWS Systems Manager
   Automation Suggested Remediations** field.

```

                        curl -v -D- -X PUT  -H "Content-Type: application/json" \
  --data '{ "update": { "'${CUSTOM_FIELD_ID}'": [ {"set": '"$(
     json_escape "$(cat value.json)")"' } ] } }' \
  -u ${JIRA_USER_PASS} ${JIRA_BASE_URL}/rest/api/2/issue/${ISSUE_KEY}


```

The issue should then show AWS Config for the bucket and a suggested
remediation to make it private.
