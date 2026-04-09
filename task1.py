# =================================================================
# PROJECT: Cloud Storage Configuration (AWS S3)
# DESCRIPTION: Automating Bucket creation, File Upload, and Permissions.
# DELIVERABLE: Python script demonstrating Cloud Bucket management.
# =================================================================

# Note: In a real environment, you need 'pip install boto3' 
# and configured AWS Credentials (AWS_ACCESS_KEY, AWS_SECRET_KEY).

class S3CloudManager:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.cloud_storage = {} # Simulating Cloud Storage Space
        print(f"☁️ Initializing Cloud Connection to AWS S3...")
        print(f"🪣 Target Bucket: {self.bucket_name}")

    def create_bucket(self, region="us-east-1"):
        """Simulates S3 Bucket Creation."""
        print(f"✅ Success: Bucket '{self.bucket_name}' created in region '{region}'.")
        self.cloud_storage[self.bucket_name] = []
        return True

    def upload_file(self, file_name, content):
        """Simulates uploading a file to the S3 bucket."""
        print(f"📤 Uploading '{file_name}' to S3...")
        file_metadata = {
            "name": file_name,
            "content": content,
            "size": f"{len(content)} bytes",
            "permission": "Private" # Default
        }
        self.cloud_storage[self.bucket_name].append(file_metadata)
        print(f"✨ File '{file_name}' is now live on the cloud.")

    def set_public_access(self, file_name):
        """Configures Access Permissions (ACLs)."""
        print(f"🔐 Modifying Permissions for '{file_name}'...")
        for file in self.cloud_storage[self.bucket_name]:
            if file['name'] == file_name:
                file['permission'] = "Public-Read (Everyone)"
                print(f"🔓 Access Updated: '{file_name}' is now PUBLIC.")
                return
        print("❌ Error: File not found.")

    def list_bucket_contents(self):
        print(f"\n--- 🌐 S3 BUCKET INVENTORY: {self.bucket_name} ---")
        for file in self.cloud_storage[self.bucket_name]:
            print(f"📄 {file['name']} | Size: {file['size']} | ACL: {file['permission']}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Initialize S3 Manager
    s3 = S3CloudManager("aditya-internship-assets-2026")

    # 2. Create the Bucket
    s3.create_bucket("ap-south-1") # Mumbai Region

    # 3. Upload Example Files (Deliverable)
    s3.upload_file("resume.pdf", "[Binary Data Content]")
    s3.upload_file("profile_picture.png", "[Image Data Content]")
    s3.upload_file("project_config.json", "{ 'version': '1
  
