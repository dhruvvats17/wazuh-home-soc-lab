# Case 002 — Network-Scan Alert Investigation

**Case status:** Evidence observed; repeatability/raw event export pending  
**Severity shown in screenshot:** Level 10  
**Rule ID shown:** 100100  
**Alert label shown:** `Nmap Scan Detected`  
**Evidence:** `../screenshots/04-network-scan-detection-alert.png`

## Summary
A Wazuh Threat Hunting event view supplied for this project shows events labelled `Nmap Scan Detected`. The visible rows include rule ID `100100` and level `10`. This supports that a network-scan-related rule matched activity in the lab at the time of capture.

## Scope
The activity is documented as part of an owned home lab using Kali Linux as a test machine. Do not run scans against systems without explicit authorization.

## Evidence
- E-04: Wazuh Threat Hunting event list with `Nmap Scan Detected`, rule ID 100100, level 10.
- Supporting host-side firewall log output: E-06, `../screenshots/06-windows-firewall-log-ip-redacted.png`.

## Triage and analysis
1. Validate the event timestamp, agent/endpoint, rule ID, and raw event JSON.
2. Identify the source and target from the private lab event fields; do not publish private IPs.
3. Compare the event time with the authorized scan test time.
4. Review surrounding firewall and endpoint events for correlated activity.
5. Confirm whether the rule is a custom rule and document the exact match conditions.
6. Repeat the test in the authorized lab and verify that a new event is generated.

## Assessment
**Current assessment: suspicious network discovery activity detected in the lab, based on the event label and screenshot.** The screenshot alone does not establish impact, successful access, or malicious intent.

## Recommended follow-up
- Export the complete alert JSON and sanitize it.
- Add exact test time and authorized test command to the lab notes.
- Re-run the detection test and retain before/after evidence.
- Confirm that rule 100100 has an intentional, documented definition and no overly broad matching logic.

## Closure
Do not mark this case as fully closed until the raw event has been reviewed and the detection has been reproduced or its existing test evidence has been documented.
