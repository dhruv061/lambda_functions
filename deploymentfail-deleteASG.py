import boto3
import json

def lambda_handler(event, context):
    print("=== RAW EVENT RECEIVED ===")
    print(json.dumps(event, indent=2))

    detail = event.get("detail", {})
    deployment_id = detail.get("deploymentId")
    deployment_group_name = detail.get("deploymentGroup")

    if not deployment_id or not deployment_group_name:
        print("❌ Missing deploymentId or deploymentGroupName.")
        return

    print(f"✅ deploymentId: {deployment_id}")
    print(f"✅ deploymentGroupName: {deployment_group_name}")

    # Create the ASG client
    autoscaling = boto3.client("autoscaling")

    try:
        response = autoscaling.describe_auto_scaling_groups()
        print(f"✅ Retrieved {len(response['AutoScalingGroups'])} ASGs")

        # Search for the matching ASG
        matching_asg = None
        for asg in response["AutoScalingGroups"]:
            asg_name = asg["AutoScalingGroupName"]
            if deployment_id in asg_name and deployment_group_name in asg_name:
                print(f"✅ Matched ASG: {asg_name}")
                matching_asg = asg_name
                break

        if matching_asg:
            print(f"🔥 Deleting ASG: {matching_asg}")
            autoscaling.delete_auto_scaling_group(
                AutoScalingGroupName=matching_asg,
                ForceDelete=True
            )
            print(f"✅ Successfully deleted ASG: {matching_asg}")
        else:
            print("⚠️ No matching ASG found to delete.")

    except Exception as e:
        print(f"❌ Error while deleting ASG: {e}")
        raise
 