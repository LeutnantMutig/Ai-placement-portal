#!/usr/bin/env python
"""
Script to reset a user's password.
Since passwords are hashed, you cannot retrieve them, but you can reset them.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_project.settings')
django.setup()

from accounts.models import CustomUser

def reset_password():
    """Reset a user's password."""
    print("=" * 80)
    print("PASSWORD RESET TOOL")
    print("=" * 80)
    print("\n[!] Note: You cannot retrieve existing passwords.")
    print("   This tool will set a new password for the user.\n")
    
    username = input("Enter username to reset password: ").strip()
    
    try:
        user = CustomUser.objects.get(username=username)
        print(f"\nUser found: {user.username} ({user.email}) - Role: {user.role}")
        
        confirm = input("\nDo you want to reset password for this user? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            new_password = input("Enter new password: ").strip()
            confirm_password = input("Confirm new password: ").strip()
            
            if new_password != confirm_password:
                print("[ERROR] Passwords do not match!")
                return
            
            if len(new_password) < 8:
                print("[!] Warning: Password is less than 8 characters. Continue anyway? (yes/no): ", end="")
                if input().strip().lower() != 'yes':
                    return
            
            user.set_password(new_password)
            user.save()
            print(f"[OK] Password reset successfully for user: {user.username}")
        else:
            print("Password reset cancelled.")
    
    except CustomUser.DoesNotExist:
        print(f"[ERROR] User '{username}' not found!")

def list_users_for_reset():
    """List all users so you can choose which one to reset."""
    print("\nAll Users:")
    print("-" * 80)
    users = CustomUser.objects.all().order_by('id')
    for user in users:
        print(f"ID: {user.id} | Username: {user.username} | Email: {user.email} | Role: {user.role}")
    print("-" * 80)

if __name__ == "__main__":
    print("\nOptions:")
    print("1. Reset password by username")
    print("2. List all users first")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        reset_password()
    elif choice == "2":
        list_users_for_reset()
        print()
        reset_password()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice!")

