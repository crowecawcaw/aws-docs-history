# Monitoring CodeArtifact events

CodeArtifact is integrated with Amazon EventBridge, a service that automates and responds to events,
including changes in a CodeArtifact repository. You can create rules for events and configure what
happens when an event matches a rule. EventBridge was formerly called CloudWatch Events.

The following actions can be triggered by an event:

- Invoking an AWS Lambda function.
- Activating an AWS Step Functions state machine.
- Notifying an Amazon SNS topic or an Amazon SQS queue.
- Starting a pipeline in AWS CodePipeline.
  CodeArtifact creates an event when a package version is created, modified, or deleted. The
  following are examples of CodeArtifact events:

- Publishing a new package version (for example, by running `npm
publish`).
- Adding a new asset to an existing package version (for example, by pushing a new
  JAR file to an existing Maven package).
- Copying a package version from one repository to another using
  `copy-package-versions`. For more information, see [Copy packages between repositories](copy-package.md "copy-package.md").
- Deleting package versions using `delete-package-versions`. For more
  information, see [Delete a package or package version](delete-package.md "delete-package.md").
- Deleting a package versions using `delete-package`. One event will be published for each version of the deleted package. For more
  information, see [Delete a package or package version](delete-package.md "delete-package.md").
- Retaining a package version in a downstream repository when it has been fetched
  from an upstream repository. For more information, see
  [Working with upstream repositories in CodeArtifact](repos-upstream.md "repos-upstream.md").
- Ingesting a package version from an external repository into a CodeArtifact repository.
  For more information, see [Connect a CodeArtifact repository to a public repository](external-connection.md "external-connection.md").
  Events are delivered to both the account that owns the domain and the account that
  administers the repository. For example, suppose that account `111111111111` owns
  the domain `my_domain`. Account `222222222222` creates a repository in
  `my_domain` called `repo2`. When a new package version is published
  to `repo2`, both accounts receive the EventBridge events. The domain-owning account
  (`111111111111`) receives events for all repositories in the domain. If a
  single account owns both the domain and the repository within it, only a single event is
  delivered.

The following topics describe the CodeArtifact event format. They show you how to configure CodeArtifact
events, and how to use events with other AWS services. For more information, see [Getting Started with Amazon EventBridge](../../../eventbridge/latest/userguide/eventbridge-getting-set-up.md "../../../eventbridge/latest/userguide/eventbridge-getting-set-up.md") in the _Amazon EventBridge User
Guide_.

## CodeArtifact event format and example

The following are event fields and descriptions along with an example of a CodeArtifact event.

### CodeArtifact event format

All CodeArtifact events include the following fields.

