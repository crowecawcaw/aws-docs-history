# Set up tags for an API stage in API Gateway

In API Gateway, you can add a tag to an API stage, remove the tag from the stage, or view the
tag. To do this, you can use the API Gateway console, the AWS CLI/SDK, or the API Gateway REST API.

A stage can also inherit tags from its parent REST API. For more information, see [Tag inheritance in the Amazon API Gateway V1 API](apigateway-tagging-supported-resources.md#apigateway-tagging-inheritance "apigateway-tagging-supported-resources.md#apigateway-tagging-inheritance").

For more information about tagging API Gateway resources, see [Tagging your API Gateway resources](apigateway-tagging.md "apigateway-tagging.md").

###### Topics

- [Set up tags for an API stage using the API Gateway console](#set-up-tags-using-console "#set-up-tags-using-console")
- [Set up tags for an API stage using the AWS CLI](#set-up-tags-using-cli "#set-up-tags-using-cli")
- [Set up tags for an API stage using the API Gateway REST API](#set-up-tags-using-api "#set-up-tags-using-api")

## Set up tags for an API stage using the API Gateway console

The following procedure describes how to set up tags for an API stage.

###### To set up tags for an API stage by using the API Gateway console

1. Sign in to the API Gateway console.
2. Choose an existing API, or create a new API that includes resources, methods,
   and the corresponding integrations.
3. Choose a stage or deploy the API to a new stage.
4. In the main navigation pane, choose **Stages**.
5. Choose the **Tags** tab. You might need to choose the right arrow button to show the tab.
6. Choose **Manage tags**.
7. In the **Tag Editor**, choose **Add tag**. Enter a tag key
   (for example, `Department`) in the **Key** field, and enter a tag value (for
   example, `Sales`) in the **Value** field. Choose **Save** to save the
   tag.
8. If needed, repeat step 5 to add more tags to the API stage. The maximum number of tags per stage
   is 50.
9. To remove an existing tag from the stage, choose **Remove**.
10. If the API has been deployed previously in the API Gateway console, you need to redeploy it for the
    changes to take effect.

## Set up tags for an API stage using the AWS CLI

You can set up tags for an API stage using the AWS CLI using the [create-stage](../../../cli/latest/reference/apigateway/create-stage.md "../../../cli/latest/reference/apigateway/create-stage.md") command or the [tag-resource](../../../cli/latest/reference/apigateway/tag-resource.md "../../../cli/latest/reference/apigateway/tag-resource.md") command. You can delete one or more tags from an API
stage using the [untag-resource](../../../cli/latest/reference/apigateway/untag-resource.md "../../../cli/latest/reference/apigateway/untag-resource.md") command.

The following [create-stage](../../../cli/latest/reference/apigateway/create-stage.md "../../../cli/latest/reference/apigateway/create-stage.md") command adds a tag when creating a `test` stage:

```
aws apigateway create-stage --rest-api-id `abc1234` --stage-name test --description 'Testing stage' --deployment-id `efg456` --tag Department=Sales
```

The following [tag-resource](../../../cli/latest/reference/apigateway/tag-resource.md "../../../cli/latest/reference/apigateway/tag-resource.md") command adds a tag to a `prod` stage:

```
aws apigateway tag-resource --resource-arn arn:aws:apigateway:`us-east-2`::/restapis/`abc123`/stages/prod --tags Department=Sales
```

The following [untag-resource](../../../cli/latest/reference/apigateway/untag-resource.md "../../../cli/latest/reference/apigateway/untag-resource.md") command removes the `Department=Sales` tag from the `test` stage:

```
aws apigateway untag-resource --resource-arn arn:aws:apigateway:`us-east-2`::/restapis/`abc123`/stages/test --tag-keys Department
```

## Set up tags for an API stage using the API Gateway REST API

You can set up tags for an API stage using the API Gateway REST API by doing one of the
following:

- Call [`tags:tag`](../api/API_TagResource.md "../api/API_TagResource.md") to tag an API stage.
- Call [`tags:untag`](../api/API_UntagResource.md "../api/API_UntagResource.md") to delete one or more tags from an API
  stage.
- Call [`stage:create`](../api/API_CreateStage.md "../api/API_CreateStage.md") to add one or more tags to an API
  stage that you're creating.

You can also call [`tags:get`](../api/API_GetTags.md "../api/API_GetTags.md") to describe tags in an API stage.

### Tag an API stage

After you deploy an API (`m5zr3vnks7`) to a stage (`test`),
tag the stage by calling [`tags:tag`](../api/API_TagResource.md "../api/API_TagResource.md"). The required stage Amazon Resource Name
(ARN) (`arn:aws:apigateway:us-east-1::/restapis/m5zr3vnks7/stages/test`)
must be URL encoded
(`arn%3Aaws%3Aapigateway%3Aus-east-1%3A%3A%2Frestapis%2Fm5zr3vnks7%2Fstages%2Ftest`).

```
PUT /tags/arn%3Aaws%3Aapigateway%3Aus-east-1%3A%3A%2Frestapis%2Fm5zr3vnks7%2Fstages%2Ftest

{
  "tags" : {
    "Department" : "Sales"
  }
}
```

You can also use the previous request to update an existing tag to a new value.

You can add tags to a stage when calling [`stage:create`](../api/API_CreateStage.md "../api/API_CreateStage.md")
to create the stage:

```
POST /restapis/<restapi_id>/stages

{
  "stageName" : "test",
  "deploymentId" : "adr134",
  "description" : "test deployment",
  "cacheClusterEnabled" : "true",
  "cacheClusterSize" : "500",
  "variables" : {
    "sv1" : "val1"
  },
  "documentationVersion" : "test",

  "tags" : {
    "Department" : "Sales",
    "Division" : "Retail"
  }
}
```

### Untag an API stage

To remove the `Department` tag from the stage, call [`tags:untag`](../api/API_UntagResource.md "../api/API_UntagResource.md"):

```
DELETE /tags/arn%3Aaws%3Aapigateway%3Aus-east-1%3A%3A%2Frestapis%2Fm5zr3vnks7%2Fstages%2Ftest?tagKeys=Department
Host: apigateway.us-east-1.amazonaws.com
Authorization: ...
```

To remove more than one tag, use a comma-separated list of tag keys in the query
expression—for example, `?tagKeys=Department,Division,…`.

### Describe tags for an API stage

To describe existing tags on a given stage, call [`tags:get`](../api/API_GetTags.md "../api/API_GetTags.md"):

```
GET /tags/arn%3Aaws%3Aapigateway%3Aus-east-1%3A%3A%2Frestapis%2Fm5zr3vnks7%2Fstages%2Ftags
Host: apigateway.us-east-1.amazonaws.com
Authorization: ...

```

The successful response is similar to the following:

```
200 OK

{
    "_links": {
        "curies": {
            "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-tags-{rel}.html",
            "name": "tags",
            "templated": true
        },
        "tags:tag": {
            "href": "/tags/arn%3Aaws%3Aapigateway%3Aus-east-1%3A%3A%2Frestapis%2Fm5zr3vnks7%2Fstages%2Ftags"
        },
        "tags:untag": {
            "href": "/tags/arn%3Aaws%3Aapigateway%3Aus-east-1%3A%3A%2Frestapis%2Fm5zr3vnks7%2Fstages%2Ftags{?tagKeys}",
            "templated": true
        }
    },
    "tags": {
        "Department": "Sales"
    }
}
```
