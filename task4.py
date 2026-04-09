# =================================================================
# PROJECT: Cloud Security Implementation Framework
# DESCRIPTION: Automating IAM Policies, Secure Storage, and Encryption.
# DELIVERABLE: Security Configuration Script and Implementation Report.
# =================================================================

import hashlib

class CloudSecurityManager:
    def __init__(self):
        self.iam_policies = {}
        self.secure_vault = {}
        print("🛡️ Initializing Cloud Security Layers...")

    def configure_iam_policy(self, role, user, permissions):
        """
        IAM (Identity and Access Management) Implementation.
        Defines who can access what resource.
        """
        policy = {
            "User": user,
            "Role": role,
            "Permissions": permissions,
            "Effect": "Allow"
        }
        self.iam_policies[user] = policy
        print(f"👤 IAM Policy Configured: User '{user}' assigned '{role}' role.")

    def encrypt_data(self, raw_data):
        """Simulates Server-Side Encryption (SSE-KMS)."""
        # Using SHA-256 to simulate AES-style encryption
        encrypted_blob = hashlib.sha256(raw_data.encode()).hexdigest()
        return f"ENC_{encrypted_blob[:16]}"

    def secure_store_upload(self, user, file_name, data):
        """
        Secure Storage Logic: Check IAM before allowing encrypted upload.
        """
        # Check if user exists in IAM
        if user not in self.iam_policies:
            print(f"🚫 ACCESS DENIED: User '{user}' not recognized by IAM.")
            return

        # Check for 'Write' permission
        if "Write" not in self.iam_policies[user]["Permissions"]:
            print(f"🚫 PERMISSION DENIED: User '{user}' does not have Write access.")
            return

        # Encrypt and Upload
        encrypted_content = self.encrypt_data(data)
        self.secure_vault[file_name] = {
            "content": encrypted_content,
            "owner": user,
            "status": "Encrypted-at-Rest"
        }
        print(f"🔒 Secure Upload: '{file_name}' encrypted and stored by {user}.")

    def generate_security_report(self):
        print("\n" + "="*50)
        print("📋 CLOUD SECURITY IMPLEMENTATION REPORT")
        print("="*50)
        print("1. IAM POLICIES:")
        for user, p in self.iam_policies.items():
            print(f"   - {user}: {p['Role']} ({p['Permissions']})")
        
        print("\n2. SECURE STORAGE (ENCRYPTED ASSETS):")
        for file, meta in self.secure_vault.items():
            print(f"   - {file}: {meta['status']} (Hash: {meta['content']})")
        print("="*50)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    security = CloudSecurityManager()

    # 1. Setup IAM Policies (Deliverable)
    security.configure_iam_policy("Admin", "Aditya_Tripathi", ["Read", "Write", "Delete"])
    security.configure_iam_policy("Viewer", "Intern_Guest", ["Read"])

    # 2.
