As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Quotas for CodeGuru Reviewer

The following table lists the current quota in Amazon CodeGuru Reviewer. This quota is for each
supported AWS Region for each AWS account.

## Repositories

| Resource                                           | Default |
| -------------------------------------------------- | ------- |
| Maximum repository size                            | 4 GB    |
| **CodeCommit repositories**                        |
| Maximum number of analyzed pull requests per month | 5,000   |
| **Source code files**                              |
| Maximum Java source code size                      | 300 MB  |
| Maximum Python source code size                    | 50 MB   |

## Tags

Tag limits apply to tags on CodeGuru Reviewer associated repository resources.

| Resource                                                 | Default                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Maximum number of tags you can associate with a resource | 50 (tags are case sensitive).                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Resource tag key names                                   | Any combination of Unicode letters, numbers, spaces, and allowed<br>characters in UTF-8 between 1 and 127 characters in length. Allowed<br>characters are `+<br>• = . _ : / @`.<br>Tag key names must be unique, and each key can only have one<br>value. A tag key name cannot:<br>• begin with `aws:`<br>• consist only of spaces<br>• end with a space<br>• contain emojis or any of the following characters: `?<br>^<br>• [ \ ~ ! # $ % &<br>• ( ) > < | " ' ` [ ] { }<br>;`  |
| Resource tag values                                      | Any combination of Unicode letters, numbers, spaces, and allowed<br>characters in UTF-8 between 0 and 255 characters in length. Allowed<br>characters are `+<br>• = . _ : / @`.<br>A key can only have one value, but many keys can have the same<br>value. A tag key value cannot contain emojis or any of the following<br>characters: `? ^<br>• [ \ ~ ! # $ % &<br>• ( ) > <                                                                             | " ' `<br>[ ] { } ;`. |

## CodeGuru Reviewer quotas for

creating, deploying, and managing an API

The following fixed quotas apply to creating, deploying, and managing an API in
CodeGuru Reviewer, using the AWS CLI, the API Gateway console, or the API Gateway REST API and its SDKs. These
quotas can't be increased.

The default quota for all except three CodeGuru Reviewer APIs is 1 request per second per
account. None of these quotas can be increased. For a list of all CodeGuru Reviewer APIs, see
[Amazon CodeGuru Reviewer Actions](../reviewer-api/API_Operations.md "../reviewer-api/API_Operations.md").

The three APIs with different default quotas are in the following table.

| Action                                                                                                                           | Default quota                         | Can be increased |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ---------------- |
| [AssociateRepository](../reviewer-api/API_AssociateRepository.md "../reviewer-api/API_AssociateRepository.md")                   | 1 request every 2 seconds per account | No               |
| [CreateCodeReview](../reviewer-api/API_CreateCodeReview.md "../reviewer-api/API_CreateCodeReview.md")                            | 1 request every 2 seconds per account | No               |
| [PutRecommendationFeedback](../reviewer-api/API_PutRecommendationFeedback.md "../reviewer-api/API_PutRecommendationFeedback.md") | 2 request per second per account      | No               |
