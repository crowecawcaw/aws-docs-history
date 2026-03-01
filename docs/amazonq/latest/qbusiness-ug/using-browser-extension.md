# Using the Amazon Q Business browser extension

The browser extension is available to Amazon Q Business users on Google
Chrome, Mozilla Firefox, and Microsoft Edge browsers.

###### Topics

- [Prerequisites for using the browser extension](#user-prerequisites "#user-prerequisites")
- [Install and configure the browser extension](#install-configure-browser-extension "#install-configure-browser-extension")
- [Common use cases for using the Amazon Q Business browser extension](#browser-extension-common-use-cases "#browser-extension-common-use-cases")
- [Considerations for using the Amazon Q Business browser extension](#browser-extension-considerations "#browser-extension-considerations")
- [Troubleshooting the Amazon Q Business browser extension](#browser-extension-troubleshooting "#browser-extension-troubleshooting")

## Prerequisites for using the browser extension

- You must be a user
- Your Amazon Q Admin must connect the browser extension with
  your Amazon Q Business web experience.
- Supported browsers are Google Chrome, Mozilla Firefox, Microsoft Edge,
  but reach out to their admin to find out which browsers are enabled for
  use with Amazon Q.

## Install and configure the browser extension

- To set up your browser extension, either wait for your IT department
  to configure and install it automatically, or follow their installation
  instructions.

The following are browser extensions from third-party providers that
may be helpful.

    + Mozilla based browsers — [https://addons.mozilla.org/en-GB/firefox/addon/amazon-q-business/](https://addons.mozilla.org/en-GB/firefox/addon/amazon-q-business/ "https://addons.mozilla.org/en-GB/firefox/addon/amazon-q-business/")
    + Chromium based browsers (including Microsoft Edge) —
     [https://chromewebstore.google.com/detail/amazon-q-business/feihpdljijcgnokhfoibicengfiellbp](https://chromewebstore.google.com/detail/amazon-q-business/feihpdljijcgnokhfoibicengfiellbp "https://chromewebstore.google.com/detail/amazon-q-business/feihpdljijcgnokhfoibicengfiellbp")

- If you have an Amazon Q Business web experience and would like
  to connect to it, navigate to it in one of your other browser windows,
  the extension will automatically detect and suggest the link to connect
  your Amazon Q web experience. If not, you will need to paste
  the link to your Amazon Q web experience at the time of
  authenticating to the Amazon Q browser extension. Your
  browser extension will remember this link for future logins, but you can
  always choose a different Amazon Q web experience
  link.
- Once you have successfully logged on, you can use your Amazon Q browser extension.

###### Tip

You can also _pin_ your Amazon Q browser
extension to have it readily accessible while using your browser.
Instructions for this are specific to your browser of choice. The following
third-party information about pinning extensions might be helpful.

- Google Chrome — [https://www.howtogeek.com/683099/how-to-pin-and-unpin-extensions-from-the-chrome-toolbar](https://www.howtogeek.com/683099/how-to-pin-and-unpin-extensions-from-the-chrome-toolbar/ "https://www.howtogeek.com/683099/how-to-pin-and-unpin-extensions-from-the-chrome-toolbar/")
- Mozilla Firefox — [https://support.mozilla.org/en-US/kb/extensions-button#w_manage-pinned-extensions](https://support.mozilla.org/en-US/kb/extensions-button#w_manage-pinned-extensions "https://support.mozilla.org/en-US/kb/extensions-button#w_manage-pinned-extensions")
- Microsoft Edge — [https://www.microsoft.com/en-us/edge/features/pin-to-taskbar](https://www.microsoft.com/en-us/edge/features/pin-to-taskbar "https://www.microsoft.com/en-us/edge/features/pin-to-taskbar")

Safari browsers are not supported at the time.

## Common use cases for using the Amazon Q Business browser extension

The following are some of the common use cases that will help you make the
best use of your Amazon Q Business browser extension:

1. **Summarize a page**
   1. Open the Amazon Q Business browser extension
   2. Login and navigate to the web page that you want to
      summarize.
   3. Use the **summarize** for a summary of a
      snapshot of that web page for the moment when you navigated to
      it.
   4. Now your conversation contains a snapshot of this web page.
      You can continue to chat about the web page and ask followup
      questions.

2. **Add web pages and files as context to an Amazon Q conversation**
   1. Switch to General Knowledge mode.
   2. If you have clicked on the summarize button, the current web
      page is already in your conversation context. To add the current
      web page to the conversation without summarizing the
      page:
      1. Choose the paperclip icon
      2. Select add current page

   3. Ask questions about the current web page snapshot.
   4. To add a file, choose the paper clip icon and browse to the
      file of your choice (~50MB maximum size limit, ~3.75MB per image)
   5. You can have up to a total of 20 web page snapshots or files in
      your conversation. To add another web page, navigate to the next
      web page that you'd like to add and repeat the first
      step.
   6. To remove an attachment, choose the paper clip icon and remove
      the web page snapshots or files of your choice.

3. **Access Amazon Q Business’ Knowledge from your company
   data sources**
   1. Switch to Company Knowledge mode
   2. Ask Q Business questions about your company’s data
      sources
   3. Get source attribution for your data sources

4. **Reset the context of your current
   conversation**
   1. To reset the context of your current conversation, choose the
      new chat bubble icon. Your chat will be free of past attachments
      and web page snapshots.

###### Important

The Amazon Q Business browser extension integration does not support [actions or plugins](actions.md "actions.md").

## Considerations for using the Amazon Q Business browser extension

1. Amazon Q Business does not use customer data for service
   improvement or for improving its underlying large language models
   (LLMs). Also, none of the data you include in your browser extension
   conversations will be indexed into your company's Amazon Q Business instance. For more information, see [Amazon Q Business Service
   improvement](service-improvement.md "service-improvement.md").
2. You can access all history of previous conversations (including
   attachments to those conversations) that have not been deleted from the
   Amazon Q web experience conversation history.
3. All conversations with Amazon Q including uploaded web page
   snapshots and files from the browser extension will be deleted after 30
   days of inactivity.
4. If you close the Amazon Q browser extension, it will start
   a new conversation the next time you reopen it.
5. Amazon Q's responses aren't always 100% accurate. For more
   information, see [Hallucination](concepts-terms.md#hallucination "concepts-terms.md#hallucination") in the topic Key concepts
   of Amazon Q Business.

## Troubleshooting the Amazon Q Business browser extension

- **My admin has enabled the browser extension, but
  I'm unable to login.**

Try having a conversation on your Amazon Q web experience
first and then try the browser extension again. If this doesn't work,
then contact your Amazon Q admin or IT department.

- **I am getting a "Can't access document"
  error.**

This happens when a web uses an unsupported format from which the
browser extension is unable to pull relevant data to provide a helpful
response. If you encounter this error and would like your web page to be
supported, please submit feedback via the feedback button in the browser
extension

- **Amazon Q doesn't respond helpfully or
  doesn't use the context of the web page I added.**

Try starting a new chat and adding the web page snapshot or file
again. If it still does not work, submit feedback using the feedback
button and include any non-confidential details about the type of web
page where the extension failed,

- **I get the error, 'To use this browser extension,
  your administrator needs to enable "Allow end users to send queries
  directly to the LLM" in the Amazon Q Business
  console'**.

Contact your Admin or IT department with the error.

- **Amazon Q doesn't recognize updated
  information when my web page changes.**

Amazon Q only has access to a snapshot of a web page.
Similar to a photograph, this is all the information in the web page
from the time it was uploaded to Amazon Q. To refresh the
snapshot of your page, remove the current snapshot of the web page,
choose a refreshed snapshot of the page, and choose
**Summarize** or **Upload** for
summarizing or further contextual analysis.
