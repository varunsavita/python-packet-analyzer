# Python Packet Analyzer

A Python-based packet analysis and automated validation framework for structured binary communication data.

## Project Objective

The project is designed to read, validate, decode and analyze hexadecimal packet data.

The framework will provide:

- Packet parsing
- Packet validation
- CRC validation
- Payload decoding
- Test automation
- CSV/Excel report generation
- Logging
- Automated test reporting

## Technology Stack

- Python
- Pytest
- Pytest HTML
- Pandas
- OpenPyXL
- Git
- GitHub Actions

## Architecture

```text
Input Packet
     |
     v
Packet Reader
     |
     v
Packet Parser
     |
     v
Packet Validator
     |
     +---- CRC Validation
     |
     v
Payload Decoder
     |
     v
Analysis Result
     |
     v
CSV / Excel Report
     |
     v
Pytest Automation