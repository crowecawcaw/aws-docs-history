# Demand Pattern and Recommendation

Demand Pattern and Recommendation examines the transformed historical demand input at
each configured forecast granularity level (for example, product, location, or channel) to
uncover underlying patterns and characteristics in your demand data. Its primary purpose is
to identify key demand pattern distribution, such as smooth, intermittent, erratic, and
lumpy. It also provides statistical insights about length of history and trailing 12-month
demand.

The analysis automatically triggers after successful data validation during the forecast
generation process, and runs in parallel with forecast creation. However, it does not block
or delay the forecasting process. The Demand Pattern analysis is triggered as part of the
same workflow as data validation when you initiate forecast creation. However, any data
validation failure prevents both the analysis from being generated and the forecast from
being created.

By providing this analytical overview, the system helps users understand the patterns in
the dataset to improve forecast accuracy.
