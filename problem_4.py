class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True

    pending_groups = group.get_groups()
    has_user = False
    while len(pending_groups) > 0 and not has_user:
        next_group = pending_groups.pop(0)
        if user in next_group.get_users():
            has_user = True
            continue
        pending_groups.extend(next_group.get_groups())

    return has_user


print(is_user_in_group(sub_child_user, parent))
# True
print(is_user_in_group(sub_child_user, child))
# True
print(is_user_in_group(sub_child_user, sub_child))
# True
print(is_user_in_group("random_user", parent))
# False
