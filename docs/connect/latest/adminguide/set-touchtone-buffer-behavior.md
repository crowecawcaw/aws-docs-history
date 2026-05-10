# Flow block in Connect Customer: Set Touchtone Buffer Behavior

## Description

Use this block to enable or disable touchtone buffering for a contact. When touchtone
buffering is enabled, customer keypad inputs (digits 0–9, #, and \*) are collected
into a buffer of up to 30 characters as the customer presses them, even while
prompts are still playing or between flow block transitions. This eliminates the
common IVR problem of dropped digits when customers type ahead of prompts.

The block has two modes:

- **Enable Buffering** — Starts collecting
  DTMF input into the buffer. Buffered digits are consumed by the next
  [Get customer input](get-customer-input.md "get-customer-input.md") or [Store customer input](store-customer-input.md "store-customer-input.md") block in the
  flow.
- **Stop and Clear** — Stops buffering and
  clears any digits in the buffer. Optionally stores the buffered input
  before clearing, with support for encryption.

## Use cases for this block

- Allow customers to navigate multi-level IVR menus without waiting for
  each prompt to finish (type-ahead).
- Capture account numbers, order IDs, or other numeric input that
  customers begin entering before the collection prompt plays.

## Supported channels

The following table lists how this block routes a contact who is using the
specified channel.

| Channel | Supported?        |
| ------- | ----------------- |
| Voice   | Yes               |
| Chat    | No — Error branch |
| Task    | No — Error branch |
| Email   | No — Error branch |

## Flow types

You can use this block in the following [flow
types](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types"):

- Inbound flow
- Customer queue flow
- Outbound whisper flow
- Transfer to agent flow
- Transfer to queue flow

## How to configure this block

You can configure the **Set Touchtone Buffer Behavior** block by
using the Connect Customer admin website, or by using the [GetParticipantInput](../APIReference/participant-actions-getparticipantinput.md "../APIReference/participant-actions-getparticipantinput.md") action in the Connect Customer flow language.

### Enable Buffering

1. In the flow designer, add the **Set Touchtone Buffer
   Behavior** block.
2. Under **Touchtone Buffer Behavior**, select
   **Enable**.
3. The buffer begins collecting customer DTMF input immediately.
   Digits remain in the buffer until they are consumed by a [Get customer input](get-customer-input.md "get-customer-input.md") or [Store customer input](store-customer-input.md "store-customer-input.md") block, or until the
   buffer is explicitly stopped and cleared.

### Stop and Clear

1. Under **Touchtone Buffer Behavior**, select
   **Stop and Clear**.
2. Optionally enable **Store input** to save the
   current buffer contents to a contact attribute before
   clearing.
3. If storing input, optionally enable **Encrypt
   input** and provide an encryption key to encrypt the stored
   value.

## Configured block

The following image shows an example of what this block looks like when it is
configured. It has the following branches:
**Success** and **Error**.

1. **Success**: The buffer behavior was set
   successfully.
2. **Error**: An error occurred, for example, the block
   was reached by a non-voice contact.

## How the buffer interacts with other blocks

- [Play prompt](play.md "play.md"): Includes a
  **Skip or interrupt this prompt when touchtone buffering is
  enabled** checkbox. When selected, if the buffer already
  contains digits, the prompt is skipped entirely. If the customer presses
  a key during the prompt, the prompt is interrupted and the digit is added
  to the buffer.
- [Get customer input](get-customer-input.md "get-customer-input.md"): If the buffer contains a
  digit, the block automatically dequeues and uses it. No configuration
  changes needed. If the buffer is empty, the customer is prompted for
  input as usual. In Amazon Lex mode, the buffer is automatically cleared
  before bot interaction begins. Buffered digits are not used, and buffer
  contents are not passed to the Amazon Lex bot.
- [Store customer input](store-customer-input.md "store-customer-input.md"): The block dequeues up to
  the maximum number of digits specified in the block configuration. If the
  buffer contains equal to or more digits than the maximum, the prompt is
  skipped and the call proceeds immediately. If the buffer has fewer digits
  than requested, the inter-digit timeout is applied to allow the caller to
  enter the remaining digits in real-time.

## Automatic clearing

The buffer is automatically cleared in the following situations:

- Buffered digits are consumed in first-in, first-out order each time a
  [Get customer input](get-customer-input.md "get-customer-input.md") or [Store customer input](store-customer-input.md "store-customer-input.md") block processes
  them.
- A **Stop and Clear** action is executed.
- When transferring to an agent or queue.
- When using [Get customer input](get-customer-input.md "get-customer-input.md") with Amazon Lex bots.
- The contact ends.

## Error scenarios

A contact is routed down the **Error** branch in the following
situations:

- The block is reached by a non-voice contact (chat, task, or
  email).
- Invalid input encryption parameters when using Stop and Clear with
  Store input enabled.

## Flow language

The **Set Touchtone Buffer Behavior** block is represented as a
`GetParticipantInput` action in the Connect Customer flow language, using the
`EnableDTMFBuffer` parameter.

**Enable buffering:**

```
{
    "Parameters": {
        "EnableDTMFBuffer": "true"
    },
    "Identifier": "unique-identifier",
    "Type": "GetParticipantInput",
    "Transitions": {
        "NextAction": "next-action-id",
        "Errors": [
            {
                "NextAction": "error-action-id",
                "ErrorType": "NoMatchingError"
            }
        ]
    }
}
```

**Stop and clear with stored encrypted
input:**

```
{
    "Parameters": {
        "EnableDTMFBuffer": "false",
        "StoreInput": "true",
        "InputEncryption": {
            "EncryptionKeyId": "your-key-id",
            "Key": "your-encryption-key"
        }
    },
    "Identifier": "unique-identifier",
    "Type": "GetParticipantInput",
    "Transitions": {
        "NextAction": "next-action-id",
        "Errors": [
            {
                "NextAction": "error-action-id",
                "ErrorType": "NoMatchingError"
            }
        ]
    }
}
```

## More resources

See [Touchtone buffering](touchtone-buffering.md "touchtone-buffering.md") for detailed information about
touchtone buffering use cases, best practices, and flow design
guidance.
