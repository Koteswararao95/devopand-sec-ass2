# DevOps & Security Assignment 2

A comprehensive DevOps and Security project demonstrating Infrastructure as Code with Terraform and PDF processing automation.

## Overview

This project combines Infrastructure as Code (Terraform) with Python automation for PDF processing. It demonstrates best practices for DevOps workflows and secure infrastructure deployment.

## Features

- **Infrastructure as Code**: Terraform configuration for AWS resources
- **PDF Processing**: Automated PDF extraction and text processing
- **Secure Deployment**: Security-focused infrastructure setup
- **Version Control**: Git-based workflow management

## Prerequisites

- Python 3.8 or higher
- Terraform 1.0 or higher
- AWS CLI configured with credentials
- Git

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Koteswararao95/devopand-sec-ass2.git
cd devopand-sec-ass2
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize Terraform:
```bash
terraform init
```

## Usage

### PDF Processing
Run the PDF extraction script:
```bash
python extract_pdf.py
```

### Infrastructure Deployment
Deploy infrastructure with Terraform:
```bash
terraform plan
terraform apply
```

## Project Structure

```
├── main.tf                          # Terraform configuration
├── extract_pdf.py                   # PDF processing script
├── reqm.md                          # Requirements documentation
├── README.md                        # This file
├── .gitignore                       # Git ignore patterns
└── .terraform/                      # Terraform dependencies
```

## Configuration

Update `main.tf` with your AWS settings:
- Region
- Instance types
- Security groups
- Storage buckets

## Security Considerations

- Store sensitive data in AWS Secrets Manager
- Use IAM roles for service authentication
- Enable encryption for data at rest and in transit
- Regularly update dependencies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## Support

For issues and questions, please open an issue on GitHub.

## License

This project is part of DevOps and Security Assignment 2.

## Author

Koteswararao95

---
Last Updated: May 2026
