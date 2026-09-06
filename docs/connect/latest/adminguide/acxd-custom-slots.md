# Custom slots

Custom slots define structured values your application can capture during a conversation.

In agentic CX designer, slots help collect information from users so a flow can
continue with the right data. A custom slot is a slot type you create for values
specific to your business, such as room types, product sizes, support categories,
appointment reasons, or yes/no choices.

For example, if a user says "I'd like a large," the application can
capture "large" as the selected value for a custom Size slot.

To access custom slots, select **Resources** from your workspace menu, then choose
**Slots**.

Use a custom slot when the user should choose from a defined set of values.

Custom slots are especially useful with User choice nodes or agent nodes because
they help the application capture a structured value and route the conversation
based on that value.

Use custom slots for business-specific values that you define.

Use built-in slots for common input types that agentic CX designer already
supports, such as:

- Date
- Time
- Email
- Phone number
- Freeform text
  You do not create built-in slots from the custom Slots resource. Instead, select the
  appropriate built-in slot when attaching slots to a flow.

## Creating a custom slot

###### To create a custom slot

1. Open **Resources** from the workspace menu.
2. Select **Slots**.
3. Select **Create slot** or **Create**.
4. Enter a clear slot name.
5. Add one or more values.
6. Save the slot.

Use a name that describes what the slot captures.

## Adding values

Values are the allowed options for the custom slot.

###### To add values

1. Open the custom slot.
2. Select **Add value**.
3. Enter the value.
4. Repeat for each option.
5. Save your changes.

Avoid values that are too similar, because closely named values can make matching less clear.
In that case, use one as the main value and add the other as a synonym.

## Synonyms

Synonyms let you define alternate phrases that should resolve to the same slot value.

For example, a "Yes" value may include synonyms such as:

- Sure
- OK
- Yep
- That works
- Sounds good

###### To add synonyms

1. Open the custom slot.
2. Expand a value.
3. Select **Add synonym**.
4. Enter one or more alternate phrases.
5. Save your changes.

Synonyms help users respond naturally while still letting the application capture a
controlled value.

## Choice payload

A choice payload defines additional information for how a value should be
displayed or handled when shown as a user selection.

Use a choice payload when you need to:

- Customize how a choice appears
- Include supporting display information
- Reference context variables in a displayed choice
- Control ordering or sorting behavior
- Add metadata that helps the frontend or flow handle the selected value

###### To add a choice payload

1. Open the custom slot.
2. Expand the value.
3. Locate the **Choice payload** field.
4. Enter the payload details.
5. Save your changes.

You can use the placeholder menu by typing { in supported fields to insert
available variables.

## Attaching a custom slot to a flow

After creating a custom slot, attach it to the flow where it will be used.

###### To attach a slot

1. Open the flow.
2. Open the flow settings from the Canvas toolbar.
3. Go to **Attached slots**.
4. Add the custom slot.
5. Give the attached slot a clear name, if prompted.
6. Save the flow.

Once attached, the slot can be used in nodes that collect or reference user responses.

## Using custom slots in a User choice node

Custom slots are commonly used with User choice nodes.

###### To use a custom slot in a User choice node

1. Open the flow in the Canvas.
2. Add or select a User choice node.
3. Choose the attached custom slot as the response source.
4. Configure paths for matched values.
5. Add a No match path for unclear or unsupported responses.
6. Save and test the flow.

## Translations

If your application supports multiple languages, translate custom slot values and
synonyms using Translations in the workspace.

Custom slots used in multilingual flows should be translated for each language your
application supports.

Review translated slot values carefully, especially when values affect routing,
compliance, or customer-facing choices.

## Sensitive slot values

Enable **Exclude from conversation history** when slot values should not appear in
conversation transcripts.

Use this setting for values that may include:

- Personal information
- Account details
- Protected user attributes
- Sensitive selections
- Any value your organization treats as confidential

Only mark a slot as non-sensitive when the captured value is safe to store and
review in conversation transcripts.
