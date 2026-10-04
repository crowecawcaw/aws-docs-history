

# Connecting to Quick datasets in apps in Quick
<a name="connecting-datasets-apps"></a>

Alongside built-in app storage, your app can query a Amazon Quick dataset directly, so app users see current data every time they open the app. The app does not copy the data. Each app user's visuals query the dataset in real time under that app user's own identity, so your row-level and column-level security keeps applying.

## Add a dataset to your app
<a name="apps-live-data-add"></a>

You add a dataset by asking the editing agent for it by name. There is no separate data-source menu.

1. In the app editor, tell the agent which dataset to use, for example: *Use the Sales Pipeline dataset to show pipeline by stage.*

1. The agent finds the dataset, learns its columns, and asks you to approve access to it. Approve the prompt so the agent can build against it.

1. The agent writes the visuals. Describe what you want in plain language, and name the columns you care about so it picks the right ones.

1. Publish. Each app user approves a one-time prompt for the dataset the first time they open the app.

**Note**  
Sharing an app does not share its data. Grant every app user read access to each dataset the app uses, or share the folder that holds them, so they see data instead of an access message.

## Which datasets you can use
<a name="apps-live-data-which"></a>

Live data works with a single-table dataset, whether it is stored in SPICE or queried directly. A dataset built with the visual join editor that produces one logical table also works.
+ **Storage and engines** — Any dataset in SPICE, plus Direct Query on Redshift, Athena, Aurora PostgreSQL, PostgreSQL, Databricks, and S3 Tables. Other engines work after you import them into SPICE.
+ **Same account and Region** — The dataset and the app must be in the same account and Region.
+ **Published version** — The app queries the published version of the dataset, so publish any dataset edits you want it to use.

Some dataset shapes are not supported for live data, including multi-table (data model) datasets, composite or child datasets, and datasets that join across sources. For the full list, see [Live data (Quick datasets)](apps-limitations.md#apps-limits-live-data).

## Keep your app working over time
<a name="apps-live-data-maintain"></a>

The app refers to each dataset's columns by their exact name and type at the time you built it, and it does not track changes automatically. If you rename or retype a column, or replace or delete the dataset, the visuals that use it stop working for app users. Changing only a dataset's display name is fine. When you do change a column or dataset, reopen the app, have the agent update the affected visuals, and publish again.

## Data freshness
<a name="apps-live-data-freshness"></a>
+ **SPICE and S3 Tables** — Results are cached for up to 12 hours. A completed SPICE refresh updates what the app shows.
+ **Direct Query** — Not cached. Every open queries the source.
+ **No refresh button** — The app re-runs its queries on each page load. The header's "Last updated" date reflects the app's last edit, not data freshness.
+ **App user time zone** — Dates and times render in each app user's browser time zone.