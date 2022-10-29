"""
	Name: aws_features_controller.py
	Date: Oct-27-2022
	Python version used: Python 3.9.5
	Description: This code / library extracts information about running Ec2 / RDS instances. Also the aggregate billing for the given month / year
	Developer : Farhan Munir
	Website: https://www.instagram.com/munirfarhan/
	
"""

import boto3
import json

class aws_list_ec2_rds_instances:

	AWS_KEY    = "<YOUR API KEY>"
	AWS_SECRET = "<YOUR API SECRET>"
	regions    = []
	
	def __init__(self):
		print("Initiating.....")
		self.regions = self.get_all_availability_zones()
	
		
	#this method retrieves the list of availability zones available for this customer/ credentials
	def get_all_availability_zones(self):
		ret = []
		ec2resource = boto3.client('ec2', aws_access_key_id=self.AWS_KEY, aws_secret_access_key=self.AWS_SECRET)
		
		regions = ec2resource.describe_regions()
		
		for region in regions['Regions']:
			
			ret.append(region['RegionName'])
		
		return ret
		
	
	################################## Functions for EC2 #######################
	
	#This method will get the list of all EC2 instances	
	def get_all_ec2_instances(self):
		ret = []
		
		try:
		
			for region in self.regions:
				# print("\nGetting data for Region:", region)	
				ec2resource = boto3.client('ec2', region_name=region, aws_access_key_id=self.AWS_KEY, aws_secret_access_key=self.AWS_SECRET)    
				reservations = ec2resource.describe_instances()
				
				for reservation in reservations['Reservations']:
					for instance in reservation['Instances']:
						ind = {}
						ind['ImageId'] = instance['ImageId']
						ind['InstanceId'] = instance['InstanceId']
						ind['InstanceType'] = instance['InstanceType']
						ind['LaunchTime'] = instance['LaunchTime']
						ind['PrivateDnsName'] = instance['PrivateDnsName']
						ind['PrivateIpAddress'] = instance['PrivateIpAddress']
						ind['State'] = instance['State']
						ind['Tags'] = instance['Tags']
						ind['region'] = region
						
						
						ret.append(ind) 
		except:
			print("Exception in getting all Instances")
			return None
				
		return ret
	
	#This method will toggle EC2 instance's state based on the provided flag and the given instance id
	#If flag == True => will turn the instance
	#Else => will turn off
	def toggle_ec2_instance(self, instance_id, availability_zone, flag):
		try:
			ec2resource = boto3.client('ec2', region_name=availability_zone, aws_access_key_id=self.AWS_KEY, aws_secret_access_key=self.AWS_SECRET)    
			if( flag == True):
				print(  f"Attempting to start instance_id: %s in %s" % (instance_id, availability_zone)  )
				
				return ec2resource.start_instances( InstanceIds=[ instance_id ] )
				
				
			else:
				print(  f"Attempting to stop instance_id: %s in %s" % (instance_id, availability_zone)  )
				
				return ec2resource.stop_instances( InstanceIds=[ instance_id ] )
		except Exception as e:
			print("Exception in toggling instance state: %s " % (str(e)))
			return None
		
	
	################################## Functions for RDS    #######################
	def get_all_rds_instances(self):
		ret = []
		
		for region in self.regions:
				# print("\nGetting data for Region:", region)	
				rds_client = boto3.client('rds', region_name=region, aws_access_key_id=self.AWS_KEY, aws_secret_access_key=self.AWS_SECRET)    
				db_instances = rds_client.describe_db_instances()
		
				for db_instance in db_instances['DBInstances']:
					ind = {}
					ind['DBInstanceIdentifier'] = db_instance['DBInstanceIdentifier']
					ind['DBInstanceClass'] = db_instance['DBInstanceClass']
					ind['Engine'] = db_instance['Engine']
					ind['DBInstanceStatus'] = db_instance['DBInstanceStatus']
					ind['Endpoint'] = db_instance['Endpoint']
					ind['Region'] = region
					ret.append(ind)
		return ret
		
	def toggle_rds_instance(self,instance_id, availability_zone, flag):
		try:
			rds_client = boto3.client('rds', region_name=availability_zone, aws_access_key_id=self.AWS_KEY, aws_secret_access_key=self.AWS_SECRET)    
			if( flag == True):
				print(  f"Attempting to start instance_id: %s in %s" % (instance_id, availability_zone)  )
				
				return rds_client.start_db_instance( DBInstanceIdentifier= instance_id  )
				
				
			else:
				print(  f"Attempting to stop instance_id: %s in %s" % (instance_id, availability_zone)  )
				
				return rds_client.stop_db_instance(  DBInstanceIdentifier= instance_id  )
		except Exception as e:
			print("Exception in toggling instance state: %s " % (str(e)))
			return None
	
	
	################################## Functions for RDS    #######################
	def get_costs(self, start_date, end_date, granularity):
		ret = []
		
		try:
			cost_client =boto3.client("ce", aws_access_key_id=self.AWS_KEY, aws_secret_access_key=self.AWS_SECRET) 
			
			print(cost_client.get_cost_and_usage( 
				TimePeriod={
					"Start":start_date, 
					"End":end_date } ,
					Granularity=granularity,
					Metrics=["AMORTIZED_COST", "UNBLENDED_COST"],
				)
			)
		
		except Exception as e:
			print("Exception in get_costs: %s " % (str(e)))
			return None
	
	

if __name__ == '__main__':

	afc = aws_list_ec2_rds_instances()
	
	print( "Getting all of the EC2 Instances\n")
	
	print( afc.get_all_ec2_instances() )
	
	print( afc.toggle_ec2_instance( "<EC2 INSTANCE ID>", "<AWS REGION OF THE Instance>",  True ) )
	
	print( "Getting all of the RDS Instances\n")
	
	print( afc.get_all_rds_instances() )
	
	print ( afc.toggle_rds_instance( "<EC2 INSTANCE ID>", "<AWS REGION OF THE Instance>",  True ) )
	
	print( afc.get_costs("<START DATE>","<END DATE>", "MONTHLY") )
	
	