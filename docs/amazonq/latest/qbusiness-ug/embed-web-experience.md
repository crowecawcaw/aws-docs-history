# Add Amazon Q embedded to your website

You can embed your Amazon Q Business web experience by adding an
`<iframe>` element to your website with the **Deployed
URL** or `defaultEndpoint` you copied earlier as the
`src` value and a minimum width of _450 pixels_ as
follows.

```

<iframe src="`Deployed-URL-or-defaultEndpoint`" style="min-width: 450px;"/>

```

Once this <iframe> is added to the website, the Amazon Q Business chat
assistant will show up and be ready to be used by your authenticated Amazon Q
users.

Amazon Q Business users must provide user authentication credentials before they
can use the embedded Amazon Q chat experience on your website. These
credentials are the same as the credentials required for the Amazon Q web
experience. To authenticate, Amazon Q opens a new browser tab or window where
users can enter their credentials. Once successfully authenticated, users can close this
tab or window and begin using the embedded Amazon Q chat experience within
the website.

###### Note

- For [anonymous applications](create-anonymous-application.md "create-anonymous-application.md"), the
  **Deployed URL** must be generated every time using the
  `CreateAnonymousWebExperienceUrl` API operation. For
  more information, see [Share an anonymous web experience](supported-exp-actions-anonymous.md#create-experience-anonymous-url "supported-exp-actions-anonymous.md#create-experience-anonymous-url").
- If your browser has a limited cookie mode (ex. Incognito mode in Chrome),
  you may have to enable third-party cookies for Amazon Q embedded to work.
- The button for copying may not work without `allow="clipboard-read;
clipboard-write"` attribute added to iframe
