# Cloud-Health-Monitor

A Python-based health check simulation designed to mimic **AWS Load Balancer** and **CloudWatch** monitoring patterns. This project demonstrates how to monitor system availability and trigger automated alerts via multiple communication channels.

## 🚀 Features
- **Health Simulation:** Logic to simulate system health status (200 OK / 500 Internal Server Error).
- **Dual Alerting Methods:** - **SMTP Version:** Sends secure email alerts using Python's `smtplib`.
  - **Webhook Version:** Integrated with external notification services.
- **Security Focused:** Uses **Environment Variables** to handle sensitive credentials, ensuring no passwords are hardcoded in the repository.

## 🛠️ Setup & Usage

### 1. Set Environment Variables

```bash
export EMAIL_PASS='your-16-character-app-password'


