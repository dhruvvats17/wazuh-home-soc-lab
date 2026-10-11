# Detection Test Plan: Network Scan

## Objective
Assess whether an authorized scan from the lab testing machine creates observable network or endpoint telemetry and whether Wazuh produces a useful alert.

## Procedure
1. Confirm target scope and authorization.
2. Record the test source, target, tool, command, and timestamp.
3. Run a low-impact scan only against the lab target.
4. Review available firewall, network, and endpoint logs.
5. Search Wazuh for correlated events.
6. Record whether detection occurred; absence of an alert is a valid finding.
7. Tune only after understanding the source event and rule logic.

## Evidence
Include the scan record, relevant raw events, any resulting Wazuh alert, and limitations. Do not claim that a scan was detected solely because the scan command completed.

## Status
Not verified by the available project notes.


## Current status

**Evidence included:** [`../screenshots/04-network-scan-detection-alert.png`](../screenshots/04-network-scan-detection-alert.png) shows event rows labelled `Nmap Scan Detected: Windows Firewall blocked TCP connection from Kali`, rule ID `100100`, level `10`, on the captured historical dashboard. Re-run the test before treating it as current configuration evidence; never infer additional results from the screenshot.
