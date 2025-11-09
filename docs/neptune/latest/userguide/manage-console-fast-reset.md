# Empty an Amazon Neptune DB cluster using the fast reset API

The Neptune fast reset REST API lets you reset a Neptune graph quicky and easily,
removing all of its data.

You can do this within a Neptune notebook using the
[%db_reset](#manage-console-fast-reset-db-reset-magic "#manage-console-fast-reset-db-reset-magic") line magic.

###### Note

This feature is available starting in [Neptune engine release 1.0.4.0](engine-releases-1.0.4.md "engine-releases-1.0.4.md").

- In most cases, a fast reset operation completes within couple of
  minutes. The duration can vary somewhat depending on the load on the cluster
  when the operation is initiated.
- A fast reset operation does not result in additional I/Os.
- Storage volume size does not shrink after a fast reset. Instead, the
  storage is reused as new data is inserted. This means that the volume sizes of snapshots
  taken before and after a fast reset operation will be the same. Volume sizes of restored
  clusters using the snapshots created before and after a fast reset operation will also
  be the same
- As part of the reset operation, all instances in the DB
  cluster are restarted.

###### Note

Under rare conditions, these server restarts may also result
in failover of the cluster.

###### Important

Using fast reset may break the integration of your Neptune DB cluster
with other services. For example:

- Fast reset deletes all stream data from your database and
  completely resets streams. This means that your stream consumers may
  no longer work without new configuration.
- Fast reset removes all metadata about SageMaker AI resources being
  used by Neptune ML, including jobs and endpoints. They continue to exist
  in SageMaker AI, and you can continue to use existing SageMaker AI endpoints for Neptune ML
  inference queries, but the Neptune ML management APIs no longer work with
  them.
- Integrations such as the full-text-search integration with
  ElasticSearch are also wiped out by fast reset, and must be re-established
  manually before they can be used again.

###### To delete all data from a Neptune DB cluster using the API

1. First, you generate a token that you can then use to perform the database reset.
   This step is intended to help prevent anyone from accidentally resetting
   a database.

You do this by sending an `HTTP POST` request to the
`/system` endpoint on the writer instance of your
DB cluster to specify the `initiateDatabaseReset` action.

The `curl` command using the JSON content-type would be:

```
curl -X POST \
  -H 'Content-Type: application/json' \
      https://`your_writer_instance_endpoint`:8182/system \
  -d '{ "action" : "initiateDatabaseReset" }'
```

Or, using the `x-www-form-urlencoded` content type:

```
curl -X POST \
  -H 'Content-Type: application/x-www-form-urlencoded' \
      https://`your_writer_instance_endpoint`:8182/system \
  -d 'action=initiateDatabaseReset '
```

The `initiateDatabaseReset` request returns the reset token
in its JSON response, like this:

```
{
  "status" : "200 OK",
  "payload" : {
    "token" : "`new_token_guid`"
  }
}
```

The token remains valid for one hour (60 minutes) after it is issued.

If you send the request to a reader instance or to the status
endpoint, Neptune will throw a `ReadOnlyViolationException`.

If you send multiple `initiateDatabaseReset` requests,
only the latest token generated will be valid for the second step,
where you actually perform the reset.

If the server restarts right after your `initiateDatabaseReset`
request, the generated token becomes invalid, and you need to send a new
request to get a new token. 2. Next, you send a `performDatabaseReset` request with the token
that you got back from `initiateDatabaseReset` to the
`/system` endpoint on the writer instance of your
DB cluster. This deletes all data from your DB cluster.

The `curl` command using the JSON content-type is:

```
curl -X POST \
  -H 'Content-Type: application/json' \
      https://`your_writer_instance_endpoint`:8182/system \
  -d '{
        "action" : "performDatabaseReset",
        "token" : "`token_guid`"
      }'
```

Or, using the `x-www-form-urlencoded` content type:

```
curl -X POST \
  -H 'Content-Type: application/x-www-form-urlencoded' \
      https://`your_writer_instance_endpoint`:8182/system \
  -d 'action=performDatabaseReset&token=`token_guid`'
```

The request returns a JSON response. If the request is accepted,
the response is:

```
{
  "status" : "200 OK"
}
```

If the token you sent doesn't match the one that was issued,
the response looks like this:

```
{
  "code" : "InvalidParameterException",
  "requestId":"`token_guid`",
  "detailedMessage" : "System command parameter 'token' : '`token_guid`' does not match database reset token"
}
```

If the request is accepted and the reset begins, the server restarts and
deletes the data. You cannot send any other requests to the DB cluster while
it is resetting.

## Using the fast reset API with IAM-Auth

If you have IAM-Auth enabled on your DB cluster, you can use [awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl") to send fast reset commands
that are authenticated using IAM-Auth:

###### Using awscurl to send fast-reset requests with IAM-Auth

1. Set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
   environment variables correctly (and also `AWS_SECURITY_TOKEN` if you are using
   temporary credential).
2. An `initiateDatabaseReset` request looks like this:

```
awscurl -X POST --service neptune-db "$SYSTEM_ENDPOINT" \
  -H 'Content-Type: application/json' --region us-west-2 \
  -d '{ "action" : "initiateDatabaseReset" }'
```

3. A `performDatabaseReset` request looks like this:

```
awscurl -X POST --service neptune-db "$SYSTEM_ENDPOINT" \
  -H 'Content-Type: application/json' --region us-west-2 \
  -d '{ "action" : "performDatabaseReset" }'
```

## Using the Neptune workbench

`%db_reset` line magic to reset a DB cluster

The Neptune workbench supports a `%db_reset` line magic that lets you
perform a fast database reset in a Neptune notebook.

If you invoke the magic without any parameters, you see a screen asking if you
want to delete all the data in your cluster, with a checkbox asking you to acknowledge
that the cluster data will no longer be available after you delete it. At that point,
you can choose to go ahead and delete the data, or cancel the operation.

A more dangerous option is to invoke `%db_reset` with the `--yes`
or `-y` option, which causes the deletion to be performed with no further
prompting.

You can also perform the reset in two steps, just as with the REST API:

```
%db_reset --generate-token
```

The response is:

```
{
  "status" : "200 OK",
  "payload" : {
    "token" : "`new_token_guid`"
  }
}
```

Then do:

```
%db_reset --token `new_token_guid`
```

The response is:

```
{
  "status" : "200 OK"
}
```

## Common error codes for fast reset operations

| Neptune error code           | HTTP status | Message                                                                               | Example                                                                                                             |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `InvalidParameterException`  | 400         | System command parameter '`action`'<br>has unsupported value '`XXX`'                  | Invalid parameter                                                                                                   |
| `InvalidParameterException`  | 400         | Too many values supplied for: `action`                                                | A fast reset request with more than one action sent with<br>header 'Content-type:application/x-www-form-urlencoded' |
| `InvalidParameterException`  | 400         | Duplicate field 'action'                                                              | A fast reset request with more than one action sent with<br>header 'Content-Type: application/json'                 |
| `MethodNotAllowedException`  | 400         | Bad route: /`bad_endpoint`                                                            | Request sent to an incorrect endpoint                                                                               |
| `MissingParameterException`  | 400         | Missing required parameters: [action]                                                 | A fast reset request doesn't contain the required 'action' parameter                                                |
| `ReadOnlyViolationException` | 400         | Writes are not permitted on a read replica instance                                   | A fast reset request was sent to a reader or status endpoint                                                        |
| `AccessDeniedException`      | 403         | Missing Authentication Token                                                          | A fast reset request was sent without correct signatures to a<br>DB endpoint with IAM-Auth enabled                  |
| `ServerShutdownException`    | 500         | Database reset is in progress. Please retry the query after the cluster is available. | When fast reset begins, existing and incoming Gremlin/Sparql<br>queries fail.                                       |
