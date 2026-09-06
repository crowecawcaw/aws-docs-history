

# Capture website visitor activity with the web data tracker
<a name="chat-widget-data-tracker"></a>

The web data tracker captures how visitors interact with your website – items clicked, searches made, form submission. It associates that activity with their profile in Customer Profiles. The tracker is part of the Communications widget and is controlled at the widget level. For an overview of how the web data tracker and web notification work together, see [Web data tracker and web notification](customer-profiles-web-tracker-and-notification.md).

## Prerequisites
<a name="chat-widget-data-tracker-prereqs"></a>
+ An Connect Customer instance with the Communications widget configured. For more information, see [Add a chat user interface to your website hosted by Connect Customer](add-chat-to-website.md).
+ Customer Profiles enabled on the instance. For more information, see [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md).

## Step 1: Enable data collection on the Communications widget
<a name="chat-widget-enable-data-collection"></a>

1. Sign in to the Connect Customer admin website.

1. In the navigation menu, choose **Channels**, then choose **Communications widgets**.

1. Create a new widget or edit an existing one. For more information, see [Add a chat user interface to your website hosted by Connect Customer](add-chat-to-website.md).

1. Enable **Data collection** to turn on clickstream tracking.

1. (Optional) The **Data collection** settings include an option for **Advanced Data Collection**. Turn this on so the service automatically gathers visitor interactions with HTML content, which produces richer and more accurate predictive insights.

1. (Optional) Enable **Web notification** if you plan to send proactive notifications from this widget. For more information, see [Send web notifications with Connect Customer outbound campaigns](outbound-campaigns-web-notification.md).

1. Add the website domains where the widget will be embedded to the allowed domains list.

1. Save the widget and copy the widget snippet code. Embed this snippet on your website in the next step.

## Step 2: Embed the widget and initialize tracking
<a name="chat-widget-embed-and-init-tracking"></a>

Embed the widget snippet in your website's HTML. After the snippet loads, initialize the tracker after you have obtained visitor consent.

```
// Start tracking visitor behavior (after obtaining consent)
await window.amazon_connect.Web.ClickStream.init();

// (Optional) Enable web notifications for this visitor
await window.amazon_connect.Web.Notification.init();
```

**Important**  
Initialize tracking only after obtaining the appropriate visitor consent in accordance with your privacy policy and applicable regulations.

**Note**  
For single-page applications, embed the snippet once at the top-level page. For multi-page applications, embed the snippet on every page where you want to capture activity.

## Step 3: (Optional) Track business-specific events
<a name="chat-widget-track-business-events"></a>

To capture custom business events – such as purchase completions, add-to-cart actions, or product views – call `recordBusinessMetric` from your website JavaScript when the event occurs.

**Important**  
If you plan to use the data tracker with recommenders requiring Item Contexts such as `Find Similar Items` and `Frequently Paired Items`, you must use business-specific events and include the `item_id` field.

### Method Signature
<a name="chat-widget-track-business-events-method"></a>

```
await amazon_connect.Web.ClickStream.recordBusinessMetric(eventType, eventPayload)
```


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| `eventType` | string | The business event name – a reserved type or any custom string. | 
| `eventPayload` | object | Event data structured using the Object Schemas below. | 

### Object Schemas
<a name="chat-widget-track-business-events-schemas"></a>

The `eventPayload` supports the following objects. Use any combination of fields to fit your use case.


| **Object** | **Key Fields** | **Description** | 
| --- | --- | --- | 
| **item** | `item_id`\*, `item_name`\*, `quantity`\*, `category`, `price`, `currency`, `impression_type`, `impression_id` | A single product or item | 
| **item\_list** | List<item> | Array of item objects (minimum 1) | 
| **cart** | `cart_id`\*, `item_list`\*, `total_value`, `currency` | Shopping cart | 
| **order** | `order_id`\*, `item_list`\*, `total_value`, `currency`, `payment_method`, `shipping_address`, `discount` | A completed order | 
| **search** | `search_query`\*, `total_matching_results`, `results_per_page`, `filter_expression`, `sort_criteria` | A search action | 
| **form** | `form_id`\*, `form_name`, `form_length`, `validation_errors`, `fields_completed` | A form interaction | 
| **scroll** | `depth_percentage`, `position_x`, `position_y` | Scroll position (at least one field required) | 
| **event\_value** | number | Numerical value representing the importance of an event | 

\* Required field

### Integration Steps and Usage Examples
<a name="chat-widget-track-business-events-examples"></a>

After calling `amazon_connect.Web.ClickStream.init()`, add `recordBusinessMetric()` calls in your website's event handlers (for example, onclick).

**Example – Add to Cart**

```
await amazon_connect.Web.ClickStream.recordBusinessMetric('add_to_cart', {
    item: {
        item_id: 'prod-123',
        item_name: 'Wireless Headphones',
        price: 49.99,
        quantity: 1,
        currency: 'USD'
    }
});
```

**Example – View Items**

```
await amazon_connect.Web.ClickStream.recordBusinessMetric('view_items', {
    item_list: [
        {
            item_id: 'item_10',
            quantity: 1,
            item_name: 'Premium Wireless Headphones',
            category: 'Electronics',
            price: 89.99,
            currency: 'USD'
        }
    ]
});
```

