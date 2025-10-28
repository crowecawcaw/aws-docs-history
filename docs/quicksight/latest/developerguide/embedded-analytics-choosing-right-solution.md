# Choose the right embedding solution

Quick Sight offers multiple options and mechanisms of embedding. You can embed a visual, a dashboard,
the complete Quick Sight console, or the natural language component Q in your application.
Furthermore, based on your organizations authentication setup, you can choose between anonymous
and registered user embedding. All of these options are possible when you onboard the Quick Sight [Embedding APIs](../APIReference/embedding-Quick Sight.md "../APIReference/embedding-Quick Sight.md").

## Anonymous user embedding

Anonymous user embedding offers a lightweight option for you to bring insights to your users without the need to register them in Quick Sight. You can use anonymous embedding to share your dashboards to any number of users in your application and scale as you go. With row-level security, you can further customize your data based on pre-determined context and showcase relevant insights to your users.

To get started with anonymous embedding, see [Embedding Quick Sight data dashboards for anonymous (unregistered) users](../user/embedded-analytics-dashboards-for-everyone.md "../user/embedded-analytics-dashboards-for-everyone.md").

## Registered user embedding

Use registered user embedding to bring Quick Sight to every user in your organization. Use Quick Sight APIs to share dashboards with users or grant them access to build dashboards from scratch, all within the context of your application. Use comprehensive user context based features like row-level security or column-level-security for fine grained data access control. You can also use features like bookmarks to deliver personalized experiences.

To get started with registered user embedding, see [Embedding Quick Sight data dashboards for registered users](../user/embedded-analytics-dashboards-for-authenticated-users.md "../user/embedded-analytics-dashboards-for-authenticated-users.md").

## 1-click Enterprise embedding

1-click Enterprise embedding is focused toward enterprises that have Quick Sight accounts set up for all of their users. With 1-click embedding, developers embed Quick Sight visuals and dashboards with a static embed code from Quick Sight that is added to an <iframe>. When a user accesses a dashboard on your intranet enterprise applications, they are required to sign in to Quick Sight.

To get started with 1-click embedding, see [1-click Enterprise embedding](../user/embedded-analytics-1-click.md "../user/embedded-analytics-1-click.md").

## 1-click public embedding

Use 1-click public embedding to take your insights to public websites with a few clicks. Developers receive an embed code from Quick Sight and add it to an <iframe>. You have full control over when dashboards go public with sharing settings that are available on the dashboard. In case of an emergency, you can revoke public sharing within seconds.

To get started with 1-click public embedding, see [Turn on public access to visuals and dashboards with a 1-click embed code](../user/embedded-analytics-1-click-public.md "../user/embedded-analytics-1-click-public.md").

Use the table below to compare the different features of each embedding option:

| Embedding option             | Embed in SaaS application | Embed in an internal application | Embed in a public portal | Embeddable content     | RLS support       | Requires user setup | Coding and insfrastructure required |
| ---------------------------- | ------------------------- | -------------------------------- | ------------------------ | ---------------------- | ----------------- | ------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Anonymous embedding          | ✓                         | ✓                                | Maybe\*                  | Dashboards, Visuals, Q | ✓ (with RLS Tags) | —                   | ✓                                   |
| Registered user embedding    | ✓                         | ✓                                | —                        | Dashboards, Visuals, Q | ✓                 | ✓                   | ✓                                   |
| 1-click Enterprise embedding | Not recommended           | ✓                                | —                        | Dashboards, Visuals    | ✓                 | ✓                   | —                                   |
| 1-click public embedding     | —                         | —                                | ✓                        | Dashboards, Visuals    | —                 | —                   | —                                   | \*Anonymous embedding delegates the responsibility of authentication to the 3P application. If the 3P application does not have user authentication, the embedded content becomes publicly accessible. |
