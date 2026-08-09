# Touchtone buffering in Connect Customer

Touchtone buffering in Connect Customer eliminates a common frustration in IVR systems by allowing
customers to enter their complete menu path immediately (such as pressing 1-2-3 in rapid
succession) or input identification numbers (such as account IDs or order numbers) without
waiting for each prompt to finish or losing their inputs. This "type-ahead" capability
reduces call handling time and improves self-service containment.

When customers interact with your IVR, they press keypad digits in response to prompts.
Traditional systems lose these inputs if entered too early or in quick succession. Touchtone
buffering solves this by collecting and storing up to 30 digits in a temporary queue until
your system is ready to process them.

###### Contents

- [Supported channels](#touchtone-buffering-supported-channels "#touchtone-buffering-supported-channels")
- [Supported blocks](#touchtone-buffering-supported-blocks "#touchtone-buffering-supported-blocks")
- [Configure touchtone
  buffering](#touchtone-buffering-configure "#touchtone-buffering-configure")
- [The buffer lifecycle](#touchtone-buffering-lifecycle "#touchtone-buffering-lifecycle")
- [Block capabilities](#touchtone-buffering-block-capabilities "#touchtone-buffering-block-capabilities")
- [Flow logging changes](#touchtone-buffering-flow-logging "#touchtone-buffering-flow-logging")
- [Common use cases](#touchtone-buffering-use-cases "#touchtone-buffering-use-cases")
- [Implementation best practices](#touchtone-buffering-best-practices "#touchtone-buffering-best-practices")

## Supported channels

Touchtone buffering is supported on the following channels:

| Channel | Supported?           |
| ------- | -------------------- |
| Voice   | Yes                  |
| Chat    | No<br>• Error branch |
| Task    | No<br>• Error branch |
| Email   | No<br>• Error branch |

## Supported blocks

The following flow blocks support touchtone buffering:

| Block                                                                                                   | Description                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Set Touchtone Buffer<br>Behavior](set-touchtone-buffer-behavior.md "set-touchtone-buffer-behavior.md") | Controls the starting, stopping, clearing, and saving<br>characters of the touchtone buffer.                                                                                                                                                                                                       |
| [Play prompt](play.md "play.md")                                                                        | Offers a new checkbox labeled **Skip or interrupt<br>this prompt when touchtone buffering is enabled**. When<br>this option is selected and touchtone buffering is enabled, the prompt<br>is skipped if the buffer contains digits, or interrupted if the<br>caller presses a key during playback. |
| [Get customer input](get-customer-input.md "get-customer-input.md")                                     | If digits exist in the buffer, they are retrieved, and the<br>flow advances without prompting the caller to provide the<br>input.                                                                                                                                                                  |
| [Store customer input](store-customer-input.md "store-customer-input.md")                               | If digits exist in the buffer, they are retrieved and<br>stored. If the buffer meets or exceeds the configured maximum<br>digits, the flow advances without prompting. Otherwise, the<br>inter-digit timeout is applied to allow the caller to enter<br>remaining digits.                          |

## Configure a flow for touchtone buffering

Touchtone buffering in Connect Customer works best when integrated with the existing [Get customer input](get-customer-input.md "get-customer-input.md") and [Store customer input](store-customer-input.md "store-customer-input.md") flow
blocks, which are specifically designed to capture touchtone keypad entries from callers.
Repeat callers, who are typically familiar with the navigation menu of the call, can use
touchtone buffering to input information ahead of time. This allows them to bypass
non-mandatory prompts and configurations set in the [Get customer input](get-customer-input.md "get-customer-input.md") and [Store customer input](store-customer-input.md "store-customer-input.md") blocks,
thereby reducing call handling time and improving efficiency.

## The buffer lifecycle

- **Enable buffering**: Use the [Set Touchtone Buffer
  Behavior](set-touchtone-buffer-behavior.md "set-touchtone-buffer-behavior.md") block from the Connect Customer flow
  designer UI to start capturing inputs.
- **Automatic collection and processing**: Use
  this block at the start of the flow to enable touchtone buffering. From that point
  onward, digits pressed by customers are stored in a 30-character buffer. The
  buffer automatically discards any used digits immediately after they are
  processed in the flow. Once the buffer reaches its 30-character limit,
  additional customer entries are ignored until space becomes available.
- **Controlled clearing**: Stop and optionally
  store buffer contents when appropriate. You can configure encryption parameters
  to encrypt the buffer entry that gets stored into the `Stored customer
 input` system attribute to protect PII.

## Block capabilities

### Set Touchtone Buffer Behavior

Enable Buffering

- Activates touchtone digit buffer collection for the
  contact.
- Buffer persists across flow modules and supports up to 30
  digits.

Stop and Clear

- Stops buffering collection and clears the buffer.
- Optionally stores buffer contents in the `Stored
 customer input` system attribute.
- Use stored values for downstream decisions if
  needed.

#### Automatic clearing

In some cases the buffer is automatically stopped and cleared:

- When transferring to an agent or queue
- When using [Get customer input](get-customer-input.md "get-customer-input.md") with Amazon Lex
  bots
- On contact disconnect

### Play Prompt

Skip or interrupt capability

- New checkbox: **Skip or interrupt this prompt when
  touchtone buffering is enabled**
- Unchecked by default for backward compatibility.
- When skip or interrupt prompt is enabled, the prompt is
  skipped entirely if the buffer contains digits.
- When skip or interrupt prompt is enabled and the buffer is
  empty, the prompt plays fully or continues until the caller
  begins entering digits, at which point it is
  interrupted.

**Use cases**

- Skip non-mandatory welcome messages for repeat callers.
- Allow experienced users to bypass menu explanations.
- Maintain required compliance messages by leaving the checkbox
  unchecked.

### Get Customer Input

DTMF mode

- If the buffer contains a digit, automatically dequeues and
  uses it.
- No configuration changes needed. Works seamlessly with
  existing flows.
- Prompts the customer for input if the buffer is
  empty.
- Dequeues one digit per invocation and continues to the next
  block immediately without waiting.

Amazon Lex mode

Automatically clears the buffer before bot interaction. Digits are
not used.

### Store Customer Input

Buffer-aware collection

- Dequeues up to the maximum number of digits specified in
  the block configuration.
- If the buffer has fewer digits than requested, applies the
  inter-digit timeout for partial buffering scenarios. For
  example, if the maximum configured digits are 6 and the
  buffer contains only 4 digits, the system waits for the
  specified timeout duration to allow the caller to enter the
  remaining digits. After the timeout expires, the call
  proceeds and stores whatever digits are present in the buffer
  at that moment.
- If the buffer contains equal to or more digits than the
  maximum configured on the block, the call proceeds
  immediately.
- **Specify a terminating
  keypress**: Flow designers can define a custom
  terminating keypress for when contacts complete their touchtone
  inputs. The terminating keypress may be up to five characters
  long, including `#`, `*`, and digits
  0-9.

## Flow logging changes

When touchtone buffering is enabled, flow logs for the following blocks indicate
whether the prompt was skipped or interrupted:

- [Play prompt](play.md "play.md")
- [Get customer input](get-customer-input.md "get-customer-input.md")
- [Store customer input](store-customer-input.md "store-customer-input.md")

## Common use cases

### Express menu navigation

**Scenario: Banking IVR with multiple menu
levels**

**Without buffering:**

1. System: "Main menu. Press 1 for..."
2. Customer waits for the prompt to finish.
3. Customer presses 1.
4. System: "Account menu. Press 1 for..."
5. Process repeats for each menu level.

**With buffering:**

1. System: "Main menu. Press 1 for..."
2. Customer immediately enters 1-2-3.
3. System skips remaining prompts and processes the full path.
4. Customer reaches their destination in seconds.

### Passing caller context using choose-to-call or app-to-call

Touchtone buffering also enables applications to pass known caller context into
a flow before the conversation starts. In choose-to-call and app-to-call scenarios,
the originating application can append a customer identifier, web session reference,
or other context to the dial string. For example,
`tel:+15555555555,1234567` sends the digits `1234567` into
the buffer the moment the call connects. The flow can then use that input to
identify the caller, look up session or account details, and provide that context
to an AI agent. This gives AI self-service the information it needs to personalize
the interaction from the first turn, without asking the caller to re-identify
themselves or explain why they are calling.

## Implementation best practices

### Strategic buffer placement

- Enable buffering early in your flow.
- Keep buffering active through menu navigation.
- Stop and clear the buffer after processing the intended input.

### Prompt configuration

Enable skip/interrupt for:

- Menu option lists
- Non-mandatory informational messages
- Repeated navigation prompts

Keep skip/interrupt disabled for:

- Legal disclaimers
- Compliance messages
- Critical instructions

### Input block design

- Use [Get customer input](get-customer-input.md "get-customer-input.md") for single-digit menu
  selections.
- Use [Store customer input](store-customer-input.md "store-customer-input.md") for multi-digit entries
  (account numbers, PINs).
- Configure appropriate maximum digit counts.
- Set reasonable inter-digit timeouts for partial buffer
  scenarios.

### Buffer management

- Store buffer contents before Amazon Lex interactions if you need the
  values later.
- Clear the buffer explicitly when starting new input sequences.
- Use stored buffer values for session management or context
  passing.
