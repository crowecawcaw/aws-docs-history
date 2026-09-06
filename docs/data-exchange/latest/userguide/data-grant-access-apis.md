

# Access an AWS Data Exchange data set containing APIs
<a name="data-grant-access-apis"></a>

The following topics describe the process of accessing a data set containing APIs on AWS Data Exchange using the AWS Data Exchange console.

## Viewing an API
<a name="data-grant-access-apis-view-api"></a>

To view an API

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, under **My data**, choose **Entitled data sets**.

1. Choose a data set.

1. Under the **Revisions** tab, choose a revision.

1. Under **API assets**, choose the API.

1. View the **Asset overview**.

1. Follow the guidance in the **Integration notes** to call the API.

## Downloading the API specification
<a name="data-grant-access-apis-downloading-api"></a>

To download the API specification

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, under **My data**, choose **Entitled data sets**.

1. Choose a data set.

1. Under the **Revisions** tab, choose a revision.

1. Under **API assets**, choose the API.

1. On the **OpenAPI 3.0** specification, choose **Download API specification**.

   The specification is downloaded onto your local computer. You can then export the asset to a third- party tool for SDK generation.

## Making an API call (console)
<a name="data-grant-access-apis-making-api-call-console"></a>

You can call a single endpoint in the AWS Data Exchange console.

To make an API call from the console

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, under **My data**, choose **Entitled data sets**.

1. Choose a data set.

1. Under the **Revisions** tab, choose a revision.

1. Under **API assets**, choose the API.

1. For **Integration notes**:

   1. Choose **Copy** to use the **Base URL**.

   1. Choose **Copy** to use the **Code structure**.

   1. Follow the information provided in the specification documentation to call the API.

## Making an API call (AWS CLI)
<a name="data-grant-access-apis-making-api-call-cli"></a>

To make an API call (AWS CLI)
+ Use the `send-api-asset` command to call the API.

  ```
  $ AWS dataexchange send-api-asset \
  --asset-id $ASSET_ID \
  --data-set-id $DATA_SET_ID \
  --revision-id $REVISION_ID \
  --body "..." \
  {
  "headers": {
  ...
  },
  "body": "..."
  }
  ```