AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Customize your

user
settings

These sections describe the kinds of user settings that you can change in the
**User Settings** pane on the **Preferences** tab:

- [General](#settings-user-change-general "#settings-user-change-general")
- [User interface](#settings-user-change-user-interface "#settings-user-change-user-interface")
- [Collaboration](#settings-user-change-collaboration "#settings-user-change-collaboration")
- [Tree and
  Go Panel](#settings-user-change-tree-and-navigate "#settings-user-change-tree-and-navigate")
- [Find in files](#settings-user-change-find-in-files "#settings-user-change-find-in-files")
- [Meta data](#settings-user-change-meta-data "#settings-user-change-meta-data")
- [Watchers](#settings-user-change-watchers "#settings-user-change-watchers")
- [Terminal](#settings-user-change-terminal "#settings-user-change-terminal")
- [Output](#settings-user-change-output "#settings-user-change-output")
- [Code editor
  (Ace)](#settings-user-change-code-editor-ace "#settings-user-change-code-editor-ace")
- [Input](#settings-user-change-input "#settings-user-change-input")
- [Hints and warnings](#settings-user-change-hints-and-warnings "#settings-user-change-hints-and-warnings")
- [Run and debug](#settings-user-change-run-and-debug "#settings-user-change-run-and-debug")
- [Preview](#settings-user-change-preview "#settings-user-change-preview")
- [Build](#settings-user-change-build "#settings-user-change-build")

## General

\***\*Reset to Factory Settings\*\***

If you choose the **Reset to Default** button, AWS Cloud9 resets all
of your user settings to the AWS Cloud9 default user settings. To confirm, choose
**Reset settings**.

###### Warning

You can't undo this action.

\***\*Warn Before Exiting\*\***

Whenever you attempt to close the IDE, AWS Cloud9 asks you to confirm that you want to
exit.

## User interface

\***\*Enable UI Animations\*\***

AWS Cloud9 uses animations in the IDE.

\***\*Use an Asterisk (\*) to Mark Changed Tabs\*\***

AWS Cloud9 adds an asterisk (**\***) to tabs that have changes but
their content isn't saved yet.

\***\*Display Title of Active Tab as Browser Title\*\***

AWS Cloud9 changes the title of the associated web browser tab to the title of the
active tab (for example, **Untitled1**,
**hello.js**, **Terminal**,
**Preferences**).

\***\*Automatically Close Empty Panes\*\***

Whenever you reload an environment, AWS Cloud9 automatically closes any panes it considers
are empty.

\***\*Environment Files Icon and Selection Style\*\***

The icon AWS Cloud9 uses for environment files, and the file selection behaviors AWS Cloud9
uses.

Valid values include:

- **Default** – AWS Cloud9 uses default icons and default file
  selection behaviors.
- **Alternative** – AWS Cloud9 uses alternative icons and
  alternative file selection behaviors.

## Collaboration

\***\*Disable collaboration security warning\*\***

When a read/write member is added to an environment, AWS Cloud9 doesn't display the security
warning dialog box.

\***\*Show Authorship Info\*\***

AWS Cloud9 underlines text that's entered by other environment members with related
highlights in the gutter.

## Tree and

Go panel

\***\*Scope Go to Anything to Favorites\*\***

**Go to File** in the **Go** window displays
results scoped only to **Favorites** in the
**Environment** window.

\***\*Enable Preview on Tree Selection\*\***

AWS Cloud9 displays the chosen file with a single click instead of a double
click.

\***\*Hidden File Pattern\*\***

The types of files for AWS Cloud9 to treat as hidden.

\***\*Reveal Active File in Project Tree\*\***

AWS Cloud9 highlights the active file in the **Environment**
window.

\***\*Download Files As\*\***

The behavior for AWS Cloud9 to use when downloading files.

Valid values include the following:

- **auto** – AWS Cloud9 downloads files without
  modification.
- **tar.gz** – AWS Cloud9 downloads files as compressed
  TAR files.
- **zip** – AWS Cloud9 downloads files as .zip
  files.

## Find in Files

\***\*Search In This Path When 'Project' Is Selected\*\***

On the find in files bar, when **Project** is selected for the
search scope, the path to search in.

\***\*Show Full Path in Results\*\***

Displays the full path to each matching file in the **Search
Results** tab.

\***\*Clear Results Before Each Search\*\***

Clears the **Search Results** tab of the results of any previous
searches before the current search begins.

\***\*Scroll Down as Search Results Come In\*\***

Scrolls the **Search Results** tab to the bottom of the list of
results as search results are identified.

\***\*Open Files when Navigating Results with (Up and Down)\*\***

As the up and down arrow keys are pressed in the **Search
Results** tab within the list of results, opens each matching file.

## Meta Data

\***\*Maximum of Undo Stack Items in Meta Data\*\***

The maximum number of items that AWS Cloud9 keeps in its list of actions that can be
undone.

## Watchers

\***\*Auto-Merge Files When a Conflict Occurs\*\***

AWS Cloud9 attempts to automatically merge files whenever a merge conflict
happens.

## Terminal

\***\*Text Color\*\***

The color of text in **Terminal** tabs.

\***\*Background Color\*\***

The background color in **Terminal** tabs.

\***\*Selection Color\*\***

The color of selected text in **Terminal** tabs.

\***\*Font Family\*\***

The text font style in **Terminal** tabs.

\***\*Font Size\*\***

The size of text in **Terminal** tabs.

\***\*Antialiased Fonts\*\***

AWS Cloud9 attempts to smooth the display of text in **Terminal**
tabs.

\***\*Blinking Cursor\*\***

AWS Cloud9 continuously blinks the cursor in **Terminal** tabs.

\***\*Scrollback\*\***

The number of lines that you can scroll up or back through in
**Terminal** tabs.

\***\*Use AWS Cloud9 as the Default Editor\*\***

Uses AWS Cloud9 as the default text editor.

## Output

\***\*Text Color\*\***

The color of text in tabs that display output.

\***\*Background Color\*\***

The background color of text in tabs that display output.

\***\*Selection Color\*\***

The color of selected text in tabs that display output.

\***\*Warn Before Closing Unnamed Configuration\*\***

AWS Cloud9 prompts you to save any unsaved configuration tab before it's closed.

\***\*Preserve log between runs\*\***

AWS Cloud9 keeps a log of all attempted runs.

## Code editor

(Ace)

\***\*Auto-pair Brackets, Quotes, etc.\*\***

AWS Cloud9 attempts to add a matching closing character for each related starting
character that is typed in editor tabs, such as for brackets, quotation marks, and
braces.

\***\*Wrap Selection with Brackets, Quote, etc.\*\***

AWS Cloud9 attempts to insert a matching closing character at the end of text in editor
tabs after the text is selected and a related started character is typed, such as for
brackets, quotation marks, and braces.

\***\*Code Folding\*\***

AWS Cloud9 attempts to show, expand, hide, or collapse sections of code in editor tabs
according to related code syntax rules.

\***\*Fade Fold Widgets\*\***

AWS Cloud9 displays code folding controls in the gutter whenever you pause the mouse
over those controls in editor tabs.

\***\*Copy With Empty Selection\*\***

AWS Cloud9 enables you to Copy and or Cut text and this option determines if empty text will be copied to the clipboard.

\***\*Full Line Selection\*\***

AWS Cloud9 selects an entire line that's triple-clicked in editor tabs.

\***\*Highlight Active Line\*\***

AWS Cloud9 highlights the entire active line in editor tabs.

\***\*Highlight Gutter Line\*\***

AWS Cloud9 highlights the location in the gutter next to the active line in editor
tabs.

\***\*Show Invisible Characters\*\***

AWS Cloud9 displays what it considers to be invisible characters in editor tabs, for
example, carriage returns and line feeds, spaces, and tabs.

\***\*Show Gutter\*\***

AWS Cloud9 displays the gutter.

\***\*Show Line Numbers\*\***

The behavior for displaying line numbers in the gutter.

Valid values include the following:

- **Normal** – Display line numbers.
- **Relative** – Display line numbers relative to the active
  line.
- **None** – Hide line numbers.

\***\*Show Indent Guides\*\***

AWS Cloud9 displays guides to more easily visualize indented text in editor
tabs.

\***\*Highlight Selected Word\*\***

AWS Cloud9 selects an entire word that's double-clicked in an editor tab.

\***\*Scroll Past the End of the Document\*\***

The behavior for allowing the user to scroll past the end of the current file in
editor tabs.

Valid values include the following:

- **Off** – Do not allow any scrolling past the end of the
  current file.
- **Half Editor Height** – Allow scrolling past the end of
  the current file to up to half the editor's screen height.
- **Full Editor Height** – Allow scrolling past the end of
  the current file to up to the editor's full screen height.

\***\*Animate Scrolling\*\***

AWS Cloud9 applies animation behaviors during scrolling actions in editor tabs.

\***\*Font Family\*\***

The style of font to use in editor tabs.

\***\*Font Size\*\***

The size of the font to use in editor tabs.

\***\*Antialiased Fonts\*\***

AWS Cloud9 attempts to smooth the display of text in editor tabs.

\***\*Show Print Margin\*\***

Displays a vertical line in editor tabs after the specified character
location.

\***\*Mouse Scroll Speed\*\***

The relative speed of mouse scrolling in editor tabs. Larger values result in
faster scrolling.

\***\*Cursor Style\*\***

The style and behavior of the pointer in editor tabs.

Valid values include:

- **Ace** – Display the pointer as a vertical bar that is
  relatively wider than **Slim**.
- **Slim** – Display the pointer as a relatively slim
  vertical bar.
- **Smooth** – Display the pointer as a vertical bar that is
  relatively wider than **Slim** and that blinks more smoothly than
  **Slim**.
- **Smooth and Slim** – Display the pointer as a relatively
  slim vertical bar that blinks more smoothly than **Slim**.
- **Wide** – Display the pointer as a relatively wide
  vertical bar.

**Merge Undo Deltas**

- **Always** – Allow merge conflicts to be reverted.
- **Never** – Never allow merge conflicts to be reverted.
- **Timed** – Allow merge conflicts to be reverted after a
  specific period.

\***\*Enable Wrapping For New Documents\*\***

AWS Cloud9 wraps code in new files.

## Input

\***\*Complete As You Type\*\***

AWS Cloud9 attempts to display possible text completions as you type.

\***\*Complete On Enter\*\***

AWS Cloud9 attempts to display possible text completions after you press
**Enter**.

\***\*Highlight Variable Under Cursor\*\***

AWS Cloud9 highlights all references in code to the selected variable.

\***\*Use Cmd-Click for Jump to Definition\*\***

AWS Cloud9 goes to any original definition for code that's selected while pressing and
holding **Command** for Mac or **Ctrl** for
Windows.

## Hints and warnings

\***\*Enable Hints and Warnings\*\***

AWS Cloud9 displays applicable hint and warning messages.

\***\*Show Available Quick Fixes on Click\*\***

AWS Cloud9 displays a tool tip with refactoring suggestions when you click on a keyword within your code.

\***\*Ignore Messages Matching Regex\*\***

AWS Cloud9 doesn't display any messages that match the specified regular expression.
For more information, see [Writing a regular expression pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern") in the _JavaScript Regular
Expressions_ topic on the Mozilla Developer Network.

## Run and debug

\***\*Save All Unsaved Tabs Before Running\*\***

Before running the associated code, AWS Cloud9 attempts to save all unsaved files with
open tabs.

## Preview

\***\*Preview Running Apps\*\***

AWS Cloud9 attempts to display a preview of the output for the code in the active tab
whenever the **Preview** button is chosen.

\***\*Default Previewer\*\***

The format AWS Cloud9 uses to preview code output.

Valid values include:

- **Raw** – Attempt to display code output in a plain
  format.
- **Browser** – Attempt to display code output in a format
  that's preferred for web browsers.

\***\*When Saving Reload Previewer\*\***

The behavior AWS Cloud9 uses for previewing code output whenever a code file is
saved.

Valid values include the following:

- **Only on Ctrl-Enter** – Attempt to preview code output
  whenever **Ctrl+Enter** is pressed for the current code
  tab.
- **Always** – Attempt to preview code output whenever a
  code file is saved.

## Build

\***\*Automatically Build Supported Files\*\***

AWS Cloud9 attempts to automatically build the current code if a build action is
started and the code is in a supported format.
