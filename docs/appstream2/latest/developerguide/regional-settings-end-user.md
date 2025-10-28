# Configure Regional Settings

You can configure regional settings so that your AppStream 2.0 Windows streaming sessions use
settings that are specific to your location or language. Changes that you make during
your streaming session are applied to future streaming sessions.

###### To configure regional settings for your Windows AppStream 2.0 streaming sessions

1.  In the top left of the AppStream 2.0 toolbar, choose the
    **Settings** icon, and then choose **Regional
    settings**.
2.  In the **Regional settings** dialog box, set the following
    options as needed. When you're done, choose **Save**.

        * **Time zone** — Determines the system time used
         by Windows and any applications that rely on the operating system time.
         Choose one of the following options:




        	+ To sync the time zone for your streaming session to match the
        	 time zone set on your device, choose **Set my time zone
        	 automatically based on my device**. This is enabled
        	 by default for both single-session and multi-session fleets, and
        	 can be disabled.
        	+ For single-session fleets, you can choose a specific time zone
        	 for your streaming session instead of using automatic
        	 redirection. To set a custom time zone, disable the
        	 **Set my time zone automatically based on my device
        	 option** in **Regional settings**,
        	 and choose a preferred time zone from the available list.
        * **Locale** (also known as culture) — Determines
         how Windows displays numbers, currency, time, and dates. AppStream 2.0 supports
         the following locales: Chinese (Simplified and Traditional), Dutch,
         English, French, German, Italian, Japanese, Korean, Portuguese, Spanish,
         and Thai.
        * **Input method** — Determines the keystroke
         combinations that can be used to input characters in another language.

    Configuring regional settings is not yet supported for Linux streaming sessions.
    However, you can switch between different input methods available in your streaming
    sessions with shortcut key combinations specified by your administrator. The default
    shortcut key combinations are “Super + Space” and “Shift + Super + Space”. “Super” is
    the “Windows” key on a Windows keyboard or the “Command” key on an Apple keyboard.
    Always check with your administrators for the shortcut keys they specified when creating
    the image. For example, in [Tutorial: Enable Japanese Support for Your
    Linux Images](enable-japanese-support-linux.md "enable-japanese-support-linux.md"), the shortcut key combinations have
    been changed to “Control + Space” and “Shift + Control + Space”.
