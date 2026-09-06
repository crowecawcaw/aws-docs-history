

# Using third party data in Quick Research (S&P Global Energy)
<a name="spgi-global-energy"></a>

S&P Global Energy Data aggregates a vast array of textual content across thousands of documents about commodity and energy markets into an AI Ready data format, updated every 30 minutes. It enables users to ask customized questions on a range of topics such as regulatory challenges, investment opportunities, and trade flows.

Sources include PDF documents, news articles, rationales, commentaries, analyses, and more, all in an LLM-friendly format. This extensive dataset features hundreds of thousands of documents enriched with metadata, embeddings, and citations. The inventory of textual content focuses on different time horizons (from daily news to 1-year outlooks to 20\+ year long-term scenario views) for each of the major industry sectors broken down by subscription packages spanning Oil, Gas, Power, Metals, Clean Energy, Agriculture, Shipping sector, and more.

Users can leverage this integration to answer customized questions, leveraging S&P Global's commodity and energy market expertise. Example prompts include (but not limited to):
+ Summarize the current regulatory challenges facing the crude oil industry and how they might impact production and pricing strategies.
+ Identify the top investment opportunities in India's wind turbine sector in 2025 and beyond, highlighting emerging technologies or companies that are innovating in this space.
+ Discuss recent environmental implications of metals extraction in Africa, and suggest sustainable practices that could be adopted in the industry.
+ Summarize the current regulatory challenges facing the US natural gas pipelines in 2025 and how that might impact US gas production through end of this decade.

## Setting up the integration
<a name="spgi-global-energy-setup"></a>

This integration requires a subscription to S&P Global Energy. S&P will need to authorize your account and someone with an Enterprise subscription to Quick (typically an admin or whomever is responsible for your organization's access to S&P data) will need to set up the integration. This person (the 'integration owner') will then share the integration with everyone at your organization who should have access. The instructions below describe these steps in more detail.

To use S&P Global Energy in Quick, you (or someone from your organization) will need to:

1. Contact S&P Global at [ai.energy@spglobal.com](mailto:ai.energy@spglobal.com) to ensure your organization subscribes to S&P Global Energy. S&P will provide you a client id and client secret.

   1. If your organization already subscribes, S&P needs to enable your account so you can access this data in Quick.

   1. If your organization does not subscribe already, S&P can help you get started with a free trial.

1. Create a Quick integration for S&P Global Energy.

   1. Open the Research page and select **New Research**.

   1. In the **Research Materials** section, find **Third party data** and select **Browse** to display a list of supported third party data integrations.

   1. Find the integration in the list and select **Connect**. This will display a pop-up with a summary of these setup steps. Select **Continue**.

   1. Enter a name and description for the integration. You can enter anything you want to help you identify this integration later.

   1. Enter the client ID and client secret provided by S&P.

   1. For the remaining fields, you can use the suggested values displayed below each input field.

1. Share the integration with anyone else at your organization who should have access.

## Using the integration in Quick Research
<a name="spgi-global-energy-using"></a>

These instructions assume that you already set up the integration (see details above), or someone at your organization set up the integration and shared it with you.

To use this integration in Quick Research:

1. Navigate to the Quick Research page and select **New Research**.

1. On the left-hand side, under **Research Materials**, there is a section called **Third Party Data**. Select the **Browse** button to display a list of supported integrations.

1. If you need to sign in, there will be a **Sign In** button in the status column. Selecting this button will open a new tab where you can sign in. After you have signed in, navigate back to the tab with Quick Research.

1. Select the check box for the integration you want to use.