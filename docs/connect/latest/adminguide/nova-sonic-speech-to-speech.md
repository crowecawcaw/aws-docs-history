

# Configure Amazon Nova Sonic Speech-to-Speech
<a name="nova-sonic-speech-to-speech"></a>

You can configure Amazon Nova Sonic as a Speech-to-Speech (S2S) model for a Conversational AI bot locale in Amazon Connect. With Speech-to-Speech, the bot converts customer speech directly into natural, expressive speech responses using Nova Sonic. Amazon Connect continues to manage orchestration, intents, and flows.

## Part 1: Configure Speech-to-Speech for a Bot Locale
<a name="configure-speech-to-speech-bot-locale"></a>

### Prerequisites
<a name="nova-sonic-prerequisites"></a>
+ [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/enable-nextgeneration-amazonconnect.html) is enabled for your instance.
+ A Conversational AI bot exists in Amazon Connect.
+ The locale you want to use with Nova Sonic is already created.
+ You have permissions to edit the bot configuration and build the language.

### Step 1: Open the Speech model configuration
<a name="open-speech-model-configuration"></a>

1. Sign in to the Amazon Connect admin website.

1. In the navigation pane, choose **Conversational AI**, and then choose **Bots**.

1. Choose the bot you want to configure, and then choose the **Configuration** tab.

1. Select the locale you want to configure.

1. In the Speech model section, choose **Edit**.

![Amazon Nova Sonic Speech-to-Speech overview.](http://docs.aws.amazon.com/connect/latest/adminguide/images/nova-sonic-overview.jpg)


### Step 2: Select Speech-to-Speech
<a name="select-speech-to-speech"></a>

In the Speech model modal, open the Model type dropdown and choose **Speech-to-Speech**.

![Model type dropdown showing Speech-to-Speech option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/nova-sonic-model-type.png)


### Step 3: Choose Amazon Nova Sonic
<a name="choose-amazon-nova-sonic"></a>

After selecting Speech-to-Speech, open Voice provider and select **Amazon Nova Sonic**. Then choose **Confirm**.

![Model type dropdown showing Speech-to-Speech option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/nova-sonic-speech-to-speech.png)


### Step 4: Review Speech model status
<a name="review-speech-model-status"></a>

The Speech model card now shows Speech-to-Speech: Amazon Nova Sonic and displays a warning to select a Nova Sonic compatible voice in your Set voice block.

![Speech model modal with Amazon Nova Sonic selected.](http://docs.aws.amazon.com/connect/latest/adminguide/images/nova-sonic-provider-selection.png)


### Step 5: Build and activate the locale
<a name="build-activate-locale"></a>

If the locale shows **Unbuilt changes**, choose **Build language**. The new STT settings become active after a successful build.

## Part 2: Configure a Nova Sonic Compatible Voice in a Flow
<a name="configure-nova-sonic-voice-flow"></a>

After enabling Nova Sonic at the bot level, you must configure a matching Nova Sonic–compatible expressive voice in your flow using the Set voice block.

### Supported Nova Sonic Voices (Launch Set)
<a name="supported-nova-sonic-voices"></a>
+ Matthew (en-US, Masculine)
+ Amy (en-GB, Feminine)
+ Olivia (en-AU, Feminine)
+ Lupe (es-US, Feminine)

### Step 1: Add or open a Set voice block
<a name="add-set-voice-block"></a>

1. Open the target flow in the Flow designer.

1. Search for Set voice in the block library.

1. Drag a Set voice block onto the canvas or open an existing one.

![Speech model card showing Nova Sonic configuration.](http://docs.aws.amazon.com/connect/latest/adminguide/images/nova-sonic-speech-model-card.jpg)


### Step 2: Select Override and Generative speaking style
<a name="select-override-generative"></a>

In Other settings, choose **Override speaking style** and select **Generative** to enable Nova Sonic expressive output.

![Set voice block configuration.](http://docs.aws.amazon.com/connect/latest/adminguide/images/nova-sonic-set-voice-block.png)


### Step 3: Select a Nova Sonic compatible voice
<a name="select-nova-sonic-voice"></a>

1. Set Voice provider to **Amazon**.

1. Under Language, select the locale that corresponds to the voice you want.

1. Under Voice, select one of the Nova Sonic–compatible voices.

![Override speaking style set to Generative.](http://docs.aws.amazon.com/connect/latest/adminguide/images/nova-sonic-generative-style.png)


### Step 4: Review selected voice
<a name="review-selected-voice"></a>

The Set voice block now shows the selected voice and style, such as Voice: Matthew (Generative).

![Set necessary fields for Sonic.](http://docs.aws.amazon.com/connect/latest/adminguide/images/nova-sonic-voice-selection.png)


### Step 5: Save and publish the flow
<a name="save-publish-flow"></a>

Choose **Save**, then **Publish** to activate the configuration.