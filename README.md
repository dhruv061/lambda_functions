# Lambda Functions
Details about all functions!!

## 1 - deploymentfail-deleteASG.py

``
Python 3.13
``

Delete ASG when Blue-green Pipeline failed,  <br/>

- In lambda function goes --> Configuration --> Enviroment variable and add below enviroment variable,

|  Key       | Value          |
|----------------------|----------------------|
| `DEPLOYMENT_GROUP_NAME`        | Your_deployment_grp_name    |

- ie.

![ eploymentfail_delete_asg ](.images/deploymentfail_delete_asg.png)

## 2 - cloudfront-invalidation-pipeline.py
``
Python 3.12
``
Invalidate Cloudfront in AWS Code Pipeline,  <br/>

## 3 - assets-s3-cloudfront-invalidation.py
``
Python 3.13
``

This is for Assets S3 bucket when we put cludfront above S3 assets, This invalidate in cloudfront when new images push in bucket,  <br/>

- In lambda function goes --> Configuration --> Enviroment variable and add below enviroment variable,

|  Key       | Value          |
|----------------------|----------------------|
| `CLOUDFRONT_DIST_ID`        | Your_cloudfront_dist_id    |

- ie.

![ eploymentfail_delete_asg ](.images/assets_s3_invalidate.png)
