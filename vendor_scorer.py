import json
import sys

def calculate_risk_score(responses):
    # Weights aligned with Maritime AI TPRM priorities (ISO 27001, EU AI Act, NIST AI RMF)
    weights = {
        "eu_ai_act_conformity": 20,
        "iso27001_supplier_security": 15,
        "data_privacy_dpdp_gdpr": 15,
        "model_drift_monitoring": 10,
        "human_in_loop_override": 10,
        "scada_edge_device_security": 15,
        "incident_response_sla": 10,
        "sub_processor_disclosure": 5
    }
    
    total_score = 0
    max_possible = sum(weights.values()) * 3 # Max score if all controls score a 3
    findings = []
    
    for key, weight in weights.items():
        val = responses.get(key, 1) 
        total_score += val * weight
        
        # Flag critical gaps (Score of 1 or 2 in high-weight areas)
        if val == 1:
            findings.append(f"CRITICAL GAP: {key.replace('_', ' ').title()} is non-compliant.")
        elif val == 2 and weight >= 15:
            findings.append(f"WARNING: {key.replace('_', ' ').title()} is only partially compliant and requires remediation.")
            
    percentage = (total_score / max_possible) * 100
    return percentage, findings

def main():
    if len(sys.argv) < 2:
        print("Usage: python vendor_scorer.py <path_to_json_file>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the path.")
        sys.exit(1)
        
    vendor_name = data.get("vendor_name", "Unknown Vendor")
    responses = data.get("responses", {})
    
    score, findings = calculate_risk_score(responses)
    
    print("\n" + "="*50)
    print("   MARITIME AI TPRM RISK ASSESSMENT REPORT")
    print("="*50)
    print(f"Vendor Assessed : {vendor_name}")
    print(f"Compliance Score: {score:.2f}%")
    
    if score < 60:
        print("Risk Rating     : HIGH (Do Not Procure / Require Major Remediation)")
    elif score < 80:
        print("Risk Rating     : MEDIUM (Conditional Approval with Remediation Plan)")
    else:
        print("Risk Rating     : LOW (Approved)")
        
    if findings:
        print("\n[!] Key Findings:")
        for finding in findings:
            print(f"    - {finding}")
    else:
        print("\n[+] No critical gaps identified.")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()