**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How Shield Advanced manages automatic mitigation

The topics in this section describe how Shield Advanced handles your configuration changes for
automatic application layer DDoS mitigation and how it handles DDoS attacks when automatic mitigation
is enabled.

###### Topics

- [How
  Shield Advanced responds to DDoS attacks with automatic mitigation](#ddos-automatic-app-layer-response-ddos-attack "#ddos-automatic-app-layer-response-ddos-attack")
- [How Shield Advanced manages the rule
  action setting](#ddos-automatic-app-layer-response-rule-action "#ddos-automatic-app-layer-response-rule-action")
- [How
  Shield Advanced manages mitigations when an attack subsides](#ddos-automatic-app-layer-response-after-attack "#ddos-automatic-app-layer-response-after-attack")
- [What happens
  when you disable automatic mitigation](#ddos-automatic-app-layer-response-disable "#ddos-automatic-app-layer-response-disable")

## How

Shield Advanced responds to DDoS attacks with automatic mitigation

When you have automatic mitigation enabled on a protected resource, the
rate-based rule `ShieldKnownOffenderIPRateBasedRule` in the Shield Advanced
rule group responds automatically to elevated traffic volumes from known DDoS
sources. This rate-limiting is applied quickly and acts as a front-line defense
against attacks.

When Shield Advanced detects an attack, it does the following:

1. Attempts to identify an attack signature that isolates the attack traffic from the
   normal traffic to your application. The goal is to produce high quality
   DDoS mitigation rules that, when placed, affect only the attack traffic
   and don't impact normal traffic to your application.
2. Evaluates the identified attack signature against the historical
   traffic patterns for the resource that's under attack as well as for any
   other resource that's associated with the same web ACL. Shield Advanced does
   this before it deploys any rules in response to the event.

Depending on the evaluation results, Shield Advanced does one of the following:

    * If Shield Advanced determines that the attack signature isolates only the traffic that is
     involved in the DDoS attack, it implements the signature in
     AWS WAF rules in the Shield Advanced mitigation rule group in the web
     ACL. Shield Advanced gives these rules the action setting that you've
     configured for the resource's automatic mitigation - either
     Count or Block.
    * Otherwise, Shield Advanced doesn't place a mitigation.

Throughout an attack, Shield Advanced sends the same notifications and provides the same
event information as for basic Shield Advanced application layer protections. You can see
the information about events and DDoS attacks, and about any Shield Advanced mitigations
for attacks, in the Shield Advanced event console. For information, see [Visibility into DDoS events with Shield Advanced](ddos-viewing-events.md "ddos-viewing-events.md").

If you've configured automatic mitigation to use the Block rule action
and you experience false positives from the mitigation rules that Shield Advanced has
deployed, you can change the rule action to Count. For information about
how to this, see [Changing the action used for automatic application layer DDoS mitigation](change-action-of-automatic-app-layer-response.md "change-action-of-automatic-app-layer-response.md").

## How Shield Advanced manages the rule

action setting

You can set the rule action for your automatic mitigations to Block or
Count.

When you change the automatic mitigation rule action setting for a
protected resource, Shield Advanced updates all rule settings for the resource. It
updates any rules that are currently in place for the resource in the Shield Advanced
rule group and it uses the new action setting when it creates new rules.

For resources that use the same web ACL, if you specify different actions, Shield Advanced uses
the Block action setting for the rule group's rate-based rule
`ShieldKnownOffenderIPRateBasedRule`. Shield Advanced creates and
manages other rules in the rule group on behalf of a specific protected
resource, and uses the action setting that you've specified for the resource.
All rules in the Shield Advanced rule group in a web ACL are applied to the web traffic
of all of the associated resources.

Changing the action setting can take a few seconds to propagate. During this
time, you might see the old setting in some places where the rule group is in
use, and the new setting in other places.

You can change the rule action setting for your automatic mitigation
configuration in the events page of the console, and through the application layer
configuration page. For information about the events page, see [Responding to DDoS events in AWS](ddos-responding.md "ddos-responding.md"). For information
about the configuration page, see [Configure application layer DDoS protections](manage-protection.md#configure-app-layer-protection "manage-protection.md#configure-app-layer-protection").

## How

Shield Advanced manages mitigations when an attack subsides

When Shield Advanced determines that mitigation rules that were deployed for a particular attack
are no longer needed, it removes them from the Shield Advanced mitigation rule group.

The removal of mitigating rules won't necessarily coincide with the end of an
attack. Shield Advanced monitors patterns of attack that it detects on your protected
resources. It might proactively defend against the recurrence of an attack
with a specific signature by keeping the rules that it has deployed against the initial occurrence of that attack in place.
As needed, Shield Advanced increases the window of time that it keeps rules in
place. This way, Shield Advanced might mitigate repeated attacks with a specific signature before they impact your
protected resources.

Shield Advanced never removes the rate-based rule
`ShieldKnownOffenderIPRateBasedRule`, which limits the volume of
requests from IP addresses that are known to be sources of DDoS attacks.

## What happens

when you disable automatic mitigation

Shield Advanced does the following when you disable automatic mitigation for a
resource:

- **Stops automatically responding to DDoS
  attacks** – Shield Advanced discontinues its automatic response
  activities for the resource.
- **Removes unneeded rules from the Shield Advanced rule
  group** – If Shield Advanced is maintaining any rules in its
  managed rule group on behalf of the protected resource, it removes them.
- **Removes the Shield Advanced rule group, if it's no longer
  in use** – If the web ACL that you have associated with
  the resource isn't associated to any other resource that has
  automatic mitigation enabled, Shield Advanced removes its rule group
  rule from the web ACL.
