# AWS S3 Setup Guide for SGD Events

## How It Works

### Local Development (Default - No Setup Needed)
- **Storage**: Local `media/` folder
- **Image URLs**: `http://127.0.0.1:8000/media/food/image.jpg`
- **No AWS credentials required**
- **Works immediately** ✅

### Production (Render with S3)
- **Storage**: AWS S3 bucket
- **Image URLs**: `https://your-bucket.s3.amazonaws.com/media/food/image.jpg`
- **Requires AWS setup**
- **Persistent storage** (images don't disappear on deploy) ✅

## AWS S3 Setup Steps

### Step 1: Create AWS Account
1. Go to https://aws.amazon.com/
2. Sign up for free tier (12 months free)
3. Verify email and add payment method (won't be charged for free tier usage)

### Step 2: Create S3 Bucket
1. Log into AWS Console
2. Search for **S3** service
3. Click **Create bucket**
4. Configure:
   - **Bucket name**: `sgd-events-media` (must be globally unique)
   - **AWS Region**: `ap-south-1` (Mumbai) or your preferred region
   - **Object Ownership**: ACLs enabled
   - **Block Public Access**: UNCHECK "Block all public access" ⚠️
   - **Bucket Versioning**: Disabled
5. Click **Create bucket**

### Step 3: Configure Bucket CORS
1. Open your bucket
2. Go to **Permissions** tab
3. Scroll to **Cross-origin resource sharing (CORS)**
4. Click **Edit** and paste:

```json
[
    {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": ["ETag"],
        "MaxAgeSeconds": 3000
    }
]
```

5. Click **Save changes**

### Step 4: Configure Bucket Policy (Make Files Public)
1. Still in **Permissions** tab
2. Scroll to **Bucket policy**
3. Click **Edit** and paste (replace `sgd-events-media` with your bucket name):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::sgd-events-media/*"
        }
    ]
}
```

4. Click **Save changes**

### Step 5: Create IAM User for Django
1. Search for **IAM** service in AWS Console
2. Click **Users** → **Create user**
3. User details:
   - **User name**: `sgd-events-django`
   - Click **Next**
4. Set permissions:
   - Select **Attach policies directly**
   - Search and select: **AmazonS3FullAccess**
   - Click **Next**
5. Review and click **Create user**

### Step 6: Create Access Keys
1. Click on the newly created user
2. Go to **Security credentials** tab
3. Scroll to **Access keys**
4. Click **Create access key**
5. Select **Application running outside AWS**
6. Click **Next** → **Create access key**
7. **IMPORTANT**: Copy and save:
   - **Access key ID** (e.g., )
   - **Secret access key** ()
   - You cannot see the secret key again!
8. Click **Done**

## Environment Variables Setup

### For Render.com Deployment

1. Go to your Render dashboard
2. Select your web service
3. Go to **Environment** tab
4. Add these variables:

| Key | Value | Example |
|-----|-------|---------|
| `USE_S3` | `True` | `True` |
| `AWS_ACCESS_KEY_ID` | Your access key | `` |
| `AWS_SECRET_ACCESS_KEY` | Your secret key | `...` |
| `AWS_STORAGE_BUCKET_NAME` | Your bucket name | `sgd-events-media` |
| `AWS_S3_REGION_NAME` | Your region | `ap-south-1` |

5. Click **Save Changes**
6. Your service will automatically redeploy

## Testing

### Test Locally (Optional - if you want to test S3 before deploying)

1. Install packages:
```bash
pip install django-storages boto3
```

2. Create `.env` file in project root:
```
USE_S3=True
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_STORAGE_BUCKET_NAME=sgd-events-media
AWS_S3_REGION_NAME=ap-south-1
```

3. Install python-dotenv:
```bash
pip install python-dotenv
```

4. Add to top of `settings.py` (after imports):
```python
from dotenv import load_dotenv
load_dotenv()
```

5. Run server and test upload:
```bash
python manage.py runserver
```

6. Go to admin → Add food item with image
7. Check your S3 bucket - image should appear!

### Test in Production (Render)

1. Deploy to Render with environment variables set
2. Go to admin panel: `https://your-app.onrender.com/admin/`
3. Add a food item with image
4. Check S3 bucket - image should be there
5. View food list page - images should load from S3

## File Organization in S3

Your bucket will look like:
```
sgd-events-media/
└── media/
    ├── food/
    │   ├── image1.jpg
    │   └── image2.png
    ├── food/gallery/
    │   └── gallery1.jpg
    ├── venues/
    │   └── venue1.jpg
    └── jewellery/
        └── item1.jpg
```

## Cost Estimate

### AWS Free Tier (First 12 months):
- ✅ 5 GB storage
- ✅ 20,000 GET requests/month
- ✅ 2,000 PUT requests/month
- ✅ 100 GB data transfer out

### After Free Tier:
- Storage: $0.023/GB/month
- GET requests: $0.0004 per 1,000 requests
- PUT requests: $0.005 per 1,000 requests

**Example costs for small app:**
- 1000 images (2GB): $0.05/month
- 10,000 page views: $0.004/month
- **Total: ~$0.10 - $0.50/month** 💰

## Troubleshooting

### Images not uploading
- ✅ Check `USE_S3=True` in environment variables
- ✅ Verify AWS credentials are correct
- ✅ Check IAM user has S3FullAccess policy
- ✅ Check Django logs for errors

### Images not displaying (403 errors)
- ✅ Verify bucket policy allows public read
- ✅ Check CORS configuration
- ✅ Ensure bucket public access is allowed
- ✅ Verify image URLs in browser console

### Images disappear after upload
- ✅ Make sure you're using S3 (check `USE_S3=True`)
- ✅ Without S3, Render deletes files on each deploy
- ✅ Check S3 bucket to confirm files are there

### Access Denied errors
- ✅ Verify IAM user has correct permissions
- ✅ Check bucket policy is set correctly
- ✅ Ensure AWS credentials are correct (no spaces/typos)

## Switching Between Local and S3

### Use Local Storage (Development):
```
# Don't set USE_S3, or set it to False
USE_S3=False
```

### Use S3 Storage (Production):
```
USE_S3=True
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_STORAGE_BUCKET_NAME=...
AWS_S3_REGION_NAME=...
```

**The app automatically switches!** No code changes needed.

## Security Best Practices

1. ✅ **Never commit AWS credentials to Git**
   - `.env` is in `.gitignore`
   - Use environment variables only

2. ✅ **Rotate access keys regularly**
   - Every 90 days recommended
   - Immediately if exposed

3. ✅ **Use IAM user with minimal permissions**
   - Only S3 access needed
   - No admin or root access

4. ✅ **Monitor AWS costs**
   - Set up billing alerts
   - Check monthly usage

## Migration from Local to S3

If you already have images locally and want to upload to S3:

```bash
# Install AWS CLI
pip install awscli

# Configure
aws configure
# Enter your access key ID
# Enter your secret access key
# Enter region (ap-south-1)
# Enter output format (json)

# Upload local media to S3
aws s3 sync media/ s3://sgd-events-media/media/ --acl public-read
```

## Support Resources

- **AWS S3 Documentation**: https://docs.aws.amazon.com/s3/
- **Django-storages**: https://django-storages.readthedocs.io/
- **Boto3**: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

---

## Quick Checklist

Before deploying to Render:

- [ ] S3 bucket created
- [ ] Bucket policy configured (public read)
- [ ] CORS configured
- [ ] IAM user created
- [ ] Access keys generated and saved
- [ ] Environment variables added to Render
- [ ] `USE_S3=True` set in Render
- [ ] Deploy and test upload

**Status**: ✅ Ready to Deploy  
**Last Updated**: January 7, 2026
