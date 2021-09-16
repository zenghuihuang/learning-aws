import boto3

def main():
    print_bucket_names()
   

if __name__ == "__main__":
    main()

#This function prints the names of Amazon S3 buckets
def print_bucket_names():
    # Use Amazon S3
    s3 = boto3.resource('s3')
    # Print out bucket names
    for bucket in s3.buckets.all():
    print(bucket.name)
