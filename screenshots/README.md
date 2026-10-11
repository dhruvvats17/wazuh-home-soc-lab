# Screenshot Evidence

These are screenshots supplied by the project owner from their Wazuh/Windows home lab. They are point-in-time evidence, not live status.

| Evidence | File | Purpose |
|---|---|---|
| E-01 | `01-wazuh-dashboard-overview.png` | Wazuh dashboard overview and historical counters |
| E-02 | `02-wazuh-agent-status-ip-redacted.png` | Windows endpoint agent shown as active; address obscured |
| E-03 | `03-threat-hunting-dashboard.png` | Threat Hunting dashboard summary |
| E-04 | `04-network-scan-detection-alert.png` | `Nmap Scan Detected`, rule ID 100100, level 10 shown in event rows |
| E-05 | `05-windows-authentication-failures.png` | Windows authentication-failure events |
| E-06 | `06-windows-firewall-log-ip-redacted.png` | Windows Firewall log output with sensitive network details redacted |

## Evidence hygiene
- Screenshots show a historical state and do not prove services are currently online.
- No screenshot has been fabricated to represent an alert.
- The supplied evidence does not include a dedicated SSH brute-force alert screenshot; that test is recorded as author-reported.
- Before adding more evidence, redact private IP addresses, public IPs, usernames, tokens, email addresses, and any unrelated personal information.
- Prefer adding a sanitized raw JSON event export alongside a screenshot for each important detection.
