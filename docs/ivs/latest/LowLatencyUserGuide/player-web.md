# IVS Player SDK: Web Guide

The Amazon Interactive Video Service (IVS) Web player SDK can be integrated with [player frameworks](#web-framework-integrations "#web-framework-integrations") like Video.js or used
standalone on top of an HTML `<video>` element.

**Latest version of Web player:** 1.46.0 ([Release
Notes](release-notes.md#oct23-25-player-web-ll "release-notes.md#oct23-25-player-web-ll"))

**Reference documentation:** For information on the most
important methods available in the Amazon IVS Web player, see the reference documentation at
[https://aws.github.io/amazon-ivs-player-docs/1.46.0/web/](https://aws.github.io/amazon-ivs-player-docs/1.46.0/web/ "https://aws.github.io/amazon-ivs-player-docs/1.46.0/web/").

### Framework Integrations

The Amazon IVS Web player SDK is designed to be easy to integrate with your
framework of choice. We offer an official Video.js integration (“tech,” in Video.js
jargon).

The following is a brief comparison of the Web players we offer:

| Player Type                                                                         | Description                                                                                                | UI                                                                                           | Plugins                                                                              |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Amazon IVS Web player SDK                                                           | A lightweight and customizable option for developers who want more control.                                | No                                                                                           | No                                                                                   |
| [Amazon IVS Player Tech for Video.js](player-videojs.md "player-videojs.md")        | A full-featured option, which may be appropriate if you already use Video.js and want a turnkey solution.  | Yes([Video.js Skins](https://videojs.com/guides/skins/ "https://videojs.com/guides/skins/")) | Yes([Video.js Plugins](https://videojs.com/plugins/ "https://videojs.com/plugins/")) |
| [Amazon IVS Player Provider for JW Player](player-jwplayer.md "player-jwplayer.md") | A full-featured option, which may be appropriate if you already use JW Player and want a turnkey solution. | Yes                                                                                          | N/A                                                                                  |
