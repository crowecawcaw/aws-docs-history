# Using shortcut keys in chat with Amazon Q Developer

Amazon Q provides keyboard shortcuts to help you interact with the agentic chat interface efficiently. Using keyboard shortcuts can help you maintain your workflow without switching between keyboard and mouse.

###### Note

Keyboard shortcuts are only currently available in the Visual Studio Code IDE.

## Keyboard shortcuts

| Keyboard shortcuts for Amazon Q chat | Action                                                                                                  | Visual Studio Code Shortcut |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------- | --------------------------- |
| Run command                          | Shift + Cmd + Enter (Mac)<br>Shift + Ctrl + Enter (Windows)<br>Shift + Meta + Enter (Linux)             |
| Reject command                       | Shift + Cmd + R (Mac)<br>Shift + Ctrl + R (Windows)<br>Shift + Meta + R (Linux)                         |
| Stop generation                      | Shift + Cmd + Backspace (Mac)<br>Shift + Ctrl + Backspace (Windows)<br>Shift + Meta + Backspace (Linux) |

## Customizing keyboard shortcuts

Shortcuts can be modified through the standard keyboard shortcut customization interface in your IDE. Amazon Q uses each IDE's native shortcut system, so any changes you make will be reflected in the Amazon Q interface. The shortcuts shown in tooltips and UI elements will automatically update to match your customized key mappings.

## Shortcut discoverability

Amazon Q provides several ways to discover keyboard shortcuts:

- **Tooltips**: Hover over the Run command button, Reject command button, or Stop button to see the current keyboard shortcut
- **Settings**: View all shortcuts in your IDE's keyboard shortcut customization interface

## Shortcut behavior

- Keyboard shortcuts for agentic chat are only active when your focus is in the Amazon Q chat panel
- This prevents conflicts with existing IDE keybindings
- If you modify a shortcut, you may need to refresh your IDE for the changes to be reflected in tooltips
