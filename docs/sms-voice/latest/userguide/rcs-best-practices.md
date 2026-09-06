

# RCS best practices
<a name="rcs-best-practices"></a>

With RCS rich messaging, you can create conversational, interactive experiences that go beyond traditional SMS. This topic provides guidance for designing effective RCS messages, including suggestion strategy, rich card and carousel layout, media optimization, message expiration, fallback planning, and monitoring.

For details on individual features, see [Configuring RCS suggestions](rcs-suggestions.md), [Sending RCS rich cards](rcs-rich-cards.md), [Sending RCS carousels](rcs-carousels.md), [Configuring RCS message expiration](rcs-message-expiration.md), [Configuring per-message SMS or MMS fallback](rcs-fallback-per-message.md), and [RCS message events](rcs-events.md).

## Conversational and interactive design
<a name="rcs-best-practices-conversational-design"></a>

RCS messages support interactive elements such as suggested replies, suggested actions, rich cards, and carousels. To use these features effectively, treat each message exchange as part of an ongoing conversation rather than a one-way notification.

Open with context and options  
Include a clear greeting, state what the user can do, and provide suggested replies to guide the next step. This sets expectations and reduces friction.

Keep messages concise  
Aim for fewer than 300 characters per text message. Break complex information into multiple messages or use a rich card for structured content.

Avoid dead ends  
Every message should lead to a next step. Offer follow-up suggestions, a main menu option, or a path to a human agent.

Address the user directly  
Use second person. Write "Your appointment is confirmed" rather than "The appointment has been confirmed."

## Suggestion strategy
<a name="rcs-best-practices-suggestions"></a>

Suggestions (both replies and actions) appear as interactive chips below your message. They reduce typing, increase engagement, and let you route responses through structured `PostbackData` values. For the full list of suggestion types, see [Configuring RCS suggestions](rcs-suggestions.md).

### Write concise action labels
<a name="rcs-best-practices-suggestions-labels"></a>

The `Text` field has a 25-character limit. Use action-oriented language that tells the user exactly what happens on tap.


**Suggestion label examples**  

| Avoid | Prefer | 
| --- | --- | 
| "Option 1" | "Book for Monday" | 
| "Click here" | "View order status" | 
| "More info" | "See pricing details" | 

### Offer 3 to 5 options
<a name="rcs-best-practices-suggestions-count"></a>

Three suggestions is ideal for most interactions. You can include up to 11 suggestions per message (4 per rich card), but more than 5 options at a time tends to overwhelm users. If you need more choices, use a carousel or split the flow into multiple steps.

### Route on PostbackData
<a name="rcs-best-practices-suggestions-postback"></a>

Use `PostbackData` for backend routing logic instead of parsing the display text. This approach supports localization (you can change the user-visible `Text` without modifying your routing) and provides structured context for your application.

Encode the action, entity, and context in the postback value. For example:

```
confirm_order_12345
cancel_appointment_20260615
nav_main_menu
```

Use consistent prefixes (such as `book_`, `confirm_`, `cancel_`, `nav_`) to simplify routing in your backend.

**Important**  
Handle stale postbacks gracefully. A user might choose a suggestion hours after receiving it. Check that the referenced entity still exists and inform the user if the action is no longer valid.

## Rich card and carousel design
<a name="rcs-best-practices-rich-cards"></a>

Rich cards and carousels present structured content (images, titles, descriptions, and suggestions) in a visual format. For implementation details, see [Sending RCS rich cards](rcs-rich-cards.md) and [Sending RCS carousels](rcs-carousels.md).

### Standalone rich cards
<a name="rcs-best-practices-standalone-cards"></a>
+ Use `VERTICAL` orientation for the most consistent rendering across devices.
+ Use `TALL` media height to give images adequate display space on both Android and iOS.
+ Keep title and description text concise. Some clients crop text beyond three lines.
+ URLs in the description text do not work as links on all clients. Use an `OpenUrl` suggested action instead of embedding links in descriptions.
+ Include one clear call-to-action suggestion per card. Multiple competing actions reduce conversion rates.

