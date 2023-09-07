# aws_connector.py (continued)
def get_iam_usernames(iam_client):
    """
    Get a list of IAM usernames.
    """
    try:
        users = iam_client.list_users()
        return [user['UserName'] for user in users['Users']]
    except Exception as e:
        raise RuntimeError(f"Error fetching IAM usernames: {str(e)}")


# iam_analyzer.py (continued)
def analyze_user_iam_permissions(iam_client, user_name):
    """
    Analyze IAM user permissions.
    """
    try:
        user_permissions = iam_client.list_user_policies(UserName=user_name)['PolicyNames']
        return user_permissions
    except Exception as e:
        raise RuntimeError(f"Error analyzing IAM permissions for user '{user_name}': {str(e)}")


# menu.py (continued)
def analyze_all_iam_users(iam_client):
    """
    Analyze IAM policies and permissions for all users.
    """
    try:
        usernames = get_iam_usernames(iam_client)
        for username in usernames:
            print(f"Analyzing IAM User: {username}")
            user_policies = analyze_iam_user_policies(iam_client, username)
            for policy in user_policies:
                analyze_policy_for_permissions(policy['PolicyDocument'], username)
            user_permissions = analyze_user_iam_permissions(iam_client, username)
            print(f"IAM Policies for {username}: {user_policies}")
            print(f"IAM Permissions for {username}: {user_permissions}")
    except Exception as e:
        print(f"Error analyzing IAM users: {str(e)}")
