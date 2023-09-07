# functions/analyze_iam_user_policies.py
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
