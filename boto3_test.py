# for copying the files

import boto3

date = ['13-03-2023', '14-03-2023', '15-03-2023']
session = boto3.Session(
    aws_access_key_id='<key_id>',
    aws_secret_access_key='<secret_key>'
)

s3 = session.resource('s3')
src_bucket = s3.Bucket('src_bucket')
dst_bucket = s3.Bucket('dest_bucket')
count = 0

for obj in src_bucket.objects.filter(Prefix='<start_of_obj>'):   #or objects.all() for retrieving the entire files from bucket
    for i in date:
        if i in obj.key:
            copy_source = {'Bucket': obj.bucket_name, 'Key': obj.key}
            dst_bucket.Object(obj.key).copy(copy_source)
            count += 1
            print(f"{count} objects done")

print('Process over')