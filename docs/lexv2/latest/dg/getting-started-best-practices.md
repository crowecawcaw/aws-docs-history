# Best Practices for Getting Started

## Conversation Design Principles

Following these conversation design principles from the start will help you build more effective, maintainable, and user-friendly Amazon Lex V2 chatbots that provide natural interactions.

### Core Design Principles

- **Start with User Goals** - Design your bot around what users want to accomplish, not what your system can do. Focus on the user's journey and desired outcomes.
- **Use Natural Language** - Write prompts and responses conversationally. Avoid technical jargon and speak as a helpful human would.
- **Provide Clear Options** - When users get stuck, offer specific examples of what they can say rather than generic help text.
- **Keep It Simple** - Start with basic functionality and gradually add complexity. Users should be able to complete common tasks quickly.
- **Handle Errors Gracefully** - When the bot doesn't understand, provide helpful guidance rather than just saying "I don't understand."
- **Confirm Important Actions** - Always confirm before taking actions that can't be easily undone, like placing orders or deleting information.
- **Provide Escape Routes** - Always give users a way to start over, get help, or connect with a human when needed.

### Conversation Flow Best Practices

- **Set Clear Expectations** - Let users know what the bot can and cannot do early in the conversation.
- **Use Progressive Disclosure** - Ask for information one piece at a time rather than overwhelming users with multiple questions.
- **Provide Context** - Remind users what information you've already collected and what you still need.
- **Make Corrections Easy** - Allow users to correct information without starting over completely.

## Real-World Use Cases and Examples

These practical examples show how to apply conversation design principles to common scenarios that new Amazon Lex V2 users encounter.

### Use Case 1: Appointment Booking

**Scenario:** A medical office wants to automate appointment scheduling.

**Challenge:** Users need to provide multiple pieces of information (service type, date, time, contact info) and may want to change details.

**Solution Approach:**

- **Start Broad:** "What type of appointment would you like to schedule?" (dental, eye exam, consultation)
- **Narrow Down:** "When would you prefer your dental appointment?" (Accept flexible input like "next week" or "Friday afternoon")
- **Confirm and Offer Changes:** "I have you scheduled for a dental cleaning on Friday, March 15th at 2 PM. Does this work for you?"
- **Handle Changes:** If user says "Can we do 3 PM instead?", update the time without restarting the entire process.

**Key Techniques:**

- Use [AMAZON.Date](built-in-slot-date.md "built-in-slot-date.md") and [AMAZON.Time](built-in-slot-time.md "built-in-slot-time.md") for flexible date/time input
- Create custom slot types for appointment types
- Use confirmation prompts before finalizing bookings

### Use Case 2: Order Status Inquiry

**Scenario:** An e-commerce company wants customers to check order status without calling support.

**Challenge:** Users might not have their order number handy, or might ask in different ways.

**Solution Approach:**

- **Multiple Entry Points:** Accept "Where's my order?", "Track my package", or "Order status"
- **Flexible Identification:** "I can help you track your order. Do you have your order number, or would you prefer to use your email address?"
- **Helpful Guidance:** "Your order number is usually in your confirmation email and starts with 'ORD-'"
- **Clear Results:** "Your order #ORD-12345 shipped yesterday and will arrive tomorrow by 8 PM. Would you like tracking details?"

**Key Techniques:**

- Use built-in slot types like AMAZON.AlphaNumeric for order numbers
- Provide multiple ways to identify orders (email, phone, order number)
- Give clear, actionable information in responses

### Use Case 3: FAQ and Support

**Scenario:** A software company wants to handle common support questions automatically.

**Challenge:** Users ask the same questions in many different ways, and some issues require human help.

**Solution Approach:**

- **Broad Intent Recognition:** Train intents to recognize variations like "I can't log in", "Login problems", "Password not working"
- **Guided Troubleshooting:** "Let's try a few quick steps. First, have you tried resetting your password?"
- **Escalation Path:** "If these steps don't work, I can connect you with our support team. Would you like me to do that?"
- **Follow-up:** "Did this solve your problem? You can always say 'help' if you need assistance with something else."

**Key Techniques:**

- Use many sample utterances to capture different ways users express problems
- Provide step-by-step guidance rather than long explanations
- Always offer a path to human support when automated help isn't sufficient

### Handling Complex Scenarios

Even simple bots encounter complex situations. Here's how to handle them gracefully:

- **When Users Change Their Mind:**
  - User: "Actually, I want roses instead of tulips"
  - Bot: "No problem! I've updated your order to roses. Your roses will be ready for pickup on Friday at 2 PM. Is that correct?"

- **When Information is Unclear:**
  - User: "I need flowers for next week"
  - Bot: "I'd be happy to help! Which day next week works best for you? You can say something like 'Monday' or 'next Tuesday'."

- **When the Bot Doesn't Understand:**
  - User: "I want the purple ones with the long stems"
  - Bot: "I want to make sure I get this right. Are you looking for purple flowers? We have purple roses, purple tulips, and purple irises available."

- **When Users Need to Start Over:**
  - User: "Cancel this, I want to start over"
  - Bot: "Of course! I've cleared your current order. What type of flowers would you like to order today?"
