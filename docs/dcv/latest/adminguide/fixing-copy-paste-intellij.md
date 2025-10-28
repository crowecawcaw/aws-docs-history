# Fixing Copy and Paste to IntelliJ IDEA

When trying to copy text from the macOS Amazon DCV Client to IntelliJ IDEA, the text
cannot be pasted. IntelliJ can't accept the cross-platform format that Amazon DCV uses by default.
To disable cross-platform text on Amazon DCV so you can paste text into IntelliJ, modify the `disabled-targets` field on the Amazon DCV Server.

This change will prevent copy and paste from working with the Amazon DCV web client.
Make sure that you want copy and paste for Intellij IDEA to work on only the
Amazon DCV Client before making this change.

###### To configure the server to paste text into IntelliJ IDEA

1. Navigate to `/etc/dcv/` and open the `dcv.conf` with
   your preferred text editor.
2. Locate the `disabled-targets` parameter in the
   `[clipboard]` section. If there is no
   `disabled-targets` or `[clipboard]`
   section, add them manually.
3. Add the following content to define the value for
   `disabled-targets`.

```
[clipboard]
disabled-targets = ['dcv/text', 'JAVA_DATAFLAVOR:application/x-java-jvm-local-objectref; class=com.intellij.codeInsight.editorActions.FoldingData']
```

4. Save and close the file.
5. [Stop](managing-sessions-lifecycle-stop.md "managing-sessions-lifecycle-stop.md") and [restart](managing-sessions-start.md "managing-sessions-start.md") the Amazon DCV session.
