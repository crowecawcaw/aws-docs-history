AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with Keybindings in the
 AWS Cloud9
 IDE

*Keybindings* define your shortcut key combinations. Keybindings apply
 across each AWS Cloud9 development environment that is associated with your IAM user. As you make changes to your
 keybindings, AWS Cloud9 pushes those changes to the cloud, and associates them with your
 IAM user. AWS Cloud9 also continually scans the cloud for changes to keybindings that are
 associated with your IAM user, and applies those changes to your current environment.

You can share your keybindings with other users.


* [View or Change Your Keybindings](#settings-keybindings-view "#settings-keybindings-view")
* [Share Your Keybindings with Another User](#settings-keybindings-share "#settings-keybindings-share")
* [Change Your Keyboard Mode](#settings-keybindings-mode "#settings-keybindings-mode")
* [Change Your Operating System Keybindings](#settings-keybindings-os "#settings-keybindings-os")
* [Change Specific Keybindings](#settings-keybindings-change "#settings-keybindings-change")
* [Remove All of Your Custom Keybindings](#settings-keybindings-reset "#settings-keybindings-reset")

## View or change your Keybindings



1. On the menu bar, choose **AWS Cloud9**, **Preferences**.
2. To view your keybindings across each environment of yours, on the **Preferences** tab, in the
side navigation pane, choose **Keybindings**.
3. To change your keybindings across each environment of yours, in the
 **Keybindings** pane, change the settings that you want.
4. To apply your changes to any environment, simply open that environment. If that environment is
already open, refresh the web browser tab for that environment.

For more information, see the following:



* [MacOS Default Keybindings Reference](keybindings-default-apple-osx.md "keybindings-default-apple-osx.md")
* [MacOS Vim Keybindings Reference](keybindings-vim-apple-osx.md "keybindings-vim-apple-osx.md")
* [MacOS Emacs Keybindings Reference](keybindings-emacs-apple-osx.md "keybindings-emacs-apple-osx.md")
* [MacOS Sublime Keybindings Reference](keybindings-sublime-apple-osx.md "keybindings-sublime-apple-osx.md")
* [Windows / Linux Default Keybindings Reference](keybindings-default-windows-linux.md "keybindings-default-windows-linux.md")
* [Windows / Linux Vim Keybindings Reference](keybindings-vim-windows-linux.md "keybindings-vim-windows-linux.md")
* [Windows / Linux Emacs Keybindings Reference](keybindings-emacs-windows-linux.md "keybindings-emacs-windows-linux.md")
* [Windows / Linux Sublime Keybindings Reference](keybindings-sublime-windows-linux.md "keybindings-sublime-windows-linux.md")

## Share your Keybindings with another user



1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose **AWS Cloud9, Open Your Keymap**.
2. In the source environment, copy the contents of the
 **keybindings.settings** tab that's displayed.
3. In the target environment, overwrite the contents of the **keybindings.settings** tab with the copied contents from the source environment.
4. In the target environment, save the **keybindings.settings** tab.

## Change your Keyboard mode


You can change the keyboard mode that the AWS Cloud9 IDE uses for interacting with text in the editor across
each environment associated with your IAM user.



1. On the menu bar, choose **AWS Cloud9**, **Preferences**.
2. On the **Preferences** tab, in the side navigation pane, choose **Keybindings**.
3. For **Keyboard Mode**, choose one of these keyboard modes:




	* **Default** to use a set of default keybindings.
	* **Vim** to use Vim mode. For more information, see the [Vim help files](https://vimhelp.appspot.com/ "https://vimhelp.appspot.com/") website.
	* **Emacs** to use Emacs mode. For more information, see [The Emacs Editor](https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html "https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html") on the GNU Operating System website.
	* **Sublime** to use Sublime mode. For more information, see the [Sublime Text Documentation](https://www.sublimetext.com/docs/3/ "https://www.sublimetext.com/docs/3/") website.

## Change your operating system Keybindings


You can change the set of operating system keybindings that the AWS Cloud9 IDE recognizes
 across each environment associated with your IAM user.



1. On the menu bar, choose **AWS Cloud9**, **Preferences**.
2. On the **Preferences** tab, in the side navigation pane, choose **Keybindings**.
3. For **Operating System**, choose one of these operating systems:




	* **Auto** for the AWS Cloud9 IDE to attempt to detect which set of operating system keybindings to use.
	* **MacOS** for the AWS Cloud9 IDE to use the keybindings that are
	 listed in the macOS format.
	* **Windows / Linux** for the AWS Cloud9 IDE to use the keybindings
	 that are listed in the Windows and Linux formats.

## Change specific Keybindings


You can change individual keybindings across each environment that's associated with your
 IAM user.


###### To change one keybinding at the same time

1. On the menu bar, choose **AWS Cloud9**, **Preferences**.
2. On the **Preferences** tab, in the side navigation pane, choose **Keybindings**.
3. In the list of keybindings, open (double-click) the keybinding in the
 **Keystroke** column that you want to change.
4. Use the keyboard to specify the replacement key combination, and then press `Enter`.


###### Note

To completely remove the current key combination, press `Backspace`
 for Windows or Linux, or `Delete` for macOS.

###### To change multiple keybindings at the same time

1. On the menu bar, choose **AWS Cloud9**, **Open Your Keymap**.
2. In the `keybindings.settings` file, define each keybinding to
 be changed. The following is example syntax.



```
[
  {
    "command": "addfavorite",
    "keys": {
      "win": ["Ctrl-Alt-F"],
      "mac": ["Ctrl-Option-F"]
    }
  },
  {
    "command": "copyFilePath",
    "keys": {
      "win": ["Ctrl-Shift-F"],
      "mac": ["Alt-Shift-F"]
    }
  }
]
```

In the example, `addFavorite` and `copyFilePath` are the
 names of keybindings in the **Keystroke** column in the
 **Keybindings** pane on the **Preferences** tab.
 The keybindings that you want are `win` and `mac` for Windows
 or Linux and macOS, respectively.


To apply your changes, save the `keybindings.settings` file.
 Your changes appear in the **Keybindings** pane after a short
 delay.

## Remove all of your custom Keybindings


You can remove all custom keybindings and restore all keybindings to their default
 values, across each environment that's associated with your IAM user.


###### Warning

You *cannot* undo this action.



1. On the menu bar, choose **AWS Cloud9**, **Preferences**.
2. On the **Preferences** tab, in the side navigation pane, choose **Keybindings**.
3. Choose **Reset to Defaults**.
