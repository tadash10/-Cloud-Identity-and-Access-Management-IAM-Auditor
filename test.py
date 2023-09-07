import boto3

def analyze_iam_policies():
    # Initialize the AWS IAM client
    iam_client = boto3.client('iam')

    # Get a list of all IAM users
    users = iam_client.list_users()

    # Iterate through each IAM user
    for user in users['Users']:
        user_name = user['UserName']
        print(f"Analyzing IAM User: {user_name}")

        # Get the attached policies for the user
        attached_policies = iam_client.list_attached_user_policies(UserName=user_name)

        # Analyze user's attached policies
        for policy in attached_policies['AttachedPolicies']:
            analyze_policy(policy['PolicyName'], user_name)

def analyze_policy(policy_name, user_name):
    # Initialize the AWS IAM client
    iam_client = boto3.client('iam')

    # Get the policy details
    policy = iam_client.get_policy(PolicyArn=policy_name)

    # Analyze the policy for permissions
    statements = policy['Policy']['DefaultVersion']['Document']['Statement']
    for statement in statements:
        if statement['Effect'] == 'Allow':
            # Check for overly permissive permissions
            if '*' in statement['Action'] or '*' in statement['Resource']:
                print(f"Vulnerability: Overly permissive permissions in policy '{policy_name}' for user '{user_name}'")
                # Add logic for recommendations on remediation

if __name__ == "__main__":
    analyze_iam_policies()
