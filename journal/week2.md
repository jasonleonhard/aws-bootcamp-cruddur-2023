# Week 2 — Distributed Tracing


# HONEYCOMB.IO SECTION 



# XRAY SECTION 

### Main files to pay attention to 

user_activities.py, messages.py, message_groups.py, .env of all importance, docker-compose.yml
when at https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/activities/@jasonleonhard


### ISSUE: "exception.message": "UserActivities.run() missing 1 required positional argument: 'user_handle'",

SOLVED: I did it badd adding that positional argument. Which was suprisingly challenging to track down at first, but I got there. 

### then the issue was 

2023-03-07T03:49:38Z [Error] Sending segment batch failed with: InvalidSignatureException: 
        status code: 403, request id: e62d2d6c-5d34-42c7-a9af-bcb3aac990ad

attempting: https://olley.hashnode.dev/aws-free-cloud-bootcamp-instrumenting-aws-x-ray-subsegments
aws xray create-group \
   --group-name "Cruddur" \
   --filter-expression "service(\"backend-flask\")"

and 
aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json
both errored similarly
An error occurred (UnrecognizedClientException) when calling the CreateSamplingRule operation: The security token included in the request is invalid.

adding aws cli to gitpod (bc it was only on my local machine before)
  pip3 install awscli --upgrade --user

then on local machine 
  cat ~/.aws/credentials

aws configure list # did not show what I expected
aws configure --profile choom # enter.....
aws configure list # still did not show what I expected
aws configure --profile choom list # shows what I expected

aws configure --profile choom
AWS Access Key ID [None]: ENTER HERE
AWS Secret Access Key [None]: ENTER HERE
Default region name [None]: us-east-1
Default output format [None]: json

back to gitpod using those creds... 
  aws configure
I also added us-east-1 and None for the other two question answers 
to start the app 
docker compose up

aws-bootcamp-cruddur-2023-backend-flask-1      | botocore.exceptions.ClientError: An error occurred (InvalidSignatureException) when calling the GetSamplingRules operation: The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation for details.

verify with 
ps aux | grep xray 
and 
brew install netcat
nc -zv localhost 2000
brew remove netcat

right click amazon/aws-xray-daemon and open in browser gives: https://2000-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/
but that does not seem to help

https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:settings/groups
removed Cruddur bc appeared to have wrong credentals and doing again 
gitpod cd to backend /workspace/aws-bootcamp-cruddur-2023/backend-flask
then 
attempting: 
aws xray create-group \
   --group-name "Cruddur" \
   --filter-expression "service(\"backend-flask\")"
output this 
{
    "Group": {
        "GroupName": "Cruddur",
        "GroupARN": "arn:aws:xray:us-east-1:811147495294:group/Cruddur/BDMTEYWF47OHAJFZQXKPPWK7LQG6R27KIERLFCW6PRWFX2YKU3ZQ",
        "FilterExpression": "service(\"backend-flask\")",
        "InsightsConfiguration": {
            "InsightsEnabled": false,
            "NotificationsEnabled": false
        }
    }
}
# and then cd back to root of project and run 
aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json
  An error occurred (InvalidRequestException) when calling the CreateSamplingRule operation: Sampling rule already exists
we can see it here
 https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:settings/sampling-rules
starting and stoping the docker container and attaching a shell to xray daemon we got this 
      *  Executing task: docker logs --tail 1000 -f 9f7fcd79ea86ea8d748be5158da87db26f08ed301964ea4278cbdafa87809eab 
      2023-03-07T04:29:18Z [Info] Initializing AWS X-Ray daemon 3.3.6
      2023-03-07T04:29:18Z [Info] Using buffer memory limit of 643 MB
      2023-03-07T04:29:18Z [Info] 10288 segment buffers allocated
      2023-03-07T04:29:18Z [Info] Using region: us-east-1
      2023-03-07T04:29:27Z [Error] Get instance id metadata failed: RequestError: send request failed
      caused by: Get "http://169.254.169.254/latest/meta-data/instance-id": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
      2023-03-07T04:29:27Z [Info] HTTP Proxy server using X-Ray Endpoint : https://xray.us-east-1.amazonaws.com
      2023-03-07T04:29:27Z [Info] Starting proxy http server on 0.0.0.0:2000

The AWS X-Ray daemon requires access to the EC2 instance metadata to retrieve information about the instance and the environment in which it is running. This information is used to create trace data and to determine the sampling rate for traces.
If the daemon is running in an environment that does not provide access to instance metadata, such as a local development environment or a container without an EC2 instance profile, it will be unable to retrieve this information and will not function correctly.
In the case of running the daemon in a Docker container, the --net=host option is required to allow the container to access the host network stack and retrieve the instance metadata. Without this option, the container will not be able to access the metadata and the daemon will not work properly.

and after I set my xray-daemon .env correctly for each area we finally could use xray 
aws-bootcamp-cruddur-2023-backend-flask-1      | 192.168.82.71 - - [07/Mar/2023 04:40:46] "GET /api/messages/@jasonleonhard HTTP/1.1" 200 -
aws-bootcamp-cruddur-2023-xray-daemon-1        | 2023-03-07T04:40:46Z [Info] Successfully sent batch of 1 segments (0.091 seconds)

rules still look the same 
https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:settings/sampling-rules
https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:settings/groups

however we finally have a trace in 
https://us-east-1.console.aws.amazon.com/xray/home?region=us-east-1#/service-map
https://us-east-1.console.aws.amazon.com/xray/home?region=us-east-1#/analytics?timeRange=PT5M

by creating them at these endpoints and frontend routes 
https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/messages/
https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/message_groups
https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/messages/@jasonleonhard
https://3000-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/messages
https://3000-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/messages/@jasonleonhard
https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:traces/query


# CLOUD WATCH LOGS SECTION 

### directions

  https://pypi.org/project/watchtower/

### install

  pip install watchtower

### hit endpoint

  https://4567-jasonleonha-awsbootcamp-f5djeabluiq.ws-eu89.gitpod.io/api/messages/@jasonleonhard

### aws console

  https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#
  https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups
  https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/cruddur
  https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/cruddur/log-events/48c7c3872689$252F$252Fusr$252Flocal$252Flib$252Fpython3.10$252Fsite-packages$252Fflask$252F__main__.py$252Fapp$252F28

### for spend considerations I have now disabled CloudWatch logs and WatchTower

    in the future I can look at these files for ease of re-setup

    .env, requirements.txt, app.py, home_activities.py