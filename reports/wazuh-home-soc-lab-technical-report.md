# Wazuh Home SOC Lab — Technical & Investigation Report

**Author:** Dhruv Vats (`dhruvvats17`)  
**Project type:** Personal home SOC lab / portfolio project  
**SIEM:** Wazuh 4.14.7  
**Endpoint:** Windows 11 with Wazuh Agent and Sysmon  
**Manager platform:** Ubuntu Server  
**Test platform:** Kali Linux  
**Report status:** Portfolio report based on available lab screenshots and author-provided test history  
**Evidence period:** Screenshots supplied in August 2026; dashboard values are historical snapshots, not live metrics.

## 1. Executive summary

This project documents a small home Security Operations Center (SOC) lab built to practice endpoint telemetry collection, centralized security monitoring, alert triage, and incident documentation using Wazuh. A Windows 11 endpoint forwards telemetry to a Wazuh manager hosted on Ubuntu Server. Sysmon supplies detailed process and host-activity events. Kali Linux is used as a controlled testing machine for authorized lab-only activity.

The supplied screenshots show a Wazuh dashboard, an active Windows agent, Threat Hunting event views, repeated Windows authentication-failure events, a custom network-scan-related alert, and Windows Firewall log output. The network-scan screenshot displays a matching event labelled **“Nmap Scan Detected”** with rule ID **100100** and severity/level **10**. These are useful evidence of a detection workflow in the lab. The screenshots are snapshots and should not be interpreted as current alert counts.

The project is intended for learning and portfolio demonstration. It is not a production SOC deployment, and no claim is made that every proposed test scenario has been completed or independently reproduced.

## 2. Objectives

- Collect Windows endpoint events centrally in Wazuh.
- Use Sysmon and Windows event telemetry to support investigation.
- Review security events in the Wazuh dashboard and Threat Hunting view.
- Demonstrate a network-scan detection and document an investigation workflow.
- Record test limitations, evidence, and follow-up improvements.
- Practice SOC L1 triage and clear incident reporting.

## 3. Lab architecture

| Component | Role |
|---|---|
| Ubuntu Server | Hosts Wazuh manager, indexer, and dashboard components |
| Wazuh 4.14.7 | Centralized security event analysis and dashboard |
| Windows 11 endpoint | Monitored victim/test endpoint |
| Wazuh Agent | Forwards configured endpoint logs to Wazuh |
| Sysmon | Adds detailed Windows process and host telemetry |
| Windows Event Logs | Provides authentication and system/security events |
| Kali Linux | Authorized lab test source for network/security exercises |

The systems were previously configured on a private home network. Private IP addresses are intentionally omitted from this public report.

## 4. Evidence reviewed

| Evidence ID | File | What it supports | Limitations |
|---|---|---|---|
| E-01 | `screenshots/01-wazuh-dashboard-overview.png` | Wazuh dashboard was accessible; historical severity counters were visible | Counts are a point-in-time snapshot |
| E-02 | `screenshots/02-wazuh-agent-status-ip-redacted.png` | Windows agent `Window-Victim` displayed as active | Snapshot only; does not prove current connectivity |
| E-03 | `screenshots/03-threat-hunting-dashboard.png` | Threat Hunting overview and event summaries were visible | Aggregated counts alone do not establish malicious activity |
| E-04 | `screenshots/04-network-scan-detection-alert.png` | Event labelled “Nmap Scan Detected”; rule ID 100100 and level 10 shown in the event list | Screenshot shows an alert match; full raw event/export and repeatability should be retained for stronger evidence |
| E-05 | `screenshots/05-windows-authentication-failures.png` | Multiple Windows logon-failure events visible in Threat Hunting | These may be benign or test-generated; attribution and cause need event-level investigation |
| E-06 | `screenshots/06-windows-firewall-log-ip-redacted.png` | Windows Firewall log output, including traffic action/protocol fields | Console output alone does not prove that each entry generated a Wazuh alert |

## 5. Findings and analysis

### Finding 1 — Endpoint telemetry path

The Wazuh dashboard screenshot and agent list indicate that the Windows endpoint was registered and shown as active at the time of capture. This supports the configured endpoint-to-manager monitoring path. Current status should be reconfirmed before a live demonstration.

**Assessment:** Configuration evidence present.  
**Recommended next check:** Confirm agent status in the dashboard and verify that a fresh test event appears with a current timestamp.

### Finding 2 — Network-scan-related alert

The Threat Hunting screenshot contains rows labelled **“Nmap Scan Detected”**, with rule ID **100100** and level **10**. This supports that a scan-related detection rule matched events in the lab at the time shown.

