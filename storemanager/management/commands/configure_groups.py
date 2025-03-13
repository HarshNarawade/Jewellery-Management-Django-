from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Set up Customer, Store Manager, and Factory Manager groups with specific permissions."

    def handle(self, *args, **kwargs):
        # Define permissions for each group
        group_permissions = {
            "Customer": ["view_order"],
            "Factory Manager": ["view_order", "change_order"],
            "Store Manager": [
                "add_order",
                "view_order",
                "change_order",
                "delete_order",
                "add_user",
                "view_user",
                "change_user",
                "delete_user",
            ],
        }

        # Loop through groups and apply permissions
        for group_name, permissions in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)

            # Assign each permission to the group
            for perm_code in permissions:
                try:
                    permission = Permission.objects.get(codename=perm_code)
                    group.permissions.add(permission)
                    self.stdout.write(f"✅ '{perm_code}' added to '{group_name}' group")
                except Permission.DoesNotExist:
                    self.stdout.write(f"⚠️ Permission '{perm_code}' not found!")

            if created:
                self.stdout.write(f"🔧 Group '{group_name}' created!")
            else:
                self.stdout.write(f"🔄 Group '{group_name}' updated!")

        self.stdout.write("🎉 All groups configured successfully!")
