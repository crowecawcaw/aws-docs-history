

# Sending RCS carousels
<a name="rcs-carousels"></a>

A carousel message in AWS End User Messaging displays 2 to 10 rich cards in a horizontally scrollable strip. Recipients can scroll through cards and choose suggestions on individual cards to take action. With carousels, you can create conversational and interactive experiences such as product catalogs, service menus, plan comparisons, and location listings.

Carousels share the same card content model as standalone rich cards (see [Sending RCS rich cards](rcs-rich-cards.md)), but carousel cards always use a vertical layout and do not support the `TALL` media height.

**Important**  
You can send RCS carousel messages in all countries where RCS is supported.

## When to use a carousel
<a name="rcs-carousels-when"></a>

Use a carousel when you want recipients to browse and compare multiple items of the same type. Common use cases include:
+ **Product catalogs**: Show multiple items with images, descriptions, and purchase buttons.
+ **Service menus**: Present service tiers or options side by side for comparison.
+ **Plan comparisons**: Let recipients compare features across plans and select one.
+ **Location listings**: Display nearby stores or offices with addresses and map actions.

If you need to display a single item with rich content, use a standalone rich card instead. For details, see [Sending RCS rich cards](rcs-rich-cards.md).

## Carousel structure
<a name="rcs-carousels-structure"></a>

You define a carousel in the `Content.Carousel` object within the `RcsMessageContent` parameter of a `SendRcsMessage` request. The carousel object contains two required fields:

`CardWidth` (required)  
The display width of all cards in the carousel. All cards share the same width. Valid values: `SMALL` or `MEDIUM`.

`CardContents` (required)  
An array of 2 to 10 card objects. Each card can contain a title, description, media, and up to 4 suggestions.

### Card width values
<a name="rcs-carousels-card-width"></a>


**Carousel card widths**  

| Value | Width | Best for | 
| --- | --- | --- | 
| SMALL | 180 DP | Compact lists, thumbnails, quick-browse experiences | 
| MEDIUM | 296 DP | Detailed cards with longer descriptions and larger images | 

### Card content fields
<a name="rcs-carousels-card-content"></a>

Each card object in the `CardContents` array supports the following fields:

`Title`  
The card title. Maximum 200 characters.

`Description`  
The card description text. Maximum 2,000 characters.

`Media`  
An image or video to display on the card. Contains the following fields:  
+ `FileUrl` (required): The URL of the media file. Must match the pattern `^(https://|s3://).+$`. Maximum 2,000 characters. Maximum file size is 100 MB.
+ `ThumbnailUrl` (optional): A thumbnail image URL displayed while the full media loads.
+ `Height`: The display height of the media. Valid values for carousel cards: `SHORT` or `MEDIUM`. The `TALL` height is not supported in carousels.

`Suggestions`  
An array of up to 4 suggested replies or actions that display below the card content. For the full list of suggestion types, see [Configuring RCS suggestions](rcs-suggestions.md).

## Card suggestions and outer suggestions
<a name="rcs-carousels-suggestions"></a>

Carousel messages support two levels of suggestions:

Card-level suggestions  
Each card can include up to 4 suggestions. These appear directly below the card content and are specific to that card (for example, "Buy this item" or "View details").

Outer (message-level) suggestions  
The top-level `Suggestions` array (a sibling of `Content` in the `RcsMessageContent` structure) defines a chip list that appears below the entire carousel. You can include up to 11 outer suggestions per message.

Use outer suggestions for navigation actions that apply to the overall message, such as "Back to menu", "Help", or "Done browsing". Avoid duplicating card-level actions in the outer chip list.

## Card height and truncation
<a name="rcs-carousels-height-truncation"></a>

All cards in a carousel are scaled to match the height of the tallest card. If a card's content exceeds the maximum display height, the messaging client truncates content in the following order:

1. Description truncated to a single line.

1. Title truncated to a single line.

1. Suggestions removed.

1. Description removed.

1. Title removed (only media remains).

When truncation is applied, a "More" indicator appears so the recipient can expand the card to full-screen view.

## Media aspect ratios
<a name="rcs-carousels-aspect-ratios"></a>

The aspect ratio of card media depends on the combination of card width and media height.


**Medium width card aspect ratios**  

| Height | Aspect ratio | 
| --- | --- | 
| MEDIUM | 4:3 | 
| SHORT | 2:1 | 


**Small width card aspect ratios**  

| Height | Aspect ratio | 
| --- | --- | 
| MEDIUM | 4:5 | 
| SHORT | 5:4 | 

**Note**  
The `TALL` media height is not supported in carousel cards. For tall media, use a standalone rich card. See [Sending RCS rich cards](rcs-rich-cards.md).

## Carousel JSON structure
<a name="rcs-carousels-schema"></a>

The following JSON shows the structure of the `RcsMessageContent` parameter for a carousel message:

```
{
  "Content": {
    "Carousel": {
      "CardWidth": "SMALL | MEDIUM",
      "CardContents": [
        {
          "Title": "Card title (max 200 chars)",
          "Description": "Card description (max 2000 chars)",
          "Media": {
            "FileUrl": "https://example.com/image.jpg",
            "ThumbnailUrl": "https://example.com/thumb.jpg",
            "Height": "SHORT | MEDIUM"
          },
          "Suggestions": [
            {
              "Reply": {
                "Text": "Button label (max 25 chars)",
                "PostbackData": "callback_data"
              }
            }
          ]
        }
      ]
    }
  },
  "Suggestions": [
    {
      "Reply": {
        "Text": "Outer chip label",
        "PostbackData": "outer_callback"
      }
    }
  ]
}
```

This value is passed as a JSON string in the `--rcs-message-content` parameter (CLI) or the `RcsMessageContent` parameter (SDK). You also specify `--destination-phone-number` and `--origination-identity` (a pool or RCS agent) in the `send-rcs-message` request.

## Carousel limits
<a name="rcs-carousels-limits"></a>


**Carousel message limits**  

| Parameter | Minimum | Maximum | 
| --- | --- | --- | 
| Cards per carousel | 2 | 10 | 
| Suggestions per card | 0 | 4 | 
| Outer suggestions per message | 0 | 11 | 
| Title length | - | 200 characters | 
| Description length | - | 2,000 characters | 
| Media file size | - | 100 MB | 
| Total payload size | - | 250 KB | 

For media format and delivery details, see [Sending RCS file messages](rcs-file-messages.md).