# aws_connector.py
import boto3

def get_iam_client():
    """
    Initialize and return the AWS IAM client.
    """
    return boto3.client('iam')


# iam_analyzer.py
def analyze_iam_user_policies(iam_client, user_name):
    """
    Analyze IAM user policies for a given user.
    """
    try:
        attached_policies = iam_client.list_attached_user_policies(UserName=user_name)
        user_policies = []
        for policy in attached_policies['AttachedPolicies']:
            policy_name = policy['PolicyName']
            policy_details = iam_client.get_policy(PolicyArn=policy['PolicyArn'])
            user_policies.append({
                'PolicyName': policy_name,
                'PolicyDocument': policy_details['Policy']['DefaultVersion']['Document'],
            })
        return user_policies
    except Exception as e:
        raise RuntimeError(f"Error analyzing IAM policies for user '{user_name}': {str(e)}")


# iam_analyzer.py (continued)
def analyze_policy_for_permissions(policy_document, user_name):
    """
    Analyze IAM policy document for overly permissive permissions.
    """
    overly_permissive_statements = []

    for statement in policy_document['Statement']:
        if statement['Effect'] == 'Allow':
            if '*' in statement.get('Action', []) or '*' in statement.get('Resource', []):
                overly_permissive_statements.append(statement)

    if overly_permissive_statements:
        print(f"Vulnerability: Overly permissive permissions in policies for user '{user_name}'")
        print("Recommendation: Review and restrict permissions as needed.")
        for statement in overly_permissive_statements:
            print(f"- Statement: {statement}")

# utils.py
def display_menu_options():
    """
    Display menu options.
    """
    print("1. Analyze IAM Policies")
    print("2. Other Menu Option 1")
    print("3. Other Menu Option 2")
    print("4. Other Menu Option 3")
    print("5. Exit")


def get_user_choice():
    """
    Get user choice from the menu.
    """
    return input("Enter your choice: ")


# menu.py
from functions.aws_connector import get_iam_client
from functions.iam_analyzer import analyze_iam_user_policies, analyze_policy_for_permissions
from functions.utils import display_menu_options, get_user_choice

def main_menu():
    iam_client = get_iam_client()
    while True:
        display_menu_options()
        choice = get_user_choice()

        if choice == '1':
            user_name = input("Enter IAM user name: ")
            user_policies = analyze_iam_user_policies(iam_client, user_name)
            for policy in user_policies:
                analyze_policy_for_permissions(policy['PolicyDocument'], user_name)
        elif choice == '2':
            # Implement other menu options here
            pass
        elif choice == '3':
            # Implement more menu options here
            pass
        elif choice == '4':
            # Implement even more menu options here
            pass
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
