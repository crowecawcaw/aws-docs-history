# Pinning context items

###### Note

Context pinning is currently only available in the VS Code IDE.

Context pinning lets you specify context items that get added to all messages within your chat session.
When you pin a context item, it's automatically included in every message within your current conversation,
eliminating the need to repeatedly type commands like `@workspace`, `@file`,
or `@folder`.

Pinned items can come from two sources: you can manually pin items you frequently reference, or Amazon Q may
automatically add context, (such as your current active file,) to improve response quality. Pinned context items
appear at the top of the text input box of your chat panel, and you have control to remove any context you don't
want included.

To help maintain clear context boundaries, pinned items only apply to your current chat tab. When you open
a new tab, you'll start fresh with only the default pinned context, such as the active file.

## Using pinned context

###### To add pinned context items

1. In your IDE, open the Amazon Q chat panel.
2. After using a context command like `@workspace`, `@file`,
   `@folder`, or `@prompt` in a chat, click the desired context
   to pin it.

Alternatively, you can click the "@ Pin Context" button to view the available options and select
a context to pin. 3. The pinned context will appear in the pinned context area at the top of your chat panel.

### Methods to pin context items

There are three ways to pin context items:

1. Using the @Pin Context menu:
   - Click the "@Pin Context" button in your chat panel.
   - Select the desired context item from the available options.

2. Using the context menu and keyboard shortcut:
   - Type "@" in the chat input to bring up the context menu.
   - Navigate to the desired item.
   - Press Option/Alt + Enter to pin the selected item.

3. Pinning from the input prompt:
   - If you've already typed a context command (like `@workspace`,
     `@file`, `@folder`, or `@prompt`)
     in your input, hover over the context item in your input.
   - Click on the item to pin it.

After pinning, the context item will appear in the pinned context area at the top of your chat's text
input box.

###### To remove pinned context items

- To remove a pinned context item, click the X on the left side of the pill. This works for both
  user-pinned and system-added context items.
