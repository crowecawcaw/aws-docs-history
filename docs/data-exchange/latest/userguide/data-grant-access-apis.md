# Access an AWS Data Exchange data set containing APIs

The following topics describe the process of accessing a data set containing APIs on AWS Data Exchange
using the AWS Data Exchange console.

## Viewing an API

To view an API

1. Open your web browser and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **My data**, choose
   **Entitled data sets**.
3. Choose a data set.
4. Under the **Revisions** tab, choose a revision.
5. Under **API assets**, choose the API.
6. View the **Asset overview**.
7. Follow the guidance in the **Integration notes** to call the API.

## Downloading the API specification

To download the API specification

1. Open your web browser and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **My data**, choose
   **Entitled data sets**.
3. Choose a data set.
4. Under the **Revisions** tab, choose a revision.
5. Under **API assets**, choose the API.
6. On the **OpenAPI 3.0** specification, choose **Download API
   specification**.

The specification is downloaded onto your local computer. You can then export the asset to
a third- party tool for SDK generation.

## Making an API call (console)

You can call a single endpoint in the AWS Data Exchange console.

To make an API call from the console

1. Open your web browser and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **My data**, choose
   **Entitled data sets**.
3. Choose a data set.
4. Under the **Revisions** tab, choose a revision.
5. Under **API assets**, choose the API.
6. For **Integration notes**:
   1. Choose **Copy** to use the **Base URL**.
   2. Choose **Copy** to use the **Code structure**.
   3. Follow the information provided in the specification documentation to call the
      API.

## Making an API call (AWS CLI)

To make an API call (AWS CLI)

- Use the `send-api-asset` command to call the API.

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
