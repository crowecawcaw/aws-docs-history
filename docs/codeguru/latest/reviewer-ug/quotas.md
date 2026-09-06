

As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

# Quotas for CodeGuru Reviewer
<a name="quotas"></a>

The following table lists the current quota in Amazon CodeGuru Reviewer. This quota is for each supported AWS Region for each AWS account. 

## Repositories
<a name="limits-reviewer-all"></a>



<table>
<thead>
  <tr><th>Resource</th><th>Default</th></tr>
</thead>
<tbody>
  <tr><td>Maximum repository size</td><td>4 GB</td></tr>
  <tr><td colspan="2"> <b>CodeCommit repositories</b></td></tr>
  <tr><td>Maximum number of analyzed pull requests per month</td><td>5,000</td></tr>
  <tr><td colspan="2"> <b>Source code files</b></td></tr>
  <tr><td>Maximum Java source code size</td><td>300 MB</td></tr>
  <tr><td>Maximum Python source code size</td><td>50 MB</td></tr>
</tbody>
</table>


## Tags
<a name="limits-tags"></a>

Tag limits apply to tags on CodeGuru Reviewer associated repository resources. 



| Resource | Default | 
| --- | --- | 
| Maximum number of tags you can associate with a resource | 50 (tags are case sensitive). | 
| Resource tag key names | Any combination of Unicode letters, numbers, spaces, and allowed characters in UTF-8 between 1 and 127 characters in length. Allowed characters are `+ - = . _ : / @`.<br />Tag key names must be unique, and each key can only have one value. A tag key name cannot:+  begin with `aws:` <br />+  consist only of spaces <br />+  end with a space <br />+  contain emojis or any of the following characters: `? ^ * [ \ ~ ! # $ % & * ( ) > < \| " ' ` [ ] { } ;`  | 
| Resource tag values | Any combination of Unicode letters, numbers, spaces, and allowed characters in UTF-8 between 0 and 255 characters in length. Allowed characters are `+ - = . _ : / @`.<br />A key can only have one value, but many keys can have the same value. A tag key value cannot contain emojis or any of the following characters:` ? ^ * [ \ ~ ! # $ % & * ( ) > < \| " ' ` [ ] { } ;`. | 

## CodeGuru Reviewer quotas for creating, deploying, and managing an API
<a name="codeguru-reviewer-control-service-limits-table"></a>

The following fixed quotas apply to creating, deploying, and managing an API in CodeGuru Reviewer, using the AWS CLI, the API Gateway console, or the API Gateway REST API and its SDKs. These quotas can't be increased.

The default quota for all except three CodeGuru Reviewer APIs is 1 request per second per account. None of these quotas can be increased. For a list of all CodeGuru Reviewer APIs, see [ Amazon CodeGuru Reviewer Actions](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_Operations.html).

The three APIs with different default quotas are in the following table.


| Action | Default quota | Can be increased | 
| --- | --- | --- | 
| [AssociateRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_AssociateRepository.html) | 1 request every 2 seconds per account | No | 
| [CreateCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview.html) | 1 request every 2 seconds per account | No | 
| [PutRecommendationFeedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_PutRecommendationFeedback.html) | 2 request per second per account | No | 