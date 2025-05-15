# product_service/migrations/0001_initial.py
# หรือที่ใดก็ตามที่คุณเก็บ user model

# from django.db import migrations

# def create_superuser(apps, schema_editor):
#     from django.contrib.auth import get_user_model
#     User = get_user_model()

#     if not User.objects.filter(username='admin').exists():
#         User.objects.create_superuser(
#             username='admin',
#             email='admin@example.com',
#             password='admin1234'
#         )
#         print('✅ Created superuser "admin"')
#     else:
#         print('ℹ️ Superuser "admin" already exists')

# class Migration(migrations.Migration):

#     initial = True

#     dependencies = []

#     operations = [
#         migrations.RunPython(create_superuser),
#     ]


from django.db import migrations, connection

def create_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    if 'auth_user' in connection.introspection.table_names():
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin1234'
            )
            print('✅ Created superuser "admin"')
        else:
            print('ℹ️ Superuser "admin" already exists')
    else:
        print('⚠️ Skipped creating superuser: auth_user table does not exist')

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        # อย่าเรียกสร้าง superuser ใน initial migration โดยตรง
        # migrations.RunPython(create_superuser),
    ]