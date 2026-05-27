# NetShield Phase 1 — Foundations

## Project Overview

NetShield Phase 1 is a beginner-level cybersecurity monitoring and detection project built using Python, Linux, SQLite, and GitHub.

The project simulates a mini SOC (Security Operations Center) workflow by:

- Monitoring Linux system information
- Generating dummy security logs
- Simulating suspicious activity safely
- Performing SQL log analysis
- Detecting suspicious IP activity
- Detecting SSH failed login attempts
- Generating security alerts and reports

The goal of this phase was to build strong foundations in:

- Linux workflows
- Python scripting
- SQL log analysis
- Detection logic
- Incident monitoring
- GitHub project structuring

---

# Technologies Used

- Ubuntu Linux
- Python 3
- SQLite3
- Git & GitHub
- Bash Terminal

---

# Folder Structure

```text
netshield-phase1
├── docs
│   ├── commands.md
│   ├── notes.md
│   ├── suspicious_ip_tracking_notes.md
│   └── workflow.md
│
├── logs
│   ├── auth.log
│   ├── incidents.log
│   └── system_info.log
│
├── netshield.db
│
├── README.md
│
└── scripts
    ├── attack_detector.py
    ├── db_init.py
    ├── incident_report.py
    ├── incident_simulator.py
    ├── ip_tracker.py
    ├── sql_log_analysis.py
    ├── ssh_failed_login_detector.py
    └── system_info.py
```

---

# Core Features

## Linux Monitoring & Logging

- System information collection
- Incident logging
- Log file generation
- Incident reporting

## SQL Log Analysis

- SQLite database integration
- SQL-based incident analysis
- Suspicious IP tracking
- Attack threshold detection
- Risk classification

## SSH Failed Login Detection

- SSH log parsing
- Failed login monitoring
- Repeated login detection
- Brute-force style attack simulation

---

# NetShield Workflow Diagram

```text
Linux Monitoring
        ↓
Dummy Log Generation
        ↓
Incident Logging
        ↓
SQLite Database Storage
        ↓
SQL Log Analysis
        ↓
Suspicious IP Tracking
        ↓
SSH Failed Login Detection
        ↓
Risk Classification
        ↓
Alert Generation
```

---

# Detection Workflow

```text
Event Generated
        ↓
Stored in Logs / Database
        ↓
Analyzed by Python Scripts
        ↓
Suspicious Activity Detected
        ↓
Risk Level Assigned
        ↓
Security Alert Generated
```

---

# Risk Classification Model

## LOW RISK

- Minor event
- Unlikely immediate threat

## MEDIUM RISK

- Suspicious behavior
- Needs monitoring

## HIGH RISK

- Repeated or dangerous activity
- Possible attack

---

# Example Outputs

## SQL Log Analysis

```text
=== NetShield SQL Log Analysis ===
Total Incidents: 3
INFO Events: 1
WARN Events: 1
ALERT Events: 1
```

## SSH Failed Login Detection

```text
=== NetShield SSH Failed Login Detector ===

Failed Login Summary:

[HIGH RISK] 192.168.1.50 failed 3 login attempts
[MEDIUM RISK] 10.0.0.25 failed 1 login attempt(s)
```

---

# Learning Outcomes

This project helped develop beginner-level understanding of:

- Linux command-line workflows
- Python scripting logic
- SQL database usage
- Log analysis concepts
- Threat detection basics
- Incident response workflow design
- GitHub repository management
- Documentation and project structuring

---

# Future Roadmap

## Phase 2 — NetShield Enterprise

Planned features:

- Asset Inventory
- Risk Scoring Engine
- Vulnerability Tracking
- Severity Classification
- Incident Timeline Management
- Enterprise Detection Workflows

## Phase 3 — NetShield Automation

Planned features:

- Python Automation
- Automated Alert Generation
- Threat Correlation
- Incident Enrichment
- Simulated Remediation Workflows
- Response Orchestration

---

# Notes

This project was created as part of a structured cybersecurity learning journey focused on:

- Building first
- Understanding second
- Developing practical SOC-style workflows
- Combining hands-on projects with cybersecurity theory and certifications
