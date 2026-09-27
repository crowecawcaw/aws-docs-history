

# Threads
<a name="omni-threads"></a>

A thread is your workspace in the CloudWatch Omni web UI: a conversation with the Omni agent together with the canvases, tabs, and views you open while you work. Omni saves the whole thread as you work — not only the chat — so you can close the browser mid-investigation and resume where you left off, on any device where you sign in to your space. Keep one thread per problem.

**What a thread holds**
+ **The conversation.** Your exchange with the Omni agent, including the queries it ran and the evidence behind its answers.
+ **Canvases and tabs.** The views you open while investigating (charts, log tables, maps, trace views), arranged on canvases, across as many tabs as you need.
+ **History.** Every canvas you visit in a thread is kept in order, so you can step back through the investigation.
+ **Investigations.** An investigation starts in a thread, and that thread is marked in your threads list so you can find the investigation again later. An investigation is not locked to that thread. You can open it from another thread, and the Investigations list can show investigations from all your Omni threads.

**Start a thread**

Choose **New thread** in the sidebar or on the **Threads** page. Asking from the input on the Omni home page also starts a thread.

You can also start from a finding instead of a blank page: choose **Investigate** on an alert, or select an anomalous range on a chart and choose **Investigate this signal**. The investigation runs in a thread, with the finding as its starting context. For what the agent can do in the conversation and how an investigation works, see [Ask the Omni agent](omni-ask-the-omni-agent.md).

**Manage your threads**

The **Threads** page lists your threads, and the sidebar shows the recent ones. Omni names a thread from the conversation; rename it to something your team would search for. From the list you can:
+ **Resume** a thread to continue working in it.
+ **Rename** or **Delete** a thread. Deleting cannot be undone, and you always keep at least one thread.
+ **Search** your threads by name.

**Collaborate and share**

To share work from a thread, use a dashboard or a link:
+ **Save a canvas as a dashboard.** The durable way to share an investigation's view: every member of the space can open a dashboard. See [Dashboards](omni-dashboards.md).
+ **Copy a canvas or panel link.** From a canvas or panel menu, copy its URL. The link carries the view, not the conversation. Opening it adds that view to the current thread.