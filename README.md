# Maritime AI Governance & Third-Party Risk Management (TPRM) Framework

## 📋 Project Overview

The 2021 Suez Canal blockage highlighted a critical vulnerability in global supply chains: the lack of real-time, predictive routing capabilities. While AI and edge computing offer solutions to prevent such bottlenecks, their integration into critical maritime infrastructure introduces significant **Third-Party Risk Management (TPRM)** and **AI Governance** challenges.

This project demonstrates a comprehensive, framework-aligned GRC approach to assessing an AI-driven edge computing vendor (**NaviEdge Solutions**) for a fictional global logistics company (**NovaTide Logistics**). It bridges the gap between traditional cybersecurity GRC, emerging AI regulations, and automated vendor risk scoring.

---

## 🎯 Scenario

**NovaTide Logistics** is procuring **NaviEdge Solutions**, an AI-powered edge platform that integrates with Port Community Systems (PCS) and vessel IoT/SCADA sensors to predict port congestion and dynamically reroute cargo in real time.

As the GRC Analyst, the objective is to evaluate this vendor and its AI system against global regulatory standards while ensuring operational resilience, data privacy, and algorithmic accountability.

---

## 🏛️ Regulatory & Framework Alignment

This assessment maps risks and controls across multiple international frameworks:

- **EU AI Act**
  - Classifies the routing AI as a **High-Risk AI System** (Annex III, Point 2 – Critical Infrastructure)
  - Evaluates Human Oversight (Article 14) and Accuracy, Robustness & Cybersecurity (Article 15)

- **ISO/IEC 27001:2022**
  - Supplier relationship controls (A.5.19–A.5.23)
  - Physical and edge device security (A.8.20, A.8.22)

- **NIST AI Risk Management Framework (AI RMF)**
  - Aligns with the **MAP**, **MEASURE**, and **GOVERN** functions
  - References GOVERN 6.1 and MEASURE 2.4

- **India Digital Personal Data Protection (DPDP) Act, 2023**
  - Evaluates processor obligations
  - Reviews cross-border data transfer safeguards

---

## 📂 Project Deliverables

### 1. AI-Enhanced TPRM Questionnaire (`TPRM_Questionnaire.xlsx`)

A vendor assessment questionnaire combining traditional cybersecurity controls with AI-specific questions, including:

- Model governance
- Model drift monitoring
- Explainability
- SCADA/IoT edge-device security
- Data privacy controls

### 2. AI Risk Register & Impact Assessment (`AI_Risk_Register.xlsx`)

A structured risk register documenting:

- Inherent vs. residual risk
- Risk owners
- Mitigation strategies
- Regulatory mappings to the EU AI Act and DPDP Act

### 3. Automated Vendor Risk Scoring Script (`vendor_scorer.py`)

A Python CLI application that:

- Reads vendor assessment responses from JSON
- Applies weighted compliance scoring
- Assigns a vendor risk rating
- Flags critical regulatory gaps automatically

### 4. Executive GRC Summary (`Executive_Summary.md`)

An executive-level report summarizing:

- Overall vendor risk posture
- Key compliance gaps
- Business impact
- Recommended remediation roadmap

---

# 🚀 Running the Automation Script

## Prerequisites

- Python 3.x

## Step 1 – Clone the Repository

```bash
git clone https://github.com/samj083/maritime-ai-grc-tprm-framework.git
cd maritime-ai-grc-tprm-framework
```

## Step 2 – Run the Vendor Scoring Script

```bash
python vendor_scorer.py sample_vendor.json
```

---

## 💻 Sample Output

```text
==================================================
   MARITIME AI TPRM RISK ASSESSMENT REPORT
==================================================

Vendor Assessed : NaviEdge Solutions (Mock Maritime AI Assessment)
Compliance Score: 81.67%
Risk Rating     : LOW (Approved)

[!] Key Findings:
    - CRITICAL GAP: Model Drift Monitoring is non-compliant.
    - WARNING: Data Privacy (DPDP/GDPR) is only partially compliant and requires remediation.
    - WARNING: SCADA Edge Device Security is only partially compliant and requires remediation.

==================================================
```

---

## 🧠 Skills Demonstrated

- **Cross-Framework Mapping**
  - Translated requirements from the EU AI Act, ISO/IEC 27001, NIST AI RMF, and India's DPDP Act into measurable vendor controls.

- **AI-Specific Third-Party Risk Management**
  - Evaluated AI lifecycle risks including model drift, explainability, bias, and edge-device security alongside traditional supplier risk.

- **GRC Automation**
  - Built a Python-based scoring engine to automate vendor assessments, improve consistency, and reduce manual review effort.

- **Risk Assessment & Governance**
  - Performed inherent and residual risk analysis with structured remediation planning.

- **Executive Communication**
  - Presented technical and regulatory findings in business-focused language suitable for executive stakeholders.

---

## ⚠️ Disclaimer

**NovaTide Logistics** and **NaviEdge Solutions** are fictional organizations created solely for portfolio demonstration purposes.

The regulations, standards, and governance frameworks referenced - including the **EU AI Act**, **ISO/IEC 27001:2022**, **NIST AI Risk Management Framework**, and **India's Digital Personal Data Protection Act (2023)** - are real. The assessment methodology reflects current industry best practices for AI Governance, Third-Party Risk Management (TPRM), and cybersecurity governance.
