# Capture website visitor activity with the web data tracker

The web data tracker captures how visitors interact with your website – items
clicked, searches made, form submission. It associates that activity
with their profile in Customer Profiles. The tracker is part of the Communications widget and is
controlled at the widget level. For an overview of how the web data tracker and web
notification work together, see [Web data tracker and web notification](customer-profiles-web-tracker-and-notification.md "customer-profiles-web-tracker-and-notification.md").

## Prerequisites

- An Connect Customer instance with the Communications widget configured. For more information,
  see [Add a chat user interface to your website hosted by Connect Customer](add-chat-to-website.md "add-chat-to-website.md").
- Customer Profiles enabled on the instance. For more information, see [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md "enable-customer-profiles.md").

## Step 1: Enable data collection on the Communications widget

1. Sign in to the Connect Customer admin website.
2. In the navigation menu, choose **Channels**, then choose
   **Communications widgets**.
3. Create a new widget or edit an existing one. For more information, see [Add a chat user interface to your website hosted by Connect Customer](add-chat-to-website.md "add-chat-to-website.md").
4. Enable **Data collection** to turn on clickstream
   tracking.
5. (Optional) The **Data collection** settings include an
   option for **Advanced Data Collection**. Turn this on so
   the service automatically gathers visitor interactions with HTML content,
   which produces richer and more accurate predictive insights.
6. (Optional) Enable **Web notification** if you plan to send
   proactive notifications from this widget. For more information, see [Send web notifications with Connect Customer outbound campaigns](outbound-campaigns-web-notification.md "outbound-campaigns-web-notification.md").
7. Add the website domains where the widget will be embedded to the allowed
   domains list.
8. Save the widget and copy the widget snippet code. Embed this snippet on
   your website in the next step.

## Step 2: Embed the widget and initialize tracking

Embed the widget snippet in your website's HTML. After the snippet loads, initialize
the tracker once you have obtained visitor consent.

```
// Start tracking visitor behavior (after obtaining consent)
await window.amazon_connect.Web.ClickStream.init();

// (Optional) Enable web notifications for this visitor
await window.amazon_connect.Web.Notification.init();
```

###### Important

Initialize tracking only after obtaining the appropriate visitor consent in
accordance with your privacy policy and applicable regulations.

###### Note

For single-page applications, embed the snippet once at the top-level page. For
multi-page applications, embed the snippet on every page where you want to capture
activity.

## Step 3: (Optional) Track business-specific events

To capture custom business events – such as purchase completions,
add-to-cart actions, or product views – call
`recordBusinessMetric` from your website JavaScript when the event
occurs.

###### Important

If you plan to use the data tracker with recommenders requiring Item Contexts
such as `Find Similar Items` and `Frequently Paired Items`,
you must use business-specific events and include the `item_id`
field.

### Method Signature

```
await amazon_connect.Web.ClickStream.recordBusinessMetric(eventType, eventPayload)
```

| **Parameter**  | **Type** | **Description**                                                    |
| -------------- | -------- | ------------------------------------------------------------------ |
| `eventType`    | string   | The business event name – a reserved type or any<br>custom string. |
| `eventPayload` | object   | Event data structured using the Object Schemas<br>below.           |

### Object Schemas

The `eventPayload` supports the following objects. Use any
combination of fields to fit your use case.

| **Object**       | **Key Fields**                                                                                                            | **Description**                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **item**         | `item_id`\*, `item_name`\*,<br>`quantity`\*, `category`,<br>`price`, `currency`,<br>`impression_type`,<br>`impression_id` | A single product or item                                   |
| **item\_list**   | List<item>                                                                                                                | Array of item objects (minimum 1)                          |
| **cart**         | `cart_id`\*, `item_list`\*,<br>`total_value`,<br>`currency`                                                               | Shopping cart                                              |
| **order**        | `order_id`\*, `item_list`\*,<br>`total_value`, `currency`,<br>`payment_method`,<br>`shipping_address`,<br>`discount`      | A completed order                                          |
| **search**       | `search_query`\*,<br>`total_matching_results`,<br>`results_per_page`,<br>`filter_expression`,<br>`sort_criteria`          | A search action                                            |
| **form**         | `form_id`\*, `form_name`,<br>`form_length`,<br>`validation_errors`,<br>`fields_completed`                                 | A form interaction                                         |
| **scroll**       | `depth_percentage`,<br>`position_x`,<br>`position_y`                                                                      | Scroll position (at least one field<br>required)           |
| **event\_value** | number                                                                                                                    | Numerical value representing the importance of an<br>event |