### Carousels
<a name="rcs-best-practices-carousels"></a>
+ Place the recommended or most relevant option in the first card position. Users engage most with the first visible card.
+ Use outer (message-level) suggestions for navigation actions such as "Back to menu" or "Help." Reserve card-level suggestions for actions specific to that card.
+ Keep card content more concise than standalone cards because carousel cards have less vertical space.
+ Carousel card media height is limited to `SHORT` or `MEDIUM` (`TALL` is not supported in carousels).
+ Ensure the combined media across all cards stays under 100 MB. Optimize images before uploading.

## Media best practices
<a name="rcs-best-practices-media"></a>

Media files (images, videos, PDFs) enhance message engagement but add payload size and rendering variability. For file format and size requirements, see [Sending rich RCS messages](rcs-rich-messaging.md).
+ Compress images before uploading. Use JPEG for photographs and PNG for graphics with transparency.
+ Keep video files under 5 MB for reliable delivery across carriers and devices.
+ Provide a `ThumbnailUrl` for video and large-file messages. Thumbnails display while the full media loads and improve the user experience on slow connections.
+ GIF animations play on Android but display as a static first frame on iOS. Do not rely on GIF animation to convey critical information.
+ Host media on HTTPS URLs or in Amazon S3 (using `s3://` URIs). All media URLs must match the pattern `^(https://|s3://).+$`.

## TTL and fallback strategy
<a name="rcs-best-practices-ttl-fallback"></a>

Time to live (TTL) and fallback configuration work together to ensure your message reaches the user even when RCS delivery fails. For implementation details, see [Configuring RCS message expiration](rcs-message-expiration.md) and [Configuring per-message SMS or MMS fallback](rcs-fallback-per-message.md).

### Setting TTL values
<a name="rcs-best-practices-ttl"></a>

Always set a `TimeToLive` value for time-sensitive content. Match the TTL to the content relevance window.


**Recommended TTL values by content type**  

| Content type | Recommended TTL | 
| --- | --- | 
| One-time password (OTP) or verification code | 30 to 120 seconds | 
| Flash sale notification | Duration until sale ends | 
| Appointment reminder | Time until appointment | 
| Delivery update | 1 to 4 hours | 

**Note**  
The API minimum is 1 second, but a TTL of at least 10 seconds is recommended to allow sufficient delivery time. The maximum is 172,800 seconds (48 hours).

### SMS or MMS fallback
<a name="rcs-best-practices-fallback"></a>

Configure a `FallbackConfiguration` for critical messages (OTPs, order confirmations, security alerts) so the content reaches the user if RCS delivery fails or expires.
+ Set the `Channel` field to `SMS` or `MMS` depending on whether you need media in the fallback.
+ Keep the `MessageBody` within 1,600 characters (the fallback limit, which is shorter than the 3,072-character RCS text limit).
+ Test fallback delivery end-to-end by sending to a phone number that does not support RCS and verifying that the SMS or MMS message arrives.

## Monitoring and events
<a name="rcs-best-practices-monitoring"></a>

Use event destinations and delivery events to monitor message performance and optimize your messaging strategy. For details on event types and configuration, see [RCS message events](rcs-events.md).
+ Configure event destinations before you begin production sending. This ensures you capture delivery, read, and expiration events from the start.
+ Monitor message expiration rates to determine whether your TTL values are appropriate. A high expiration rate suggests the TTL is too short or that many recipients do not have RCS-capable devices.
+ Track read receipts for relative comparison (A/B testing) rather than as an absolute metric. Not all clients report read status.
+ Use delivery confirmation events to cancel redundant fallback timers in your application logic if you manage fallback externally.

## Device and client rendering variance
<a name="rcs-best-practices-device-variance"></a>

RCS messages render differently across Android and iOS clients. Design for the lowest common denominator and test on both platforms before launching a campaign.


**Rendering differences between Android and iOS**  

