# aws_list_ec2_rds_instances

## Code by Ronin1770

## Free Code for AWS Boto3 API

My Webiste: - [Farhan Munir @Instagram](https://www.instagram.com/munirfarhan/)
## Features
This code library allows you to:
- Get the list of EC2 Instances across all available regions (for your account)
- Start and Stop EC2 Instances
- Get the list of RDS Instances across all available regions (for your account)
- Start and Stop RDS Instances
- Query AWS CostExplorer API to get Amortized and Unblended costs for up to a period of 12 months

# Prerequisites 
- Python 3.7 or higher
- Python pip installer for Boto3
- Boto3 SDK for python. You can install using:
```
    pip install boto3
```
- AWS API User's API Key and Key_Secret. You will need to add them on line #16 and #17 of the Python file.

```
import boto3
import json

class aws_features_controller:

	AWS_KEY    = "<YOUR API KEY>"
	AWS_SECRET = "<YOUR API SECRET>"
```

- AWS API User with followinig privileges
-- AmazanEC2FullAccess
-- AmazanRDSFullAccess
-- Inline Policy for CostExplorer with following rules:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ce:GetRightsizingRecommendation",
                "ce:GetCostAndUsage",
                "ce:GetSavingsPlansUtilization",
                "ce:GetReservationPurchaseRecommendation",
                "ce:ListCostCategoryDefinitions",
                "ce:GetCostForecast",
                "ce:GetPreferences",
                "ce:ListTagsForResource",
                "ce:GetReservationUtilization",
                "ce:GetCostCategories",
                "ce:GetSavingsPlansPurchaseRecommendation",
                "ce:GetDimensionValues",
                "ce:GetSavingsPlansUtilizationDetails",
                "ce:GetCostAndUsageWithResources",
                "ce:ListCostAllocationTags",
                "ce:DescribeReport",
                "ce:GetReservationCoverage",
                "ce:GetSavingsPlansCoverage",
                "ce:DescribeNotificationSubscription",
                "ce:GetTags",
                "ce:GetUsageForecast"
            ],
            "Resource": "*"
        }
    ]
}
```

#Running the Code

You can execute the code using the following syntax (based on your system):

```
>python aws_features_controller 
```
or 

```
>python3 aws_features_controller 
```

# Get the list of all Instances

## Arguments
None

## Sample code:

```
if __name__ == '__main__':
	afc = aws_features_controller()
print( "Getting all of the EC2 Instances\n")
	
	print( afc.get_all_ec2_instances() )
```

# Start the EC2 Instance:

## Arguments

- Instance ID: i-11111e2222222e (for example)
- Flag: True
- Region: us-east-1

```
## Sample code:
if __name__ == '__main__':
	afc = aws_features_controller()
	print( afc.toggle_ec2_instance( "i-11111e2222222e", "us-east-1",True ) )
```	

# Stop the EC2  Instance

## Arguments
- Instance ID: i-11111e2222222e (for example)
- Flag: False
- Region: us-east-1

## Sample code:

```
if __name__ == '__main__':
	afc = aws_features_controller()
	print( afc.toggle_ec2_instance( "i-11111e2222222e", "us-east-1",False ) )
```	

# Getting the List of RDS Instances
## Arguments
None:

## Sample Code
```
if __name__ == '__main__':

	afc = aws_features_controller()
	print( afc.get_all_rds_instances() )
```

# Starting RDS Instance
## Arguments

- DBIdentifier: xxxxx-tttt-1
- Availability_zone: us-east-1
- Flag: True

## Sample Code
```
if __name__ == '__main__':

	afc = aws_features_controller()
	print ( afc.toggle_rds_instance( "xxxxx-tttt-1", "us-east-1", True )  )
```

# Stopping RDS Instance
## Arguments
- DBIdentifier: xxxxx-tttt-1
- Availability_zone: us-east-1
- Flag: False

## Sample Code
```
if __name__ == '__main__':

	afc = aws_features_controller()
	print ( afc.toggle_rds_instance( "xxxxx-tttt-1", "us-east-1", False)  )
```

# Get Costing over time
## Arguments
- Start Date: 2022-01-01
- End Date: 2022-10-28
- Aggregation: MONTHLY

## Sample code:
```
if __name__ == '__main__':

	afc = aws_features_controller()
	print( afc.get_costs("2022-01-01","2022-10-28", "MONTHLY") )
```
