from admin_privileges import Admin

admin = Admin('Artyom', 'lipovoy', 200)
admin.describe_user()
admin.privileges.show_privileges()
admin.increment_login_attempts(10)
admin.describe_user()
admin.increment_login_attempts(10)
admin.describe_user()
