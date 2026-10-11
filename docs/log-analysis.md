# Security Log Analysis Notes

## General method
1. Identify the source, event ID, timestamp, and timezone.
2. Determine which host generated the event.
3. Extract relevant fields without changing the raw evidence.
4. Compare with nearby events and expected system behavior.
5. Distinguish an observation from an interpretation.
6. Record queries, time range, and limitations.

## Windows / Sysmon
For process creation, examine the image, parent image, command line when available, user, and timestamp. Interpret fields in context; a familiar process name alone does not establish legitimacy.

## Authentication
Review repeated failures, source, target account, time interval, and nearby successes. Failed logins can have benign explanations.

## Firewall
Identify whether the event represents an allow or drop, the relevant protocol and endpoints, and the rule that matched. Verify that the event was actually collected by Wazuh.

## Evidence quality
Prefer exact timestamps, raw event details, and reproducible steps. Redact sensitive information before sharing. Never invent missing fields.
