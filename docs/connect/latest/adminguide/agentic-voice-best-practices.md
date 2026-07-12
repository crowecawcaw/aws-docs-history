# Agentic voice best practices

Amazon Connect agentic voice combines advanced speech recognition (ASR) with expressive, natural-sounding voices to deliver a complete voice AI experience. Advanced ASR provides natural, low-latency turn taking in real-time conversations, while the voice engine delivers lifelike speech across 50+ locales. Together, these components power seamless, human-like interactions between callers and Amazon Connect AI agents. This guide covers configuration and best practices for both components, so you can get the most out of the full agentic voice experience.

This guide covers:

- Session attribute syntax for ASR controls.
- Barge-in (interrupt) behavior and when to disable it.
- End-of-turn tuning for Advanced ASR.
- Handling long-running tool calls.
- Text formatting best practices for voice output.
- Speech control tags for fine-grained voice control.
- System prompts for Amazon Connect AI agents.
- Contact center examples.
- Polyglot voice configuration for multi-language support.

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

###### Note

**A timeout-driven re-prompt is not real barge-in.** A common point of confusion: if a caller goes silent and the end-of-turn fallback fires, the bot might end the turn or re-prompt on its own. This can look like an interruption, but it is the end-of-turn detection firing, not the caller barging in. The fix is almost always tuning the end-of-turn settings — not the allow-interrupt flag.

### End-of-turn tuning

Advanced ASR ends a turn when either condition is met first:

- **End-of-turn confidence threshold** — the model is confident enough that the caller has finished. This is the primary signal and is what makes turn taking sound natural.
- **End-of-turn silence timeout** — the caller has been silent for the configured time. This is the fallback (a caller trailing off or going quiet).

End-of-turn settings| Setting | Session attribute | Default | Range |
| --- | --- | --- | --- |
| End-of-turn confidence threshold | `x-amz-lex:audio:end-confidence-threshold` | 0.7 | 0.5–0.9 |
| End-of-turn silence timeout | `x-amz-lex:audio:end-timeout-ms` | 640 ms | 500–10,000 ms |

Higher values make the bot wait longer and end turns more conservatively (fewer premature cutoffs, slightly more latency). Lower values end turns sooner (lower latency, higher chance of cutting off a caller who pauses). The confidence threshold is the primary lever; the silence timeout only matters when confidence has not already ended the turn.

**Out-of-range behavior:**

- `end-confidence-threshold` outside 0.5–0.9 is rejected with an invalid session attribute error.
- `end-timeout-ms` below 500 or above 10,000 is silently clamped to the nearest supported value.

**Choosing values**

Choosing end-of-turn values| Scenario | Recommended settings | Notes |
| --- | --- | --- |
| Natural conversation | Defaults (0.7 / 640 ms) | Tuned for responsive general-purpose turn taking. |
| Sensitive or dictated input (OTP, account number) | threshold: 0.9, timeout: 2,000–4,000 ms | Tolerates pauses. Reset for the next slot after collection. |
| Short exchanges (yes/no, single word) | threshold: ~0.5, timeout: ~500 ms | Faster turns. Test for premature cutoffs first. |

**Example**

Conservative end-of-turn detection for the `AccountNumber` slot of the `VerifyIdentity` intent:

```
{
  "sessionState": {
    "sessionAttributes": {
      "x-amz-lex:audio:end-confidence-threshold:VerifyIdentity:AccountNumber": "0.9",
      "x-amz-lex:audio:end-timeout-ms:VerifyIdentity:AccountNumber": "3000"
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
| `x-amz-lex:audio:end-timeout-ms:<intent>:<slot>` | 640 ms | EOT fallback. Range 500–10,000 ms. Out-of-range clamped. |

### Common ASR mistakes

Common ASR mistakes| Mistake | Why it's bad | Fix |
| --- | --- | --- |
| Low confidence threshold while collecting dictated digits | Bot cuts the caller off between groups | Raise confidence and timeout on that slot, reset after. |
| Disabling barge-in globally | Caller can't correct the bot anywhere | Disable only on disclaimer/compliance prompts. |
| Applying a `*:*` default to fix one slot | Changes pacing for the whole bot | Scope the attribute to the specific intent/slot. |
| Setting threshold outside 0.5–0.9 | Request is rejected with an error | Keep it in range. Only `end-timeout-ms` clamps silently. |
| Leaving input window open during a long tool call | Caller sits in dead air | Finish the tool call first or play a filler prompt. |
| Treating an EOT re-prompt as real barge-in | Wrong fix applied to allow-interrupt | Tune the end-of-turn settings instead. |

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

### System prompt for Amazon Connect AI agents

When Amazon Connect AI Agents generate text that will be spoken, add these speech formatting instructions to your agent's system prompt. Copy and paste the block below directly into your prompt configuration.

###### Note

These prompts are templates to get you started. Modify them for your specific use case, tone, and business requirements.

###### Tip

For guidance on optimizing your AI agent prompt for voice performance and latency, see [Prompt engineering best practices for Connect AI agents](agentic-self-service-prompt-best-practices.md "agentic-self-service-prompt-best-practices.md").

**Speech output formatting prompt**

```
## Speech Output Formatting
Everything you output will be spoken aloud by text-to-speech.
Follow these rules:

