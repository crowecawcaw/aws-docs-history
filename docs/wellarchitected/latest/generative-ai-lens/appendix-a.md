# Appendix A: Best practice lifecycle mapping

This table maps the best practices in this lens to the stages of the
generative AI lifecycle. This mapping is only a suggestion and is
prone to adjustments based on your business problem, generative AI
use case, and other external factors. An absence of a best practice
does not indicate no best practices exist for the corresponding
lifecycle phase, but that they are not relevant for discussion in
this lens. An example of this is the absence of performance
efficiency best practices in the deployment phase of the lifecycle.
This lens approaches performance efficiency for generative AI from
the perspective of inference latency and model response quality. The
best practices for these initiatives fall more appropriately under
different lifecycle phases. This mapping is subject to change and
grow as the scope of this lens evolves over time.

|                        | Scoping                      | Model selection              | Model customization            | Development and integration                    | Deployment                                                                                              | Continuous improvement                                     |
| ---------------------- | ---------------------------- | ---------------------------- | ------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Operational excellence | GENOPS02-BP03                |                              | GENOPS03-BP01, GENOPS05-BP01   | GENOPS03-BP02                                  | GENOPS02-BP01, GENOPS02-BP02                                                                            | GENOPS01-BP01, GENOPS01-BP02, GENOPS04-BP01, GENOPS04-BP02 |
| Security               |                              |                              | GENSEC05-BP01                  | GENSEC02-BP01, GENSEC06-BP01                   | GENSEC01-BP01, GENSEC01-BP02, GENSEC01-BP03, GENSEC01-BP04, GENSEC03-BP01, GENSEC04-BP02, GENSEC06-BP01 | GENSEC04-BP01                                              |
| Reliability            |                              | GENREL01-BP01, GENREL05-BP01 | GENREL06-BP01                  | GENREL02-BP01, GENREL03-BP02, GENREL04-BP02    | GENREL03-BP01, GENREL05-BP02, GENREL05-BP03, GENREL06-BP01                                              | GENREL04-BP02                                              |
| Performance efficiency | GENPERF01-BP02               | GENPER02-BP03                | GENPERF01-BP01, GENPERF03-BP01 | GENPERF02-BP01, GENPERF02-BP02, GENPERF04-BP01 |                                                                                                         | GENPERF04-BP01                                             |
| Cost optimization      | GENCOST02-BP01               | GENCOST01-BP01               |                                | GENCOST02-BP02, GENCOST03-BP02                 | GENCOST04-BP01, GENCOST05-BP01                                                                          | GENCOST03-BP01                                             |
| Sustainability         | GENSUS01-BP01, GENSUS01-BP02 |                              | GENSUS02-BP01                  | GENSUS03-BP01                                  |                                                                                                         |                                                            |
