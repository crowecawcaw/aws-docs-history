# Agentic voice best practices

Amazon Connect agentic voice combines advanced speech recognition (ASR) with expressive, natural-sounding voices to deliver a complete voice AI experience. Advanced ASR provides natural, low-latency turn taking in real-time conversations, while the voice engine delivers lifelike speech across 50+ locales. Together, these components power seamless, human-like interactions between callers and Amazon Connect AI agents. This guide covers configuration and best practices for both components, so you can get the most out of the full agentic voice experience.

###### Note

To use Amazon Connect agentic voice features, make sure Amazon Connect Customer is enabled for your instance. Amazon Connect agentic voice is the default voice provider for Amazon Connect Customer.

This guide covers:

- Session attribute syntax for ASR controls.
- Barge-in (interrupt) behavior and when to disable it.
- End-of-turn tuning for Advanced ASR.
- Language hints for multilingual speech recognition.
- Handling long-running tool calls.
- Text formatting best practices for voice output.
- Speech control tags for fine-grained voice control.
- System prompts for Amazon Connect AI agents.
- Contact center examples.
- Multilingual voice configuration for multi-language support.

## Advanced speech recognition (ASR) best practices

The Advanced ASR speech model preference is a streaming recognizer designed for natural, low-latency turn taking in real-time conversations. Instead of relying only on a fixed window of silence, it evaluates the caller's speech as they talk and predicts when the caller has finished — the end of turn (EOT).

### Session attribute syntax

The controls in this section are set with standard Lex V2 session attributes in the `x-amz-lex` namespace. You set them when you start a conversation and can override them in a Lambda function (for example, to relax detection only while collecting a sensitive value).

Scope every attribute to an intent and slot:

```
x-amz-lex:audio:<setting>:<intentName>:<slotToElicit>
```

- Use `*` as the intent or slot name to set a default that applies everywhere.
- Any intent- or slot-specific setting takes precedence over a `*` default.

**Do:**

- Set conservative values only on the slots that need them (for example, an account-number slot), and leave everything else on defaults.
- Reset relaxed values for the next slot after a sensitive collection is complete.

**Don't:**

- Apply a single aggressive `*:*` default globally to fix one slot — it changes pacing for every turn in the bot.

### Barge-in (interrupt behavior)

Barge-in lets the caller interrupt a prompt the bot is playing. It is enabled by default, which is usually what you want for natural conversation. You control it with:

```
x-amz-lex:allow-interrupt:<intentName>:<slotToElicit>
```

Default: `true`

**Disable barge-in (`false`) when:**

- Playing legal, compliance, or recording-disclosure language that must be heard in full.
- Reading back a confirmation that the caller should not talk over.

**Keep barge-in enabled when:**

- The caller might want to correct or short-cut the bot mid-prompt — the normal conversational case.

###### Example

For a self-service AI agent, leave barge-in on everywhere by default. Disable it only where a prompt must be heard in full — for example, a legal or compliance disclaimer. Set the attributes when you start the conversation. Keep the default on with a `*:*` entry, and turn barge-in off only for the intent that plays the disclaimer:

```
{
  "sessionState": {
    "sessionAttributes": {
      "x-amz-lex:allow-interrupt:*:*": "true",
      "x-amz-lex:allow-interrupt:Disclaimer:*": "false"
    }
  }
}
```

The intent- and slot-specific entry takes precedence over the `*:*` default, so the caller can interrupt everywhere except while the `Disclaimer` intent is speaking. If you set the disclaimer attribute in a Lambda function instead, set it before the disclaimer prompt plays. Reset it to `true` afterward so the rest of the conversation stays interruptible.

###### Note

**A timeout-driven re-prompt is not real barge-in.** A common point of confusion: if a caller goes silent and the end-of-turn fallback fires, the bot might end the turn or re-prompt on its own. This can look like an interruption, but it is the end-of-turn detection firing, not the caller barging in. The fix is almost always tuning the end-of-turn settings — not the allow-interrupt flag.