1. GENERAL FORMATTING
- Use full sentences with normal capitalization. Always end with . ? or !
- Use conventional written forms for numbers, dates, acronyms, symbols.
- Do NOT use markdown, bullet points, headers, bold, raw JSON, emoji,
  or special characters.
- Write plain prose only.

2. SPELLING OUT CODES AND IDS
- For codes or IDs that must be read character-by-character, except for phone numbers, wrap in <spell> tags:
  Example: Your confirmation code is <spell>TKT4829XB</spell>.

3. THINGS TO AVOID
- Do not output bullet points, numbered lists, or structured formatting.
- Do not use asterisks, hashtags, or markdown syntax.
- Do not include internal thoughts, reasoning, or meta-commentary.
- Do not use parentheses, brackets, curly braces, or quotation marks.

4. NATURALNESS
- Respond as if speaking directly to the caller.
- Keep responses concise. Avoid long monologues.
- Use natural transitions ("Let me check that for you.",
  "Here is what I found.").
```

**Polyglot add-on**

If your bot uses a polyglot voice, add the following to your system prompt to enable multi-language responses:

```
## Language Handling
You are connected to a polyglot voice that supports: English, German,
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
| Non-polyglot voice for multi-language | Voice retains primary locale accent | Use a polyglot voice for native pronunciation. |
| Wrapping text in markdown bold or italics | Engine speaks the asterisks aloud | Remove all markdown formatting. |
| Sending malformed or unclosed tags | Engine speaks raw tag text | Validate tags are well-formed with matching brackets. |

### Polyglot voice configuration

#### What are polyglot voices?

Polyglot voices are specially trained to speak multiple languages naturally. Unlike standard voices — which retain the accent of their primary locale — polyglot voices deliver native-sounding pronunciation across their supported languages.

Amazon Connect agentic voice offers the following polyglot voices:

Polyglot voices| Voice | Gender | Supported languages |
| --- | --- | --- |
| Katie (en-US) | Female | English, Spanish, German, French, Hindi, Italian, Japanese, Norwegian, Portuguese (BR), Russian |
| Blake (en-US) | Male | English, Spanish, German, French, Hindi, Italian, Japanese, Norwegian, Portuguese (BR), Russian |
| Brooke (en-US) | Female | English, Spanish, German, French, Hindi, Italian, Japanese, Norwegian, Portuguese (BR), Russian |
| Ronald (en-US) | Male | English, Spanish, German, French, Hindi, Italian, Japanese, Norwegian, Portuguese (BR), Russian |
| Gemma (en-GB) | Female | English (UK), Spanish, German, Hindi, Italian, Portuguese (BR) |

#### Configuration

Polyglot voices are configured at build time using the Set voice block:

- **Engine** — Set to Agentic voice.
- **Language** — Set to the primary language for the interaction.
- **Voice** — Set to one of the voices listed in the above table.

The voice delivers speech in the configured language. To serve multiple languages, create separate contact flows per language, each configured with the appropriate locale for that polyglot voice.

#### Configuring your AI agent for polyglot responses

When using a polyglot voice, your AI agent receives transcriptions from ASR in whatever language the caller speaks. To respond in the caller's language, add language-handling instructions to your system prompt (see the Polyglot add-on above).

**How it works:**

- Caller speaks in Spanish → ASR transcribes in Spanish → Agent sees Spanish text.
- Agent recognizes Spanish is in the supported locale list.
- Agent responds in Spanish → Polyglot voice delivers native-sounding Spanish speech.

**Example exchange:**

```
Caller (transcribed): "Necesito verificar el estado de mi pedido."
Agent: "Con gusto le ayudo. ¿Puede proporcionarme su número de pedido?"
```

#### English code-switching

If the caller uses English terms (brand names, product codes) within a non-English language, keep your response in the caller's language. Embed English terms naturally — there's no need to translate brand names, codes, or identifiers.

```
Caller: "Quiero saber el estado de mi Amazon Prime membership."
Agent: "Claro, voy a revisar su Amazon Prime membership. Un momento por favor."
```

#### Polyglot best practices

**Do:**

- Use a polyglot voice when your use case requires natural-sounding speech in multiple languages.
- Write output text in the target language — the polyglot voice handles pronunciation natively.
- Set the language in your flow configuration to match the expected caller language.
- Use code-switching for short English phrases (brand names, codes) in any voice.
- Add the polyglot language-handling block to your AI agent system prompt.

**Don't:**

- Configure a polyglot voice for a locale it does not support — use a locale-native voice instead.
- Assume all voices sound equally natural across languages.
- Mix multiple languages in a single agent response.
- Translate brand names, product codes, or confirmation numbers — keep them in their original form.

#### Examples

**German conversation with English brand terms:**

```
Ihr Amazon Web Services Konto wurde erfolgreich aktualisiert. Kann ich Ihnen noch mit etwas anderem helfen?
```

English brand names are preserved as-is within the German response.

**Non-polyglot voice speaking another language:**

```
Bonjour, comment puis-je vous aider aujourd'hui?
```

Any agentic voice can speak another language, but non-polyglot voices carry their primary locale accent. For native-sounding French, use a polyglot voice configured for fr\_FR.
