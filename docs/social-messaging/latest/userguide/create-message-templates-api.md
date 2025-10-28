# Creating message templates with the CreateWhatsAppMessageTemplate API

You can create customized WhatsApp message templates using the API. This topic describes how to use the
[CreateWhatsAppMessageTemplate](../APIReference/API_CreateWhatsAppMessageTemplate.md "../APIReference/API_CreateWhatsAppMessageTemplate.md")
to create a variety of message templates.

## Message template components

message templates can include the following components:

- **Header**: Title text that appears at the top
- **Body**: Main message content with variable placeholders
- **Footer**: Additional information at the bottom
- **Buttons**: Clickable elements that link to URLs

In the following examples Replace `ENDPOINT` and `WABA_ID` with your actual
endpoint URL and ID.

## Create a basic English utility template

This example creates a utility message template in English that uses only the `BODY` component, and doesn't include `HEADER`, `FOOTER`, or `BUTTON` components.
The body text uses variable placeholders.

```
`$` `aws socialmessaging create-whatsapp-message-template --region `us-east-1` --endpoint-url `ENDPOINT_URL` \
--id `WABA_ID` \
--template-definition '{
 "name": "order_update_basic",
 "language": "en_US",
 "allow_category_change": true,
 "category": "UTILITY",
 "components": [
 {
 "type": "BODY",
 "text": "Hi {{1}}, your order #{{2}} has been shipped. Track your delivery below."
 }
 ]
}'`
```

## Create a basic English utility template with button

This example creates a utility message template in English that includes `BODY` and `BUTTON` components.

```
`$` `aws socialmessaging create-whatsapp-message-template --region `us-east-1` --endpoint-url `ENDPOINT_URL` \
--id `WABA_ID` \
--template-definition '{
 "name": "order_update_with_button",
 "language": "en_US",
 "allow_category_change": true,
 "category": "UTILITY",
 "components": [
 {
 "type": "BODY",
 "text": "Hi {{1}}, your order #{{2}} has been shipped. Track your delivery below."
 },
 {
 "type": "BUTTONS",
 "buttons": [
 {
 "type": "URL",
 "text": "Track Order",
 "url": "https://example.com/track"
 }
 ]
 }
 ]
}'`
```

## Create a complex English utility message template with a header, body, and button

This example creates a utility message template in English that includes `HEADER`,`BODY`, and `BUTTON` components.

```
`$` `aws socialmessaging create-whatsapp-message-template --region `us-east-1` --endpoint-url `ENDPOINT_URL` \
--id `WABA_ID` \
--template-definition '{
 "name": "account_creation_confirmation_3333",
 "category": "UTILITY",
 "language": "en_US",
 "status": "APPROVED",
 "components": [
 {
 "type": "HEADER",
 "format": "TEXT",
 "text": "Finalize account set-up"
 },
 {
 "type": "BODY",
 "text": "Hi {{1}},\n\nYour new account has been created successfully. \n\nPlease verify {{2}} to complete your profile.",
 "example": {
 "body_text": [
 [
 "John",
 "your email address"
 ]
 ]
 }
 },
 {
 "type": "BUTTONS",
 "buttons": [
 {
 "type": "URL",
 "text": "Verify account",
 "url": "https://www.example.com/"
 }
 ]
 }
 ]
}'`
```

## Create a basic marketing message template

This example creates a basic marketing message template that includes only a `BODY` component.

```
`$` `aws socialmessaging create-whatsapp-message-template --region us-east-1 --endpoint-url `ENDPOINT_URL` \
--id `WABA_ID` \
--template-definition '{
 "id": "1290345849293233",
 "name": "holiday_special_1395238",
 "category": "MARKETING",
 "language": "en_US",
 "status": "PENDING",
 "components": [
 {
 "type": "BODY",
 "text": "Season's Greetings {{1}}!\n\nCelebrate {{2}} with amazing deals up to {{3}} off.\n\nPlus, get free gift wrapping on all orders above $50.",
 "example": {
 "body_text": [
 [
 "Pawan",
 "Christmas",
 "30%"
 ]
 ]
 }
 }
 ],
 "metaTemplateId": "1290345849293233"
}'`
```

## Create a complex marketing message template

This example creates a marketing message template in English that includes `HEADER`,`BODY`, and `BUTTON` components.

```
`$` `aws socialmessaging create-whatsapp-message-template --region us-east-1 \
--endpoint-url `ENDPOINT_URL` \
--id `WABA_ID` \
--template-definition '{
 "name": "summer_sale_1",
 "category": "MARKETING",
 "language": "en_US",
 "status": "APPROVED",
 "components": [
 {
 "type": "HEADER",
 "format": "TEXT",
 "text": "Summer Sale!"
 },
 {
 "type": "BODY",
 "text": "Hi {{1}}! Get {{2}} off all summer items. Shop now before stock runs out!"
 },
 {
 "type": "FOOTER",
 "text": "Valid until August 31st"
 },
 {
 "type": "BUTTONS",
 "buttons": [
 {
 "type": "URL",
 "text": "Shop Now",
 "url": "https://example.com/sale"
 }
 ]
 }
 ]
}'`
```