### Reserved Event Types
<a name="chat-widget-track-business-events-reserved"></a>

The following event types are reserved with predefined schemas:


| **Event Type** | **Required Object** | **Description** | 
| --- | --- | --- | 
| `add_to_cart` | item | Tracks when a visitor adds an item to their cart | 
| `purchase` | order | Tracks a completed purchase | 
| `view_items` | item\_list | Tracks when a visitor views one or more items | 

### Custom Events
<a name="chat-widget-track-business-events-custom"></a>

Beyond the reserved event types, you can define any custom event type string (for example, `clear_cart` or `wishlist_add`). For custom events:
+ The service does not enforce strict validation on the event structure.
+ You can use any combination of fields from the Object Schemas above to fit your use case.
+ Use field names exactly as shown (for example, `cart_id`, not `cartId`).

```
await amazon_connect.Web.ClickStream.recordBusinessMetric('clear_cart', {
    cart_id: 'cart-123',
    item_list: [
        { item_id: 'p1', item_name: 'Widget', quantity: 1 }
    ]
});
```

## Associate clickstream with Customer Profile
<a name="chat-widget-data-tracker-authenticated-users"></a>

Clickstream data captured by the web data tracker is continuously streamed to Customer Profiles. How data is associated with a profile depends on whether profile keys are provided during widget initialization.


| **Visitor type** | **Profile association behavior** | 
| --- | --- | 
| Visitor without profile keys (anonymous) | Tracked by an anonymous identifier stored in a browser cookie that expires after 7 days. During this period, clickstream data from the same visitor is linked to a single anonymous profile. After the cookie expires, a new anonymous identifier is generated and subsequent activity is tracked under a new profile. No personally identifiable information is collected.<br />If profile keys are provided during widget initialization, clickstream data is linked to the corresponding known profile instead of the anonymous profile. | 
| Visitor with profile keys | When you pass profile keys during widget initialization, the service links all clickstream activity to that user's known profile in Customer Profiles. This enables richer personalization and more accurate trigger conditions. | 

### Link web analytics events with existing profiles
<a name="chat-widget-data-tracker-auth-profile-keys"></a>

To associate tracking with a known profile, set `profileKeys` in your JWT claims to search for and associate with an existing profile at connection time, and the service uses these keys to find a matching profile through the `SearchProfiles` API. This requires security to be enabled on your Communications widget. For setup details, see [Step 3: Confirm and copy communications widget code and security keys](add-chat-to-website.md#confirm-and-copy-chat-widget-script).

```
{
  "sub": "<widgetId>",
  "iat": 1234567890,
  "exp": 1234571490,
  "profileKeys": {
    "_email": "user@example.com",
    "_account": "ACCT-12345"
  },
  "profileKeysOperator": "OR"
}
```
+ `profileKeys` – A key-value object where each key is a searchable Customer Profiles identifier (for example, `_email`, `_phone`, `_account`) and the value is the lookup value.
+ `profileKeysOperator` (optional) – `"AND"` or `"OR"` (default: `"OR"`). Determines whether the profile must match all keys or any key.
+ If exactly one profile is found, it is associated with the session.
+ If no profile is found, the session proceeds anonymously (a new profile can be created later).
+ If multiple profiles are found, `window.amazon_connect.Web.ClickStream.init()` returns an error. Revise your key selection to ensure uniqueness.

**Set object count limits to prevent eviction issues**  
If linking with an existing profile, we recommend setting `MaxProfileObjectCount` on `WebAnalytics-Clickstream` and `_webAnalytics` object types. These data tracker event objects accumulate over time. Without this setting, the service does not consider them for eviction when a profile reaches its object limit. For more information about data limits, see [Customer Profiles data limits](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles-data-limits.html).

### Grouping events by a custom identifier
<a name="chat-widget-data-tracker-auth-custom-id"></a>

If you don't need to link to an existing profile but want to group clickstream activity on your own, you can provide a custom identifier. Clickstream events sharing the same identifier are grouped under a common `_webAnalyticsUserId` profile key.

There are two ways to provide it:
+ **Via JWT claims** – Set the `customerId` field in your JWT claims (requires security enabled).
+ **Via initialization** – Pass the identifier as an argument when initializing the tracker:

  ```
  // Pass the custom user id as a positional string argument.
  await window.amazon_connect.Web.ClickStream.init('<custom-user-id>');
  ```

**Note**  
If `profileKeys` are also provided and resolve to an existing profile, profile resolution uses that result and skips this custom identifier.

## What is captured
<a name="chat-widget-data-tracker-what-is-captured"></a>

For the full list of activities the tracker captures by default, see [What the web data tracker captures](customer-profiles-web-tracker-and-notification.md#web-tracker-what-is-captured).

## Privacy and consent
<a name="chat-widget-data-tracker-privacy"></a>

The web data tracker is opt-in by design. If you do not enable **Data collection** on the Communications widget, no clickstream data is captured. Form field values, passwords, and payment information are never collected automatically, even when form submission events are tracked.

**Important**  
You are responsible for obtaining appropriate visitor consent before initializing data tracking, in accordance with your privacy policy and applicable regulations such as the General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA).