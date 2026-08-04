import grp

def get_admin_users():
    admin_groups = ["sudo", "wheel"]
    admin_users = set()

    for group in admin_groups:
        try:
            group_info = grp.getgrnam(group)
            admin_users.update(group_info.gr_mem)
        except KeyError:
            continue

    return list(admin_users)