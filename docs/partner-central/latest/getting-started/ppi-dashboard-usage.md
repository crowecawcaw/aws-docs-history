

# Using the Performance Indicators dashboard
<a name="ppi-dashboard-usage"></a>

The Performance Indicators dashboard provides real-time visibility into your performance metrics and trends. This section explains how to access and use the dashboard.

## Dashboard sections
<a name="ppi-dashboard-sections"></a>

The Performance Indicators dashboard contains the following key sections:
+ **Migration summary data** – This section summarizes your overall performance:
  + Your overall Performance Indicators score
  + Current performance tier
+ **Key contributing metrics** – This section shows the data behind each key metric:
  + Underlying data used to calculate each key metric
  + Actual numbers and percentages
  + Month-over-month (MoM) trending data
+ **Migration level summary** – This section shows underlying migration partner ecosystem (MPE) level data used to calculate each key metric

### Migration Level Summary data definitions
<a name="ppi-dashboard-mls-definitions"></a>

The following table defines each column in the Migration level summary and explains how to use it.


| Column | What it tells you | How to use it | 
| --- | --- | --- | 
| MPE ID | A unique ID for one migration project. Every row is one project. | Use it to find and track an individual migration. | 
| Customer account name | The end customer being migrated. | Identify which customer the row is about. | 
| Customer type / geo | The customer segment (Commercial or Public Sector) and region (NAMER, LATAM, EMEA, APJ, GCR). | Group your results by segment and region. | 
| Estimated migrations ARR | The expected yearly revenue the migrated workloads should generate once live. This is the target you are measured against. | See the revenue goal each project is held to. | 
| Assess funded / claimed | Whether the early Assess phase received approved AWS funding, and whether you have drawn it down. | Confirm the project qualifies and funding is collected. | 
| Assess status | The outcome of the Assess phase: Won, Lost, or In progress. | Track how many early opportunities convert to committed migrations. | 
| Mobilize funded / claimed | Whether the active migration phase received approved AWS funding, and whether you have drawn it down. | Confirm the delivery phase is funded and claimed. | 
| Tenure in days | How long the project has been running, counted from the Mobilize start date. | Judge whether a project has had enough time to show results (very new projects are not yet judged on speed or revenue). | 
| $1K status | Whether an Assess won, active migration has reached its first revenue milestone of $1,000. It credits qualifying won migrations, so a deal that is not yet won, or is no longer active, may show as not attained even if some usage exists. | The earliest sign a qualifying migration has started generating real usage. | 
| Monthly tagged spend (Months 1 to 6) | The attributed AWS spend generated in each of the first six months after the project start. Month 1 is the calendar month of Mobilize Start Date. Months 2–6 are the following calendar months. | See how quickly a migration ramps. Reaching $50K within the first three months is the fast-ramp bar. | 
| Terminal spend and MRR | The actual revenue delivered near the end of the migration, and the monthly target it is compared against. | Compare what the migration actually delivered against what was expected. | 
| Performance status | A simple health label (Performing or Underperforming) based on whether the migration is hitting its revenue bar. | A quick flag for which projects are behind on revenue. | 

**Reading blanks and zeros:** A blank cell usually means that measure does not apply yet (for example, final revenue only appears once a migration completes). A zero means it is being tracked but nothing has been billed yet.

## Using the dashboard
<a name="ppi-dashboard-using"></a>

**To open the Performance Indicators dashboard**

1. Sign in to AWS Partner Central as an alliance lead.

1. Under **Partner Analytics**, open the **Dashboards** list.

1. Choose the **Performance Indicators** dashboard.

**To filter your dashboard data**

1. For **Display data by**, select **Current monthly score** to see your most recent performance snapshot, or select **Historic monthly view** to see a line graph of 12 months of performance trends.

1. For **Customer geography**, select **All geographies**, **NAMER (North America)**, **EMEA (Europe, Middle East, Africa)**, **APJ (Asia Pacific and Japan)**, or **LATAM (Latin America)**.
**Note**  
Your Performance Indicators score remains at the global level regardless of the geography you select.

1. For **Customer type**, select **Commercial Sector (CS)** or **Public Sector (PS)**.

**To interpret your metrics**

1. Review your overall Performance Indicators score. This is your primary indicator of performance.

1. Examine individual metric scores. Identify which areas are strong and which need attention.

1. Check contributing metrics. Understand the underlying data driving each score.

1. Review historical trends. Look for patterns and the impact of improvement efforts.

1. Compare to thresholds. See how close you are to the next performance tier.

### Example interpretation
<a name="ppi-dashboard-example-interpretation"></a>

In this example, your overall Performance Indicators score is 83%, with the following breakdown:
+ **Migration Win Rate** – 3 points (85% conversion)
+ **Speed to Value** – 2 points (72% of projects hit target)
+ **Portfolio Success** – 3 points (95% revenue achievement)
+ **Project Success** – 2 points (30% of projects below 50%)

This makes you a top performer overall, with particular strength in win rate and portfolio-level execution. Focus on improving speed to value and project consistency to reach 100%.

## Dashboard refresh frequency
<a name="ppi-dashboard-refresh"></a>

Keep the following refresh cadence in mind:
+ Performance Indicators scores are calculated monthly
+ Data is refreshed on the 1st of each month
+ Historical data is available for the past 12 months
+ Real-time project data might take 2–3 business days to reflect in Performance Indicators calculations