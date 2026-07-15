# Linux Security Auditor

> 🚧 This project is currently a work in progress.

A Python-based security auditing tool for Linux systems.

## About

Linux Security Auditor collects system information and performs security checks to help identify potential configuration issues on a Linux machine.

The goal of this project is to learn more about Linux by building a practical auditing tool.

## Current Features

- Collects hostname information
- Detects Linux distribution
- Detects kernel version

## Planned Features

- [ ] Check user privileges
- [ ] Audit sudo users
- [ ] Check firewall status
- [ ] Analyze open ports
- [ ] Review SSH configuration
- [ ] Check available updates
- [ ] Generate security reports

## Requirements

- Linux operating system
- Python 3
- Python packages:
  - distro
 
## Installation

Clone the repository:

```bash
git clone <repository-url>
cd linux-security-auditor
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the auditor:
```
python3 auditor.py
```
