

# Screens
<a name="companion-app-screens"></a>


| Tab | Contents | 
| --- | --- | 
| Home | Vehicle summary and quick actions, including claiming an assigned vehicle when the CMS main API is configured. | 
| Vehicle | Live telemetry, vehicle state, trip history, health detail, and the remote controls sheet. | 
| Alerts | Real-time driver signals — diagnostic trouble codes, safety events, and triage outcomes. | 
| AVX Cards | Open Findings from the owner’s Tier 2 agents — health, coverage, energy, and mobility position — with approve, dismiss, and drill-down affordances. Actions in progress are tracked here until they complete or fail. | 
| Service / Dealer | Service history and appointment booking. Labelled per tenant segment, as described above. | 
| Buy | The Acquire journey. Present only for segments whose configuration enables it. | 
| Account | Profile, settings, and notification consent. | 

The assistant is not a tab. It opens as a full-screen presentation from anywhere in the app, so a conversation can start in the context the driver is already in — and the Service tab’s **Book Service** action opens it with a primed prompt, so the conversation begins as though the driver had asked for it out loud.

iPhone’s tab bar shows at most five items and moves the remainder into a system overflow list. Buy occupies a visible slot and Account is the tab allowed to overflow, which is a product decision rather than an accident. One consequence is worth recording because it cost a silent failure: a tab inside the overflow list does not update SwiftUI’s selection binding, so any screen whose content depends on observing a selection change renders nothing there, with no error. Screens in overflow-eligible slots therefore render their content directly rather than presenting it in response to becoming selected.

Layout branches on a named layout context derived once at the view root and injected through the environment, rather than on raw size-class values — which keeps layout decisions explicit and snapshot-testable.

The screenshots below show the app signed in as a Meridian Motors driver.

![Sign-in screen: the Meridian Motors wordmark above an email and password form, a Remember me toggle, a Forgot password link, and Help, Contact Us, Legal and Privacy links](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/ca-screens/ios-01-signin.png)


![Home tab: a greeting with the driver’s city, a critical vehicle alert banner, an upgrade offer card based on the driver’s 2025 Meridian Azimuth, and the vehicle card with its plate, color and connection status](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/ca-screens/ios-02-main.png)


![Home tab scrolled to the vehicle summary: quick actions for Controls, Health and Book service, then odometer, fuel, speed and trips tiles and the vehicle health card](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/ca-screens/ios-03-vehicle-detail.png)


![Assistant: the connected assistant header with the driver, vehicle and odometer, a Ready state, and a prompt to type a message or tap the microphone](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/ca-screens/ios-04-assistant.png)