### End-of-turn tuning

Advanced ASR ends a turn when either condition is met first:

- **End-of-turn confidence threshold** — the model is confident enough that the caller has finished. This is the primary signal and is what makes turn taking sound natural.
- **End-of-turn silence timeout** — the caller has been silent for the configured time. This is the fallback (a caller trailing off or going quiet).

End-of-turn settings| Setting | Session attribute | Default | Range |
| --- | --- | --- | --- |
| End-of-turn confidence threshold | `x-amz-lex:audio:end-confidence-threshold` | 0.7 | 0.5–0.9 |
| End-of-turn silence timeout | `x-amz-lex:audio:end-timeout-ms` | 5,000 ms | 500–10,000 ms |

Higher values make the bot wait longer and end turns more conservatively (fewer premature cutoffs, slightly more latency). Lower values end turns sooner (lower latency, higher chance of cutting off a caller who pauses). The confidence threshold is the primary lever; the silence timeout only matters when confidence has not already ended the turn.

**Out-of-range behavior:**

- `end-confidence-threshold` outside 0.5–0.9 is rejected with an invalid session attribute error.
- `end-timeout-ms` below 500 or above 10,000 is silently clamped to the nearest supported value.

**Choosing values**

Choosing end-of-turn values| Scenario | Recommended settings | Notes |
| --- | --- | --- |
| Natural conversation | Defaults (0.7 / 5,000 ms) | Tuned for responsive general-purpose turn taking. |
| Sensitive or dictated input (OTP, account number) | threshold: 0.9, timeout: 6,000–8,000 ms | Tolerates pauses. Reset for the next slot after collection. |
| Short exchanges (yes/no, single word) | threshold: ~0.5, timeout: ~500 ms | Faster turns. Test for premature cutoffs first. |

**Example**

Conservative end-of-turn detection for the `AccountNumber` slot of the `VerifyIdentity` intent:

```
{
  "sessionState": {
    "sessionAttributes": {
      "x-amz-lex:audio:end-confidence-threshold:VerifyIdentity:AccountNumber": "0.9",
      "x-amz-lex:audio:end-timeout-ms:VerifyIdentity:AccountNumber": "7000"
    }
  }
}
```

A single default for every intent and slot:

```
{
  "sessionState": {
    "sessionAttributes": {
      "x-amz-lex:audio:end-confidence-threshold:*:*": "0.8",
      "x-amz-lex:audio:end-timeout-ms:*:*": "800"
    }
  }
}
```

### Language hints for multilingual recognition

Advanced ASR recognizes multiple languages in the same conversation without being told which languages to expect. It detects the language from the caller's speech, so a caller can start in English and switch to Spanish and the transcription follows. This is the default behavior and needs no configuration.

If you already know which languages your callers use, you can bias recognition toward them with language hints. Hints help most when two languages sound similar. They also help when short utterances — a single word, a digit, a yes/no — give the model little to work with. You set them with:

```
x-amz-lex:audio:locale-override:<intentName>:<slotToElicit>
```

Default: no hints — Advanced ASR detects the language on its own.

Scope the attribute the same way as the other controls in this section. Use `*:*` to bias every turn in the conversation, or name an intent and slot to bias only the turns where you know the expected language.

###### Value format

Set the value to the language codes you want to bias toward, most likely first. Use a comma-separated list, optionally wrapped in brackets and quotes if that is easier to produce from your flow or Lambda function. Advanced ASR ignores surrounding whitespace and treats underscores as hyphens, so `pt_BR` and `pt-BR` are equivalent.

The following table shows example attribute values and the languages each one biases Advanced ASR toward.

Language hint values| Attribute value | Languages Advanced ASR is biased toward |
| --- | --- |
| Attribute not set | None. Advanced ASR detects the language from the caller's speech. |
| `es,en-US` | Spanish, then US English |
| `["ja"]` | Japanese |
| `[ "es" , "en" ]` | Spanish, then English |
| `fr, de , it` | French, then German, then Italian |

###### Validation

