import boto3

# Create an S3 client
s3 = boto3.client('s3')


'''
# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)
'''

# Create an S3 client
#s3 = boto3.client('s3')

filename = 'C:/Users/Mostie/Downloads/installer.php'
bucket_name = 'mostie-algemeen'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)