**Assessment:** Screenshot evidence of a matching alert is present.  
**Recommended next check:** Export the full event JSON, record the test time and source host, repeat the authorized scan, and verify that the event count/timestamp changes as expected.

### Finding 3 — Windows authentication failures

The authentication-failure screenshot shows multiple logon-failure events associated with the Windows endpoint. Repeated failures warrant triage but are not automatically proof of brute force. A SOC analyst should inspect event IDs, usernames, source workstation/IP (in the private lab), time range, frequency, and whether a successful logon followed the failures.

**Assessment:** Authentication-failure event evidence present; cause is not conclusively established by the screenshot alone.  
**Recommended next check:** Correlate raw Windows Security events (commonly 4625 for failed logon and 4624 for successful logon) with timestamps and the source fields available in the event.

### Finding 4 — Firewall log collection

The Windows Firewall console screenshot shows firewall log entries and action/protocol fields. This supports that firewall logging was available for review. It does not independently prove that all firewall entries were parsed or matched by Wazuh.

**Assessment:** Host-side firewall-log evidence present.  
**Recommended next check:** Confirm the log path is configured for collection, generate one safe authorized test event, and verify the matching raw event and Wazuh rule in the dashboard.

### Finding 5 — SSH brute-force exercise

The project owner reports that an SSH brute-force exercise and related alert were tested. No dedicated SSH alert screenshot was identified among the supplied evidence used for this report, so this is recorded as **author-reported**, not independently evidenced in this report.

**Assessment:** Author-reported test; screenshot evidence pending.  
**Recommended next check:** Capture the relevant Wazuh alert details and a sanitized event export during a repeatable lab-only test.

## 6. SOC L1 investigation workflow used

1. **Validate the alert:** Record the rule ID, severity, event time, agent, and alert description.
2. **Scope the event:** Set a clear time range and identify the relevant endpoint and source.
3. **Collect evidence:** Review the alert JSON, related Windows/Sysmon events, and relevant firewall or authentication logs.
4. **Correlate:** Compare repeated events, source/destination details, process/user fields, and nearby successful activity.
5. **Assess severity:** Consider confidence, asset importance, event frequency, and evidence of impact.
6. **Decide and escalate:** Classify as benign/expected, suspicious, or confirmed malicious only when supported by evidence.
7. **Document:** Record findings, actions, limitations, and recommended follow-up.
8. **Close carefully:** Do not claim containment or remediation unless it was actually performed and verified.

## 7. MITRE ATT&CK context

The following are potential mappings for investigation context, not proof that a technique occurred:

- **T1046 — Network Service Discovery:** potentially relevant to a network scan.
- **T1110 — Brute Force:** potentially relevant to repeated authentication failures when evidence supports a password-guessing pattern.
- **T1078 — Valid Accounts:** consider only if evidence shows a successful login using a valid account in a suspicious context.

Mappings must be selected based on the observed behavior and raw evidence, not merely the alert label.

## 8. Limitations

- This is a personal lab, not a production SOC.
- Screenshots are point-in-time evidence and do not prove the current health of services.
- Screenshot evidence does not replace raw JSON/EVTX exports, timestamps, repeatability notes, or hashes.
- The SSH brute-force result is author-reported because a dedicated screenshot was not present in the evidence reviewed.
- Windows authentication failures may have benign causes; they require correlation before being classified as brute force.
- The firewall console screenshot does not by itself confirm end-to-end Wazuh ingestion and rule matching for each line.
- No containment action or real-world compromise is claimed.

## 9. Recommendations / next steps

1. Export sanitized JSON for the network-scan alert and authentication-failure events.
2. Repeat SSH and network-scan tests only inside the owned/authorized lab and capture timestamped screenshots.
3. Record test commands, source/target lab roles, expected outcome, actual outcome, and cleanup.
4. Add a before/after view showing the detection rule and the event that matched it.
5. Revalidate custom rules with Wazuh's rule-testing tools and confirm end-to-end matching.
6. Redact usernames, public IPs, hostnames, tokens, and any sensitive data before public upload.
7. Keep the README aligned with the evidence actually present in the repository.

## 10. Conclusion

The available evidence demonstrates a functioning Wazuh learning environment with a Windows endpoint shown as active, Threat Hunting event views, Windows authentication-failure telemetry, firewall logs, and a network-scan-related alert match. The project documents how a junior SOC analyst can move from alert validation to event correlation, evidence recording, and a cautious written assessment. Further raw-event exports and repeatable test captures will strengthen the portfolio.

---

**Author:** Dhruv Vats  
**GitHub:** https://github.com/dhruvvats17  
**Repository (after creation):** https://github.com/dhruvvats17/wazuh-home-soc-lab
