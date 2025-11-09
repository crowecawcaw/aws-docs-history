# Using shortcut keys

While getting inline suggestions from Amazon Q, you can use keyboard shortcuts for common
actions you take, such as initiating Amazon Q or accepting a recommendation.

Choose the integrated development environment (IDE) where you are developing code to see
keyboard shortcuts for your IDE.

Visual Studio Code

| Action                     | Keyboard shortcut                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Manually initiate Amazon Q | MacOS: Option + C<br>Windows: Alt + C                                                                          |
| Accept a recommendation    | Tab                                                                                                            |
| Next recommendation        | Right arrow                                                                                                    |
| Previous recommendation    | Left arrow                                                                                                     |
| Reject a recommendation    | ESC, backspace, or keep typing and the recommendation will disappear as soon as there is a character mismatch. |
| Accept next word           | Cmd + right arrow                                                                                              |

To change keybindings in VS Code, see [Key Bindings for Visual Studio Code](https://code.visualstudio.com/docs/getstarted/keybindings "https://code.visualstudio.com/docs/getstarted/keybindings") on the VS Code website.

###### Note

The inline suggestions toolbar in VS Code is disabled by default. For more information, see [Redesigned inline suggestions toolbar](https://code.visualstudio.com/updates/v1_75#_redesigned-inline-suggestions-toolbar "https://code.visualstudio.com/updates/v1_75#_redesigned-inline-suggestions-toolbar") on the VS Code website.

JetBrains

| Action                     | Keyboard shortcut                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Manually initiate Amazon Q | MacOS: Option + C<br>Windows: Alt + C                                                                          |
| Accept a recommendation    | Tab                                                                                                            |
| Next recommendation        | Right arrow                                                                                                    |
| Previous recommendation    | Left arrow                                                                                                     |
| Reject a recommendation    | ESC, backspace, or keep typing and the recommendation will disappear as soon as there is a character mismatch. |

To change keybindings in IntelliJ, see [IntelliJ IDEA keyboard shortcuts](https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html "https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html") on the JetBrains website.

Eclipse

| Action                     | Keyboard shortcut                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Manually initiate Amazon Q | MacOS: Option + C<br>Windows: Alt + C                                                                          |
| Accept a recommendation    | Tab                                                                                                            |
| Next recommendation        | MacOS: Option + ]<br>Windows: Alt + ]                                                                          |
| Previous recommendation    | MacOS: Option + [<br>Windows: Alt + [                                                                          |
| Reject a recommendation    | ESC, backspace, or keep typing and the recommendation will disappear as soon as there is a character mismatch. |

To change keybindings in Eclipse, see [Changing the key bindings](https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.platform.doc.user%2Ftasks%2Ftkeybindings.htm "https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.platform.doc.user%2Ftasks%2Ftkeybindings.htm") in the Eclipse documentation.

Toolkit for Visual Studio

| Action                                                                                    | Keyboard shortcut                                                                                              |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Manually initiate Amazon Q<br>`AWSToolkit.CodeWhisperer.GetSuggestion` in the keybindings | Windows: Alt + C                                                                                               |
| Accept a recommendation                                                                   | Tab                                                                                                            |
| Next recommendation<br>`Edit.NextSuggestion` in the keybindings                           | Windows: Alt + .                                                                                               |
| Previous recommendation<br>`Edit.PreviousSuggestion` in the keybindings                   | Windows: Alt + ,                                                                                               |
| Reject a recommendation                                                                   | ESC, backspace, or keep typing and the recommendation will disappear as soon as there is a character mismatch. |

See also Microsoft's [Visual Studio default keyboard shortcuts](https://visualstudio.microsoft.com/keyboard-shortcuts.pdf "https://visualstudio.microsoft.com/keyboard-shortcuts.pdf").

To change keybindings in Visual Studio, use Tools -> Options -> Keyboard.

Amazon SageMaker AI

| Action                     | Keyboard shortcut                     |
| -------------------------- | ------------------------------------- |
| Manually initiate Amazon Q | MacOS: Option + C<br>Windows: Alt + C |
| Accept a recommendation    | Tab                                   |
| Next recommendation        | Down arrow                            |
| Previous recommendation    | Up arrow                              |
| Reject a recommendation    | ESC                                   |

JupyterLab

| Action                     | Keyboard shortcut                     |
| -------------------------- | ------------------------------------- |
| Manually initiate Amazon Q | MacOS: Option + C<br>Windows: Alt + C |
| Accept a recommendation    | Tab                                   |
| Next recommendation        | Down arrow                            |
| Previous recommendation    | Up arrow                              |
| Reject a recommendation    | ESC                                   |

AWS Glue Studio Notebook

| Action                     | Keyboard shortcut                     |
| -------------------------- | ------------------------------------- |
| Manually initiate Amazon Q | MacOS: Option + C<br>Windows: Alt + C |
| Accept a recommendation    | Tab                                   |
| Next recommendation        | Down arrow                            |
| Previous recommendation    | Up arrow                              |
| Reject a recommendation    | ESC                                   |

AWS Lambda

| Action                           | Keyboard shortcut                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Manually fetch a code suggestion | MacOS: Option + C<br>Windows: Alt + C                                                                    |
| Accept a suggestion              | Tab                                                                                                      |
| Reject a suggestion              | ESC, Backspace, scroll in any direction, or keep typing and the recommendation automatically disappears. |

To change the key bindings, use the following procedure.

1. While viewing a particular function, choose the gear icon to open the **Preferences** tab.
2. On the **Preferences** tab, select **Keybindings**.
3. In the keybindings search box, enter Amazon Q.

![Keybindings settings in AWS Cloud9 IDE with Amazon CodeWhisperer option highlighted.](images/CWSPR-Lambda-keybinding-settings.png)

AWS Cloud9

| Action                           | Keyboard shortcut                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Manually fetch a code suggestion | MacOS: Option + C<br>Windows: Alt + C                                                                    |
| Accept a suggestion              | Tab                                                                                                      |
| Reject a suggestion              | ESC, Backspace, scroll in any direction, or keep typing and the recommendation automatically disappears. |

1. While viewing a particular environment, choose the gear icon to open the **Preferences** tab.
2. On the **Preferences** tab, select **Keybindings**.
3. In the keybindings search box, enter Amazon Q.
4. In the Keystroke column, double-click the space corresponding to the function you're interested in.
5. Enter the keys that you want to bind the function to.

![AWS Cloud9 interface showing Keybindings settings with options for keyboard mode and custom keybindings.](images/CWSPR-C9-keybinding-settings.png)
