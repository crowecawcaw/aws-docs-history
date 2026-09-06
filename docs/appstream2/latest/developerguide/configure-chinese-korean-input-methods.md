

# Configuring Chinese and Korean input methods on the image
<a name="configure-chinese-korean-input-methods"></a>

Although end users can select from 9 supported input methods during their streaming sessions through **Preferences** > **Input method**, certain input methods require you to pre-install the corresponding language components on the image before they can function correctly. These input methods include Chinese (Taiwan), Chinese (Pinyin), Chinese (Traditional, DaYi), and Korean.

Without these language components, selecting these input methods from Preferences might result in keystrokes being passed through as literal English characters.

## Prerequisites
<a name="configure-chinese-korean-prerequisites"></a>

Before you begin, make sure that your environment meets the following requirements:
+ An Image Builder running Windows Server 2019 or later
+ Administrator access to the Image Builder

## Configure Chinese (Traditional, Taiwan) — Bopomofo input
<a name="configure-chinese-traditional-taiwan"></a>

1. Open the [WorkSpaces Applications console](https://console.aws.amazon.com/appstream2/), and then launch and connect to your **Image Builder**.

1. Open **Settings** > **Time & Language** > **Language**, then select **Add a language** and choose **Chinese (Traditional, Taiwan)**.

   Alternatively, open PowerShell as Administrator and run:

   ```
   $langList = Get-WinUserLanguageList
   $langList.Add("zh-Hant-TW")
   Set-WinUserLanguageList $langList -Force
   ```

1. Verify that the Basic Typing language component is installed:

   ```
   Get-WindowsCapability -Online | Where-Object { $_.Name -like "*zh-TW*" -and $_.State -eq "Installed" }
   ```

   You should see `Language.Basic~~~zh-TW~0.0.1.0` in the output.

1. (Optional) Verify the language is registered with the correct IME:

   ```
   Get-WinUserLanguageList
   ```

   Confirm that `zh-Hant-TW` appears with `InputMethodTips` containing the Bopomofo IME identifier.

1. On the Image Builder desktop, open **Image Assistant** and follow the steps to create your image.

1. Create or update your fleet using the new image.

After this configuration, end users can select **Chinese (Taiwan)** from **Preferences** > **Input method** during their streaming sessions. Bopomofo input functions correctly, and users can switch between Chinese (Taiwan) and Chinese (Pinyin) input methods through Preferences.

## Configure Chinese (Simplified) — Pinyin input
<a name="configure-chinese-simplified-pinyin"></a>

1. Open the [WorkSpaces Applications console](https://console.aws.amazon.com/appstream2/), and then launch and connect to your **Image Builder**.

1. Open PowerShell as Administrator and run:

   ```
   $langList = Get-WinUserLanguageList
   $langList.Add("zh-Hans-CN")
   Set-WinUserLanguageList $langList -Force
   ```

1. Verify installation:

   ```
   Get-WindowsCapability -Online | Where-Object { $_.Name -like "*zh-CN*" -and $_.State -eq "Installed" }
   ```

   You should see `Language.Basic~~~zh-CN~0.0.1.0` in the output.

1. Create your image and fleet.

## Configure Korean input
<a name="configure-korean-input"></a>

1. Open the [WorkSpaces Applications console](https://console.aws.amazon.com/appstream2/), and then launch and connect to your **Image Builder**.

1. Open PowerShell as Administrator and run:

   ```
   $langList = Get-WinUserLanguageList
   $langList.Add("ko-KR")
   Set-WinUserLanguageList $langList -Force
   ```

1. Verify installation:

   ```
   Get-WindowsCapability -Online | Where-Object { $_.Name -like "*ko-KR*" -and $_.State -eq "Installed" }
   ```

   You should see `Language.Basic~~~ko-KR~0.0.1.0` in the output.

1. Create your image and fleet.

## Verifying the configuration
<a name="configure-chinese-korean-verification"></a>

After creating your fleet from the configured image, verify the input method works:

1. Connect to a streaming session.

1. Open **Preferences** > **Input method** and select the desired input method (for example, Chinese (Taiwan)).

1. Open a text application (for example, Notepad).

1. Type test characters:
   + For Bopomofo: Type **su3** — this should produce 你
   + For Pinyin: Type **nihao** — this should produce 你好
   + For Korean: Type using the Korean keyboard layout — Hangul characters should appear

## Important notes
<a name="configure-chinese-korean-important-notes"></a>
+ **Wait for installation to complete:** After adding a language, allow time for the IME installation to finish before testing. If you attempt to type immediately, you might receive a notification that the IME is not ready.
+ **Multiple languages:** You can install multiple language components on the same image. End users can switch between all configured input methods through Preferences.
+ **Japanese does not require this step:** Japanese input works without additional configuration because the base image includes the required language components by default.
+ **DaYi input method:** Chinese (Traditional, DaYi) uses the same `zh-Hant-TW` language pack as Bopomofo. After installing the Chinese (Traditional, Taiwan) language, both Bopomofo and DaYi IMEs are available for end users to select.
+ **Admin defaults vs. user-selectable:** This procedure makes the input methods functional for end users to select during sessions. The admin-configurable default input method (configured through Template User or Image Assistant) still supports only English (United States) and Japanese.
+ **Reboot consideration:** In most cases, a reboot is not required after adding a language. However, if the input method does not function correctly after installation, restart the Image Builder before creating the image.