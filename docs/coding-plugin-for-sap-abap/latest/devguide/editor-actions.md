

# Editor actions
<a name="editor-actions"></a>

 AWS Coding Plugin for SAP ABAP ("Coding Plugin") brings Kiro into the editors in Eclipse. You act on code without leaving the editor: run an action on a selection from the context menu, or modify a selection with inline assist.

## Context menu actions
<a name="editor-actions-context-menu"></a>

Select code in an editor, open the context menu, and choose the AWS Coding Plugin submenu. The submenu offers five actions:
+  **Explain** asks Kiro to describe the selected code. The response appears in the chat panel.
+  **Fix**, **Optimize**, and **Refactor** each ask Kiro to rewrite the selection. The proposed change appears as an inline diff in the editor.
+  **Send to Prompt** copies the selection into the chat input so you can add an instruction before submitting.

To use a context menu action:

1. Open an ABAP object or a text file in the editor.

1. Select the code you want to act on.

1. Open the context menu for the selection, choose AWS Coding Plugin, and then choose the action.

## Inline assist
<a name="editor-actions-inline-assist"></a>

Inline assist changes a selection in place, without going to the chat panel.

1. Select the code you want to change.

1. Press  Ctrl Shift I  (macOS:  Cmd Shift I ) to open the inline assist input next to the selection.

1. Type an instruction and press Enter.

1. Review the inline diff, then choose **Accept** or **Reject**.

 **Accept** replaces the selection with the proposed change. **Reject** or Esc restores the original code. If Coding Plugin cannot parse the response into code, it declines the change and restores your selection.

**Note**  
While the inline diff is displayed, the editor shows syntax errors from the diff rendering. These errors clear after you accept or reject the change.