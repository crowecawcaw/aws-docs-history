# Tutorial: Configure a domain with the internal user database

and HTTP basic authentication

This tutorial covers another popular [fine-grained access
control](fgac.md "fgac.md") use case: a master user in the internal user database and HTTP basic
authentication for OpenSearch Dashboards. The master user can then sign in to OpenSearch Dashboards,
create an internal user, map the user to a role, and use fine-grained access control to limit
the user's permissions.

You'll complete the following steps in this tutorial:

1. [Create a domain with a master user](#fgac-http-auth-domain "#fgac-http-auth-domain")
2. [Configure an internal user in
   OpenSearch Dashboards](#fgac-http-auth-dashboards-user "#fgac-http-auth-dashboards-user")
3. [Map roles in
   OpenSearch Dashboards](#fgac-http-auth-dashboards-map "#fgac-http-auth-dashboards-map")
4. [Test the permissions](#fgac-http-auth-test "#fgac-http-auth-test")

## Step 1: Create a domain

Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home/](https://console.aws.amazon.com/aos/home/ "https://console.aws.amazon.com/aos/home/") and [create a domain](createupdatedomains.md "createupdatedomains.md") with the following settings:

- OpenSearch 1.0 or later, or Elasticsearch 7.9 or later
- Public access
- Fine-grained access control with a master user in the internal user database
  (`TheMasterUser` for the rest of this tutorial)
- Amazon Cognito authentication for Dashboards _disabled_
- The following access policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "es:ESHttp*"
 ],
 "Resource": "arn:aws:es:`us-east-1`:`111122223333`:domain/`{domain-name}`/*"
 }
 ]
}`

```

- HTTPS required for all traffic to the domain
- Node-to-node encryption
- Encryption of data at rest

## Step 2: Create an internal user in

OpenSearch Dashboards

Now that you have a domain, you can sign in to OpenSearch Dashboards and create an internal
user.

1. Go back to the OpenSearch Service console and navigate to the OpenSearch Dashboards URL for the domain
   you created. The URL follows this format:
   ``domain-endpoint`/\_dashboards/`.
2. Sign in with the `TheMasterUser`.
3. Choose **Add sample data** and add the sample flight data.
4. In the left navigation pane, choose **Security**,
   **Internal users**, **Create internal user**.
5. Name the user `new-user` and specify a password. Then choose
   **Create**.

## Step 3: Map roles in

OpenSearch Dashboards

Now that your user is configured, you can map your user to a role.

1. Stay in the **Security** section of OpenSearch Dashboards and choose
   **Roles**, **Create role**.
2. Name the role `new-role`.
3. For **Index**, specify
   `opensearch_dashboards_sample_data_fli*`
   (`kibana_sample_data_fli*` on Elasticsearch domains) for the index
   pattern.
4. For the action group, choose **read**.
5. For **Document level security**, specify the following
   query:

```
{
  "match": {
    "FlightDelay": true
  }
}
```

6. For field-level security, choose **Exclude** and specify
   `FlightNum`.
7. For **Anonymization**, specify `Dest`.
8. Choose **Create**.
9. Choose **Mapped users**, **Manage mapping**. Then
   add `new-user` to **Users** and choose
   **Map**.
10. Return to the list of roles and choose
    **opensearch_dashboards_user**. Choose **Mapped
    users**, **Manage mapping**. Then add `new-user`
    to **Users** and choose **Map**.

## Step 4: Test the permissions

When your roles are mapped correctly, you can sign in as the limited user and test the
permissions.

1. In a new, private browser window, navigate to the OpenSearch Dashboards URL for the
   domain, sign in using the `new-user` credentials, and choose
   **Explore on my own**.
2. Go to **Dev Tools** and run the default search:

```
GET _search
{
  "query": {
    "match_all": {}
  }
}
```

Note the permissions error. `new-user` doesn't have permissions to run
cluster-wide searches. 3. Run another search:

```
GET dashboards_sample_data_flights/_search
{
  "query": {
    "match_all": {}
  }
}
```

Note that all matching documents have a `FlightDelay` field of
`true`, an anonymized `Dest` field, and no
`FlightNum` field. 4. In your original browser window, signed in as `TheMasterUser`, choose
**Dev Tools** and perform the same searches. Note the difference in
permissions, number of hits, matching documents, and included fields.
