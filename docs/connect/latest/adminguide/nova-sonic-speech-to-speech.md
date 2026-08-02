# Configure Amazon Nova Sonic Speech-to-Speech

You can configure Amazon Nova Sonic as a Speech-to-Speech (S2S) model for a Conversational AI bot locale in Amazon Connect. With Speech-to-Speech, the bot converts customer speech directly into natural, expressive speech responses using Nova Sonic. Amazon Connect continues to manage orchestration, intents, and flows.

## Part 1: Configure Speech-to-Speech for a Bot Locale

### Prerequisites

- [Amazon Connect Customer](enable-nextgeneration-amazonconnect.md "enable-nextgeneration-amazonconnect.md") is enabled for your instance.
- A Conversational AI bot exists in Amazon Connect.
- The locale you want to use with Nova Sonic is already created.
- You have permissions to edit the bot configuration and build the language.

### Step 1: Open the Speech model configuration

1. Sign in to the Amazon Connect admin website.
2. In the navigation pane, choose **Conversational AI**, and then choose **Bots**.
3. Choose the bot you want to configure, and then choose the **Configuration** tab.
4. Select the locale you want to configure.
5. In the Speech model section, choose **Edit**.

![Amazon Nova Sonic Speech-to-Speech overview.](images/nova-sonic-overview.jpg)

### Step 2: Select Speech-to-Speech

In the Speech model modal, open the Model type dropdown and choose **Speech-to-Speech**.

![Model type dropdown showing Speech-to-Speech option.](images/nova-sonic-model-type.png)

### Step 3: Choose Amazon Nova Sonic

After selecting Speech-to-Speech, open Voice provider and select **Amazon Nova Sonic**. Then choose **Confirm**.

![Model type dropdown showing Speech-to-Speech option.](images/nova-sonic-speech-to-speech.png)

### Step 4: Review Speech model status

The Speech model card now shows Speech-to-Speech: Amazon Nova Sonic and displays a warning to select a Nova Sonic compatible voice in your Set voice block.

![Speech model modal with Amazon Nova Sonic selected.](images/nova-sonic-provider-selection.png)

### Step 5: Build and activate the locale

If the locale shows **Unbuilt changes**, choose **Build language**. The new STT settings become active after a successful build.

## Part 2: Configure a Nova Sonic Compatible Voice in a Flow

After enabling Nova Sonic at the bot level, you must configure a matching Nova Sonic–compatible expressive voice in your flow using the Set voice block.

### Supported Nova Sonic Voices (Launch Set)

- Matthew (en-US, Masculine)
- Amy (en-GB, Feminine)
- Olivia (en-AU, Feminine)
- Lupe (es-US, Feminine)

### Step 1: Add or open a Set voice block

1. Open the target flow in the Flow designer.
2. Search for Set voice in the block library.
3. Drag a Set voice block onto the canvas or open an existing one.

![Speech model card showing Nova Sonic configuration.](images/nova-sonic-speech-model-card.jpg)

### Step 2: Select Override and Generative speaking style

In Other settings, choose **Override speaking style** and select **Generative** to enable Nova Sonic expressive output.

![Set voice block configuration.](images/nova-sonic-set-voice-block.png)

### Step 3: Select a Nova Sonic compatible voice

1. Set Voice provider to **Amazon**.
2. Under Language, select the locale that corresponds to the voice you want.
3. Under Voice, select one of the Nova Sonic–compatible voices.

![Override speaking style set to Generative.](images/nova-sonic-generative-style.png)

### Step 4: Review selected voice

The Set voice block now shows the selected voice and style, such as Voice: Matthew (Generative).

![Set necessary fields for Sonic.](images/nova-sonic-voice-selection.png)

### Step 5: Save and publish the flow

Choose **Save**, then **Publish** to activate the configuration.
