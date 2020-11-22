
# Prerequistes. .

CDK version > 1.41

(1) Pipeline account and region should be boostraped, 

'''cdk bootstrap --profile <yourpipelineprofile>'''

(2) Application accounts and regions shoudl be bootstrap.

'''cdk bootstrap  --trust <accountnumberofpipelineaccount> --cloudformation-execution-policies 'arn:aws:iam::aws:policy/AdministratorAccess' --profile <applcaitonaccontprofile> '''


# Deploy. (once only)
(1) cdk deploy --profile <yourpipelineprofile>
(2) Clone codecommit repo ( that was created in 1 above ). 
(3) Make changes etc ( to either pipeline or application, commit to repo, it will rebuild. 







Need to edit the cdk.json file  must have ""@aws-cdk/core:newStyleStackSynthesis": "true"

