# Generated by Django 5.0.6 on 2024-07-07 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnhChiTietSanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'anh_chi_tiet_san_pham',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChiTietDatHang',
            fields=[
                
                ('id_dat_hang', models.ForeignKey(db_column='ID_dat_hang', on_delete=django.db.models.deletion.DO_NOTHING, to='home.dathang')),
                ('id_san_pham', models.ForeignKey(db_column='ID_san_pham', on_delete=django.db.models.deletion.DO_NOTHING, to='home.sanpham')),
                ('so_luong', models.IntegerField(blank=True, null=True)),
                ('ghi_chu', models.TextField(blank=True, null=True)),
                ('id_nguoi_dung', models.ForeignKey(db_column='ID_nguoi_dung', on_delete=django.db.models.deletion.DO_NOTHING, to='home.nguoidung')),
            ],
            options={
                'db_table': 'chi_tiet_dat_hang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatHang',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ghi_chu', models.TextField(blank=True, null=True)),
                ('ma_giam_gia', models.CharField(blank=True, max_length=50, null=True)),
                ('trang_thai_dat_hang', models.CharField(blank=True, max_length=255, null=True)),
                ('ngay_them', models.DateTimeField()),
                ('dia_chi', models.TextField(blank=True, null=True)),
                ('sdt', models.CharField(blank=True, max_length=255, null=True)),
                ('id_nguoi_dung', models.ForeignKey(db_column='ID_nguoi_dung', on_delete=django.db.models.deletion.DO_NOTHING, to='home.nguoidung')),
            ],
            options={
                'db_table': 'dat_hang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LoaiSanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_loai_san_pham', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'loai_san_pham',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ho_dem', models.CharField(blank=True, max_length=255, null=True)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('ho_va_ten', models.CharField(blank=True, max_length=255, null=True)),
                ('chi_tieu', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ngay_sinh', models.DateField(blank=True, null=True)),
                ('so_dien_thoai', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('mat_khau', models.CharField(blank=True, max_length=255, null=True)),
                ('dia_chi', models.TextField(blank=True, null=True)),
                ('ngay_them', models.DateTimeField()),
                ('ngay_cap_nhat', models.DateTimeField()),
                ('vai_tro', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'nguoi_dung',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ten_san_pham', models.CharField(blank=True, max_length=255, null=True)),
                ('gia_san_pham', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mo_ta_san_pham', models.TextField(blank=True, null=True)),
                ('ma_giam_gia', models.CharField(blank=True, max_length=50, null=True)),
                ('so_luong_san_pham', models.CharField(blank=True, max_length=11, null=True)),
                ('hinh_anh_san_pham', models.CharField(blank=True, max_length=255, null=True)),
                ('ngay_them', models.DateTimeField()),
                ('ngay_cap_nhat', models.DateTimeField()),
                ('id_loai_san_pham', models.ForeignKey(db_column='ID_loai_san_pham', on_delete=django.db.models.deletion.DO_NOTHING, to='home.loaisanpham')),
            ],
            options={
                'db_table': 'san_pham',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrangThaiNguoiDung',
            fields=[
                ('id_nguoi_dung', models.OneToOneField(db_column='ID_nguoi_dung', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='home.nguoidung')),
                ('trang_thai', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'trang_thai_nguoi_dung',
                'managed': False,
            },
        ),
    ]
