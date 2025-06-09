import boto3
import os
import logging

# Initialize boto3 clients
s3 = boto3.client('s3')
cloudfront = boto3.client('cloudfront')

# Environment variables for the CloudFront distribution ID
CLOUDFRONT_DIST_ID = os.environ['CLOUDFRONT_DIST_ID']

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Get the S3 bucket name and object key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        logger.info(f"New image uploaded to S3: {object_key} in bucket {bucket_name}")

        # Define the CloudFront invalidation path (we'll invalidate the specific image)
        invalidation_path = f"/{object_key}"

        # Create the CloudFront invalidation request
        invalidation_response = cloudfront.create_invalidation(
            DistributionId=CLOUDFRONT_DIST_ID,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [invalidation_path],
                },
                'CallerReference': str(context.aws_request_id),  # Unique value for the invalidation
            }
        )

        logger.info(f"Invalidation request sent for {invalidation_path}. Invalidation ID: {invalidation_response['Invalidation']['Id']}")

    except Exception as e:
        logger.error(f"Error occurred while processing the event: {str(e)}")
        raise e
 