| Feature | Android | iOS | 
| --- | --- | --- | 
| GIF images | Animated | Static (first frame only) | 
| Link previews in text | URL anywhere in message | URL must be the last element. A URL followed by additional text may not be clickable. | 
| Card media heights | Respects SHORT, MEDIUM, and TALL | Renders all vertical heights identically. Might ignore the height property. | 
| Suggestion chip order | Preserved as sent | Might reorder chips | 
| Suggested action persistence | Actions outside cards disappear after tap. Card buttons persist. | All buttons (card and non-card) persist after tap. | 
| Display name with path characters (/, \\, :) | Rendered as registered | Characters may be stripped by the iOS rendering layer | 
| Agent banner image | Visible on agent profile | Not displayed | 
| Privacy policy link | Visible on agent profile | Not displayed | 
| Multiple contacts per type | All contact entries visible | Only first contact per type visible (by list order) | 
| Media with large accessibility text sizes | Stable rendering | May crop images when large text sizes are enabled | 
| Carrier verification badge | "Verified by [Carrier]" or "Verified by Google" | Same badge values. Rendering controlled by Apple. | 

Design recommendations based on these differences:
+ Use `VERTICAL` card orientation for consistent layout.
+ Place URLs at the end of text messages to ensure link previews render on iOS.
+ Do not depend on GIF animation to communicate essential information.
+ Test suggestion ordering on both platforms if the sequence is meaningful to the user flow.

### Display name rendering on iOS
<a name="rcs-best-practices-display-name-ios"></a>

Apple's iOS Messages app may strip characters that resemble operating system path separators (`/`, `\`, `:`) or URL escape sequences from the displayed agent name. This behavior is controlled at the OS level and cannot be overridden by AWS, Google, carriers, or messaging partners.

To avoid display name mismatches:
+ Use only alphanumeric characters, spaces, hyphens, periods, and standard punctuation (such as `&`, `'`, `!`) in your display name.
+ Do not use forward slashes, backslashes, or colons as part of your brand name.
+ If your brand name includes these characters, consider an alternative representation (for example, use a hyphen or space instead of a slash).
+ Always verify your agent's appearance on an iOS test device during the testing phase before requesting carrier launch. This is one of the primary purposes of testing agents.

If you have already launched an agent with an affected display name and need to change it, contact AWS Support. Display name changes on launched agents require carrier re-approval.

### Agent profile visibility on iOS
<a name="rcs-best-practices-agent-profile-ios"></a>

Some agent profile elements that are visible on Android are not displayed on iOS:
+ **Banner image**: Not shown on iOS. Do not rely on the banner to communicate critical brand information.
+ **Privacy policy link**: Not visible in the iOS agent profile view. Ensure your privacy policy is accessible through other means (such as your website or a suggested action in your welcome message).
+ **Multiple contacts**: If you configure multiple phone numbers, emails, or websites, iOS shows only the first entry per contact type. Place your primary contact first in the list when configuring your agent.

### Testing across platforms
<a name="rcs-best-practices-testing-platforms"></a>

RCS rendering depends on the recipient's operating system version, device model, and carrier configuration. Before requesting carrier launch:
+ Send test messages to both Android and iOS devices.
+ Verify display name, logo, banner, description, suggested actions, rich cards, and media on both platforms.
+ Test with different text sizes and accessibility settings on iOS.
+ Confirm link previews render correctly on both platforms.

Apple's RCS implementation is still evolving. Behaviors may change with iOS updates. Monitor your messaging experience after iOS releases and adjust your content accordingly.

## Opt-out handling
<a name="rcs-best-practices-opt-out"></a>

Respect user opt-out preferences immediately and consistently across all messaging channels.
+ Honor STOP and UNSUBSCRIBE keywords by ceasing all non-essential messages immediately after the opt-out request.
+ Send a brief opt-out confirmation that includes your brand name so the user knows which sender they unsubscribed from.
+ Maintain your own opt-out database and synchronize it across channels (RCS, SMS, MMS) to prevent sending on one channel after the user opted out on another.
+ Consult your legal team regarding which message types (such as OTPs or fraud alerts) might still be sent after an opt-out.

**Note**  
AWS End User Messaging provides opt-out list management for SMS and MMS. For RCS, coordinate your opt-out handling with both the AWS End User Messaging opt-out lists and your own application-level records.