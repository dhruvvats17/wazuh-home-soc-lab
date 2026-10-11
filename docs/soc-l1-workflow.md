# SOC L1 Workflow

## 1. Alert intake
Record alert time, rule ID, level, agent/host, event source, and alert description. Preserve the original event details.

## 2. Validate telemetry
Confirm the event exists in the source log and that timestamps/timezones align. Check whether the endpoint and log source are healthy.

## 3. Triage
Ask whether the activity is expected, whether the rule condition matches the evidence, and whether severity is appropriate. A rule level is not the same as a confirmed incident severity.

## 4. Investigate
Inspect relevant event fields, nearby events, authentication activity, process relationships, and network context available in the lab.

## 5. Correlate and scope
Look for related events in the same time window and other available log sources. Avoid claiming broad impact without evidence.

## 6. Classify
Use a cautious conclusion: benign, suspicious, or inconclusive. Explain the evidence and uncertainty.

## 7. Recommend and escalate
Follow authorization and incident-response policy. For a learning lab, document suggested containment or follow-up rather than claiming production actions were performed.

## 8. Report
Include facts, timestamps, evidence, queries/steps, findings, limitations, and recommendations. Make the report reproducible.
