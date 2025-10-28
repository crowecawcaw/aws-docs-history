# Filter Bitbucket webhook events (SDK)

To use the AWS CodeBuild SDK to filter webhook events, use the `filterGroups`
field in the request syntax of the `CreateWebhook` or
`UpdateWebhook` API methods. For more information, see [WebhookFilter](../APIReference/API_WebhookFilter.md "../APIReference/API_WebhookFilter.md") in the _CodeBuild API Reference_.

To create a webhook filter that triggers a build for pull requests only, insert the
following into the request syntax:

```
"filterGroups": [
  [
    {
      "type": "EVENT",
      "pattern": "PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_MERGED, PULL_REQUEST_CLOSED"
    }
  ]
]

```

To create a webhook filter that triggers a build for specified branches only, use the
`pattern` parameter to specify a regular expression to filter branch
names. Using an example of two filter groups, a build is triggered when one or both
evaluate to true:

- The first filter group specifies pull requests that are created or updated on
  branches with Git reference names that match the regular expression
  `^refs/heads/main$` and head references that match
  `^refs/heads/myBranch$`.
- The second filter group specifies push requests on branches with Git reference
  names that match the regular expression `^refs/heads/myBranch$`.

```
"filterGroups": [
  [
    {
      "type": "EVENT",
      "pattern": "PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_CLOSED"
    },
    {
      "type": "HEAD_REF",
      "pattern": "^refs/heads/myBranch$"
    },
    {
      "type": "BASE_REF",
      "pattern": "^refs/heads/main$"
    }
  ],
  [
    {
      "type": "EVENT",
      "pattern": "PUSH"
    },
    {
      "type": "HEAD_REF",
      "pattern": "^refs/heads/myBranch$"
    }
  ]
]

```

You can use the `excludeMatchedPattern` parameter to specify which events
do not trigger a build. In this example, a build is triggered for all requests except
tag events.

```
"filterGroups": [
  [
    {
      "type": "EVENT",
      "pattern": "PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_MERGED, PULL_REQUEST_CLOSED"
    },
    {
      "type": "HEAD_REF",
      "pattern": "^refs/tags/.*",
      "excludeMatchedPattern": true
    }
  ]
]

```

You can create a filter that triggers a build only when a change is made by a
Bitbucket user with account ID `actor-account-id`.

###### Note

For information about how to find your Bitbucket account ID, see
https://api.bitbucket.org/2.0/users/`user-name`, where
`user-name` is your Bitbucket user name.

```
"filterGroups": [
  [
    {
      "type": "EVENT",
      "pattern": "PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_MERGED, PULL_REQUEST_CLOSED"
    },
    {
      "type": "ACTOR_ACCOUNT_ID",
      "pattern": "actor-account-id"
    }
  ]
]

```

You can create a filter that triggers a build only when files with names that match
the regular expression in the `pattern` argument change. In this example, the
filter group specifies that a build is triggered only when files with a name that
matches the regular expression `^buildspec.*` change.

```
"filterGroups": [
  [
    {
      "type": "EVENT",
      "pattern": "PUSH"
    },
    {
      "type": "FILE_PATH",
      "pattern": "^buildspec.*"
    }
  ]
]

```

In this example, the filter group specifies that a build is triggered only when files are changed in
`src` or `test` folders.

```
"filterGroups": [
    [
        {
            "type": "EVENT",
            "pattern": "PUSH"
        },
        {
            "type": "FILE_PATH",
            "pattern": "^src/.+|^test/.+"
        }
    ]
]
```

You can create a filter that triggers a build only when the head commit message
matches the regular expression in the pattern argument. In this example, the filter
group specifies that a build is triggered only when the head commit message of the push
event matches the regular expression `\[CodeBuild\]`.

```
  "filterGroups": [
    [
      {
        "type": "EVENT",
        "pattern": "PUSH"
      },
      {
        "type": "COMMIT_MESSAGE",
        "pattern": "\[CodeBuild\]"
      }
    ]
  ]

```
