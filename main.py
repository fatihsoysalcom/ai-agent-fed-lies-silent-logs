import logging

# Configure basic logging to simulate traditional system logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def assess_credit_risk(applicant_data):
    """
    Simulates a simple AI agent assessing credit risk based on provided data.
    In a real scenario, this would be a complex machine learning model.
    """
    income = applicant_data.get('income', 0)
    debt = applicant_data.get('debt', 0)
    credit_score = applicant_data.get('credit_score', 0)

    # Simple rule-based risk assessment for demonstration
    if credit_score < 600:
        risk_level = "High"
    elif credit_score < 700 and income / (debt + 1) < 2.0: # Income-to-debt ratio
        risk_level = "Medium"
    else:
        risk_level = "Low"

    decision = "Approved" if risk_level == "Low" else "Denied"
    return decision, risk_level

def log_ai_decision(applicant_id, processed_data, decision, risk_level):
    """
    Simulates a traditional logging system for AI decisions.
    It logs the data *as seen by the AI* and its decision.
    Crucially, it does NOT inherently detect if the input data was manipulated.
    """
    logging.info(f"Applicant ID: {applicant_id}")
    # This log entry shows the data the AI processed. If this data was manipulated,
    # the log itself won't indicate that fact, making the manipulation 'silent'.
    logging.info(f"  Processed Data: {processed_data}")
    logging.info(f"  Decision: {decision}, Risk Level: {risk_level}")

def main():
    print("--- Demonstrating AI Agent with Legitimate Data ---")
    applicant_id_1 = "APP001"
    legitimate_data = {
        'income': 70000,
        'debt': 20000,
        'credit_score': 720
    }
    print(f"Original (true) data for {applicant_id_1}: {legitimate_data}")

    decision_1, risk_1 = assess_credit_risk(legitimate_data)
    log_ai_decision(applicant_id_1, legitimate_data, decision_1, risk_1)
    print(f"AI Decision for {applicant_id_1}: {decision_1} (Risk: {risk_1})\n")

    print("--- Demonstrating AI Agent with Manipulated Data ---")
    applicant_id_2 = "APP002"
    # This applicant should be high risk based on their true financial situation
    original_high_risk_data = {
        'income': 30000,
        'debt': 25000,
        'credit_score': 550 # Truly high risk
    }
    print(f"Original (true) data for {applicant_id_2}: {original_high_risk_data}")

    # Simulate data manipulation: an attacker boosts credit score and income,
    # and reduces debt to make a high-risk applicant appear low-risk.
    manipulated_data = {
        'income': 80000,
        'debt': 10000,
        'credit_score': 750 # Artificially boosted
    }
    print(f"Manipulated data fed to AI for {applicant_id_2}: {manipulated_data}")

    decision_2, risk_2 = assess_credit_risk(manipulated_data)
    # The log records the manipulated data and the decision based on it.
    # It does NOT show the 'original_high_risk_data' or flag the manipulation.
    # This is where the logs become 'silent' about the lie.
    log_ai_decision(applicant_id_2, manipulated_data, decision_2, risk_2)
    print(f"AI Decision for {applicant_id_2}: {decision_2} (Risk: {risk_2})")

    print("\n--- Observation ---")
    print("The log for APP002 shows 'Processed Data' as the manipulated data.")
    print("The AI's decision appears legitimate based on *that* data, without revealing the underlying manipulation.")
    print("This demonstrates how traditional logs can be 'silent' about 'lies' fed to AI agents,")
    print("making it hard to detect malicious data inputs or system vulnerabilities.")

if __name__ == "__main__":
    main()
