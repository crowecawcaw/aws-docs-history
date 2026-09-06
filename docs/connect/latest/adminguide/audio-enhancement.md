

# Enable Audio Enhancement for agents in Connect Customer
<a name="audio-enhancement"></a>

Audio Enhancement improves audio quality and reliability on the agent's side by reducing background noise and isolating the agent's voice during calls. This feature includes two enhancement modes: noise suppression and voice isolation.

## How Audio Enhancement works
<a name="audio-enhancement-how-it-works"></a>

Audio Enhancement processes audio in real-time and improves the audio quality perceived by the end-customer in one of two modes:
+ **Noise suppression** - Reduces background noise from the agent's environment.
+ **Voice isolation** - Reduces background noise and isolates the agent's voice when multiple people are speaking in the contact center environment.

The feature automatically applies to incoming and outgoing calls once enabled for an agent.

## Prerequisites
<a name="audio-enhancement-prerequisites"></a>

Before enabling Audio Enhancement, ensure the agent environment meets these requirements:
+ **CPU** - Minimum 4-core CPU or 4 vCPU for virtual machines
+ **Memory** - Follow CCP hardware recommendations (see [Agent headset and workstation requirements for using the Contact Control Panel (CCP)](ccp-agent-hardware.md))
+ **Phone type** - Softphone users only
+ **Infrastructure** - Native, embedded, custom, and [VDI client with local browser access](https://docs.aws.amazon.com/connect/latest/adminguide/scenario-deployment-approaches.html#vdi-with-browser) are supported; [VDI with Amazon Connect audio optimization](https://docs.aws.amazon.com/connect/latest/adminguide/scenario-deployment-approaches.html#vdi-citrix) is not supported
+ **Custom CCP using Connect Customer APIs** – If you are using Connect Customer APIs to build your own custom CCP, you must use [Connect Customer Streams JS version 2.25.2](https://github.com/amazon-connect/amazon-connect-streams/releases/tag/2.25.2) or later

## Enable Audio Enhancement for agents
<a name="audio-enhancement-enable"></a>

Audio Enhancement is disabled by default. Administrators must enable it for specific agents through user management settings.

**To enable Audio Enhancement**

1. In the Connect Customer admin website, choose **Users** and then choose **User management**.

1. Review the **Audio Enhancement** column to see current settings for each agent.

1. Select one or more agents, then choose **Edit**.

1. Make sure to set **Phone type** to **Soft phone**.

1. In the user edit panel, expand the **Audio Enhancement** dropdown and select your preferred mode:
   + **Isolate Agent's Voice** – Suppresses background noise and isolates the agent's voice. This mode should only be enabled if the agent uses a wired headset. If you're not sure whether your agents will consistently use a wired headset, we recommend configuring 'Suppress Background Noise' mode instead.
   + **Suppress Background Noise** – Suppresses background noise. You can use this mode with any headset configuration, including wired headsets, wireless headsets, or no headset.
   + **No enhancement** – Disables Audio Enhancement capability. This is the default setting.
**Important**  
Voice isolation should only be used with a wired headset.  
![The Audio Enhancement dropdown in the user edit panel.](http://docs.aws.amazon.com/connect/latest/adminguide/images/admin-website-voice-enhancement.png)

1. Choose **Save**.

**Important**  
Changes to Audio Enhancement settings take effect on the agent's next call. Current ongoing calls are not affected.

## Allow agents to control their Audio Enhancement settings
<a name="audio-enhancement-agent-control"></a>

To let agents adjust their own Audio Enhancement settings during work sessions, you must enable the appropriate security profile permission.

**To allow agents to control Audio Enhancement**

1. In the Connect Customer admin website, choose **Users**, **Security profiles**.

1. Select the security profile assigned to your agents.

1. Expand **Contact Control Panel (CCP)** permissions.

1. Select **Audio device settings**.  
![The Audio device settings permission in the Contact Control Panel (CCP) section of the security profile.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_audio_device_settings.png)

1. Choose **Save**.

After enabling this permission, agents will see Audio Enhancement controls in their CCP.

![The Audio Enhancement controls in the CCP.](http://docs.aws.amazon.com/connect/latest/adminguide/images/ccp-audio-enhancement-dropdown.png)


**Important notes about agent control**  
If you don't want your agents to adjust the Audio Enhancement settings, do not enable the **Audio device settings** security profile permission for those agents.
Audio Enhancement changes take effect on the agent's next call, not during ongoing calls. However, changing the microphone device immediately applies the latest configured settings, even during active calls.
The system doesn't automatically adjust settings when agents change headsets - agents must manually update their Audio Enhancement mode.
When both administrators and agents can control Audio Enhancement, the most recent change takes effect.

## Set up Audio Enhancement mode through Connect Customer APIs
<a name="audio-enhancement-api"></a>

If you are using the Connect Customer APIs, you can set the Audio Enhancement mode by including the [VoiceEnhancementConfigs](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateUser.html#connect-CreateUser-request-VoiceEnhancementConfigs) parameter in the [CreateUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateUser.html) or [UpdateUserConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserConfig.html) requests.

For example, the body of the `UpdateUserConfig` request should be:

```
POST /users/InstanceId/UserId/config HTTP/1.1
Content-type: application/json
{
   ...,
   "VoiceEnhancementConfigs": [ 
      { 
         "Channel": "VOICE",
         "VoiceEnhancementMode": "VOICE_ISOLATION"
      }
   ]
}
```

For both endpoints, the accepted values of `VoiceEnhancementMode` are `VOICE_ISOLATION`, `NOISE_SUPPRESSION`, or `NONE`.

## Set up Audio Enhancement mode for custom CCP
<a name="audio-enhancement-custom-ccp"></a>

If you are using a custom CCP with the Connect Customer Streams API, you can set the Audio Enhancement mode in either of the following ways:
+ **Using agent.setVoiceEnhancementMode API**

  ```
  agent.setVoiceEnhancementMode("VOICE_ISOLATION");
  ```
+ **Using agent.setConfiguration API**

  ```
  const configuration = agent.getConfiguration();
  agent.setConfiguration({
    ...configuration,
    voiceEnhancementMode: "NOISE_SUPPRESSION",
  });
  ```
+ **Using the ConnectSDK** – Reference the [setVoiceEnhancementMode()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-setvoiceenhancementmode.html) and [getVoiceEnhancementMode()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-getvoiceenhancementmode.html) methods in the Voice API.

In all cases, the accepted values are `VOICE_ISOLATION`, `NOISE_SUPPRESSION`, or `NONE`. After the mode is set, Connect Customer Streams will apply the selected Audio Enhancement.

## Troubleshooting
<a name="audio-enhancement-troubleshooting"></a>

If your customers report any audio quality issues:

1. Please make sure that Voice Isolation mode is enabled only if the agent is using a wired headset.

1. Confirm the agent's device meets minimum CPU requirements.

1. Check that the agent is using a supported CCP configuration.

If you require additional support, contact AWS Support and include:
+ The affected contact IDs and AWS account ID
+ Call recordings for affected contacts
+ Confirmation of the agent's audio setup and selected enhancement mode

## Related topics
<a name="audio-enhancement-related"></a>
+ [Agent headset and workstation requirements for using the Contact Control Panel (CCP)](ccp-agent-hardware.md)
+ [Security profiles for Connect Customer and Contact Control Panel (CCP) access](connect-security-profiles.md)
+ [Provide agents with access to the Connect Customer Contact Control Panel (CCP)](amazon-connect-contact-control-panel.md)
+ [Set up your contact center in Connect Customer](amazon-connect-contact-centers.md)