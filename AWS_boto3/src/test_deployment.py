from src.ec2.vpc import VPC
from src.client_locator import EC2Client

def main():
    #create a VPC
    ec2_client = EC2Client().get_client()
    vpc = VPC(ec2_client)

    vpc_responce = vpc.create_vpc()

    print('VPC created: '+str(vpc_responce))

if __name__=='__main__':
    main()