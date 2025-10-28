# Upgrade to the latest Amazon Connect Contact Control Panel

(CCP).

The URL for the latest Contact Control Panel (CCP) ends with
**ccp-v2**

You only need to upgrade to the latest CCP if you're using one the following
options:

- [The URL for your CCP ends with /ccp#](upgrade-browser-ccp.md "upgrade-browser-ccp.md")
- [You use the Amazon Connect Streams API](upgrade-ccp-streams-api.md "upgrade-ccp-streams-api.md"). The
  URL associated with `initCCP()` ends with **/ccp#**
  If you’re still unsure whether your using the latest CCP, go to [Compare the earlier and latest CCP](upgrade-browser-ccp.md#ui-comparison "upgrade-browser-ccp.md#ui-comparison") to see if your CCP looks like
  the latest one.

## Upgrade on your own schedule, before your automatic

upgrade date

To upgrade to the latest CCP before your automatic upgrade date, use the steps in the
following sections:

- [Upgrade your Contact Control Panel (CCP) when your
  CCP URL ends with /ccp#](upgrade-browser-ccp.md "upgrade-browser-ccp.md")
- [Upgrade your Contact Control Panel (CCP) when
  using the Amazon Connect Streams API](upgrade-ccp-streams-api.md "upgrade-ccp-streams-api.md")

## Upgrade later, automatically

If you don't want to upgrade now, you can choose to wait until your scheduled upgrade
date.

Between now and your scheduled upgrade date, we recommend the following change
management steps:

- Compare how the upgraded CCP differs from the earlier one. For side-by-side
  visuals, see [Compare the earlier and latest CCP](upgrade-browser-ccp.md#ui-comparison "upgrade-browser-ccp.md#ui-comparison").
- Upgrade your CCP in a test environment. Use the latest CCP to learn how it's
  different, and to check your configurations.
- Communicate to your agents when the upgrade is going to take place.
- Train your agents to help them get ready.

## Schedule for the automatic upgrade

Your automatic upgrade date is dependent on your usage. Following is the schedule
for when we will start migrating environments:

- <100 weekly minutes - start migrating on August 16, 2024
- <1K weekly minutes - start migrating on August 30, 2024
- <10K weekly minutes - start migrating on September 13, 2024
- <100K weekly minutes - start migrating on October 4, 2024
- > 100K weekly minutes - start migrating on November 1, 2024
