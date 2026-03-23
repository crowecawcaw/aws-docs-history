# Unit Conversions

Preprocessors apply unit conversions during normalization to ensure all data uses canonical units:

| Conversion | Formula      | When Used               |
| ---------- | ------------ | ----------------------- |
| m/s → mph  | × 2.23694    | OEM speed in metric     |
| km → miles | × 0.621371   | OEM odometer            |
| °C → °F    | (× 9/5) + 32 | OEM temperature         |
| kPa → PSI  | × 0.145038   | OEM tire pressure (kPa) |
| bar → PSI  | × 14.5038    | OEM tire pressure (bar) |
| m/s² → g   | ÷ 9.80665    | OEM acceleration        |