- Each entry must be a valid language code. Use a two- or three-letter base code, optionally followed by a hyphen and a region subtag — for example `es`, `en-US`, or `pt-BR`.
- Entries that do not match that form are dropped, and the remaining valid entries are still applied. If no valid entry remains, the conversation proceeds with no hints instead of failing.
- Advanced ASR passes through and ignores a well-formed code that it does not recognize. The code does not produce an error, but it does not bias recognition either, so verify the codes you send.
- Advanced ASR removes duplicates. It applies at most 10 hints and ignores any beyond the tenth.

###### Example

The following example biases recognition for a line whose callers speak Spanish or English, with Spanish the more common language:

```
{
  "sessionState": {
    "sessionAttributes": {
      "x-amz-lex:audio:locale-override:*:*": "es,en-US"
    }
  }
}
```

###### Do

- Leave the attribute unset unless you have a specific reason to bias recognition. Detection handles most multilingual conversations.
- List only the languages your callers actually speak, most likely first.

###### Don't

- List languages beyond those your callers actually speak. A long list dilutes the bias and removes the benefit of setting hints at all.
- Send a single hint to lock the conversation to one language. A hint biases recognition; it does not restrict it. To restrict the languages the AI agent responds in, see [Restricting to specific languages](#agentic-voice-multilingual-restricting "#agentic-voice-multilingual-restricting").

###### Tip

Language hints bias speech recognition — what the bot hears. They do not change which language the bot speaks. For the response language, use the AI agent system prompt and a multilingual voice. See [Multilingual voice configuration](#agentic-voice-polyglot-configuration "#agentic-voice-polyglot-configuration").

### Handling long-running tool calls

When an AI agent or Lambda makes a long-running tool call (a backend lookup, an external API, a model invocation) before the bot is ready to listen, the caller sits in silence. To the caller this can feel like the bot stalled or talked over them when it finally responds.

**Mitigations:**

- Complete the long-running work before the bot opens the mic. Finish the tool call before the bot elicits the next slot.
- Play a holding or filler prompt ("One moment while I pull that up…") so the caller is not sitting in silence.
- Enable filler audio sounds during tool calls or turn by turn.
- Keep barge-in enabled through these steps so that if the caller speaks during a filler prompt, they can move things along.

###### Tip

Validate latency end-to-end with your actual tool calls. The goal is that the caller is never left in dead air waiting on the backend.

### ASR session attribute quick reference

ASR session attribute quick reference| Attribute | Default | Notes |
| --- | --- | --- |
| `x-amz-lex:allow-interrupt:<intent>:<slot>` | true | Barge-in. Set `false` for disclaimers. |
| `x-amz-lex:audio:end-confidence-threshold:<intent>:<slot>` | 0.7 | Primary EOT signal. Range 0.5–0.9. Out-of-range rejected. |
| `x-amz-lex:audio:end-timeout-ms:<intent>:<slot>` | 5,000 ms | EOT fallback. Range 500–10,000 ms. Out-of-range clamped. |
| `x-amz-lex:audio:locale-override:<intent>:<slot>` | Not set | Language hints biasing recognition. Comma-separated codes, max 10. |

### Common ASR mistakes

Common ASR mistakes| Mistake | Why it's bad | Fix |
| --- | --- | --- |
| Low confidence threshold while collecting dictated digits | Bot cuts the caller off between groups | Raise confidence and timeout on that slot, reset after. |
| Disabling barge-in globally | Caller can't correct the bot anywhere | Disable only on disclaimer/compliance prompts. |
| Applying a `*:*` default to fix one slot | Changes pacing for the whole bot | Scope the attribute to the specific intent/slot. |
| Setting threshold outside 0.5–0.9 | Request is rejected with an error | Keep it in range. Only `end-timeout-ms` clamps silently. |
| Leaving input window open during a long tool call | Caller sits in dead air | Finish the tool call first or play a filler prompt. |
| Treating an EOT re-prompt as real barge-in | Wrong fix applied to allow-interrupt | Tune the end-of-turn settings instead. |
| Listing many languages in `locale-override` | Dilutes the bias it was set to provide | List only the languages callers speak, most likely first. |

## Voice best practices

Amazon Connect agentic voice delivers expressive, natural-sounding text-to-speech across 50+ locales. The engine automatically normalizes written text into natural speech. In most cases, you can pass text as-is and get great results without any special formatting.

### Text formatting

**General rules**

Pass natural, well-punctuated text. Full sentences with normal capitalization and punctuation produce the best pacing and intonation.

**Do:**

- Use complete sentences with terminal punctuation (. ? !).
- Use normal capitalization.
- Keep numbers, dates, and common formats in conventional written form.
- Keep each generation to at least a full sentence or phrase. Very short fragments tend to sound less natural.

**Don't:**

- Strip punctuation or force ALL CAPS.
- Include markdown, raw JSON, emoji, or special characters.
- Send numbers, alphanumerics, or spell tags by themselves without full context.
- Wrap text in markdown bold or italics — the engine will attempt to speak the asterisks.
- Use parentheses, brackets, curly braces, angle brackets, and quotation marks.

**Automatic normalization**

The engine reads common written formats as natural speech. Most times, you don't need to reformat them:

Automatic text normalization| Type | Pass this | Engine reads as |
| --- | --- | --- |
| Large numbers | 1,234,567 | "one million two hundred thirty-four thousand..." |
| Phone numbers | (415) 555-1212 | Natural phone number pacing |
| Email addresses | user@example.com | "user at example dot com" |
| Dates | 04/20/2025 | Locale-appropriate date reading |
| Times | 7:00 PM | "seven PM" |
| Acronyms | NASA, USA | Spoken as expected |
| Percentages | 12% | "twelve percent" |

###### Tip

Email addresses read well in written form. You can also instruct your agent to output the spoken form directly (for example, "user at example dot com") if you want precise control.

### Speech control tags

The voice engine automatically infers appropriate pacing and emotion from transcript content. Use control tags only for specific use cases where the default does not satisfy. All tags are placed directly in the transcript.

#### Speed

Control the speaking rate. Range: 0.6 (slow) to 1.5 (fast). Default: 1.0.

```
<speed ratio="0.85"/>This call may be recorded for quality purposes.
```

Speed values| Value | Use when |
| --- | --- |
| 0.8 | Reading important information or legal language |
| 1.0 | Default — natural conversational speed |
| 1.2 | Faster-paced dialogue |

To reset speed after slowing down:

```
<speed ratio="0.85"/>Important notice.<speed ratio="1.0"/>Now, how can I help?
```

#### Volume

Control loudness. Range: 0.5 (quiet) to 2.0 (loud). Default: 1.0.

```
<volume ratio="0.5"/>I'll speak softly for this part.
```

#### Breaks

Insert pauses. Specify duration in seconds (s) or milliseconds (ms).

```
Your balance is $1,234.<break time="500ms"/>Your next payment is due June 15th.
```

Use breaks for:

- Pacing between pieces of information.
- Before legal or compliance language.
- Between menu options in an IVR.

###### Note

Natural punctuation should be the first tool for pausing. A comma or period usually produces the right pause. Break tags are best reserved for explicit silences of specific duration.

#### Spell

Force character-by-character readout for codes, IDs, phone numbers, or any string that should be spoken letter-by-letter.

```
Your confirmation code is <spell>TKT4829XB</spell>.
```

For long sequences, add a space inside the spell tag wrapper to insert pauses:

```
Your phone number is <spell>(415)</spell><break time="200ms"/><spell>5551212</spell>.
```

**Alternative formats (without tags):**

- Space-delimited: A B C 1 2 3
- Grouped with commas: A B C, 1 2 3.
- Slowed and enunciated: A, B, C, 1, 2, 3

###### Note

The model treats ALL CAPS text the same as wrapping it in <spell> tags — it will be read out letter by letter. For example, "ACME BANK" would be spoken as "A-C-M-E B-A-N-K." To have the model speak it as a word, use standard capitalization: "Acme Bank."

#### Emotion

The model naturally infers emotional tone from content — no tags needed in most cases. Emotion tags are a beta capability and work most reliably when the emotion matches the transcript.

```
<emotion value="sympathetic"/>I understand this is frustrating. Let me investigate that for you.
```

Primary emotions: `neutral`, `angry`, `excited`, `content`, `sad`, and `scared`.

#### Laughter

Insert `[laughter]` to produce a natural laugh.

```
Oh, I've actually heard that one before! [laughter] Alright, let's get this sorted out.
```

#### Tag reference

Speech control tag reference| Tag | What it does | Example |
| --- | --- | --- |
| `<speed ratio="X"/>` | Speaking rate (0.6–1.5) | `<speed ratio="0.85"/>` |
| `<volume ratio="X"/>` | Loudness (0.5–2.0) | `<volume ratio="1.5"/>` |
| `<break time="Xs"/>` | Pause (seconds or ms) | `<break time="500ms"/>` |
| `<spell>...</spell>` | Character-by-character readout | `<spell>AB12CD</spell>` |
| `<emotion value="X"/>` | Emotional tone | `<emotion value="content"/>` |
| `[laughter]` | Natural laughter | `[laughter]` |

#### Malformed tags

- Well-formed tags enclosed in matching `<...>` are processed correctly by the engine.
- Malformed or unclosed tags will not be silently dropped — the engine will speak the malformed text aloud.
- Unsupported SSML wrappers like `<speak>...</speak>` are not required and should not be included.

###### Tip

If the engine encounters a tag it cannot parse, it will attempt to speak the raw text including tag fragments. Always validate that your tags are well-formed.

### Multilingual voice configuration

Amazon Connect agentic voice includes multilingual voices that can speak multiple languages and switch between them seamlessly mid-conversation. A caller can start in English, switch to Spanish, and the agent follows — no flow changes or interruptions required. In the Set Voice block, these voices are labeled as polyglot voices. This guide uses the term multilingual voices to describe them. This section covers how to configure multilingual voices and what to watch out for.

#### Multilingual voices

Multilingual voices natively switch between supported languages within a single conversation. Use a multilingual voice when your contact center needs to handle callers who speak different languages or switch languages mid-call.

Multilingual voices| Voice | Gender | Supported languages |
| --- | --- | --- |
| Katie | Feminine | English, German, Spanish, French, Hindi, Italian, Japanese, Norwegian, Portuguese, Russian |
| Blake | Masculine | English, German, Spanish, French, Hindi, Italian, Japanese, Norwegian, Portuguese, Russian |
| Brooke | Feminine | English, German, Spanish, French, Hindi, Italian, Japanese, Norwegian, Portuguese, Russian |
| Ronald | Masculine | English, German, Spanish, French, Hindi, Italian, Japanese, Norwegian, Portuguese, Russian |
| Gemma | Feminine | English, German, Spanish, French, Hindi, Italian, Japanese, Norwegian, Portuguese, Russian |

#### Configuration

##### Step 1: Build your Amazon Lex bot in the multilingual voice's locale

If you use a multilingual voice, you need only a single Amazon Lex bot locale. Build your bot in the locale that matches the multilingual voice (for example, en-US or en-GB). You do not need to add every language the multilingual voice supports as a separate locale in Amazon Lex.

**Do:**

- Build your bot in en-US (or en-GB if using a UK English multilingual voice).
- Use a single locale. The AI agent and multilingual voice handle multilingual conversations without additional Amazon Lex locales.

**Don't:**

- Add separate Amazon Lex bot locales for every language the multilingual voice supports. This is unnecessary — the AI agent handles language switching through the prompt.

If you need to support a language that is not in the multilingual voice's supported language list (for example, Thai or Tagalog), create a separate bot for that locale and use a locale-specific voice. See [Using a non-multilingual agentic voice in a non-English locale](#agentic-voice-multilingual-non-english-locale "#agentic-voice-multilingual-non-english-locale").

##### Step 2: Match the Lex bot locale to the Set Voice block

The language attribute set in the Set Voice block must match the locale of your Lex bot. If they do not match, then the Get Customer Input block returns an error. Update the Set Voice block language to match your bot locale.

For multilingual voices built on an English locale:

1. In the Set Voice block, select the multilingual voice (for example, Brooke) and set the language to English (US).
2. Your Lex bot must have en-US as a built locale.

##### First-turn greeting

On the first turn, the AI agent has not received any caller input. Without input, the agent cannot detect the caller's language. The voice speaks the greeting text configured in the Get Customer Input block. If you want the bot to greet the caller in a specific language, make sure the greeting message in that block is written in that language.

For example, if your primary caller base speaks Spanish, configure the Get Customer Input greeting in Spanish:

```
Hola, gracias por llamar. ¿Cómo puedo ayudarle hoy?
```

After the first turn, the AI agent takes over and detects and follows the caller's language for the rest of the conversation.

##### Step 3: Add language-handling instructions to the AI agent system prompt

Add a language-handling section to your AI agent's system prompt. This section drives the multilingual behavior. The AI agent detects the caller's language from the transcript and responds in that language.

Template (customize for your use case):

```
You are connected to a multilingual voice that supports the following languages: English, German, Spanish, French, Hindi, Italian, Japanese, Norwegian, Portuguese, and Russian.

Language handling rules:
Detect the language of the caller's input from the transcription.
If the caller speaks in one of the supported languages listed above, respond in that same language.
If the caller speaks a language not in the supported list, respond in English and politely let them know you can assist in the supported languages.
Always respond in one language at a time. Do not mix languages in a single response unless the caller mixes first.
If the caller switches languages mid-conversation, follow their lead immediately.
When responding in any non-English language, always use proper accent marks, diacritics, and locale-appropriate formatting (for example, é, ñ, ü, ç). This ensures the voice engine produces natural pronunciation.
Keep English brand names, product names, codes, and identifiers in English. Do not translate them.
```

###### Tip

Only list languages your multilingual voice actually supports in the prompt. Listing unsupported languages causes the agent to claim it can help, but the TTS produces unnatural output.

##### Using a non-multilingual agentic voice in a non-English locale

If you are using an agentic voice that is not a multilingual voice (for example, a Thai, Korean, or Portuguese voice), you must explicitly set the language attribute so the system routes to the correct ASR engine.

**Option A: Set Voice block**

1. Select your non-English voice (for example, a Thai voice for the th-TH locale).
2. Set the language to the matching locale (for example, th-TH).
3. Build your Lex bot with a matching locale (th-TH).

**Option B: Set Contact Attributes block**

If the Set Voice block does not expose the language setting for your configuration, you can set the language using the Set Contact Attributes block before the Get Customer Input block:

- **Type** — System
- **Attribute** — Language
- **Value** — The locale code (for example, tl-PH for Tagalog, th-TH for Thai)

#### Restricting to specific languages

If your contact center only supports a subset of languages, simplify the prompt:

```
You support English and Spanish on this line only.
Detect the language of the caller's input.
If the caller speaks English or Spanish, respond in that language.
If the caller speaks any other language, respond in English: I apologize, but I can only assist in English or Spanish. How can I help you today?
If the caller switches between English and Spanish, follow their lead.
Use proper accent marks when responding in Spanish (á, é, í, ó, ú, ñ, ü).
Keep brand names and codes in English.
```

### System prompt for Amazon Connect AI agents

When Amazon Connect AI Agents generate text that will be spoken, add these speech formatting instructions to your agent's system prompt. Copy and paste the block below directly into your prompt configuration.

###### Note

These prompts are templates to get you started. Modify them for your specific use case, tone, and business requirements.

###### Tip

For guidance on optimizing your AI agent prompt for voice performance and latency, see [Prompt engineering best practices for AI agents](agentic-self-service-prompt-best-practices.md "agentic-self-service-prompt-best-practices.md").

**Speech output formatting prompt**

```
Speech Output Formatting
Everything you output will be spoken aloud by text-to-speech.
Follow these rules:

GENERAL FORMATTING
Use full sentences with normal capitalization. Always end with . ? or !
Use conventional written forms for numbers, dates, acronyms, symbols.
Do NOT use markdown, bullet points, headers, bold, raw JSON, emoji, or special characters.
Write plain prose only.

SPELLING OUT CODES AND IDS
For codes or IDs that must be read character-by-character, except for phone numbers, wrap in <spell> tags:
Example: Your confirmation code is <spell>TKT4829XB</spell>. Was that the account ending in <spell>1234</spell>?

THINGS TO AVOID
Do not output bullet points, numbered lists, or structured formatting.
Do not use asterisks, hashtags, or markdown syntax.
Do not include internal thoughts, reasoning, or meta-commentary.
Do not use parentheses, brackets, curly braces, or quotation marks.

NATURALNESS
Respond as if speaking directly to the caller.
Keep responses concise. Avoid long monologues.
Use natural transitions like: Let me check that for you. Or: Here is what I found.
```

**Multilingual add-on**

If your bot uses a multilingual voice, add the following to your system prompt to enable multi-language responses:

```
Language Handling
You are connected to a multilingual voice that supports: English, German,
Spanish, French, Hindi, Italian, Japanese, Norwegian, Portuguese, and Russian.

Detect the language of the caller input from the transcription. If the
caller speaks in one of the supported locales, respond in that language.
If the caller speaks a language not in the supported list, respond in
English and politely let them know you can assist in English.

Always respond in one language at a time. Do not mix multiple languages
in a single response. If the caller switches languages mid-conversation,
follow their lead and switch your responses to match.

When responding in a non-English language, always use proper accent marks,
diacritics, and locale-appropriate formatting. This ensures the voice
engine produces natural, native-sounding pronunciation.
```

### Contact center examples

**IVR greeting**

```
Hi, thanks for calling. How can I help you today?
```

No tags needed — the engine handles conversational greetings naturally.

**Legal disclaimer (slowed)**

```
<speed ratio="0.85"/>This call may be recorded for quality assurance purposes. By continuing, you consent to recording.
```

Pair with barge-in disabled at the flow level.

**Reading back an account number**

With spell tags:

```
Your account number is <spell>1234</spell> <spell>5678</spell> <spell>9012</spell>.
```

Without spell tags:

```
Your account number is 1 2 3 4, 5 6 7 8, 9 0 1 2.
```

**Confirmation with reference code**

```
I've created your ticket. Your reference number is <spell>TKT4829XB</spell>. Is there anything else I can help with?
```

**Menu options**

```
Press 1 for billing.<break time="500ms"/>Press 2 for technical support.<break time="500ms"/>Press 3 to speak with an agent.
```

**Spelling a customer's name**

```
Let me confirm — your last name is Smith, spelled <spell>SMITH</spell>. Is that correct?
```

### Common text-to-speech mistakes

Common text-to-speech mistakes| Mistake | Why it's bad | Fix |
| --- | --- | --- |
| Stripping punctuation | Ruins pacing and intonation | Keep natural punctuation. |
| ALL CAPS text | Changes how the engine reads | Use normal capitalization. |
| Including markdown | Engine speaks formatting characters | Strip before sending, or instruct agent to avoid. |
| Streaming incomplete tags | Tags get read aloud as text | Buffer complete tag values before sending. |
| Mismatched emotion + content | Produces unnatural output | Align emotion with content, or omit. |
| Over-engineering the prompt | Can reduce naturalness | Start simple — add tags only where needed. |
| Non-multilingual voice for multi-language | Voice retains primary locale accent | Use a multilingual voice for native pronunciation. |
| Wrapping text in markdown bold or italics | Engine speaks the asterisks aloud | Remove all markdown formatting. |
| Sending malformed or unclosed tags | Engine speaks raw tag text | Validate tags are well-formed with matching brackets. |