| Event field             | Description                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| version                 | The version of the event format. There is currently only a single<br>version, `0`.                                                                                                                                                                                                                                                                               |
| id                      | A unique identifier for the event.                                                                                                                                                                                                                                                                                                                               |
| detail-type             | The type of event. This determines the fields in the<br>`detail` object. The one `detail-type`<br>currently supported is `CodeArtifact Package Version State Change`.                                                                                                                                                                                            |
| source                  | The source of the event. For CodeArtifact, it will be `aws.codeartifact`.                                                                                                                                                                                                                                                                                        |
| account                 | The AWS account ID of the account that receives the event.                                                                                                                                                                                                                                                                                                       |
| time                    | The exact time the event was triggered.                                                                                                                                                                                                                                                                                                                          |
| region                  | The region where the event was triggered.                                                                                                                                                                                                                                                                                                                        |
| resources               | A list that contains the ARN of the package that changed. The list<br>contains one entry. For information about package ARN format, see [Grant write access to<br>packages](repo-policies.md#granting-write-access-to-specific-packages "repo-policies.md#granting-write-access-to-specific-packages").                                                          |
| domainName              | The domain that contains the repository that contains the<br>package.                                                                                                                                                                                                                                                                                            |
| domainOwner             | The AWS account ID of the owner of the domain.                                                                                                                                                                                                                                                                                                                   |
| repositoryName          | The repository that contains the package.                                                                                                                                                                                                                                                                                                                        |
| repositoryAdministrator | The AWS account ID of the administrator of the repository.                                                                                                                                                                                                                                                                                                       |
| packageFormat           | The format of the package that triggered the event.                                                                                                                                                                                                                                                                                                              |
| packageNamespace        | The namespace of the package that triggered the event.                                                                                                                                                                                                                                                                                                           |
| packageName             | The name of the package that triggered the event.                                                                                                                                                                                                                                                                                                                |
| packageVersion          | The version of the package that triggered the event.                                                                                                                                                                                                                                                                                                             |
| packageVersionState     | The state of the package version when the event was triggered.<br>Possible values are `Unfinished`, `Published`,<br>`Unlisted`, `Archived`, and<br>`Disposed`.                                                                                                                                                                                                   |
| packageVersionRevision  | A value that uniquely identifies the state of the assets and metadata<br>of the package version when the event was triggered. If the package<br>version is modified (for example, by adding another JAR file to a Maven<br>package), the `packageVersionRevision` changes.                                                                                       |
| changes.assetsAdded     | The number of assets added to a package that triggered an event.<br>Examples of an asset are a Maven JAR file or a Python wheel.                                                                                                                                                                                                                                 |
| changes.assetsRemoved   | The number of assets removed from a package that triggered an<br>event.                                                                                                                                                                                                                                                                                          |
| changes.assetsUpdated   | The number of assets modified in the package that triggered the<br>event.                                                                                                                                                                                                                                                                                        |
| changes.metadataUpdated | A boolean value that is set to `true` if the event<br>includes modified package-level metadata. For example, an event might<br>modify a Maven `pom.xml` file.                                                                                                                                                                                                    |
| changes.statusChanged   | A boolean value that is set to `true` if the event's<br>`packageVersionStatus` is modified(for example, if<br>`packageVersionStatus` changes from<br>`Unfinished` to `Published`).                                                                                                                                                                               |
| operationType           | Describes the high-level type of the package version change. The<br>possible values are `Created`, `Updated`, and<br>`Deleted`.                                                                                                                                                                                                                                  |
| sequenceNumber          | An integer that specifies an event number for a package. Each event<br>on a package increments the `sequenceNumber` so events can be<br>arranged sequentially. An event can increment the<br>`sequenceNumber` by any integer number. Note EventBridge events might be received out of order.<br>`sequenceNumber` can be used to determine their<br>actual order. |
| eventDeduplicationId    | An ID used to differentiate duplicate EventBridge events. In rare cases,<br>EventBridge might trigger the same rule more than once for a single event or<br>scheduled time. Or, it might invoke the same target more than once for a<br>given triggered rule.                                                                                                    |

### CodeArtifact event example

The following is an example of a CodeArtifact event that might be triggered when an npm
package is published.

```
{
      "version":"0",
      "id":"73f03fec-a137-971e-6ac6-07c8ffffffff",
      "detail-type":"CodeArtifact Package Version State Change",
      "source":"aws.codeartifact",
      "account":"123456789012",
      "time":"2019-11-21T23:19:54Z",
      "region":"us-west-2",
      "resources":["arn:aws:codeartifact:us-west-2:111122223333:package/my_domain/myrepo/npm//mypackage"],
      "detail":{
        "domainName":"my_domain",
        "domainOwner":"111122223333",
        "repositoryName":"myrepo",
        "repositoryAdministrator":"123456789012",
        "packageFormat":"npm",
        "packageNamespace":null,
        "packageName":"mypackage",
        "packageVersion":"1.0.0",
        "packageVersionState":"Published",
        "packageVersionRevision":"0E5DE26A4CD79FDF3EBC4924FFFFFFFF",
        "changes":{
          "assetsAdded":1,
          "assetsRemoved":0,
          "metadataUpdated":true,
          "assetsUpdated":0,
          "statusChanged":true
        },
        "operationType":"Created",
        "sequenceNumber":1,
        "eventDeduplicationId":"2mEO0A2Ke07rWUTBXk3CAiQhdTXF4N94LNaT/ffffff="
      }
    }
```
