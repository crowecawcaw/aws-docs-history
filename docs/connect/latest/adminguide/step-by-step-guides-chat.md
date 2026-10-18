

# Use step-by-step guides in chats
<a name="step-by-step-guides-chat"></a>

You can show step-by-step guides to customers in chat for self-service. A guide collects context from the customer and passes it to the agent if the chat transfers. You can reuse a guide that you built for agents, so you maintain one guide instead of two.<a name="step-by-step-guides-chat-enable"></a>

1. Set up [step-by-step guides](step-by-step-guided-experiences.md) for agents. Confirm that a guide opens when a contact is offered to an agent.

1. In your chat flow, add a [Show view](show-view-block.md) block to show the view, the same way you would for agents. In the following example, the guide starts when the customer chooses the chat bubble. The flow shows two views, then transfers the chat to an agent.  
![A chat flow that uses the Show view block.](https://docs.aws.amazon.com/connect/latest/adminguide/images/step-by-step-guides-chat-enable-1.png)

1. In the Connect Customer admin workspace, create a [communications widget](add-chat-to-website.md). Set its chat flow to the flow from step 2.  
![A communications widget with its chat flow set to the flow from step 2.](https://docs.aws.amazon.com/connect/latest/adminguide/images/step-by-step-guides-chat-enable-2.png)

   The widget generates a script similar to the following:

   ```
   <script type="text/javascript">
     (function(w, d, x, id){
       s=d.createElement('script');
       s.src='https://d38ij7tdo5kvz7.cloudfront.net/amazon-connect-chat-interface-client.js';
       s.async=1;
       s.id=id;
       d.getElementsByTagName('head')[0].appendChild(s);
       w[x] =  w[x] || function() { (w[x].ac = w[x].ac || []).push(arguments) };
     })(window, document, 'amazon_connect', '0b68a091-3538-4dcd-888e-f3b3ae64c5aa');
     amazon_connect('styles', { iconType: 'CHAT', openChat: { color: '#ffffff', backgroundColor: '#123456' }, closeChat: { color: '#ffffff', backgroundColor: '#123456'} });
     amazon_connect('snippetId', 'QVFJREFIZ3R0VzRTQkxzUnR6S1BPcXRseVBOUVlvWVlFclZwZmJ5bWZUc1hHVU1SM0FHM3BsdU4yaTZVTW9jeTRqQTRWMDJZQUFBQWJqQnNCZ2txaGtpRzl3MEJCd2FnWHpCZEFnRUFNRmdHQ1NxR1NJYjNEUUVIQVRBZUJnbGdoa2dCWlFNRUFTNHdFUVFNRFB0SmlxckgzenRMTjJ4cUFnRVFnQ3RxUHVQZm1Zd1F2ZjZVTzJ2ZTk5am1aUWEwZW53SHFzcmQ5bkdzRVdrNHJIbkJGTk81ekRBK0o4L1Q6OnBwUTZuLzRRKzVvdWdiUHhJRUU2MGM0TDlhcXEyZ0tramVmNkp3N2YvNXBIMTRwdDJSWmFVcjdzVTNzaXorc1BHTHhSOGd0b285dWpiemFrTU1tbWZoY0VCUEY4S3Z1ckdXNnZtV0ZjcVNFYnhrZlpuMVpsb1FGQjZ1SW5LMi9laHlmQVhXY3JXS1NDL1oxd29UejVkSUYwOFBoT3QvUT0=');
     amazon_connect('supportedMessagingContentTypes', [ 'text/plain', 'text/markdown' ]);
   </script>
   ```

   The last line lists the allowed message content types. To show guides in chat, add the interactive message types. For example:

   ```
   amazon_connect('supportedMessagingContentTypes', ['text/plain', 'application/vnd.amazonaws.connect.message.interactive', 'application/vnd.amazonaws.connect.message.interactive.response']);                        
   ```

1. Add the following URL to your allowlist so guides work in chat:
   + `{{your-website-url}}/views/renderer/`

   If your website uses a content security policy (CSP) for the chat widget, it already allows a CloudFront URL, such as:
   + `https://{{unique-id}}.cloudfront.net/amazon-connect-chat-interface.js`

**Note**  
You can also use guides in chat with a custom communications widget. For more information, see the [Connect Customer chat interface](https://github.com/amazon-connect/amazon-connect-chat-interface) on GitHub.