\* Required field

### Integration Steps and Usage Examples

After calling `amazon_connect.Web.ClickStream.init()`, add
`recordBusinessMetric()` calls in your website's event handlers
(for example, onclick).

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

The following event types are reserved with predefined schemas:

| **Event<br>Type** | **Required<br>Object** | **Description**                                     |
| ----------------- | ---------------------- | --------------------------------------------------- |
| `add_to_cart`     | item                   | Tracks when a visitor adds an item to their<br>cart |
| `purchase`        | order                  | Tracks a completed purchase                         |
| `view_items`      | item\_list             | Tracks when a visitor views one or more<br>items    |

### Custom Events

Beyond the reserved event types, you can define any custom event type string
(for example, `clear_cart` or `wishlist_add`). For custom
events:

- The service does not enforce strict validation on the event
  structure.
- You can use any combination of fields from the Object Schemas above
  to fit your use case.
- Use field names exactly as shown (for example, `cart_id`, not
  `cartId`).

```
await amazon_connect.Web.ClickStream.recordBusinessMetric('clear_cart', {
    cart_id: 'cart-123',
    item_list: [
        { item_id: 'p1', item_name: 'Widget', quantity: 1 }
    ]
});
```

## Associate clickstream with authenticated users

Clickstream data captured by the web data tracker is continuously streamed to Customer Profiles
and associated with the visitor's profile. The following table describes how that
association behaves for anonymous and authenticated visitors.

| **Visitor type**      | **Profile association<br>behavior**                                                                                                                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anonymous visitor     | Tracked by session identifier only. Behavioral data is<br>captured but not linked to a known customer identity. No<br>personally identifiable information is collected.                                                                                  |
| Authenticated visitor | When you pass an authenticated user ID during widget<br>initialization, the service links all clickstream activity to<br>that user's known profile in Customer Profiles. This enables richer<br>personalization and more accurate trigger<br>conditions. |

To associate tracking with an authenticated user, use one of the following
approaches:

- **(Recommended) Use the CustomerId JWT
  claim** – If you enabled security on your Communications widget,
  include the authenticated user ID in the `CustomerId` field of
  your JSON Web Token (JWT) claims. This links clickstream activity to the
  user's profile without exposing the ID in client-side code. For setup
  details, see [Step 3: Confirm and copy communications widget code and security keys](add-chat-to-website.md#confirm-and-copy-chat-widget-script "add-chat-to-website.md#confirm-and-copy-chat-widget-script").
- **Pass the user ID during initialization**
  – If security is not enabled on your widget, pass the authenticated
  user ID as an argument when initializing the tracker:

```
await window.amazon_connect.Web.ClickStream.init('<authenticated-user-id>');
```

###### Important

If an authenticated user ID is passed, it links to existing profiles via the
account key. Since data tracker events accumulate over time, set object limits
for `WebAnalytics-Clickstream` and `_webAnalytics` to
prevent new events from overwriting other object types once the profile object
limit is reached. For configuration guidance, see [Customer Profiles data limits](customer-profiles-data-limits.md "customer-profiles-data-limits.md").

## What is captured

For the full list of activities the tracker captures by default, see [What the web data tracker captures](customer-profiles-web-tracker-and-notification.md#web-tracker-what-is-captured "customer-profiles-web-tracker-and-notification.md#web-tracker-what-is-captured").

## Privacy and consent

The web data tracker is opt-in by design. If you do not enable **Data
collection** on the Communications widget, no clickstream data is captured. Form
field values, passwords, and payment information are never collected automatically,
even when form submission events are tracked.

###### Important

You are responsible for obtaining appropriate visitor consent before
initializing data tracking, in accordance with your privacy policy and applicable
regulations such as the General Data Protection Regulation (GDPR) and the
California Consumer Privacy Act (CCPA).
