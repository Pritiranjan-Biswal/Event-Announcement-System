# ⚙️ Detailed Setup: Event Announcement System

This guide explains how to deploy and test the Event Announcement System step-by-step using **AWS Lambda**, **API Gateway**, and **SNS**.

---

## 🧩 AWS Services Used

| Service | Purpose |
|----------|----------|
| **Amazon API Gateway** | Exposes a public REST API endpoint |
| **AWS Lambda** | Executes the backend logic (publishes messages to SNS) |
| **Amazon SNS** | Sends notifications to subscribers |
| **IAM** | Provides permissions for Lambda to access SNS |
| **CloudWatch** | Monitors and logs Lambda executions |

---

## 🪶 Steps to Build

### 1️⃣ Create SNS Topic
- Go to **Amazon SNS → Topics → Create Topic**
- Choose *Standard*, name it `event-announcements`
- Copy the **Topic ARN**
- Add an **Email subscription** and confirm from your inbox

![SNS Topic](./screenshots/sns-topic.png)

---

### 2️⃣ Create Lambda Function
- Go to **AWS Lambda → Create Function**
- Runtime: *Python 3.11*
- Add SNS publish permissions
- Paste your Lambda code

![Lambda Config](./screenshots/lambda-config.png)

---

### 3️⃣ Create API Gateway
- Create a **REST API**
- Resource: `/publish-event`
- Method: `POST` → Integrate with Lambda
- Add **Mapping Template**:
  ```json
  { "body": $input.body }
